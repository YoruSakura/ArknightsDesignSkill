# Foundations — `<Theme Title>` 视觉铁律与令牌基座

> 新建专题时，先基于真实游戏实机或官方专题页采风记录填入以下四节，删除所有 `TODO`。

## 一、视觉哲学与采风来源

- **真实视觉来源**：TODO（记录对应的游戏内界面/官方专题站实机观察要点）
- **核心气质关键词**：TODO（3~5 个精确形容词，避免泛泛而谈）

## 二、与通用 PRTS Design 的刻意边界

| 维度 | 通用 PRTS (`arknights-design`) | 本专题 (`arknights-<slug>`) |
| :--- | :--- | :--- |
| 色彩极性 | 黑白灰炭 + 冰青 `#18D1FF` / `#0098DC` | TODO |
| 几何形状 | 纯直角 `0px`，严禁 45° 切角 | TODO |
| 字体气质 | 工业无衬线 + 等宽标号 | TODO |
| 空间骨架 | 官网漂浮顶栏/右轨 或 Wiki 终端 | TODO |

## 三、色彩令牌与对比度约束

- 列出背景层、表面层、主/次/弱文字层、强调色层与语义告警色层。
- 所有正文文字对比度 ≥ 4.5:1，大号展示标题与交互边框 ≥ 3:1。
- 给出品牌换色覆盖清单（仅覆写语义强调令牌，不破坏中性基底层级）。

## 四、四层字体角色与动效节律（一等视觉维度）

- 按四层角色定义开源字体（含字重、字宽、衬线/无衬线选型、Google Fonts 链接、`@fontsource` 离线方案与系统回退链）：
  1. **Display 展示巨字**：`--ak-<slug>-font-display`（TODO）
  2. **CJK 中文标题与正文**：`--ak-<slug>-font-body`（TODO）
  3. **Mono / Tabular 编号与数据**：`--ak-<slug>-font-mono`（TODO，配 `tabular-nums`）
  4. **Accent 装饰副标 / 引言**：`--ak-<slug>-font-accent`（TODO）
- **动效语言**：定义本专题的过渡时长、缓动曲线与专属 `@keyframes`，并声明 `prefers-reduced-motion: reduce` 行为。
