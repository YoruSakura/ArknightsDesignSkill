# Arknights Contingency Contract · 设计规范与色彩矩阵

> 本 Skill 提炼自《明日方舟》高难危机合约 / 行动协议及同系战术端局界面。为保证技术诚实与可追溯性，先声明原站（`ignoredone.space/index.php/arknights_design` 与 `coverdesign`）各素材的真实取材来源与边界。

---

## 一、素材溯源与诚实边界声明

| 取材主题 | 原站真实归属与状态 | 凝练到本系统的视觉语法 |
| :--- | :--- | :--- |
| **`arclight`（弧光行动）** | `coverdesign` 栏目实有（`弧光作战 880 / 645 / 675` 全量加载） | **演播室巨型评分体 + 青金星盘基调**：超粗等宽分数主字（`880`）、`3×3` 点阵微记号、微距星标徽章 |
| **`regulation`（卫戍协议「规程」）** | `arknights_design` 2026/1108（34/34 张完整 UI，含 `契约调整` 面板） | **构成主义绯红/深炭灰/薄荷青双极**：顶部 `契约调整` 多行词条互斥点选网格、橙金 `规程等级 1/2/3` 阶梯选择 |
| **`vector`（矢量突破）** | `arknights_design` 2024/0926（18/18 张完整 UI） | **冷银灰建筑线框 + 电紫 + 酸橙黄**：`LV.15–19` 步进竖卡片列阵、`COMPLETED` 大字结算横条 |
| **`dos`（DOS 纷争演绎）** | `arknights_design` 2023/1002（封面加载，内页 CDN 重定向未展开） | **高冷单色黑灰 + 电钴蓝基准线**：极简直线边框与纯数据表格节奏 |
| *早年危机合约（#0–#12）* | 原站主网格未收录 | 本体系已补齐标准的「词条互斥分组 + 风险总分即时叠加」交互逻辑；若需特定旧赛季（如黄铁黄/铅封灰红）可按本手册第五节令牌微调 |

---

## 二、四角语义调色盘与版式差异化（`[data-cc-theme]`）

全部 4 套预设共用同一套直角框架与交互契约，并原生兼容 `:root[data-theme="light"]` 与 `:root[data-theme="dark"]`，同时在纹理、线型与字族上做结构区分：

1. **`arclight`（默认 · 演播室青金）**
   - Dark：`#0A1015` 深海炭底 + `#121A22` 面板面 + 官网青 `--cc-accent: #18D1FF` + 香槟金 `--cc-accent-2: #F0C65A`。
   - Light：`#EEF3F7` 冷灰雾底 + `#FFFFFF` 白卡面 + 对比青 `--cc-accent: #0076A8` + 暗金 `--cc-accent-2: #9A6D00`。
   - 版式特征：左 5px 青金竖柱 Hero + 演播室大号 `Oswald` 评分体与 `3×3` 点阵。
2. **`regulation`（卫戍规程 · 构成主义红×薄荷青）**
   - Dark：`#0F1315` 深枪灰 + 战术薄荷 `--cc-accent: #00D8A0` + 琥珀 `--cc-accent-2: #F59E0B` + Hero 构成主义左绯红柱 `#D93843`。
   - Light：`#EDF1F0` 雾灰 + `--cc-accent: #007A5A`。
   - 版式特征：Hero 顶部叠加 6px 构成主义 45° 红斜纹警戒带（`.cc-hero::after`），`.cc-panel__head` 左侧配 4px 绯红强调竖线。
3. **`vector`（矢量突破 · 电紫×酸橙）**
   - Dark：`#111218` + 电紫 `--cc-accent: #A78BFA` + 酸橙 `--cc-accent-2: #E5F500`。
   - Light：`#EBEDF2` 建筑纸灰 + 深紫 `--cc-accent: #5B32E6`。
   - 版式特征：Hero 叠 28px 工程制图方格底纹与 4px 酸橙顶边；`.cc-heading` 由左竖线转为 3px 顶划线；已通过波次卡（`.cc-wave-card.is-cleared`）配顶/底双边高亮。
4. **`dos`（DOS 演练 · 单色×钴蓝）**
   - Dark：`#0C0D10` + 电钴 `--cc-accent: #3B82F6`。
   - Light：`#F2F4F7` + 深钴 `--cc-accent: #1D4ED8`。
   - 版式特征：Hero 转用底部 4px 电钴基准线；`.cc-heading` 转作底部水平下划线；`.cc-stat` 顶置 2px 刻度线且数值与评分主字切换为 `JetBrains Mono` 等宽字体。

---

## 三、字体与版式铁律

1. **巨型评分与表格数字分离**：`.cc-hero__score`、`.cc-stat__val`、`.cc-wave-card__lv` 使用强压迫感的 `--cc-font-display`（`Oswald` + `Archivo`）配合 `tabular-nums`；而 `.cc-table` 数据列和词条加分权重严格使用 `--cc-font-body` / `--cc-font-mono` + `tabular-nums`，确保多行数字对齐不发虚。
2. **直角刚性骨骼**：卡片、契约词条按钮、阶梯选择器、分段开关一律 `border-radius: 0`，严禁 `clip-path` 45° 切角、菱形 `<polygon>` 或大圆角阴影卡片。
3. **恒深色 Hero 安全规则**：`.cc-hero` 在 Light 模式下依然维持高对比深底（线性渐变，无光晕模糊），因此内部必须锁定亮色文字 `#F4F7FA` 与高明度高亮色，严禁继承浅色背景的深暗主色。
4. **状态语义色（亮色模式必配）**：`--cc-success` / `--cc-warning` / `--cc-danger`（及 `-bg`）在每个亮色子主题下都必须取暗态值（如 `#0d825d` / `#a15c00` / `#c4232d`）；严禁继承暗色基线的薄荷绿与琥珀，否则浅底对比度仅约 2:1。
5. **品牌配色自定义边界**：业务网站如需接入自有品牌强调色，只覆写 `:root` 或 `[data-cc-theme]` 上的 `--cc-accent` / `--cc-accent-fg` / `--cc-accent-hover` / `--cc-accent-subtle` / `--cc-accent-2`，务必同时核对亮/暗双模式下文本对比度 $\ge 4.5:1$。
