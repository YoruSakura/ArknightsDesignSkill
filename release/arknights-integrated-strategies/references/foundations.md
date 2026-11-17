# Arknights Integrated Strategies · 五代主题规范与素材溯源

> 本 Skill 提炼自《明日方舟》集成战略（Integrated Strategies）五大视觉代际。下表如实记录原站（`ignoredone.space/index.php/arknights_design`）各期素材的真实加载与推导粒度。

---

## 一、五代主题溯源与真实覆盖说明

| 时代标识 (`data-is-theme`) | 对应集成战略 | 原站取材状态 | 提炼出的视觉语法与排版基因 |
| :--- | :--- | :--- | :--- |
| **`sarkaz`（默认）** | IS#5 · 萨卡兹的无终奇语（2024/0714） | **33/33 张完整实机 UI & KV 加载** | **炭墨暗底 + 腐蚀金垂直光柱 + 深红异变**：`.is-hero__pillars` 垂直光柱、双线裱框、三列垂直吊挂的 `本月委托栏`（`甲`/`乙`/`丙`）与探索节点图 |
| **`sui-garden`** | IS#6 · 岁的界园志异（2025/0715） | **146 张主体完整实机 UI 加载** | **双极画卷美学**：Light 模式呈莲粉与石青水墨书卷（`--is-accent: #187A6E`, `--is-accent-2: #C2315C`），Dark 模式呈墨夜薄荷青与朱砂系统盘（`#2DD4A8` + `#E04A3F`），搭配古典 `Noto Serif SC` 与括注拼音 `.is-ruby-title` |
| **`caerula`** | IS#3 · 水月与深蓝之树（2022/0923） | 仅封面可用（内页遭遇 CDN 重定向异常） | **深渊靛蓝 + 生物荧光青紫**：深海冷蓝 `#08111E` 与亮青 `#38BDF8` / 紫水母微光 `#A78BFA`，细衬线标题栈 `Cormorant Garamond` |
| **`joklumarkar`** | IS#4 · 探索者的银凇止境（2023/0711） | 仅封面可用（内页遭遇 CDN 重定向异常） | **冰川灰银 + 冻晶青蓝**：寒雾中性灰阶搭配冷冽青蓝 `#7DD3FC` / `#2C5E8A`，窄幅大写副标叠压厚重宋体主标题 |
| **`blackflow`** | IS#7 · 沉沦者的黑流拟海（2026/0712） | 仅封面可用（内页遭遇 CDN 重定向异常） | **浸水暗青灰 + 低饱和单色磷光**：拟态 CRT 监视器与沉海密室幽闭灰调（`#0B1113` + `#54B5AD`） |
| *IS#1 灰蕈迷境 & IS#2 傀影* | — | 原站 2019–2026 网格未收录 | 若项目需 IS#2 红黑剧场感，可参考主 Skill `theater` 丝绒深红与鎏金配色做局部令牌覆盖 |

---

## 二、排版、装帧与形状规则

1. **双衬线典籍层次**：
   - 中文主标题、章节头、节点名、委托牌、藏品名一律使用 `--is-font-serif`（`Noto Serif SC`）；
   - 外文副题与 Hero 主英文采用 `--is-font-drama`（`Cormorant Garamond` 回退 `Noto Serif SC`）；
   - 状态代码、希望/源石锭读数、时间节点采用 `--is-font-label` + `tabular-nums`，严格表格数字栏走正文字体 + `tabular-nums`。
2. **双线框骨与形状收敛**：
   - 主图台 `.is-hero`、典籍框 `.is-folio-box`、月度委托卡 `.is-commission-card` 采用**外框 + `inset` 4px–5px 细线框**的屏风/画卷装帧，**严格保持 `border-radius: 0`**；
   - 节点探索路径 `.is-route-map` 一律使用直角矩形节点与清晰分栏，严禁 `rotate(45deg)` 大菱形或 `<polygon>` 等距斜块。
3. **品牌配色覆写方法**：若业务网站仅借鉴集成战略的探险路径与图鉴结构、需要自有 VI 配色，仅在 `:root` 覆盖 `--is-accent` / `--is-accent-fg` / `--is-accent-2` / `--is-bg-canvas` / `--is-bg-surface`，同时确保 `.is-hero` 恒深色底面内保持高对比亮字。
