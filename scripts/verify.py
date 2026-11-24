#!/usr/bin/env python3
"""Repository consistency, animation integrity, release sync, and headless Chrome render/behavior verifier.

Run static & animation checks:
  python3 scripts/verify.py

Run full headless Chrome render (1440px / 390px x light / dark) + DOM/ARIA/animation checks:
  python3 scripts/verify.py --render --out /tmp/arknights-verify
"""
from __future__ import annotations

import argparse
import http.server
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import threading

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSS_FILES = [
    "resources/prts-design.css",
    "resources/prts-tokens.css",
    "resources/prts-addons.css",
    "resources/endfield-standalone.css",
    "resources/endfield-theme.css",
]
STATE_CLASSES = {
    "corner-brackets", "hazard", "is-open", "is-selected", "is-invalid",
    "is-done", "is-current", "is-expanded", "is-active", "is-playing", "num",
}
DOC_CLASS_WHITELIST = {"ak-rt-"}


def load_defined_classes() -> set[str]:
    css = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in CSS_FILES)
    return set(re.findall(r"\.([a-zA-Z_-][a-zA-Z0-9_-]*)", css))


def check_html_files(defined: set[str]) -> list[str]:
    errors: list[str] = []
    for hp in sorted((ROOT / "examples").glob("*.html")):
        txt = hp.read_text(encoding="utf-8")
        local_css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", txt, re.S))
        scoped = defined | set(re.findall(r"\.([a-zA-Z_-][a-zA-Z0-9_-]*)", local_css))
        used = {c for m in re.findall(r'class="([^"]+)"', txt) for c in m.split()}
        missing = sorted(
            c for c in used
            if (c.startswith(("ak-", "ef-")) or c in STATE_CLASSES) and c not in scoped
        )
        inline_grids = len(re.findall(r"grid-template-columns\s*:", txt))
        fake_hex = [t for t in ("0x7F3A", "0xDEAD") if t in txt]
        if missing:
            errors.append(f"{hp.name}: missing classes {missing}")
        if inline_grids:
            errors.append(f"{hp.name}: found {inline_grids} inline grid-template-columns")
        if fake_hex:
            errors.append(f"{hp.name}: leaked fake hex tokens {fake_hex}")
        print(f"[HTML] {hp.name}: {len(used)} classes, missing={missing}, inline_grid={inline_grids}")
    return errors


def check_markdown_files(defined: set[str]) -> list[str]:
    errors: list[str] = []
    mds = [ROOT / "SKILL.md", ROOT / "README.md", *(ROOT / "references").rglob("*.md")]
    for mp in sorted(mds):
        txt = mp.read_text(encoding="utf-8")
        classes = (
            {c for m in re.findall(r'class="([^"]+)"', txt) for c in m.split()}
            | set(re.findall(r"\.((?:ak|ef)-[a-zA-Z0-9_-]+)", txt))
        )
        missing = sorted(
            c for c in classes
            if c.startswith(("ak-", "ef-")) and c not in defined and c not in DOC_CLASS_WHITELIST
        )
        broken_links: list[str] = []
        for target in re.findall(r"\]\(((?:\.\.?/)[^)#]+)", txt):
            resolved = (mp.parent / target).resolve()
            if not resolved.exists():
                broken_links.append(target)
        if missing:
            errors.append(f"{mp.relative_to(ROOT)}: missing documented classes {missing}")
        if broken_links:
            errors.append(f"{mp.relative_to(ROOT)}: broken relative links {broken_links}")
        print(f"[DOCS] {mp.relative_to(ROOT)}: classes={len(classes)}, missing={missing}, broken_links={broken_links}")
    return errors


def check_css_animations() -> list[str]:
    errors: list[str] = []
    for rel, disallow_unused in (
        ("resources/prts-design.css", False),
        ("resources/prts-addons.css", True),
        ("resources/endfield-standalone.css", True),
    ):
        txt = (ROOT / rel).read_text(encoding="utf-8")
        kfs = set(re.findall(r"@keyframes\s+([a-zA-Z0-9_-]+)", txt))
        used = set(re.findall(r"animation(?:-name)?\s*:\s*([a-zA-Z0-9_-]+)", txt))
        for m in re.findall(r"animation\s*:\s*([^;}{]+)", txt):
            for kf in kfs:
                if kf in m:
                    used.add(kf)
        missing = sorted(used - kfs - {"none"})
        unused = sorted(kfs - used)
        has_prm = "prefers-reduced-motion" in txt
        if missing:
            errors.append(f"{rel}: missing keyframes {missing}")
        if disallow_unused and unused:
            errors.append(f"{rel}: unused keyframes {unused}")
        if not has_prm:
            errors.append(f"{rel}: missing @media (prefers-reduced-motion: reduce)")
        print(f"[ANIM] {rel}: keyframes={len(kfs)}, missing={missing}, unused={unused}, reduced_motion={has_prm}")
    return errors


def check_release_bundle() -> list[str]:
    """Ensure release/arknights-design/ is strictly synced with canonical Skill assets."""
    errors: list[str] = []
    bundle = ROOT / "release" / "arknights-design"
    if not bundle.is_dir():
        return ["release/arknights-design directory is missing (run scripts/package-release.py)"]

    expected: dict[str, pathlib.Path] = {}
    for rel in ("SKILL.md", "LICENSE", "NOTICE.md"):
        expected[rel] = ROOT / rel
    for d in ("references", "resources", "examples"):
        for f in sorted((ROOT / d).rglob("*")):
            if f.is_file():
                expected[str(f.relative_to(ROOT))] = f

    actual = {str(p.relative_to(bundle)): p for p in sorted(bundle.rglob("*")) if p.is_file()}
    stale = sorted(set(actual) - set(expected))
    if stale:
        errors.append(f"release/arknights-design has stale files: {stale}")
    for rel, src in sorted(expected.items()):
        dst = bundle / rel
        if not dst.exists():
            errors.append(f"release/arknights-design/{rel}: missing")
        elif src.read_bytes() != dst.read_bytes():
            errors.append(f"release/arknights-design/{rel}: out of sync (run scripts/package-release.py)")
    print(f"[RELEASE] Checked {len(expected)} files in release/arknights-design (stale={len(stale)})")
    return errors


def run_chrome_render_and_behavior(out_dir: pathlib.Path) -> list[str]:
    errors: list[str] = []
    out_dir.mkdir(parents=True, exist_ok=True)
    pages = [
        ("prts-bp", "examples/prts-boilerplate.html", 2250, 3550),
        ("prts-comp", "examples/prts-components.html", 3950, 6150),
        ("ef-bp", "examples/endfield-boilerplate.html", 1700, 2500),
        ("ef-comp", "examples/endfield-components.html", 4600, 7400),
    ]
    for tag, src, dh, mh in pages:
        for theme in ("light", "dark"):
            txt = (ROOT / src).read_text(encoding="utf-8")
            txt = txt.replace('href="../resources/', f'href="file://{ROOT}/resources/')
            txt = txt.replace('href="./', f'href="file://{ROOT}/examples/')
            txt = re.sub(r'(<html[^>]*data-theme=")[^"]*(")', rf"\g<1>{theme}\g<2>", txt, count=1)
            txt = txt.replace("localStorage.getItem", "(function(){return null;})")
            tmp = out_dir / f"{tag}-{theme}.html"
            tmp.write_text(txt, encoding="utf-8")
            for w, h in [(1440, dh), (390, mh)]:
                png = out_dir / f"{tag}-{theme}-{w}x{h}.png"
                subprocess.run(
                    [
                        "google-chrome", "--headless=new", "--no-sandbox", "--hide-scrollbars",
                        f"--window-size={w},{h}", "--virtual-time-budget=4000",
                        f"--screenshot={png}", f"file://{tmp}",
                    ],
                    check=True,
                    capture_output=True,
                )
    print(f"[RENDER] Rendered {len(pages) * 4} screenshots into {out_dir}")

    prts_bp_probe = """
<script>
window.addEventListener('load', () => {
  const anims = {
    heroScan: getComputedStyle(document.querySelector('.ak-hero--editorial__title')).animationName,
    heroWipe: getComputedStyle(document.querySelector('.ak-hero--editorial__rule')).animationName,
    waveBar: getComputedStyle(document.querySelector('.ak-wave-btn.is-playing .ak-wave-bars i')).animationName,
  };
  document.querySelectorAll('.ak-thumb-card')[2].click();
  const focalSwitched = document.getElementById('brief-cn').textContent === '陈'
    && document.getElementById('ak-scrub-thumb').style.getPropertyValue('--_thumb-x') === '50%';
  document.querySelectorAll('.ak-filter-strip__btn')[1].click();
  const feedFiltered = [...document.querySelectorAll('#ak-feed-list .ak-folio-item')]
    .every(el => el.dataset.cat === 'notice' ? !el.hidden : el.hidden);
  document.querySelectorAll('#ak-world-list .ak-folio-item')[2].click();
  const worldSwitched = document.getElementById('ak-world-note').textContent.includes('NOMADIC CITY');
  const audioBtn = document.getElementById('ak-audio-toggle');
  audioBtn.click();
  const audioToggled = audioBtn.getAttribute('aria-pressed') === 'false' && !audioBtn.classList.contains('is-playing');
  const railNavBtn = document.querySelector('.ak-rail-nav__item[data-sec="02"]');
  railNavBtn.click();
  const railSynced = document.getElementById('rail-num').textContent === '02'
    && document.querySelector('.ak-topbar__link[data-sec="02"]').classList.contains('is-active');
  const secLabelsMatch = [...document.querySelectorAll('.ak-topbar__link[data-sec]')].every(a => {
    const r = document.querySelector(`.ak-rail-nav__item[data-sec="${a.dataset.sec}"]`);
    return r && r.dataset.secEn === a.dataset.secEn;
  });
  const heroRect = document.querySelector('.ak-hero--editorial').getBoundingClientRect();
  const statRect = document.querySelector('.ak-stat-row--open').getBoundingClientRect();
  const statsClearOfWatermark = statRect.top >= heroRect.bottom - 1;
  const noOverflow = document.documentElement.scrollWidth <= document.documentElement.clientWidth;
  document.body.setAttribute('data-verify', JSON.stringify({
    anims, focalSwitched, feedFiltered, worldSwitched, audioToggled, railSynced, secLabelsMatch, statsClearOfWatermark, noOverflow
  }));
});
</script>
"""
    ef_probe = """
<script>
window.addEventListener('load', () => {
  const anims = {
    sectionBlock: getComputedStyle(document.querySelector('.ef-section-title__block')).animationName,
    sectionArrow: getComputedStyle(document.querySelector('.ef-section-title__block > span')).animationName,
    sectionTitle: getComputedStyle(document.querySelector('.ef-section-title__en')).animationName,
    banner: getComputedStyle(document.querySelector('.ef-completion-banner')).animationName,
    sparkline: getComputedStyle(document.querySelector('.ef-sparkline')).animationName,
    tickRing: getComputedStyle(document.querySelector('.ef-tick-ring--spin .ef-tick-ring__svg')).animationName,
    recDot: getComputedStyle(document.querySelector('.ef-rec__dot')).animationName,
    indetFill: getComputedStyle(document.querySelector('.ef-progress--indeterminate .ef-progress__fill')).animationName,
    marquee: getComputedStyle(document.querySelector('.ef-marquee__track')).animationName,
    scrollHint: getComputedStyle(document.querySelector('.ef-scroll-hint__line'), '::after').animationName,
    bracketCorner: getComputedStyle(document.querySelector('.ef-viewfinder__corners')).animationName,
    menuBar: (() => {
      document.getElementById('ef-dd-strong-btn').click();
      return getComputedStyle(document.querySelector('#ef-dd-strong .ef-menu'), '::before').animationName;
    })(),
  };
  document.body.click();
  const closedByOutsideClick = !document.getElementById('ef-dd-strong').classList.contains('is-open');
  const tabsOk = [...document.querySelectorAll('[data-ef-tabs]')].every(list => {
    const tabs = [...list.querySelectorAll('[role="tab"]')];
    tabs[0].dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
    const r = tabs[1].getAttribute('aria-selected') === 'true' && tabs[1].tabIndex === 0;
    tabs[1].dispatchEvent(new KeyboardEvent('keydown', { key: 'Home', bubbles: true }));
    return r && tabs[0].getAttribute('aria-selected') === 'true';
  });
  const cbi = document.getElementById('ef-combo-in');
  cbi.value = 'E03';
  cbi.dispatchEvent(new Event('input', { bubbles: true }));
  cbi.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowDown', bubbles: true }));
  const focusedOpt = document.activeElement;
  const comboArrowOk = document.getElementById('ef-combobox').classList.contains('is-open')
    && focusedOpt && focusedOpt.getAttribute('role') === 'option' && focusedOpt.textContent.includes('E03');
  document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
  const comboEscOk = !document.getElementById('ef-combobox').classList.contains('is-open') && document.activeElement === cbi;
  cbi.value = '';
  cbi.dispatchEvent(new Event('input', { bubbles: true }));
  moveCar(1);
  const carouselOk = document.getElementById('ef-car-count').textContent === '2 / 3';
  const noOverflow = document.documentElement.scrollWidth <= document.documentElement.clientWidth;
  document.body.setAttribute('data-verify', JSON.stringify({ anims, closedByOutsideClick, tabsOk, comboArrowOk, comboEscOk, carouselOk, noOverflow }));
});
</script>
"""
    prts_probe = """
<script>
window.addEventListener('load', () => {
  const anims = {
    spinnerRipple: getComputedStyle(document.querySelector('.ak-spinner'), '::after').animationName,
    loaderBar: getComputedStyle(document.querySelector('.ak-loader > i')).animationName,
    skeleton: getComputedStyle(document.querySelector('.ak-skeleton')).animationName,
    indeterminate: getComputedStyle(document.querySelector('.ak-progress--indeterminate'), '::before').animationName,
    voiceWave: getComputedStyle(document.querySelector('.is-playing ~ * .ak-voice__wave > i')).animationName,
    editorialRuleScan: getComputedStyle(document.querySelector('#editorial .ak-anim-scan')).animationName,
  };
  document.getElementById('demo-dd-btn').click();
  const ddOpened = document.getElementById('demo-dd').classList.contains('is-open');
  document.body.click();
  const ddClosed = !document.getElementById('demo-dd').classList.contains('is-open');
  const drawerHidden = getComputedStyle(document.getElementById('ak-right-drawer')).visibility === 'hidden';
  const metaEl = document.querySelector('#editorial .ak-folio-item__meta');
  const metaTitleEl = metaEl && metaEl.nextElementSibling;
  const folioMetaStacked = !!(metaEl && metaTitleEl && metaEl.getBoundingClientRect().bottom <= metaTitleEl.getBoundingClientRect().top + 1);
  const waveBtn = document.querySelector('#editorial .ak-wave-btn');
  const isLight = document.documentElement.dataset.theme === 'light';
  const wavePlayColor = getComputedStyle(waveBtn).color;
  waveBtn.style.transition = 'none';
  waveBtn.click();
  const waveIdleColor = getComputedStyle(waveBtn).color;
  const waveAriaSynced = waveBtn.getAttribute('aria-pressed') === 'false';
  waveBtn.style.transition = '';
  const waveContrastOk = waveAriaSynced && (!isLight || (wavePlayColor === 'rgb(0, 114, 168)' && waveIdleColor === 'rgb(69, 70, 71)'));
  const noOverflow = document.documentElement.scrollWidth <= document.documentElement.clientWidth;
  document.body.setAttribute('data-verify', JSON.stringify({ anims, ddOpened, ddClosed, drawerHidden, folioMetaStacked, waveContrastOk, noOverflow }));
});
</script>
"""
    for src_name, html_file, probe in [
        ("prts-boilerplate", out_dir / "prts-bp-dark.html", prts_bp_probe),
        ("prts-components-dark", out_dir / "prts-comp-dark.html", prts_probe),
        ("prts-components-light", out_dir / "prts-comp-light.html", prts_probe),
        ("endfield-components", out_dir / "ef-comp-light.html", ef_probe),
    ]:
        probe_file = out_dir / f"probe-{src_name}.html"
        probe_file.write_text(html_file.read_text(encoding="utf-8").replace("</body>", probe + "</body>"), encoding="utf-8")
        r = subprocess.run(
            ["google-chrome", "--headless=new", "--no-sandbox", "--window-size=1440,900", "--virtual-time-budget=2500", "--dump-dom", f"file://{probe_file}"],
            check=True, capture_output=True, text=True,
        )
        m = re.search(r'data-verify="([^"]+)"', r.stdout)
        if not m:
            errors.append(f"{src_name}: DOM verification probe did not execute")
            continue
        data = json.loads(m.group(1).replace("&quot;", '"'))
        print(f"[PROBE] {src_name}: {json.dumps(data, ensure_ascii=False)}")
        for k, v in data.get("anims", {}).items():
            if not v or v == "none":
                errors.append(f"{src_name}: animation '{k}' resolved to '{v}'")
        for k, v in data.items():
            if k != "anims" and not v:
                errors.append(f"{src_name}: assertion '{k}' failed")

    errors.extend(check_mobile_viewports())
    return errors


def check_mobile_viewports() -> list[str]:
    """Verify exact 375px and 390px layout width via same-origin iframes (avoids headless window min-width clamp)."""
    errors: list[str] = []
    pages = sorted((ROOT / "examples").glob("*.html"))
    rels = ["/" + str(p.relative_to(ROOT)).replace("\\", "/") for p in pages]
    names = [str(p.relative_to(ROOT)) for p in pages]

    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=str(ROOT), **kw)

        def log_message(self, *a):
            pass

        def do_GET(self):
            m = re.match(r"^/__mobile_(\d+)$", self.path)
            if m:
                w = int(m.group(1))
                frames = "".join(
                    f'<iframe id="f{i}" src="{rel}" style="width:{w}px;height:900px;border:0;display:block"></iframe>'
                    for i, rel in enumerate(rels)
                )
                body = (
                    f"<!doctype html><html><body>{frames}<script>"
                    "window.addEventListener('load', () => {"
                    f"const names = {json.dumps(names)};"
                    "const res = names.map((name, i) => {"
                    "const d = document.getElementById('f' + i).contentDocument;"
                    "const de = d.documentElement;"
                    "const ro = d.querySelector('.ef-viewfinder__ro');"
                    "const cor = d.querySelector('.ef-viewfinder__corners');"
                    "const tbBrand = d.querySelector('.ak-topbar__brand');"
                    "const tbTools = d.querySelector('.ak-topbar__tools');"
                    "const topbarClear = tbBrand && tbTools ? (tbBrand.getBoundingClientRect().right <= tbTools.getBoundingClientRect().left + 1) : true;"
                    "return { name, cw: de.clientWidth, sw: de.scrollWidth, ok: de.scrollWidth <= de.clientWidth, topbarClear,"
                    " vfVisible: ro && cor ? (getComputedStyle(ro).display !== 'none' && getComputedStyle(cor).display !== 'none') : true };"
                    "}); document.body.setAttribute('data-mverify', JSON.stringify(res)); });</script></body></html>"
                ).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            return super().do_GET()

    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), QuietHandler)
    port = httpd.server_address[1]
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        for w in (375, 390):
            r = subprocess.run(
                ["google-chrome", "--headless=new", "--no-sandbox", "--window-size=1200,1200", "--virtual-time-budget=3000", "--dump-dom", f"http://127.0.0.1:{port}/__mobile_{w}"],
                check=True, capture_output=True, text=True,
            )
            m = re.search(r'data-mverify="([^"]+)"', r.stdout)
            if not m:
                errors.append(f"mobile {w}px: iframe probe did not execute")
                continue
            rows = json.loads(m.group(1).replace("&quot;", '"'))
            print(f"[MOBILE {w}px] {json.dumps(rows, ensure_ascii=False)}")
            for row in rows:
                if not row["ok"]:
                    errors.append(f"{row['name']} @ {w}px (cw={row['cw']}): scrollWidth {row['sw']} > clientWidth {row['cw']}")
                if not row["topbarClear"]:
                    errors.append(f"{row['name']} @ {w}px: ak-topbar brand overlaps right tools")
                if not row["vfVisible"]:
                    errors.append(f"{row['name']} @ {w}px: viewfinder corners/readout hidden")
    finally:
        httpd.shutdown()
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--render", action="store_true", help="Run headless Chrome screenshots and DOM/animation probes")
    parser.add_argument("--out", default=str(pathlib.Path(tempfile.gettempdir()) / "arknights-design-verify"))
    args = parser.parse_args()

    defined = load_defined_classes()
    errors = []
    errors.extend(check_html_files(defined))
    errors.extend(check_markdown_files(defined))
    errors.extend(check_css_animations())
    errors.extend(check_release_bundle())
    if args.render:
        errors.extend(run_chrome_render_and_behavior(pathlib.Path(args.out)))

    if errors:
        print("\nFAILED:")
        for e in errors:
            print("  -", e)
        return 1
    print("\nALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
