# AGENTS.md — 协作规范与项目记忆

> 面向所有在本仓库工作的 AI 助手与人类协作者（Antigravity / Claude Code / Cursor / Codex）。
> **改动前先读本文件；改动后更新第四节“项目记忆”。** 语言：中文为主，代码与标识符保持英文。

## 一、项目是什么

`arknights-design`：一个面向 AI 编码助手的前端设计 **Skill**，包含两套**互相正交**的设计体系：

| 体系 | 前缀 | 气质 | 形状铁律 |
| :--- | :--- | :--- | :--- |
| A · PRTS Design（明日方舟本家） | `.ak-*` / `--ak-*` | 黑白为体、青为用；档案(亮)/终端(暗) | 纯直角，**严禁 45° 切角**，无辉光 |
| B · Endfield UI（终末地） | `.ef-*` / `--ef-*` | 工业编辑风；纸与墨 + 信号黄 | 形状即语义；切角只给行动/机械控件 |

入口：[SKILL.md](./SKILL.md)。结构说明：[README.md](./README.md)。

> **当前分支定位（`suite/endfield`）**：本分支基于 `main`（`v1.4` 通用基座）独立演进**《明日方舟：终末地》特色活动/区域/阵营专题子 Skill 套组**（位于 [`suites/endfield/`](./suites/endfield/README.md)）。**不动 `main` 通用基座的核心铁律**；每个专题子 Skill 必须完全自包含、采风先行并遵守 [`suites/endfield/SUITE_SPEC.md`](./suites/endfield/SUITE_SPEC.md)。

## 二、目录职责与“谁能改什么”

| 路径 | 性质 | 规则 |
| :--- | :--- | :--- |
| `suites/endfield/**` | **终末地专题子 Skill 套组** | ✅ 本分支主力工作区；遵循 [`suites/endfield/SUITE_SPEC.md`](./suites/endfield/SUITE_SPEC.md)，`_template/` 仅作脚手架不打包 |
| `resources/prts-design.css` `prts-tokens.css` `endfield-theme.css` | **上游同步生成** | ❌ 不要手改；由 `scripts/sync-upstream.py` 覆盖 |
| `resources/prts-addons.css` | 本仓库自有升级与补丁层 | ✅ 对 PRTS 上游修正及官网展示载体扩展均写这里，紧随 `prts-design.css` 引入 |
| `resources/endfield-standalone.css` | **手工维护** | ✅ 可改；末尾“Skill 补丁层”区块为本仓库自有，同步/合并时勿丢 |
| `references/**` | 规范文档 | ✅ 规则变更必须同步改文档，文档与 CSS/样板不得矛盾 |
| `examples/**` | 整页样板 | ✅ 必须通过第三节的渲染验证 |
| `SKILL.md` | Skill 总入口 | ✅ 保持精炼；新增硬规则放“第四步/第五步” |
| `scripts/verify.py` | 校验与回归门禁 | ✅ 新增/修改组件、动效或文档类名时须同步扩展探针与校验 |
| `scripts/package-release.py` | Skill 发布打包脚本 | ✅ 修改 Skill 资源/规范后重跑以更新 `release/` |
| `release/**` | **打包脚本生成** | ❌ 不要直接手改包内副本；统一改根目录源文件后重新运行 `package-release.py` |
| `LICENSE` `NOTICE.md` | 许可 | ✅ 引入新上游时同步更新 NOTICE |

## 三、工作流程（硬性）

1. **先读后改**：改任一体系前，先读对应 `references/*/foundations.md`，确认不违反该体系铁律；**严禁把 A、B 两套规则混用**。
2. **布局只用类，不写死内联 grid**（`.ak-layout`、`.ef-hero__grid`、`.ef-split`、`.ef-stat-row`、`.ef-section`）。新增布局必须带手机断点。
3. **改了 CSS / 样板 / 规范，必须渲染验证**（不能只“看代码觉得对”）：
   ```bash
   # 在仓库根目录一键运行：静态类/链接/关键帧检查 + 1440px/390px 亮暗全页渲染 + Chrome 实时动效/交互探针
   python3 scripts/verify.py --render --out /tmp/arknights-verify
   ```
   检查清单见 [SKILL.md 第五步](./SKILL.md)：无文字重叠/裁切、390px 无横向溢出、亮暗对比度、无纯色占位块。
4. **规则 ↔ 实现一致**：SKILL.md / references 里写的类名必须在 CSS 里真实存在（`python3 scripts/verify.py` 会比对样板与文档中的 `.ak-*` / `.ef-*` 类及 `@keyframes`）。
5. **小步提交**：一个主题一个 commit，信息用 `feat|fix|docs|chore: 简述`。**不要未经用户要求就 commit / push。**
6. **字体作为一等视觉设计维度（且零商业侵权资产）**：不引入鹰角官方位图与商业字体，但**绝不能只把字体当合规回退草草带过**。每套体系或专题子 Skill 必须按真实气质独立定义四层字体角色（展示巨字 Display / 中文标题与正文 CJK / 技术编号与等宽数据 Mono·Tabular / 装饰副标 Accent），明确字重、字宽（Condensed/Extended）、字距与衬线/无衬线选型，选用合法开源字体并同时提供 Google Fonts + `@fontsource` 离线自托管与系统回退链；渲染验证时须确认目标字体真实生效。
7. **视觉语言与网站原型解耦（反“万物皆控制台”惯性）**：设计系统定义的是配色、字阶、几何、节奏与交互质感，**不等于只能做后台控制台/监控面板**。必须先识别用户的真实网站类型（官网落地页 / 长文博客与文档 / 作品集与商品画廊 / 登录表单与专题页 / 控制台工作台），再挑选匹配的空间骨架与组件；非后台场景严禁硬塞侧边监控栏、KPI 指标卡、实时状态灯或数据表。
8. 回复保持简洁；引用文件用相对链接。

## 四、项目记忆（Project Memory）

> 追加式。每条：日期 · 现象 → 根因 → 处理 → 防再犯。

### 2026-11-16 · 首次质量审查与修复（渲染 1440px / 390px × 亮暗）

| # | 现象 | 根因 | 处理 | 防再犯 |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Endfield 首屏巨字 `#PERLICA` 与面包屑/标题叠压、顶部被裁 | 巨字 `top:-16px` 与内容层同位；内容层无让位 | 新增 `.ef-hero` / `.ef-hero__ghost` / `.ef-hero__grid`（`padding-top = --text-ghost × .65`，内容 z-index:1） | SKILL 第五步“无重叠”检查；references 增“防重叠布局”附录 |
| 2 | 两个样板手机端不可用（Endfield 内容整屏不可见；PRTS 内容被挤成竖排） | Endfield 侧轨 `100vh sticky` 且 `1fr` 被内容撑破；PRTS 内联 `200px 1fr` 覆盖了响应式 | Endfield <1024 侧轨改顶部横轨、列用 `minmax(0,1fr)`、新增响应式布局类；PRTS 去掉内联 grid，补抽屉入口 `.ak-local-nav__menu` + 遮罩，表格包 `.ak-table-scroll` | 禁止内联 grid；必须截 390px 图 |
| 3 | PRTS 亮色模式 Hero 内“开始行动”黑底黑字几乎不可见 | `.ak-btn--contrast` 随主题反转，而 Hero 恒黑 | `prts-addons.css`：`.ak-hero .ak-btn--contrast` 恒白底黑字 | 恒深色区域内的反转按钮要单独检查亮暗两主题 |
| 4 | PRTS Hero 右侧大块纯青色像占位图 | 上游 `.ak-hero__side` 实心 `#18D1FF @ .9` | addons：右缘 8px 青条 + 渐隐网点，支持放 `<img>` | 禁止大面积纯色占位块 |
| 5 | 规范与实现不符：字体 Bender/Novecento 未附带；Google Fonts 在大陆可能不可达 | 商业字体不能分发；仅在线字体 | SKILL.md 增“字体说明”（回退链 + 自托管建议） | NOTICE 写明字体授权由使用者自行获得 |
| 6 | 自检清单只查规则不看渲染，漏掉 1-4 | 流程缺口 | SKILL.md 新增“第五步：渲染验证” | 本文件第三节第 3 条 |
| 7 | 风格路由对“只说明日方舟风格”有歧义 | 文案“询问或提供对比”不确定 | 改为：先确认；无法提问默认体系 A 并声明假设 | — |
| 8 | 文案日文残留 `必ず`；主题按钮初始态写死且不持久化 | 笔误 / 样板简化 | 改为“必须”；两样板主题用 localStorage 持久化，`aria-pressed` 同步 | — |
| 9 | `sync-upstream.py` 不生成 `endfield-standalone.css`，README 暗示全是同步产物 | 该文件为手工维护 | 脚本头部注释与本文件第二节写明 | 合并上游更新时人工比对 |
| 10 | 缺 LICENSE / NOTICE | 仅 README 提及 MIT | 新增 `LICENSE`、`NOTICE.md` | 引入新上游时更新 NOTICE |

### 2026-11-16 · 二次互审补全（Antigravity Chrome 实渲染 8 图 + 文档一致性校验）

| # | 现象 | 根因 | 处理 | 防再犯 |
| :-: | :--- | :--- | :--- | :--- |
| 11 | `references/prts/decor-and-components.md` 第 3 节仍写死内联 `grid-template-columns: 200px minmax(0, 1fr)`，且遗漏 `prts-addons.css`、`.ak-local-nav__menu`、`.ak-drawer-scrim`、`.ak-table-scroll` | 文档未随首次修复同步 | 改用纯类 `.ak-layout` 并补齐 `prts-addons.css` 与抽屉/滚表结构 | 改示例或规范后同步检查正文片段 |
| 12 | PRTS 桌面页眉搜索快捷键 `/`（`.ak-search__kbd`）浮到整行最右（`终端 (Dark)` 右侧） | 上游 `.ak-search__kbd` 为 `position: absolute`，而 `.ak-search-trigger` 为 `inline-flex` 且未设 `position: relative` | `prts-addons.css` 设 `.ak-search-trigger { position: relative; }` 并将内嵌 `.ak-search__kbd` 改为流式贴右；同步收窄手机端 `.ak-header .ak-seg` 按钮内边距、精简 `DEPLOYED // 编队` 标签防单字折行 | 新增组件变体时检查 `.ak-*` 绝对定位锚点与 390px 换行 |
| 13 | Endfield 亮色模式下，局部暗色面板 `DIJIANG` 的四角括号（`.corner-brackets`）在白纸背景上“隐身” | 面板内 `[data-theme="dark"]` 将 `--ef-ink` 覆写为 `#fafafa`，而 `::after` 位于外扩 `-4px` 的白色宿主画布上 | `endfield-standalone.css` 新增 `--ef-page-ink`；`:not(html)[data-theme].corner-brackets::after` 默认读取 `--ef-page-ink` | 异色局部容器若带外扩装饰（`inset < 0`），颜色须取宿主层令牌 |
| 14 | Endfield 390px 手机端黄色色带 `.ef-band-title` 右侧 `SECTION 02 OF 03 / PIPELINE TELEMETRY` 被裁切 | `.ef-band-title` 未允许换行且 `--text-3xl` 在 390px 过宽，超出部分被 `overflow: hidden` 截断 | `endfield-standalone.css` 为 `.ef-band-title` 补 `flex-wrap: wrap` 与 `<768px` 缩字号/内边距，新增 `.ef-band-title__meta` | 含 `overflow: hidden` 的横幅必须配 `flex-wrap` 与窄屏字阶 |
| 15 | Endfield `纸白`/`烟黑` 按钮未体现当前激活态；两样板首次加载若无 `localStorage` 不主动同步 `aria-pressed` | `aria-pressed` 仅在点击回调更新，且 Endfield 按钮未绑状态样式 | 两样板拆出 `applyTheme(theme, persist)` 从 `dataset.theme` 同步状态；`endfield-standalone.css` 补 `.ef-btn[aria-pressed]` 样式 | 主题开关须支持“DOM 预置状态即按钮状态” |

### 2026-11-16 · 跨框架通用组件库大而全扩充（双体系 Catalog + 交互陈列页 + 实渲染复核）

| # | 现象 | 根因 | 处理 | 防再犯 |
| :-: | :--- | :--- | :--- | :--- |
| 16 | Endfield 此前仅覆盖少量页面展示组件，缺少全套可脱离 React 直接移植的菜单/表单/反馈/数据组件 | 上游为 `@endfield-ui/react`，未在独立 CSS 中全量展开 | 在 `endfield-standalone.css` 补齐 8.1–8.6 全套样式与 `.ef-grid-2` / `.ef-grid-3` 等响应助手，并新增 `references/*/components-catalog.md` 与 `examples/*-components.html` | 文档/目录同步列出“框架无关语义状态钩子” |
| 17 | `<header class="ef-panel__head" data-theme="inverse">` 亮色下白底白字不可见（同时影响 `endfield-boilerplate` 与 `endfield-components`） | `.ef-panel__head` 读取 `--ef-surface-inverse` / `--ef-ink-inverse`，而 `data-theme="inverse"` 内部已做过一次反转，导致二次反转回宿主同色 | `endfield-standalone.css` 新增 `.ef-panel__head[data-theme="inverse"]` 直接读取 `--ef-surface` / `--ef-ink` / `--ef-accent-ink` | 凡自带 `[data-theme="inverse"]` 作用域的反转块，须区分作用域内外令牌 |
| 18 | `.ef-switch-dual` 首选项 `2D` 无法高亮；暗色分页禁用左钮融入背景；`.ef-avatar` 多字折行 | `.ef-switch-dual__knob` span 干扰 `:first-of-type` 命中；暗色 `--ef-disabled` 与分页 `--ef-surface-muted` 同为 `#282828` | 改为显式 `.ef-switch-dual__opt--off/--on`；覆盖 `.ef-pagination .ef-icon-btn:disabled` 底色；`.ef-avatar` 加 `line-height: 1; white-space: nowrap;` | 同父级含装饰节点时禁止依赖 `:first-of-type`；同色调容器内检查禁用态对比度 |
| 19 | `.ef-completion-banner__word` 大字描边 `COMPLETED` 压在黄底 CTA 按钮前方；`.ef-flyout__item` 暗条字符对比偏弱 | `position: absolute` 节点在 DOM 后方且未分 `z-index` 层级 | 内容节点设 `z-index: 1`、水印设 `z-index: 0`；`.ef-flyout__item` 提亮至 `#fafafa` | 含背景大字水印的横幅必须在 CSS 明示 `z-index` 前后层级 |
| 20 | PRTS `<button class="ak-menu__item">` 受基础按钮样式残留边框，且 `<hr class="ak-divider--text">` 无法承载文字标签 | `ak-menu__item` 用 `<button>` 继承基础按钮样式；`<hr>` 为空元素不能放文本 | `prts-addons.css` 对 `.ak-menu .ak-menu__item` 去框去底；文字分割线规范改为 `<div class="ak-divider ak-divider--text"><span>…</span></div>` | 文档示例统一用真实可渲染标签验证后再收录 |

### 2026-11-16 · 组件库审查修复（实渲染 + 行为测试：键盘、抽屉焦点、遮罩）

| # | 现象 | 根因 | 处理 | 防再犯 |
| :-: | :--- | :--- | :--- | :--- |
| 21 | PRTS 右侧抽屉在桌面端无遮罩、点外部关不掉 | `prts-addons.css` 把 `.ak-drawer-scrim.is-open` 限定在 <1120px | 遮罩改为所有宽度生效 | 通用浮层的辅助元素不要绑定“只为某断点写”的媒体查询 |
| 22 | `.ak-drawer` 关闭态可被 Tab 聚焦，阴影漏到视口右缘 | 只靠 `transform` 移出屏幕，缺 `visibility:hidden` | addons：`.ak-drawer:not(.is-open){visibility:hidden;box-shadow:none}`，收起时延迟隐藏；两页抽屉补 `role="dialog" aria-modal`，打开聚焦首个按钮、关闭还焦点 | 屏幕外元素必须同时退出无障碍树与 Tab 序 |
| 23 | Tabs 只有 `role="tab"`，缺 `aria-controls`/`aria-labelledby`、roving `tabindex`、方向键 | 示例只绑了 click | 两页示例与两份 catalog 补齐 ARIA 契约，`initTabs()` 支持 ←→/↑↓/Home/End；已用脚本模拟键盘验证 | catalog 的 HTML 片段必须是“可原样复制且合规”的完整片段 |
| 24 | SKILL.md 写“34 类”无依据；必读手册由 2 份变 3 份，体量过大 | 夸大描述；组件目录被当成必读 | 改为“五大类”；组件目录改为**按需读取**，必读仅 foundations + 母题/装饰 | 数量类描述须可核对；渐进式披露中大文件默认按需 |
| 25 | PRTS 手机端分区标题孤字（“标”单独成行）；暗色下屏蔽词是刺眼白条 | 标题无均衡断行；上游遮盖条取 `--ak-fg` | addons：`text-wrap:balance`、英文副标 `nowrap`、编号 `flex:none`；暗色屏蔽词改深灰条 | 双语标题+右侧编号的组合须检查窄屏换行 |
| 26 | Endfield 陈列页一排无文字的小徽章看不出是什么组件 | 只摆了组件，没有标注 | 拆成带微标注的 `.ef-demo-cell`（仅陈列页内样式） | 陈列页每个组件必须有可读名称 |
| 27 | Endfield 分页 `01 / 12` 斜纹底显脏 | 在灰底叠斜纹，又配灰色禁用钮 | `.ef-pagination` 去掉斜纹，纯色底 | 斜纹只用于有明确语义的位置（标题带/抽屉头） |

### 2026-11-16 · 上游全量对照补齐、动效监控与自动化视觉校验

| # | 现象 | 根因 | 处理 | 防再犯 |
| :-: | :--- | :--- | :--- | :--- |
| 28 | 对照上游发现 Endfield 缺 8.7–8.8 控件及 `foundations.md` 已承诺的 `Sparkline`；两份目录漏录多组内置类（`.ef-top-bar`/`.ef-toc`/`.ef-tooltip`/`.ak-loader`/`.ak-skeleton`/`.ak-fab`/PRTS 领域件蓝图）；`endfield-boilerplate` 缺 `Sparkline` 与完整 Footer | 上轮按通用组件归类扩展，未逐项比对上游源码模块与目录索引 | 在 `endfield-standalone.css` 补全 8.7–8.8 全套组件、`endfield-boilerplate.html` 嵌 `Sparkline` 与 `.ef-footer`，扩充双目录（含 `@fontsource` 引入方案）及两份陈列页；新增 `scripts/verify.py` | 每次增删组件或同步上游后跑 `python3 scripts/verify.py` 校验类覆盖与文档链接 |
| 29 | Endfield 动效存在缺漏：`ef-indeterminate-y` 与 8 个 `.animate-*` 类缺失；`SectionTitle` 的 `↘` 未包裹导致三段式旋转不触发；`ef-menu::before`、View Transitions 缺位；`[data-ef-tip]` 改 `display` 触发 reflow | 早期只搬运了 7 个动画类，未逐行对照上游 `motion.md` 与 `theme.css` | 补齐 16 `@keyframes` + 17 `.animate-*` + `View Transitions`；包裹 `.ef-section-title__block > span` 触发 `100ms` 旋转与 `200ms` 标题淡入；升级非对称聚焦线、`.ef-completion-banner` `wipe-in` 及零 reflow `[data-ef-tip]` | `verify.py` 强制校零缺失/零闲置 `@keyframes`、`prefers-reduced-motion` 及 Chrome 实时 `animationName` 探针 |
| 30 | 两套组件陈列页 Dropdown 仅支持点击触发器开关，无点击外部关闭与方向键导航 | 上轮遗留为轻量展示脚本 | `endfield-components.html` 与 `prts-components.html` 补齐点击外部关闭、`ArrowUp`/`ArrowDown` 与 `Esc` 归还焦点，并在两份 catalog 明示契约 | `verify.py --render` 内置点击外部关闭与 Tabs 键盘实测探针 |
| 31 | `endfield-components.html` 第 5 节 1440px 下 `.ef-schedule` 被 `.ef-calendar` 挤成窄列竖排；`.ef-viewfinder` 四角读数与 `TickRing` 间距偏紧 | `.ef-calendar` 与 `.ef-schedule` 共处半栏 `.ef-row` 宽度不足；`.ef-tick-ring` 默认 `168px` 与内边距叠加 | 第 5 节右栏改用 `.ef-stack` 纵向排布；`.ef-viewfinder` 内边距调至 `46px 28px`、角标内移 `10px`，演示环 `--_s: 112px` | 固定列宽组件（日历）勿与文本列表硬塞同排 `.ef-row`，改后必须看 1440px 实渲染图 |
| 32 | 390px 手机端 `.ef-viewfinder` 四角括号、角标读数与内嵌 `[ REC ]` 全部消失；`prts-components.html` 在 375px–390px 下顶栏 `.ak-header__tools` 超出视口 2px | `@media (max-width: 639px)` 无条件隐藏了 `.ef-viewfinder__corners` 与 `.ef-viewfinder__ro`；`PRTS.COMPONENTS` 15 字符品牌词配 `.ak-seg` 按钮在 375px 下总宽达 377px | 默认保留 `.ef-viewfinder` 四角与读数（`<480px` 微调内边距与字号，仅 `.ef-viewfinder--compact-mobile` 修饰类才隐藏）；`prts-addons.css` 收紧 `<640px` 顶栏分段钮至 `padding: 0 7px; font-size: var(--ak-fs-xs)` | 窄屏媒体查询勿一刀切隐藏核心演示特征；长品牌词页面须测 375px 宽度溢出 |
| 33 | `endfield-components.html` 的 Combobox 输入框按 `ArrowDown` 无法聚焦下拉项；Carousel 仅按钮点击更新页码，原生横向滑动不同步 | 键盘监听仅绑在 `.ef-menu` 内部；`#ef-car-track` 未监听原生 `scroll` 事件 | 为 `#ef-combo-in` 补齐 `ArrowDown`/`ArrowUp` 展开并聚焦首尾可选项；为 `#ef-car-track` 增加被动 `scroll` 监听同步 `01/03` 计数与标题；`verify.py` 增补 `comboArrowOk` 与 `noOverflow` 探针 | 声明支持键盘或原生 `scroll-snap` 同步的控件必须绑定对应事件并纳入探针 |
| 34 | 真实 `cw=360px` 极窄屏下 `endfield-boilerplate.html` `.ef-stat`（370px）与 `prts-components.html` 页眉/分页栏（369–370px）仍溢出；`endfield-components.html` Combobox 过滤后按上下键会命中隐藏项，且选定/按 `Esc` 归还焦点会触发 `focus` 立即重开 | 无头 Chrome `--dump-dom` 将窗口夹紧至 485px 掩盖窄屏实宽；`endfield-boilerplate` 内联 `font-size: var(--text-5xl)` 覆盖了 `14vw` 断点规则；`.ak-pagination` 缺换行与 `<420px` 品牌字号收敛；菜单键盘监听未跳过 `display:none`，且 Combobox `focus` 监听未区分程序性焦点归还 | `endfield-standalone.css` 增 `.ef-stat__value--xl` 与 `.ef-stat__main` 折行并移除内联字号；`prts-addons.css` 增 `<420px` 品牌字阶/缩容与 `.ak-pagination{flex-wrap:wrap}`；`endfield-components.html` 过滤隐藏菜单项并为选定/`Esc` 归还焦点加 `skipOpen` 保护；`verify.py` 增同源 `375px/390px` iframe 实测 | 移动端溢出探针须在不受桌面最小窗宽夹紧影响的受控视口中校验；带 `focus` 自动展开的输入框在归还焦点时须防重开 |
| 35 | `SKILL.md` 第五步包含本仓库专用 `scripts/verify.py` 链接与“同步脚本”措辞，下游项目单独拷贝 Skill 文件夹时会形成断链并误导弱模型去运行不存在的校验脚本 | 上轮未区分“仓库研发视角”与“下游测试项目运行时视角”，且缺独立发布目录 | 清理 `SKILL.md` 中的仓库维护专有措辞（保留在 `README.md`/`AGENTS.md`），新增 `.gitignore` 与 [`scripts/package-release.py`](./scripts/package-release.py)，打包零冗余的 [`release/arknights-design/`](./release/arknights-design/) 与 `release/arknights-design.zip` 并校验包内零断链、零维护文件泄露 | 下游入口文档 `SKILL.md` 严禁引用 `scripts/` 或 `AGENTS.md` 等维护态文件；每次发布测试包一律用打包脚本校验 |
| 36 | 下游用 DeepSeek 4.1 flash 跑通 `test-01`~`test-04` 四项冷启动盲测：前 3 项体系还原度与 ARIA 交互全过（仅 `test-03` 残留 `北岭` 地名），`test-04` 冲突压测因以“按需求破例”让步，直接丢掉 `.ak-*` 基座、放行 `style="grid-template-columns"`、`0x7F3A` 及 `RHODES ISLAND` | 此前 `SKILL.md` 未区分“可随机应变的局部视觉衍生”与“不可破例的工程/基座/脱敏底线”，导致模型面对用户显式偏离指令时全盘放弃底座 | 在 `SKILL.md` 第三步新增第 4 项「弹性适配边界」并同步细化第四步自检：锁定等价实现三底线（基座组件复用、响应式 CSS 类代内联 grid、样板专有词黑名单），明确领域图表/SVG 开放拓展与用户显式偏好仅限局部派生、不偏离主视觉方向；重打包 `release/` | 业务自定义需求统一收敛为“主骨架/令牌不丢 + 局部扩展类派生”，禁止绕开基座或用内联布局妥协 |
| 37 | 下游业务站点需接入自有品牌配色时，上游 `.ak-hero__*` / `.ak-switch` 仍直读 `--ak-cyan-500` / `--ak-blue-600`，Endfield `.ef-hazard` / `.ef-data-row__val--accent` / `.ef-toast__tone` / 暗态 `--ef-focus` / `.ef-btn--action::after` 未联动品牌令牌，且规范未写明换色边界 | 早期配色只针对官方青/信号黄，未在文档与补丁层显式暴露“换强调不换骨”覆盖清单 | `prts-addons.css` 让 `.ak-hero__*` 改读 `--ak-theme-accent`、`.ak-switch > input:checked` 改读 `--ak-accent`；`endfield-standalone.css` 让 `.ef-hazard` / `.ef-data-row__val--accent` / `.ef-toast__tone` 联动 `--ef-action`、暗/反转态 `--ef-focus` 联动 `--ef-accent-ink(-inverse)`、`.ef-btn--action::after` 改读 `currentColor`；在 `SKILL.md` 及两份 `foundations.md` 写入品牌换色令牌清单与对比度约束，并在 `verify.py` 增加 `release/` 同步校验后重打 `release/` | 品牌换色一律通过语义令牌覆盖完成，保留 90% 中性纸墨基底并同步校验 `--ef-on-action` / `--ef-accent-ink` 对比度与 `release/` 一致性 |

### 2026-11-17 · 官方活动 6 系列视觉体系提炼与总成样板（`regulation` / `anniversary` / `sui` / `exhibition` / `brawl` / `theater`）

| # | 现象 | 根因 | 处理 | 防再犯 |
| :-: | :--- | :--- | :--- | :--- |
| 38 | 基于官网 2019–2026 海报档案扩展 6 套系列模板后，初轮 `verify.py` 暴露 4 处不存在工具类/文档类名（`ak-items-stretch`/`ak-mt-3`/`.ak-link`）；实看 390px 渲染图发现周年/剧场页 `.ak-tabs--block` 右侧裁切、波普页 `.ak-panel__head` 配 3 枚 `.ak-btn-group` 按钮时标题被挤压折行；暗色下 `.ak-brawl-poster` 内置 `--ak-accent` 原为亮黄需独立锁黑对比 | 样式未检查窄屏下 `.ak-tabs--block` 与带按钮组面板头换行；明黄海报区内部令牌未同时覆盖 `--ak-accent`/`--ak-bg-surface-2`；手写类名未对照 `prts-design.css` utilities | 新增 [`resources/prts-series.css`](./resources/prts-series.css)、[`references/series/event-series-templates.md`](./references/series/event-series-templates.md) 及 6 份脱敏交互样板 [`examples/series-*.html`](./examples/series-regulation.html)；锁死 `.ak-brawl-poster` 内部黑黄对比与 `[data-ak-series="exhibition"]` CMY 对比；`<640px` 为 `[data-ak-series]` 补 `.ak-tabs--block` 与 `.ak-panel__head` 换行；扩展 `verify.py` 覆盖 `prts-series.css` 动画/类、6 套样板脱敏黑名单、40 张亮暗渲染图及 Chrome 交互探针并重打 `release/`（全部通过） | 新增系列层必须在 `verify.py` 注册动画与 375/390/1440 渲染探针；带按钮组的 `.ak-panel__head` 与 3 项以上 `.ak-tabs--block` 窄屏默认允许换行 |

### 2026-11-17 · 1.1 活动系列美学审查修复（`sr-*` 40 图复核）

| # | 现象 | 根因 | 处理 | 防再犯 |
| :-: | :--- | :--- | :--- | :--- |
| 39 | `series-regulation` / `series-exhibition` 用整块等距菱形 SVG 作拓扑/展位地图，节点标签相互压叠；`series-theater` 带框菱形幕次徽章、`series-anniversary` Hero 菱形线稿，均越过「源石菱形仅限 4 处」与 PRTS 形状铁律 | 系列扩展时按“海报感”引入了等距/菱形母题，未回对 `foundations.md` | 地图改为直角矩形节点 + 连线；`.ak-emblem-diamond` 改为直角 `.ak-act-mark`；Hero 线稿改矩形；展位页补操作按钮消除右栏空白；文档新增系列页形状红线 | `verify.py` 静态扫描 `series-*.html` 禁 `<polygon>`/`rotate(45`/`clip-path` |
| 40 | 亮色模式下系列 Hero（恒深色）眉题用亮态强调色，对比度约 2–3:1；径向渐变近似“晕光” | `.ak-hero__eyebrow` 读 `--ak-theme-accent`，亮态值偏深 | 各系列 `.ak-hero` 内锁定暗态强调色；径向渐变改线性渐变 | 恒深色容器内必须覆盖主题强调令牌（同第 3 条） |
| 41 | `COMPLETED` 水印被奖励 chip 压住截断；样板泄漏 `WAI-ARIA TABS/REPERTORY` 开发术语；面板头逐个双语；390px 统计标签孤字折行 | 水印写死 `right:92px`；标签借用实现名；文案未精简 | 水印改 flex 项；术语替换为业务文案；去掉多余英文副标并缩短统计标签；`verify.py` 增 `wmClear` 探针与术语扫描 | 绝对定位装饰必须相对真实兄弟元素让位 |

### 2026-11-24 · 清理独立皮肤模板并依据 `ak.hypergryph.com` 实测重塑本家主体系

| # | 现象 | 根因 | 处理 | 防再犯 |
| :-: | :--- | :--- | :--- | :--- |
| 42 | 对比 Endfield UI 与开启 SwiftShader WebGL 后的明日方舟官网 [`ak.hypergryph.com`](https://ak.hypergryph.com/#index) 全 8 屏实机画面后，确认此前的 6 套 `series-*` 活动皮肤与独立专题 `cc-*` 模板均陷于“拿单张海报封面硬拼 CSS 框/SVG 道具、全套同质化盒状结构”，且主 PRTS 样板锁定在 MediaWiki 侧栏与套娃边框中（“只能看但缺少建筑感”） | PRTS 上游源于 `MooncellWiki/prts-design` 百科皮肤，缺失 `ak.hypergryph.com` 官网的去边框、斜光三角暗格、漂浮双语顶栏与不对称节奏；单独皮肤项目则强行用 CSS 框模拟平面插画 | ① **彻底做减法**：清空未提交的 `skills/arknights-contingency-contract/` 及 `release/arknights-contingency-contract*`，并移除 6 套 `examples/series-*.html`、`resources/prts-series.css` 与 `references/series/`；② **爆改升级主体系 PRTS Design**：在 [`resources/prts-addons.css`](./resources/prts-addons.css) 沉淀 **Carrier 1（官网展示与门户骨架）**（`.ak-bg-lattice` 三角暗格斜光画布、`.ak-topbar` 漂浮双语顶栏 + `.ak-wave-btn` 声波钮、`.ak-stage-shell` + `.ak-index-rail` 右侧竖轨序号、`.ak-hero--editorial` + `.ak-brief` & `.ak-thumb-grid` 焦点滑轨、`.ak-rule` 1px 标尺实块、`.ak-stat--minimal` 去框指标、`.ak-folio-list` 无框清单、`.ak-news-grid--staggered` 错位无框双列情报卡、`.ak-showcase-strip` 四列暗幕竖切与 `ak-wipe-x` / `ak-scan-in` / `ak-wave-eq` 硬切动效）；③ 重写 [`examples/prts-boilerplate.html`](./examples/prts-boilerplate.html)、扩展 [`examples/prts-components.html`](./examples/prts-components.html) 并同步升级 [`references/prts/foundations.md`](./references/prts/foundations.md)、[`decor-and-components.md`](./references/prts/decor-and-components.md)、[`SKILL.md`](./SKILL.md)、[`README.md`](./README.md) 与 `verify.py` / `package-release.py` | 禁止拿单张海报/封面插画强拼独立皮肤模板；本家网页默认走官网建筑去框化展示载体或克制使用百科终端面板，改后须跑 `verify.py --render` 并实看 1440px/390px 亮暗双极截图 |
| 43 | `v1.2-dev` 审美实渲染审查检出：① `.ak-wave-btn` 在亮色正文面板内播放态对比度仅 ~1.9:1、暂停态近乎隐身；② `.ak-folio-item__meta` 短标题下与大标题横排撞行；③ 亮色 `.ak-hero--editorial__rule::before` 误用深黑容器专用的 `--ak-theme-accent`；④ `.ak-ghost-word` 垫在 4 列统计数字背面、第 02 节左栏下方留白失衡与 4 张新闻卡横幅雷同、顶栏/右轨 04 项英文不一致、`.ak-bg-lattice` CSS 斜线抗锯齿微抖 | `.ak-wave-btn` 直读 `--ak-chrome-fg-2`/`--ak-theme-accent`；`.ak-folio-item__main` 用横排 `flex-wrap` 兼顾两种布局；Hero 标尺读错极性令牌；统计区嵌套在水印容器内 | ① `.ak-wave-btn` 改读作用域语义令牌（`--ak-fg-secondary`/`--ak-link`，仅 `.ak-topbar` 内取 `--ak-theme-accent`）；② `.ak-folio-item__meta` 设 `flex: 0 0 100%` 稳定独占首行，增 `.ak-folio-more`；③ `.ak-hero--editorial__rule::before` 改用 `var(--ak-accent)`；④ 统计区移出 Hero 避开水印，补齐左栏清单与 `.ak-news-card__head--grid/--halftone` / `--inverse` 克制变体，`.ak-bg-lattice` 改内联 SVG 向量三角网格，统一顶栏/右轨 `data-sec-en` 并清除 Hero 内联样式 | `verify.py` 增亮色 `prts-components-light` 探针校验 `waveContrastOk` / `folioMetaStacked`，并在 `prts-boilerplate` 探针校验 `statsClearOfWatermark` / `secLabelsMatch` |
| 44 | 全站可交互组件与关键帧动效复查检出：① `prts-addons.css` 与 `endfield-standalone.css` 均缺 `[hidden] { display: none !important; }`，导致 `.ak-folio-item`/`ef-item-slot`（`display: grid`）在设 `hidden` 后仍未视觉隐藏；② PRTS 上游 `.ak-popover` 缺独立 `.ak-tip-anchor` 显隐规则，且 `prts-components.html` 遗漏 Popover 演示及分页/精英阶段/技能等级/屏蔽词/官网清单交互；③ Endfield 样板 Hero 与仓储矩阵筛选/格点选定无事件联动，组件目录缺 `.ef-loader`/`.animate-flicker`/`.animate-fill` 演练与分页/导航器/头像/OTP/月历/工具栏/重播动效交互，且 `.ef-btn[aria-pressed="false"]` 覆写了 `.ef-btn--light` 点阵外观；④ 两份目录及样板缺完备键盘切换与滚动高亮联动 | `display: grid` 优先级高于 UA `[hidden]`；上游 Popover 依赖 Vue `v-show` 控制；初版陈列页与样板保留了一批仅静态展示的按钮与离屏动画；`.ef-tag` 固定 24px 高但未加 `nowrap` | ① 双 CSS 补齐 `.ak-scope [hidden]`/`.ef-scope [hidden]`、`button.ef-avatar` 无边框、`.ef-table--compact`、`.ef-btn[aria-pressed="false"]:not(.ef-btn--light)` 与 `.ef-tag` 防折行，新增 `ak-corner-lock`、`.ak-tip-anchor.is-open > .ak-popover`、`.ak-brief.is-updating` 扫描切换与 `.ak-news-card__head::after` 缓显；② 补齐 `prts-components.html` 的 Popover/分页/阶段/技能等级/屏蔽词/清单/动效重播，完善 `prts-boilerplate.html` 缩略卡键盘导航与滚动联动；③ `endfield-boilerplate.html` 增 `.animate-flicker`、仓储筛选/落格属性面板与 Hero 行动联动，`endfield-components.html` 补齐工具栏/分页/导航器/头像/OTP/月历/班表/`.ef-loader` 与「重播入场动效」，并扩展 `verify.py` 实机 DOM/显示/键盘/动效探针 | 凡设置了 `display: grid/flex` 的组件切换 `hidden` 时须通过 `[hidden] { display: none !important; }` 兜底并在 `verify.py` 检查 `getComputedStyle(el).display === 'none'`；离屏或状态型关键帧（`ef-fill`/`ef-flicker`/`ak-corner-lock`）统一纳入加载态 + 重播交互验证 |
| 45 | `065261d` 实渲染审查检出：① 嵌入式 `.ef-loader` 在 Endfield 暗色下背景 `#141414` 与画布撞色且无边框导致容器轮廓蒸发；② 高视口初次加载时 `IntersectionObserver` 把 `endfield-boilerplate` 侧轨高亮错标到第 2 项；③ 黑底 `.ef-panel__head[data-theme="inverse"]` 内的「重播入场动效」按钮偏闷且含内联尺寸，下方 `.corner-brackets` 标签贴顶偏挤 | `.ef-loader` 缺暗色表面阶差与细框；滚动监听缺 `scrollY < 40` 首屏兜底且多段相交时后项覆盖前项；反转标题头按钮无专用描边类 | `endfield-standalone.css` 为非全屏 `.ef-loader` 补细框与暗色深墨 `#0c0c0c` 底，新增 `.ef-btn--head` 与 `.ef-row--bracket-pad`；三份样板滚动监听统一增加 `scrollY < 40` 锁定首屏及取最靠上相交项 | `verify.py` 增 `endfield-components-dark` 探针校验 `loaderFramedOk`，并在 `endfield-boilerplate` 校验 `initialRailFirst` |

### 2026-11-25 · 字体设计盲区复盘与专题套组硬性记忆

| # | 现象 | 根因 | 处理 | 防再犯 |
| :-: | :--- | :--- | :--- | :--- |
| 46 | 前期设计注意力集中在色板、几何形状与页面骨架，却普遍忽略了**字体作为核心风格识别维度**的重要性，导致不同风格容易在字型气质上同质化、退化成普通默认黑体网页 | 此前只在第 #5 条从“版权/CDN 合规回退”视角提及字体，未把「展示字宽窄、衬线/无衬线气质、中文体例、等宽编号与字距节律」列为采风与设计的一等要素 | ① 在本文件第三节第 6 条与第五节自检明确「字体一等视觉原则」：采风阶段必须同步采集字型气质，按四层角色（Display 展示 / CJK 正文与大标 / Mono·Tabular 编号数据 / Accent 副标）选用契合该风格的开源字体（例如战术/机能走压缩高耸无衬线与机械等宽、炎国/岁家走宋体衬线与典雅拉丁衬线、剧场/阵营典籍走高反差古典衬线、波普/庆典走强表现力宽重展示体），并配齐 `@fontsource` 与系统回退链；② 同步纳入 `suite/arknights` 与 `suite/endfield` 专题规范与渲染检查 | 凡新建或升级任意设计体系/专题子 Skill，必须先定「四层字体角色与字型气质」再定版式；渲染审查时核验字体确实加载生效且不与主基座千篇一律 |
| 47 | 现有样板与 DeepSeek 盲测产物几乎清一色落入「后台控制台 / 监控调度台」（左侧导航轨 + KPI 数字条 + 遥测表 + 状态灯），忽略了现实中官网落地页、长文博客/文档、作品集/商城画廊、登录/营销专题页等非控制台网站类型 | 现有整页样板与规范示例高度锚定在“调度台 / 情报终端 / 数据矩阵”场景，将“设计语言”与“控制台布局原型”隐性焊死，导致小模型拿到非后台需求也惯性套壳做控制台 | ① 在本文件第三节第 7 条与第五节自检立下「视觉语言与网站原型解耦」红线，按五大常见网站类型（官网落地页 / 博客文档阅读 / 画廊作品集与电商 / 登录表单与专题页 / 控制台）分别匹配空间结构，非后台场景主动剥离侧栏、KPI 与状态灯；② 后续在 `SKILL.md` 与 `suite/*` 的 `SUITE_SPEC.md` 中引入页面原型路由，并按场景补充非控制台整页样板，打破样板锚定偏差 | 新建或评审任何 Skill 与样板前，先问「这是不是控制台需求？」——若不是，禁止出现无意义的侧边管理轨、监控 KPI 块与 `ONLINE/TELEMETRY` 装饰 |
| 48 | `v1.3-dev` 通用网站原型重构实渲染检出：① `.ef-has-reveal .ef-reveal.is-in` 复用无 `to { opacity: 1 }` 的 `ef-shift-in` 关键帧，导致 `opacity: 0` 态触发入场后停在透明不可见；② `.ef-plan-card` 纵向 flex 拉伸子级 `.ef-tag` 成满宽色条；③ `endfield-landing.html` 顶栏与首屏同时放黄色按钮违反“单屏仅一个黄主行动”铁律；④ `prts-editorial.html` 正文代码块文本含 `grid-template-columns:` 触发静态内联栅格检查 | `ef-shift-in` 仅声明 `from` 关键帧，终止值依赖元素自身 `opacity`；flex 默认 `align-items: stretch`；顶栏误用 `.ef-btn--action` | ① `.ef-has-reveal .ef-reveal.is-in` 与 `.ak-has-reveal .ak-reveal.is-in` 显式声明 `opacity: 1`；② `.ef-plan-card > .ef-tag` 设 `align-self: flex-start`；③ `endfield-landing.html` 顶栏按钮改默认墨色 `.ef-btn`，首屏保留唯一切角黄行动 `.ef-btn--cut`；④ 改写 `prts-editorial.html` 代码示例为复用语义类，在 `verify.py` 新增 `ef-landing` / `prts-editorial` 亮暗探针与 `revealVisibleOk` 断言 | 凡只写 `from` 关键帧的淡入动画（如 `ef-shift-in`），激活类必须显式设回 `opacity: 1`，并在探针校验计算后透明度；flex 卡片内的 `.ef-tag` 统一 `align-self: flex-start` |
| 49 | `48d7eeb`（`v1.3` 本地提交）全量实渲染审美与规范复审检出：① PRTS `.ak-article-head__kicker` 误用 `var(--ak-link)` 致暗色不可点击眉题呈亮冰青 `#5ddcff`，且 `.ak-prose p` `(0,1,1)` 覆盖了 `.ak-article-head__lead` 下边距致导语与作者栏 `0px` 贴死；② `.ak-topbar__wordmark` 在 `≤420px` 写死 `max-width: 112px`，致 `MONOLITH.NOTES` 在 390px 留有余量时过早截断为 `MONOLITH.NO…`；③ Endfield `.ef-landing-hero > .ef-hero__ghost` 紧贴粘性顶栏底线被削平顶弧，暗色下 `.ef-showcase-card__media` 纯黑 `#000000` 吞没网格肌理，两份新样板画廊卡媒体区空置，且暗色下移动端「菜单」与个人定价钮误用恒浅色 `.ef-btn--light` 反客为主；④ 恒深色登录栏 `.ak-auth-visual` / `.ef-auth-brand` 未锁暗态语义令牌（亮色宿主下子元素黑底黑字或 `#6b5d00` 低对比失效），`motifs-and-components.md` 顶栏蓝图仍残留 `ef-btn--action` | 排版容器元素级规则特指度高于单类；窄屏品牌宽度写死固定像素而非 flex 自适应收缩；恒深色分屏栏遗漏暗态令牌作用域；文档蓝图未与样板同步去黄钮 | ① `.ak-article-head__kicker` 改 `--ak-fg-muted` + `8px` 实块锚点，补齐 `.ak-prose .ak-article-head__lead` 间距、正文链接/列表样式与 `.ak-prose-diagram`，顶栏品牌改为 flex 自适应省略；② `.ef-landing-hero > .ef-hero__ghost` 下移留出 10px 呼吸距并对齐版心，调优 `.ef-showcase-card__media` 表面混色与叠层，为两份新样板共 9 张画廊卡补入精密矢量工程/建筑线稿 `.ak-work-card__art` / `.ef-showcase-card__art`；③ 移动端菜单与次级定价钮改语义 `.ef-btn`，抽离 `.ef-specimen-card` / `.ef-section-bar` 清理内联样式与硬编码色值，为 `.ak-auth-visual` / `.ef-auth-brand` 锁齐暗态令牌并补全 `.ef-prose`；④ 修正 `motifs-and-components.md` 蓝图与 `README.md` / `foundations.md` 描述，扩展 `verify.py` 探针并重打 `release/` | 新增恒深色局部容器（Hero/顶栏/登录品牌栏）必须在 CSS 内自带暗态令牌作用域并用亮色探针实测；含 `.ak-prose p` / `.ef-prose p` 的阅读容器内子组件须注意 `(0,1,1)` 特指度覆盖 |
| 50 | `v1.3` 虽新增两份非控制台样板，但「2 体系 × 5 原型」仍有明显空缺（无 Endfield 三栏技术文档站、无 PRTS 商业产品落地页与检索空态、双体系 `.ak-auth-shell` / `.ef-auth-shell` 均为零样板，且缺 `examples/index.html` 总览入口）；补全 5 份高杠杆样板首次实渲染又检出：① `endfield-docs.html` 的 `<svg width="440">` 致 375px/390px 溢出至 457px，且 `.ef-alert`（`display: flex`）内裸放行内元素导致文字竖列切碎；② `endfield-auth.html` `//ACCESS` 巨字与左上角品牌重叠；③ `prts-auth.html` 左栏内嵌 `<div class="ak-bg-lattice">` 占位把品牌顶推到中段，右栏 `.ak-seg` 拉伸失衡 | 原型矩阵尚未对称闭环；flex 提示框未包裹单一文本块；SVG 缺 `max-width: 100%`；分屏品牌巨字沿用了 Hero `top: 0` 坐标 | ① 新增 `examples/index.html`、`prts-landing.html`（商业落地页+搜索空态+定价）、`endfield-docs.html`（三栏文档 `.ef-docs-shell`+搜索空态+API 表）、`prts-auth.html` 与 `endfield-auth.html`（双体系分屏登录+报错校验+3 步 OTP 向导），同步扩展双 CSS 与 `verify.py` 至 44 图 + 19 实时探针；② 为 `.ef-prose figure svg` 设 `max-width: 100%; height: auto` 并为 `.ef-alert` 内文包块容器；③ 下移 `.ef-auth-brand > .ef-hero__ghost` 至 `top: 88px`（窄屏 `64px`）避让左上角品牌；④ 将 `.ak-bg-lattice` 直接挂在 `.ak-auth-visual` 本身并补 `.ak-auth-stack` 与 `.ak-seg` 左对齐 | 凡 `display: flex` 的提示条（如 `.ef-alert`）内含行内 `<strong>`/`<code>` 时必须包单一块容器；文档内插图 SVG 严禁只写固定 `width` 而不加 `max-width: 100%` |
| 51 | `1043184`（`v1.4-dev`）44 图审美复核检出：① `prts-auth.html` 未清零 `body` 默认 `8px` 外边距致深黑品牌栏四周露白边，且底部 `.ak-article-meta a` 裸链接退回浏览器默认亮蓝下划线；② `<a class="ak-btn ak-btn--block">` 为 `content-box` 叠加水平 `padding` 致 `prts-landing.html` 定价卡按钮越出右缘，且 390px 首屏眉题折行偏紧、标题末字孤行；③ `endfield-docs.html` 侧栏生态外链重复渲染双 `↗`、390px 代码页签尾项裁切、滚表缺边缘渐隐提示；④ `examples/index.html` 未在首屏按 `dataset.theme` 同步主题按钮 `aria-pressed` | `<button>` 默认 `border-box` 而 `<a class="ak-btn">` 默认 `content-box`；`body.ak-scope` 未内置 `margin: 0`；总览页遗漏 `initTheme()` 初始化 | ① `prts-addons.css` 内置 `body.ak-scope { margin: 0 }`、`.ak-btn { box-sizing: border-box; max-width: 100% }`、`.ak-article-meta a:not([class])` 令牌色，放宽 `.ak-article-head__kicker` 行高至 `1.45` 并调优 `.ak-landing-hero__title` 窄屏字阶下限；② `endfield-standalone.css` 为 `.ef-table-wrap` 增补纯 CSS `local/scroll` 滚动边缘渐隐提示并收紧 `≤639px` `.ef-tab` 字号内边距，`endfield-docs.html` 去除重复 `↗`；③ `examples/index.html` 补齐 `applyTheme` 持久化与初始状态同步，扩展 `verify.py` 至 20 组探针并重打 `v1.4-dev` 包 | 多元素共用的按钮类（`<a>`/`<button>`）须显式 `box-sizing: border-box`；所有带主题开关的独立页面须同时跑亮暗双极 `themeBtnSynced` 探针 |

**已知遗留 / 待办**
- Endfield 窄屏巨字被右侧截断属于“越界截断”的有意效果，极窄屏（<360px）可视需求再缩字号。
- 样板用的数据为虚构示例；真实项目需替换，**微文字必须是真实可读内容**（见 SKILL 红线）。
- 仓库不内置 `.woff2` 商业/开源字体二进制，但已在两份 `components-catalog.md` 补充 `@fontsource` 离线自托管安装与引入片段。
- 业务项目接入时，原生 `<dialog>` 自带焦点捕获；两份陈列页的受控 Dropdown 已实现点击外部关闭与方向键/`Esc` 导航，若在项目中改用 `<details class="ef-dropdown">` 或独立 `.ef-popover`，仍需按 catalog 契约补齐外部关闭脚本。
- 仓库静态与视觉门禁已封装为 [`scripts/verify.py`](./scripts/verify.py)（`--render` 跑 44 张 1440px/390px 亮暗截图 + Chrome 实时动效/交互探针），并由 [`scripts/package-release.py`](./scripts/package-release.py) 输出纯净单包 [`release/arknights-design/`](./release/arknights-design/)。

## 五、给 AI 助手的快速自检（交付前 30 秒）

- [ ] 我是否混用了 A/B 两套规则？（PRTS 不许切角/圆角卡片；Endfield 不许四角全切）
- [ ] 我改的是“可手改”的文件吗？（见第二节表）
- [ ] 我是否为本体系/专题独立选定了四层字体角色与字型气质，并在渲染图里确认生效（而非沿用默认黑体）？
- [ ] 我是否按真实网站类型选择布局原型（而非把落地页/博客/画廊硬做成控制台）？
- [ ] 我渲染并看过 1440px 与 390px、亮与暗了吗？
- [ ] 文档、CSS、样板三者一致吗？
- [ ] 我把这次的现象→根因→处理追加进第四节了吗？
