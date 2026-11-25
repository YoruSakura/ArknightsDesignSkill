# Endfield UI（明日方舟：终末地）母题与组件实现蓝图

> 本手册提供两套无缝等价的实现方案：
> 1. **方案 A（零依赖通用纯 CSS，适合任意框架 HTML / Vue / React / Vite）**：直接拷贝并引入本 Skill 的 [`resources/endfield-standalone.css`](../../resources/endfield-standalone.css)，在根节点加 `class="ef-scope"`。
> 2. **方案 B（Tailwind CSS v4 / `@endfield-ui/react`）**：拷贝 [`resources/endfield-theme.css`](../../resources/endfield-theme.css)（含 `@theme` 与 `@utility`），或直接 `pnpm add @endfield-ui/react`。

---

## 一、 字体与样式表初始化

```html
<!doctype html>
<html lang="zh-CN" data-theme="light"> <!-- 默认 light（纸白画册）；设为 dark 切至烟黑 HUD -->
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- 四个核心开源英文字体：Archivo (宽体展示)、Outfit (几何标题)、Space Grotesk (等宽技术数)、JetBrains Mono -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@125,600..800&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+SC:wght@400;500;700&family=Outfit:wght@300;500;700&family=Space+Grotesk:wght@400;500;700&display=swap">
  <link rel="stylesheet" href="./endfield-standalone.css">
</head>
<body class="ef-scope">
  <!-- 页面内容 -->
</body>
</html>
```

---

## 二、 标志性母题（Motifs）实现套路

### 1. 镂空巨字（`ghost-hatch` / `ghost-outline`）与微文字（Micro-text）
巨字（`clamp(5rem, 10.4vw, 12.5rem)`）与微文字（10–12px）成对出现，形成「200px $\rightarrow$ 10px $\rightarrow$ 16–40px 正文」的三级尺度跳越：
```html
<section style="position: relative; overflow: clip; padding: 64px 40px;">
  <!-- 背景层：斜纹镂空巨字，允许越界被容器上沿/右沿截断，必须加 aria-hidden="true" -->
  <span aria-hidden="true" class="ghost-hatch" style="position: absolute; top: -18px; left: 24px;">
    //LOGISTICS
  </span>

  <!-- 内容层（首屏 Hero 请使用文末「安全布局」的 .ef-hero / .ef-hero__ghost / .ef-hero__grid） -->
  <div style="position: relative; z-index: 1; padding-top: calc(var(--text-ghost) * 0.55);">
    <!-- 微标行：真实可读的栏目名、日期或版本号，绝不写假十六进制乱码 -->
    <p style="font-family: var(--font-tech); font-size: var(--text-xs); color: var(--ef-ink-secondary); margin: 0 0 8px;">
      // TALOS-II INDUSTRIAL NETWORK　REV 2026.11
    </p>
  </div>
</section>
```

### 2. 三种分节标题（`SectionTitle`）与方括号姓名（`BracketTitle`）
```html
<!-- 形态 A：标准分节标题（灰色滑块 + ↘ 斜箭头 + 英文在上/中文在下） -->
<header class="ef-section-title">
  <span class="ef-section-title__meta">▼ // SECTION 01</span>
  <div class="ef-section-title__row">
    <span class="ef-section-title__block" aria-hidden="true">↘</span>
    <p class="ef-section-title__en">INTEGRATED INDUSTRY</p>
  </div>
  <h2 class="ef-section-title__cn">集成工业系统</h2>
</header>

<!-- 形态 B：通栏信号黄色带标题（用于亮暗版块切换处的"换气"，一页最多 1~2 条） -->
<div class="ef-band-title">
  <div>
    <p class="ef-band-title__sub">ARKNIGHTS: ENDFIELD // TALOS-II</p>
    <h2 class="ef-band-title__main">FRONTIER DEPOT</h2>
  </div>
  <span style="font-family: var(--font-tech); font-size: var(--text-xs);">SECTOR 04 // ACTIVE</span>
</div>

<!-- 方括号标题：仅用于人物、地点、归档条目名称 [ 名称 ] -->
<h3 class="ef-bracket-title">佩丽卡</h3>
```

### 3. 注册色条（`ef-reg-strip` CMY 印刷校准条）
一个版块最多一处，放在角色名称下方或分节标签旁（页面有彩色图表时避免贴近图表）：
```html
<div aria-hidden="true" class="ef-reg-strip" style="margin: 12px 0 20px;">
  <span class="m"></span>
  <span class="c"></span>
  <span class="y"></span>
  <span class="rule"></span>
</div>
```

### 4. 45° 切角（`cut-tr`）与斜楔（`wedge-r`）——保持焦点环完整的画法
* `clip-path` 会裁掉元素的 `outline` 焦点环。**可聚焦按钮必须把切角画在 `::before` 伪元素上**（`.ef-btn--cut` 已内置此实现）；不可聚焦的小角标可直接加 `.cut-tr` / `.cut-br`：
```html
<!-- 游戏风格切角主行动按钮（一屏仅限一个黄色主行动！） -->
<button type="button" class="ef-btn ef-btn--cut">
  <span>启动基建管线</span>
</button>

<!-- 楔形一级页签（选中项黄底墨字 + 右侧斜切，坐在一条 2px 墨线上） -->
<div role="tablist" style="display: flex; gap: 4px; border-bottom: 2px solid var(--ef-ink);">
  <button type="button" role="tab" aria-selected="true"
    style="position: relative; isolation: isolate; height: 40px; padding: 0 28px 0 16px; border: 0; background: transparent; color: var(--ef-on-action); font-weight: 700; cursor: pointer;">
    <span aria-hidden="true" class="wedge-r" style="position: absolute; inset: 0; z-index: -1; background: var(--ef-action);"></span>
    在途批次
  </button>
  <button type="button" role="tab" aria-selected="false"
    style="height: 40px; padding: 0 24px 0 16px; border: 0; background: transparent; color: var(--ef-ink-secondary); font-weight: 500; cursor: pointer;">
    历史归档
  </button>
</div>
```

### 5. 角括号选中（`corner-brackets`）与测绘叠层（`Viewfinder` / `TickRing`）
* **角括号（`.corner-brackets`）**：用于物品格、图鉴矩阵的**选中态**（画在 `::after` 上，外扩 4px，带 200ms 伸展落位动画）。
* **取景角与刻度圆环（`TickRing`）**：仅用于展示性主视觉画面或三维模型/地图焦点，**严禁在普通表单页四角画取景角**：
```html
<!-- 刻度圆环 SVG（围绕主视觉焦点，两段不对称粗弧 + 40 根刻度线） -->
<svg viewBox="0 0 240 240" width="220" height="220" aria-hidden="true" class="animate-spin-slow" style="color: var(--ef-ink); pointer-events: none;">
  <circle cx="120" cy="120" r="96" fill="none" stroke="currentColor" stroke-opacity=".25" />
  <circle cx="120" cy="120" r="114" fill="none" stroke="currentColor" stroke-opacity=".4" stroke-width="8" pathLength="400" stroke-dasharray="1.5 8.5" />
  <path d="M120 6A114 114 0 0 1 219 63" fill="none" stroke="currentColor" stroke-opacity=".55" stroke-width="5" />
  <path d="M63 219A114 114 0 0 1 12 155" fill="none" stroke="currentColor" stroke-opacity=".45" stroke-width="4" />
</svg>
```

### 6. 三种背景底纹（`dot-grid` / `blueprint-grid` / `contour`）
**一屏只选一种**，且必须画在独立的 `pointer-events: none` 空装饰层上（特别是 `contour` 用了 `mask-image`，直接写在内容容器上会遮掉内容）：
```html
<div style="position: relative; overflow: clip;">
  <!-- 独立装饰层：右下角等高线，朝左上淡出 -->
  <div aria-hidden="true" class="contour" style="position: absolute; inset: 0; pointer-events: none;"></div>
  <!-- 真实内容 -->
  <div style="position: relative; z-index: 1;">…</div>
</div>
```

---

## 三、 核心组件蓝图

### 1. 应用外壳：左侧窄轨（`SideRail`）+ 偏心主舞台
```html
<div class="ef-app-shell">
  <aside class="ef-side-rail" aria-label="主导航">
    <div class="ef-side-rail__brand">
      ENDFIELD // UI
      <div style="font-family: var(--font-tech); font-size: var(--text-micro); color: var(--ef-ink-tertiary); font-weight: 400; margin-top: 2px;">
        TALOS-II TERMINAL
      </div>
    </div>
    <nav class="ef-side-rail__nav">
      <div class="ef-side-rail__group">// 调度中心</div>
      <a href="#overview" class="ef-side-rail__item is-current" aria-current="page">总览看板</a>
      <a href="#depot" class="ef-side-rail__item">物资仓库</a>
      <a href="#pipeline" class="ef-side-rail__item">产耗监控</a>
      <div class="ef-side-rail__group">// 档案</div>
      <a href="#operators" class="ef-side-rail__item">干员名册</a>
    </nav>
    <!-- 整个界面唯一的主行动块：默认反转黑底白字，悬停变信号黄底墨字 -->
    <a href="#launch" class="ef-nav-action">
      <span>▶</span>
      <span style="width: 1px; height: 14px; background: currentColor; opacity: .3;"></span>
      <span>进入拓荒区</span>
    </a>
  </aside>

  <main>
    <!-- 主舞台内容 -->
  </main>
</div>
```

### 2. 按钮组（`ef-btn`）
* **规则**：4px 微圆角；带前置图标时，图标与文字之间夹一条 `1×14px` 的 30% 透明度细竖线（`.ef-btn__sep`）；"取消 + 确认"用 `.ef-btn--light` + `.ef-btn`，把唯一的 `.ef-btn--action` 留给页面最高优先级行动：
```html
<div style="display: flex; gap: 12px; align-items: center;">
  <button type="button" class="ef-btn ef-btn--light">重置筛选</button>
  <button type="button" class="ef-btn">
    <span>⚙</span>
    <span class="ef-btn__sep" aria-hidden="true"></span>
    <span>管线配置</span>
  </button>
  <button type="button" class="ef-btn ef-btn--action">签收批次</button>
</div>
```

### 3. 名值对（`ef-tag-pair`）与胶囊族（`ef-filter-chip` / `ef-resource-chip`）
* **形状即语义**：静态归档属性用**直角无缝贴合的名值对**；可变筛选与顶部资源用**胶囊**：
```html
<!-- 直角名值对（名与值紧贴无缝，多组之间隔 8px） -->
<div style="display: flex; flex-wrap: wrap; gap: 8px;">
  <span class="ef-tag-pair">
    <span class="ef-tag-pair__key">阵营</span>
    <span class="ef-tag-pair__val">终末地工业</span>
  </span>
  <span class="ef-tag-pair ef-tag-pair--emphasis">
    <span class="ef-tag-pair__key">权限等级</span>
    <span class="ef-tag-pair__val">LEVEL 04</span>
  </span>
  <span class="ef-tag ef-tag--gain">+14.5% 产能</span>
</div>

<!-- 胶囊筛选器与资源条 -->
<div style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-top: 12px;">
  <button type="button" class="ef-filter-chip is-selected" aria-pressed="true">全部矿物</button>
  <button type="button" class="ef-filter-chip" aria-pressed="false">源石结晶</button>
  <button type="button" class="ef-filter-chip" aria-pressed="false">合成构件</button>
  <span class="ef-resource-chip" style="margin-left: auto;">
    <span class="ef-resource-chip__icon">⚡</span>
    <span>4,820 / 5,000 kW</span>
  </span>
</div>
```

### 4. 统计块（`ef-stat`）与面板（`ef-panel`）
* **统计块不装进卡片框**，靠左侧 `3px` 墨色竖线 + `// LABEL` + 大号 `Space Grotesk` 等宽数字立住：
```html
<div style="display: flex; flex-wrap: wrap; gap: 40px;">
  <div class="ef-stat">
    <span class="ef-stat__label">TOTAL OUTPUT</span>
    <div class="ef-stat__main">
      <span class="ef-stat__value" style="font-size: var(--text-5xl);">12,480</span>
      <span class="ef-stat__unit">件/时</span>
      <span class="ef-tag ef-tag--gain">+8.2%</span>
    </div>
  </div>
  <div class="ef-stat">
    <span class="ef-stat__label">LINE LOAD</span>
    <div class="ef-stat__main">
      <span class="ef-stat__value">94.2</span>
      <span class="ef-stat__unit">%</span>
    </div>
  </div>
</div>

<!-- 面板 Panel：直角 1px 线无阴影，顶部反转标题带（data-theme="inverse"）+ 左缘 4px 强调竖条 -->
<section class="ef-panel" style="margin-top: 24px;">
  <header class="ef-panel__head" data-theme="inverse">
    <h3 class="ef-panel__title">三号管廊转运明细</h3>
    <span style="font-family: var(--font-tech); font-size: var(--text-xs); opacity: .75;">BATCH // TR-2041</span>
  </header>
  <div class="ef-panel__body">
    <!-- 面板内属性行或表单 -->
  </div>
</section>
```

### 5. 物品矩阵格（`ef-item-grid` + `ef-item-slot`）
* 稀有度（`data-rarity="1..4"`）表现为**底部 40% 向上消散的渐变**（绝非整圈彩色描边）；选中态加上 `.corner-brackets`：
```html
<div class="ef-item-grid" role="group" aria-label="仓库物品矩阵">
  <button type="button" class="ef-item-slot corner-brackets" data-rarity="4" aria-pressed="true">
    <span class="ef-item-slot__new">NEW</span>
    <span style="font-family: var(--font-tech); font-weight: 700;">[高纯源石]</span>
    <span class="ef-item-slot__count">42</span>
  </button>
  <button type="button" class="ef-item-slot" data-rarity="3" aria-pressed="false">
    <span style="font-family: var(--font-tech); font-weight: 700;">[紫晶构件]</span>
    <span class="ef-item-slot__count">128</span>
  </button>
  <button type="button" class="ef-item-slot" data-rarity="2" aria-pressed="false">
    <span style="font-family: var(--font-tech); font-weight: 700;">[铁矿石]</span>
    <span class="ef-item-slot__count">960</span>
  </button>
</div>
```

### 6. 数据简报深色行带（`ef-data-list` + `ef-data-row`）
* 浅色凹陷画布上排列固定深色（`#141414`）的行带，数字严格遵守**蓝=产出（`--info`）、黄=消耗（`--accent`）、红=超支（`--danger`）**：
```html
<div class="ef-data-list" role="table" aria-label="管线产耗监控">
  <div class="ef-data-row is-fav" style="--cat-color: var(--color-data);">
    <span class="ef-data-row__cat" aria-hidden="true"></span>
    <span class="ef-data-row__dot" aria-hidden="true"></span>
    <span class="ef-data-row__name">北岭精炼厂 #01 · 晶体提纯</span>
    <span class="ef-data-row__val ef-data-row__val--info">+320 / min</span>
    <span class="ef-data-row__ref">理论 350</span>
  </div>
  <div class="ef-data-row" style="--cat-color: var(--color-alert);">
    <span class="ef-data-row__cat" aria-hidden="true"></span>
    <span class="ef-data-row__dot" aria-hidden="true"></span>
    <span class="ef-data-row__name">四号反应堆 · 冷却液循环</span>
    <span class="ef-data-row__val ef-data-row__val--danger">-45 / min (超支)</span>
    <span class="ef-data-row__ref">安全线 0</span>
  </div>
</div>
```

### 7. 凹陷输入框（`ef-input-box`）、无边框提示条（`ef-alert`）、进度条（`ef-progress`）
```html
<div class="ef-field">
  <label class="ef-field__label" for="station-id">中继站代号</label>
  <div class="ef-input-box">
    <input id="station-id" class="ef-input" type="text" placeholder="例如 TALOS-N07" />
  </div>
</div>

<!-- 进度条：灰轨 + 信号黄填充（绝不用蓝色或绿色画进度条！） -->
<div class="ef-progress" style="margin-top: 16px;">
  <div class="ef-progress__track" role="progressbar" aria-valuenow="78" aria-valuemin="0" aria-valuemax="100">
    <div class="ef-progress__fill" style="width: 78%;"></div>
  </div>
  <span class="ef-progress__val">78%</span>
</div>

<!-- 提示条：不围整圈外框，只靠 surface-raised 底 + 左缘 4px 语义色条 -->
<div class="ef-alert ef-alert--warning" role="alert" style="margin-top: 16px;">
  <strong>▲</strong>
  <div>二号矿脉采集速率下降，请检查供电桩连接状态。</div>
</div>
```

---

## 四、 通用非控制台网站原型骨架（品牌落地页 / 博客文档 / 画廊 / 登录页）

做品牌官网、产品落地页、作品集、博客文档或登录表单时，**严禁默认套用 `.ef-app-shell`（224px 后台侧轨）**，请改用 `endfield-standalone.css` 第 9 节提供的无侧栏通用网站骨架（完整可交互示范见 [`examples/endfield-landing.html`](../../examples/endfield-landing.html)）：

```html
<!-- 1. 顶部 3px 信号黄阅读进度条 + 无侧栏官网顶栏 -->
<div class="ef-read-bar" aria-hidden="true"></div>
<header class="ef-site-header">
  <div class="ef-site-header__inner">
    <a class="ef-site-header__brand" href="#top"><span class="ef-site-header__mark">KL</span><span>BRAND</span></a>
    <nav class="ef-site-header__nav">
      <a class="ef-site-header__link is-current" href="#top" aria-current="page">概览</a>
      <a class="ef-site-header__link" href="#catalog">画廊</a>
    </nav>
    <div class="ef-site-header__actions">
      <button type="button" class="ef-btn ef-btn--sm ef-site-header__cta">预约体验</button>
      <button type="button" class="ef-btn ef-btn--sm ef-site-header__menu">菜单</button>
    </div>
  </div>
</header>

<!-- 2. 无侧栏落地页首屏 (.ef-landing-hero) + 全幅内容舞台 (.ef-site-main / .ef-site-section) -->
<section class="ef-landing-hero">
  <span aria-hidden="true" class="ghost-hatch ef-hero__ghost">//SERIES</span>
  <div class="ef-site-main">
    <div class="ef-landing-hero__grid">
      <div>
        <h1 class="ef-landing-hero__title">主标题</h1>
        <p class="ef-landing-hero__lead">副标题导语…</p>
      </div>
      <div>右侧焦点产品/视觉块</div>
    </div>
  </div>
</section>

<div class="ef-site-main">
  <!-- 3. 无边框特性分栏 (.ef-feature-grid)、产品/作品画廊 (.ef-gallery-grid) 与定价方案 (.ef-pricing-grid) -->
  <section class="ef-site-section">
    <div class="ef-feature-grid">
      <article class="ef-feature-item ef-reveal"><span class="ef-feature-item__num">01</span><h3 class="ef-feature-item__title">特性</h3><p class="ef-feature-item__desc">说明</p></article>
    </div>
    <div class="ef-gallery-grid">
      <button type="button" class="ef-showcase-card ef-reveal">
        <div class="ef-showcase-card__media"><span class="ef-showcase-card__code">ID // 01</span><span class="ef-showcase-card__fig">MODEL</span></div>
        <div class="ef-showcase-card__body"><div class="ef-showcase-card__head"><h3 class="ef-showcase-card__title">名称</h3><span class="ef-showcase-card__price">¥2,499</span></div><p class="ef-showcase-card__desc">摘要</p></div>
      </button>
    </div>
    <div class="ef-pricing-grid">
      <article class="ef-plan-card ef-plan-card--featured"><h3 class="ef-plan-card__name">方案</h3><div class="ef-plan-card__price">¥299<small>/ 月</small></div><ul class="ef-plan-card__list"><li>权益条目</li></ul></article>
    </div>
  </section>

  <!-- 4. 长文博客/文档阅读壳 (.ef-article-shell + .ef-prose) -->
  <div class="ef-article-shell">
    <article class="ef-prose"><h2>章节</h2><p>72ch 舒适阅读正文…</p></article>
    <aside><ul class="ef-toc"><li class="ef-toc__item is-current"><a href="#">目录</a></li></ul></aside>
  </div>
</div>

<!-- 5. 登录 / 表单向导分屏壳 (.ef-auth-shell) -->
<div class="ef-auth-shell">
  <section class="ef-auth-brand">左侧深色品牌宣言</section>
  <section class="ef-auth-card">右侧极简表单</section>
</div>
```

---

## 附：Hero 与镂空巨字的安全布局（防重叠）

镂空巨字（`ghost-hatch`）是**背景层**，必须与标题/面包屑分层，否则会出现文字叠压、被裁切的事故：

```html
<section class="ef-hero">
  <span aria-hidden="true" class="ghost-hatch ef-hero__ghost">//PERLICA</span>
  <div class="ef-hero__grid"> <!-- 内容层：自带 padding-top = 巨字高度 × 0.65，且 z-index:1 -->
    …标题 / 方括号姓名 / 行动按钮…
  </div>
</section>
```

- 禁止对巨字与内容层使用同一坐标系的 `top: 0`；巨字只允许“越界截断”，不允许压在可读文字上。
- 版块布局只用 `.ef-hero__grid` / `.ef-split` / `.ef-stat-row` / `.ef-section`（已含手机断点），不要写内联 `grid-template-columns`。
- `.ef-app-shell` 手机列必须是 `minmax(0,1fr)`，否则内容会撑出视口。
