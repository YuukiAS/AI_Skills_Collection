# Final Report

## What this task solved

`render-chinese-math-pdf` 现在把“PDF 渲染成功”和“用户拿到最终文件”分开判断。
在已经验证的当前 Codex 客户端中，正常 PDF 请求完成后的第一次回复会直接给出
同一个通过质量检查的最终 PDF，用户无需再追问“PDF 呢”。

## What changed

- production `SKILL.md` 明确要求第一次完成回复以真实最终 PDF 文件入口开头，
  并在回复前确认文件可读、非空且与通过 QA 的候选一致。
- `references/checklists.md` 增加最终文件身份、真实入口和诚实失败检查。
- 目标回归保护首次交付合同及伪链接、路径、hash、receipt、preview、queued
  状态不能替代用户文件交付的边界。
- standalone skill 已准备为 `0.3`，对应 README、CHANGELOG、registry、catalog
  和 canonical TODO backlink 已在 task branch 收口；中央 plugin 版本未改变。
- D1 首次回复事件、D2 受控失败、D3 兼容回归和仓库基线差分均留下可复核证据。

## New capabilities / behavior

当用户自然地要求生成中文、中英混排或数学 PDF 时，skill 会继续使用原有
Pandoc/XeLaTeX 路线完成渲染和 QA，然后在第一次完成回复中直接提供最终 PDF
文件入口。若最终文件缺失、不可读或当前宿主不能合法提供入口，回复会明确说明
“文件交付尚未完成”，而不会把服务器路径、receipt、hash、preview 或伪造 URL
包装成已经交付。

## Deliberately not adopted / unchanged

- 没有重写 renderer，也没有改变 Pandoc AST、XeLaTeX、字体、公式、模板、
  project profile authority 或现有 PDF QA。
- 没有新增公共下载服务、第三方网盘、外部 API、凭据路径或未经授权的文件外传。
- 没有修 Presentations、Research Authoring、generated publication baseline、
  Bridge Kit、Slurm 或其他 plugin 的既有问题。
- 没有重新渲染或替换已经验收的最终 PDF 来刷新结果。

## Example usage

用户可以直接说：

> 把这份中英文数学 Markdown 渲染成正式 PDF。

成功时，第一次完成回复会先显示可打开、可另存为的最终 PDF 文件入口，再简要
说明渲染与 QA 结果。若回复前发现文件不可读，则会说明 PDF renderer 已完成但
用户文件交付未完成，并由执行端重新渲染、核验后再交付。

## Regression and remaining limitations

独立 Reviewer 重跑 32 项 PDF/standalone 目标测试并全部通过，也直接检查了最终
PDF、receipt、字体、提取文本和整页 preview。修订后的仓库基线差分门使用真实
workflow 命令比较 then-current main 和 exact final candidate：候选没有新增测试
失败、没有恶化共有 assertion diagnostics，也没有新增或扩大 generated/publication
差异。

GitHub Actions run `38706208966` 仍真实为 `FAIL`，其中四个 current-main 既有
跨插件/generated baseline failures 没有被本任务修复。三个 platform smoke jobs
仍为 PASS，候选及其相关 surface 在其后没有变化。本报告的 PASS 只覆盖 bounded
PDF product/reviewer acceptance；merge、正式 release、Issue #101/Project closure
和 task branch 清理仍属于后续 integration/release closure。

当前实测结论只适用于已确认能够打开、另存 host-local PDF 入口的这个 Codex
客户端，不能外推到所有客户端、远程宿主或第三方文件传输。

## Technical appendix

- Task branch：`reviewed/documents-media--pdf-save-as-delivery`
- Implementation commit：
  `5c92bf4f599d378ff68444b0fa85f5d56bbbd628`
- Then-current main differential baseline：
  `362a8cab6991120a79600352d070926e2602dcbd`
- Final PDF：
  `private/exports/documents-media--pdf-save-as-delivery/d1-final-candidate/project/final-bilingual-math-delivery.pdf`
- Final PDF SHA-256：
  `5e51c6873d8ff64ee68fd49b45dd881a043b48073496ca7987fbc06696f35d50`
- Final PDF identity：43853 bytes，1 页 A4
- D1 event：
  `results/documents-media--pdf-save-as-delivery/D1_DELIVERY_EVENT.md`
- Differential evidence：
  `results/documents-media--pdf-save-as-delivery/CI_BASELINE_DIFFERENTIAL.md`
- Historical CI：run `38706208966`，结论保持 `failure`
- REVIEW_2：bounded PDF product/reviewer acceptance `PASS`
