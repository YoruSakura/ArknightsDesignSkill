# PRTS Design（明日方舟本家）双载体骨架、建筑母题与核心蓝图

> 只需在页面先后引入 [`resources/prts-design.css`](../../resources/prts-design.css) 与官网架构扩展层 [`resources/prts-addons.css`](../../resources/prts-addons.css)，并在 `<body>` 上加 `class="ak-scope"`，即可按需选用「官网展示（Carrier 1）」或「Wiki 档案终端（Carrier 2）」两大骨架及全套 `.ak-*` 组件。

---

## 一、 根作用域、氛围画布与主题切换

```html
<!doctype html>
<html lang="zh-CN" data-theme="dark"> <!-- 'dark'(官网/终端默认) | 'light'(档案制图白) -->
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="./prts-design.css">
  <link rel="stylesheet" href="./prts-addons.css">
  <style>body { margin: 0; min-height: 100vh; display: flex; flex-direction: column; }</style>
</head>
<!-- 加 .ak-bg-lattice 启用官网三角网格暗格 + 对角斜光 + 左下角半调渐隐 -->
<body class="ak-scope ak-bg-lattice">
  <!-- 页面内容 -->
</body>
</html>
```

* **局部异色区域**：在子容器上声明 `class="ak-scope" data-theme="dark"` 可锁定局部终端暗底（常见于亮色文档页中的控制台预览窗）。

---

## 二、 载体 1：官网展示与指挥门户骨架（默认首选，对齐 `ak.hypergryph.com`）

适用于着陆页、品牌产品站、战区/业务指挥总览与情报门户：**去左侧大百科栏、去套娃卡片边框**。

### 1. 极简漂浮双语顶栏（`.ak-topbar`）+ 右侧标尺窄轨（`.ak-stage-shell` / `.ak-index-rail`）
```html
<header class="ak-topbar">
  <div class="ak-topbar__inner">
    <a class="ak-topbar__brand" href="#index">
      <span class="ak-topbar__mark" aria-hidden="true">RI</span>
      <span class="ak-topbar__wordmark">PRTS.TERMINAL<small>COMMAND NETWORK</small></span>
    </a>
    <nav class="ak-topbar__nav" aria-label="主导航">
      <a class="ak-topbar__link is-active" href="#index" aria-current="page"><strong>INDEX</strong><span>首页概览</span></a>
      <a class="ak-topbar__link" href="#information"><strong>INFORMATION</strong><span>情报中心</span></a>
      <a class="ak-topbar__link" href="#archive"><strong>DIRECTORY</strong><span>档案矩阵</span></a>
    </nav>
    <div class="ak-topbar__tools">
      <button type="button" class="ak-wave-btn is-playing" aria-pressed="true" aria-label="切换终端信号声波">
        <span class="ak-wave-bars" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span>
        <span>SIGNAL</span>
      </button>
      <div class="ak-seg" role="group" aria-label="界面主题切换">
        <button type="button" aria-pressed="false">档案</button>
        <button type="button" class="is-active" aria-pressed="true">终端</button>
      </div>
      <button type="button" class="ak-topbar__menu" id="ak-menu-btn" aria-controls="ak-nav-drawer" aria-expanded="false">菜单</button>
    </div>
  </div>
</header>

<div class="ak-stage-shell">
  <main class="ak-stage-main">
    <!-- 主舞台内容（见下文各核心机关） -->
  </main>
  <aside class="ak-index-rail" aria-label="章节索引">
    <div class="ak-index-rail__sticky">
      <div class="ak-index-rail__counter">
        <span class="ak-index-rail__num">01</span>
        <div class="ak-index-rail__meta">// <span>01 / 04</span><span>INDEX</span></div>
      </div>
      <nav class="ak-rail-nav">
        <a class="ak-rail-nav__item is-active" href="#index"><span>01</span><span>首页概览</span></a>
        <a class="ak-rail-nav__item" href="#information"><span>02</span><span>情报中心</span></a>
      </nav>
      <div class="ak-index-rail__status"><div>LINK // ONLINE</div><div>REV // 2026.11</div></div>
    </div>
  </aside>
</div>
```

### 2. 无边框开放 Hero（`.ak-hero--editorial`）与焦点击选卡（`.ak-brief` + `.ak-thumb-grid`）
* 用**开放三角暗格舞台 + 左下截断巨字 `.ak-ghost-word` + 短青实条延伸细线 `.ak-hero--editorial__rule`** 取代笨重的黑底白框与空心点阵占位块：
```html
<section class="ak-hero--editorial" id="index">
  <span class="ak-ghost-word" aria-hidden="true">RHODES // PRTS</span>
  <div class="ak-hero--editorial__grid">
    <div>
      <div class="ak-hero--editorial__eyebrow"><i aria-hidden="true"></i><span>COMMAND // BUILD 4.2</span></div>
      <h1 class="ak-hero--editorial__title ak-anim-scan">
        ARKNIGHTS PRTS
        <span class="cn">罗德岛战术情报门户</span>
      </h1>
      <div class="ak-hero--editorial__rule ak-anim-wipe" aria-hidden="true"></div>
      <p class="ak-hero--editorial__desc">去边框化工业架构与非对称错位情报流。</p>
      <div class="ak-flex ak-wrap ak-gap-3 ak-mt-6">
        <a class="ak-btn ak-btn--contrast ak-btn--lg" href="#archive">检视作战矩阵</a>
        <a class="ak-btn ak-btn--primary ak-btn--lg" href="#information">最新调度简报</a>
      </div>
    </div>

    <div class="ak-hero__focal">
      <div class="ak-brief" aria-live="polite">
        <div class="ak-brief__head">
          <span class="ak-brief__name">凯尔希</span>
          <span class="ak-brief__en">KAL'TSIT // SW03</span>
        </div>
        <div class="ak-brief__voice">医疗部门总负责人 · TERMINAL READY</div>
        <p class="ak-brief__copy">直接督导外勤战术编队调度与极端环境应急救援协议。</p>
      </div>
      <div class="ak-thumb-grid" role="group" aria-label="核心焦点切换">
        <button type="button" class="ak-thumb-card is-active" aria-pressed="true">
          <span class="ak-thumb-card__code">01 // MED</span>
          <span class="ak-thumb-card__name">凯尔希</span>
        </button>
        <button type="button" class="ak-thumb-card" aria-pressed="false">
          <span class="ak-thumb-card__code">02 // CMD</span>
          <span class="ak-thumb-card__name">阿米娅</span>
        </button>
      </div>
      <div class="ak-scrub-bar" aria-hidden="true"><i style="--_thumb-x: 0%;"></i></div>
    </div>
  </div>
</section>
```

### 3. 去框化核心机关（`.ak-rule` / `.ak-stat--minimal` / `.ak-folio-list` / `.ak-news-grid` / `.ak-showcase-strip`）
```html
<!-- A. 1px 建筑标尺分割线（左端 4px 实块） -->
<div class="ak-rule">
  <div class="ak-rule__head">
    <h2 class="ak-rule__title">情报中心</h2>
    <span class="ak-rule__en" lang="en">INFORMATION</span>
  </div>
  <span class="ak-rule__aside">02 // LIVE FEED</span>
</div>

<!-- B. 去框化指标读数（无四面方框，仅顶线 + 左端 28px 青色短块） -->
<div class="ak-stat-row--open">
  <div class="ak-stat--minimal">
    <span class="ak-stat__label">DEPLOYED // 现役编队</span>
    <span class="ak-stat__value">12<small>/ 12</small></span>
    <span class="ak-stat__delta ak-stat__delta--up">▲ 满员待命</span>
  </div>
</div>

<!-- C. 非对称双栏 (.ak-split) + 筛选条 (.ak-filter-strip) + 无边框清单 (.ak-folio-list) -->
<div class="ak-split">
  <div>
    <div class="ak-filter-strip" role="group" aria-label="情报筛选">
      <button type="button" class="ak-filter-strip__btn is-active" aria-pressed="true">最新</button>
      <button type="button" class="ak-filter-strip__btn" aria-pressed="false">公告</button>
    </div>
    <div class="ak-folio-list">
      <button type="button" class="ak-folio-item is-active">
        <span class="ak-folio-item__main">
          <span class="ak-folio-item__meta">新闻 · 2026 // 11 / 18</span>
          <span class="ak-folio-item__title">第 71 期战区后勤调度纪要</span>
        </span>
        <span class="ak-folio-item__arrow" aria-hidden="true">›</span>
      </button>
    </div>
    <a class="ak-folio-more ak-chevrons" href="#archive">VIEW ALL DISPATCHES</a>
  </div>

  <!-- D. 错位双列新闻卡（右列自动下沉错位，头部可选 --grid / --halftone 底纹与 --inverse 角标） -->
  <div class="ak-news-grid ak-news-grid--staggered">
    <a class="ak-news-card" href="#archive">
      <div class="ak-news-card__head ak-news-card__head--grid">
        <span class="ak-news-card__seal">RI // 01</span>
        <span class="ak-news-card__en">DISPATCH</span>
        <span class="ak-news-card__sub">战术调度</span>
        <span class="ak-news-card__band ak-news-card__band--inverse">— TERMINAL</span>
      </div>
      <div class="ak-news-card__body">
        <span class="ak-news-card__cat">新闻</span>
        <span class="ak-news-card__date">2026 // 11 / 18</span>
        <h3 class="ak-news-card__title">切尔诺伯格外环观测站重连完成</h3>
      </div>
    </a>
  </div>
</div>

<!-- E. 四列通栏暗幕切割条 + 官网极简页脚 -->
<div class="ak-showcase-strip">
  <a class="ak-showcase-col" href="./prts-components.html">
    <span class="ak-showcase-col__mark" aria-hidden="true">01</span>
    <h3 class="ak-showcase-col__title">通用组件百科</h3>
    <span class="ak-showcase-col__en">COMPONENT CATALOG</span>
    <span class="ak-showcase-col__more">VIEW MORE ›</span>
  </a>
</div>
<footer class="ak-footer ak-footer--editorial">
  <span class="ak-watermark" aria-hidden="true">RHODES</span>
  <div class="ak-footer__inner">…</div>
</footer>
```

> 移动端抽屉入口 `#ak-menu-btn` 配合 `<aside class="ak-drawer ak-drawer--left">` 与 `<div class="ak-drawer-scrim">` 使用，内部列表结构用 `.ak-drawer-nav` / `.ak-drawer-nav__head` / `.ak-drawer-nav__link`。

---

## 三、 载体 2：PRTS 资料百科与密集表单外壳（Wiki / Console）

当需求明确为**百科词条站、文档中心、多级导航图鉴或高密度后台表格**时，采用 `MooncellWiki/prts-design` 经典三列页眉与左侧树状侧栏骨架（完整交互见 [`examples/prts-components.html`](../../examples/prts-components.html)）：

```html
<header class="ak-header">
  <div class="ak-header__inner">
    <a class="ak-header__logo" href="#">
      <span class="ak-header__wordmark">PRTS.WIKI<small>RHODES ARCHIVE</small></span>
    </a>
    <div class="ak-header__search">
      <button type="button" class="ak-search-trigger">
        <span class="ak-search-trigger__icon">⌕</span>
        <span class="ak-search-trigger__label">检索干员档案、关卡、模组…</span>
        <kbd class="ak-search__kbd">/</kbd>
      </button>
    </div>
    <div class="ak-header__tools">
      <div class="ak-seg" role="group" aria-label="界面主题">
        <button type="button" aria-pressed="false">档案</button>
        <button type="button" class="is-active" aria-pressed="true">终端</button>
      </div>
    </div>
  </div>
  <nav class="ak-local-nav" aria-label="页面菜单">
    <button type="button" class="ak-local-nav__btn ak-local-nav__menu" id="ak-menu-btn" aria-controls="ak-sidebar" aria-expanded="false">菜单</button>
  </nav>
</header>
<div class="ak-drawer-scrim" id="ak-scrim"></div>

<div class="ak-layout ak-layout--no-toc">
  <aside class="ak-sidebar" id="ak-sidebar">
    <div class="ak-portlet">
      <h3 class="ak-portlet__title">DATABASE // 目录</h3>
      <ul><li class="is-active"><a href="#">干员一览</a></li></ul>
    </div>
  </aside>
  <main class="ak-main">…</main>
</div>
```

---

## 四、 签名装饰工具类与经典通用组件

* **背景纹理与大字**：`.ak-bg-grid`（32px 终端网格）· `.ak-bg-dots` · `.ak-bg-diag` · `.ak-scanlines` · `.ak-brackets`（图片容器角标）· `.ak-watermark`
* **警示斜纹（仅限危险/占位，勿作页脚常规装饰）**：`.ak-stripes`（`--hazard` / `--danger`）+ `.ak-stripe-bar` / `.ak-stripe-edge`
* **角标与网点**：`.ak-corner`（`--tr` / `--yellow` / `--lg`）· `.ak-halftone` · `.ak-blue-band` · `.ak-inverse`
* **行动与指示**：`.ak-chevrons`（悬停右移 `»`）· `.ak-code-id` · `.ak-overline` · `.ak-display` · `.ak-num`
* **按钮、面板、消息与滚表**：
```html
<div class="ak-flex ak-wrap ak-gap-2 ak-items-center">
  <button type="button" class="ak-btn ak-btn--primary">主行动</button>
  <button type="button" class="ak-btn ak-btn--contrast">强动作反转</button>
  <button type="button" class="ak-btn ak-btn--outline">描边</button>
  <button type="button" class="ak-btn ak-btn--danger ak-stripes">危险操作</button>
</div>

<!-- 表格必须外包 .ak-table-scroll 防 390px 挤压；数字列用 <td class="num"> 走正文等宽数字 -->
<div class="ak-table-scroll">
  <table class="ak-table">
    <thead><tr><th>干员代号</th><th>职业</th><th class="num">生命上限</th></tr></thead>
    <tbody><tr class="is-selected"><td><b>陈</b> <span class="ak-code-id">LM04</span></td><td>近卫</td><td class="num">2,880</td></tr></tbody>
  </table>
</div>
```

> 更多通用组件（下拉菜单、四态页签、原生 `<dialog>`、右侧 `.ak-drawer`、Toast、表单控件）与方舟领域组件（`.ak-op-card`、`.ak-skill`、`.ak-module`、`.ak-dossier`、`.ak-stage`）见按需目录 [`components-catalog.md`](./components-catalog.md)。
