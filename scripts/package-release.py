#!/usr/bin/env python3
"""Build a clean, self-contained, test-ready Skill bundle under release/arknights-design/.

Usage:
  python3 scripts/package-release.py
"""
from __future__ import annotations

import pathlib
import re
import shutil
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
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


def copy_bundle() -> list[pathlib.Path]:
    """Recreate release/arknights-design cleanly from canonical repository assets."""
    RELEASE_DIR.mkdir(parents=True, exist_ok=True)
    if BUNDLE_DIR.exists():
        shutil.rmtree(BUNDLE_DIR)
    BUNDLE_DIR.mkdir(parents=True, exist_ok=True)

    for rel in INCLUDE_FILES:
        src = ROOT / rel
        if not src.exists():
            raise FileNotFoundError(f"Missing required root file: {rel}")
        shutil.copy2(src, BUNDLE_DIR / rel)

    for rel_dir in INCLUDE_DIRS:
        src_dir = ROOT / rel_dir
        if not src_dir.is_dir():
            raise NotADirectoryError(f"Missing required directory: {rel_dir}")
        shutil.copytree(src_dir, BUNDLE_DIR / rel_dir, ignore=IGNORE_PATTERNS)

    return sorted(p for p in BUNDLE_DIR.rglob("*") if p.is_file())


def verify_bundle(files: list[pathlib.Path]) -> None:
    """Validate frontmatter, asset isolation, and zero broken relative links inside the bundle."""
    skill_md = BUNDLE_DIR / "SKILL.md"
    head = skill_md.read_text(encoding="utf-8")
    if not re.match(r"^---\s*\nname:\s*arknights-design\s*\ndescription:", head):
        raise ValueError("release/arknights-design/SKILL.md missing valid frontmatter")

    forbidden = {"AGENTS.md", "scripts", "verify.py", "sync-upstream.py"}
    leaked = [p.relative_to(BUNDLE_DIR) for p in files if p.name in forbidden or "scripts" in p.parts]
    if leaked:
        raise ValueError(f"Maintainer artifacts leaked into release bundle: {leaked}")

    for md in sorted(BUNDLE_DIR.rglob("*.md")):
        txt = md.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(((?:\.\.?/)[^)#]+)", txt):
            resolved = (md.parent / target).resolve()
            if not resolved.is_relative_to(BUNDLE_DIR.resolve()) or not resolved.exists():
                raise ValueError(f"Broken or escaping link in {md.relative_to(BUNDLE_DIR)}: {target}")

    for hp in sorted((BUNDLE_DIR / "examples").glob("*.html")):
        txt = hp.read_text(encoding="utf-8")
        for target in re.findall(r'(?:href|src)="((?:\.\.?/)[^"#?]+)"', txt):
            resolved = (hp.parent / target).resolve()
            if not resolved.is_relative_to(BUNDLE_DIR.resolve()) or not resolved.exists():
                raise ValueError(f"Broken or escaping asset in {hp.relative_to(BUNDLE_DIR)}: {target}")


def build_zip(files: list[pathlib.Path]) -> None:
    """Create release/arknights-design.zip preserving the arknights-design/ top-level folder."""
    if ARCHIVE_PATH.exists():
        ARCHIVE_PATH.unlink()
    with zipfile.ZipFile(ARCHIVE_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in files:
            arcname = pathlib.Path(BUNDLE_NAME) / path.relative_to(BUNDLE_DIR)
            zf.write(path, arcname.as_posix())


def write_release_readme(files: list[pathlib.Path]) -> None:
    total_kb = sum(p.stat().st_size for p in files) / 1024
    zip_kb = ARCHIVE_PATH.stat().st_size / 1024
    content = f"""# Release Bundle — `arknights-design`

本目录由 [`scripts/package-release.py`](../scripts/package-release.py) 生成，包含可直接复制或解压接入下游前端项目的纯运行时 Skill 包（共 {len(files)} 个文件，未压缩 {total_kb:.1f} KB；压缩包 {zip_kb:.1f} KB），已剔除维护文档（`AGENTS.md`）与同步/校验脚本（`scripts/`）。

## 包含文件

- `arknights-design/`：可直接拷贝或软链接的完整 Skill 文件夹（含 `SKILL.md`、`LICENSE`、`NOTICE.md`、`references/`、`resources/`、`examples/`）
- `arknights-design.zip`：同内容的便携压缩包（顶层目录为 `arknights-design/`）

## 快速安装到测试项目

```bash
# 方式一：拷贝到测试项目的 .agents/skills/（Antigravity / 通用）
mkdir -p /path/to/test-project/.agents/skills
cp -r release/arknights-design /path/to/test-project/.agents/skills/

# 方式二：或拷贝到 .claude/skills/（Claude Code）
mkdir -p /path/to/test-project/.claude/skills
cp -r release/arknights-design /path/to/test-project/.claude/skills/

# 方式三：安装到全局 Skill 目录，所有空测试目录直接生效
mkdir -p ~/.agents/skills ~/.claude/skills
cp -r release/arknights-design ~/.agents/skills/
# 或软链接指向本目录以便随改随测：
# ln -s "$PWD/release/arknights-design" ~/.agents/skills/arknights-design
```
"""
    (RELEASE_DIR / "README.md").write_text(content, encoding="utf-8")


def main() -> int:
    files = copy_bundle()
    verify_bundle(files)
    build_zip(files)
    write_release_readme(files)
    print(f"[RELEASE] Packaged {len(files)} files -> {BUNDLE_DIR.relative_to(ROOT)}")
    print(f"[RELEASE] Archive created -> {ARCHIVE_PATH.relative_to(ROOT)} ({ARCHIVE_PATH.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
