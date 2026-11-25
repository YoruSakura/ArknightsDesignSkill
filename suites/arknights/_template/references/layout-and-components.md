# Layout & Components — `<Theme Title>` 专属骨架与组件契约

> 严禁把其他活动模板或主 PRTS 的盒状卡片直接照搬过来；本文件只沉淀**属于本专题自身**的空间骨架、视觉母题与交互控件。

## 一、标志性页面骨架

- 描述 1440px 桌面端核心空间结构（如主导航形态、首屏层次、非对称比例、索引导轨等）。
- 描述 `<1024px` 与 `<640px` 的响应式降维方案（禁止内联 `grid-template-columns`）。

## 二、专属视觉母题

- 列出 2~4 个仅靠纯 CSS / 内联矢量 SVG 实现、无需外部位图的高识别度母题类（全部以 `.ak-<slug>-*` 命名）。

## 三、可交互组件与 WAI-ARIA 契约

- **状态钩子**：统一使用 `.is-active` / `.is-open` / `.is-selected` + `aria-pressed` / `aria-selected` / `aria-expanded` / `hidden`。
- **键盘与焦点**：页签支持 `Arrow` / `Home` / `End`（roving `tabindex`）；浮层/抽屉支持 `Esc` 关闭与焦点归还、点击外部关闭。
- **可移植代码片段**：为每个核心组件提供可直接复制到任意前端框架的最小语义 HTML。
