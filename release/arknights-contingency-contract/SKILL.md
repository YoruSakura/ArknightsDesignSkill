---
name: arknights-contingency-contract
description: >-
  Standalone frontend design skill inspired by Arknights Contingency Contract / Battleplan Arclight /
  Stronghold Protocol Regulation / Vector Breakthrough / DOS high-difficulty tactical systems. Provides
  orthogonal industrial layout grids, broadcast-scale score Hero, interactive Contract Tag Matrix
  (契约调整), tier/wave selectors, and 4 switchable themes with Light/Dark support.
---

# Arknights Contingency Contract Frontend Design Skill (`arknights-contingency-contract`)

面向高难战术契约推演、混沌工程演练台、压力测试评分系统与高对比度工业监控面板的独立设计 **Skill**。
核心风格凝练自《明日方舟》**行动协议「弧光行动」**、**卫戍协议「规程」（含契约调整）**、**矢量突破**与 **DOS 纷争演绎**四大高难挑战视觉体系，具备完整的多主题切换与纯直角响应式骨骼。

---

## 第一步：按需读取规范与拷贝资源

开始编码前，必须先用 `read_file` 阅读规范文档：
1. **必读基础与色彩矩阵**：[`references/foundations.md`](./references/foundations.md)（含原站素材溯源与诚实边界、4 套主题令牌、品牌换色接口与排版铁律）
2. **组件蓝图与交互契约**：[`references/components-and-motifs.md`](./references/components-and-motifs.md)（按需对照 DOM/ARIA/JS 契约）
3. **零依赖样式表**：拷贝 [`resources/cc-design.css`](./resources/cc-design.css) 到目标项目的样式目录并在入口引入；如需参考完整交互结构，阅读 [`examples/index.html`](./examples/index.html)（**严禁直接照搬样板业务文案**）。

---

## 第二步：初始化目标项目

1. **选定子主题与明暗默认态**：
   - 在 `<html>` 声明 `data-theme="dark|light"` 与 `data-cc-theme="arclight|regulation|vector|dos"`（默认推荐 `arclight` 弧光演播青金）。
   - 在 `<head>` 引入 `Oswald`、`Chakra Petch`、`JetBrains Mono` 与 `Noto Sans SC`（离线或大陆环境参考 `components-and-motifs.md` 使用 `@fontsource`）。
2. **搭建正统骨架**：
   - 必须使用 `.cc-header`（含 `<1120px` 抽屉开关 `.cc-menu-btn` + `.cc-sidebar` + `.cc-scrim`）、`.cc-layout`、`.cc-main`、`.cc-footer`；
   - **禁止手写内联 `grid-template-columns`**，一律使用 `.cc-hero__grid` / `.cc-stat-row` / `.cc-split` / `.cc-grid-2` / `.cc-grid-3` / `.cc-wave-grid`；宽表格必须嵌套 `.cc-table-scroll`。
3. **组合高难契约核心模块**：
   - 顶区：`.cc-hero` + `.cc-hero__scorebox` 巨型动态风险评分；
   - 交互核心：`.cc-contract-tracks`（支持同组 `data-group` 互斥切换与实时计分）；
   - 辅助反馈：`.cc-tier-list` 压力阶梯 + `.cc-wave-grid` 步进波次卡 + `.cc-mission-item`（`COMPLETED` flex 避让水印结算行） + 完整 WAI-ARIA `.cc-tabs`。
4. **品牌配色覆写底线**：若需适配网站自有 VI，仅在 `:root` 覆写 `--cc-accent` / `--cc-accent-fg` / `--cc-accent-hover` / `--cc-accent-subtle` / `--cc-accent-2`，保留中性工业灰墨底盘与亮/暗双模式对比度。

---

## 第三步：交付前自检与渲染门禁

- [ ] 全页保持**纯直角 `border-radius: 0`**，无任何 45° 切角（`clip-path`）、整块菱形 `<polygon>`、投影发光与泛滥毛玻璃；
- [ ] **无内联 `grid-template-columns`**，且未残留样板专属测试词汇或伪十六进制乱码；
- [ ] `.cc-hero` 内文字、`.cc-contract-tag.is-selected` 与 `.cc-mission-item__wm` 在亮/暗双模式下均对比清晰且互不压字；
- [ ] 交付前使用无头 Chrome 实际验证 **`1440px` 桌面与 `390px`/`375px` 手机 × 亮/暗** 无横向溢出且无截断。
