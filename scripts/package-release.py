#!/usr/bin/env python3
"""Build a clean, self-contained, release-ready Skill bundle under release/arknights-design/.

Usage:
  python3 scripts/package-release.py [--version v1.0]
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
BUNDLE_NAME = "arknights-design"
BUNDLE_DIR = RELEASE_DIR / BUNDLE_NAME
ARCHIVE_PATH = RELEASE_DIR / f"{BUNDLE_NAME}.zip"

INCLUDE_FILES = [
    "SKILL.md",
    "LICENSE",
    "NOTICE.md",
]
INCLUDE_DIRS = [
    "references",
    "resources",
    "examples",
]
IGNORE_PATTERNS = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", "Thumbs.db", "*.tmp")


def discover_suite_skills() -> list[pathlib.Path]:
    """Discover real standalone sub-skills under suites/<game>/<skill-name>/ (ignoring _template and hidden dirs)."""
    suites_root = ROOT / "suites"
    if not suites_root.is_dir():
        return []
    found: list[pathlib.Path] = []
    for game_dir in sorted(suites_root.iterdir()):
        if not game_dir.is_dir() or game_dir.name.startswith((".", "_")):
            continue
        for skill_dir in sorted(game_dir.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name.startswith((".", "_")):
                continue
            if (skill_dir / "SKILL.md").is_file():
                found.append(skill_dir)
    return found


def copy_bundle(src_root: pathlib.Path = ROOT, bundle_dir: pathlib.Path = BUNDLE_DIR) -> list[pathlib.Path]:
    """Recreate a clean release bundle directory from canonical source assets."""
    RELEASE_DIR.mkdir(parents=True, exist_ok=True)
    if bundle_dir.exists():
        shutil.rmtree(bundle_dir)
    bundle_dir.mkdir(parents=True, exist_ok=True)

    for rel in INCLUDE_FILES:
        src = src_root / rel
        if not src.exists() and src_root != ROOT and rel in ("LICENSE", "NOTICE.md"):
            src = ROOT / rel
        if not src.exists():
            raise FileNotFoundError(f"Missing required file for {bundle_dir.name}: {rel}")
        shutil.copy2(src, bundle_dir / rel)

    for rel_dir in INCLUDE_DIRS:
        src_dir = src_root / rel_dir
        if not src_dir.is_dir():
            raise NotADirectoryError(f"Missing required directory for {bundle_dir.name}: {rel_dir}")
        shutil.copytree(src_dir, bundle_dir / rel_dir, ignore=IGNORE_PATTERNS)

    return sorted(p for p in bundle_dir.rglob("*") if p.is_file())


def verify_bundle(files: list[pathlib.Path], bundle_name: str = BUNDLE_NAME, bundle_dir: pathlib.Path = BUNDLE_DIR) -> None:
    """Validate frontmatter, asset isolation, and zero broken relative links inside the bundle."""
    skill_md = bundle_dir / "SKILL.md"
    head = skill_md.read_text(encoding="utf-8")
    if not re.match(rf"^---\s*\nname:\s*{re.escape(bundle_name)}\s*\ndescription:", head):
        raise ValueError(f"release/{bundle_name}/SKILL.md missing valid frontmatter for '{bundle_name}'")

    forbidden = {"AGENTS.md", "SUITE_SPEC.md", "scripts", "verify.py", "sync-upstream.py"}
    leaked = [p.relative_to(bundle_dir) for p in files if p.name in forbidden or "scripts" in p.parts]
    if leaked:
        raise ValueError(f"Maintainer artifacts leaked into release/{bundle_name}: {leaked}")

    for md in sorted(bundle_dir.rglob("*.md")):
        txt = md.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(((?:\.\.?/)[^)#]+)", txt):
            resolved = (md.parent / target).resolve()
            if not resolved.is_relative_to(bundle_dir.resolve()) or not resolved.exists():
                raise ValueError(f"Broken or escaping link in {bundle_name}/{md.relative_to(bundle_dir)}: {target}")

    for hp in sorted((bundle_dir / "examples").glob("*.html")):
        txt = hp.read_text(encoding="utf-8")
        for target in re.findall(r'(?:href|src)="((?:\.\.?/)[^"#?]+)"', txt):
            resolved = (hp.parent / target).resolve()
            if not resolved.is_relative_to(bundle_dir.resolve()) or not resolved.exists():
                raise ValueError(f"Broken or escaping asset in {bundle_name}/{hp.relative_to(bundle_dir)}: {target}")


def build_zip(files: list[pathlib.Path], bundle_name: str = BUNDLE_NAME, bundle_dir: pathlib.Path = BUNDLE_DIR, archive_path: pathlib.Path = ARCHIVE_PATH) -> None:
    """Create release/<bundle_name>.zip preserving the <bundle_name>/ top-level folder."""
    if archive_path.exists():
        archive_path.unlink()
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in files:
            arcname = pathlib.Path(bundle_name) / path.relative_to(bundle_dir)
            zf.write(path, arcname.as_posix())


def write_release_readme(bundles: list[tuple[str, list[pathlib.Path], pathlib.Path]], version: str) -> None:
    is_pre = any(k in version.lower() for k in ("beta", "alpha", "rc", "dev"))
    stage_label = "开发测试版（Pre-release · 待审查）" if "dev" in version.lower() else ("测试版（Pre-release · 待审查）" if is_pre else "正式版")

    if len(bundles) == 1:
        name, files, archive_path = bundles[0]
        total_kb = sum(p.stat().st_size for p in files) / 1024
        zip_bytes = archive_path.read_bytes()
        zip_kb = len(zip_bytes) / 1024
        sha256 = hashlib.sha256(zip_bytes).hexdigest()
        content = f"""# Release Bundle — `{name}` ({version})

本目录由 [`scripts/package-release.py`](../scripts/package-release.py) 生成，包含可直接复制或解压接入下游前端项目的**{stage_label}纯运行时 Skill 包**（版本 `{version}`，共 {len(files)} 个文件，未压缩 {total_kb:.1f} KB；压缩包 {zip_kb:.1f} KB），已剔除维护文档（`AGENTS.md`）与同步/校验脚本（`scripts/`）。

## 包含产物

- `{name}/`：可直接拷贝或软链接的完整 Skill 文件夹（含 `SKILL.md`、`LICENSE`、`NOTICE.md`、`references/`、`resources/`、`examples/`）
- `{name}.zip`：同内容的便携压缩包（顶层目录为 `{name}/`，`SHA-256`: `{sha256}`）

## 快速安装到项目

```bash
# 方式一：拷贝到目标项目的 .agents/skills/（Antigravity / 通用）
mkdir -p /path/to/your-project/.agents/skills
cp -r release/{name} /path/to/your-project/.agents/skills/

# 方式二：或拷贝到 .claude/skills/（Claude Code）
mkdir -p /path/to/your-project/.claude/skills
cp -r release/{name} /path/to/your-project/.claude/skills/

# 方式三：安装到全局 Skill 目录，所有项目直接生效
mkdir -p ~/.agents/skills ~/.claude/skills
cp -r release/{name} ~/.agents/skills/
# 或软链接指向本目录随仓库更新：
# ln -s "$PWD/release/{name}" ~/.agents/skills/{name}
```
"""
    else:
        rows = []
        for name, files, archive_path in bundles:
            total_kb = sum(p.stat().st_size for p in files) / 1024
            zip_bytes = archive_path.read_bytes()
            zip_kb = len(zip_bytes) / 1024
            sha256 = hashlib.sha256(zip_bytes).hexdigest()
            rows.append(f"| `{name}` | {len(files)} | {total_kb:.1f} KB | {zip_kb:.1f} KB | `{sha256}` |")
        table = "\n".join(rows)
        content = f"""# Release Bundles — ArknightsDesignSkill ({version})

本目录由 [`scripts/package-release.py`](../scripts/package-release.py) 生成，包含 **{len(bundles)} 个独立自包含的{stage_label}纯运行时 Skill 包**（版本 `{version}`），均已剔除维护文档与脚本，可按需单独安装避免小模型上下文串味。

## 包含产物

| Skill 包名 | 文件数 | 未压缩体积 | ZIP 体积 | ZIP SHA-256 |
| :--- | :-: | :-: | :-: | :--- |
{table}

## 按需安装到项目

```bash
# 仅复制需要的单个 Skill 目录到目标项目的 .agents/skills/ 或 .claude/skills/
mkdir -p /path/to/your-project/.agents/skills
cp -r release/<skill-name> /path/to/your-project/.agents/skills/
```
"""
    (RELEASE_DIR / "README.md").write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default=DEFAULT_VERSION, help="Release version label recorded in release/README.md")
    args = parser.parse_args()

    packaged: list[tuple[str, list[pathlib.Path], pathlib.Path]] = []
    targets: list[tuple[str, pathlib.Path]] = [(BUNDLE_NAME, ROOT)]
    for skill_dir in discover_suite_skills():
        targets.append((skill_dir.name, skill_dir))

    for name, src_root in targets:
        bdir = RELEASE_DIR / name
        zpath = RELEASE_DIR / f"{name}.zip"
        files = copy_bundle(src_root, bdir)
        verify_bundle(files, name, bdir)
        build_zip(files, name, bdir, zpath)
        packaged.append((name, files, zpath))
        print(f"[RELEASE {args.version}] Packaged {len(files)} files -> {bdir.relative_to(ROOT)}")
        print(f"[RELEASE {args.version}] Archive created -> {zpath.relative_to(ROOT)} ({zpath.stat().st_size} bytes)")

    write_release_readme(packaged, args.version)
    return 0


if __name__ == "__main__":
    sys.exit(main())
