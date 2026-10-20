# Clear Writing 0.6 Phase C 对 Planner–Critic 1.8 的真实事故证据

日期：2026-10-21  
治理任务：`chatgpt-web--pass-integrity`  
来源任务：`clear-writing--single-entry-artifact-finalization`  
批准包：`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`  
Phase C evidence：`38a81dc1df9a362ecee4be597cb3db5bd6fcac41`

本文件只记录已发生事实与其对治理验收的直接含义，不修改 Clear Writing 0.6 产品语义。

## 已发生事实

1. Phase C 在正式 Personal Plugin mutation 前安全停止；当前 `writing-style` 仍为 `0.5.0`，`PERSONAL_PLUGIN_MUTATED=NO`，G1–G5 未运行。
2. Plugin Creator 的真实旧版本归档返回 `current.tar.gz` / `application/gzip`，而冻结 `prepare-restore` 实现只用 `zipfile.ZipFile` 消费 baseline/candidate archive；该执行面还没有证明短期下载 URL 能被可靠物化为 builder/update 所需本地文件。
3. G1-B/G2/G3 要求 fresh ChatGPT Web conversation + `GPT-5.6 Sol` + explicit Clear Writing selection；批准包把 Phase C 交给长期 Planner，但没有证明该 Planner surface 具有“创建新 Web conversation 并显式选择插件”的动作。
4. 安全停止后的用户回复说明了两个 blocker 和大量机器状态，但没有把“归档兼容由谁修、执行职责缺口由谁修、用户现在需不需要动作、唯一下一入口是什么”完整交付给用户，而是以“需要一个同时具备若干能力的执行面”结束。
5. 当前正式 Planner/Critic 1.7 已经存在以下原则：
   - 未知能力需要在设计阶段用受控小探针核实，不能把假设当已验证能力；
   - Critic 必须查清谁执行、失败后是否有合法恢复路径，不能到最后一步首次发现；
   - 批准范围内普通 bug/runtime/loader/Gate failure 默认留在同一 Codex task；
   - Planner 对执行中断/恢复结果必须给唯一下一用户入口；
   - Planner/Critic 用户摘要必须先用自然中文说明结论、影响、剩余问题、用户动作和下一接收方。
6. 因此本事故不能简单归因为“缺少这些原则”。1.8 需要补的是：让这些原则变成可观察的 evidence obligation 与真实回复验收对象，避免再次被纸面文字满足。

## 对 1.8 的直接要求

- execution-ready 审查必须对真正决定“能不能实施/能不能安全恢复”的关键接口索取现实证据，而不是只看 Plan 中是否写了工具名、执行者或恢复步骤；
- 尚未验证的接口只能作为条件性假设，并必须冻结谁、何时、在什么副作用边界前验证，失败时怎样停；
- 非终态交接必须以实际用户回复为验收对象；抽象的“需要某种环境”不是唯一下一入口；
- 用户可读层必须独立成立，不能靠后面的机器状态块补全含义；
- Clear Writing 可辅助表达，但“加载/调用过写作 skill”本身不证明最终完整回复合格。

## 本治理任务不据此授权

- 不修改 Clear Writing 0.6 产品；
- 不修改 Plugin Creator；
- 不修改 Bridge Kit；
- 不修改 Capability Gate Policy；
- 不修改 AI Research Stack Project setting；
- 不启动任何 live plugin mutation 或付费验证。
