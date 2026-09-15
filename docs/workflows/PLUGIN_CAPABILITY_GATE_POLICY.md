# Plugin Capability Gate Policy

版本：1.0  
日期：2026-09-15  
适用范围：AI_Skills_Collection 所有中央 plugin / skill / profile 的正式能力 refinement、release 与 maturity 判断。

## 1. 核心原则

正式插件不能因为“读了很多资料、接入很多资源、tests/CI 通过、生成了很多 evidence”就算完成。Planner 必须先把插件声称提供的用户能力拆成一组可观察、可失败、可独立验收的 capability gates；Critic 必须审查这些 gates 是否足够、是否重复、是否可以被 proxy PASS 钻空子。

Gate 不是固定模板，也不要求所有插件有相同数量。不同插件应按真实用户任务和最可能失败方式设计自己的 gate。Gate 数量以覆盖必要能力为准，不以“越多越稳”为目标。

## 2. Planner 必须给出 Capability Gate Matrix

任何会改变正式 plugin production behavior、准备 release、或准备把某 plugin 提升为更成熟状态的 Plan，都必须在执行前给出一个简洁的 Capability Gate Matrix。可以直接写在 Plan 中，不新增 schema/ledger。

每个 gate 至少说明：

- `Capability / claim`：它证明哪一个用户能力；
- `Why distinct`：与其他 gate 的区别，为什么不是重复检查；
- `Normal entry`：从普通用户真实入口怎样触发；
- `Evidence`：必须看到什么真实行为、artifact、render 或 runtime 证据；
- `Failure`：什么结果明确算失败；
- `Regression boundary`：本轮修复不能破坏哪些既有能力；
- `Final-candidate requirement`：该 gate 是否必须由最终待发布 candidate 直接通过。

两个 gate 如果主要验证同一件事，Planner 应合并；只有在它们证明不同风险（例如语义正确 vs 真实 render、一次成功 vs 预先要求的稳定性重复）时才保留，并说明区别。

## 3. 设计 gate 时必须考虑、但不机械套用的能力维度

Planner/Critic 至少逐项判断下列维度是否与目标 plugin 有关；不相关的明确跳过，相关的必须有 gate 或说明由哪个 gate 覆盖：

1. **Discovery / routing / install**：普通用户能否发现、安装并自然触发正确能力，真实 runtime identity 是否正确。
2. **Core domain behavior**：插件最核心的专业任务是否真正完成，不用 helper、fixture 或 prompt hardcode 冒充。
3. **Input diversity / task families**：目标能力是否只会一个窄例子，还是覆盖产品声明中重要的输入类型/任务族。
4. **Output / artifact quality**：最终用户实际消费的文本、图、PPT、UI、代码、报告或工作流是否达到对应领域标准。
5. **Fidelity / invariants / safety boundary**：哪些事实、数据语义、公式、引用、权限、状态、身份、可编辑性或用户材料不能被修坏。
6. **Should-not-change / compatibility**：简单任务、其他 route、已有插件能力和合法例外是否保持正常，防止修一处坏一片。
7. **Complex / long / scale case**：如果产品声称处理长文、大图、多阶段 workflow、大数据或复杂任务，必须直接验证代表性完整任务，不能只测片段。
8. **Generalization / fresh evidence**：在开发回归全部通过后，是否需要冻结新的真实/公开安全样本证明没有只针对已知失败调参；fresh 数量和任务族按风险决定，不机械固定。
9. **Production entry / integration**：最终能力是否从正式 plugin、真实安装、正常入口和正确资源绑定运行，而不是测试脚本单独可用。
10. **Human / independent qualitative judgment**：凡是自然语言、视觉、交互、科研解释等无法靠机械指标证明的质量，是否有能直接看到完整产物的独立审查。

这些是设计问题清单，不是强制十个 gate。一个设计良好的 gate 可以覆盖多个紧密相关维度，但 Planner 必须说明覆盖关系；Critic 要拒绝明显遗漏或用一个笼统“综合 PASS”掩盖多个未观察能力。

## 4. 资源与知识整合的验收

“下载、clone、读完、加入 reference、写进 registry、构建 corpus”都不是插件能力完成。

如果某轮目标包含外部资源、论文、repo、模板、案例库或知识库，至少要证明：

`INSPECTED -> RUNTIME_SELECTED -> ACTUALLY_CONSUMED -> OUTPUT_AFFECTED -> QUALITY_REVIEWED`

只有正常 production path 真正消费资源、资源改变了输出/决策，并且改变后的结果通过质量 gate，才能声称该资源已整合。否则只能说已发现、已检查或已准备，不能算能力 gate PASS。

## 5. Final candidate 与证据拼接限制

正式 release 所需 gates 必须绑定同一个最终候选版本和最终 production identity。旧候选通过的关键 gate 不能替代后来修改后的最终候选；不同版本各通过一半 gate 不能拼成 release PASS。

已知回归可以反复用于开发。fresh/holdout 只在候选和评审标准冻结后使用；看过并据此调过的样本失去 fresh 身份。真实基础设施错误、Reviewer 越权和产品失败必须分别归因，不能为了维持 fresh PASS 改写历史。

## 6. Critic 对 Gate Matrix 的审查职责

Critic 在执行前必须独立回答：

- 这些 gate 是否覆盖了插件真正声称的主要能力和高风险失败？
- 是否有两个或多个 gate 其实重复证明同一件事，徒增时间/费用？
- 是否漏掉了 normal entry、完整 artifact、should-not-change、复杂任务或真实 production behavior？
- 是否用 tests、schema、关键词、资源数量、receipt、synthetic fixture 或“吃进很多资料”冒充用户能力？
- gate 是否可被 test-specific hardcode、静默 fallback、换低质输出、只跑最好一次等方式钻空子？
- Reviewer/Terra 是否真的能访问 gate 所需 source/artifact/render，并且评分标准来自冻结合同？
- fresh/paid gate 是否放得太早，导致首次真正定性审查发生在不可恢复的最后一步？
- 所有必须发布的 gate 是否最终由同一个 final candidate 直接通过？

Gate Matrix 过重时，Critic 应要求合并/删除；过简时要求补上缺失能力。最终必须以真实能力覆盖率和证据质量为理由，而不是追求固定 gate 数。

## 7. 非绑定示例

这些例子只说明如何按插件能力设计，不是固定模板：

- **Clear Writing**：source fidelity；自然中文与结构；公式/表格/代码/引用；脏 source 清理与 reader relevance；长文完整任务；兼容 route；fresh generalization；正式安装/routing；完整成稿定性审查。
- **Verified Workflow / workflow-core**：handoff/state transition；授权语义与不重复索权；wait/resume/recovery；证据传递与角色边界；并行任务隔离；真实 production entry；失败时不靠 schema PASS 冒充实际流程成功。
- **Scientific Visualization**：数据/统计语义；视觉编码和图型选择；标签/图例/布局；多 panel/复杂数据；真实 render 可读性；可编辑/导出；source fidelity；正常调用与 fresh real-data cases。
- **Presentations**：内容/科学 fidelity；storyline；页面信息层级；真实视觉与布局；公式/图表；模板/资源真实消费；editable PPTX；逐页 render；完整 deck 节奏；正常入口。

Planner 应根据当前 plugin 的用户承诺重新设计 gates，而不是复制这些名称。

## 8. 与 maturity / release 的关系

本政策不创造新的 maturity taxonomy。`docs/PLUGIN_MATURITY.md` 仍以真实任务、真实 artifact/render 和用户验收为基础。

Capability Gate PASS 证明的是冻结范围内的 release readiness；长期 `alpha/stable` 还需要多个独立真实任务的持续使用。一次完整 gate matrix PASS 不等于 universally mature，但没有充分 capability gates 的 plugin 不应因 tests/CI 或资源摄入量而被称为正式可用。
