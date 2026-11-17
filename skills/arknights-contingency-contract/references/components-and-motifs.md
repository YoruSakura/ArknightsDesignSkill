# Arknights Contingency Contract · 组件与契约蓝图

> 本手册记录 [`resources/cc-design.css`](../resources/cc-design.css) 已内置的所有组件 DOM 结构、状态类名及 WAI-ARIA 交互契约，不绑定特定前端框架。

---

## 一、 壳层与响应式布局类（严禁写死内联 grid）

* **整页壳层**：`.cc-header`（吸顶终端顶栏） + `.cc-menu-btn`（`<1120px` 抽屉触发钮） + `.cc-scrim` + `.cc-layout`（`aside.cc-sidebar` + `main.cc-main`） + `.cc-footer`
* **多栏栅格类**：`.cc-stat-row`（4 列统计块）、`.cc-grid-2`、`.cc-grid-3`、`.cc-split`（`1.35fr : 0.85fr` 偏心双栏）、`.cc-wave-grid`（5 列步进波次卡片）

---

## 二、 核心战术组件蓝图

### 1. 演播评分 Hero（`.cc-hero` + `.cc-hero__scorebox`）
```html
<section class="cc-hero">
  <div class="cc-hero__grid">
    <div>
      <div class="cc-hero__eyebrow"><span class="cc-live-dot" aria-hidden="true"></span> OPERATION // ARCLIGHT-08</div>
      <h1 class="cc-hero__title">BENCHMARK STRESS OPS <span>全链路分布式压测契约推演台</span></h1>
      <p class="cc-hero__desc">多维风险词条自由组合、互斥校验与实时评级核算。</p>
      <div class="cc-hero__actions">
        <button type="button" class="cc-btn cc-btn--contrast">启动合规验证</button>
        <a class="cc-btn cc-btn--primary" href="#contracts">调整契约词条</a>
      </div>
    </div>
    <div class="cc-hero__scorebox" aria-live="polite">
      <div class="cc-hero__score-meta">
        <span>RISK RATING // 危级评分</span>
        <span class="cc-dots-3x3" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span>
      </div>
      <div class="cc-hero__score" id="cc-total-score">880</div>
      <div class="cc-tag cc-tag--accent">S-RANK // LV.18 EQUIV</div>
    </div>
  </div>
</section>
```

### 2. 契约调整多轨词条矩（`.cc-contract-tracks` / `.cc-contract-tag`）
```html
<div class="cc-contract-tracks">
  <div class="cc-contract-row">
    <div class="cc-contract-cat">链路注入<small>LATENCY</small></div>
    <div class="cc-contract-group" role="group" aria-label="链路注入词条">
      <button type="button" class="cc-contract-tag is-selected" data-group="lat" data-pts="2" aria-pressed="true">
        <span>边缘节点超时阈值降至 180ms</span>
        <span class="cc-contract-tag__pts">+2</span>
      </button>
      <button type="button" class="cc-contract-tag" data-group="lat" data-pts="3" aria-pressed="false">
        <span>全区边缘节点超时阈值降至 90ms</span>
        <span class="cc-contract-tag__pts">+3</span>
      </button>
    </div>
  </div>
</div>
```
> **交互契约**：同一 `data-group` 内为互斥等级——选中同组新词条时须自动取消同组旧词条的 `.is-selected` 与 `aria-pressed="true"`，并同步重算总分与状态徽标。

### 3. 规程阶梯（`.cc-tier-list`）、步进波次格（`.cc-wave-grid`）与水印结算行（`.cc-mission-item`）
```html
<!-- 规程阶梯 -->
<div class="cc-tier-list" role="radiogroup" aria-label="演练规程等级">
  <button type="button" class="cc-tier is-active">
    <span><span class="cc-tier__lv">LV.02</span> 跨区仲裁切换 · 摘除 30% 边缘副本</span>
    <span class="cc-tag cc-tag--accent">现行</span>
  </button>
</div>

<!-- 矢量突破风步进波次卡片列阵 -->
<div class="cc-wave-grid">
  <article class="cc-wave-card is-cleared">
    <span class="cc-wave-card__code">VEC-01</span>
    <span class="cc-wave-card__lv">LV.15</span>
    <span class="cc-tag cc-tag--success">PASSED</span>
  </article>
</div>

<!-- 结算行（.cc-mission-item__wm 为独立 flex 节点，绝不遮盖右侧 reward） -->
<div class="cc-mission-item">
  <div class="cc-mission-item__main"><strong>M-01 // 网关零丢包降级切换</strong></div>
  <span class="cc-mission-item__wm" aria-hidden="true">COMPLETED</span>
  <span class="cc-mission-item__reward">+200 PTS</span>
</div>
```

### 4. WAI-ARIA Tabs（`.cc-tabs`）与滚表（`.cc-table-scroll > .cc-table`）
- `.cc-tab` 必须携带 `role="tab"`, `id`, `aria-controls`, `aria-selected` 与 roving `tabindex` (`0`/`-1`)；支持 `ArrowLeft` / `ArrowRight` / `Home` / `End` 键盘切换。
- 宽表必须包裹在 `<div class="cc-table-scroll">` 中，防止 `<640px` 窄屏撑宽产生横向滚动条。

---

## 三、 离线自托管字体配置

```css
/* 替代 Google Fonts CDN（国内/内网环境） */
/* npm i @fontsource/oswald @fontsource/chakra-petch @fontsource/jetbrains-mono @fontsource/noto-sans-sc */
import '@fontsource/oswald/700.css';
import '@fontsource/chakra-petch/600.css';
import '@fontsource/jetbrains-mono/700.css';
import '@fontsource/noto-sans-sc/400.css';
```
