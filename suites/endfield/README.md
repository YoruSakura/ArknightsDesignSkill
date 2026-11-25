# Endfield Theme Suite — 明日方舟：终末地特色专题设计套组

> **所属分支**：`suite/endfield`（基于 `main` 的通用 `v1.3` 基座演进，不污染 `main` 纯净通用包）  
> **创建与验收规范**：动工任何新专题前必读 [`SUITE_SPEC.md`](./SUITE_SPEC.md)

## 定位与设计边界

- 仓库根目录的 [`arknights-design`](../../SKILL.md) 负责**通用大方向**（本家 PRTS + 终末地纸墨信号黄工业编辑风通用多原型与控制台），规则严格且经小模型盲测验证，适用于大多数站点、专栏、画廊与控制台。
- 本目录（`suites/endfield/`）专门承载**与主 Endfield UI（纸白/烟黑 + 信号黄 `#FFFA00`）主题基调不相容、但极具独立视觉识别度的游戏内特色活动 / 开拓区 / 阵营 / 玩法专题**。
- **渐进式独立子 Skill**：每个专题都是完全自包含的独立 Skill（独立 `SKILL.md`、独立前缀 `.ef-<slug>-*`、独立骨架、独立打包产物），按需单独安装给 AI 助手，严禁互相依赖或串味混搭。

---

## 专题子 Skill 索引

| 子 Skill 目录 | 对应活动 / 区域 / 玩法方向 | 前缀 | 状态 | 说明 |
| :--- | :--- | :--- | :-: | :--- |
| [`_template/`](./_template/SKILL.md) | 空白标准化脚手架 | `.ef-<slug>-*` | 脚手架 | 新建专题时复制此目录，**不参与发布打包** |
| *（待定）* | *下一步逐个采风后补充* | — | 待启动 | 每套均须先实机/官网采风并过双门禁验收 |

---

## 快速新建一个终末地专题子 Skill

1. **先采风，再立项**：按 [`SUITE_SPEC.md`](./SUITE_SPEC.md) 第 1 节完成游戏实机界面或官方专题页采集，明确「为什么不能用主 Endfield UI 解决」及 3~5 个独有视觉铁律。
2. **复制脚手架**：
   ```bash
   cp -r suites/endfield/_template suites/endfield/endfield-<slug>
   ```
3. **补齐规范、样式与整页样板**：替换 `<slug>` 占位符，完善 `SKILL.md`、`references/`、`resources/theme.css` 与 `examples/index.html`。
4. **打包与校验**：
   ```bash
   python3 scripts/package-release.py --version v1.3-endfield-dev
   python3 scripts/verify.py --render --out /tmp/endfield-suite-verify
   ```
   待 1440px / 390px / 375px 实渲染与小模型冷启动盲测均通过后，再合入对应发布流程。
