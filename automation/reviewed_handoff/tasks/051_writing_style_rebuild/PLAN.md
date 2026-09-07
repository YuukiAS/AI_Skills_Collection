---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: 051_writing_style_rebuild
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan — 051 writing-style rebuild

## Objective and value

Rebuild the existing `writing-style` plugin's **heavy Chinese rewrite path** so a normal user can ask the installed plugin to reorganize a long scientific/technical document into natural, reader-facing Chinese without losing facts, numbers, formulas, citations, comparison conditions, uncertainty, attribution, caveats, or conclusion strength.

The accepted architecture baseline is `results/050_writing_style_host_codex_runtime/CLEAR_LANGUAGE_PRODUCTION_REDESIGN_PLAN_V0_3_2026-09-07.md` at design commit `7c105b5c6b15e30441292fba57ba5e672a652f17` on `reviewed/050_writing_style_host_codex_runtime`. Task 050 remains historical evidence only; its Round-5 implementation `590502f5a78b2032f2238380aa68ea8287d50b9c` may be selectively ported only where it still satisfies this Plan.

Planner Five-Pass preflight decision:

- **Product:** the target is ordinary installed-plugin heavy rewrite, not a helper, benchmark, forced subskill invocation, or sentence-level polish.
- **Reality:** current `main` still packages `writing-fidelity`, `scientific-prose`, and `chinese-prose`; `scientific-rewrite` is absent. Current `writing-fidelity` protects source headings/order too broadly for authorized structural rewrite. Current `main` is `887b071999eaa5ba2af992857b63bb54f30fc61f`; the 051 branch base is `6fa8f5c54351ee8c7097745ed5baa3d502313af0`, and the intervening main change is repository guidance/context-budget policy, which Executor must obey without treating it as a reason to redesign the task.
- **Alternatives:** reject continued Round-5 source-conditioned local rewriting, reject paid per-stage generation, reject fake hard isolation through nested Codex, and reject regex/English-density/readability proxies. Use the Critic-approved v0.3 semantic realization architecture.
- **Red team:** the Plan explicitly closes source-copy fallback, fixed-size chunk fallback, Latin-span exact-item inflation, source leakage through repair/assembly, forced-route-only success, process-PASS-as-quality, and adaptive holdout chasing.
- **Execution:** implement one bounded successor release under the existing `writing-style` slug, prove real routing/artifact quality, then close source/generated/version/release integration. Do not start another redesign chain inside Executor work.

Feedback promotion decision: **PROMOTE_NOW** for the next-generation heavy Chinese structural rewrite capability under the existing `writing-style` plugin. The later `writing-style -> clear-language` slug migration and cross-plugin consumer wiring remain separate work and are not promoted by 051.

Maintenance companion: `ai-skills-core`

Domain owner: `writing-style`

## Frozen decisions

### Runtime ownership

The four logical owners below are the owners of the **heavy Chinese rewrite path**, not the complete `writing-style` plugin:

1. `scientific-rewrite`: raw-source understanding, source anchors, Meaning Map, Reader Plan, semantic bundle sizing, heavy-route orchestration, assembly, source-aware semantic audit orchestration, repair routing, re-verification, and architecture receipt.
2. `chinese-prose`: reusable Chinese realization core. Preserve its existing `POLISH_EXISTING` behavior and add `REALIZE_MEANING` for generation from already-fixed meaning.
3. `writing-fidelity`: literal/semantic preservation contract, including an explicit `STRUCTURAL_REWRITE` mode.
4. `rewrite_support.py`: deterministic/mechanical support only; it cannot generate reader prose or certify semantic/readability quality.

Existing `scientific-prose` remains the English scientific-prose route and must not be removed, absorbed, or routed through the Chinese heavy path.

### Heavy path

The production heavy path is:

```text
raw source
-> source anchors
-> Meaning Map
-> Reader Plan
-> REALIZE_MEANING
-> assembly
-> exact + semantic fidelity audit
-> structured targeted repair when needed
-> re-assembly when needed
-> re-verification
-> final candidate
```

`REALIZE_MEANING` uses **soft isolation**. The host Codex may have seen the source earlier in the same task/session, but the formal realization instruction/input surface must not re-present raw source paragraphs, source quotations, source tails/previews, source excerpts, source-shaped rewrite templates, prior rejected candidates, manual GPT reference text, Latin-span inventories, QA ledgers, or old `exact_identity/useful_recognition/ordinary_reasoning` classifications as drafting inputs.

Do not create ad-hoc nested `codex exec`, a second model runtime, or another isolation subsystem merely to claim the writer has forgotten the source. If soft isolation is materially insufficient in real artifacts, return to Planner rather than silently recreating the old writer.

### Meaning Map and Reader Plan

Meaning Map is meaning-centric and source-auditable. It must preserve, where relevant, claim/evidence identity, polarity, comparator, condition/scope, caveat/limitation, uncertainty/modality, negative findings, attribution, conclusion strength, future/candidate status, exact required identities, and bidirectional source-anchor authority.

A deterministic/helper path must have **no** fallback equivalent to `source excerpt -> normalized_meaning`. Missing/malformed semantic extraction is a semantic failure/repair condition. An exact source-copy regression fixture may be rejected mechanically, but no similarity/readability score may substitute for semantic extraction.

Reader Plan owns reader-question order, meaning ownership, semantic dependencies, and information shape. Mechanical size limits may only signal `NEEDS_SEMANTIC_SPLIT`; they must not choose the final heavy bundle boundary. The old `4 paragraphs / ~2800 chars` behavior cannot be the production heavy splitter.

`seed-transformations.json` may remain historical/provenance material but must not condition production realization with literal rewrite templates.

### Exact-item boundary

An ordinary Latin technical word is **not** a required exact item merely because it is a Latin span. Exact preservation is reserved for identities whose literal identity matters, such as formal algorithm/model/dataset/metric/package/API/code/path/config/citation identities, exact formulas/notation, machine-facing tokens, or user-explicit protected spans. Ordinary reasoning, organization, comparison, qualification, and transition language remains eligible for natural Chinese realization.

### Structural fidelity override

`writing-fidelity` must encode task-mode-specific behavior.

For `STRUCTURAL_REWRITE`, protect by default:

- facts/claims/evidence and polarity;
- attribution;
- comparator and comparison direction;
- conditions, scope, exceptions;
- caveats/limitations;
- uncertainty/modality;
- negative findings;
- conclusion strength;
- numbers/dates/units;
- formulas/notation;
- citations;
- exact formal identities;
- explicit user no-touch constraints.

Do **not** automatically protect source headings, paragraph boundaries/order, section order, or internal workflow labels when structural rewriting is authorized. User-explicit structure constraints override this default freedom.

### Audit, repair, and assembly

The semantic auditor may read the raw source. Findings must bind to meaning IDs/source anchors. A repair packet sent back to `REALIZE_MEANING` may contain only structured items such as bundle id, affected meaning IDs, finding type, required semantic correction, required exact-item IDs, and allowed semantic operations. It must not contain source quotations/prose or a target rewrite sentence.

If Meaning Map itself is wrong, repair the Meaning Map first and update dependent Reader Plan bindings before re-realization.

Assembly may consume Reader Plan, realized bundles, meaning ownership, bundle dependencies/purpose, required exact objects, and already-established terminology. It must not receive the raw source as drafting material or become a second whole-document source-conditioned writer.

Default maximum: two targeted repair passes for the same unresolved bundle in one production attempt. Persistent substantive failure returns `qa_failed / NEEDS_GPT_PLANNER` as appropriate; do not lower fidelity or restore forbidden fallback behavior.

### Generation and paid-review boundary

Normal generation, semantic extraction, planning, realization, ordinary semantic audit, repair, and assembly are host-Codex owned. **No paid OpenAI/Terra call is allowed in those stages.** Ordinary push/CI must not trigger paid review.

For independent artifact-aware final text evidence, 051 uses Bridge Kit Text Review only at the final-candidate/review boundary, never as generation. One final candidate-only Text Review call is allowed because the same host model cannot independently certify the reader-facing quality of its own private artifact and the GitHub Scheduled Reviewer otherwise cannot legally inspect host-local private text.

Paid review contract:

```text
model: gpt-5.6-terra
max paid calls for 051: 1
per-call worst-case ceiling: USD 0.25
campaign reserved-cost hard ceiling: USD 0.25
automatic paid retries: 0
trigger: explicit/manual only
paid tools: none
input boundary: final combined candidate text + audience + frozen review questions only; no raw source, Meaning Map, Reader Plan, intermediate drafts, internal self-audit, repo workflow logs, or secrets
```

Every call must use the repository persistent pre-request reservation/accounting policy. If the real combined request cannot fit the frozen per-call ceiling or the review infrastructure/billing accounting is not verified, do not send it; return to Planner/human review strategy instead of expanding budget. External review evidence cannot override explicit user rejection.

### Version/release decision

Current sources show repository `5.0.3` and `writing-style 0.1`.

```text
Repository bump decision: PATCH
Reason: 051 changes an existing plugin's compatible production behavior/quality without adding a new repository-level capability or breaking the plugin slug/install contract.

Affected plugins:
- writing-style: 0.1 -> 0.2
  Reason: successful 051 delivery adds a real heavy Chinese source-faithful structural rewrite production path and ordinary-user routing that version 0.1 does not provide.
```

The version bump occurs **exactly once and only at final accepted release closure**, after real replay, unrelated regression, required human/artifact gates, final CI, and Reviewer acceptance. If another branch advances repository version or `writing-style` version before integration, do not overwrite concurrent history or double-bump; treat it as an integration/Planner decision. Do not change `writing-style` maturity status from `unclassified` solely because 051 passes.

## Positive completion

051 is complete only when a normal user, through the real installed `writing-style` plugin, can make a natural request to structurally rewrite a long Chinese scientific/technical document and the released plugin automatically uses the new heavy path, preserves the source's substantive scientific meaning and exact required identities, materially lowers reader burden, and closes release/integration without relying on task-specific wording hacks.

Positive completion requires all of the following real outcomes:

1. Ordinary installed-plugin black-box routing selects the heavy route for a realistic long Chinese source-faithful rewrite without the prompt naming `scientific-rewrite`, Meaning Map, Reader Plan, `REALIZE_MEANING`, stage packets, or validators.
2. Short/local Chinese polish remains light; fidelity-only work remains fidelity-only; English scientific prose remains on `scientific-prose`.
3. Known 050 A/B/C regression inputs are replayed only as `KNOWN_REGRESSION`, through the same production route, with no old candidate/reference/diagnosis leakage. The user accepts the resulting real artifact quality.
4. The complete private report is produced through the same production architecture and accepted by the user; no alternate full-report writer is allowed.
5. A small, different, real scientific/technical holdout from another document family is frozen before evaluation, run only after the implementation is frozen, and passes without holdout-specific tuning or adaptive replacement. The user remains the final qualitative authority.
6. Final private text is available to the independent Scheduled Reviewer through a hash-bound Bridge Kit Text Review evidence path; process summaries alone cannot stand in for the artifact.
7. Final source/generated parity, relevant local regressions, explicit final GitHub integration/release CI, install/upgrade smoke, version/changelog closure, and integration back to the then-current `main` succeed.

Maximum claim scope: a successful 051 proves that the accepted heavy Chinese rewrite path works on the frozen known regression family, the complete real report, and one frozen fresh real holdout through the ordinary installed route. It does **not** prove universal writing quality, every language, every document domain, future cross-plugin consumer integration, or the proposed `clear-language` rename.

## Non-substitutable semantics

The following substitutions are forbidden even if tests or CI pass:

- source-conditioned paragraph/unit paraphrase in place of semantic realization;
- raw source prose as a co-primary `REALIZE_MEANING` input;
- fixed-size character/paragraph chunking as the heavy semantic planner;
- helper-generated source-copy Meaning Map content;
- literal seed rewrite templates or Latin/English QA classes as writer conditioning;
- treating arbitrary Latin spans as exact identities;
- source prose/quotations hidden inside repair findings;
- assembly that rereads the source and globally rewrites the document;
- preserving source headings/order at the expense of an explicitly authorized structural rewrite;
- phrase blacklists, English-density scores, regex readability proxies, self-filled PASS fields, or receipts as proof of reader quality;
- forced subskill invocation as proof of ordinary-user routing;
- synthetic/toy text as replacement for required real known-regression/full-report/fresh-holdout evidence;
- adapting production behavior to a failed holdout, replacing the holdout, or repeatedly drawing new holdouts until one passes;
- paid per-stage generation/reasoning/rewrite;
- dropping the existing English `scientific-prose` route;
- renaming the `writing-style` slug during 051;
- allowing the language layer to invent domain scientific semantics or decide research-document/deck structure owned by other plugins;
- treating schema/tests/CI/render success as a substitute for user artifact acceptance.

No equivalent fallback is pre-authorized for these semantics. If one becomes necessary, return to Planner/human decision with evidence.

## Implementation scope

Executor starts from `reviewed/051_writing_style_rebuild` and must obey the latest `origin/main/AGENTS.md` governance/context-budget rules. Do not merge the entire 050 branch. Selective historical porting may read commit `590502f5a78b2032f2238380aa68ea8287d50b9c` only for implementation fragments that still match this Plan.

Expected production surfaces:

- add `skills/writing/core/scientific-rewrite/` as the heavy orchestrator, rewritten to this Plan rather than copied unchanged from Round 5;
- add/replace a mechanical-only `skills/writing/core/scientific-rewrite/scripts/rewrite_support.py` and only the references/contracts genuinely needed by the new runtime;
- update `skills/writing/core/chinese-prose/SKILL.md` to preserve existing local polish and add `REALIZE_MEANING`;
- update `skills/writing/core/writing-fidelity/SKILL.md` with the explicit `STRUCTURAL_REWRITE` preservation override and semantic-audit/repair boundary;
- preserve `skills/writing/core/scientific-prose/**` unless a minimal routing compatibility edit is demonstrably required; do not redesign its English behavior;
- update `scripts/codex_marketplace_config.json` so released `writing-style` packages/routes the heavy skill while retaining current light/English skills;
- update the existing profile/routing source only if required for the real installed plugin path; do not create a new profile/dependency schema merely for 051;
- regenerate `plugins/codex/plugins/writing-style/**` and other generated marketplace outputs through the canonical generator; never hand-edit generated payloads;
- add/update focused tests for routing, semantic/mechanical boundaries, structural fidelity, source/generated parity, privacy, and unrelated light/English regressions;
- create a 051-local production replay/evidence contract; do not reuse or rewrite 050's historical replay contract;
- use installed production `workflow-core`, `ai-skills-core`, and `writing-style` for the required maintenance/domain preflight and final replay, not source-file reading as a substitute for production invocation;
- update `docs/plugin-todos/writing-style.md` only to record the bounded 051 closure without marking the separate slug rename/broad consumer-integration proposal complete;
- at final accepted release only, update `scripts/codex_marketplace_config.json`, `docs/plugin-changelogs/writing-style.md`, root `CHANGELOG.md`, `VERSION`, README release dashboard and generated release surfaces required by the canonical version policy;
- keep task-local private plaintext, user review Markdown/PDF, holdout source, and intermediate semantic artifacts out of public Git; commit only permitted encrypted/repo-safe evidence, hashes, manifests, receipts, and public-safe regressions.

Human-review rendering is a task acceptance companion, not a new `writing-style` runtime dependency. Whenever 051 produces Markdown/scientific-report text for human acceptance, invoke the installed `render-chinese-math-pdf` skill and its environment probe/production renderer. For multi-candidate review, build a task-local combined Markdown and render a single combined PDF. Do not invent a parallel PDF renderer or hard-code machine paths into reusable source.

## Acceptance and regression gates

### Gate 1 — implementation/mechanism PROCESS PASS

Focused local tests must prove observable contracts, including:

- absent semantic extraction fails rather than being helper-filled from source;
- known direct source-copy fallback is rejected without inventing semantic similarity scoring;
- every substantive source anchor has meaning ownership and every meaning has source authority;
- realization/repair schemas have no raw-source/source-quotation drafting fields;
- assembly drafting input excludes raw source;
- Reader Plan owns valid meaning IDs and fixed-size splitters cannot select final heavy bundles;
- ordinary Latin technical words do not become exact items merely because they are Latin spans;
- exact literals/formulas/citations remain protected;
- structural rewrite can improve headings/order without fidelity failure while comparator/caveat/uncertainty drift fails;
- production routing keeps heavy Chinese, short Chinese polish, fidelity-only, and English scientific prose distinct;
- production heavy generation makes no paid external model call;
- private replay commits no private plaintext and ordinary push triggers no paid review;
- source/generated Marketplace parity is exact.

This gate is PROCESS PASS only and cannot establish reader-facing quality.

### Gate 2 — ordinary installed-plugin routing

Use the real installed `writing-style@yuukias-ai-skills` production route / Bridge-owned `ai-bridge plugin-replay` equivalent. The user prompt must be natural and must not contain internal heavy-subskill/stage names. A heavy-route receipt must show that the plugin itself selected the new path.

A forced `writing-style:scientific-rewrite` replay is diagnostic only and cannot satisfy this gate.

### Gate 3 — known A/B/C regression PRODUCT / ARTIFACT gate

A/B/C may be read/replayed only because this Plan freezes them as `KNOWN_REGRESSION` from 050. They cannot consume 050 state/review budget and cannot be called unseen/generalization evidence.

Generate through the real ordinary installed route. Do not expose v0.3, failure diagnosis, old candidates, manual reference output, expected bad vocabulary, or task-specific phrase rules to the writer.

After mechanical/fidelity checks, produce a task-local `combined_known_regression_review.md` (or equivalently clear combined Markdown) and render `combined_known_regression_review.pdf` through the installed `render-chinese-math-pdf` skill. Render QA must check CJK glyphs, formulas, tables/page overflow and basic PDF text-layer readability. User `ACCEPT` is required before full-report evaluation. User rejection overrides all process/reviewer PASS and routes to bounded repair or Planner according to the failure class.

### Gate 4 — complete real private report PRODUCT / ARTIFACT gate

Only after Gate 3 user acceptance, produce the complete private report through the identical installed heavy architecture. No alternate writer/helper architecture is allowed.

Preserve a task-local final Markdown and render a review PDF with `render-chinese-math-pdf`; if comparison is useful, use one combined Markdown/PDF rather than scattered outputs. User `ACCEPT` is required. Keep plaintext host-local; record artifact hashes and the human decision without committing private text.

### Gate 5 — frozen fresh real holdout generalization gate

Before the first holdout evaluation, freeze one complete holdout batch containing one small but non-trivial real scientific/technical source from a different document family, with source identity/hash/range, acceptance questions and the exact frozen implementation commit. If no legitimate fresh source is already authorized, request the user's artifact/authorization; this is a human-input gate, not `BLOCKED`.

The holdout must use a normal black-box `writing-style` prompt. During the batch, production code/rules/prompts/validators are frozen. A failed holdout is a failed batch: no holdout-specific repair, no replacement/chasing, no turning the failed text into a tuning fixture and re-claiming unseen PASS. Generic recovery may occur only on non-holdout/public-safe/known-regression material; consuming a later fresh batch requires a new explicit decision.

Render the holdout review Markdown/PDF through `render-chinese-math-pdf` and require user qualitative acceptance. The claim remains limited to this frozen batch.

### Gate 6 — final independent text evidence

After Gates 3–5 are user-accepted and the implementation candidate is frozen, create one final combined candidate-only UTF-8 Markdown packet containing the final reader-facing candidate texts needed to assess reader burden across the accepted known-regression/full-report/holdout outputs, without raw source/intermediate data. Hash-bind it to the accepted artifacts.

Because these texts may be private, set/use Bridge Kit Text Review evidence under:

```text
results/051_writing_style_rebuild/text_review/payload.age
results/051_writing_style_rebuild/text_review/text_inputs.json
results/051_writing_style_rebuild/text_review/TEXT_REVIEW.json
```

Use the single frozen paid call budget above. The independent review evaluates reader-facing clarity/naturalness and obvious candidate-quality regressions only; source fidelity remains owned by the source-aware host audit/mechanical checks. Missing/stale/malformed Text Review evidence means `WAITING_FOR_EVIDENCE / NEEDS_REVIEW`, not PASS. Terra PASS cannot override user rejection.

### Gate 7 — release candidate / final CI PROCESS PASS

Only after implementation candidate freeze and required artifact gates:

- run focused local tests and unrelated light/English regressions;
- verify source/generated parity and private-data boundaries;
- perform version/changelog/release preflight;
- explicitly dispatch the repository's required heavyweight integration/release CI on the task branch; do not require full CI after every development push;
- perform real install/upgrade smoke for released `writing-style` and ordinary black-box heavy routing.

CI failure caused by 051 is `REVISE`; transient/infrastructure issues use bounded recovery/waiting semantics, not a fake product failure.

### Gate 8 — GPT Reviewer and integration

Reviewer must distinguish PROCESS PASS from PRODUCT / ARTIFACT PASS. It must read the actual implementation diff, CI, source/generated/version closure, human-acceptance hashes/receipts, and current Bridge Kit `TEXT_REVIEW.json`; it must not infer text quality from Executor summary or receipt alone.

After required Reviewer PASS and frozen human gates, perform integration preflight against then-current `main`. Preserve concurrent main changes. If `main` has competing edits in the same writing-style/version/release surfaces, return to Planner/integration decision instead of overwriting them. With no real conflict, merge/integrate per repository policy and verify the released install path.

### Release closure

If all gates pass and `main` has not independently advanced the affected versions, release as repository patch `5.0.4` with `writing-style 0.2`, bumping each exactly once. If concurrent release history changes those numeric baselines first, stop at integration decision; do not silently choose a new version or overwrite changelogs.

## Natural-language usage / routing expectations

Heavy Chinese rewrite examples that should naturally enter the new route:

- “把这份较长科研报告重新组织成自然中文，数字、公式、引用、比较条件和限制都不能丢；不要逐句翻译，也不要总结掉内容。”
- “内容都对，但现在像项目备忘录。按原意重新讲清楚，让第一次看的研究者能顺着读下去，正式算法名和数据集名保留。”
- “保留所有实验事实和结论强度，但允许重排章节和段落，把公式放回它真正回答的问题附近。”

Requests that must stay off the heavy route:

- “把这两句话改自然一点。” -> `chinese-prose` light/local path.
- “只检查数字、公式、引用和版本标签有没有被改。” -> fidelity-only path.
- “Polish this English Results paragraph without overclaiming.” -> existing `scientific-prose` route.

A user must never need to know or name `scientific-rewrite`, `REALIZE_MEANING`, Meaning Map, Reader Plan, stage packets, validator fields, or internal task identifiers.

## Out of scope

- No `writing-style -> clear-language` slug/display-name migration in 051.
- No presentations/research-writing/statistical-modeling/scientific-visualization/medical-imaging/bioinformatics consumer wiring in this task.
- No new generic dependency schema, Reviewed Handoff state/role, queue service, long-running worker, or model-isolation runtime.
- No redesign of English `scientific-prose` beyond minimal routing compatibility needed to prevent regression.
- No new external paid generation pipeline and no per-stage Terra review.
- No phrase blacklist, English-density/readability score, project-specific vocabulary rules, or holdout-specific tuning.
- No wholesale merge/vendor of the 050 branch, failed Round-6 work, or external humanizer repositories.
- No claim that one fresh holdout proves universal generalization.
- No automatic maturity promotion to `alpha`/`stable`.
- No publication of private source/rewrite plaintext, credentials, or manual reference text to the public repository.
