# Arknights Integrated Strategies · 组件与契约蓝图

> 本手册记录 [`resources/is-design.css`](../resources/is-design.css) 已内置的所有组件 DOM 结构、状态钩子与跨框架移植契约。

---

## 一、 壳层与多栏栅格（禁用内联 grid）

* **壳层**：`.is-header` + `.is-menu-btn`（`<1120px` 抽屉触发钮） + `.is-scrim` + `.is-layout`（`aside.is-sidebar` + `main.is-main`） + `.is-footer`
* **布局类**：`.is-hud-strip`（4 列 HUD 状态带）、`.is-split`（`1.35fr : 0.85fr` 路径图 + 详情栏）、`.is-route-map`（3 列节点网格）、`.is-commission-grid`（3 列委托牌）、`.is-relic-grid`（4 列藏品陈列）

---

## 二、 核心集成战略组件 DOM 蓝图

### 1. 光柱主舞台 Hero & 注音标题（`.is-hero` / `.is-ruby-title`）
```html
<section class="is-hero">
  <div class="is-hero__pillars" aria-hidden="true"></div>
  <div class="is-hero__content">
    <div class="is-hero__eyebrow"><span class="is-pulse" aria-hidden="true"></span> EXPEDITION FOLIO // LAYER 05</div>
    <h1 class="is-hero__title">ABYSSAL EXPEDITION <span class="cn">多维路径沙盒与典籍推演卷宗</span></h1>
    <p class="is-hero__desc">支持五代主题实时切换的分支路径决策、月度委托牌及藏品图鉴系统。</p>
    <div class="is-hero__actions">
      <a class="is-btn is-btn--contrast" href="#routes">进入节点推演</a>
      <a class="is-btn is-btn--primary" href="#relics">检视藏品图鉴</a>
    </div>
  </div>
</section>

<!-- 岁界园括注拼音标题 -->
<div class="is-ruby-title" aria-label="界园志异">
  <div class="is-ruby-word"><strong>界</strong><span>[jiè]</span></div>
  <div class="is-ruby-word"><strong>园</strong><span>[yuán]</span></div>
  <div class="is-ruby-word"><strong>志</strong><span>[zhì]</span></div>
  <div class="is-ruby-word"><strong>异</strong><span>[yì]</span></div>
</div>
```

### 2. 分支探险节点图与右栏事件简报（`.is-route-map` / `.is-route-node`）
```html
<div class="is-split">
  <div class="is-route-map" role="group" aria-label="探索节点路径选择">
    <div class="is-route-col">
      <div class="is-route-col__stage">DEPTH 01 // 起点</div>
      <button type="button" class="is-route-node is-selected" aria-pressed="true">
        <span class="is-route-node__type">NODE A1 · 校验</span>
        <span class="is-route-node__name">边缘观测站入网自检</span>
      </button>
    </div>
    <!-- 第 2、3 列照此组织；点击同步右侧面板详情与资源 HUD -->
  </div>
  <div class="is-panel">...</div>
</div>
```

### 3. 月度委托牌（`.is-commission-grid`）与藏品陈列架（`.is-relic-grid`）
```html
<!-- 本月委托栏（甲/乙/丙竖牌） -->
<div class="is-commission-grid">
  <article class="is-commission-card">
    <div class="is-commission-seal" aria-hidden="true">甲</div>
    <h3 class="is-commission-card__title">零误报全链路巡检</h3>
    <p class="is-commission-card__desc">单轮巡检内保持全分支节点校验零超时。</p>
    <div><span class="is-tag is-tag--accent">赏格 +500</span></div>
  </article>
</div>

<!-- 可点击切换详情的藏品架 -->
<div class="is-relic-grid">
  <button type="button" class="is-relic-card is-selected" aria-pressed="true">
    <span class="is-relic-card__code">CURIO // NO.014</span>
    <span class="is-relic-card__name">黄铜浑天校准仪</span>
    <span class="is-tag is-tag--accent">已收录</span>
  </button>
</div>
<div class="is-relic-detail" aria-live="polite">...</div>
```

### 4. 页签、涂黑密语（`.is-redacted`）与结算表（`.is-table-scroll > .is-table`）
- `.is-tabs > .is-tab` 按完整 WAI-ARIA `tablist` 规范配 `id`/`aria-controls`/`aria-labelledby` 与 roving `tabindex` 键盘支持；
- 涉密片段使用 `<span class="is-redacted" tabindex="0">...</span>`，支持鼠标悬停及键盘聚焦显露原文；
- `.is-table-scroll` 内 `.is-table` 数值列带 `.num`，保持对齐的 `tabular-nums`。

---

## 三、 离线字体引入片段

```css
/* 推荐安装开源衬线与标牌字体包以保障国内/离线环境还原度 */
/* npm i @fontsource/noto-serif-sc @fontsource/cormorant-garamond @fontsource/chakra-petch @fontsource/noto-sans-sc */
import '@fontsource/noto-serif-sc/700.css';
import '@fontsource/cormorant-garamond/700.css';
import '@fontsource/chakra-petch/600.css';
import '@fontsource/noto-sans-sc/400.css';
```
