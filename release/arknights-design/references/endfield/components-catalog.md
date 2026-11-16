# Endfield UI 全组件目录与交互蓝图（框架无关版）

> 本手册补全 [`motifs-and-components.md`](./motifs-and-components.md) 之外、[`resources/endfield-standalone.css`](../../resources/endfield-standalone.css) 第 8 节已内置的全套工业编辑风通用与交互组件。**零构建依赖**——AI 助手可直接复制 HTML 结构与 ARIA 状态属性，快速移植为 React / Vue / Svelte / 原生组件。
> 完整可视化对照见 [`examples/endfield-components.html`](../../examples/endfield-components.html)。

---

## 一、 按钮族、图标钮与工具栏

```html
<!-- 按钮变体：唯一信号黄(action / cut) · 默认深灰(control) · 浅灰点阵(light) · 返回斜纹(back) · 危险(danger) · 行内文字(text) -->
<div class="ef-row">
  <button type="button" class="ef-btn ef-btn--action">确认调度</button>
  <button type="button" class="ef-btn"><span>◈</span><span class="ef-btn__sep" aria-hidden="true"></span><span>保存配置</span></button>
  <button type="button" class="ef-btn ef-btn--light">取消</button>
  <button type="button" class="ef-btn ef-btn--back">← 返回</button>
  <button type="button" class="ef-btn ef-btn--danger">删除批次</button>
  <a href="#logs" class="ef-btn ef-btn--text">查看变更记录</a>
  <button type="button" class="ef-btn" disabled>已禁用</button>
</div>

<!-- 按钮组：.ef-btn-group（--sm / --between / --vertical）与图标钮：.ef-icon-btn（--plain / --accent / --inverse / --floating / --close） -->
<div class="ef-row">
  <button type="button" class="ef-icon-btn" aria-label="刷新">↻</button>
  <button type="button" class="ef-icon-btn ef-icon-btn--accent" aria-label="下一项">›</button>
  <button type="button" class="ef-icon-btn ef-icon-btn--inverse" aria-pressed="true" aria-label="固定">⌖</button>
  <button type="button" class="ef-icon-btn ef-icon-btn--floating" aria-label="上一步">←</button>
  <button type="button" class="ef-icon-btn ef-icon-btn--close" aria-label="关闭"><span>✕</span></button>
</div>

<!-- 工具栏：40px 直角轨道，激活项黑底白字 + 黄色图标记号 -->
<div class="ef-toolbar" role="toolbar" aria-label="视图工具">
  <button type="button" class="ef-toolbar__btn is-active" aria-pressed="true"><span class="ef-toolbar__icon">▤</span><span>标准</span></button>
  <button type="button" class="ef-toolbar__btn" aria-pressed="false"><span>▥</span><span>紧凑</span></button>
  <span class="ef-toolbar__sep" aria-hidden="true"></span>
  <button type="button" class="ef-toolbar__btn">导出 CSV</button>
</div>
```

---

## 二、 导航体系（Breadcrumb / PageHeader / Tabs / Pagination / Steps / Toc）

### 1. 三种官方页签（`ef-tabs`）
* `ef-tabs--block`：网站默认，**激活时文字左移让位并淡入右侧箭头**（不用黄色）；
* `ef-tabs--capsule`：筛选类目用，激活项反转黑底；
* `ef-tabs--wedge`：游戏一级页签，**斜楔画在 `::before` 上并坐在 2px 墨色基线上**（一页仅用一组）。

```html
<!-- 形态 1：官网格子式页签 -->
<div class="ef-tabs ef-tabs--block" role="tablist" aria-label="分类">
  <button type="button" role="tab" class="ef-tab is-active" id="ef-block-tab0" aria-controls="ef-block-panel0" aria-selected="true">工业概况</button>
  <button type="button" role="tab" class="ef-tab" id="ef-block-tab1" aria-controls="ef-block-panel1" aria-selected="false" tabindex="-1">供电网络</button>
  <button type="button" role="tab" class="ef-tab" id="ef-block-tab2" aria-controls="ef-block-panel2" aria-selected="false" tabindex="-1">运输清单</button>
</div>
<!-- 每个 tab 对应一个 <div class="ef-tabpanel" role="tabpanel" id="ef-block-panelN" aria-labelledby="ef-block-tabN" tabindex="0">，非激活加 hidden -->

<!-- 形态 2：胶囊页签 -->
<div class="ef-tabs ef-tabs--capsule" role="tablist" aria-label="分类">
  <button type="button" role="tab" class="ef-tab is-active" id="ef-capsule-tab0" aria-controls="ef-capsule-panel0" aria-selected="true">全部</button>
  <button type="button" role="tab" class="ef-tab" id="ef-capsule-tab1" aria-controls="ef-capsule-panel1" aria-selected="false" tabindex="-1">源石产物</button>
</div>
<!-- 每个 tab 对应一个 <div class="ef-tabpanel" role="tabpanel" id="ef-capsule-panelN" aria-labelledby="ef-capsule-tabN" tabindex="0">，非激活加 hidden -->

<!-- 形态 3：游戏楔形页签 -->
<div class="ef-tabs ef-tabs--wedge" role="tablist" aria-label="分类">
  <button type="button" role="tab" class="ef-tab is-active" id="ef-wedge-tab0" aria-controls="ef-wedge-panel0" aria-selected="true">在途批次</button>
  <button type="button" role="tab" class="ef-tab" id="ef-wedge-tab1" aria-controls="ef-wedge-panel1" aria-selected="false" tabindex="-1">历史归档</button>
</div>
<!-- 每个 tab 对应一个 <div class="ef-tabpanel" role="tabpanel" id="ef-wedge-panelN" aria-labelledby="ef-wedge-tabN" tabindex="0">，非激活加 hidden -->
```

> **ARIA 契约（必须保留，否则不合规）**：`tablist` 内每个 `tab` 带 `id` + `aria-controls`，对应 `tabpanel` 带 `id` + `aria-labelledby`；仅激活项 `tabindex="0"`，其余 `tabindex="-1"`（roving tabindex）；`←/→`（竖排用 `↑/↓`）切换焦点并激活，`Home/End` 跳首尾。参考实现见 `examples/endfield-components.html` 的 `initTabs()`。

### 2. 面包屑、页头、分页、胶囊导航器、步骤条与页内目录
```html
<!-- 面包屑（双斜杠起头 + 单斜杠分隔） -->
<ol class="ef-breadcrumb">
  <li><a href="#site">塔卫二中枢</a></li>
  <li><a href="#logistics">仓储调度</a></li>
  <li aria-current="page">批次 TR-2041</li>
</ol>

<!-- 页头：40×40 斜纹暗灰返回方块 + 微文字 + 标题 + 行动区 -->
<header class="ef-page-header">
  <span class="ef-page-header__meta">// LOGISTICS · BATCH #2041</span>
  <div class="ef-page-header__row">
    <div class="ef-page-header__main">
      <a href="#back" class="ef-page-header__back" aria-label="返回列表">←</a>
      <div>
        <h2 class="ef-page-header__title">十月第二批转运清单</h2>
        <p class="ef-page-header__desc">由北区仓储站发出，经三号管廊转运至终末地总控站。</p>
      </div>
    </div>
    <div class="ef-btn-group ef-btn-group--sm">
      <button type="button" class="ef-btn ef-btn--light">退回修订</button>
      <button type="button" class="ef-btn">签收本批</button>
    </div>
  </div>
</header>

<!-- 分页条（斜纹轨 + 方形翻页钮 + Display 等宽页码） -->
<nav class="ef-pagination" aria-label="分页">
  <button type="button" class="ef-icon-btn ef-icon-btn--sm ef-icon-btn--accent" disabled aria-label="上一页">‹</button>
  <span class="ef-pagination__counter"><strong>01</strong> / 12</span>
  <button type="button" class="ef-icon-btn ef-icon-btn--sm ef-icon-btn--accent" aria-label="下一页">›</button>
</nav>

<!-- 胶囊导航器与进度短横 -->
<div class="ef-navigator" role="group" aria-label="区段切换">
  <button type="button" class="ef-icon-btn ef-icon-btn--sm ef-icon-btn--floating" aria-label="上一项">‹</button>
  <span class="ef-navigator__body"><span class="ef-navigator__index">02 / 04</span><span>三号精炼工段</span></span>
  <button type="button" class="ef-icon-btn ef-icon-btn--sm ef-icon-btn--floating" aria-label="下一项">›</button>
</div>
<div class="ef-dash-indicator" role="img" aria-label="第 2 项，共 4 项"><i></i><i class="is-active"></i><i></i><i></i></div>

<!-- 步骤条（24px 编号方章，窄屏自动竖排） -->
<ol class="ef-steps">
  <li class="ef-step is-done">
    <div class="ef-step__head"><span class="ef-step__badge">✓</span><span class="ef-step__line"></span></div>
    <span class="ef-step__title">原料入库核验</span>
  </li>
  <li class="ef-step is-current">
    <div class="ef-step__head"><span class="ef-step__badge">02</span><span class="ef-step__line"></span></div>
    <span class="ef-step__title">管廊压力测试</span>
  </li>
  <li class="ef-step">
    <div class="ef-step__head"><span class="ef-step__badge">03</span><span class="ef-step__line"></span></div>
    <span class="ef-step__title">并网激活</span>
  </li>
</ol>
```

---

## 三、 浮层与菜单（Dropdown / Flyout / Popover / Dialog / Drawer / Toast）

* **招牌细节**：菜单与气泡顶部带 **50% 宽度信号黄强调条 + 靠左 32px 朝下小三角**；支持浅色 `.ef-menu`（当前项带左缘 3px 墨条）与固定深色 `.ef-menu--strong`（当前项整行信号黄）。

```html
<!-- 1. 零 JS 下拉菜单（<details class="ef-dropdown">，或用 .ef-menu-anchor.is-open 走 JS 控制） -->
<details class="ef-dropdown">
  <summary class="ef-btn">操作菜单 ▾</summary>
  <div class="ef-menu" role="menu">
    <div class="ef-menu__label">// ACTION</div>
    <button type="button" class="ef-menu__item is-active" role="menuitem">查看管线拓扑 <span class="ef-menu__kbd">G</span></button>
    <button type="button" class="ef-menu__item" role="menuitem">导出遥测日志</button>
    <div class="ef-menu__sep"></div>
    <button type="button" class="ef-menu__item ef-menu__item--danger" role="menuitem">紧急熔断</button>
  </div>
</details>

<!-- 2. 固定深色菜单变体 -->
<div class="ef-menu-anchor is-open">
  <button type="button" class="ef-btn ef-btn--sm">切换节点 ▾</button>
  <div class="ef-menu ef-menu--strong" role="menu">
    <button type="button" class="ef-menu__item is-active" role="menuitem">TALOS-II 主站</button>
    <button type="button" class="ef-menu__item" role="menuitem">北岭精炼厂</button>
  </div>
</div>

<!-- 3. 展开条 FlyoutBar（黑条 + 左 4px 黄线） & 零 JS 提示 [data-ef-tip] -->
<div class="ef-flyout" role="toolbar" aria-label="快捷分享">
  <button type="button" class="ef-flyout__item" data-ef-tip="复制链接">⌘</button>
  <button type="button" class="ef-flyout__item" data-ef-tip="导出图片">◫</button>
</div>

<!-- 4. 原生弹窗 <dialog class="ef-dialog">（斜纹暗黑 64px 标题带 + 点阵内衬卡片） -->
<dialog id="ef-demo-dialog" class="ef-dialog">
  <header class="ef-dialog__head">
    <h3 class="ef-dialog__title">管线参数修订</h3>
    <div class="ef-dialog__dots" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
    <button type="button" class="ef-dialog__close" onclick="this.closest('dialog').close()" aria-label="关闭"><span>✕</span></button>
  </header>
  <div class="ef-dialog__body">
    <div class="ef-dialog__card">
      修改三号管廊核心压力阈值将触发实时校准并记录至系统审计日志。
    </div>
  </div>
  <footer class="ef-dialog__foot">
    <button type="button" class="ef-btn ef-btn--light" onclick="this.closest('dialog').close()">取消</button>
    <button type="button" class="ef-btn" onclick="this.closest('dialog').close()">确认变更</button>
  </footer>
</dialog>

<!-- 5. 抽屉（加 .is-open 滑出）与 轻提示（88% 黑底） -->
<div class="ef-drawer-backdrop" id="ef-drawer-backdrop"></div>
<aside class="ef-drawer ef-drawer--accent" id="ef-demo-drawer" role="dialog" aria-modal="true" aria-label="批次回溯">
  <header class="ef-drawer__head">
    <h3 class="ef-drawer__title">批次遥测详情</h3>
    <button type="button" class="ef-icon-btn ef-icon-btn--close" aria-label="关闭抽屉"><span>✕</span></button>
  </header>
  <div class="ef-drawer__body">抽屉正文内容…</div>
</aside>

<div class="ef-toast-region" aria-live="polite">
  <div class="ef-toast ef-toast--success" role="status">
    <span class="ef-toast__tone" aria-hidden="true"></span>
    <span>已写入仓储调度台日志</span>
  </div>
</div>
```

---

## 四、 表单全控件（含菱形切换方案）

* 默认使用**方案 A（方形复选 / 圆形单选）**；在 `<html>` 或局部容器加 `data-choice="diamond"` 即可一键切换为**方案 B（全菱形符号）**。

```html
<!-- 凹陷输入框 / 凹陷区域内用描边变体 .ef-input-box--outline / 多行文本 / 下拉选择 / 验证码 -->
<div class="ef-field">
  <label class="ef-field__label" for="ef-code">中继代号 <span class="ef-field__req">*</span></label>
  <div class="ef-input-box"><input id="ef-code" class="ef-input" type="text" placeholder="TALOS-N07"></div>
  <span class="ef-field__help">标准工程编号，含连字符</span>
</div>

<div class="ef-field">
  <label class="ef-field__label" for="ef-region">目标区域</label>
  <div class="ef-input-box">
    <select id="ef-region" class="ef-select">
      <option>四号谷地 · 集成核心</option>
      <option>北岭矿区 · 东段</option>
    </select>
  </div>
</div>

<!-- 复选 / 单选 / 开关 / 双标签开关 / 分段选择 / 步进器 / 滑块 -->
<label class="ef-check"><input type="checkbox" checked> <span>启用自动负载均衡</span></label>
<label class="ef-check"><input type="radio" name="ef-mode" checked> <span>纸白档案</span></label>
<label class="ef-switch"><input type="checkbox" checked> <span>实时监控遥测</span></label>

<label class="ef-switch-dual">
  <input type="checkbox" aria-label="视角模式">
  <span class="ef-switch-dual__knob" aria-hidden="true"></span>
  <span class="ef-switch-dual__opt ef-switch-dual__opt--off">2D</span>
  <span class="ef-switch-dual__opt ef-switch-dual__opt--on">3D</span>
</label>

<div class="ef-seg" role="group" aria-label="采样频率">
  <button type="button" class="is-selected" aria-pressed="true">100ms</button>
  <button type="button" aria-pressed="false">500ms</button>
  <button type="button" aria-pressed="false">1s</button>
</div>

<div class="ef-stepper">
  <button type="button" class="ef-stepper__btn" aria-label="减少">−</button>
  <input type="text" class="ef-stepper__input" value="12" aria-label="管线数量">
  <button type="button" class="ef-stepper__btn" aria-label="增加">+</button>
</div>

<div class="ef-slider-wrap">
  <input type="range" class="ef-slider" min="0" max="100" value="60" aria-label="功率分配">
  <span class="ef-slider__val">60%</span>
</div>
```

---

## 五、 数据表格、折叠、时间线与反馈状态

```html
<!-- 1. 表格：1px 仅横线无竖线，反转黑头带 + 右对齐等宽数字 + 选中行左 4px 黄条 -->
<div class="ef-table-wrap">
  <table class="ef-table">
    <thead>
      <tr>
        <th>批次编号</th>
        <th>产线来源</th>
        <th class="num">净增量</th>
        <th class="num">负载率</th>
      </tr>
    </thead>
    <tbody>
      <tr class="is-selected">
        <td>TR-2041</td>
        <td>北岭精炼厂 #01</td>
        <td class="num">+420</td>
        <td class="num">94.2%</td>
      </tr>
      <tr>
        <td>TR-2042</td>
        <td>三号管廊枢纽</td>
        <td class="num">180</td>
        <td class="num">81.0%</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- 2. 原生 <details> 折叠面板（无外框，+ / − 号切换） -->
<div class="ef-accordion">
  <details class="ef-accordion__item" open>
    <summary class="ef-accordion__trigger">一、协议链路恢复前提</summary>
    <div class="ef-accordion__body">需保证总控站电力储备高于 80% 且无严重侵蚀干扰。</div>
  </details>
  <details class="ef-accordion__item">
    <summary class="ef-accordion__trigger">二、异常自动熔断规则</summary>
    <div class="ef-accordion__body">连续三次冷却液超支即切断反应堆输入管线。</div>
  </details>
</div>

<!-- 3. 菱形时间线（轴线不穿过空心菱形） -->
<ol class="ef-timeline">
  <li class="ef-timeline__item is-past">
    <div class="ef-timeline__axis"><span class="ef-timeline__node"></span></div>
    <div>
      <div class="ef-timeline__date">2026.11.01</div>
      <h4 class="ef-timeline__title">完成一期供电桩架设</h4>
    </div>
  </li>
  <li class="ef-timeline__item is-current">
    <div class="ef-timeline__axis"><span class="ef-timeline__node"></span></div>
    <div>
      <div class="ef-timeline__date">2026.11.16</div>
      <h4 class="ef-timeline__title">管线联调测试</h4>
      <p class="ef-timeline__desc">正在校验高纯源石结晶自动分拣节拍。</p>
    </div>
  </li>
  <li class="ef-timeline__item">
    <div class="ef-timeline__axis"><span class="ef-timeline__node"></span></div>
    <div>
      <div class="ef-timeline__date">2026.11.24</div>
      <h4 class="ef-timeline__title">正式投产</h4>
    </div>
  </li>
</ol>

<!-- 4. 通知角标（橙色方块/旋转菱形）、术语着色、进度环、空状态与完成横幅 -->
<span class="ef-badge-wrap">
  <button type="button" class="ef-icon-btn" aria-label="系统警报">!</button>
  <span class="ef-badge ef-badge--dot" aria-label="有未读提示"></span>
</span>
<span class="ef-badge">12</span>
<span class="ef-countdown">03:42:18</span>
<span class="ef-countdown ef-countdown--urgent">! 00:18:40</span>
<strong class="ef-term ef-term--info">净产出 +320</strong>
<div class="ef-ring" style="--_v: 78;"><span>78</span></div>

<section class="ef-completion-banner" role="status">
  <div>
    <h3 class="ef-completion-banner__title">开拓区三号网段验收完毕</h3>
    <p class="ef-completion-banner__desc">所有中继节点运行稳定，已解锁四级仓储转运权限。</p>
  </div>
  <button type="button" class="ef-btn ef-btn--action">签收许可</button>
  <span class="ef-completion-banner__word" aria-hidden="true">COMPLETED</span>
</section>

<!-- 5. 不确定进度、分段进度、骨架屏、空状态、任务行列表、键值属性、键盘提示与带字分割线 -->
<div class="ef-progress ef-progress--indeterminate">
  <div class="ef-progress__track" role="progressbar" aria-label="链路同步中"><div class="ef-progress__fill"></div></div>
</div>
<div class="ef-progress ef-progress--segmented">
  <div class="ef-progress__track" role="progressbar" aria-valuenow="3" aria-valuemin="0" aria-valuemax="5">
    <i class="is-on"></i><i class="is-on"></i><i class="is-on"></i><i></i><i></i>
  </div>
</div>

<div class="ef-skeleton ef-skeleton--text"></div>
<div class="ef-skeleton ef-skeleton--text"></div>
<span class="ef-spinner" role="status" aria-label="加载中"></span>
<span class="ef-kbd">CTRL+K</span>
<div class="ef-divider ef-divider--text" role="separator"><span>TELEMETRY // LOGS</span></div>

<div class="ef-empty">
  <h4 class="ef-empty__title">当前区段暂无在途清单</h4>
  <p class="ef-empty__desc">切换筛选胶囊或等待下一次自动调度周期。</p>
</div>

<div class="ef-list">
  <div class="ef-list__row is-selected"><span>核心协议链路 · 实时遥测</span><span>ACTIVE</span></div>
  <div class="ef-list__row is-completed"><span>北岭矿区初次测绘</span><span class="ef-list__done-word" aria-hidden="true">DONE</span></div>
</div>

<div class="ef-prop-list">
  <div class="ef-prop-row"><span class="ef-prop-row__k">发起站点</span><span class="ef-prop-row__v">NORTH-RIDGE #01</span></div>
</div>

<!-- 6. 顶栏 (.ef-top-bar)、页内目录 (.ef-toc)、头像切换 (.ef-avatar-switcher) 与返回顶部 (.ef-back-to-top) -->
<header class="ef-top-bar">
  <strong>ENDFIELD // OPS</strong>
  <span class="ef-top-bar__spacer"></span>
  <div class="ef-avatar-switcher">
    <span class="ef-avatar ef-avatar--sm">佩</span>
    <span class="ef-avatar is-selected">管</span>
  </div>
  <button type="button" class="ef-back-to-top" aria-label="回到顶部">↑</button>
</header>
<ul class="ef-toc">
  <li class="ef-toc__item is-current"><a href="#sec-overview">总览</a></li>
  <li class="ef-toc__item ef-toc__item--l2"><a href="#sec-power">电力拓扑</a></li>
</ul>
```

---

## 六、 高阶表单与选择器（Combobox / TagInput / Calendar / DatePicker / FileUpload / Textarea / OTP）

```html
<!-- 1. 多行文本 (.ef-textarea) 与六位分段验证码 (.ef-otp) -->
<textarea class="ef-textarea" placeholder="填写调度附注…"></textarea>
<div class="ef-otp" aria-label="六位交接口令">
  <input class="ef-otp__cell" maxlength="1" value="2" aria-label="第 1 位">
  <input class="ef-otp__cell" maxlength="1" value="0" aria-label="第 2 位">
  <input class="ef-otp__cell" maxlength="1" value="4" aria-label="第 3 位">
  <span class="ef-otp__dash" aria-hidden="true"></span>
  <input class="ef-otp__cell" maxlength="1" aria-label="第 4 位">
  <input class="ef-otp__cell" maxlength="1" aria-label="第 5 位">
  <input class="ef-otp__cell" maxlength="1" aria-label="第 6 位">
</div>

<!-- 2. 可搜索下拉组合框 (.ef-combobox，切 .is-open 展开 .ef-menu) -->
<div class="ef-combobox is-open">
  <div class="ef-input-box ef-combobox__box">
    <input class="ef-input" type="text" role="combobox" aria-expanded="true" placeholder="筛选节点编号…">
    <button type="button" class="ef-combobox__toggle" aria-label="展开候选列表">▾</button>
  </div>
  <div class="ef-menu" role="listbox">
    <button type="button" class="ef-menu__item is-active" role="option" aria-selected="true">TALOS-N07 · 北岭枢纽</button>
    <button type="button" class="ef-menu__item" role="option" aria-selected="false">TALOS-E03 · 东段矿区</button>
  </div>
</div>

<!-- 3. 多标签输入 (.ef-tag-input + .ef-tag-chip，非胶囊以区分状态与已定值) -->
<div class="ef-input-box ef-tag-input">
  <span class="ef-tag-chip">高纯源石 <button type="button" class="ef-tag-chip__del" aria-label="移除 高纯源石">✕</button></span>
  <span class="ef-tag-chip">协议核心 <button type="button" class="ef-tag-chip__del" aria-label="移除 协议核心">✕</button></span>
  <input class="ef-tag-input__entry" type="text" placeholder="回车添加关键词">
  <span class="ef-tag-input__count">2 / 8</span>
</div>

<!-- 4. 工业月历 (.ef-calendar) 与日期选择器 (.ef-datepicker) -->
<div class="ef-calendar" role="grid" aria-label="2026年11月">
  <div class="ef-cal__head">
    <button type="button" class="ef-icon-btn ef-icon-btn--sm" aria-label="上个月">‹</button>
    <span class="ef-cal__title">2026年11月</span>
    <button type="button" class="ef-icon-btn ef-icon-btn--sm" aria-label="下个月">›</button>
  </div>
  <div class="ef-cal__grid">
    <span class="ef-cal__wk">一</span><span class="ef-cal__wk">二</span><span class="ef-cal__wk">三</span><span class="ef-cal__wk">四</span><span class="ef-cal__wk">五</span><span class="ef-cal__wk">六</span><span class="ef-cal__wk">日</span>
    <button type="button" class="ef-cal__day">15</button>
    <button type="button" class="ef-cal__day is-selected is-today" aria-current="date" aria-selected="true">16</button>
    <button type="button" class="ef-cal__day is-in-range">17</button>
    <button type="button" class="ef-cal__day" disabled>18</button>
  </div>
</div>

<!-- 5. 文件上传投放区与文件行 (.ef-upload / .ef-file-item) -->
<div class="ef-upload">
  <label class="ef-upload__drop">
    <input type="file" multiple>
    <div>
      <div class="ef-upload__hint">将图纸拖至此处，或 <u>点击选择文件</u></div>
      <div class="ef-upload__desc">支持 PDF / PNG / SVG，单文件不超过 10 MB</div>
    </div>
  </label>
  <div class="ef-file-item">
    <span class="ef-file-item__ext">PDF</span>
    <span class="ef-file-item__name">north-ridge-grid-v4.pdf</span>
    <span class="ef-file-item__size">2.4 MB</span>
    <button type="button" class="ef-icon-btn ef-icon-btn--sm" aria-label="移除文件">✕</button>
    <span class="ef-file-item__bar"><i style="width: 68%;"></i></span>
  </div>
</div>
```

---

## 七、 测绘 HUD、媒体展示与动效/移植契约

```html
<!-- 1. 迷你走势面积图 (.ef-sparkline：无坐标轴网格，蓝色产出 / 红色超支，600ms 从左擦入) -->
<svg class="ef-sparkline" viewBox="0 0 120 32" preserveAspectRatio="none" aria-hidden="true">
  <polygon class="ef-sparkline__area" points="0,32 0,22 24,18 48,20 72,10 96,12 120,4 120,32"/>
  <polyline class="ef-sparkline__line" points="0,22 24,18 48,20 72,10 96,12 120,4"/>
</svg>

<!-- 2. 刻度圆环 (.ef-tick-ring)、取景角 (.ef-viewfinder，可选 .ef-viewfinder--compact-mobile 窄屏收敛)、录制闪烁 (.ef-rec)、滚动提示 (.ef-scroll-hint) 与跑马灯 (.ef-marquee) -->
<div class="ef-tick-ring ef-tick-ring--spin">
  <svg class="ef-tick-ring__svg" viewBox="0 0 240 240" aria-hidden="true">
    <circle cx="120" cy="120" r="96" fill="none" stroke="currentColor" stroke-opacity=".3"/>
    <circle cx="120" cy="120" r="112" fill="none" stroke="currentColor" stroke-opacity=".55" stroke-width="7" pathLength="400" stroke-dasharray="1.5 8.5"/>
    <path d="M120 8A112 112 0 0 1 217 64" fill="none" stroke="currentColor" stroke-opacity=".65" stroke-width="5"/>
  </svg>
  <span class="ef-tick-ring__center">ORBITAL</span>
</div>

<div class="ef-viewfinder" data-theme="dark">
  <span class="ef-viewfinder__corners" aria-hidden="true"></span>
  <span class="ef-viewfinder__crosshair" aria-hidden="true"></span>
  <span class="ef-viewfinder__ro ef-viewfinder__ro--tl">CAM // N-07</span>
  <span class="ef-viewfinder__ro ef-viewfinder__ro--br">2026.11.16</span>
</div>

<span class="ef-rec"><span class="ef-rec__dot" aria-hidden="true"></span><span class="ef-rec__br">[</span> REC <span class="ef-rec__br">]</span></span>
<div class="ef-scroll-hint" aria-hidden="true"><span class="ef-scroll-hint__label">SCROLL</span><span class="ef-scroll-hint__line"></span></div>

<!-- 3. 媒体卡 (.ef-media-card + .ef-play-mark)、轮播 (.ef-carousel)、加载页 (.ef-loader) 与工业页脚 (.ef-footer) -->
<article class="ef-media-card">
  <div class="ef-media-card__thumb"><span class="ef-play-mark ef-media-card__play" aria-hidden="true"></span></div>
  <div class="ef-media-card__meta"><span class="ef-tag">PV</span><span>// FIELD LOG · 2026.11.16</span></div>
  <h3 class="ef-media-card__title"><a href="#media">北岭自动化产线实机演示</a></h3>
</article>

<footer class="ef-footer">
  <div class="ef-hazard" style="height: 8px;" aria-hidden="true"></div>
  <div class="ef-footer__inner">
    <span class="ef-footer__meta">ENDFIELD // TALOS-II INDUSTRIAL EDITORIAL</span>
    <nav class="ef-footer__links"><a href="#top">回到顶部</a></nav>
  </div>
</footer>
```

### 动效清单、浮层交互与离线字体
1. **动画类清单**：`resources/endfield-standalone.css` 内置全部 16 个关键帧与 `.animate-{flicker,fill,scroll-hint,breathe,marquee,spin,spin-slow,blink,slide-in,turn-in,fade-in,indeterminate,indeterminate-y,pulse,bracket-in,shift-in,wipe-in}`（含 `--stagger` 与 `prefers-reduced-motion` 自动静止）。其中 `.ef-section-title__block > span` 触发 `100ms` 旋转、标题 `200ms` 淡入；`.ef-menu::before` 在展开时从左延伸；`[data-theme-switching]::view-transition-*(root)` 支持亮/暗切换平滑过渡。
2. **Dropdown / Popover 关闭契约**：受控菜单及 `<details class="ef-dropdown">` 应同时绑定「点击组件外部关闭」与 `Esc` 关闭归还焦点（完整参考实现见 [`examples/endfield-components.html`](../../examples/endfield-components.html)）。
3. **离线 / 中国大陆字体自托管**（替代 Google Fonts CDN）：
   ```css
   /* 安装：npm i @fontsource/archivo @fontsource/outfit @fontsource/space-grotesk @fontsource/jetbrains-mono @fontsource/noto-sans-sc */
   import '@fontsource/archivo/700.css';
   import '@fontsource/outfit/500.css';
   import '@fontsource/space-grotesk/500.css';
   import '@fontsource/noto-sans-sc/400.css';
   ```

