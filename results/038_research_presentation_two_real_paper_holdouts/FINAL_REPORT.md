# Final Report

## What this task solved

038 完成了 Stage 5 的第一次双真实论文 unseen holdout 验收，并把“工程闭环已经能运行”与“真实论文汇报已经达到成熟博士组会质量”明确区分开。两篇公开论文都完成了预生成 exclusion/license/source audit、完整 source staging、bundle freeze-before-render、正常 production entry 调用、exact-CUHK 编译、真实像素渲染与 task-local item-level Terra 审查。

最终结论不是质量 PASS。统计方法论文与医学影像论文都在真实像素上暴露了成熟度 blocker；随后唯一允许的 shipped bounded quality loop 也按设计 fail closed，没有越权手工修补或偷偷修改 frozen input。因此这次 unseen failure 被完整保留下来，成为后续通用恢复的真实依据。

## What changed

本 task 只增加评估输入、真实论文 source/asset、生成结果、render/quality-loop evidence 与 Reviewed Handoff artifacts，没有修改 `skills/`、`plugins/`、gold library、layout rules、selector、validator、tests 或 shared production behavior。

Statistics holdout 使用 Bürkner (2017) 的 brms 论文，生成了模型、kidney example、fitting workflow、package comparison 与 limitation/decision pages。Medical holdout 使用 Ma et al. (2024) 的 MedSAM 论文及许可覆盖的真实医学图像，生成了 DSC/model、内部验证、architecture、limitations 与 external CT same-case comparison pages。

Round-1 Terra 对两个 deck 给出七个 blocking findings。Round-1 review 只授权现有 bounded quality loop 消费这些 finding。Executor 第二次运行没有修改 source bundle 或 production code，而是把 Terra evidence 交给正常 quality-loop consumer；consumer 因 finding 缺少其要求的 `repair_intent` 而对两套 deck 都返回 `QUALITY_LOOP_FAIL_NO_WINNER`，repair count 保持 0。

## New capabilities / behavior

这轮新增的主要价值是可验证的真实泛化证据，而不是宣称新的 production 能力：

- 已经证明正常 entrypoint 可以从两篇真实公开论文的冻结输入生成独立 exact-CUHK deck、PDF、逐页 PNG、contact sheet、source-fidelity map 与 render identities；
- 已经证明医学路线能够直接携带文章许可覆盖的真实 MedSAM medical-image pixels，而不是 fabricated medical imagery；
- 已经证明 task-local Terra 可以对两套真实 paper deck 逐页及整套 contact sheet 给出成熟度判断；
- 已经证明当前 bounded quality loop 面对不带 `repair_intent` 的真实 Terra blocker 会 fail closed，而不会擅自应用不安全 repair 或伪造质量 PASS。

这些证据同时暴露了下一步唯一需要修的通用缺口：真实 item-level Terra finding 到有限 repair family 的 consumer adaptation，以及 repair directive 对实际 layout/render 的可执行闭环。

## Deliberately not adopted / unchanged

没有为了让 038 好看而进行任何以下操作：

- 没有在看到 slides/Terra 后改写 frozen source bundle；
- 没有手工 patch `.tex`、PNG、PDF 或医学图像；
- 没有为 brms、MedSAM、kidney example、CT case 或具体页号增加 production special case；
- 没有修改 shared/plugin production code、gold、layout、selector、validator、prompt 或 CI；
- 没有把 CI green、PDF compile 或 top-level workflow success 当成最终视觉质量 PASS；
- 没有执行第二次 repair，也没有制造第三轮 GPT review。

两篇论文已经作为真实 unseen holdout 被系统看过并暴露 blocker，从本 task 结束起不再具备后续 Stage-5 unseen 资格。

## Example usage

如果用户请求“把这篇统计方法论文做成 CUHK 组会汇报”，当前系统已经能够从真实论文对象生成一套 brms/Stan-specific deck，而不是回落到合成 calibration 内容；但本次真实结果仍有内部制作语言泄漏、图表缩放和布局碰撞，因此不能交付为最终成熟产品。

如果用户请求“把这篇医学影像论文做成 CUHK 组会汇报”，当前系统已经能够真实使用 MedSAM 文章中的医学图像和 segmentation evidence，并保持文章 attribution；但 architecture、limitations 与 same-case comparison 页面仍存在遮挡/碰撞，因此同样未达到最终可交付标准。

如果 page-level visual review 返回未知或当前 consumer 无法安全解释的 blocker，当前 quality loop 会选择 no-winner 并停止，而不是从不安全修复里强行挑一个。这一 fail-closed 行为在本 task 中被真实触发和验证。

## Regression and remaining limitations

真实 GitHub CI 已通过，且 `base_commit..implementation_commit` diff 没有发现 Executor 越权修改 Planner/Reviewer authority 或 production system。source bundles、render identities 与 Round-1 visual evidence 均被保留。

剩余 blocker 有两层。第一，两个当前 holdout 的最终像素仍保留 Round-1 七个 blocking findings：statistics deck 有内部 fixture 语言、workflow/footer overlap、不可读 table、closing diagram collision；medical deck 有 architecture footer overlap、limitations collision 和遮挡真实 CT crop 的 legend/connector。两个 contact sheet 都被 item-level Terra 判为未达到 mature doctoral group-meeting / strong paper-talk bar。

第二，shared `deck_quality_loop.py` 只接受 finding 自带的 `repair_intent` / `intent`，而真实 Terra blocker 没有该字段；同时当前用于 `RESCALE_PRIMARY_OBJECT` / `REPAIR_ANNOTATION_LEGEND` 的 spec hint 在仓库没有独立生产消费者证据。因此下一轮必须是新的非-holdout、bounded generic recovery：继续使用现有 Visual Review contract/state machine，把真实 requirement/finding 安全映射到有限 repair family，并证明 directives 真正改变 render，而不是只改变状态记录。未知/歧义 finding 必须继续 fail closed。

038 本身已经达到两轮 review 上限。其 terminal `REVIEW_LIMIT` 历史应保留，但这不是需要用户在产品语义上做选择的人工门；Program Goal 已授权在唯一、质量保持、范围明确的情况下自动进入新的 recovery task。

## Technical appendix

- Task key: `038_research_presentation_two_real_paper_holdouts`
- Base commit: `9a38a5f3cfbb499e88d0f68efe080a47f71c6e5b`
- Final Executor implementation commit: `be001f2d29a308a4cadeb9b841fcc9cfe239ea3b`
- Published control commit checked by CI: `ab9c12c74274ddb8f2e976937bdffd22179179e5`
- GitHub `Codex Marketplace` run: `33245235906`, conclusion `success`
- Round-1 Terra archive: `results/038_research_presentation_two_real_paper_holdouts/visual_review/VISUAL_REVIEW_1ce506ed08d5_REVIEW_1_USED.json`
- Statistics source-bundle SHA256: `32d1a9d1241ff8b4c77b6a98fe5b20b5b88ed04f3d60b0b10f9897304f15421b`
- Statistics rendered-pixel identity: `43b45471bbdf47f02232bab4be023356b7e325b33b3524c78318c63c302260c8`
- Medical source-bundle SHA256: `fef82966184d4db938d4bfdd12101d289ebdca80bf246a3ed7c9fb72f42fa33b`
- Medical rendered-pixel identity: `21e4c10f254650e5bbc83b79295d0d219da82a03b7bef6d31637c307dd2e72bf`
- Statistics quality-loop evidence: `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/quality_loop_state.json`
- Medical quality-loop evidence: `results/038_research_presentation_two_real_paper_holdouts/medical/generated/quality_loop_state.json`
- Round-1 review: `results/038_research_presentation_two_real_paper_holdouts/REVIEW_1.md`
- Round-2 review: `results/038_research_presentation_two_real_paper_holdouts/REVIEW_2.md`
- Final task decision: second-round `REVISE`; preserve review-limit history and route a separate generic recovery before any new Stage-5 unseen papers are consumed.
