# Release Bundle — `arknights-design` (v1.2-dev)

本目录由 [`scripts/package-release.py`](../scripts/package-release.py) 生成，包含可直接复制或解压接入下游前端项目的**开发测试版（Pre-release · 待审查）纯运行时 Skill 包**（版本 `v1.2-dev`，共 18 个文件，未压缩 829.0 KB；压缩包 243.2 KB），已剔除维护文档（`AGENTS.md`）与同步/校验脚本（`scripts/`）。

## 包含产物

- `arknights-design/`：可直接拷贝或软链接的完整 Skill 文件夹（含 `SKILL.md`、`LICENSE`、`NOTICE.md`、`references/`、`resources/`、`examples/`）
- `arknights-design.zip`：同内容的便携压缩包（顶层目录为 `arknights-design/`，`SHA-256`: `18ac33ff7c8591265f7cd93b00afcbddd216dd6601784116f350f804cd070108`）

## 快速安装到项目

```bash
# 方式一：拷贝到目标项目的 .agents/skills/（Antigravity / 通用）
mkdir -p /path/to/your-project/.agents/skills
cp -r release/arknights-design /path/to/your-project/.agents/skills/

# 方式二：或拷贝到 .claude/skills/（Claude Code）
mkdir -p /path/to/your-project/.claude/skills
cp -r release/arknights-design /path/to/your-project/.claude/skills/

# 方式三：安装到全局 Skill 目录，所有项目直接生效
mkdir -p ~/.agents/skills ~/.claude/skills
cp -r release/arknights-design ~/.agents/skills/
# 或软链接指向本目录随仓库更新：
# ln -s "$PWD/release/arknights-design" ~/.agents/skills/arknights-design
```
