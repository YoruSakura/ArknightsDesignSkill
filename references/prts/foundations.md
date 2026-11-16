# PRTS Design（明日方舟本家）基础设计规范

> 来源依据：`MooncellWiki/prts-design`（MIT 协议）· `prts.wiki` 新版皮肤与明日方舟官网 / 游戏内 UI 实测规范。

---

## 一、 核心设计理念（六条铁律）

**一句话总结**：**黑白为体、青为用；直角、斜纹、网点；拉丁大写字作装饰层，中文思源做正文；终端（暗）/ 档案（亮）双正典主题。**
UI 的本质是**「罗德岛档案 / PRTS 终端」**，而不是科幻驾驶舱。

| 维度 | PRTS Design 规范 |
| :--- | :--- |
| **世界观母体** | 泰拉 · PRTS 终端（暗色） / 罗德岛人事档案（亮色） |
| **母色体系** | 黑白灰为主体 + 官网青 `#18D1FF`（暗色主强调）/ 游戏蓝 `#0098DC`（亮色主强调）+ 次强调黄 `#FFD800` + 危险红 `#C82A36` / `#A40000` |
| **形状铁律** | **纯直角 `border-radius: 0`**；角标直角三角、45° 警示斜纹填充、半调网点。**严禁 45° 切角（chamfer）/ 斜切平行四边形 / 斜带**——整套系统盒轮廓不出现 45° 斜边 |
| **光效铁律** | **无辉光（No Glow）**；层级与选中靠**色条、黑白明度反转、角标三角**表达，不用霓虹发光 |
| **字体分工** | 中文正文永远用 `Noto Sans SC` / `Source Han Sans SC`（行高 `1.7`）；大写拉丁展示字（`Novecento Sans Wide` / `Bender` / `Oswald`）仅作装饰、编号、面板级 HUD 数值 |
| **双正典主题** | 档案模式（亮，`data-theme="light"`）与终端模式（暗，`data-theme="dark"`）完全等价；页眉 `.ak-header` 与页脚 `.ak-footer` 永远保持「黑框」（无论页面亮暗，顶栏和底栏恒为深黑玻璃框） |

---

## 二、 严格 DO / DON'T 审查清单

### ✅ DO（必须做到）
1. **黑框白纸 / 黑框黑纸**：顶部导航栏（`.ak-header`）和页脚（`.ak-footer`）在亮暗主题下**恒为深黑背景**（`--ak-chrome-bg`），右侧带半调网点渐隐，配青色选中态与白色线稿图标。
2. **色条 + 1px 细框直角拼接**：标题、面板头、消息框、代码块最常见的强调是「左侧 4px 粗色条（或顶部 3px 色条）+ 1px 细框」。直接写 `border-left: 4px` + `border: 1px` 会被浏览器在转角处斜接（miter）出一道小斜边，**必须使用 `border-image` 直角拼接**：
   ```css
   border: 1px solid var(--ak-border);
   border-left-width: 4px;
   border-image: linear-gradient(to right, var(--ak-accent) 4px, var(--ak-border) 4px) 1 1 1 4;
   ```
3. **黑白反转做强动作**：游戏内「开始行动」这类强动作使用 `.ak-btn--contrast` 或 `.ak-inverse`（亮色下黑底白字、暗色下白底黑字），主色实底 `.ak-btn--primary` 一屏只放一处。
4. **源石菱形（`◆`）的克制使用**：虽然盒子轮廓严禁斜切，但**独立的小菱形**（正方形转 45°）是有意致敬「源石」的母题，仅限用于四处：
   - 无序列表项目符号（5px 旋转正方形）
   - 加载指示器 `.ak-spinner`（中央空心菱形 + 扩散涟漪菱形）
   - 时间线 `.ak-timeline` 节点（空心未到 / 主色实心已到）
   - 敌人威胁度评级（点亮的红色小菱形）
5. **整块链接组件标 `.ak-not-prose`**：当卡片（`a.ak-card` / `a.ak-op-card` / `a.ak-stage`）整体是 `<a>` 时，必须在最外层加上 `ak-not-prose`，防止正文 `a:visited` 将卡片文字染成褪色链接色。

### ❌ DON'T（绝对禁止）
1. **禁止圆角卡片、玻璃拟态、发光阴影**：除单选框（正圆）、徽标胶囊（`.ak-badge`）、环形进度（`.ak-ring`）和输入框的 `2px` 微圆角外，所有卡片、面板、按钮、标签一律 `border-radius: 0`。
2. **禁止切角（Corner Cut）与平行四边形斜切**：切角属于《终末地》游戏 HUD，**不属于明日方舟本家 PRTS Design**。
3. **禁止滥用青色给不可点击的小标签**：青色（`--ak-accent`）专属于**链接、选中态、焦点、主动作按钮、标题色条**。卡片眉题（`.ak-card__eyebrow`）、章节英文副标（`.ak-heading__en`）、属性名（`.ak-attr__label`）、统计标签（`.ak-stat__label`）必须用灰色 `--ak-fg-muted`，绝不用青色！
4. **禁止在表格数字列使用 Bender 字体**：`Bender`（`--ak-font-label`）数字是比例宽度且 14px 下笔画过细，**只用于面板级大号粗体独立数值（`.ak-num`、`.ak-stat__value`、`.ak-attr__value`）**。所有 `<table>`、`.ak-table`、`.ak-kv` 里的数字必须使用正文字体（`--ak-font-body`）+ `font-variant-numeric: tabular-nums`。
5. **禁止给成排的标题逐个配英文副标**：双语标题（中文 + 大写英文）一页只出现 1～2 处（如页面主标题、Hero 横幅、一级大章节头）。并排的卡片标题、成组的面板标题只写中文，避免满屏灰色英文造成视觉噪音。

---

## 三、 色彩令牌速查表（`--ak-*`）

直接引入本 Skill 的 [`resources/prts-design.css`](../../resources/prts-design.css) 即可获得全部令牌与组件样式。

### 1. 语义令牌（随 `data-theme="light | dark"` 自动切换，组件只用这一层）

| 语义令牌 | 档案模式（Light 默认） | 终端模式（Dark） | 用途说明 |
| :--- | :--- | :--- | :--- |
| `--ak-bg-canvas` | `#f5f5f5` | `#0f0f10` | 页面画布底色（`body` 背景） |
| `--ak-bg-surface` | `#ffffff` | `#1a1b1c` | 卡片、面板、表格、弹窗表面 |
| `--ak-bg-surface-2` | `#f5f5f5` | `#232425` | 面板头部、表头、卡片页脚、次级按钮底 |
| `--ak-bg-surface-3` | `#ebebeb` | `#2d2e30` | 按钮悬停、默认标签底、进度条轨道 |
| `--ak-bg-inset` | `#eef0f1` | `#141516` | 凹陷区域、只读输入框 |
| `--ak-bg-inverse` | `#1d1f20` | `#ffffff` | 黑白反转块底（强动作按钮、选中阶段页签） |
| `--ak-fg` | `#1d1f20` | `#f0f0f0` | 主文字颜色 |
| `--ak-fg-secondary` | `#454647` | `#c9c9c9` | 次要正文、表格表头字、默认筛选芯片字 |
| `--ak-fg-muted` | `#626262` | `#8d8d8d` | 辅助说明、overline 小标签、英文副题 |
| `--ak-fg-inverse` | `#ffffff` | `#181818` | 黑白反转块上的文字颜色 |
| `--ak-accent` | `#0098dc`（游戏蓝） | `#18d1ff`（官网青） | 主强调色：主按钮、选中边条、激活项 |
| `--ak-accent-fg` | `#ffffff` | `#000000` | 主强调色块上的文字颜色 |
| `--ak-accent-subtle` | `rgba(0,152,220,.10)` | `rgba(24,209,255,.10)` | 选中行淡青底、高亮块底 |
| `--ak-accent-2` | `#ffd800` | `#ffd800` | 次强调黄：通知计数徽标、星级、警示 |
| `--ak-border` | `#d9dbdc` | `#2f3133` | 常规 1px 边框与分隔线 |
| `--ak-border-strong` | `#b1b1b1` | `#4a4c4f` | 按钮、输入框、表头底边强边框 |
| `--ak-info` / `--ak-success` / `--ak-warning` / `--ak-danger` | `#0072a8` / `#1f8f5f` / `#b86f00` / `#c8102e` | `#5ddcff` / `#4fd18f` / `#ffb340` / `#ff5c5c` | 四态语义文字/色条色（另有对应 `-bg` 淡底） |

### 2. 方舟专属领域令牌

* **稀有度色阶（1★ ～ 6★）**：
  * 填充色：`--ak-rarity-1` (`#bababa`)、`--ak-rarity-2` (`#d3dc35`)、`--ak-rarity-3` (`#82c5f5`)、`--ak-rarity-4` (`#bf96ed`)、`--ak-rarity-5` (`#efd691`)、`--ak-rarity-6` (`#ff9433`)
  * 亮暗自适应文字色：`--ak-rarity-1-text` ～ `--ak-rarity-6-text`
  * 容器加 `data-rarity="6"` 后，内部自动注入 `--ak-r` 与 `--ak-r-text`，可直接配合 `.ak-r-chip`、`.ak-r-bar`、`.ak-r-text` 使用。
* **技能技力（SP）回复色**：
  * `--ak-sp-auto` (`#8ec31f` 自动回复)、`--ak-sp-attack` (`#fc793e` 攻击回复)、`--ak-sp-hit` (`#f4af09` 受击回复)、`--ak-sp-passive-recovery` (`#c289e3`)、`--ak-sp-passive` (`#808080` 被动)
* **游戏内富文本着色（`.ak-rt-*`）**：
  * `.ak-rt-vup`（增益蓝）、`.ak-rt-vdown`（减益橙红）、`.ak-rt-rem`（提醒橙）、`.ak-rt-kw`（关键词青蓝）、`.ak-rt-imp`（警告红）、`.ak-rt-enemy`（敌方红）、`.ak-rt-gild`（镀层绿）、`.ak-rt-term`（带虚线下划线的术语提示）

---

## 四、 字体与排版令牌

```html
<!-- 推荐在 <head> 引入开源替代字体 Oswald 与 Chakra Petch -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;600;700&family=Noto+Sans+SC:wght@400;500;700;800&family=Oswald:wght@500;700&display=swap">
```

* `--ak-font-body`：思源黑体 / Noto Sans SC（正文、标题、表格数字）
* `--ak-font-display`：Novecento Sans Wide / Oswald（拉丁大写展示字，**必配 `font-variant-numeric: lining-nums`**）
* `--ak-font-label`：Bender / Chakra Petch（HUD 标签、overline、面板大数字）
* `--ak-font-mono`：系统等宽字体（代码、键帽 `.ak-kbd`）
* 字阶：`--ak-fs-display-xl` (56px) · `--ak-fs-display` (40px) · `--ak-fs-h1` (32px) · `--ak-fs-h2` (24px) · `--ak-fs-h3` (20px) · `--ak-fs-body` (16px) · `--ak-fs-sm` (14px) · `--ak-fs-xs` (12px) · `--ak-fs-overline` (11px)
