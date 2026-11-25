# PRTS Design（明日方舟本家）基础设计规范

> 来源依据：`ak.hypergryph.com` 明日方舟官网实测设计语言 × `MooncellWiki/prts-design`（MIT 协议）组件基座与游戏内 PRTS 终端规范。

---

## 一、 一句话定位与两种宏观载体

**一句话定位**：**黑白灰炭为体、冰青为用；纯直角无切角、无辉光；以“开放三角暗格画布 + 极简 1px 建筑标尺线 + 极限排版对比”替代套娃边框。**
UI 的本质是**《明日方舟》官网的冷峻建筑感与罗德岛 PRTS 指挥终端**，**绝对不要一上来就把它做成“四面带边框的 Wiki 百科侧栏”**。

开始写页面前，先根据业务形态选定宏观载体：

| 维度 | 载体 1：官网展示 / 概念门户（默认，师法 `ak.hypergryph.com`） | 载体 2：PRTS 百科 / 档案控制台（`MooncellWiki/prts-design`） |
| :--- | :--- | :--- |
| **适用场景** | 产品官网、品牌落地页、智能调度台主页、情报简报站 | 百科图鉴、文档站、高密度筛选表单、干员数值矩阵表 |
| **顶栏导航** | 极简漂浮深黑玻璃条 `.ak-topbar`（双语上下叠排导航 `EN / 中文` + 右侧声波与主题开关） | 三列终端页眉 `.ak-header`（Logo + `/` 快捷键检索触发器 + 主题开关） |
| **主体骨架** | 开放大气画布 `.ak-bg-lattice` + 全幅无侧栏 `.ak-site-shell`（长文博客用 `.ak-prose-shell`、画廊用 `.ak-gallery-grid`、登录用 `.ak-auth-shell`；概念门户可选配右侧 1px 竖轨 `.ak-stage-shell` + `.ak-index-rail`） | `.ak-layout` 两列布局（左侧 `.ak-sidebar` / `.ak-portlet` 导航树 + 主内容 `.ak-main`，<1120px 自动折叠为抽屉） |
| **边框纪律** | **去边框化（能划线的绝不画框）**：`.ak-rule` 1px 标尺配实块、`.ak-stat--minimal` 顶线指标、`.ak-folio-list` 无框清单、`.ak-news-grid--staggered` 错位无框下文字 | 按功能克制分组使用 `.ak-panel` / `.ak-table`（`1px` 细框 + `border-image` 4px 色条直角拼接） |
| **Hero 构图** | 开放 `.ak-hero--editorial`（左下贴边低透巨字 `.ak-ghost-word` + 左侧大标题 + 右侧 `.ak-brief` & 4 格 `.ak-thumb-card` 缩略选卡与滑轨） | 经典 `.ak-hero` 或紧接任务状态条进入数据矩阵 |

---

## 二、 六条核心构图原则（判断“像不像真方舟”的唯一标准）

### 1. 黑白灰炭为体，冰青仅作锋利点睛
* **大面积永远是克制的黑炭灰阶或制图灰白**：暗色主题下用 `#0f0f10`–`#1a1b1c` + 微弱三角网格暗格与斜光束（`.ak-bg-lattice`），亮色主题用 `#f5f5f5` / `#ffffff` 档案制图白。
* **主强调色克制且分明**：终端（暗）下用官网冰青 `--ak-cyan-500` (`#18D1FF`)；档案（亮）下用游戏蓝 `--ak-blue-500` (`#0098DC`，小字可点击标签用 `--ak-link` `#0072A8` 保证 5:1+ 对比度）；次强调黄 `#FFD800` 仅用于计数/关键提示。
* **不滥用工业警戒条纹**：黄黑斜纹 `.ak-stripes` **只留给明确的危险操作、施工占位或告警提示**，严禁当成常规页脚或页面装饰条满屏贴。
* **黑框顶栏与页脚**：无论页面处在档案（Light）还是终端（Dark），顶栏（`.ak-topbar` / `.ak-header`）与页脚（`.ak-footer`）永远保持深黑底，构成「黑框白纸 / 黑框黑纸」。

### 2. 反“套娃边框”：能用一根 1px 线解决，绝不画四边方框
* 官网高级感的第一来源是**大量留白与极简建筑标尺线**，而不是把每个统计数字、每条新闻、每张卡片都框在 `1px solid` 方盒里再叠一层方盒：
  * 分节分隔优先使用 `.ak-rule`（一条 `1px` 细横线 + 左端一块 `4px × 48px` 纯实心短块）；
  * 统计数字在展示页优先使用 `.ak-stat-row--open > .ak-stat--minimal`（只留顶线 + 左端 `28px` 青色短条，**零左右底边框**）；
  * 条目列表、设定索引、情报流优先使用 `.ak-folio-list > .ak-folio-item`（无背景框、仅靠 `1px` 底分隔线、字阶落差与左缘 `3px` 悬停/激活细条）；
  * 数据表外层如无需分组标题栏，直接 `<div class="ak-table-scroll"><table class="ak-table">…</table></div>`，不再外面硬套一层 `.ak-panel` 框。

### 3. 三层景深与不对称错位节奏
* **背景层（极低透明、绝不压字）**：`.ak-bg-lattice` 三角分割网格 + 对角斜光 + 左下角半调圆点渐隐，以及 `.ak-ghost-word` / `.ak-watermark` 贴边截断巨字（`rgba(255,255,255,0.042)` / `rgba(0,0,0,0.045)`），允许越界被容器裁切，不可干扰前景阅读。
* **内容层（破除齐头对称网格）**：采用 `.ak-split`（`0.9fr : 1.35fr` 不等宽分栏）和 `.ak-news-grid--staggered`（错位双列卡片，右列桌面端视觉下沉 40px），以及 `.ak-showcase-strip`（四列垂直无间隙暗幕切分）。
* **前景层**：仅保留漂浮双语顶栏 `.ak-topbar`（或 `.ak-header`）与右侧 `1px` 竖轨索引 `.ak-index-rail`。

### 4. 三种字体分工与双斜杠语法
* **字族职责严明**：
  * `--ak-font-display`（`Oswald` / `Novecento Sans Wide`，必配 `font-variant-numeric: lining-nums`）：Hero 大号全大写英文字、错位序号 `01`、情报卡 `NEWS / DISPATCH`、去边框指标大数字。
  * `--ak-font-label`（`Chakra Petch` / `Bender`）：双斜杠眉题 `RHODES ISLAND ://`、状态代号 `RI // 01`、等宽时间戳 **`YYYY // MM / DD`**（如 `2026 // 11 / 18`）。
  * `--ak-font-body`（`Noto Sans SC` / 思源黑体，行高 `1.7`）：中文正文、界面控件与**全部 `<table>` 表格数字**（表格内禁止用 Bender，必开 `tabular-nums`）。
* **双语克制律**：双语主标题在一页中保持重点聚焦（Hero、`.ak-topbar`、主章节 `.ak-rule`）；成组列出的普通子标题或表格项不再逐行硬配灰色英文，避免满屏英文噪音。

### 5. 纯直角 `0px` 铁律、无辉光与极微选中标记
* **形状底线**：除正圆进度环（`.ak-ring`）、单选框、徽标胶囊（`.ak-badge`）与输入框 `2px` 极微倒角外，所有卡片、按钮、菜单、抽屉与焦点框一律 **`border-radius: 0`**；**严禁 45° 切角（`cut-tr`/`wedge-r`）与斜切平行四边形**（切角属于终末地）。
* **无辉光（No Glow）**：禁用霓虹外发光与大面积毛玻璃卡片；选中态靠**黑白反转（`.ak-btn--contrast` / `.ak-tabs--block`）、右上/左上小青色直角三角（`.ak-corner` / `.ak-thumb-card.is-active::before`）或左缘/底边实条**表达。
* **源石菱形（`◆`）仅限四处**：无序列表符号、加载指示器 `.ak-spinner`、时间线 `.ak-timeline` 节点、敌人威胁度评级。

### 6. 动效人格：硬切扫描（Scan & Wipe），禁用弹簧回弹
* 过渡短促干脆（`180ms–340ms`，`cubic-bezier(0.2, 0, 0, 1)`），悬停只做边框显影、箭头发梢位移或短实块延展，**不上浮、不放大、无弹性过冲**。
* 核心动效类（内置于 [`resources/prts-addons.css`](../../resources/prts-addons.css) 并遵守 `prefers-reduced-motion`）：
  * `.ak-anim-wipe`（`ak-wipe-x`）：左向右硬切擦入，用于 `.ak-hero--editorial__rule` 等标志性色条；
  * `.ak-anim-scan`（`ak-scan-in`）：自上而下硬朗揭示，用于展示标题与分节标尺；
  * `.ak-wave-btn.is-playing`（`ak-wave-eq`）：官网右上角 5 竖条终端信号声波指示动画。

---

## 三、 严格 DO / DON'T 审查清单

### ✅ DO
1. **黑框顶栏 + 亮暗双正典**：载体 1 用 `.ak-topbar`、载体 2 用 `.ak-header`；切换 `data-theme="dark | light"` 时，暗底不粘死黑、亮底保证文字/强调对比（小字标签用 `var(--ak-link)` `#0072A8`）。
2. **直角拼接 `border-image`**：需要做传统左 4px 色条 + 1px 细框面板或消息条时，沿用 `prts-design.css` 内置的 `border-image` 直角拼接，不产生浏览器 miter 斜角。
3. **整卡链接标 `.ak-not-prose`**：整块 `<a>` 的卡片/列表项避免正文 `a:visited` 染色污染。

### ❌ DON'T
1. **禁止未看需求就一律套 Wiki 侧栏 + 四框卡片**：非百科网站优先用载体 1 官网展示壳（`.ak-topbar` + `.ak-stage-shell` + `.ak-rule` / `.ak-folio-list`），告别套娃边框。
2. **禁止不可点击小标签用亮青色 `#18D1FF`**：眉题、属性名、英文副标用灰色 `--ak-fg-muted`，亮色下的小号强调文字用 `--ak-link` (`#0072a8`)。
3. **禁止表格内用 Bender 与伪造十六进制乱码**：微标行、版本号与日期必须真实可读（严禁 `0x7F3A` / `0xDEAD`）。

---

## 四、 色彩令牌速查表（`--ak-*`）

直接引入 [`resources/prts-design.css`](../../resources/prts-design.css) 与 [`resources/prts-addons.css`](../../resources/prts-addons.css) 即可获得全部令牌与双载体样式。

### 1. 语义令牌（随 `data-theme="light | dark"` 自动切换）

| 语义令牌 | 档案模式（Light） | 终端模式（Dark 默认） | 用途说明 |
| :--- | :--- | :--- | :--- |
| `--ak-bg-canvas` | `#f5f5f5` | `#0f0f10` | 页面画布底色（`.ak-bg-lattice` 在此基础上叠加三角网格与微光） |
| `--ak-bg-surface` | `#ffffff` | `#1a1b1c` | 卡片、表格、弹窗、缩略选卡表面 |
| `--ak-bg-surface-2` | `#f5f5f5` | `#232425` | 面板头部、表头、次级表面 |
| `--ak-bg-surface-3` | `#ebebeb` | `#2d2e30` | 按钮悬停、默认标签底、进度条轨道 |
| `--ak-bg-inset` | `#eef0f1` | `#141516` | 凹陷区域、只读输入框 |
| `--ak-bg-inverse` | `#1d1f20` | `#ffffff` | 黑白反转块底（强动作按钮、选中阶段页签） |
| `--ak-fg` | `#1d1f20` | `#f0f0f0` | 主文字颜色与核心建筑标尺实块色 |
| `--ak-fg-secondary` | `#454647` | `#c9c9c9` | 次要正文、导语、表头字 |
| `--ak-fg-muted` | `#626262` | `#8d8d8d` | 辅助说明、overline 小标签、英文副题、时间戳 |
| `--ak-fg-inverse` | `#ffffff` | `#181818` | 黑白反转块上的文字颜色 |
| `--ak-accent` | `#0098dc`（游戏蓝） | `#18d1ff`（官网青） | 主强调色：主按钮、选中边条、激活项、右轨大序号 |
| `--ak-accent-fg` | `#ffffff` | `#000000` | 主强调色块上的反色文字 |
| `--ak-link` | `#0072a8` | `#5ddcff` | 链接、情报分类小字、清单激活箭头（亮色保障 5:1+ 对比度） |
| `--ak-accent-2` | `#ffd800` | `#ffd800` | 次强调黄：通知计数徽标、星级、局部警示 |
| `--ak-border` | `#d9dbdc` | `#2f3133` | 1px 建筑分隔线、竖轨边线、常规细边框 |
| `--ak-info` / `--ak-success` / `--ak-warning` / `--ak-danger` | `#0072a8` / `#1f8f5f` / `#b86f00` / `#c8102e` | `#5ddcff` / `#4fd18f` / `#ffb340` / `#ff5c5c` | 四态语义文字/色条色 |

> **项目品牌换色接口**：保留黑白灰基底（`--ak-bg-*` / `--ak-fg-*`）与纯直角骨架，只需覆盖 `--ak-theme-accent` / `--ak-theme-accent-fg` / `--ak-theme-accent-subtle`（联动深黑容器：顶栏 `.ak-topbar` / `.ak-header`、`.ak-brief`、`.ak-news-card__band`、`.ak-showcase-col` 与页脚）与亮暗两态下的 `--ak-accent` / `--ak-accent-hover` / `--ak-accent-fg` / `--ak-link` / `--ak-focus`（联动画布主体：`.ak-hero--editorial__rule`、主按钮、去框指标短条、正文 `.ak-wave-btn` 与链接），即可切入网站自有品牌色。

### 2. 方舟专属领域令牌

* **稀有度色阶（1★ ～ 6★）**：`--ak-rarity-1` (`#bababa`) ～ `--ak-rarity-6` (`#ff9433`)，配 `--ak-rarity-1-text` ～ `--ak-rarity-6-text` 与 `data-rarity="6"` 自动注入。
* **技能技力（SP）回复色**：`--ak-sp-auto` (`#8ec31f`)、`--ak-sp-attack` (`#fc793e`)、`--ak-sp-hit` (`#f4af09`)、`--ak-sp-passive-recovery` (`#c289e3`)、`--ak-sp-passive` (`#808080`)。
* **游戏内富文本着色（`.ak-rt-*`）**：`.ak-rt-vup` / `.ak-rt-vdown` / `.ak-rt-rem` / `.ak-rt-kw` / `.ak-rt-imp` / `.ak-rt-enemy` / `.ak-rt-gild` / `.ak-rt-term`。

---

## 五、 字体与排版令牌

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;600;700&family=Noto+Sans+SC:wght@400;500;700;800&family=Oswald:wght@500;700&display=swap">
```

* `--ak-font-body`：思源黑体 / Noto Sans SC（正文、中文标题、表格数字）
* `--ak-font-display`：Novecento Sans Wide / Oswald（拉丁大写展示字、错位序号、去边框大指标数字，**必配 `font-variant-numeric: lining-nums`**）
* `--ak-font-label`：Bender / Chakra Petch（微标、日期 `2026 // 11 / 18`、代号）
* `--ak-font-mono`：系统等宽字体（代码、键帽 `.ak-kbd`）
