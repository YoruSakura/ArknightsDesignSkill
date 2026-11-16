---
name: arknights-design
description: >-
  Use this skill whenever the user asks to design, initialize, build, or refactor a frontend website,
  web app, component, or UI boilerplate in Arknights style (明日方舟本家 PRTS 终端/档案风格) or
  Arknights: Endfield style (明日方舟：终末地 工业编辑风 / Endfield UI). Provides complete design
  specifications, anti-pattern checklists, ready-to-copy CSS token & component bundles, and page blueprints.
---

# Arknights & Endfield Frontend Design Skill (`arknights-design`)

本 Skill 包含《明日方舟》本家（**PRTS Design**）与《明日方舟：终末地》（**Endfield UI**）两套完整、正交的前端设计系统。
**注意：这两套系统的视觉语法截然不同，严禁将两者的规则混为一谈！**

---

## 第一步：判定目标视觉体系（Style Router）

在开始写代码前，先根据用户需求判定采用哪一套设计体系（若用户仅说“明日方舟风格”未指明本家还是终末地，**先向用户确认**；无法提问时默认采用体系 A（本家 PRTS），并在回复中明确写出这一假设，且不得混用两套规则）：

| 维度 | 体系 A：明日方舟本家 (`PRTS Design`) | 体系 B：明日方舟：终末地 (`Endfield UI`) |
| :--- | :--- | :--- |
| **核心气质** | **罗德岛档案（亮）/ PRTS 终端（暗）** | **工业编辑风（Industrial Editorial）**——印出来的技术画册与测绘终端 |
| **色彩哲学** | **黑白为体、青为用**：暗底配官网青 `#18D1FF`，亮底配游戏蓝 `#0098DC`；次强调黄 `#FFD800`；顶栏与页脚恒为深黑框 | **纸与墨是主体，信号黄是唯一焦点**：13 级纯中性灰 + 信号黄 `#FFFA00`（一屏黄面积 $\le 10\%$，白底严禁用黄字，用 `#6B5D00`） |
| **形状铁律** | **纯直角 `border-radius: 0`，严禁任何 45° 切角/斜切**；色条与 1px 细框用 `border-image` 直角拼接；独立小图形用源石菱形 `◆` | **形状即语义**：面板/归档标签用直角，按钮统一 `4px` 微圆角，主要行动/机械控件用 `45°` 单角切角（`cut-tr`）或斜楔（`wedge-r`），头像/仪表用正圆，筛选/资源用胶囊 |
| **边框与阴影** | 卡片与面板带 `1px solid var(--ak-border)` 细框 + 左侧 `4px` 或顶部 `3px` 色条；无辉光 | **默认不围整圈边框**（统计块靠左缘 3px 墨线，提示条靠左缘 4px 色条，输入框用凹陷底 + 2px 底边线）；浮层用零偏移环境阴影 `0 0 <blur>` |
| **装饰母题** | 45° 警示斜纹（`.ak-stripes`）、半调网点渐隐（`.ak-halftone`）、角标直角三角（`.ak-corner`）、黑白反转（`.ak-inverse`） | 斜纹镂空巨字（`ghost-hatch`）、标准滑块分节标题（`[███ ↘]`）、方括号姓名（`[ 名称 ]`）、CMY 注册色条、四角 L 形括号（`corner-brackets`）、等高线（`contour`） |

---

## 第二步：按需读取深度规范与拷贝静态资源（Progressive Disclosure）

确定目标体系后，**必须先用 `read_file` 阅读对应的两份基础手册（foundations + 母题/装饰）**；组件目录（components-catalog）体量较大，**仅在需要具体组件的 DOM/类名/ARIA 契约时再按需读取**，并将对应的 CSS 资源文件拷贝到目标前端项目中：

### 选体系 A（明日方舟本家 · PRTS Design）时：
1. **必读规范**：
   - [PRTS 基础设计规范与色彩/排版令牌](./references/prts/foundations.md)
   - [PRTS 装饰母题与壳层/核心组件蓝图](./references/prts/decor-and-components.md)
   - [PRTS 全组件目录与交互蓝图](./references/prts/components-catalog.md)（**按需读取**：按钮、菜单/页签/分页、表单、弹窗/抽屉/Toast、进度/时间线/步骤条 五大类通用 UI + 方舟领域件完整蓝图 + `@fontsource` 离线字体配置，可直接跨框架移植）
2. **可直接拷贝到目标项目的样式资源**：
   - 完整样式表（含令牌 + `.ak-scope` + 全部通用组件 + 方舟装饰 + 领域组件 + `.ak-header`/`.ak-footer` 骨架，零外部图片依赖）：[`resources/prts-design.css`](./resources/prts-design.css)
   - **补丁层（必须紧随 `prts-design.css` 之后引入）**：[`resources/prts-addons.css`](./resources/prts-addons.css) —— 修正黑色 Hero 内 contrast 按钮对比度、Hero 色面、搜索键帽、菜单按钮重置、宽表格横向滚动、抽屉遮罩等；对样式的任何修正都写在这里，不要直接改 `prts-design.css`
   - 仅需令牌变量时：[`resources/prts-tokens.css`](./resources/prts-tokens.css)
   - 样板与组件对照（仅作构图与交互结构参考，**严禁直接照搬测试业务文案与假数据**）：
     - 整页构图样板：[`examples/prts-boilerplate.html`](./examples/prts-boilerplate.html)
     - 全组件交互目录：[`examples/prts-components.html`](./examples/prts-components.html)

### 选体系 B（明日方舟：终末地 · Endfield UI）时：
1. **必读规范**：
   - [Endfield 基础设计规范、六大原则与七大界面家族](./references/endfield/foundations.md)
   - [Endfield 母题工具类与核心展示组件](./references/endfield/motifs-and-components.md)
   - [Endfield 全组件目录与交互蓝图](./references/endfield/components-catalog.md)（**按需读取**：按钮/工具栏、三态页签、分页步骤、下拉/气泡、弹窗/抽屉/Toast、表单含菱形切换、表格/折叠/时间线、高阶选择器与测绘 HUD `Sparkline`/`TickRing`/`Viewfinder`/`Carousel` + 16 个关键帧与 17 个 `.animate-*` 动效类）
2. **可直接拷贝到目标项目的样式资源**：
   - 零依赖通用纯 CSS 版（含 `--ef-*` 亮/暗/反转三套令牌 + 全部母题类 + 全套 `.ef-*` 通用交互组件，适用于任意 HTML / Vue / React / Svelte 项目，AI 可直接按类名与 ARIA 状态契约移植封装）：[`resources/endfield-standalone.css`](./resources/endfield-standalone.css)
   - Tailwind CSS v4 专用版（含 `@theme`、`@theme inline`、`@utility`）：[`resources/endfield-theme.css`](./resources/endfield-theme.css)
   - 样板与组件对照（仅作构图与交互结构参考，**严禁直接照搬测试业务文案与假数据**）：
     - 整页构图样板：[`examples/endfield-boilerplate.html`](./examples/endfield-boilerplate.html)
     - 全组件交互目录：[`examples/endfield-components.html`](./examples/endfield-components.html)

---

## 第三步：项目初始化与开发执行流程

当用户要求“使用本 Skill 初始化一个网站样板 / 组件页面”时，严格按以下步骤执行：

1. **注入样式基座与字体**：
   - 将本 Skill 目录下的 [`resources/prts-design.css`](./resources/prts-design.css)（+ [`resources/prts-addons.css`](./resources/prts-addons.css)）或 [`resources/endfield-standalone.css`](./resources/endfield-standalone.css) 复制到目标项目的静态样式目录（如 `src/styles/` 或 `public/`）并在入口引入。
   - 在 `<head>` 引入对应的 Google Fonts 开源字体（PRTS：`Oswald` + `Chakra Petch` + `Noto Sans SC`；Endfield：`Archivo` + `Outfit` + `Space Grotesk` + `JetBrains Mono` + `Noto Sans SC`）。
   - 字体说明：规范中的 `Bender` / `Novecento Sans Wide` 为商业字体，本 Skill 不附带，实际回退到 `Oswald` / `Chakra Petch`。面向中国大陆用户时，Google Fonts 可能不可达，建议用 `@fontsource`（两份 `components-catalog.md` 均附安装与引入代码）或本地 `@font-face` 自托管，并保留 `Noto Sans SC` → 系统黑体的回退链。
2. **搭建符合正统构图的页面外壳**（**响应式是硬要求**：布局一律用类 `.ak-layout` / `.ak-grid-2` / `.ef-hero__grid` / `.ef-split` / `.ef-grid-2` / `.ef-grid-3` / `.ef-stat-row` / `.ef-section`，**禁止写死内联 `grid-template-columns`**；PRTS <1120px 侧栏变抽屉，需 `.ak-local-nav__menu` 入口，参考样板；Endfield <1024px 侧轨变顶部横轨）：
   - **PRTS**：采用「黑色终端顶栏 `.ak-header` + 左侧导航导轨 `.ak-sidebar` + 主内容区 `.ak-main` + 黑色斜纹顶边页脚 `.ak-footer`」，支持「档案（Light）/ 终端（Dark）」一键切换。
   - **Endfield**：采用「左侧窄轨 `.ef-side-rail`（底部配唯一主行动块 `.ef-nav-action`）+ 偏心构图主舞台（`1.5fr : 0.9fr` 不等宽分栏）+ 通栏信号黄色带标题 `.ef-band-title` 分隔亮暗版块」，支持「纸白（Light）/ 烟黑（Dark）」切换及局部 `[data-theme="inverse"]` 反转标题带。
3. **组合标志性母题与全组件库（跨框架通用）**：
   - 拒绝千篇一律的居中三卡片网格！按 `components-catalog.md` 的 DOM 与 ARIA 状态契约（如 `.is-active` / `.is-open` / `aria-pressed` / `aria-selected` / 原生 `<details>` / `<dialog>`）直接在 HTML、React TSX、Vue SFC 或 Svelte 中复刻按钮、菜单、弹窗、表单与数据表，严禁脱离既有 CSS 另起炉灶。
   - 必须组合使用各体系的签名级组件（如 PRTS 的 `.ak-hero`、`.ak-news`、`.ak-panel`、`.ak-stat`、`.ak-table`、`.ak-stage`；Endfield 的 `ghost-hatch` 镂空巨字、`ef-section-title` 滑块标题、`ef-bracket-title` 方括号名、`ef-reg-strip` 三原色校准条、`ef-stat` 左竖线统计块、`ef-data-row` 深色数据行带、`ef-item-slot` 底部稀有度渐变格 + `corner-brackets` 四角括号选中）。
4. **弹性适配边界（主方向不可偏离，业务差异可随机应变）**：
   - **工程与基座底线（等价替代，不写死妥协）**：任何需求不得绕开 `--ak-*` / `--ef-*` 令牌与既有 `.ak-*` / `.ef-*` 基座重写平行皮肤；若用户要求特定多栏（如三联工作台），**必须用带手机降维断点的 CSS 类实现，严禁在 HTML 写死内联 `grid-template-columns`**；若用户要求“硬核编号感”，替换为真实业务编号，**禁用 `0x7F3A` / `0xDEAD` 伪乱码**，并彻底替换非游戏业务中的样板地名/专有名词（如 `PERLICA`、`DIJIANG`、`TALOS-N07`、`北岭`、`罗德岛`）。
   - **品牌配色换皮（换强调不换骨）**：若业务网站需要接入自有品牌配色，禁止整页铺满高饱和彩底或重绘主题层，应通过语义令牌覆盖完成「90% 中性纸墨骨架 + ≤10% 品牌主色」映射——**PRTS** 覆盖 `--ak-theme-accent` / `--ak-theme-accent-fg` / `--ak-theme-accent-subtle` 与亮/暗 `--ak-accent` / `--ak-accent-hover` / `--ak-accent-fg` / `--ak-link` / `--ak-focus`（保留黑白灰画布与黑框顶栏）；**Endfield** 覆盖 `--ef-action` / `--ef-action-pressed` / `--ef-on-action` / `--ef-accent-ink` / `--ef-accent-ink-inverse`（中性灰阶画布至多微调冷暖倾向，**必须按品牌色明度重设 `--ef-on-action` 反色字与亮底深档 `--ef-accent-ink` 保证对比度**）。
   - **业务可视化与布局扩展（鼓励自由发挥）**：DAG 拓扑、测绘剖面 SVG、多维监控图等高阶领域模块可随业务自由创作，只需继承对应体系的语义色彩与字体变量，自动兼容亮/暗双主题与 390px 响应。
   - **外观偏好的有条件让步**：默认严格遵守第四步质感红线；仅当用户**明确坚持**特定局部表现（如要求局部面板带微圆角或浅透明）时，才允许在不破坏主体系色彩哲学、导航外壳、标准表格/表单底座与对比度前提下，用**局部自定义扩展类**实现最小化派生并提示偏离，**禁止借“破例”将整站改造成通用发光圆角 SaaS**。

---

## 第四步：交付前的人类级视觉自检清单（Self-Audit）

在完成代码编写后，逐条对照以下红线自检，任何一条违规必须立即修正：

- [ ] **是否混淆了两套系统的形状？**
  - PRTS 默认严禁出现 `clip-path` 45° 切角或圆角卡片；
  - Endfield 严禁四角全切八边形，切角只用于行动/机械控件，且可聚焦按钮的切角必须画在 `::before` 上以保留焦点环。
- [ ] **颜色对比度与面积预算是否合规？**
  - PRTS 的不可点击小标签（overline / eyebrow / 章节英文副标）是否误用了强调色？（必须用 `--ak-fg-muted` 灰色）；
  - Endfield 的信号黄 / 品牌填充色是否控制在全屏面积 10% 以内？亮色白底上文字强调必须使用深档 `--ef-accent-ink`（默认 `#6B5D00`），且自定义品牌换色时 `--ef-on-action` / `--ak-accent-fg` 必须满足高对比可读性。
- [ ] **数字与英文排版是否克制且真实？**
  - PRTS 的 `<table>` 数字列是否使用了正文字体 + `tabular-nums`（严禁在表格内用 Bender）？双语标题是否控制在一页 1～2 处？
  - 微文字（Micro-text）是否为真实可读的栏目名、日期、版本号、设备/节点编号？（严禁 `0x7F3A`、`0xDEAD` 等假十六进制乱码，非游戏项目禁止残留 `PERLICA` / `DIJIANG` / `TALOS-N07` / `北岭` / `罗德岛`）。
- [ ] **是否杜绝了通用 SaaS / 科幻俗套（并守住主基调）？**
  - 默认严禁大圆角（`8px–16px`）投影卡片、悬停上浮放大、毛玻璃发光霓虹边与六边形蜂窝网格；即使用户明确坚持了局部定制，也仅允许以局部扩展类附着在既有骨架上并在交付说明中标注，主体依然保留清晰的原体系质感与基座组件复用。

---

## 第五步：渲染验证（硬性门槛，不通过不得交付）

规则自检只能查“写了什么”，查不出“长什么样”。接入业务项目并编写完成后，交付前**必须真的渲染**（桌面 1440px + 手机 390px × 亮/暗 4 张图）并人工/视觉看图：

```bash
# 桌面 + 手机，亮 + 暗，共 4 张（把 data-theme 改一下再截一次）
google-chrome --headless=new --no-sandbox --hide-scrollbars --window-size=1440,1300 --virtual-time-budget=6000 --screenshot=desktop.png file://$PWD/index.html
google-chrome --headless=new --no-sandbox --hide-scrollbars --window-size=390,2400  --virtual-time-budget=6000 --screenshot=mobile.png  file://$PWD/index.html
```

逐项检查，任一项不过必须修复：
- [ ] **无文字重叠/被裁切**：镂空巨字（`ghost-hatch`）只能是背景层，与标题、面包屑之间要留出空间（用 `.ef-hero__ghost` + `.ef-hero__grid`）。
- [ ] **手机 390px 无横向溢出**、主内容可见、表格不被挤成逐字竖排（宽表格套 `.ak-table-scroll`）。
- [ ] **亮/暗两套主题下所有按钮、文字对比度足够**（尤其“恒为黑底”的区域内的 contrast/反转按钮）。
- [ ] **没有大面积纯色占位块**；Hero 色面要么是网点渐隐，要么放真实图片。
- [ ] 主题切换按钮初始状态与 `data-theme` 一致，并持久化用户选择。
