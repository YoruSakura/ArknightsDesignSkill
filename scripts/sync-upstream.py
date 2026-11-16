#!/usr/bin/env python3
"""
Sync and bundle CSS tokens & stylesheets from upstream repositories:
- MooncellWiki/prts-design (MIT)
- icaruszezen/endfield-ui (MIT)
"""
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_DIR = os.path.join(ROOT, "resources")

def bundle_css(file_path: str) -> str:
    base_dir = os.path.dirname(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    def repl(match):
        imp_path = match.group(1)
        full_imp = os.path.join(base_dir, imp_path)
        return f"\n/* === {imp_path} === */\n" + bundle_css(full_imp)

    return re.sub(r"@import\s+url\([\"']?([^\"')]+)[\"']?\)\s*;", repl, content)


def sync_from_dirs(prts_dir: str, endfield_dir: str):
    os.makedirs(RESOURCES_DIR, exist_ok=True)

    # 1. PRTS Tokens
    prts_css_src = os.path.join(prts_dir, "packages", "css", "src")
    shutil.copyfile(
        os.path.join(prts_css_src, "tokens.css"),
        os.path.join(RESOURCES_DIR, "prts-tokens.css"),
    )

    # 2. PRTS Full Standalone + Chrome CSS
    standalone_css = bundle_css(os.path.join(prts_css_src, "standalone.css"))
    chrome_css = bundle_css(os.path.join(prts_css_src, "chrome", "index.css"))
    banner = (
        "/*! PRTS Design · @mooncellwiki/prts-design-css (Standalone + Chrome) · MIT License\n"
        " *  Source: https://github.com/MooncellWiki/prts-design\n"
        " *  Docs:   https://mooncellwiki.github.io/prts-design/\n"
        " */\n"
    )
    with open(os.path.join(RESOURCES_DIR, "prts-design.css"), "w", encoding="utf-8") as f:
        f.write(banner + standalone_css + "\n/* === chrome/index.css === */\n" + chrome_css)

    # 3. Endfield Tailwind v4 Theme + Utilities
    ef_styles_dir = os.path.join(endfield_dir, "packages", "ui", "src", "styles")
    with open(os.path.join(ef_styles_dir, "theme.css"), "r", encoding="utf-8") as f:
        ef_theme = f.read()
    with open(os.path.join(ef_styles_dir, "utilities.css"), "r", encoding="utf-8") as f:
        ef_utils = f.read()

    ef_banner = (
        "/*! Endfield UI · @endfield-ui/react (Tailwind v4 Theme + Motif Utilities) · MIT License\n"
        " *  Source: https://github.com/icaruszezen/endfield-ui\n"
        " *  Docs:   https://icaruszezen.github.io/endfield-ui/design/\n"
        " */\n"
    )
    with open(os.path.join(RESOURCES_DIR, "endfield-theme.css"), "w", encoding="utf-8") as f:
        f.write(ef_banner + ef_theme + "\n/* === utilities.css === */\n" + ef_utils)

    print("Synced resources/prts-tokens.css, resources/prts-design.css, resources/endfield-theme.css")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        sync_from_dirs(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python3 scripts/sync-upstream.py <prts-design-dir> <endfield-ui-dir>")
        sys.exit(1)
