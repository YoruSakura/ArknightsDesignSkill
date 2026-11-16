# Release Bundle — `arknights-design`

本目录由 [`scripts/package-release.py`](../scripts/package-release.py) 生成，包含可直接复制或解压接入下游前端项目的纯运行时 Skill 包（共 18 个文件，未压缩 779.6 KB；压缩包 233.3 KB），已剔除维护文档（`AGENTS.md`）与同步/校验脚本（`scripts/`）。

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
