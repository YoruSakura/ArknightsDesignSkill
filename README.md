# ArknightsDesignSkill (`arknights-design`)

面向 AI 编码助手（Antigravity / Claude Code / Cursor / Codex）的 **《明日方舟》本家（PRTS Design）** 与 **《明日方舟：终末地》（Endfield UI）** 双体系前端设计 **Skill** 与**框架无关组件参考库**。

零外部图片依赖、零构建工具门槛——不仅提供完整 CSS 令牌与样式底座，还沉淀了按需加载的设计规范、全套可跨框架移植（HTML / React / Vue / Svelte）的 DOM + WAI-ARIA 组件蓝图、整页构图样板与反模式防呆清单。

---

## 核心特性

### 1. 两套正交设计体系（严格隔离，严禁混用）

| 维度 | 体系 A · 明日方舟本家 (`PRTS Design`) | 体系 B · 明日方舟：终末地 (`Endfield UI`) |
| :--- | :--- | :--- |
| **类/令牌前缀** | `.ak-*` / `--ak-*` | `.ef-*` / `--ef-*` |
| **核心气质** | 罗德岛档案（Light）/ PRTS 终端（Dark） | 工业编辑风（Industrial Editorial）：纸白（Light）/ 烟黑（Dark） |
| **色彩哲学** | **黑白为体、青为用**：暗底配青 `#18D1FF`，亮底配游戏蓝 `#0098DC`，次强调黄 `#FFD800` | **纸与墨是主体，信号黄是唯一焦点**：13 级纯中性灰 + `#FFFA00`（单屏面积 ≤ 10%，白底字改用 `#6B5D00`） |
| **形状铁律** | **纯直角 `border-radius: 0`，严禁任何 45° 切角/斜切**；独立小装饰用源石菱形 | **形状即语义**：面板直角、按钮 4px 微圆角、核心行动/机械件单角切角或斜楔、筛选用胶囊 |
| **装饰母题** | 45° 警示斜纹、半调网点渐隐、直角三角角标、黑白反转块 | 斜纹镂空巨字（`ghost-hatch`）、滑块分节标题、方括号姓名、CMY 注册条、四角 L 形括号 |
| **领域与通用组件** | 按钮/菜单/四态页签/原生弹窗与抽屉/Toast/表单/时间线 + 干员·技能·模组·密录·剧情对话·语音声波·关卡/敌人卡 | 按钮/工具栏/三态页签/分页与步骤条/菜单气泡/表单（含菱形切换）/Combobox/日历/上传 + 测绘 HUD（Sparkline/TickRing/Viewfinder/Carousel/Schedule/Footer） |

### 2. 框架无关 · 直接照抄仿写

* **纯 CSS + 语义化 HTML**：[`resources/prts-design.css`](./resources/prts-design.css)（配 [`prts-addons.css`](./resources/prts-addons.css)）与 [`resources/endfield-standalone.css`](./resources/endfield-standalone.css) 可直接拷入任意静态页、React、Vue 3 或 Svelte 项目。
* **标准 ARIA 与状态钩子**：组件文档明确约定 `.is-active` / `.is-open` / `.is-selected`、`aria-pressed` / `aria-selected` / `aria-expanded`、`roving tabindex` 与原生 `<dialog>` / `<details>` 用法，AI 可按目标框架惯例直接封装为受控组件。
* **Tailwind v4 支持**：同步附带 [`resources/endfield-theme.css`](./resources/endfield-theme.css)（含 `@theme`、`@theme inline` 与 `@utility`）。

### 3. 渐进式披露 & 视觉防呆

* [`SKILL.md`](./SKILL.md) 控制首屏上下文开销：先判别体系，再必读 `foundations` 与母题规范，仅在需要具体控件契约时按需读取 `components-catalog.md`。
* 内置「交付前自检清单」与自动化校验脚本 [`scripts/verify.py`](./scripts/verify.py)（类名/链接/关键帧静态扫描 + Chrome 无头 1440px 桌面 & 390px 手机 × 亮/暗 16 图渲染与交互动画探针），历史真实视觉审查记录沉淀于 [`AGENTS.md`](./AGENTS.md)。

---

## 快速开始

### 在其他前端项目中接入本 Skill

将本仓库克隆或链接到目标项目的 Skill 目录（以项目级接入为例）：

```bash
# Antigravity / 通用 .agents 目录
git clone https://github.com/YoruSakura/ArknightsDesignSkill.git .agents/skills/arknights-design

# Claude Code 项目级目录（如使用软链接复用同一份目录）
mkdir -p .claude/skills && ln -s ../../.agents/skills/arknights-design .claude/skills/arknights-design
```

> 若希望所有项目全局可用，也可克隆到 `~/.agents/skills/arknights-design` 或 `~/.claude/skills/arknights-design`（遵循对应客户端的 Skill 发现路径）。

### 用 Prompt 触发测试

接入完成后，可在目标项目中直接向 AI 发出类似指令：

* **测试 PRTS 本家风格**
  > 使用 `arknights-design` skill，采用 PRTS 体系初始化一个罗德岛作战情报与干员编队管理站点，支持档案（Light）/ 终端（Dark）切换与响应式抽屉。
* **测试 Endfield 终末地风格**
  > 使用 `arknights-design` skill，采用 Endfield UI 体系搭建一个塔卫二开拓区仓储物流与产线遥测控制台，使用纸白/烟黑双主题及官方组件样式。
* **按需移植单类组件**
  > 参照 `arknights-design` 的 Endfield 组件目录，将三态楔形页签、带菱形切换方案的表单控件及原生 `<dialog>` 移植为本项目的 React / Vue 组件。

---

## 本地预览样板与组件陈列页

仓库内 `examples/` 均为零依赖静态页面（除可选的 Google Fonts 链接外无外部资源），直接用任意浏览器打开或本地起静态服务器即可交互体验亮/暗切换、抽屉、弹窗、键盘导航及菱形开关：

```bash
python3 -m http.server 8080
```

| 页面 | 定位 | 核心覆盖内容 |
| :--- | :--- | :--- |
| [`examples/prts-boilerplate.html`](./examples/prts-boilerplate.html) | PRTS 整页构图样板 | 终端顶栏、响应式侧栏抽屉、Banner、Hero 视觉区、数据矩阵表、密录档案、暗色页脚 |
| [`examples/prts-components.html`](./examples/prts-components.html) | PRTS 全组件对照与交互陈列 | 按钮/筛选芯片、`<details>`/受控下拉菜单、面包屑/路径条、WAI-ARIA 多态页签、表单、弹窗/抽屉/Toast、骨架屏/进度与干员/技能/模组/声波领域件 |
| [`examples/endfield-boilerplate.html`](./examples/endfield-boilerplate.html) | Endfield 整页构图样板 | 左侧窄轨、镂空巨字叠加排版、Hero、信号黄色带、左竖线统计块、深色数据行带（含内嵌 Sparkline 走势图）、仓储物品格与完整 Footer/回到顶部 |
| [`examples/endfield-components.html`](./examples/endfield-components.html) | Endfield 全组件对照与交互陈列 | 按钮族与展开条、三态页签、分页/步骤条、浅/强暗菜单、实色底点阵弹窗/抽屉、方圆↔菱形表单、Combobox/TagInput/文件上传/日历/排期/取景框 HUD/轮播与跑马灯 |

> **字体与离线环境说明**：原版规范提及的商业字体 `Bender`、`Novecento Sans Wide` 未随本仓库分发，样式表默认回退至 `Oswald`、`Chakra Petch`、`Archivo`、`Outfit`、`Space Grotesk`、`JetBrains Mono` 与 `Noto Sans SC`（国内网络可用 `@fontsource` 或本地 `@font-face` 自托管，两份 `components-catalog.md` 均附完整引入代码）。

---

## 目录结构

```text
ArknightsDesignSkill/
├── AGENTS.md                                 # AI 协作规范、目录修改边界与项目视觉审查记忆
├── LICENSE                                   # MIT License（本仓库）
├── NOTICE.md                                 # 上游开源项目署名、许可与商标/字体说明
├── README.md
├── SKILL.md                                  # Skill 总入口：风格路由器、渐进式披露索引、工作流与自检红线
├── references/                               # 【按需读取】深度规范与 DOM / ARIA / CSS 蓝图
│   ├── prts/
│   │   ├── foundations.md                    # PRTS 视觉哲学（黑白为体青为用、纯直角禁切角、双正典主题、令牌表）
│   │   ├── decor-and-components.md           # PRTS 装饰母题（斜纹/网点/角标/反转）与外壳/核心组件蓝图
│   │   └── components-catalog.md             # PRTS 全组件目录与 ARIA 契约（通用 UI + 方舟领域件速查）
│   └── endfield/
│       ├── foundations.md                    # Endfield 工业编辑风总纲、六条原则、角色色分工与界面家族
│       ├── motifs-and-components.md          # Endfield 母题工具类与核心展示组件
│       └── components-catalog.md             # Endfield 全组件目录与 ARIA 契约（含菱形选择控件方案）
├── resources/                                # 【可直接拷贝】零外部位图依赖 CSS 样式表与令牌
│   ├── prts-design.css                       # PRTS Design 完整单文件样式表（Standalone + Chrome 骨架）
│   ├── prts-addons.css                       # PRTS 自有补丁层（Hero/搜索快捷键/菜单按钮/滚动表/抽屉遮罩等）；紧随 prts-design.css 引入
│   ├── prts-tokens.css                       # PRTS Design 纯令牌变量文件
│   ├── endfield-standalone.css               # Endfield UI 零依赖纯 CSS 样式表（令牌 + 16 关键帧动画 + 母题 + 8.1–8.8 全套组件 + Skill 补丁层）
│   └── endfield-theme.css                    # Endfield UI Tailwind CSS v4 @theme / @utility 专用样式
├── examples/                                 # 【整页构图锚点 & 全组件可视化目录】
│   ├── prts-boilerplate.html
│   ├── prts-components.html
│   ├── endfield-boilerplate.html
│   └── endfield-components.html
└── scripts/
    ├── sync-upstream.py                      # 从本地上游仓库同步生成 prts-tokens.css / prts-design.css / endfield-theme.css
    └── verify.py                             # 静态一致性、动画关键帧审计与无头 Chrome 16 图渲染/交互探针校验脚本
```

---

## 维护与上游同步说明

若上游开源设计系统有更新，可在本地同步仓库后运行 [`scripts/sync-upstream.py`](./scripts/sync-upstream.py)，改动完成后运行 [`scripts/verify.py`](./scripts/verify.py) 做回归验证：

```bash
python3 scripts/sync-upstream.py <path-to-prts-design> <path-to-endfield-ui>
python3 scripts/verify.py --render --out /tmp/arknights-verify
```

* `resources/prts-design.css`、`resources/prts-tokens.css` 与 `resources/endfield-theme.css` 由脚本覆盖生成，**勿手改**；
* 对 PRTS 上游的兼容性修正统一写在 [`resources/prts-addons.css`](./resources/prts-addons.css)；
* [`resources/endfield-standalone.css`](./resources/endfield-standalone.css) 为手工维护的零依赖全量 CSS（末尾 `Skill 补丁层` 为本仓库自有响应式及组件修复规则），合并上游更新时需人工比对保留。

---

## 开源许可与致谢

本仓库基于 [MIT License](./LICENSE) 开源，核心规范与样式底座提炼并重构自以下优秀的社区开源项目（详细署名与版权说明见 [`NOTICE.md`](./NOTICE.md)）：

* [MooncellWiki/prts-design](https://github.com/MooncellWiki/prts-design)（MIT License · `@mooncellwiki/prts-design-css`）
* [icaruszezen/endfield-ui](https://github.com/icaruszezen/endfield-ui)（MIT License · `@endfield-ui/react`）

> 本仓库**不包含**任何上海鹰角网络科技有限公司的官方游戏位图资源或商业字体文件；《明日方舟》《明日方舟：终末地》及相关名称、视觉商标版权归上海鹰角网络科技有限公司所有。
