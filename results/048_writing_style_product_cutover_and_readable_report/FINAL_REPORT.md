# Final Report

## What this task solved

048 把此前停留在实验阶段的中文科研长文重写能力推进到了真实产品候选：用户仍然只需要从 `writing-style` 入口提出“把这份科研长文说人话但不能改科学内容”的自然请求，系统会在正常安装的插件中进入内部 `scientific-rewrite` 路径，而不是要求用户知道隐藏 skill 名称。

同时，用户指定的 22 页 Deep Research 报告已经通过安全的私有文本转换链生成完整重写稿，并经过独立全文 Text Review。当前自动化、CI、production entrypoint 和独立 artifact review 均已通过；最后尚未完成的是用户本人实际阅读完整私有稿并明确 ACCEPT。按冻结产品合同，在这个人工门槛通过前，任务不做版本升级、不合并 main，也不宣称最终 Product PASS。

## What changed

AI_Skills 新增 `skills/writing/core/scientific-rewrite/`，并最小调整 `writing-fidelity`、`chinese-prose` 与 Marketplace routing。核心变化不是增加一组禁词，而是把长篇科研重写改成“先理解论证，再重写表达”：建立文档地图和完整论证单元，用 Meaning Card 与 Fidelity Ledger 区分需要逐字保护的对象和允许彻底换中文句法但不能改变含义的科学关系，随后做精确检查、语义审计、局部修复和全文一致性检查。

Bridge Kit 同期补齐了可复用的私有文本转换能力：本地私有源先 age 加密，GitHub 只保存密文和 manifest；GitHub Actions 在临时 runner 解密并通过 OpenAI Responses API、`store=false` 完成转换；模型输出在 runner 内再次加密给本地 receiver，公开 Git 不保存原文或重写正文。AI_Skills 的 transform workflow 固定到明确的 Bridge Kit commit，并继续用现有 Text Review 做独立全文复核。

Review 1 暴露的两个工程问题也已收口：当前 048 tree 中涉及 presentations 的路径与 latest main 内容身份一致，不再由 048 拥有越界 presentation 改动；此外，`ai-skills-core` maintenance preflight 和正常安装后的 `writing-style` fresh-session routing 都已留下真实 production evidence。

## New capabilities / behavior

`writing-style` 现在具备内部 `scientific-rewrite` 路径，可处理已有中文或中文为主的科研/技术长文高保真重表达。长篇请求会进入 meaning-first 流程；轻度中文润色仍停留在 `chinese-prose`；仅检查数字、公式、引用、版本或保护内容时仍由 `writing-fidelity` 负责。

新的私有文本转换链让“完整私有长文经过 OpenAI 处理但 plaintext 不进入 GitHub”成为可复用能力。输入和输出都使用 age 密文；OpenAI 调用明确使用 `store=false`；本地可以安全解密最终结果，再将完整候选送入独立 Text Review。

对本轮真实 Deep Research 报告，完整候选已经生成。独立 Text Review 对完整 source + candidate 的科学/来源保真、中文可读性、完整性与全文一致性均给出 PASS，且 `blocking_findings=[]`。公开固定回归中，两组需要重写的材料没有出现 critical fidelity drift，两组 should-not-fix 保持低编辑/不深改。

## Deliberately not adopted / unchanged

048 没有新建顶级 humanizer/scientific-rewrite plugin；用户入口仍是 `writing-style`。没有加入 Gemini、Claude routing、fine-tuning、embedding/vector DB、FAISS/Chroma/BGE，也没有重新 Source Scout。

没有把 `provenance`、`estimand`、`scientific gap` 等历史失败词汇做成项目专用黑名单，也没有使用英文比例、禁词计数或 AI-detector 分数作为产品门槛。`academic-humanizer` 仍只是以后英文 academic-writing 审计的参考来源。

044 和 047 均保持历史只读；048 不重开旧 control plane。私有报告也不再依赖 raw `codex exec`、复制 `auth.json` 或 plaintext Git。`presentations` 不属于 048 产品范围；当前 presentation baseline repair 已独立进入 main，048 只与最新 main 对齐其内容。

## Example usage

普通用户可以继续直接说：

```text
把这份中文科研报告说人话一些，但不要改变事实、数字、公式、引用、专业术语和结论强度。
```

这类长篇、已有原文、高保真请求会进入 `scientific-rewrite`。

较轻的请求：

```text
帮我把这两段中文稍微润色顺一点，不要大改。
```

应保持在 `chinese-prose`。

只做保真审计时：

```text
只检查数字、公式、引用和版本有没有被改坏，不要重写正文。
```

应进入 `writing-fidelity`。

## Regression and remaining limitations

当前 048 branch 的 `Codex Marketplace` CI 已通过，latest main baseline CI 也已独立通过。source/generated `scientific-rewrite/SKILL.md` 内容身份一致；normal Marketplace shadow install、fresh session 与 production maintenance replay 均已落地。

私有报告的机械 helper 仍留下 29 个 citation/path extractor fragment miss，但这些记录不包含 missing span plaintext。Review 1 已核对这些属于 helper/ledger fragment 问题而非已确认的科学漂移；随后完整私有 Text Review 明确审查引用、路径、科学关系、限定条件、比较、归因和结论强度，并给出 PASS。因此当前没有证据要求重新生成全文，但这仍是最终人工阅读时值得留意的剩余风险。

最重要的剩余门槛是用户本人阅读。自动 Text Review 不能替代“这份报告是否真的适合用户接下来几天连续阅读并据此跑实验”的实际体验。若用户 REJECT，应只根据真实阅读反馈做 bounded generic repair；不得重新开启 044/047，也不得把单个报告措辞硬编码成 production phrase rules。

在用户 ACCEPT 之前：`writing-style` 保持现有版本，repository 不 release，048 不 merge main。

## Technical appendix

- 048 implementation identity: `928de2325d781ca630883d03e0f381092675b269`
- Review 1 repair branch CI tip: `e0f6900b420654a8d8cbaea92c8b3b1935296c9a`
- 048 CI: `Codex Marketplace` run `33622264270`, success
- latest main snapshot: `0bae10b5ab5df914d77ca29212845f9e39146452`
- main baseline CI: run `33621860808`, success
- Bridge Kit companion used by the task: `65ea9c59afbe2db88bb5d60bf8752f82719f0087`
- writing-style generated plugin id: `writing-style@yuukias-ai-skills`
- ai-skills-core generated plugin id: `ai-skills-core@yuukias-ai-skills`
- production entrypoint evidence: `results/048_writing_style_product_cutover_and_readable_report/production_entrypoint/PRODUCTION_ENTRYPOINT_EVIDENCE.md`
- public regression evidence: `results/048_writing_style_product_cutover_and_readable_report/public_regression/PUBLIC_REGRESSION_REPORT.md`
- private transform evidence: `results/048_writing_style_product_cutover_and_readable_report/text_transform/TEXT_TRANSFORM.json`
- private fidelity evidence: `results/048_writing_style_product_cutover_and_readable_report/private_fidelity/PRIVATE_FIDELITY_EXACT_REPORT.json`
- private Text Review evidence: `results/048_writing_style_product_cutover_and_readable_report/text_review/TEXT_REVIEW.json`
- Review 1: `results/048_writing_style_product_cutover_and_readable_report/REVIEW_1.md`
- Review 2: `results/048_writing_style_product_cutover_and_readable_report/REVIEW_2.md`
- current tracked candidate SHA-256 in private-fidelity evidence: `f5d64e5a94f244e8201d9fbe3c2b735bcf7558a20e92c2ef13b219c1fa546025`
- Text Review: `overall_decision=PASS`, `blocking_findings=[]`
- Repository bump decision: `NONE` until user ACCEPT
- `writing-style`: `NO_BUMP` until user ACCEPT
- merge main: `NO` until user ACCEPT
- next required action: user reads the complete locally decrypted Deep Research rewrite and records `ACCEPT` or `REJECT`
