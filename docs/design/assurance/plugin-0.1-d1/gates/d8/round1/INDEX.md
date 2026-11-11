# D8 读者复述：第 1 轮

受审 Blueprint：`docs/design/assurance/plugin-0.1-d1/blueprint.json`，提交 `bfb49470fc349c1cd6ef3154ab0566ca93167fdd`。共 51 个复述单位，每个单位开一个全新的 GPT 对话（Thinking，推理强度调到最高），把对应提示词整段贴进去。不要在同一个对话里跑两个单位。

读者结果写回 `results/`。D1 会逐条对照原意判断是否复述正确，再整理成检查器要求的 `readability-review.json`。复述有误的步骤由 D1 改写文字，下一轮换新读者重读。

| # | 单位 | 类别 | 标题 | 提示词 |
|---|---|---|---|---|
| 01 | `ws-state` | 正常走查（walk-source） | 定位当前任务 | `prompts/01-ws-state.md` |
| 02 | `ws-writer` | 正常走查（walk-source） | 确认写入基线 | `prompts/02-ws-writer.md` |
| 03 | `ws-dispatch` | 正常走查（walk-source） | 决定下一角色 | `prompts/03-ws-dispatch.md` |
| 04 | `ws-prompts` | 正常走查（walk-source） | 交出完整消息 | `prompts/04-ws-prompts.md` |
| 05 | `ws-designer` | 正常走查（walk-source） | 独立完成候选 | `prompts/05-ws-designer.md` |
| 06 | `ws-owner` | 正常走查（walk-source） | 收敛两份原稿 | `prompts/06-ws-owner.md` |
| 07 | `wb-source` | 正常走查（walk-built） | 核对源文件 | `prompts/07-wb-source.md` |
| 08 | `wb-planning` | 正常走查（walk-built） | 确定读取来源 | `prompts/08-wb-planning.md` |
| 09 | `wb-execution` | 正常走查（walk-built） | 生成执行包 | `prompts/09-wb-execution.md` |
| 10 | `wb-capability` | 正常走查（walk-built） | 转入真实验证 | `prompts/10-wb-capability.md` |
| 11 | `wi-entry` | 正常走查（walk-installed） | 调用已派发技能 | `prompts/11-wi-entry.md` |
| 12 | `wi-check` | 正常走查（walk-installed） | 观察真实使用 | `prompts/12-wi-check.md` |
| 13 | `wr-contract` | 正常走查（walk-real） | 核对九项语义 | `prompts/13-wr-contract.md` |
| 14 | `wr-gates` | 正常走查（walk-real） | 完成四项关卡 | `prompts/14-wr-gates.md` |
| 15 | `wr-freeze` | 正常走查（walk-real） | 批准具体设计 | `prompts/15-wr-freeze.md` |
| 16 | `wr-owner` | 正常走查（walk-real） | 接收交付责任 | `prompts/16-wr-owner.md` |
| 17 | `wr-build` | 正常走查（walk-real） | 实现并申报 | `prompts/17-wr-build.md` |
| 18 | `wr-calibration` | 正常走查（walk-real） | 校准验收实现 | `prompts/18-wr-calibration.md` |
| 19 | `wr-asset` | 正常走查（walk-real） | 审查验收变化 | `prompts/19-wr-asset.md` |
| 20 | `wr-candidate` | 正常走查（walk-real） | 固定最终对象 | `prompts/20-wr-candidate.md` |
| 21 | `wr-evidence` | 正常走查（walk-real） | 读取直接证据 | `prompts/21-wr-evidence.md` |
| 22 | `wr-sign` | 正常走查（walk-real） | 亲读后签发 | `prompts/22-wr-sign.md` |
| 23 | `fail-write-step-1` | 失败处理（fail-write） | 发现与传递异常 | `prompts/23-fail-write-step-1.md` |
| 24 | `fail-write-step-2` | 失败处理（fail-write） | 识别问题并交回 | `prompts/24-fail-write-step-2.md` |
| 25 | `fail-write-whole` | 失败情形整体收场（fail-write） | 整体收场说明 | `prompts/25-fail-write-whole.md` |
| 26 | `fail-role-step-1` | 失败处理（fail-role） | 发现与传递异常 | `prompts/26-fail-role-step-1.md` |
| 27 | `fail-role-step-2` | 失败处理（fail-role） | 识别问题并交回 | `prompts/27-fail-role-step-2.md` |
| 28 | `fail-role-whole` | 失败情形整体收场（fail-role） | 整体收场说明 | `prompts/28-fail-role-whole.md` |
| 29 | `fail-checker-step-1` | 失败处理（fail-checker） | 发现与传递异常 | `prompts/29-fail-checker-step-1.md` |
| 30 | `fail-checker-step-2` | 失败处理（fail-checker） | 识别问题并交回 | `prompts/30-fail-checker-step-2.md` |
| 31 | `fail-checker-whole` | 失败情形整体收场（fail-checker） | 整体收场说明 | `prompts/31-fail-checker-whole.md` |
| 32 | `fail-premise-step-1` | 失败处理（fail-premise） | 发现与传递异常 | `prompts/32-fail-premise-step-1.md` |
| 33 | `fail-premise-step-2` | 失败处理（fail-premise） | 识别问题并交回 | `prompts/33-fail-premise-step-2.md` |
| 34 | `fail-premise-whole` | 失败情形整体收场（fail-premise） | 整体收场说明 | `prompts/34-fail-premise-whole.md` |
| 35 | `fail-semantic-step-1` | 失败处理（fail-semantic） | 发现与传递异常 | `prompts/35-fail-semantic-step-1.md` |
| 36 | `fail-semantic-step-2` | 失败处理（fail-semantic） | 识别问题并交回 | `prompts/36-fail-semantic-step-2.md` |
| 37 | `fail-semantic-whole` | 失败情形整体收场（fail-semantic） | 整体收场说明 | `prompts/37-fail-semantic-whole.md` |
| 38 | `fail-calibration-step-1` | 失败处理（fail-calibration） | 发现与传递异常 | `prompts/38-fail-calibration-step-1.md` |
| 39 | `fail-calibration-step-2` | 失败处理（fail-calibration） | 识别问题并交回 | `prompts/39-fail-calibration-step-2.md` |
| 40 | `fail-calibration-whole` | 失败情形整体收场（fail-calibration） | 整体收场说明 | `prompts/40-fail-calibration-whole.md` |
| 41 | `fail-candidate-step-1` | 失败处理（fail-candidate） | 发现与传递异常 | `prompts/41-fail-candidate-step-1.md` |
| 42 | `fail-candidate-step-2` | 失败处理（fail-candidate） | 发现与传递异常 | `prompts/42-fail-candidate-step-2.md` |
| 43 | `fail-candidate-step-3` | 失败处理（fail-candidate） | 识别问题并交回 | `prompts/43-fail-candidate-step-3.md` |
| 44 | `fail-candidate-whole` | 失败情形整体收场（fail-candidate） | 整体收场说明 | `prompts/44-fail-candidate-whole.md` |
| 45 | `fail-missing-step-1` | 失败处理（fail-missing） | 发现与传递异常 | `prompts/45-fail-missing-step-1.md` |
| 46 | `fail-missing-step-2` | 失败处理（fail-missing） | 识别问题并交回 | `prompts/46-fail-missing-step-2.md` |
| 47 | `fail-missing-whole` | 失败情形整体收场（fail-missing） | 整体收场说明 | `prompts/47-fail-missing-whole.md` |
| 48 | `fail-package-step-1` | 失败处理（fail-package） | 发现与传递异常 | `prompts/48-fail-package-step-1.md` |
| 49 | `fail-package-step-2` | 失败处理（fail-package） | 发现与传递异常 | `prompts/49-fail-package-step-2.md` |
| 50 | `fail-package-step-3` | 失败处理（fail-package） | 识别问题并交回 | `prompts/50-fail-package-step-3.md` |
| 51 | `fail-package-whole` | 失败情形整体收场（fail-package） | 整体收场说明 | `prompts/51-fail-package-whole.md` |
