# SUITE_SPEC — 明日方舟本家专题子 Skill 规范与验收红线

> 本规范沉淀自 `v1.1` / `v1.2` 的历史视觉复盘（见仓库根目录 [`AGENTS.md`](../../AGENTS.md)）。凡在 `suite/arknights` 分支新建或迭代任何本家专题子 Skill，必须逐条遵守。

---

## 一、立项前置：实机采风，严禁凭空硬凑

1. **必须先拿真实视觉依据**：动工前必须基于对应活动/玩法的**游戏内实机 UI 截图、官方专题网站实机渲染（含 WebGL 页面用外部 Chrome 采集）或官方视觉拆解**建立事实档案，明确记录：
   - 页面空间骨架（非盒状或特有信息架构）
   - 色板层级与亮/暗极性（含正文与微文字对比度）
   - 字体气质（展示字 / 正文字 / 编号字及其开源回退链）
   - 独有几何形状、图形母题与交互节拍
2. **严禁三类反模式**：
   - ❌ **海报硬拼**：只看一张主视觉插画，用 CSS 方框/SVG 道具强行模仿平面海报；
   - ❌ **同质套壳**：只给通用卡片换个强调色，版式骨架千篇一律；
   - ❌ **跨活动混搭**：把不同玩法、不同阵营的视觉符号混进同一套模板。

---

## 二、目录结构与完全自包含原则

每个真实专题子 Skill 位于 `suites/arknights/arknights-<slug>/`，结构如下（标准模板见 [`_template/`](./_template/SKILL.md)）：

```text
suites/arknights/arknights-<slug>/
├── SKILL.md                          # 独立入口（≤ 120 行，含 YAML frontmatter）
├── references/
│   ├── foundations.md                # 视觉哲学、色板对比度、字体与形状铁律、与主 PRTS 边界
│   └── layout-and-components.md      # 专属页面骨架、独有母题与可交互组件 ARIA 契约
├── resources/
│   └── theme.css                     # 独立命名空间 CSS（.ak-<slug>-* / --ak-<slug>-*）
└── examples/
    └── index.html                    # 完整可交互脱敏整页样板
```

- **彻底解耦**：专题子 Skill **不得**通过相对路径引用根目录 `resources/prts-*.css` 或其他子 Skill 文件；打包至 `release/arknights-<slug>/` 后必须能够脱离本仓库独立安装运行。
- **允许刻意破例，但必须自洽**：主 PRTS 要求「纯直角、严禁 45° 切角、黑灰白 + 冰青」；专题子 Skill 允许根据该活动真实 UI 打破这些限制（例如战术切角、宣纸衬线、高对比警示网格、典籍花边等），但必须在 `references/foundations.md` 显式列出「与主 PRTS 的刻意偏离项」并保持本套内部自洽。
- **命名空间隔离**：CSS 类与自定义属性统一使用短且唯一的专属前缀（如 `.ak-<slug>-*` / `--ak-<slug>-*` 或简写双字母前缀），防止与其他 Skill 冲突。

---

## 三、小模型友好与工程底线

1. **渐进式披露**：`SKILL.md` 控制精炼体量（建议 80~120 行），按「场景判别 → 必读清单 → 执行与弹性适配边界 → 自检红线 → 渲染验证」组织，把大段组件 DOM 蓝图下沉至 `references/`。
2. **业务脱敏黑名单**：每个子 Skill 必须在 `SKILL.md` 明确「样板虚构代号/游戏专有词严禁漏入非游戏业务项目」，杜绝假十六进制（`0x7F3A`、`0xDEAD` 等），微文字一律为真实可读内容。
3. **无商业/侵权资产**：不内置鹰角官方位图或商业字体文件，字体均提供开源回退链与离线 `@fontsource` 方案。
4. **响应式与交互硬约束**：
   - 严禁在 HTML 写死内联 `grid-template-columns`；全部布局走 CSS 响应式类，必须适配 `1440px`、`390px` 与 `375px` 零横向溢出。
   - 作用域根节点必须带 `[hidden] { display: none !important; }`，防止 `display: grid/flex` 组件覆盖原生隐藏属性。
   - 抽屉/弹窗/页签/下拉菜单须遵守 WAI-ARIA 键盘与焦点归还契约；所有 `@keyframes` 须配 `@media (prefers-reduced-motion: reduce)` 保护。

---

## 四、双门禁验收标准（转正前提）

1. **自动化校验与实渲染审查**：
   - `python3 scripts/package-release.py` 成功生成纯净独立包 `release/arknights-<slug>/` 与 `.zip`（零断链、零越界引用、零维护文件泄露）。
   - `python3 scripts/verify.py --render --out /tmp/arknights-suite-verify` 全量通过（HTML 类存在性、Markdown 链接、CSS `@keyframes` 零闲置、`release/` 同步、1440px/390px 渲染与 375px/390px 零横向溢出），并人工逐张复核渲染图对比度与排版节奏。
2. **小模型冷启动盲测**：
   - 单独安装 `release/arknights-<slug>/` 给轻量模型完成真实业务页面盲测，确认小模型能在不串味、不漏基座、不泄漏游戏词的前提下稳定还原该专题气质。
