# PRTS Design 全组件目录与交互蓝图（框架无关版）

> 本手册补齐 [`decor-and-components.md`](./decor-and-components.md) 之外、[`resources/prts-design.css`](../../resources/prts-design.css)（含 [`prts-addons.css`](../../resources/prts-addons.css)）**已内置**的全部通用交互组件与领域部件。所有 HTML/CSS 均不绑定前端框架：AI 助手可直接复制语义结构与 ARIA 状态位，移植为 React / Vue / Svelte 组件或原生脚本。

---

## 一、 按钮与工具组（Button & ButtonGroup）

```html
<!-- 全部变体：主色(一处) / 黑白反转 / 默认 / 描边 / 幽灵 / 危险(可叠斜纹) / 链接 -->
<div class="ak-flex ak-wrap ak-gap-2 ak-items-center">
  <button type="button" class="ak-btn ak-btn--primary">确认部署</button>
  <button type="button" class="ak-btn ak-btn--contrast">开始行动</button>
  <button type="button" class="ak-btn">编队管理</button>
  <button type="button" class="ak-btn ak-btn--outline">详情</button>
  <button type="button" class="ak-btn ak-btn--ghost">取消</button>
  <button type="button" class="ak-btn ak-btn--danger ak-stripes">撤离</button>
  <a href="#help" class="ak-btn ak-btn--link">查看文档</a>
  <button type="button" class="ak-btn is-loading" aria-busy="true">同步中</button>
  <button type="button" class="ak-btn" disabled>已锁定</button>
</div>

<!-- 尺寸与图标钮：xs(24) / sm(30) / 默认(36) / lg(44) / xl(56) -->
<div class="ak-flex ak-wrap ak-gap-2 ak-items-center ak-mt-2">
  <button type="button" class="ak-btn ak-btn--xs">XS</button>
  <button type="button" class="ak-btn ak-btn--sm">SM</button>
  <button type="button" class="ak-btn ak-btn--lg">LG</button>
  <button type="button" class="ak-btn ak-btn--icon" aria-label="筛选">⌕</button>
  <!-- 紧贴按钮组：高亮项用 .is-active -->
  <div class="ak-btn-group" role="group" aria-label="视图切换">
    <button type="button" class="ak-btn ak-btn--sm is-active">网格</button>
    <button type="button" class="ak-btn ak-btn--sm">列表</button>
    <button type="button" class="ak-btn ak-btn--sm">矩阵</button>
  </div>
</div>
```

---

## 二、 导航、下拉菜单与分页

### 1. 下拉菜单（`.ak-dropdown` + `.ak-menu`）
* **零 JS 原生 `<details>` 写法**（CSS 已支持 `details[open] > .ak-menu`）与 **JS 受控写法**（在 `.ak-dropdown` 上切换 `.is-open`）：
```html
<!-- 写法 A：零 JS 原生开关 -->
<div class="ak-dropdown">
  <details>
    <summary class="ak-btn">操作菜单 ▾</summary>
    <div class="ak-menu">
      <div class="ak-menu__label">TACTICAL</div>
      <button type="button" class="ak-menu__item is-active">查看干员档案</button>
      <a href="#export" class="ak-menu__item">导出 JSON 数据</a>
      <div class="ak-menu__sep"></div>
      <button type="button" class="ak-menu__item ak-menu__item--danger">解散编队</button>
    </div>
  </details>
</div>

<!-- 写法 B：右对齐分组菜单（移植 React/Vue 时切换 .ak-dropdown.is-open） -->
<div class="ak-dropdown is-open">
  <button type="button" class="ak-btn ak-btn--outline" aria-expanded="true">更多操作 ▾</button>
  <div class="ak-menu ak-menu--right" role="menu">
    <div class="ak-menu__head"><span>当前节点：PRTS-04</span></div>
    <nav class="ak-menu__group">
      <div class="ak-menu__label">ACTIONS</div>
      <ul>
        <li><a href="#sync">立即同步</a></li>
        <li><button type="button" class="ak-menu__item" aria-disabled="true">只读归档</button></li>
      </ul>
    </nav>
  </div>
</div>
```

### 2. 标签页四态（`.ak-tabs`）
* 支持下划线（默认）、胶囊（`.ak-tabs--pill`）、**游戏内黑白反转块（`.ak-tabs--block`）**与左竖排（`.ak-tabset--left > .ak-tabs--vertical`）：
```html
<div class="ak-tabs ak-tabs--block" role="tablist" aria-label="干员档案">
  <button type="button" role="tab" class="ak-tab is-active" id="ak-tab0" aria-controls="ak-panel0" aria-selected="true">作战记录 <small>12</small></button>
  <button type="button" role="tab" class="ak-tab" id="ak-tab1" aria-controls="ak-panel1" aria-selected="false" tabindex="-1">基建排班</button>
  <button type="button" role="tab" class="ak-tab" id="ak-tab2" aria-controls="ak-panel2" aria-selected="false" tabindex="-1">模组任务</button>
</div>
<div class="ak-tabpanel" role="tabpanel" id="ak-panel0" aria-labelledby="ak-tab0" tabindex="0">当前激活面板内容</div>
<div class="ak-tabpanel" role="tabpanel" id="ak-panel1" aria-labelledby="ak-tab1" tabindex="0" hidden>…</div>
<div class="ak-tabpanel" role="tabpanel" id="ak-panel2" aria-labelledby="ak-tab2" tabindex="0" hidden>…</div>
```

> **ARIA 契约（必须保留，否则不合规）**：`tablist` 内每个 `tab` 带 `id` + `aria-controls`，对应 `tabpanel` 带 `id` + `aria-labelledby`；仅激活项 `tabindex="0"`，其余 `tabindex="-1"`（roving tabindex）；`←/→`（竖排用 `↑/↓`）切换焦点并激活，`Home/End` 跳首尾。参考实现见 `examples/*-components.html` 的 `initTabs()`。

### 3. 面包屑（`.ak-breadcrumb`）、路径条（`.ak-pathnav`）、分页（`.ak-pagination`）
```html
<!-- 面包屑 -->
<ol class="ak-breadcrumb">
  <li><a href="#home">罗德岛首页</a></li>
  <li><a href="#ops">干员一览</a></li>
  <li aria-current="page">陈</li>
</ol>

<!-- 游戏内路径条（斜切箭头只用于此路径条，非盒子切角） -->
<div class="ak-pathnav ak-not-prose" role="navigation" aria-label="条目路径">
  <span class="ak-pathnav__home"><a href="#home">首页</a></span>
  <span class="ak-pathnav__up"><a href="#list">近卫干员</a></span>
  <span class="ak-pathnav__here">陈 (Ch'en)</span>
</div>

<!-- 分页 -->
<nav class="ak-pagination" aria-label="分页导航">
  <button type="button" class="ak-pagination__item is-disabled" disabled>‹</button>
  <button type="button" class="ak-pagination__item is-active" aria-current="page">1</button>
  <a href="#p2" class="ak-pagination__item">2</a>
  <span class="ak-pagination__ellipsis">…</span>
  <a href="#p8" class="ak-pagination__item">8</a>
  <button type="button" class="ak-pagination__item">›</button>
</nav>
```

---

## 三、 表单与输入控件（Forms）

`scope.css` 与 `components/form.css` 已接管所有裸表单元素及 `.ak-*` 类，纯直角 + 焦距蓝描边：

```html
<!-- 标准文本 / 组合前缀 / 下拉 / 多行文本 -->
<div class="ak-field">
  <label class="ak-label" for="op-code">干员代号 <span class="req">*</span></label>
  <input id="op-code" class="ak-input" type="text" placeholder="例如 CHEN_LM04">
  <span class="ak-help">唯一识别符，支持大写字母与下划线</span>
</div>

<div class="ak-field is-invalid">
  <label class="ak-label" for="node-url">终端节点</label>
  <div class="ak-input-group">
    <span class="ak-input-group__addon">HTTPS://</span>
    <input id="node-url" class="ak-input" type="text" value="invalid node" aria-invalid="true">
  </div>
  <span class="ak-help ak-help--error">节点格式校验未通过</span>
</div>

<div class="ak-field">
  <label class="ak-label" for="prof-sel">所属职业</label>
  <select id="prof-sel" class="ak-select">
    <option>近卫 · GUARD</option>
    <option>狙击 · SNIPER</option>
    <option>术师 · CASTER</option>
  </select>
</div>

<!-- 复选（18px 纯直角）/ 单选（18px 正圆）/ 开关（40×22px 直角滑块）/ 步进器 / 滑杆 -->
<div class="ak-check-group">
  <label class="ak-check"><input type="checkbox" checked> <span>启用精英二立绘</span></label>
  <label class="ak-check"><input type="checkbox"> <span>显示潜能满级数值</span></label>
</div>

<div class="ak-check-group ak-mt-2">
  <label class="ak-check"><input type="radio" name="sort" checked> <span>按稀有度</span></label>
  <label class="ak-check"><input type="radio" name="sort"> <span>按实装时间</span></label>
</div>

<div class="ak-flex ak-wrap ak-gap-4 ak-items-center ak-mt-4">
  <label class="ak-switch"><input type="checkbox" checked> <span>自动同步终端</span></label>
  <div class="ak-number">
    <button type="button" aria-label="减少">−</button>
    <input type="number" value="7" min="1" max="10" aria-label="技能等级">
    <button type="button" aria-label="增加">+</button>
  </div>
  <input type="range" class="ak-slider" min="0" max="100" value="65" style="max-width: 180px;" aria-label="音量">
</div>
```

---

## 四、 浮层、弹窗、抽屉与反馈

### 1. 原生 `<dialog class="ak-dialog">` 与右侧抽屉 `.ak-drawer`
```html
<!-- 弹窗（JS 调用 dialog.showModal() / dialog.close()） -->
<dialog id="demo-dialog" class="ak-dialog">
  <header class="ak-dialog__head">
    <h3 class="ak-dialog__title">确认重置编队</h3>
    <button type="button" class="ak-btn ak-btn--ghost ak-btn--icon ak-btn--sm" onclick="this.closest('dialog').close()" aria-label="关闭">✕</button>
  </header>
  <div class="ak-dialog__body">
    将清空当前作战梯队配置并同步至 PRTS 终端缓存。
  </div>
  <footer class="ak-dialog__foot">
    <button type="button" class="ak-btn" onclick="this.closest('dialog').close()">取消</button>
    <button type="button" class="ak-btn ak-btn--primary" onclick="this.closest('dialog').close()">确认执行</button>
  </footer>
</dialog>

<!-- 右侧抽屉（加 .is-open 滑出）+ 遮罩（.ak-drawer-scrim.is-open，所有宽度生效，需 prts-addons.css） -->
<div class="ak-drawer-scrim" id="scrim"></div>
<aside class="ak-drawer ak-drawer--right" role="dialog" aria-modal="true" aria-label="详情抽屉">
  <!-- 内容 -->
</aside>
```
> **抽屉契约**：关闭态必须 `visibility:hidden`（`prts-addons.css` 已处理，否则 Tab 会进入屏幕外抽屉）；打开时把焦点移到抽屉内首个按钮，关闭时还给触发按钮；`Esc` 与点击遮罩均可关闭。

### 2. Toast 轻提示、气泡与纯 CSS Tooltip
```html
<!-- 角落 Toast 栈（--success / --warning / --danger） -->
<div class="ak-toasts">
  <div class="ak-toast ak-toast--success" role="status">
    <div class="ak-toast__body">
      <div class="ak-toast__title">神经连接已同步</div>
      <div>干员编队配置写入完成。</div>
    </div>
    <div class="ak-toast__progress"></div>
  </div>
</div>

<!-- 零 JS 悬停/聚焦文字提示：[data-ak-tip]；行内术语提示：.ak-term；键盘按键：.ak-kbd -->
<button type="button" class="ak-btn" data-ak-tip="按 / 快捷键可快速检索档案">快捷键说明 <kbd class="ak-kbd">/</kbd></button>
<span class="ak-term" data-ak-tip="攻击回复：每次普通攻击积累 1 点技力">技力机制</span>

<!-- 气泡卡片（需锚点 .ak-tip-anchor，点击显示） -->
<span class="ak-tip-anchor">
  <button type="button" class="ak-btn ak-btn--sm">查看节点参数</button>
  <div class="ak-popover ak-popover--bottom-start">
    <div class="ak-popover__title">中继节点 #07</div>
    <div>延迟 14ms · 在线负载 42%</div>
  </div>
</span>
```

### 3. 正文提示框（`.ak-cbox`）、手风琴（`.ak-details`）、消息横幅（`.ak-message`）
```html
<!-- Cbox（Wiki 常用正文提示框：默认蓝 / --tip 绿 / --warning 橙 / --danger 红） -->
<div class="ak-cbox ak-cbox--tip">
  <div class="ak-cbox__icon" aria-hidden="true">i</div>
  <div class="ak-cbox__body">
    <div class="ak-cbox__title">档案检索提示</div>
    本条目已更新至「怒号光明」版本数据。
  </div>
</div>

<!-- 零 JS 手风琴（原生 <details>） -->
<details class="ak-details" open>
  <summary>第一阶段 · 基础解锁条件</summary>
  <div class="ak-details__body">完成主线关卡 JT8-2 且干员信赖度达到 50%。</div>
</details>
```

---

## 五、 进度、时间线、步骤条与空状态

```html
<!-- 线性进度 / 分段进度 / 环形进度 -->
<div class="ak-progress-label"><span>MISSION SYNC</span><span>72%</span></div>
<div class="ak-progress" style="--_v: 72%;"></div>

<div class="ak-progress ak-progress--segmented ak-mt-2">
  <i class="is-on"></i><i class="is-on"></i><i class="is-on"></i><i></i><i></i>
</div>

<div class="ak-ring ak-mt-4" style="--_v: 85;"><span>85%</span></div>

<!-- 菱形时间线（严格遵守源石菱形仅限 4 处之规范） -->
<ul class="ak-timeline">
  <li class="is-done">
    <span class="ak-timeline__date">STEP 01 // COMPLETE</span>
    <div class="ak-timeline__title">核心干员集结完毕</div>
    <p class="ak-timeline__desc">完成近卫局与罗德岛联合通讯协议握手。</p>
  </li>
  <li class="is-active">
    <span class="ak-timeline__date">STEP 02 // IN PROGRESS</span>
    <div class="ak-timeline__title">突破核心城外环防御</div>
  </li>
  <li>
    <span class="ak-timeline__date">STEP 03 // PENDING</span>
    <div class="ak-timeline__title">接管主控终端控制权</div>
  </li>
</ul>

<!-- 步骤条 -->
<ol class="ak-stepper">
  <li class="ak-step is-done">验证身份</li>
  <li class="ak-step is-active">配置小队</li>
  <li class="ak-step">下达行动</li>
</ol>

<!-- 菱形加载涟漪、骨架屏与空状态 -->
<span class="ak-spinner" aria-label="加载中"></span>
<div class="ak-skeleton ak-skeleton--text"></div>
<div class="ak-empty">
  <div class="ak-empty__code">NO DATA</div>
  <p class="ak-empty__title">当前筛选条件下暂无干员记录</p>
  <button type="button" class="ak-btn ak-btn--sm">重置筛选条件</button>
</div>
```

---

## 六、 方舟领域常用数据卡速查（PRTS CSS 已内置）

以下类均已内置于 `resources/prts-design.css`，可在Wiki工具站 / 资料面板直接组合（完整示例见 [`examples/prts-components.html`](../../examples/prts-components.html)）：

| 组件 | 核心类名 | 用途要点 |
| :--- | :--- | :--- |
| **干员属性格 / 键值表** | `.ak-attrs` / `.ak-attr` / `.ak-kv` | `.ak-attrs` 1px 网格底色分割；`.ak-kv` 键值表格，数字回正文字体 |
| **攻击范围格** | `.ak-range` (`i.self`, `i.on`, `i.off`) | `--cols` 控制列数，`.ak-range--sm` 适配卡片内嵌 |
| **干员密录 / 加密档案** | `.ak-dossier` (`.is-locked`), `.ak-archive`, `.ak-redacted` | `.ak-redacted` 涂黑屏蔽词，悬停/聚焦显字 |
| **关卡卡 & 理智** | `.ak-stage` (`--hard`, `--ex`, `--story`), `.ak-stage-code`, `.ak-sanity` | 整卡链接加 `.ak-not-prose`；左侧 4px 色条直角拼接 |
| **敌人威胁评级卡** | `.ak-enemy` (`--boss`, `--elite`), `.ak-enemy__level` | 红色小菱形（源石菱形允许位）标示威胁等级 |
| **倒计时 & 活动卡** | `.ak-countdown`, `.ak-event` (`.is-live`, `.is-ended`) | 进行中带红色闪烁方点 |
| **头像与分割线** | `.ak-avatar` (`--sm|--lg`, `--round`), `.ak-divider` (`--accent`, `--text`) | 仅需要时用 `--round`，普通 UI 保持直角 |

### AI 跨框架移植约定
1. 任意框架（React/Vue/Svelte）只需保持上述 `ak-*` 类名与状态钩子（`.is-active` / `.is-open` / `.is-selected` / `aria-pressed` / `aria-selected` / `aria-expanded`）即可 1:1 复刻视觉与亮暗双主题。
2. 弹窗优先用原生 `<dialog class="ak-dialog">`（`.showModal()` 自带焦点捕获与 `Esc` 关闭）；手风琴优先 `<details class="ak-details">`；下拉菜单优先 `.ak-dropdown > details` 或在根上控制 `.is-open`。
