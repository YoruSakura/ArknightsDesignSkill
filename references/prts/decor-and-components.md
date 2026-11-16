# PRTS Design（明日方舟本家）装饰语言与组件蓝图

> 只需在页面引入 [`resources/prts-design.css`](../../resources/prts-design.css)（或通过 CDN 引入 `@mooncellwiki/prts-design-css`），并在 `<body>` 或容器上添加 `class="ak-scope"`，即可直接使用以下所有 DOM 结构与类名。

---

## 一、 根作用域与主题切换

```html
<!doctype html>
<html lang="zh-CN" data-theme="dark"> <!-- 'dark'(终端) | 'light'(档案) | 不写跟随系统 -->
<head>
  <link rel="stylesheet" href="./prts-design.css">
  <style>
    body { margin: 0; background: var(--ak-bg-canvas); }
  </style>
</head>
<body class="ak-scope">
  <!-- 页面内容 -->
</body>
</html>
```

* **局部主题**：在任意子容器上写 `<div class="ak-scope" data-theme="dark">`，该容器内部即强制使用终端暗色主题（自带画布背景色）。

---

## 二、 装饰母题（Signature Decorations）

方舟界面的「签名」是一组可叠加在任意盒子上的纯 CSS 装饰类：

### 1. 45° 警示斜纹（`.ak-stripes`）
用于危险操作、施工占位、禁用态或分隔条：
```html
<!-- 6px 高的黄黑警示分隔条 -->
<div class="ak-stripes ak-stripes--hazard ak-stripe-bar"></div>
<!-- 6px 高的红黑危险分隔条 -->
<div class="ak-stripes ak-stripes--danger ak-stripe-bar"></div>
<!-- 左缘 8px 宽黄黑警示边条的容器 -->
<div class="ak-stripe-edge" style="padding: 12px 16px 12px 20px; border: 1px solid var(--ak-border);">
  作战区域警戒提示
</div>
```

### 2. 半调网点（`.ak-halftone`）与蓝色标题条（`.ak-blue-band`）
```html
<!-- 游戏内经典蓝底 + 右侧白网点渐隐标题条 -->
<div class="ak-blue-band ak-halftone">
  <span>公开招募</span>
  <span class="ak-en ak-fs-xs" style="opacity: .8">RECRUITMENT</span>
</div>

<!-- 黑白反转 + 半调网点块 -->
<div class="ak-halftone ak-inverse" style="padding: 10px 14px; font-weight: 700;">
  终端 TERMINAL
</div>
```

### 3. 角标直角三角（`.ak-corner`）
```html
<!-- 左上角主色三角（选中态） -->
<div class="ak-corner ak-bg-surface-2 ak-p-3 ak-border">左上青色角标</div>
<!-- 右上角大号黄色三角（UP / 推荐） -->
<div class="ak-corner ak-corner--tr ak-corner--yellow ak-corner--lg ak-bg-surface-2 ak-p-3 ak-border">
  右上黄色角标
</div>
```

### 4. 终端背景纹样与大字水印
* `.ak-bg-grid`（32px 终端网格）· `.ak-bg-dots`（12px 点阵）· `.ak-bg-diag`（细斜线）· `.ak-scanlines`（扫描线伪元素）
* `.ak-brackets`：仅用于图片容器的左上/右下 L 形细线角标
* `.ak-watermark`：贴在 `position: relative; overflow: hidden` 容器右下角的 5% 透明度巨型大写英文水印：
  ```html
  <div class="ak-relative ak-border ak-p-4" style="overflow: hidden;">
    <span class="ak-watermark">RHODES ISLAND</span>
    <!-- 正文 -->
  </div>
  ```

### 5. 拉丁装饰字与编号
* `.ak-display` / `.ak-display--xl`：大号拉丁展示标题（`Novecento` / `Oswald`）
* `.ak-overline`：11px 大写灰色眉题标签（**绝不上青色**）
* `.ak-num`：面板级粗体大号 HUD 数字（**严禁放进 `<table>`**）
* `.ak-code-id`：档案编号，如 `<span class="ak-code-id">LM04 // CHEN</span>`
* `.ak-chevrons`：尾部自动带 `»` 且悬停右移的动作链接 `<a class="ak-chevrons" href="#">查看全部干员</a>`

---

## 三、 整页外壳骨架（Chrome Shell）

页眉 `.ak-header` 与页脚 `.ak-footer` 在亮暗两套主题下**永远是深黑框**（黑框白纸 / 黑框黑纸）：

```html
<!-- 1. 顶部黑色终端栏 -->
<header class="ak-header">
  <div class="ak-header__inner">
    <a class="ak-header__logo" href="#">
      <span class="ak-header__wordmark">
        PRTS.TERMINAL
        <small>RHODES ISLAND NEURAL NETWORK</small>
      </span>
    </a>
    <div class="ak-header__search">
      <button type="button" class="ak-search-trigger">
        <span class="ak-search-trigger__icon">🔍</span>
        <span class="ak-search-trigger__label">搜索干员、作战记录、档案…</span>
        <kbd class="ak-search__kbd">/</kbd>
      </button>
    </div>
    <div class="ak-header__tools">
      <!-- 亮暗主题分段开关 -->
      <div class="ak-seg" role="group" aria-label="界面主题">
        <button type="button" data-theme-btn="light">档案</button>
        <button type="button" data-theme-btn="dark" class="is-active" aria-pressed="true">终端</button>
      </div>
    </div>
  </div>
</header>

<!-- 2. 主体两列布局（左侧导轨 + 右侧主内容区） -->
<div class="ak-layout ak-layout--no-toc" style="max-width: 1680px; margin: 0 auto; padding: 24px; display: grid; grid-template-columns: 200px minmax(0, 1fr); gap: 24px;">
  <aside class="ak-sidebar">
    <div class="ak-portlet">
      <h3 class="ak-portlet__title">导航终端</h3>
      <ul>
        <li class="is-active"><a href="#">控制中枢</a></li>
        <li><a href="#">干员档案</a></li>
        <li><a href="#">作战情报</a></li>
        <li><a href="#">后勤基建</a></li>
      </ul>
    </div>
  </aside>

  <main class="ak-main">
    <!-- 页面内容 -->
  </main>
</div>

<!-- 3. 底部黑色页脚（顶缘自带 4px 青色斜纹条） -->
<footer class="ak-footer">
  <span class="ak-watermark">RHODES</span>
  <div class="ak-footer__inner">
    <div class="ak-footer__brand">
      <div class="ak-header__wordmark">PRTS.WIKI</div>
      <p>罗德岛制药公司公开信息终端 · 黑白为体，青为用。</p>
    </div>
    <div class="ak-footer__col">
      <h4>ARCHIVE // 档案</h4>
      <ul>
        <li><a href="#">干员一览</a></li>
        <li><a href="#">敌人数据库</a></li>
      </ul>
    </div>
    <div class="ak-footer__col">
      <h4>TERMINAL // 终端</h4>
      <ul>
        <li><a href="#">公开招募计算</a></li>
        <li><a href="#">基建排班表</a></li>
      </ul>
    </div>
  </div>
  <div class="ak-footer__bottom">
    <div class="ak-footer__bottom-text">
      <span class="ak-en">PRTS DESIGN SYSTEM</span>
      <span>MIT License</span>
    </div>
  </div>
</footer>
```

---

## 四、 通用 UI 组件蓝图

### 1. 章节标题（`.ak-heading`）
```html
<!-- 左侧 8px 主色粗条 + 中文粗体 + 右侧灰色大写英文（一页仅 1~2 处带英文） -->
<div class="ak-heading">
  <h2 class="ak-heading__title">作战终端概览</h2>
  <span class="ak-heading__en" lang="en">OPERATION OVERVIEW</span>
  <span class="ak-heading__aside"><a class="ak-chevrons" href="#">全部记录</a></span>
</div>

<!-- 底部细线 + 左侧 120px 主色短横条变体 -->
<div class="ak-heading ak-heading--underline">
  <h2 class="ak-heading__title">编队配置</h2>
</div>
```

### 2. 按钮（`.ak-btn`）与分段控件（`.ak-seg`）
```html
<div class="ak-flex ak-wrap ak-gap-2 ak-items-center">
  <!-- 主色按钮（一处最多一枚） -->
  <button type="button" class="ak-btn ak-btn--primary">确认部署</button>
  <!-- 黑白反转强动作（游戏内 btn_on） -->
  <button type="button" class="ak-btn ak-btn--contrast">开始行动</button>
  <!-- 默认深灰/浅灰按钮 -->
  <button type="button" class="ak-btn">编队管理</button>
  <!-- 描边按钮 -->
  <button type="button" class="ak-btn ak-btn--outline">详情</button>
  <!-- 危险斜纹按钮 -->
  <button type="button" class="ak-btn ak-btn--danger ak-stripes">放弃行动</button>
</div>
```

### 3. 标签（`.ak-tag`）、筛选芯片（`.ak-chip`）、计数徽标（`.ak-badge`）
```html
<!-- 标签（静态属性） -->
<span class="ak-tag">默认</span>
<span class="ak-tag ak-tag--accent">主色</span>
<span class="ak-tag ak-tag--yellow">提示</span>
<span class="ak-tag ak-tag--new">NEW</span>
<span class="ak-tag ak-tag--danger-solid">BREAKING</span>

<!-- 筛选芯片（可点击切换，选中时左上角带直角小三角） -->
<button type="button" class="ak-chip is-active" aria-pressed="true">近卫</button>
<button type="button" class="ak-chip" aria-pressed="false">重装</button>

<!-- 计数徽标（默认黄色正圆/胶囊，不用红色报普通未读） -->
<span class="ak-badge">8</span>
<span class="ak-badge ak-badge--danger">!</span>
```

### 4. 面板（`.ak-panel`）与卡片（`.ak-card`）
* **分工**：**面板**是页面上一块有名字的区域（左 4px 色条头栏）；**卡片**是一组并列条目中的一件。
```html
<!-- 面板 Panel（左 4px 色条 + 1px 细框 border-image 直角拼接） -->
<section class="ak-panel">
  <header class="ak-panel__head">
    <h3 class="ak-panel__title">今日轮换情报 <span class="ak-en">DAILY ROTATION</span></h3>
    <span class="ak-code-id">2026.11.16</span>
  </header>
  <div class="ak-panel__body">
    面板内容区…
  </div>
</section>

<!-- 卡片网格 Card Grid -->
<div class="ak-card-grid">
  <!-- 顶部 3px 色条卡片 -->
  <article class="ak-card ak-card--accent-top ak-card--hover">
    <div class="ak-card__body">
      <span class="ak-card__eyebrow">CHAPTER 08</span> <!-- 灰色 overline，严禁上青 -->
      <h4 class="ak-card__title">怒号光明</h4>
      <p class="ak-fs-sm ak-fg-2 ak-mt-2">切尔诺伯格核心城控制塔突入作战。</p>
    </div>
    <footer class="ak-card__footer">
      <span class="ak-tag ak-tag--accent-soft">主线剧情</span>
      <a class="ak-chevrons ak-fs-xs" style="margin-left: auto;" href="#">进入章节</a>
    </footer>
  </article>

  <!-- 选中态卡片（左上角直角三角 + 主色内描边） -->
  <article class="ak-card is-selected">
    <div class="ak-card__header">
      <h4 class="ak-card__title">战术演习 #04</h4>
      <span class="ak-tag ak-tag--accent">进行中</span>
    </div>
    <div class="ak-card__body">当前激活的演习方案。</div>
  </article>
</div>
```

### 5. 统计读数（`.ak-stat`）与属性格（`.ak-attrs`）
```html
<div class="ak-stat-row">
  <div class="ak-stat">
    <span class="ak-stat__label">OPERATORS // 已招募</span>
    <span class="ak-stat__value">284<small>/ 310</small></span>
    <span class="ak-stat__delta ak-stat__delta--up">▲ 本周 +3</span>
  </div>
  <div class="ak-stat">
    <span class="ak-stat__label">SANITY // 理智储备</span>
    <span class="ak-stat__value">135<small>/ 135</small></span>
    <span class="ak-stat__delta">自动回复中</span>
  </div>
</div>
```

### 6. 标签页（`.ak-tabs`）、消息框（`.ak-message`）、数据表（`.ak-table`）
```html
<!-- 标签页（默认底边色条 + 左上小三角；或加 ak-tabs--block 走黑白反转块） -->
<div class="ak-tabs" role="tablist">
  <button type="button" role="tab" class="ak-tab is-active" aria-selected="true">作战报表</button>
  <button type="button" role="tab" class="ak-tab" aria-selected="false">物资库存</button>
</div>

<!-- 消息框（左侧 4px 语义色条 + 1px 细框直角拼接） -->
<div class="ak-message ak-message--warning ak-mt-4">
  <div class="ak-message__body">
    <div class="ak-message__title">理智即将溢出</div>
    <div>预计 24 分钟后达到上限，请及时规划作战行动。</div>
  </div>
</div>

<!-- 数据表（数字列必须加 class="num"，使用正文字体等宽数字，严禁用 Bender） -->
<table class="ak-table ak-mt-4">
  <thead>
    <tr>
      <th>代号</th>
      <th>职业</th>
      <th>稀有度</th>
      <th class="num">生命上限</th>
      <th class="num">攻击力</th>
    </tr>
  </thead>
  <tbody>
    <tr class="is-selected">
      <td><b>维什戴尔</b></td>
      <td>狙击 · 投掷手</td>
      <td><span data-rarity="6" class="ak-r-chip">★6</span></td>
      <td class="num">2,418</td>
      <td class="num">892</td>
    </tr>
    <tr>
      <td><b>陈</b></td>
      <td>近卫 · 剑豪</td>
      <td><span data-rarity="6" class="ak-r-chip">★6</span></td>
      <td class="num">2,880</td>
      <td class="num">610</td>
    </tr>
  </tbody>
</table>
```

---

## 五、 明日方舟专属领域组件

1. **官网风 Hero 横幅（`.ak-hero`）**：黑底 + 青色眉题 + 大号拉丁字 + 220×8px 青色粗横条 + 右侧 22% 宽青色半调网点立面：
   ```html
   <section class="ak-hero">
     <div class="ak-hero__side"></div>
     <div class="ak-hero__eyebrow">RHODES ISLAND // TACTICAL TERMINAL</div>
     <h1 class="ak-hero__title">
       ARKNIGHTS PRTS
       <span class="cn">罗德岛神经连接终端</span>
     </h1>
     <div class="ak-hero__bar"></div>
     <p class="ak-hero__desc">整合泰拉大陆干员档案、作战地图、敌人情报与基建后勤数据。</p>
   </section>
   ```
2. **主界面 Breaking News 横幅（`.ak-news`）**：
   ```html
   <div class="ak-news">
     <span class="ak-news__label">BREAKING NEWS</span>
     <span class="ak-news__text">「怒号光明」主题曲复刻开启 · 新增模组系统数据已同步</span>
   </div>
   ```
3. **技能芯片（`.ak-sp*`）与关卡卡（`.ak-stage`）**：
   ```html
   <div class="ak-flex ak-gap-2 ak-items-center">
     <span class="ak-sp">自动回复</span>
     <span class="ak-sp-trigger">手动触发</span>
     <span class="ak-sp-init">15</span>
     <span class="ak-sp-cost">30</span>
     <span class="ak-sp-dur">25s</span>
   </div>
   ```
