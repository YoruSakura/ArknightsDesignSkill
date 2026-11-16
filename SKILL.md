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

在开始写代码前，先根据用户需求判定采用哪一套设计体系（若用户仅说“明日方舟风格”未指明本家还是终末地，默认优先询问或提供双风格对比/切换）：

| 维度 | 体系 A：明日方舟本家 (`PRTS Design`) | 体系 B：明日方舟：终末地 (`Endfield UI`) |
| :--- | :--- | :--- |
| **核心气质** | **罗德岛档案（亮）/ PRTS 终端（暗）** | **工业编辑风（Industrial Editorial）**——印出来的技术画册与测绘终端 |
| **色彩哲学** | **黑白为体、青为用**：暗底配官网青 `#18D1FF`，亮底配游戏蓝 `#0098DC`；次强调黄 `#FFD800`；顶栏与页脚恒为深黑框 | **纸与墨是主体，信号黄是唯一焦点**：13 级纯中性灰 + 信号黄 `#FFFA00`（一屏黄面积 $\le 10\%$，白底严禁用黄字，用 `#6B5D00`） |
| **形状铁律** | **纯直角 `border-radius: 0`，严禁任何 45° 切角/斜切**；色条与 1px 细框用 `border-image` 直角拼接；独立小图形用源石菱形 `◆` | **形状即语义**：面板/归档标签用直角，按钮统一 `4px` 微圆角，主要行动/机械控件用 `45°` 单角切角（`cut-tr`）或斜楔（`wedge-r`），头像/仪表用正圆，筛选/资源用胶囊 |
| **边框与阴影** | 卡片与面板带 `1px solid var(--ak-border)` 细框 + 左侧 `4px` 或顶部 `3px` 色条；无辉光 | **默认不围整圈边框**（统计块靠左缘 3px 墨线，提示条靠左缘 4px 色条，输入框用凹陷底 + 2px 底边线）；浮层用零偏移环境阴影 `0 0 <blur>` |
| **装饰母题** | 45° 警示斜纹（`.ak-stripes`）、半调网点渐隐（`.ak-halftone`）、角标直角三角（`.ak-corner`）、黑白反转（`.ak-inverse`） | 斜纹镂空巨字（`ghost-hatch`）、标准滑块分节标题（`[███ ↘]`）、方括号姓名（`[ 名称 ]`）、CMY 注册色条、四角 L 形括号（`corner-brackets`）、等高线（`contour`） |

---

## 第二步：按需读取深度规范与拷贝静态资源（Progressive Disclosure）

确定目标体系后，**必须先用 `read_file` 阅读对应的两份参考手册**，并将对应的 CSS 资源文件拷贝到目标前端项目中：

### 选体系 A（明日方舟本家 · PRTS Design）时：
1. **必读规范**：
   - [PRTS 基础设计规范与色彩/排版令牌](./references/prts/foundations.md)
   - [PRTS 装饰母题与全组件 DOM+CSS 蓝图](./references/prts/decor-and-components.md)
2. **可直接拷贝到目标项目的样式资源**：
   - 完整样式表（含令牌 + `.ak-scope` + 全部通用组件 + 方舟装饰 + 领域组件 + `.ak-header`/`.ak-footer` 骨架，零外部图片依赖）：[`resources/prts-design.css`](./resources/prts-design.css)
   - 仅需令牌变量时：[`resources/prts-tokens.css`](./resources/prts-tokens.css)
   - 整页标准样板参考：[`examples/prts-boilerplate.html`](./examples/prts-boilerplate.html)

### 选体系 B（明日方舟：终末地 · Endfield UI）时：
1. **必读规范**：
   - [Endfield 基础设计规范、六大原则与七大界面家族](./references/endfield/foundations.md)
   - [Endfield 母题工具类与核心组件实现蓝图](./references/endfield/motifs-and-components.md)
2. **可直接拷贝到目标项目的样式资源**：
   - 零依赖通用纯 CSS 版（含 `--ef-*` 亮/暗/反转三套令牌 + 全部母题类 + 核心组件 `.ef-*`，适用于任意 HTML / Vue / React / Vite 项目）：[`resources/endfield-standalone.css`](./resources/endfield-standalone.css)
   - Tailwind CSS v4 专用版（含 `@theme`、`@theme inline`、`@utility`）：[`resources/endfield-theme.css`](./resources/endfield-theme.css)
   - 整页标准样板参考：[`examples/endfield-boilerplate.html`](./examples/endfield-boilerplate.html)

---

## 第三步：项目初始化与开发执行流程

当用户要求“使用本 Skill 初始化一个网站样板 / 组件页面”时，严格按以下步骤执行：

1. **注入样式基座与字体**：
   - 将 [`resources/prts-design.css`](./resources/prts-design.css) 或 [`resources/endfield-standalone.css`](./resources/endfield-standalone.css) 复制到目标项目的静态样式目录（如 `src/styles/` 或 `public/`）并在入口引入。
   - 在 `<head>` 引入对应的 Google Fonts 开源字体（PRTS：`Oswald` + `Chakra Petch` + `Noto Sans SC`；Endfield：`Archivo` + `Outfit` + `Space Grotesk` + `JetBrains Mono` + `Noto Sans SC`）。
2. **搭建符合正统构图的页面外壳**：
   - **PRTS**：采用「黑色终端顶栏 `.ak-header` + 左侧导航导轨 `.ak-sidebar` + 主内容区 `.ak-main` + 黑色斜纹顶边页脚 `.ak-footer`」，支持「档案（Light）/ 终端（Dark）」一键切换。
   - **Endfield**：采用「左侧窄轨 `.ef-side-rail`（底部配唯一主行动块 `.ef-nav-action`）+ 偏心构图主舞台（`1.5fr : 0.9fr` 不等宽分栏）+ 通栏信号黄色带标题 `.ef-band-title` 分隔亮暗版块」，支持「纸白（Light）/ 烟黑（Dark）」切换及局部 `[data-theme="inverse"]` 反转标题带。
3. **组合标志性母题与业务组件**：
   - 拒绝千篇一律的居中三卡片网格！必ず组合使用各体系的签名级组件（如 PRTS 的 `.ak-hero`、`.ak-news`、`.ak-panel`、`.ak-stat`、`.ak-table`、`.ak-stage`；Endfield 的 `ghost-hatch` 镂空巨字、`ef-section-title` 滑块标题、`ef-bracket-title` 方括号名、`ef-reg-strip` 三原色校准条、`ef-stat` 左竖线统计块、`ef-data-row` 深色数据行带、`ef-item-slot` 底部稀有度渐变格 + `corner-brackets` 四角括号选中）。

---

## 第四步：交付前的人类级视觉自检清单（Self-Audit）

在完成代码编写后，逐条对照以下红线自检，任何一条违规必须立即修正：

- [ ] **是否混淆了两套系统的形状？**
  - PRTS 严禁出现 `clip-path` 45° 切角或圆角卡片；
  - Endfield 严禁四角全切八边形，切角只用于行动/机械控件，且可聚焦按钮的切角必须画在 `::before` 上以保留焦点环。
- [ ] **颜色对比度与面积预算是否合规？**
  - PRTS 的不可点击小标签（overline / eyebrow / 章节英文副标）是否误用了青色？（必须用 `--ak-fg-muted` 灰色）；
  - Endfield 的信号黄 `#FFFA00` 是否控制在全屏面积 10% 以内？亮色白底上是否误用了 `#FFFA00` 作文字？（白底强调字必须用 `--ef-accent-ink: #6B5D00`）。
- [ ] **数字与英文排版是否克制且真实？**
  - PRTS 的 `<table>` 数字列是否使用了正文字体 + `tabular-nums`（严禁在表格内用 Bender）？双语标题是否控制在一页 1～2 处？
  - Endfield 的微文字（Micro-text）是否是真实可读的栏目名、日期、版本号？（严禁出现 `0x7F3A` 等假十六进制乱码或无意义伪代码）。
- [ ] **是否杜绝了通用 SaaS / 科幻俗套？**
  - 严禁大圆角（`8px–16px`）投影卡片、严禁悬停上浮放大、严禁毛玻璃发光霓虹边、严禁六边形蜂窝网格。
