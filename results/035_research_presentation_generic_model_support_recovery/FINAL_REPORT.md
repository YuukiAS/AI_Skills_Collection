# Final Report

## What this task solved

035 关闭了 034 留下的核心通用性问题：统计模型页不再把 clustered interval calibration 工程样例中的 ICC、center variation、interval comparison 或 `source-grounded` 制作话术当成所有未来模型页的默认内容。当前模型页的辅助解释现在由当前 source/page-job 自己提供的 scientific objects、key message、annotation 等字段驱动；完全无关的 Cox model regression 也经过同一共享路径，证明共享 renderer 不依赖当前 fixture 术语才能工作。

当前工程 deck 的模型页因此同时满足两点：公式仍然是主科学对象，页面没有退回公式+单句的欠填充状态；supporting copy 又不再依赖当前 clustered fixture hardcode。fresh Terra 对当前 `slide_2_statistical_model` 给出 item-level `PASS`。

035 不能被标成 PASS 的原因已经不是原始 source-grounding blocker，而是 fresh 完整 deck 审查暴露了两个此前像素未变化但投影尺度仍不够稳定的 process pages：实验设计页和下一实验页。它们使当前 `deck_contact_sheet` 仍为 `REVISE`。由于 035 第一轮已经冻结 slide 3–7，第二轮不能越界继续修改，因此任务合法停在 review limit；剩余问题适合由新的 bounded recovery 单独处理。

## What changed

共享 `STATISTICAL_MODEL` 页面生成路径被改为 source-driven supporting layer。模型组件和解释区只从当前 spec/source fields 读取科学信息；没有这些字段时不会再用内部制作话术或 clustered/ICC 文案填空。shared skill source 与 Codex marketplace mirror 保持一致。

测试层增加了与 clustered calibration 无关的 Cox model regression，真实穿过同一个共享 model layout/emission path，并检查 unrelated model 自己的术语能够进入 audience-facing TeX，同时当前 fixture 的 ICC、center variation、interval comparison、`Calibration link`、`Source-grounded terms` 不会泄露。

第一轮返修又只调整了模型页本身的几何与字号利用，让公式、source-backed annotation、`Model components` 与 `Interpretation` 更充分使用页面空间。与此同时，医学影像 overlay 的生成顺序被确定化，避免同一语义页面因非决定性资源顺序产生无关像素漂移。

## New capabilities / behavior

普通 research-presentation 生产路径现在可以面对不同统计模型时使用各自 source-backed 的模型组成与解释，而不是继承上一份 benchmark 的领域词汇。例如 clustered mixed model 可以展示其来源明确支持的 cluster/ICC 解释，而 Cox model 会展示 baseline hazard、covariate effects 等它自己的对象，不会自动出现 ICC 或 interval-calibration 文案。

当前模型页的 production render 也已通过 fresh item-level visual review：公式仍然是主对象，辅助解释可读，CUHK identity 正常，且没有 workflow/provenance/repository 等内部语言泄漏。

## Deliberately not adopted / unchanged

035 没有重写 Stage 2 gold composition library、Stage 3 scientific layout system、032 storyline/workstream grouping、deck-quality-loop 状态机、automatic repair budget 或 medical TP/FP/FN semantics。也没有运行 Stage 5 双-paper holdout。

第二轮没有为了让 035 通过而擅自修改实验设计页和下一实验页。Review 1 已明确把 slide 3–7 冻结为回归边界；fresh Terra 后续对 slides 4 / 6 提出的 projection-scale 问题属于新的、范围明确的 deck-quality blocker，应隔离到新的 recovery，而不是在 035 内制造第三轮或扩大原任务。

也没有用 034 对同一 slides 4 / 6 像素的旧 PASS 覆盖 035 的 fresh REVISE。两次审查差异被保留，因为 Program Goal 要求用当前 item/page-level evidence 判断成熟度，而不是挑选更宽松的历史结果。

## Example usage

用户提供一篇 clustered mixed-effects 方法论文时，系统可以使用论文自己的公式、cluster 结构、ICC 或其他来源明确支持的模型解释组织模型页；这些信息来自当前 source，而不是固定模板。

用户换成 Cox proportional hazards paper 时，同一生产路径会展示该模型的 hazard/baseline-risk/covariate 结构及 source-backed interpretation，不会残留 clustered calibration 的 ICC、center variation 或 interval comparison。

如果某篇 paper 只提供公式而没有足够 supporting model fields，系统允许模型页少一个辅助 block，而不是用 `source-grounded`、workflow 或无来源科学结论填充空白。

## Regression and remaining limitations

真实 GitHub CI 已通过，shared/plugin parity、完整 presentation regression、marketplace/skills/Reviewed Handoff validation 均由当前实现与 CI 证据支持。fresh visual evidence 与 implementation `d44adaef...`、当前 render-input identity、rendered-pixel identity 和 contact-sheet identity 一致。

模型页自身已通过 fresh Terra。当前剩余限制是实验设计页和下一实验页在最新 item-level Terra 中都被判 `REVISE`：中央流程/标签相对画布过小，存在明显未利用空间，部分 copy 与连接器在投影尺度下偏小；因此完整 `deck_contact_sheet` 也未达到稳定的 mature doctoral group-meeting / strong conference-talk bar。

这两个页面的 PNG SHA 与 034 evidence 完全相同，因此不是 035 新引入的 regression；但 Stage 4 仍不能据此忽略当前 blocker。后续需要一个只处理 `EXPERIMENT_DESIGN` / `NEXT_EXPERIMENT` projection scale 的 bounded recovery，并重新取得 fresh item-level PASS。

## Technical appendix

- task: `035_research_presentation_generic_model_support_recovery`
- implementation commit: `d44adaef2949d18843d5c8b22b78357345e3ab62`
- real CI locator before review transition: `dc638497a9e50a37219c1c02300a4453a20139d9`
- `Codex Marketplace` workflow run: `33211165241`, success
- fresh `AI Bridge Visual Review` run: `33213659687`, success with evidence committed
- visual evidence: `results/035_research_presentation_generic_model_support_recovery/visual_review/VISUAL_REVIEW.json`
- current model-page SHA: `18260a71aef6d59a0e02ffa87e5defb4bc03b44d0235984c2cc6eceebe7f9123`
- current experiment-design SHA: `e1775c71ddee184155cd69bc7c9858a5967be5c6a220cd0c6c25b33e372f69f1`
- current next-experiment SHA: `0fc4574ecbb5deb5ffac2cecbddcdd66967e2301c3199a931ffe06507f1e95aa`
- current contact-sheet SHA: `e47b99e2c698574f000ae668c41aea33ae7a974baf4761fc2f871be2d75577a8`
- render-input identity: `b6d7e55ec16a0a5d4140fcb322a2fb6b165fb4ad82420148f1edb6ccfa1bbed1`
- rendered-pixel identity: `1bab501f9986710211824c33702814608a32e89910fb65f6cae56e3ddca8ca9f`
- review history: `REVIEW_1.md = REVISE`, `REVIEW_2.md = REVISE`; no third review permitted
- remaining blocker: fresh Terra item-level `REVISE` for `slide_4_experiment_design`, `slide_6_next_experiment`, and `deck_contact_sheet`
