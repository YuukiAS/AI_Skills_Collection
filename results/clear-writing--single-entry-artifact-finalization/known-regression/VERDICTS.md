# 已知回归：本地完整产物审查

证据类型：`LOCAL_WRAPPER_SOURCE_REPLAY_NOT_WEB_GATE`。
执行者逐项读取原始 TASK / INPUT 与完整实际产物，不用聊天完成回执代替产物。
独立实现审查另见 `../review/IMPLEMENTATION_REVIEW.md`。

13 个任务均只有一次有效模型回答，未因质量、格式或语言重跑。
原始运行提交为 `f86c4d0d3374a57cd27da1cee74f210c50e18150`；后续
`8a1b0a77d6e182423ac24779f8748fc3e5362d9b` 与
`079bd7987bb33d624d244feb415327d5cf2343d8` 只修正构建器的引用校验和回放记录/采集机制。
两者的 wrapper source、六项 route source 和实际回放 ZIP 完全相同，ZIP SHA-256 为
`e4c451841583cb6e1ae4212f8d8559b93ef4272f66d687d3f6762f6114a73dc6`。
没有把旧运行的 source_commit 改成新提交；完整输入、实际输出与回执 hash 见 `INPUT_MANIFEST.json` / `RUNS.json`。

| 样本 | 结论 | 完整产物中的依据 |
| --- | --- | --- |
| KR-WEB-01 | PASS | 先解释尚不能判定可上线，保留恢复验证边界、精确命令和无需用户行动的事实，不扩写流程。 |
| KR-WEB-02 | PASS | 指出 A/B 的实际冲突和 B 缺乏支持，不为结果补造因果解释。 |
| KR-WEB-03 | PASS | 保留功能开关与版本回退的真实区别、适用场景和例子，说明不能假定兼容性；正向深度未丢失。 |
| KR-WEB-04 | PASS | 直接解释 CSV 导入和全部记录校验后才 READY，不把内部阶段名堆给读者。 |
| KR-WEB-05 | PASS | 保留 4 周、18%、6 周、3 团队及混杂限制；明确区分来源共识和助手的有限建议。 |
| KR-WEB-06 | PASS | 以连续推理解释校准、背景漂移和残差，先定义对象再给公式；例子明确是示意，没有杜撰阈值。 |
| KR-WEB-07 | PASS | 普通概念自然中文化，保留 Temporal Fusion Transformer (TFT)、时间窗口、分组留出、命令和路径；未声称跨季节验证成立。 |
| KR-WEB-08 | PASS | 完整比较完全、不、部分合并，保留 5 与 500 的样本量对照、收缩权重直觉和假设边界；额外正态教学模型明确标作示意而非实测模型。 |
| KR-WEB-09 | PASS | 先解释组/时间/通道与各层对象，再给残差及权重公式；不把未知估计量猜成均值，明确 u_a_b_c 缺定义。 |
| CW-CONTROL-01 | PASS | 完整合同原样保留，没有以摘要代替用户要求的完整产物。 |
| CW-CONTROL-02 | PASS | 真正有分支和逐步执行价值的结构保留，条件未因去模板化丢失。 |
| CW-CONTROL-03 | PASS | JSON 的实际产物与原始精确输入逐字节一致，包括末尾 LF；没有加说明或代码围栏。 |
| CW-CONTROL-04 | PASS | 正式产品名、插件名、命令、提交、状态值与路径保持，普通解释使用自然中文。 |

上述结论基于语义、保真与任务要求，不用固定字数、段落数、标题数、关键词或英文比例判定。
正向深度样本 03/08/09 不是越短越好。

回放通过 canonical `ai-bridge plugin-replay` 运行，显式提供相同 wrapper ZIP 与原始 fixtures，
使用当前 Codex 身份和继承的运行模型 `gpt-6.1-sol`，没有切换 formal Web 模型。
已安装的六项专业能力仍为 0.5；新 wrapper 由本地包显式消费，不冒充账户上的 0.6 已安装。
这些只支持开发阶段已知回归，不证明 ChatGPT 真实 Skill inventory、GitHub 写入最终化或 G1-G6。
G3 Reader Guide 未用于开发调参，G6 fresh 样本未选择或消费。

机器本地完整回放保留在长期 checkout 的
`private/exports/clear-writing--single-entry-artifact-finalization/known-regression/<case>/replay/`。
公开目录只含 public-safe fixtures、任务、实际输出及无秘密的运行身份/hash。
