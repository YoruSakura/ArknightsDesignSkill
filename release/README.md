# Release Bundles — ArknightsDesignSkill Ecosystem (v1.2-beta.1)

本目录由 [`scripts/package-release.py`](../scripts/package-release.py) 生成，包含可直接复制或解压接入下游前端项目的 **3 个测试版（Pre-release · 待审查）纯运行时 Skill 独立包**（版本 `v1.2-beta.1`），已剔除维护文档（`AGENTS.md`）与同步/校验脚本（`scripts/`）。

## 包含产物

| Skill 包名 | 定位与覆盖内容 | 文件数 | ZIP 体积 | ZIP SHA-256 |
| :--- | :--- | :-: | :-: | :--- |
| `arknights-design` | 主双体系（PRTS 本家 + Endfield UI）与六大官方活动系列预设 | 26 | 276.2 KB | `10aade390d620e9a294d20ab280fe351f1a0a6672a93c8422c511b2a8ae70978` |
| `arknights-contingency-contract` | 高难危机合约 / 行动协议 / 卫戍规程 / 矢量突破 / DOS 独立 Skill（.cc-*） | 7 | 21.1 KB | `bad2025ce549d38d84b3c3d438c39e4bd51fac8a6f587aa6ee6aa5ad6e94f19f` |
| `arknights-integrated-strategies` | 集成战略五代主题（萨卡兹 / 岁界园 / 水月 / 银凇 / 黑流）独立 Skill（.is-*） | 7 | 21.7 KB | `bca6bc5726b09ef992f44ea5991f00fd2fba785c8fcd290b779fa2bfd16e952e` |

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
