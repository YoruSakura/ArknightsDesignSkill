---
name: arknights-design
description: >-
  Use this skill whenever the user asks to design, initialize, build, or refactor ANY frontend website,
  landing page, blog, documentation site, portfolio/store gallery, auth/form flow, dashboard/console,
  or UI component in Arknights style (明日方舟本家 PRTS 建筑极简风格) or Arknights: Endfield style
  (明日方舟：终末地 工业编辑风 / Endfield UI). Decouples visual language from page archetype with
  ready-to-copy CSS token & component bundles, typography hierarchy, motion, and anti-pattern checklists.
---

# Arknights & Endfield Frontend Design Skill (`arknights-design`)

本 Skill 包含《明日方舟》本家（**PRTS Design**）与《明日方舟：终末地》（**Endfield UI**）两套正交的通用前端设计系统。
**两条核心总纲：**
1. **体系严格隔离**：PRTS 与 Endfield 视觉语法截然不同，严禁混用；
2. **视觉语言与网站原型解耦**：两套体系均适用于**所有类型网站**（官网落地页、博客/文档、作品集/商城画廊、登录表单、控制台），**严禁把所有需求默认做成后台控制台**！

---

## 第一步：正交双路由（先定视觉体系，再定网站原型）

### 1A. 判定视觉体系（Style Router）
若用户仅说“明日方舟风格”未指明本家还是终末地，**先向用户确认**；无法提问时默认采用体系 A（本家 PRTS）并明确声明假设：

| 维度 | 体系 A：明日方舟本家 (`PRTS Design`) | 体系 B：明日方舟：终末地 (`Endfield UI`) |
| :--- | :--- | :--- |
| **核心气质** | **冷峻建筑极简 + 制图档案（亮）/ 暗夜终端（暗）** | **工业编辑风（Industrial Editorial）**——印刷级技术画册与精密仪器 |
| **色彩哲学** | 黑白灰炭为体、冰青为用：暗底 `#18D1FF` / 亮底 `#0098DC`（小字 `#0072A8`）；黄黑条纹仅限警示；顶栏与页脚恒深黑 | 纸白/烟黑 13 级纯中性灰 + 唯一信号黄 `#FFFA00`（单屏黄面积 $\le 10\%$，亮底字用 `#6B5D00`） |
| **四层字体** | Display `Oswald`（开 `lining-nums`） / Label `Chakra Petch` / Body `Noto Sans SC`（表格必用正文 + `tabular-nums`） / Mono 等宽 | Display 宽体 `Archivo` / Latin `Outfit` / Tech `Space Grotesk` / Body `Noto Sans SC` + `JetBrains Mono` |
| **形状铁律** | **纯直角 `border-radius: 0`，严禁任何 45° 切角/斜切**；无辉光；独立小菱形 `◆` 仅限 4 处 | **形状即语义**：面板/输入直角、按钮 `4px`、主行动/机械件单角 `45°` 切角（`cut-tr` 画在 `::before`）、筛选用胶囊、头像/仪表用正圆 |

### 1B. 判定网站原型（Page Archetype Router — 反“万物皆控制台”）
动笔前先识别用户要做的真实网站类型，**按原型挑外壳，严格遵守右侧“禁塞清单”**：

| 网站原型 | PRTS 推荐外壳与核心类 | Endfield 推荐外壳与核心类 | **严禁硬塞的控制台噪音** |
| :--- | :--- | :--- | :--- |
| **1. 品牌官网 / 产品落地页** | `.ak-topbar` + `.ak-site-shell` + `.ak-landing-hero`（或 `.ak-stage-shell` + `.ak-hero--editorial`）+ `.ak-feature-grid` / `.ak-pricing-grid` + `.ak-footer--editorial` | `.ef-site-header` + `.ef-site-main` + `.ef-landing-hero` + `.ef-band-title` + `.ef-feature-grid` / `.ef-pricing-grid` + `.ef-accordion` + `.ef-footer` | ❌ 常驻 224px 后台侧轨、KPI 监控数字条、遥测表、`ONLINE` 状态灯 |
| **2. 博客 / 长文 / 技术文档** | `.ak-topbar` + `.ak-read-bar` + `.ak-site-shell` + `.ak-prose-shell`（`72ch` 正文 `.ak-prose` + 粘性 `.ak-article-toc` + `.ak-article-pager`） | `.ef-site-header` + `.ef-read-bar` + `.ef-site-main` + `.ef-docs-shell`（三栏左树 + `72ch` `.ef-prose` + `.ef-toc`）或 `.ef-article-shell`（两栏） | ❌ 大面积巨字水印压正文、监控卡片堆叠、遥测行带、物品格 |
| **3. 作品集 / 图鉴 / 电商画廊** | `.ak-topbar` + `.ak-site-shell` + `.ak-catalog-bar`（搜索 + `.ak-filter-strip`）+ `.ak-gallery-grid` / `.ak-work-card` + `.ak-empty` + 右侧 `.ak-drawer` | `.ef-site-header` + `.ef-site-main` + `.ef-filter-chip` + `.ef-gallery-grid` / `.ef-showcase-card` + `.ef-empty` + 右侧 `.ef-drawer` | ❌ 后台管理侧栏、KPI 仪表块、实时链路读数 |
| **4. 登录 / 表单向导 / 活动单页** | `.ak-auth-shell`（`.ak-auth-visual` + `.ak-auth-form`）+ `.ak-stepper` + `.ak-auth-otp` + 表单报错校验 | `.ef-auth-shell`（`.ef-auth-brand` + `.ef-auth-card`）+ `.ef-steps` + `.ef-otp` + `.ef-field__error` | ❌ 多级顶栏导航、侧边栏、多列大页脚 |
| **5. 控制台 / 监控台 / 管理后台** | `.ak-header` + `.ak-layout` + `.ak-sidebar` + `.ak-table-scroll` / `.ak-stat--minimal` + `.ak-drawer` | `.ef-app-shell` + `.ef-side-rail` + `.ef-stat-row` + `.ef-data-list` / `.ef-sparkline` / `.ef-item-grid` | —（**仅此类后台/监控需求才启用侧栏与监控组件**） |

---

## 第二步：按需读取深度规范与拷贝静态资源（Progressive Disclosure）

确定体系与原型后，先用 `read_file` 阅读对应的两份基础手册（`foundations` + 母题/骨架）；`components-catalog.md` 仅在需要具体控件 DOM/ARIA 契约时按需读取：

### 体系 A（明日方舟本家 · PRTS Design）
1. **必读规范**：
   - [PRTS 基础设计规范与令牌表](./references/prts/foundations.md)
   - [PRTS 多原型骨架、建筑母题与核心蓝图](./references/prts/decor-and-components.md)
   - [PRTS 全组件目录与交互蓝图](./references/prts/components-catalog.md)（按需读取，含 `@fontsource` 离线字体配置）
2. **拷贝样式资源**（必须按顺序引入）：
   - [`resources/prts-design.css`](./resources/prts-design.css)（上游完整底座与通用/领域组件）
   - [`resources/prts-addons.css`](./resources/prts-addons.css)（官网/博客/画廊/登录全原型壳层、硬切动效与上游补丁）
   - 仅需令牌时：[`resources/prts-tokens.css`](./resources/prts-tokens.css)
3. **分原型参考样板**（按目标网站类型挑对应的看，**严禁抄录测试文案**；全景索引见 [`examples/index.html`](./examples/index.html)）：
   - 商业产品落地页 + 多维检索画廊与空态（原型 1+3 · 无侧栏）：[`examples/prts-landing.html`](./examples/prts-landing.html)
   - 长文专栏 + 作品画廊（原型 2+3 · 无侧栏）：[`examples/prts-editorial.html`](./examples/prts-editorial.html)
   - 分屏登录 + 3 步入驻向导（原型 4 · 表单报错/OTP）：[`examples/prts-auth.html`](./examples/prts-auth.html)
   - 官网概念门户（原型 1 · 暗色主视觉）：[`examples/prts-boilerplate.html`](./examples/prts-boilerplate.html)
   - 百科侧栏外壳 & 全组件目录（原型 5）：[`examples/prts-components.html`](./examples/prts-components.html)

### 体系 B（明日方舟：终末地 · Endfield UI）
1. **必读规范**：
   - [Endfield 基础设计规范、角色色与载体边界](./references/endfield/foundations.md)
   - [Endfield 多原型骨架、母题与核心组件蓝图](./references/endfield/motifs-and-components.md)
   - [Endfield 全组件目录与交互蓝图](./references/endfield/components-catalog.md)（按需读取，含 16 个关键帧与 `@fontsource` 配置）
2. **拷贝样式资源**：
   - 零依赖纯 CSS 全套（含全部 5 类网站外壳 + 通用组件 + 16 关键帧）：[`resources/endfield-standalone.css`](./resources/endfield-standalone.css)
   - Tailwind CSS v4 专用：[`resources/endfield-theme.css`](./resources/endfield-theme.css)
3. **分原型参考样板**（按目标网站类型挑对应的看，**严禁抄录测试文案**）：
   - 品牌产品落地页 + 筛选画廊 + 定价 + FAQ（原型 1+3 · 无侧栏）：[`examples/endfield-landing.html`](./examples/endfield-landing.html)
   - 三栏技术文档 + API 参考站（原型 2 · 左树检索/空态/右 TOC）：[`examples/endfield-docs.html`](./examples/endfield-docs.html)
   - 分屏登录 + 3 步设备激活向导（原型 4 · 校验/OTP/完成横幅）：[`examples/endfield-auth.html`](./examples/endfield-auth.html)
   - 工业调度控制台（原型 5 · 含侧轨与遥测）：[`examples/endfield-boilerplate.html`](./examples/endfield-boilerplate.html)
   - 全组件与动效目录：[`examples/endfield-components.html`](./examples/endfield-components.html)

---

## 第三步：项目初始化与开发执行流程

1. **注入样式基座与四层字体（字体是一等视觉要素）**：
   - 拷贝对应 CSS 到项目并引入开源字体（PRTS：`Oswald` + `Chakra Petch` + `Noto Sans SC`；Endfield：`Archivo` wdth 125 + `Outfit` + `Space Grotesk` + `JetBrains Mono` + `Noto Sans SC`）。
   - 中国大陆或内网环境请用 `@fontsource`（见两份 `components-catalog.md`）或本地 `@font-face` 自托管，并保留系统回退链；商业字体 `Bender` / `Novecento` 不随包分发。
2. **按 1B 原型搭外壳（严禁写死内联 `grid-template-columns`）**：
   - 官网落地页 / 博客 / 画廊 / 登录页**优先使用无侧栏外壳**（PRTS：`.ak-topbar` + `.ak-site-shell` / `.ak-prose-shell` / `.ak-auth-shell`；Endfield：`.ef-site-header` + `.ef-site-main` + `.ef-landing-hero` / `.ef-article-shell` / `.ef-auth-shell`）。
   - 仅当业务明确是管理后台、百科树或调度监控台时，才启用 `.ak-layout` + `.ak-sidebar` 或 `.ef-app-shell` + `.ef-side-rail`。
3. **母题「按需点菜」（克制上限原则）**：
   - **单页只需选用 2~3 个契合当前原型的标志性母题即可立住风格**（色板 + 字体 + 如 1px 标尺 / 信号黄换气带 / 切角主行动 / 滚动进度细线 `.ak-read-bar` / `.ef-read-bar`），**严禁把整本目录的组件硬塞进同一页**。
   - 交互组件遵循 `components-catalog.md` 的 WAI-ARIA 状态契约（`roving tabindex`、抽屉/浮层 `Esc` 关闭与焦点归还、`[hidden]` 真实隐藏、`prefers-reduced-motion` 保护）。
4. **弹性适配边界与品牌换色（换强调不换骨）**：
   - **工程底线不妥协**：必须复用 `--ak-*` / `--ef-*` 令牌与内置响应式类，**严禁内联 `grid-template-columns`**，**禁用 `0x7F3A` / `0xDEAD` 假十六进制**，非游戏项目彻底清除样板专有词（`PERLICA`、`DIJIANG`、`TALOS-N07`、`北岭`、`罗德岛` 等）。
   - **品牌换色**：保留 90% 中性纸墨基底，仅覆写语义强调令牌——PRTS 覆写 `--ak-theme-accent*` 与 `--ak-accent` / `--ak-link` / `--ak-focus`；Endfield 覆写 `--ef-action*` / `--ef-on-action` / `--ef-accent-ink*` 并校验对比度。
   - **外观偏好的有条件让步**：用户明确坚持的局部诉求通过局部扩展类派生并提示偏离，绝不借“破例”将整站改成圆角霓虹发光 SaaS。

---

## 第四步：交付前自检清单（Self-Audit）

- [ ] **网站原型是否匹配？** 非控制台需求（落地页、博客、文档、画廊、登录页）是否已彻底剥离无关侧栏、KPI 指标块、数据表与 `ONLINE/TELEMETRY` 状态装饰？
- [ ] **字体是否按四层角色生效？** 展示字、标号/等宽数字与中文正文是否清晰区分，PRTS 表格数字使用正文字体 + `tabular-nums`，未退化成单一默认字体？
- [ ] **形状与边框铁律是否守住？** PRTS 全程 `0px` 无 45° 切角、无套娃框、无辉光；Endfield 不画八边形、可聚焦切角画在 `::before`、悬停不上浮不放大？
- [ ] **对比度、黄面积与微文字是否合规？** Endfield 单屏黄面积 $\le 10\%$、亮底强调文字用 `--ef-accent-ink`；PRTS 亮底小字用 `--ak-link`；微文字均为真实业务内容，零假乱码、零游戏词泄漏？

---

## 第五步：渲染验证（硬性门槛）

交付前必须在真实浏览器中渲染核对 `1440px` 桌面与 `390px` 手机 × 亮/暗 4 张图：

```bash
google-chrome --headless=new --no-sandbox --hide-scrollbars --window-size=1440,1300 --virtual-time-budget=6000 --screenshot=desktop.png file://$PWD/index.html
google-chrome --headless=new --no-sandbox --hide-scrollbars --window-size=390,2400  --virtual-time-budget=6000 --screenshot=mobile.png  file://$PWD/index.html
```

- [ ] 无文字重叠、裁切或极窄屏（`375px` / `390px`）横向溢出；宽表格包 `.ak-table-scroll` / `.ef-table-wrap`；
- [ ] 亮/暗两套主题对比度清晰，按钮/表单/抽屉/筛选/切换开关均真实可交互且状态与 DOM 同步；
- [ ] 目标开源字体已正确加载生效，无无意义纯色占位块。
