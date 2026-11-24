---
name: arknights-design
description: >-
  Use this skill whenever the user asks to design, initialize, build, or refactor a frontend website,
  web app, component, or UI boilerplate in Arknights style (明日方舟本家 PRTS 官网与终端档案风格) or
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
| **核心气质** | **官网冷峻建筑展示 + PRTS 终端（暗）/ 罗德岛制图档案（亮）** | **工业编辑风（Industrial Editorial）**——印出来的技术画册与测绘终端 |
| **色彩哲学** | **黑白灰炭为体、冰青为用**：暗底配官网冰青 `#18D1FF`，亮底配游戏蓝 `#0098DC`（小字链接 `#0072A8`）；黄黑条纹仅限警示；顶栏与页脚恒为深黑框 | **纸与墨是主体，信号黄是唯一焦点**：13 级纯中性灰 + 信号黄 `#FFFA00`（一屏黄面积 $\le 10\%$，白底严禁用黄字，用 `#6B5D00`） |
| **形状铁律** | **纯直角 `border-radius: 0`，严禁任何 45° 切角/斜切**；精选焦点击选角标用右上/左上直角三角；独立小图形仅 4 处用源石菱形 `◆` | **形状即语义**：面板/归档标签用直角，按钮统一 `4px` 微圆角，主要行动/机械控件用 `45°` 单角切角（`cut-tr`）或斜楔（`wedge-r`），头像/仪表用正圆，筛选/资源用胶囊 |
| **边框与层次** | **反套娃框**：官网展示载体靠三角暗格、`.ak-rule` 1px 标尺配实块、`.ak-folio-list` 底线与不对称错位双栏立住层次；百科面板才用 `1px` 细框 + `border-image` 色条直角拼接；无辉光 | **默认不围整圈边框**（统计块靠左缘 3px 墨线，提示条靠左缘 4px 色条，输入框用凹陷底 + 2px 底边线）；浮层用零偏移环境阴影 `0 0 <blur>` |
| **装饰母题** | 三角网格暗格 `.ak-bg-lattice`、贴边截断水印 `.ak-ghost-word`、右下反白斜暗卡片 `.ak-news-card`、硬切擦入 `.ak-anim-wipe`/`.ak-anim-scan`、声波条 `.ak-wave-btn`、半调网点 `.ak-halftone` | 斜纹镂空巨字（`ghost-hatch`）、滑块分节标题（`[███ ↘]`）、方括号姓名（`[ 名称 ]`）、CMY 注册色条、四角 L 形括号（`corner-brackets`）、等高线（`contour`） |

---

## 第二步：按需读取深度规范与拷贝静态资源（Progressive Disclosure）

确定目标体系后，**必须先用 `read_file` 阅读对应的两份基础手册（foundations + 母题/骨架）**；组件目录（components-catalog）体量较大，**仅在需要具体组件的 DOM/类名/ARIA 契约时再按需读取**，并将对应的 CSS 资源文件拷贝到目标前端项目中：

### 选体系 A（明日方舟本家 · PRTS Design）时：
1. **必读规范**：
   - [PRTS 基础设计规范与双载体/六原则/令牌表](./references/prts/foundations.md)
   - [PRTS 官网与终端双载体骨架、建筑母题与核心蓝图](./references/prts/decor-and-components.md)
   - [PRTS 全组件目录与交互蓝图](./references/prts/components-catalog.md)（**按需读取**：按钮、菜单/四态页签/分页、表单、弹窗/抽屉/Toast、进度/时间线/步骤条 五大类通用 UI + 方舟领域件完整蓝图 + `@fontsource` 离线字体配置，可直接跨框架移植）
2. **可直接拷贝到目标项目的样式资源**：
   - 上游完整样式底座（含令牌 + `.ak-scope` + 全部通用组件 + 方舟领域组件 + Wiki 骨架，零外部图片依赖）：[`resources/prts-design.css`](./resources/prts-design.css)
   - **官网架构升级与补丁层（必须紧随 `prts-design.css` 之后引入）**：[`resources/prts-addons.css`](./resources/prts-addons.css) —— 提供官网 `.ak-topbar`、`.ak-bg-lattice`、`.ak-stage-shell` + `.ak-index-rail`、`.ak-hero--editorial`、`.ak-rule`、`.ak-stat--minimal`、`.ak-folio-list`、`.ak-news-grid--staggered`、`.ak-showcase-strip`、硬切动画 `.ak-anim-wipe`/`.ak-anim-scan` 与上游兼容补丁；对 PRTS 的扩展均写在此处，勿直接改 `prts-design.css`
   - 仅需令牌变量时：[`resources/prts-tokens.css`](./resources/prts-tokens.css)
   - 样板与组件对照（仅作构图与交互结构参考，**严禁直接照搬测试业务文案与假数据**）：
     - 官网级整页构图样板：[`examples/prts-boilerplate.html`](./examples/prts-boilerplate.html)
     - Wiki 百科外壳 & 全组件交互目录：[`examples/prts-components.html`](./examples/prts-components.html)

### 选体系 B（明日方舟：终末地 · Endfield UI）时：
1. **必读规范**：
   - [Endfield 基础设计规范、六大原则与七大界面家族](./references/endfield/foundations.md)
   - [Endfield 母题工具类与核心展示组件](./references/endfield/motifs-and-components.md)
   - [Endfield 全组件目录与交互蓝图](./references/endfield/components-catalog.md)（**按需读取**：按钮/工具栏、三态页签、分页步骤、下拉/气泡、弹窗/抽屉/Toast、表单含菱形切换、表格/折叠/时间线、高阶选择器与测绘 HUD `Sparkline`/`TickRing`/`Viewfinder`/`Carousel` + 16 个关键帧与 17 个 `.animate-*` 动效类）
2. **可直接拷贝到目标项目的样式资源**：
   - 零依赖通用纯 CSS 版（含 `--ef-*` 亮/暗/反转三套令牌 + 全部母题类 + 全套 `.ef-*` 通用交互组件，适用于任意 HTML / Vue / React / Svelte 项目）：[`resources/endfield-standalone.css`](./resources/endfield-standalone.css)
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
2. **按载体搭建正统构图外壳**（**响应式是硬要求**：布局一律用内置类 `.ak-stage-shell` / `.ak-hero--editorial__grid` / `.ak-split` / `.ak-news-grid` / `.ak-showcase-strip` / `.ak-layout` / `.ef-hero__grid` / `.ef-split` / `.ef-grid-2` / `.ef-grid-3` / `.ef-stat-row` / `.ef-section`，**禁止写死内联 `grid-template-columns`**）：
   - **PRTS · 载体 1（官网/门户默认）**：采用「极简漂浮双语顶栏 `.ak-topbar` + 三角暗格斜光画布 `.ak-bg-lattice` + 右侧 1px 竖轨索引 `.ak-index-rail`（`01 // 01 / 04`）+ 开放 `.ak-hero--editorial` + `.ak-rule` 1px 标尺分割」，<1024px 隐藏右轨并切换左侧导航抽屉入口 `.ak-topbar__menu`。
   - **PRTS · 载体 2（Wiki/档案控制台）**：仅当需要强侧栏检索与长篇词条目录时，采用「`.ak-header` + `.ak-layout` + `.ak-sidebar` + `.ak-footer`」，<1120px 侧栏变抽屉（需 `.ak-local-nav__menu` + `.ak-drawer-scrim`）。
   - **Endfield**：采用「左侧窄轨 `.ef-side-rail`（底部配唯一主行动块 `.ef-nav-action`）+ 偏心构图主舞台（`1.5fr : 0.9fr` 不等宽分栏）+ 通栏信号黄色带标题 `.ef-band-title` 分隔亮暗版块」，<1024px 侧轨变顶部横轨，支持「纸白 / 烟黑」与 `[data-theme="inverse"]`。
3. **组合标志性母题与去边框构图（跨框架通用）**：
   - 拒绝千篇一律的“四方框卡片堆叠”！优先使用去框化机关建立呼吸感：
     - **PRTS**：组合 `.ak-ghost-word` 贴边裁切巨字、`.ak-brief` + `.ak-thumb-card` 选卡滑轨、`.ak-stat--minimal` 去框数字、`.ak-folio-list` 1px 分隔清单、`.ak-news-grid--staggered` 错位无框下文字情报卡、`.ak-showcase-strip` 四列暗幕竖切与 `.ak-anim-wipe`/`.ak-anim-scan` 硬切扫描；表格统一套 `.ak-table-scroll`。
     - **Endfield**：组合 `ghost-hatch`、`ef-section-title` 滑块标题、`ef-bracket-title` 方括号名、`ef-reg-strip`、`ef-stat` 左竖线统计块、`ef-data-row` + `.ef-sparkline`、`ef-item-slot` + `corner-brackets`。
   - 所有交互组件严格按 `components-catalog.md` 的 DOM 与 ARIA 状态契约（`.is-active` / `.is-open` / `aria-pressed` / `aria-selected` / `roving tabindex` / 原生 `<details>` / `<dialog>`）跨框架实现。
4. **弹性适配边界（主方向不可偏离，业务差异可随机应变）**：
   - **工程与基座底线（等价替代，不写死妥协）**：任何需求不得绕开 `--ak-*` / `--ef-*` 令牌与既有 `.ak-*` / `.ef-*` 基座重写平行皮肤；多栏扩展必须用带手机降维断点的 CSS 类实现，**严禁在 HTML 写死内联 `grid-template-columns`**；“硬核编号感”须用真实可读业务编号，**禁用 `0x7F3A` / `0xDEAD` 伪乱码**，并彻底替换非游戏业务中的样板专有词（如 `PERLICA`、`DIJIANG`、`TALOS-N07`、`北岭`、`罗德岛`）。
   - **品牌配色换皮（换强调不换骨）**：禁止整页铺满高饱和彩底或硬造拼贴活动皮肤，应通过语义令牌覆盖完成「90% 中性纸墨骨架 + ≤10% 品牌主色」映射——**PRTS** 覆盖 `--ak-theme-accent` / `--ak-theme-accent-fg` / `--ak-theme-accent-subtle` 与亮/暗 `--ak-accent` / `--ak-accent-hover` / `--ak-accent-fg` / `--ak-link` / `--ak-focus`（保留黑白灰画布与深黑顶栏）；**Endfield** 覆盖 `--ef-action` / `--ef-action-pressed` / `--ef-on-action` / `--ef-accent-ink` / `--ef-accent-ink-inverse`（中性灰阶画布至多微调冷暖倾向，按品牌色明度重设 `--ef-on-action` 与亮底深档 `--ef-accent-ink`）。
   - **业务可视化与布局扩展**：DAG 拓扑、测绘剖面 SVG、多维监控图等高阶领域模块随业务自由创作，继承对应体系色彩与字体变量并兼容亮暗双主题与 390px 响应。
   - **外观偏好的有条件让步**：默认严格遵守第四步质感红线；仅当用户**明确坚持**特定局部表现时，才允许以**局部自定义扩展类**做最小化派生并提示偏离，**禁止借“破例”将整站改造成通用发光圆角 SaaS**。

---

## 第四步：交付前的人类级视觉自检清单（Self-Audit）

在完成代码编写后，逐条对照以下红线自检，任何一条违规必须立即修正：

- [ ] **是否混淆了两套系统的形状与边框纪律？**
  - PRTS 严禁任何 `45°` 切角或圆角卡片，禁用把所有数据块、清单都套进四边 `1px` 套娃盒里的呆板做法，黄黑条纹只留给危险提示；
  - Endfield 严禁四角全切八边形，切角只用于行动/机械控件，且可聚焦按钮的切角必须画在 `::before` 上以保留焦点环。
- [ ] **颜色对比度与面积预算是否合规？**
  - PRTS 不可点击小标签（eyebrow / 英文副标）严禁亮青（必须 `--ak-fg-muted` 灰色），亮色下小字彩色分类用 `--ak-link` (`#0072a8`)；
  - Endfield 的信号黄 / 品牌填充色控制在全屏面积 10% 以内，亮底文字强调必须使用深档 `--ef-accent-ink`（默认 `#6B5D00`）。
- [ ] **数字、双斜杠日期与英文排版是否克制且真实？**
  - PRTS 的 `<table>` 数字列是否使用正文字体 + `tabular-nums`（严禁表格内用 Bender）？日期可使用 `YYYY // MM / DD` 等宽对齐；成排普通标题不再逐个强配英文副标；
  - 微文字是否为真实可读的栏目名、日期、版本号、节点编号（严禁 `0x7F3A`、`0xDEAD` 及非游戏项目残留 `PERLICA` / `DIJIANG` / `TALOS-N07` / `北岭` / `罗德岛`）。
- [ ] **是否杜绝了通用 SaaS / 科幻俗套（并守住主基调）？**
  - 默认严禁大圆角（`8px–16px`）投影卡片、悬停上浮放大、毛玻璃发光霓虹边与六边形蜂窝网格。

---

## 第五步：渲染验证（硬性门槛，不通过不得交付）

规则自检只能查“写了什么”，查不出“长什么样”。接入业务项目并编写完成后，交付前**必须真的渲染**（桌面 1440px + 手机 390px × 亮/暗 4 张图）并人工/视觉看图：

```bash
google-chrome --headless=new --no-sandbox --hide-scrollbars --window-size=1440,1300 --virtual-time-budget=6000 --screenshot=desktop.png file://$PWD/index.html
google-chrome --headless=new --no-sandbox --hide-scrollbars --window-size=390,2400  --virtual-time-budget=6000 --screenshot=mobile.png  file://$PWD/index.html
```

逐项检查，任一项不过必须修复：
- [ ] **无文字重叠/被裁切**：`ghost-hatch`（Endfield）或 `.ak-ghost-word`（PRTS）只能是极低透明背景层，与前景标题、面包屑、图标互不遮挡阅读；
- [ ] **手机 390px 无横向溢出**、主内容可见、表格不被挤成逐字竖排（宽表格套 `.ak-table-scroll`）；
- [ ] **亮/暗两套主题下所有按钮、文字对比度足够**（尤其恒深黑顶栏、Hero 与 `.ak-brief` 区块内的对比文字与按钮）；
- [ ] **没有大面积纯色或空洞占位块**；
- [ ] 主题切换按钮初始状态与 `data-theme` 一致，并持久化用户选择。
