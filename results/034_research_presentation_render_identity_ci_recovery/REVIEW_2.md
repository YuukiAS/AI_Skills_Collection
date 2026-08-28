---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 034_research_presentation_render_identity_ci_recovery
review_round: 2
decision: REVISE
implementation_commit: fc0b8908b865de464c0d1ddf4475a9e57c11bbd5
---

# GPT Review

## Decision

REVISE。

第二轮 fresh evidence 已关闭第一轮两个可见 blocker：标题页不再泄露 `production regression` / `source bundle` 元语言；模型页现在有公式、模型角色和解释层，fresh Terra 对六个内容页与整套 contact sheet 均给出 item-level PASS，真实 GitHub `Codex Marketplace` CI 也完整通过。034 原本的 dual render-input / rendered-pixel identity recovery 同样保持闭合。

但独立检查共享 production code 后仍发现一个冻结范围内的 blocker：第一轮为修复模型页欠填充而新增的 equation-support 文案并没有完全由通用 source fields 驱动。`generate_cuhk_scientific_layout_stage3.py::emit_equation` 当前对所有 `STATISTICAL_MODEL` 页面无条件写入当前 clustered-calibration fixture 专用语义，包括 `Calibration link` 以及 `Center variation and individual variation define the ICC before the interval comparison.`；当 `scientific_objects` 缺失时还会显示 `Source-grounded terms remain attached to the equation.`。因此当前工程样例像素虽然成熟，但同一 normal production path 遇到 Cox model、Bayesian model 或其他非 clustered/ICC 模型时会把错误的 clustered-calibration 文案带到 audience-facing slide。这直接违反 Review 1 已冻结的“只消费现有 source-supported information、不得按当前 clustered fixture 的术语写死、不得出现制作/来源元语言”的修复边界。

本 task 已用满两轮 review，不能创建 `REVIEW_3`。按照 Program Goal 的 Quality-Preserving Continuation Policy，保留 034 的 review-limit 历史；这个 blocker 已被定位到唯一、范围清楚、质量保持的共享 equation-support generalization，因此后续应由新的 bounded recovery 处理，而不是降低 source-fidelity / mature-quality bar 或要求用户决定。

## Blocking findings

### 1. 模型页 supporting copy 仍含当前 fixture 专用科学语义与 audience-facing 元语言 fallback

**Plan / regression boundary**

Review 1 对模型页最小修复明确要求：新增 supporting content 只能消费已有 page-job/source evidence；实现必须由通用 `key_message` / `scientific_objects` / annotation 等字段驱动，不能按当前 clustered fixture 的标题、术语、页号或 gold ID 写死。Program Goal 同时禁止 audience-facing workflow / source-grounding 元语言和 holdout-specific hardcode。

**Observed evidence**

当前共享 `skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py` 的 `emit_equation` 中：

- supporting block 标题固定为 `Calibration link`；
- 页底 caption 固定为 `Center variation and individual variation define the ICC before the interval comparison.`；
- `scientific_objects` 为空时固定 fallback 为 `Source-grounded terms remain attached to the equation.`。

这些文本不是从当前 `spec` 的 source fields 读取。当前 Stage 4 engineering bundle 恰好就是 clustered interval calibration，所以 fresh Terra 看见的是语义正确的页面；但这只证明 fixture 命中硬编码，不能证明 normal production 对未见统计模型 source-faithful。尤其当前 bundle 的 model page 并没有提供 `caption` 字段，说明页底 ICC 文案是 renderer 自行补出的科学陈述。

**Minimal repair**

建立一个非常小的、通用的 model-support emission contract：

- 方程主对象不变；
- supporting body 只能来自 `scientific_objects`、`key_message`、`annotation`、显式 source-backed caption/label 等已有 source fields；
- generic furniture label 可以使用不携带当前领域科学语义的中性名称，例如 `Model components` / `Interpretation`，或消费显式 source-backed label；
- 没有 supporting source field 时宁可少一个 block / caption，也不能生成 `source-grounded` 元语言或虚构 clustered/ICC/interval-calibration 文案；
- shared/plugin mirror 保持 parity；不得改 Stage 2/3 gold bar、deck quality loop、storyline、medical semantics 或 repair budget。

**Required closure evidence**

- 新增至少一个与 clustered calibration 完全无关的 `STATISTICAL_MODEL` regression（例如 survival / Bayesian / causal / generic methodology model），通过 normal shared production/layout path 生成 TeX，并证明输出只包含该 fixture 提供的模型 supporting fields，不出现 `ICC`、`center variation`、`interval comparison`、`Calibration link` 或 `Source-grounded terms` 等当前硬编码；
- 当前 Stage 4 engineering bundle 仍保持 source-faithful、公式为主对象且模型页不重新退化为空页；
- shared/plugin parity、targeted/full tests、skills/marketplace validation 与真实 GitHub CI 通过；
- 如果当前 engineering pixels 因 generic labels/caption 变化，必须重新真实 render 并取得 fresh task-local item/contact-sheet evidence；如果像素严格未变，也必须用 identity/evidence 证明未变，不能复用不匹配的视觉证据。

## Non-blocking notes

- fresh Terra 与当前 manifest/implementation/pixel identity 一致，`slide_2_statistical_model`、slide 3–7 和 `deck_contact_sheet` 全部 PASS；contact sheet 明确认可标题→公式→结果图→实验设计→失败图→下一实验→医学影像的节奏，且无重复模板脸或明显过空/过密页面。
- 第一轮 title leakage blocker 已关闭：当前 `main.tex` subtitle 为研究描述，不再出现生产/来源包工程措辞；通用 metadata anti-leak gate 已接入 normal bundle loading。
- 034 核心 identity contract 没有新 blocker：render-input identity 绑定实际 `main.tex` / `scientific_layouts.tex` / assets；真实 render 时 pixel/contact-sheet identity 仍严格存在；no-render path 不要求伪造像素 SHA。
- 当前唯一 blocker 是 equation supporting copy 的通用 source-grounding；不要在 recovery 中重做已通过的整套 deck 视觉、identity、storyline 或 quality loop。
