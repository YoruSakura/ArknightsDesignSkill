# Release Bundles — ArknightsDesignSkill Ecosystem (v1.2)

本目录由 [`scripts/package-release.py`](../scripts/package-release.py) 生成，包含可直接复制或解压接入下游前端项目的 **3 个正式版纯运行时 Skill 独立包**（版本 `v1.2`），已剔除维护文档（`AGENTS.md`）与同步/校验脚本（`scripts/`）。

## 包含产物

| Skill 包名 | 定位与覆盖内容 | 文件数 | ZIP 体积 | ZIP SHA-256 |
| :--- | :--- | :-: | :-: | :--- |
| `arknights-design` | 主双体系（PRTS 本家 + Endfield UI）与六大官方活动系列预设 | 26 | 276.5 KB | `0fdc917ad22ebf11a36170027148dbc062e36c0c3d5d701c8998250715d9173a` |
| `arknights-contingency-contract` | 高难危机合约 / 行动协议 / 卫戍规程 / 矢量突破 / DOS 独立 Skill（.cc-*） | 7 | 22.3 KB | `1b37a6c130c473278d306b2a39cae0bc1650b66f30cbcd3d578ff836d8b96b68` |
| `arknights-integrated-strategies` | 集成战略五代主题（萨卡兹 / 岁界园 / 水月 / 银凇 / 黑流）独立 Skill（.is-*） | 7 | 23.6 KB | `57f868ae5cc93fcca01c480857e69a7209dd1ca4865d23ccf13eb270ce53f9e9` |

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
