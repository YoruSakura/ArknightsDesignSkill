# ArknightsDesignSkill (`arknights-design`)

面向 AI 编码助手（Antigravity / Claude Code / Cursor / Codex）的 **《明日方舟》本家（PRTS Design）** 与 **《明日方舟：终末地》（Endfield UI）** 双体系前端设计 Skill 库。

---

## 目录结构

```text
ArknightsDesignSkill/
├── AGENTS.md                                 # 协作规范 + 项目记忆（改动前必读，改动后更新）
├── LICENSE                                   # MIT（本仓库）；上游声明见 NOTICE.md
├── NOTICE.md                                 # 上游开源项目署名与许可
├── SKILL.md                                  # Skill 总入口：风格路由器、渐进式披露索引、开发工作流与红线自检表
├── references/                               # 【按需读取】深度设计规范与组件 DOM/CSS 蓝图
│   ├── prts/
│   │   ├── foundations.md                    # PRTS 视觉哲学（黑白为体青为用、全直角禁切角、双正典主题、令牌表）
│   │   ├── decor-and-components.md           # PRTS 装饰母题（斜纹/网点/角标/反转）与外壳/常用组件蓝图
│   │   └── components-catalog.md             # PRTS 全组件目录（按钮/菜单/弹窗/抽屉/表单/进度/时间线/领域件）
│   └── endfield/
│       ├── foundations.md                    # Endfield 工业编辑风总纲、六条核心原则、角色色分工与七大界面家族
│       ├── motifs-and-components.md          # Endfield 母题工具类（镂空巨字/滑块标题/切角/等高线/角括号）与核心展示件
│       └── components-catalog.md             # Endfield 全组件目录（三态页签/菜单/弹窗抽屉/表单含菱形/表格/反馈）
├── resources/                                # 【可直接拷贝】零外部图片依赖的完整 CSS 样式表与设计令牌
│   ├── prts-design.css                       # PRTS Design 完整单文件样式表（Standalone + Chrome 骨架）
│   ├── prts-addons.css                       # PRTS 补丁层（Hero 按钮/色面、菜单、表格滚动、抽屉遮罩）；紧随 prts-design.css 引入
│   ├── prts-tokens.css                       # PRTS Design 纯令牌变量文件
│   ├── endfield-standalone.css               # Endfield UI 零依赖纯 CSS 样式表（令牌 + 动画 + 母题 + 全套组件，全框架通用）
│   └── endfield-theme.css                    # Endfield UI Tailwind CSS v4 专用 @theme 与 @utility 样式文件
├── examples/                                 # 【整页构图锚点 & 全组件可视化目录】
│   ├── prts-boilerplate.html                 # 明日方舟本家（PRTS 终端/档案）整页网站样板
│   ├── prts-components.html                  # PRTS 全组件对照目录与交互参考（可跨框架移植）
│   ├── endfield-boilerplate.html             # 明日方舟：终末地（工业编辑风）整页网站样板
│   └── endfield-components.html              # Endfield 全组件对照目录与交互参考（含菱形表单实时切换）
└── scripts/
    └── sync-upstream.py                      # 从上游开源仓库同步最新令牌与样式的构建脚本
```

---

## 如何放入其他项目并进行组合式测试？

在任意新建的前端测试项目中，将本仓库拷贝或软链接到该项目的 `.agents/skills/arknights-design`（或 `.claude/skills/arknights-design`）：

```bash
mkdir -p /path/to/test-project/.agents/skills
cp -r /home/sakura/local本地开发/ArknightsDesignSkill /path/to/test-project/.agents/skills/arknights-design
```

随后让任意 AI 大模型在该测试项目中执行类似指令即可验收：
* **测试本家风格**：「使用 `arknights-design` skill，初始化一个明日方舟 PRTS 风格的罗德岛作战情报与干员编队管理网站样板。」
* **测试终末地风格**：「使用 `arknights-design` skill，初始化一个明日方舟：终末地工业编辑风的塔卫二开拓区物资调度与产线监控网站样板。」

---

## 开源致谢与许可

本 Skill 提炼并打包自以下两个优秀的社区开源设计系统（均采用 MIT License，本仓库不包含任何鹰角网络官方游戏位图或商业字体文件）：
* [MooncellWiki/prts-design](https://github.com/MooncellWiki/prts-design)（MIT License）
* [icaruszezen/endfield-ui](https://github.com/icaruszezen/endfield-ui)（MIT License）
