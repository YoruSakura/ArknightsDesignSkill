#!/usr/bin/env python3
"""Build clean, self-contained release bundles under release/ for all Skills in this repo.

Usage:
  python3 scripts/package-release.py [--version v1.2]
"""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import shutil
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_VERSION = "v1.2"
RELEASE_DIR = ROOT / "release"
IGNORE_PATTERNS = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", "Thumbs.db", "*.tmp")

BUNDLES: list[tuple[str, pathlib.Path, str]] = [
    ("arknights-design", ROOT, "主双体系（PRTS 本家 + Endfield UI）与六大官方活动系列预设"),
    (
        "arknights-contingency-contract",
        ROOT / "skills" / "arknights-contingency-contract",
        "高难危机合约 / 行动协议 / 卫戍规程 / 矢量突破 / DOS 独立 Skill（.cc-*）",
    ),
    (
        "arknights-integrated-strategies",
        ROOT / "skills" / "arknights-integrated-strategies",
        "集成战略五代主题（萨卡兹 / 岁界园 / 水月 / 银凇 / 黑流）独立 Skill（.is-*）",
    ),
]


def copy_bundle(name: str, src_root: pathlib.Path) -> list[pathlib.Path]:
    """Recreate release/<name>/ cleanly from canonical repository assets."""
    bundle_dir = RELEASE_DIR / name
    RELEASE_DIR.mkdir(parents=True, exist_ok=True)
    if bundle_dir.exists():
        shutil.rmtree(bundle_dir)
    bundle_dir.mkdir(parents=True, exist_ok=True)

    # Always include SKILL.md from the skill source root, plus shared LICENSE/NOTICE.md
    skill_md = src_root / "SKILL.md"
    if not skill_md.exists():
        raise FileNotFoundError(f"Missing SKILL.md in {src_root}")
    shutil.copy2(skill_md, bundle_dir / "SKILL.md")

    for shared in ("LICENSE", "NOTICE.md"):
        src = src_root / shared if (src_root / shared).exists() else ROOT / shared
        if not src.exists():
            raise FileNotFoundError(f"Missing shared metadata file: {shared}")
        shutil.copy2(src, bundle_dir / shared)

    for rel_dir in ("references", "resources", "examples"):
        src_dir = src_root / rel_dir
        if not src_dir.is_dir():
            raise NotADirectoryError(f"Missing required directory {rel_dir} in {src_root}")
        shutil.copytree(src_dir, bundle_dir / rel_dir, ignore=IGNORE_PATTERNS)

    return sorted(p for p in bundle_dir.rglob("*") if p.is_file())


def verify_bundle(name: str, files: list[pathlib.Path]) -> None:
    """Validate frontmatter, asset isolation, and zero broken relative links inside the bundle."""
    bundle_dir = RELEASE_DIR / name
    head = (bundle_dir / "SKILL.md").read_text(encoding="utf-8")
    if not re.match(rf"^---\s*\nname:\s*{re.escape(name)}\s*\ndescription:", head):
        raise ValueError(f"release/{name}/SKILL.md missing valid frontmatter (expected name: {name})")

    forbidden = {"AGENTS.md", "scripts", "verify.py", "sync-upstream.py"}
    leaked = [p.relative_to(bundle_dir) for p in files if p.name in forbidden or "scripts" in p.parts]
    if leaked:
        raise ValueError(f"Maintainer artifacts leaked into release/{name}: {leaked}")

    for md in sorted(bundle_dir.rglob("*.md")):
        txt = md.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(((?:\.\.?/)[^)#]+)", txt):
            resolved = (md.parent / target).resolve()
            if not resolved.is_relative_to(bundle_dir.resolve()) or not resolved.exists():
                raise ValueError(f"Broken or escaping link in {name}/{md.relative_to(bundle_dir)}: {target}")

    for hp in sorted((bundle_dir / "examples").glob("*.html")):
        txt = hp.read_text(encoding="utf-8")
        for target in re.findall(r'(?:href|src)="((?:\.\.?/)[^"#?]+)"', txt):
            resolved = (hp.parent / target).resolve()
            if not resolved.is_relative_to(bundle_dir.resolve()) or not resolved.exists():
                raise ValueError(f"Broken or escaping asset in {name}/{hp.relative_to(bundle_dir)}: {target}")


def build_zip(name: str, files: list[pathlib.Path]) -> pathlib.Path:
    """Create release/<name>.zip preserving the <name>/ top-level folder."""
    bundle_dir = RELEASE_DIR / name
    archive_path = RELEASE_DIR / f"{name}.zip"
    if archive_path.exists():
        archive_path.unlink()
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in files:
            arcname = pathlib.Path(name) / path.relative_to(bundle_dir)
            zf.write(path, arcname.as_posix())
    return archive_path


def write_release_readme(summaries: list[dict[str, object]], version: str) -> None:
    is_pre = any(k in version.lower() for k in ("beta", "alpha", "rc"))
    stage_label = "测试版（Pre-release · 待审查）" if is_pre else "正式版"
    rows = "\n".join(
        f"| `{s['name']}` | {s['desc']} | {s['count']} | {s['zip_kb']:.1f} KB | `{s['sha256']}` |"
        for s in summaries
    )
    content = f"""# Release Bundles — ArknightsDesignSkill Ecosystem ({version})

本目录由 [`scripts/package-release.py`](../scripts/package-release.py) 生成，包含可直接复制或解压接入下游前端项目的 **3 个{stage_label}纯运行时 Skill 独立包**（版本 `{version}`），已剔除维护文档（`AGENTS.md`）与同步/校验脚本（`scripts/`）。

## 包含产物

| Skill 包名 | 定位与覆盖内容 | 文件数 | ZIP 体积 | ZIP SHA-256 |
| :--- | :--- | :-: | :-: | :--- |
{rows}

## 快速安装到项目

```bash
# 按需任选单个或多个 Skill 拷贝到目标项目的 .agents/skills/（Antigravity / 通用）
mkdir -p /path/to/your-project/.agents/skills
cp -r release/arknights-design /path/to/your-project/.agents/skills/
cp -r release/arknights-contingency-contract /path/to/your-project/.agents/skills/
cp -r release/arknights-integrated-strategies /path/to/your-project/.agents/skills/

# Claude Code 项目级目录（.claude/skills/）或全局目录（~/.agents/skills/）同理：
mkdir -p ~/.agents/skills ~/.claude/skills
cp -r release/arknights-* ~/.agents/skills/
```
"""
    (RELEASE_DIR / "README.md").write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default=DEFAULT_VERSION, help="Release version label recorded in release/README.md")
    args = parser.parse_args()

    summaries: list[dict[str, object]] = []
    for name, src_root, desc in BUNDLES:
        files = copy_bundle(name, src_root)
        verify_bundle(name, files)
        archive_path = build_zip(name, files)
        zip_bytes = archive_path.read_bytes()
        sha256 = hashlib.sha256(zip_bytes).hexdigest()
        summaries.append({
            "name": name,
            "desc": desc,
            "count": len(files),
            "zip_kb": len(zip_bytes) / 1024,
            "sha256": sha256,
        })
        print(f"[RELEASE {args.version}] {name}: {len(files)} files -> release/{name}/ | {archive_path.name} ({len(zip_bytes)} bytes)")

    write_release_readme(summaries, args.version)
    return 0


if __name__ == "__main__":
    sys.exit(main())
