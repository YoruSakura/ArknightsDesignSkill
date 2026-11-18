---
name: arknights-integrated-strategies
description: >-
  Standalone frontend design skill inspired by Arknights Integrated Strategies eras (IS#3 Caerula Arbor,
  IS#4 Joklumarkar, IS#5 Sarkaz Furnaceside Fables, IS#6 Sui's Garden of Grotesqueries, IS#7 Blackflow).
  Provides branching expedition node maps, double-line folio frames, monthly commission ledgers, relic
  inventory inspectors, and 5 switchable era themes supporting both Light and Dark modes.
---

# Arknights Integrated Strategies Frontend Design Skill (`arknights-integrated-strategies`)

面向多路径沙盒推演、路线图决策台、专题数字典籍、遗物/成就图鉴库与月度委托看板的独立前端设计 **Skill**。
风格提炼自《明日方舟》五代「集成战略」美学档案：**萨卡兹的无终奇语（暗金光柱）**、**岁的界园志异（莲粉石青×墨夜朱砂双极）**、**水月与深蓝之树（深渊荧光）**、**探索者的银凇止境（冰原霜蓝）**与**沉沦者的黑流拟海（浸水 CRT 青灰）**。

---

## 第一步：按需读取规范与拷贝资源

开始编写代码前，先用 `read_file` 阅读规范文档：
1. **五代美学规范与真实溯源**：[`references/foundations.md`](./references/foundations.md)（含原站素材覆盖说明、5 套主题调色盘、双衬线排版规则与直角装帧红线）
2. **组件蓝图与契约**：[`references/components-and-motifs.md`](./references/components-and-motifs.md)
3. **零依赖样式表**：拷贝 [`resources/is-design.css`](./resources/is-design.css) 到目标项目；整页结构参考 [`examples/index.html`](./examples/index.html)（**严禁照搬样板业务文案**）。

---

## 第二步：初始化与构建流程

1. **注入样式与字体**：
   - 引入 `resources/is-design.css`，并在 `<html>` 设 `data-theme="dark|light"` 与 `data-is-theme="sarkaz|sui-garden|caerula|joklumarkar|blackflow"`。
   - 加载 `Noto Serif SC`、`Cormorant Garamond`、`Oswald`、`Chakra Petch`、`JetBrains Mono` 与 `Noto Sans SC`（离线可用 `@fontsource`，见规范文档）。
2. **搭建典籍骨架**：
   - 使用 `.is-header` + `<1120px` 抽屉侧栏 `.is-sidebar`（配 `.is-menu-btn` / `.is-scrim`） + `.is-layout` + `.is-footer`；
   - **禁止内联 `grid-template-columns`**，全部栏位使用 `.is-hero__grid` / `.is-hud-strip` / `.is-split` / `.is-route-map` / `.is-commission-grid` / `.is-relic-grid`。
3. **组装集成战略签名模块**：
   - 顶区：`.is-hero`（带 `.is-hero__pillars` 光柱饰线 + 右侧 `.is-hero__crest` 罗马数字编章碑牌）+ 可选 `.is-ruby-title` 括注拼音；
   - 中区交互：`.is-route-map` 3 列分支节点选择器联动右栏详情、`.is-commission-grid` 甲乙丙竖牌、`.is-relic-grid` 藏品图鉴卡及下方 `.is-relic-detail` 详述面板；
   - 底部记录：完整 WAI-ARIA `.is-tabs` 切换探索编年、`.is-redacted` 涂黑线索与 `.is-table-scroll > .is-table` 结算表。

---

## 第三步：交付前自检清单

- [ ] 全页严格保持**直角框骨与双线裱框**（`border-radius: 0`），分支节点与饰线不含 `clip-path` 45° 切角、菱形 `<polygon>` 与通用 SaaS 浮起阴影；
- [ ] **无内联 `grid-template-columns`**，且样板词汇与测试假名彻底替换为当前产品业务内容；
- [ ] `.is-hero` 恒深色底面内保持高对比文字，且五代主题切换下各按钮、标签、表格与涂黑条均对比可读；
- [ ] 实际用无头 Chrome 检查 `1440px` 桌面与 `390px`/`375px` 手机亮/暗渲染图，确认无文字压叠或横向溢出。
