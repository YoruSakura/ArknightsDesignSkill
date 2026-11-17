# 官方活动系列视觉预设与平面母题规范（PRTS Series Extensions）

> **按需读取**：仅当用户明确要求参照《明日方舟》特定大型活动系列（如危机合约/卫戍协议、周年感谢庆典、炎国「岁」系列、奇象巡展/PFC、喧闹法则、集成战略/暗黑剧场）构建页面时读取本手册，并配套引入 [`resources/prts-series.css`](../../resources/prts-series.css)。
> 引入顺序：`prts-design.css` → `prts-addons.css` → `prts-series.css`，并在 `<html>`（或 `.ak-scope` 根元素）声明 `[data-ak-series="..."]`。

---

## 一、六大核心活动系列速查矩阵

| 系列标识 (`data-ak-series`) | 灵感谱系 | 色彩签名（亮 / 暗） | 字体补充 | 核心专属组件 / 母题 | 参考整页样板 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`regulation`** | 卫戍协议・危机合约・DOS | 深枪灰/雾青 + 高敏战术青绿 `#00D8A0` / 琥珀橙 `#F59E0B` | 默认 `Oswald` + `Chakra Petch` + `Noto Sans SC` | `.ak-tier-list`、`.ak-tier`、`.ak-mission-item`（`COMPLETED` 斜水纹）、`.ak-series-pulse` | [`examples/series-regulation.html`](../../examples/series-regulation.html) |
| **`anniversary`** | 感谢庆典・周年特设站 | 暖象牙/曜石黑 + 绯红 `#E03C4B` + 暖金 `#E5B85C` | 默认体系（标题克制衬线或黑体） | `.ak-ribbon-head` 对称绶带、WAI-ARIA `.ak-tabs--block`、`.ak-timeline`、`.ak-card--accent-top` | [`examples/series-anniversary.html`](../../examples/series-anniversary.html) |
| **`sui`** | 炎国「岁」系列（辞岁行/墟/界园） | 宣纸米白 `#F7F3EB` / 墨夜 `#10141A` + 朱砂 `#B82925` + 石青 `#1B7A78` | 正文标题叠 `--ak-font-serif`（`Noto Serif SC`） | `.ak-fret-box` 回纹双框、`.ak-ruby-title` / `.ak-ruby-word` 注音大字、`.ak-year-stepper`、`.ak-edge-strip` | [`examples/series-sui.html`](../../examples/series-sui.html) |
| **`exhibition`** | 奇象巡展・PFC 矢量波普 | 净白画布 `#F4F5F7` / 墨灰 `#101216` + CMY 洋红 `#FF2A85` / 亮青 `#00B7E6` / 酸橙 `#C8F000` | 默认无衬线工业体（配空心描边展示字） | `.ak-title-outline` 空心大字、`.ak-signage`、`.ak-pop-card`（CMY 三色顶条）、`.ak-gallery-masonry` + `.ak-badge-tall` | [`examples/series-exhibition.html`](../../examples/series-exhibition.html) |
| **`brawl`** | 喧闹法则・Vitafield 街头刊物 | 暖再生纸/混凝土黑 + 工业明黄 `#FFD100` | 高张力窄黑 + 等宽索引标签 | `.ak-brawl-poster`、`.ak-index-row`（`01-` + `1/4`）、`.ak-stamp-pair`、`.ak-ticket` + `.ak-barcode`、`.ak-crop-marks` | [`examples/series-brawl.html`](../../examples/series-brawl.html) |
| **`theater`** | 集成战略・暗黑剧场典籍 | 羊皮暖白/黑莓曜石 `#0F0B0D` + 丝绒深红 `#C94658` + 鎏金 `#D4AF6A` | `--ak-font-drama`（`Cormorant Garamond` + `Noto Serif SC`） | `.ak-playbill-frame` 双线剧目框、`.ak-emblem-diamond`、`.ak-dialogue`、`.ak-redacted` | [`examples/series-theater.html`](../../examples/series-theater.html) |

---

## 二、核心准则与与常规 PRTS 的显式例外边界

使用 `[data-ak-series]` 时，仍须严守 [`foundations.md`](../prts/foundations.md) 与 [`decor-and-components.md`](../prts/decor-and-components.md) 的主体架构（黑框顶栏 `.ak-header` / 黑底斜纹页脚 `.ak-footer` / `<1120px` 抽屉侧栏 / 零 `grid-template-columns` 内联硬编码 / 零 Endfield 45° 切角与霓虹发光）。仅下列**已文档化的系列特征**构成合法视觉覆盖：

1. **展示字体覆盖（`sui` 与 `theater`）**：
   - `sui` 允许 `h1`、`h2`、`.ak-hero__title .cn`、`.ak-heading__title` 采用 `--ak-font-serif`（`Noto Serif SC`）；
   - `theater` 允许 `.ak-hero__title`、`.ak-heading__title`、`.ak-playbill-frame__title` 采用 `--ak-font-drama`（`Cormorant Garamond` 回退 `Noto Serif SC`）。
   - 离线/国内环境可在项目中通过 `@fontsource/noto-serif-sc` 与 `@fontsource/cormorant-garamond` 自托管替代 Google Fonts。
2. **Wave / Pop 轻圆角卡片例外（`exhibition` 专用）**：
   - `.ak-pop-card` 在 `[data-ak-series="exhibition"]` 中刻意使用 `border-radius: 10px` 搭配顶部 CMY 6px 三色注册条 `.ak-pop-card__cmy` 与轻量投射阴影，用于还原矢量波普周边/巡展手账气质；**切勿将其滥用到非 `exhibition` 系列页面，更不得演变为通用毛玻璃 SaaS 发光卡片**。
3. **满版高饱和明黄海报名片区（`brawl` 专用）**：
   - `.ak-brawl-poster` 在明暗两套主题下均保持 `#FFD100` 明黄实底与 `#121212` 纯黑墨字，内部 `.ak-btn--primary`、`.ak-btn--contrast`、`.ak-tag` 与 `--ak-link` 已通过局部令牌锁定高对比黑黄反色，确保在暗色模式下依然可读。

---

## 三、全套系列专属组件结构参考（可直接跨框架复刻）

### 1. 布局栅格助手（内置响应式降维，替代内联 `grid`）
* `.ak-series-grid-2`（`<640px` 收单列）
* `.ak-series-grid-3`（`<1024px` 两列，`<640px` 收单列）
* `.ak-series-split`（桌面 `1.35fr : 0.85fr` 偏心分栏，`<1024px` 堆叠单列）

### 2. 平面印刷与街头档案母题（`brawl` / `sui` / `exhibition` 通用）
```html
<!-- 前导大号编号与分数角标 + 工业路牌 + 双拼印章 -->
<div class="ak-index-row">
  <span class="ak-index-no">01-</span>
  <span class="ak-index-frac">VOL.04 <sup>1/4</sup></span>
</div>

<div class="ak-stamp-pair">
  <span class="ak-stamp-pair__left">ARCHIVE</span>
  <span class="ak-stamp-pair__right">
    <span>CATALOGUE INDEXED</span>
    <small>EDITION // 2026</small>
  </span>
</div>

<div class="ak-signage">
  <span class="ak-signage__arrows">&gt;&gt;&gt;</span>
  <span>SECTION TELEMETRY</span>
</div>

<!-- 裁切线框与竖排字带 -->
<div class="ak-crop-marks">
  <div class="ak-ticket">
    <div class="ak-ticket__head"><span>DISPATCH PASS</span><span>#04</span></div>
    <div class="ak-ticket__body">
      <div class="ak-barcode" aria-hidden="true"></div>
    </div>
  </div>
</div>
<div class="ak-edge-strip" aria-hidden="true">EDITION // FOLIO 2026</div>
```

### 3. 卫戍规程・庆典绶带・岁序回纹・波普图库・剧目框
```html
<!-- 规程等级卡与带 COMPLETED 水印结算行 -->
<div class="ak-tier-list" role="radiogroup" aria-label="演练等级">
  <button type="button" class="ak-tier is-active">
    <span class="ak-tier__title"><span class="ak-tier__lv">LV.02</span> 跨区仲裁切换</span>
    <span class="ak-tag ak-tag--accent">现行 ×1.5</span>
  </button>
</div>
<div class="ak-mission-item">
  <span class="ak-mission-item__wm" aria-hidden="true">COMPLETED</span>
  <div class="ak-mission-item__main"><strong>M-01 // 网关零丢包降级切换</strong></div>
  <span class="ak-mission-item__reward">+1,200 PTS</span>
</div>

<!-- 周年对称绶带 -->
<div class="ak-ribbon-head">
  <span class="ak-ribbon-head__mark" aria-hidden="true">❖</span>
  <span>EDITION 07 · GRAND RELEASE</span>
  <span class="ak-ribbon-head__mark" aria-hidden="true">❖</span>
</div>

<!-- 岁系列回纹框 + 注音标题 + 年份步进 -->
<section class="ak-fret-box">
  <div class="ak-ruby-title">
    <div class="ak-ruby-word"><strong>岁</strong><span>SUÌ</span></div>
    <div class="ak-ruby-word"><strong>序</strong><span>XÙ</span></div>
  </div>
  <div class="ak-year-stepper" role="group" aria-label="年份切换">
    <button type="button" class="ak-year-stepper__btn" aria-label="上一年">◀</button>
    <span class="ak-year-stepper__val">2026</span>
    <button type="button" class="ak-year-stepper__btn" aria-label="下一年">▶</button>
  </div>
</section>

<!-- 波普 CMY 导览卡 & 变列宽图库 -->
<article class="ak-pop-card">
  <div class="ak-pop-card__cmy" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="ak-pop-card__body">...</div>
</article>
<div class="ak-gallery-masonry" style="--_cols: 3;">
  <article class="ak-gallery-card">
    <span class="ak-badge-tall">长图 // 1:3</span>
  </article>
</div>

<!-- 暗黑剧场双线剧目框与幕次菱形 -->
<section class="ak-playbill-frame">
  <span class="ak-emblem-diamond" aria-hidden="true"><span>VI</span></span>
  <h2 class="ak-playbill-frame__title">夜曲第四章 · 空场回声</h2>
</section>
```

---

## 四、按活动子系列进一步细分拓展方法

1. **确定底层大类后再做局部主题派生**：先在 `regulation | anniversary | sui | exhibition | brawl | theater` 中选定最贴近的主系列；再针对单一活动主题（如夏日海岸风、冬日雪境、联动乐队主题）在项目样式文件内覆盖 `[data-ak-series="..."]` 的 `--ak-accent` / `--ak-theme-accent` / `--ak-accent-2` / `--ak-bg-canvas`，同时保证亮暗两模式均各自声明对比色令牌（参考 [`SKILL.md`](../../SKILL.md) 第三步「品牌配色换皮」规则）。
2. **禁止在样板外泄露测试词或假十六进制**：复用 6 套整页模板时，必须完整替换为当前产品的真实站点名称、栏目、日期与业务编码。
