---
name: arknights-<slug>
description: "TODO: 一句话写清适用场景、视觉气质、核心组件与触发关键词（用于替代或补充通用 PRTS 风格）。"
---

# Arknights Theme Skill · `<Theme Title>`（`.ak-<slug>-*`）

> 本 Skill 为独立自包含的《明日方舟》专题设计体系，与通用 `arknights-design`（PRTS 本家）**互相独立、严禁混用**。
> 若用户只需要通用的明日方舟官网/百科终端风，请改用主 Skill `arknights-design`。

## 第一步：确认适用边界与网站原型（先原型，再视觉）

- **适用场景**：TODO（写明该活动/玩法对应的真实业务场景与视觉调性）
- **与主 PRTS 的核心差异**：TODO（明确哪些主 PRTS 铁律在此专题中被刻意替代）
- **网站原型判别**：先识别用户的真实站点类型（① 官网落地页 / ② 长文博客与文档 / ③ 作品集与商品画廊 / ④ 登录表单与专题页 / ⑤ 控制台工作台），选择对应空间骨架；**非控制台场景严禁硬塞侧边监控轨、KPI 指标卡或遥测状态灯**。

## 第二步：必读规范（渐进式披露）

动手写代码前，先读取本目录两份规范：
1. [`references/foundations.md`](./references/foundations.md) — 色板对比度、字阶回退链、几何铁律与主题极性。
2. [`references/layout-and-components.md`](./references/layout-and-components.md) — 专属空间骨架、独有视觉母题与交互组件 ARIA 契约。

现成样式表与整页参考：
- 样式底座：[`resources/theme.css`](./resources/theme.css)
- 整页可交互样板：[`examples/index.html`](./examples/index.html)

## 第三步：实现与弹性适配边界

1. **复用底座与令牌**：直接引入 [`resources/theme.css`](./resources/theme.css) 并通过语义变量适配业务品牌，不绕开底座手写重复样式。
2. **禁止内联栅格**：全部多栏结构使用 CSS 响应式布局类，严禁在 HTML 中写死 `style="grid-template-columns: ..."`。
3. **业务脱敏与局部拓展**：领域图表与业务组件可基于本套语义变量自由拓展，但严禁把样板示例中的游戏专有代号或假十六进制写入真实业务页面。

## 第四步：交付前自检红线

- [ ] 未混入主 PRTS（`.ak-*`）或 Endfield（`.ef-*`）样式表与规则。
- [ ] 已按四层字体角色（Display / CJK / Mono / Accent）正确配置字体，渲染图未退化成单一默认黑体。
- [ ] 已按真实网站类型匹配布局原型，非控制台需求无多余侧边监控栏与 KPI 装饰。
- [ ] 所有自定义动效均有 `@media (prefers-reduced-motion: reduce)` 保护。
- [ ] 交互控件（Tab / 抽屉 / 筛选 / 菜单）具备完整键盘导航、焦点管理与真实隐藏态（`[hidden]`）。
- [ ] 正文与微文字均为真实可读业务内容，无假十六进制与样板专有词泄漏。

## 第五步：渲染验证

交付前必须在真实浏览器中核对 `1440px` 桌面端与 `390px` / `375px` 移动端（以及所支持的亮/暗极性）：
- 无文字叠压、裁切或极窄屏横向溢出；
- 所有状态色、反白按钮与微文字满足清晰可读对比度；
- 无无意义纯色占位块。
