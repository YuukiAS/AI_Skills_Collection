# Assurance 0.2 冻结审阅

相比 0.1，0.2 将 D1 澄清改为按决策树分轮、同轮问完互不依赖的用户问题，并把冻结审阅七部分直接放进 Blueprint，用户只批准内容快照，不再另批一份冻结说明（依据 [REVISION_0.2_PLAN](../../../REVISION_0.2_PLAN.md)）。

四道设计关卡已按本轮收敛规则通过，详见 [最终关卡汇总](../GATES_0.2_FINAL.md)。本轮只准备审阅材料，**尚未冻结**；插件实现与 9 个产品回归尚未运行。

## 请检查

1. 决定与默认做法是否符合您的取舍；仍需用户决定的问题，以及接受的假设是否完整、准确。
2. 哪些动作需要您转交、确认或授权，工作量、费用和权限边界是否可接受；未知下载大小是否明确标为“未记录”，单项超过 100 MB 是否仍先问您。
3. 角色启用时机、运行位置、派发者与责任是否清楚；**批准者是用户，D1 取得批准后执行冻结**。
4. 验收与回归的派生统计是否与设计一致：76 个验收器；R1–R8、S1 共 9 个用例、20 条检查（新能力 14、真实问题 3、受影响旧能力 1、冒烟 2）。D7 是冷读开工关卡，产品回归由原交付验收机制执行。
5. 不做及不保证的事项是否可接受；架构流程图中的阶段顺序、退回路线和职责是否符合预期。

## 截图与打开方式

使用 Asteria-Blueprint 的 freeze-review 视图，版本为 `229e1736f445bdecffd84773ad543e5f452d65df`。在本地预览中点击“冻结审阅”→“打开 Blueprint 文件”，选择仓库内 [当前 blueprint.json](../../../blueprint.json)；查看架构时点击“架构”→“流程图”。文件在浏览器本地读取，本轮未向外部服务上传。

以下 PNG 来自加载当前原始 Blueprint 后的真实页面：七部分各按完整内容导出整页截图，保留原页面样式、正文、派生表格和当前快照；只解除截图用的滚动高度限制，未改写 Blueprint 或应用源文件。验收分类保持可折叠摘要，9 个回归用例展开；架构图以原生尺寸完整截取。

| 部分 | 整页截图 |
|---|---|
| 决定与默认做法 | [decisions.png](decisions.png) |
| 需要用户决定或确认 | [asks.png](asks.png) |
| 工作量、费用与权限 | [costs.png](costs.png) |
| 角色分工及原档次表 | [roles.png](roles.png) |
| 验收与回归 | [validation.png](validation.png) |
| 下载与安装 | [downloads.png](downloads.png) |
| 不做及不保证的事 | [nongoals.png](nongoals.png) |
| 架构流程图 | [architecture-flowchart.png](architecture-flowchart.png) |

截图尺寸、PNG 文件哈希及渲染身份见 [capture-manifest.json](capture-manifest.json)。

截图中的 D5–D8 均显示“未记录”：该界面只读取 Blueprint 内已有的结构化关卡状态，当前关卡结果保存在外部证据文件中。本轮没有为改变显示而修改 Blueprint；真实最终状态请看 [GATES_0.2_FINAL.md](../GATES_0.2_FINAL.md)。验收器尚未运行与四道设计关卡完成是两种不同事实。

## 批准对象与方式

`snapshot_sha256`：

```text
dc6953587e95044854b914447effacaaa9edc9187b2a63fa4315dd999238a886
```

哈希由 `snapshotOf` + `canonicalize@2.1.0`（JCS）+ SHA-256 计算，与 0.1 冻结采用同一算法；Blueprint 原始字节哈希及核对边界见 [最终关卡汇总](../GATES_0.2_FINAL.md)。

审阅无误后，请回复：

> 批准 0.2，snapshot dc6953587e95044854b914447effacaaa9edc9187b2a63fa4315dd999238a886

批准仅针对上述快照。若需要修改，请指出对应部分；修改后应按既定修订规则核对受影响关卡并重新计算批准对象。本页不是批准记录，也不执行冻结。
