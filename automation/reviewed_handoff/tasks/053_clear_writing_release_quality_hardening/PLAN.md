---
schema: AI_BRIDGE_REVIEWED_PLAN_V2
task_key: 053_clear_writing_release_quality_hardening
decision: PLAN_FROZEN
---

# Reviewed Handoff Plan

## Objective and value

Close the observed Clear Writing 0.2 release-quality failures without redesigning the 051/052 heavy Chinese rewrite architecture. The target is a reader-ready Chinese scientific/technical artifact, not another mechanical receipt: clean Markdown, correctly rendered PDF, intact mathematics and tables, requested Simplified/Traditional Chinese, low unnecessary English/internal-audit language, and proposition-level fidelity across long documents.

Maintenance companion: `ai-skills-core`

Domain owner: `writing-style`

The canonical completion contract remains `docs/goals/053_CLEAR_WRITING_RELEASE_QUALITY_HARDENING_GOAL.md`. This Plan only makes that Goal executable; no child objective, phase, test, commit, or gate may weaken or replace it.

## Frozen decisions

Preserve the existing 051/052 ownership and heavy-route architecture:

- ordinary long Chinese/Chinese-dominant source-faithful technical rewrite continues to route through `writing-style` -> `scientific-rewrite`;
- Host Codex continues to own semantic extraction, Reader Plan, realization orchestration, assembly, semantic audit, repair, and final prose;
- `chinese-prose` continues to own `REALIZE_MEANING` and final reader-facing Chinese expression;
- `writing-fidelity` continues to protect the proposition/evidence graph, formulas, exact identities, attribution, conditions, caveats, uncertainty, comparisons, and conclusion strength;
- `rewrite_support.py` remains mechanical: it may extract/protect/check structured exact relationships and reject bad artifacts, but it must not become a prose generator or broad source-markup rewriter;
- `scientific-prose` remains the English route and must not be absorbed into the heavy Chinese path;
- 051 remains `STOPPED / NOT_RELEASED` history. Its Gate 4 Deep Research artifact is a read-only style/render floor, not a releasable predecessor and not fresh evidence;
- 052 remains completed history. Its Bloom/Python `re`/FFT and packet-isolation evidence are known regressions only and do not prove 053 quality by themselves.

Observed failure ownership is frozen as follows:

1. Raw wiki/HTML/template/citation syntax leakage is a source-representation-to-reader-output contract failure. `scientific-rewrite` must treat platform syntax as representation rather than reader prose; candidate-level mechanical validation may reject leaked syntax. Citation meaning, mathematical relations, and legitimate attribution must survive normalization.
2. Formula-like fenced `text`, raw/unrendered LaTeX, and raw Markdown-table presentation are candidate representation failures. The candidate must contain normal renderable Markdown/LaTeX math and renderable tables before PDF rendering. The renderer may verify presentation but may not hide a bad candidate.
3. Operator/symbol loss such as `k − 1 -> k 1`, damaged subscripts/exponents, or broken variable relations is a fidelity failure. Protect the relation itself, not merely nearby digits or tokens. Any helper change must preserve rather than rewrite mathematical semantics.
4. Simplified/Traditional Chinese consistency is a reader-facing language constraint owned by the existing Chinese realization/final-pass layer. Default to Simplified Chinese for ordinary Simplified-Chinese requests unless the user requests Traditional Chinese; proper nouns, formulas, code, paths, citations, datasets, metrics, APIs, and necessary acronyms remain unchanged.
5. Unnecessary ordinary English and internal `provenance`/`audit`/repository/planning language are Chinese realization/relevance failures. Keep formal identities and legitimate scholarly attribution; remove process framing from reader prose.
6. Long-document proposition/fidelity drift is a structural fidelity failure. Full-source proposition/evidence coverage, conditions, attribution, uncertainty, negative findings, formulas, citations, and decision boundaries must survive regrouping. Exact-token checks alone are insufficient.

The implementation must compare and reject these alternatives:

- **Renderer-only masking:** rejected because a dirty Markdown candidate or lost operator cannot be repaired by PDF rendering.
- **Large mechanical source-markup postprocessor:** rejected because broad regex/string rewriting can damage operators, citations, subscripts, formulas, and source meaning. Mechanical code may parse/protect/check narrowly defined structures and fail closed, not author prose.
- **Heavy-route rewrite or a new top-level writing plugin/skill:** rejected because 051/052 already established the routing/Meaning Map/Reader Plan/REALIZE_MEANING architecture; 053 is a bounded quality hardening.
- **Prompt-only wording tweak as the whole fix:** insufficient where deterministic representation/fidelity failures require explicit contracts and validators. Prompt/skill-contract clarification is allowed as part of the existing architecture, but it must be paired with observable regressions for symbols, renderability, language variant, and proposition coverage.
- **New Reviewed Handoff schema/state/ledger/runtime/Bridge/Host Policy framework:** rejected. Reuse current workflow and existing canonical candidate/Text Review paths.

Before editing production plugin source, Executor must confirm production `ai-skills-core` is installed/enabled and actually invoke it for maintenance preflight. `ai-skills-core` owns source authority, duplicate/TODO triage, generated parity, production replay, unrelated regressions, version/changelog/release closure, and release-policy checks; `writing-style` owns language/fidelity judgments.

If a real execution-process failure occurs during 053 that is independent of writing-style semantics, explicitly test whether it can recur in future AI_Skills tasks. Only when there is a concrete observed failure plus a minimal reusable prevention rule should Executor add concise generic AGENTS/workflow hardening, preferably as a separate governance commit safe to integrate independently. Do not invent new control-plane infrastructure merely to document an incident.

## Positive completion

053 is complete only when the final frozen Clear Writing candidate produces genuinely reader-ready Markdown/PDF rather than merely passing mechanical checks. The observable product result must simultaneously satisfy all of the following:

- Bloom known regression contains no reader-visible raw wiki/HTML/template/citation markup, preserves the Bloom mechanism, citation meaning, target Chinese variant, and relations such as `k − 1`, and does not regress 052 source-process framing;
- FFT known regression uses real renderable math rather than fenced `text`, preserves DFT and complexity relations/conditions/attribution, and renders cleanly;
- the complete private Deep Research source is directly replayed by the final 053 candidate, not substituted by predecessor evidence; its Markdown/PDF is at least as good as the 051 Gate 4 style/render floor on formula/table readability while retaining useful 0.2 structural expansion, substantially reducing ordinary English/internal audit framing, and preserving proposition/evidence boundaries throughout the full document;
- Python `re`, light-Chinese polish, fidelity-only, English `scientific-prose`, 052 source-process framing, and review-packet isolation remain compatible;
- exactly two pre-frozen fresh public-safe holdouts from different document families both pass as a complete batch, in both Markdown and rendered PDF, with proposition/exact-item audit; one is math/markup-rich and one is long-form Chinese scientific/technical material;
- one and only one final candidate-only `gpt-5.6-terra` Text Review passes after all local/known/fresh/render gates; the review plaintext contains only natural document titles plus real candidate texts, while task/Gate/recovery/candidate/Reviewer metadata remains outside plaintext;
- focused tests, full tests, source/generated parity, required release CI, version/changelog closure, bounded production install/upgrade smoke, and ordinary natural production routing all pass;
- Scheduled GPT Reviewer independently establishes both PROCESS PASS and PRODUCT / ARTIFACT PASS for the evidence it can actually inspect;
- the comprehensive acceptance dossier and complete Deep Research final PDF exist under `private/exports/053_clear_writing_release_quality_hardening/`, the user returns `ACCEPT`, and 053 is integrated conflict-free into then-current `main` with remote/released Clear Writing identity verified.

Maximum claim scope: PASS supports this bounded 053 release-quality closure for Clear Writing heavy Chinese scientific/technical rewrite plus the explicitly tested compatibility routes. It does not establish universal writing quality, arbitrary markup conversion, domain-semantic authorship, a new renderer, or correctness for all languages/document families.

A partial implementation, local test pass, candidate replay, CI pass, Reviewer handoff, or human-gate arrival is `IN_PROGRESS`, never overall Goal completion.

## Non-substitutable semantics

- **Candidate quality precedes rendering.** Markdown itself must be reader-clean and semantically correct. PDF QA is an additional gate, not a sanitizer.
- **Mathematics is semantic content.** Operators, signs, exponents, subscripts, variables, equalities/inequalities, asymptotic relations, and scope/conditions must survive source interpretation and realization. A formula represented as ordinary fenced text is not an acceptable substitute for renderable math.
- **Markup is representation, not prose.** `{{...}}`, `<ref>...</ref>`, HTML comments, wiki citation/template scaffolding, and analogous source-platform syntax must not appear in normal reader-facing prose unless the user explicitly asks to discuss markup/code. Their scientific/citation meaning must not be deleted with the syntax.
- **Tables remain tables.** Tabular scientific content may be reorganized when structurally authorized, but final Markdown/PDF must present it as an actual readable table or an intentionally re-expressed semantic structure; raw Markdown table syntax rendered as body text is failure.
- **Target Chinese variant is part of the request.** Simplified/Traditional normalization may touch ordinary prose only. It must not alter protected formal identities or scientific notation.
- **English retention is semantic, not blacklist-driven.** Keep formal names, model/algorithm/dataset/metric identities, code, paths, APIs, citations, and terms whose English is required for precision/lookup. Ordinary reasoning, transitions, internal audit language, and repository/process framing should be natural Chinese when the target is Chinese.
- **Structural rewrite may reorder; it may not drift.** Reader Plan restructuring is allowed, but every substantive source proposition must retain evidence authority, attribution, polarity, conditions, comparators, caveats, uncertainty, limitation, and conclusion strength. No unsupported strengthening, invention, omission, or reattribution.
- **051 is a style/render floor only.** Do not copy its structure blindly, modify its stopped history, or claim it was released. A 053 candidate may be more complete than 051 but may not regress below its formula/table/readability baseline merely to satisfy 052's narrower rubric.
- **052 evidence is regression evidence, not fresh generalization.** Bloom, FFT, Python `re`, and wrapper/source-process cases cannot be counted among the two 053 fresh holdouts.
- **Complete Deep Research evidence is mandatory.** The exact private source must be replayed by the 053 candidate. Existing 0.2/051 outputs are comparison baselines only. At most two 053 candidate replays of that exact private source are authorized; if the second 053 replay still cannot close the known regression, stop 053 under the current scope rather than requesting a routine third replay.
- **Fresh evaluation is a frozen two-item batch.** After known regressions pass, freeze the production candidate and a manifest containing exactly two public-safe, semantically complete sources: H1 math/markup-rich technical material and H2 long-form Chinese scientific/technical material, from different document families and unused for 050–053 tuning. Freeze source identity/range/hash/completeness evidence before candidate generation. No adaptive third holdout, no replacement after seeing output, and no production tuning during the batch. Any true holdout failure fails the 053 fresh gate under this Plan.
- **Paid review is single-shot and last among artifact-quality gates.** Exactly one final `gpt-5.6-terra` Text Review is authorized, `store=false`, automatic paid retry `0`, worst-case per-call cost `<= USD 0.25`, only after known regressions, both fresh holdouts, and rendered QA pass. No second paid Terra review under 053.
- **Private scope is fixed.** Only the already-authorized same Deep Research private artifact may be used candidate-only through existing canonical Codex/OpenAI and final Text Review paths. No new private artifact, provider, credential transfer, or broader cost scope.

## Implementation scope

Production changes must stay inside the existing Clear Writing architecture and the minimum supporting release surface:

- `skills/writing/core/scientific-rewrite/SKILL.md` and its existing scripts, especially `scripts/rewrite_support.py`, for heavy-route representation/fidelity/output contracts and narrow mechanical validation/protection;
- `skills/writing/core/chinese-prose/SKILL.md` for natural Chinese realization, target Simplified/Traditional consistency, necessary-vs-ordinary English decisions, and reader-facing removal of internal audit/planning language;
- `skills/writing/core/writing-fidelity/SKILL.md` for mathematical/proposition/evidence preservation and long-document structural fidelity;
- `skills/writing/core/scientific-prose/SKILL.md` only if needed to preserve compatibility; do not redesign the English route;
- focused tests such as `tests/test_scientific_rewrite.py` and existing writing-style/chinese-prose/fidelity tests; add narrow regressions for observed failures rather than a parallel framework;
- canonical source-to-generated Marketplace surfaces, including generated `plugins/codex/plugins/writing-style/**`, only through the existing generator/source authority rather than hand-edited divergence;
- existing writing-style marketplace/version/changelog/release metadata and repository release dashboard/version contract if the production behavior changes and is accepted;
- `docs/plugin-todos/writing-style.md` for this real-use failure record;
- `results/053_clear_writing_release_quality_hardening/**` for public-safe manifests, regression artifacts, audits, render QA evidence, Text Review evidence, release evidence, and Reviewer artifacts;
- repo-local `private/exports/053_clear_writing_release_quality_hardening/**` for private Deep Research replay, rendered PDF, comparison evidence, and final human acceptance dossier. Private plaintext must not be committed or pushed.

Do not modify the PDF renderer merely to make a failing candidate look clean. Reuse the mature `render-chinese-math-pdf` route for actual render QA. Do not create a new top-level skill/plugin, alternate heavy runtime, schema/state/ledger, or review transport.

The minimal likely mechanical extension is to make exact/representation validation understand the observed raw-markup math/operator structures and reader-visible artifact defects without mechanically authoring prose. Executor must first write focused failing tests from the observed cases, then choose the smallest owner-layer changes that close them.

## Acceptance and regression gates

Execute in this order. Later gates cannot compensate for an earlier failure.

1. **Maintenance preflight / source authority**
   - production `ai-skills-core` is installed/enabled and actually invoked;
   - confirm current source/generated authority, duplicate/TODO status, latest version policy, release contract, and exact branch state;
   - no production change before capturing focused failing regressions for the observed 0.2 defects.

2. **Focused implementation/mechanical regressions**
   - raw wiki/template/HTML/citation syntax leakage is detected/rejected in normal reader candidates without deleting citation meaning;
   - formula-like fenced `text`, unrendered math, and raw table presentation fail the appropriate candidate/render gate;
   - `k − 1`, `k-1`, exponents, subscripts, signs, variables, and mathematical relations survive extraction/normalization/realization checks;
   - requested Simplified/Traditional Chinese constraint is testable while protected technical identities remain unchanged;
   - ordinary-English/internal-audit framing regressions are covered without global English banning;
   - proposition/evidence audit catches critical omission, invention, strengthening, changed condition/comparator, reattribution, lost uncertainty, or detached caveat;
   - source-process framing and internal workflow leakage tests from 052 remain PASS;
   - source and generated plugin surfaces are kept in parity through the existing generator.

3. **Known product regressions — all must PASS before any fresh evaluation**
   - **K1 Bloom raw wikitext:** rerun the public known source. Require no raw wiki/HTML/template syntax, readable citation meaning, intact `k − 1`/variable relations, correct requested Chinese variant, and no source-process regression. Preserve 051 Bloom only as historical failure evidence and the 052 Bloom output only as known regression evidence.
   - **K2 FFT math:** rerun the known FFT case. Require a real DFT mathematical expression rather than fenced text; correct `O(N^2)`, `O(N log N)`, `(N/2)\log_2 N` relations, Cooley–Tukey condition/caveat/attribution, and clean PDF formula rendering.
   - **K3 complete Deep Research:** directly run the complete exact private source through the current 053 candidate. Compare the full candidate against both the immutable 051 Gate 4 historical artifact and current 0.2 diagnostic. Inspect the whole document, not only opening pages. Require formula/table readability at least at the 051 style/render floor, materially lower unnecessary English/internal audit framing than 0.2, direct reader-facing opening, full proposition/evidence coverage, unchanged numerical/method/citation/GO-STOP/uncertainty boundaries, and a clean complete PDF. Maximum two 053 candidate replays total for this exact private source; replay count and source identity must be recorded.
   - **K4 compatibility:** Python `re`, light-Chinese polish, fidelity-only, English `scientific-prose`, 052 source-process framing, and 052 review-packet wrapper isolation all remain PASS.

4. **Candidate and fresh-holdout freeze**
   - after K1–K4 PASS, freeze the exact production candidate commit;
   - before any fresh candidate generation, write one complete two-item holdout manifest with exact source URLs/locators, source ranges, hashes, document-family labels, public-safe status, semantic-completeness evidence, and explicit evidence that neither source was used in 050–053 tuning;
   - H1 must be math/markup-rich technical material containing real formulas/symbols plus citation or structured markup;
   - H2 must be a semantically complete long-form Chinese scientific/technical reader document, not task/CI/FINAL_REPORT/plugin source/synthetic toy;
   - H1 and H2 must come from different document families;
   - batch size is exactly two, replacement is forbidden, and the production candidate cannot change after freeze.

5. **Fresh two-item generalization batch**
   - run both frozen sources exactly once through the frozen candidate as needed by the canonical replay path;
   - retain candidate Markdown, source/candidate proposition audit, exact-item audit, and normal rendered PDF for each;
   - any real failure fails the whole fresh gate. Do not tune on the failed output, replace it, or add a third holdout under 053.

6. **Reader-visible render QA**
   - using the existing `render-chinese-math-pdf` route, render and actually inspect Bloom, FFT, both fresh holdouts, and the complete Deep Research final artifact;
   - verify no visible raw wiki/HTML/template syntax, raw Markdown table-as-text, unrendered LaTeX, formula code fences, clipping, missing glyphs, operator/subscript/exponent loss, requested-script mismatch, workflow/provenance leakage, audit-like opening, or unnecessary English sentence scaffolding;
   - file existence or renderer success alone is not PASS. Public-safe rendered evidence must be inspectable by Reviewer; private Deep Research render stays repo-private for Terra/user acceptance.

7. **Single final independent Terra review**
   - only after Gates 1–6 above are PASS and candidate is frozen;
   - exactly one `gpt-5.6-terra` candidate-only Text Review, `store=false`, automatic paid retry `0`, worst-case `<= USD 0.25`;
   - plaintext contains only natural document titles plus real final candidate texts. All Gate/task/recovery/candidate/Reviewer/Executor/commit/hash/run metadata remains in manifest/metadata and outside reader-facing plaintext;
   - rubric covers natural target Chinese, formula/table representation, raw markup leakage, symbol/operator loss, internal audit/planning language, fact/condition/limitation/attribution drift, and whether the complete Deep Research report reads like a document for an advisor/reader rather than an execution record;
   - a Terra REVISE cannot trigger a second paid review within 053. Route to the legal Planner/human stop decision rather than silently retrying or expanding scope.

8. **Release closure / production entrypoint**
   - Terra PASS first, then focused + full tests, generator/source parity, required release CI, version/changelog/repository release closure, bounded live install/upgrade smoke, ordinary natural heavy-route production smoke, and restoration/verification of prior live state;
   - if accepted changes alter user-facing production behavior and current policy still requires it, bump Clear Writing exactly once (expected `0.2 -> 0.3` under the current Goal, but read current policy at execution time) and update all required generated/version/changelog/dashboard surfaces. Do not hard-code repository version;
   - no fake `Unreleased` deferral for a completed production behavior change.

9. **Scheduled GPT Reviewer**
   - independently inspect real production diff, source/generated parity, focused/full/CI evidence, K1–K4 outputs, both frozen fresh holdout Markdown artifacts and rendered-PDF QA evidence, final Terra evidence, production install/routing smoke, version/changelog closure, and public artifact quality;
   - explicitly separate PROCESS PASS from PRODUCT / ARTIFACT PASS;
   - receipts/Executor summaries cannot substitute for reading public candidate artifacts and render evidence;
   - if the private Deep Research plaintext/PDF is unavailable in the Reviewer environment, state that limitation rather than pretending to inspect it. Terra's candidate review plus the user's final PDF acceptance remain mandatory private-artifact gates;
   - Reviewer must REVISE for visible raw markup, formula-like fenced text, unrendered math, raw Markdown table presentation, operator/symbol loss, obvious target-script mismatch, unnecessary workflow/audit framing, critical meaning/condition/attribution drift, or a quality regression below the 051 historical style/render floor.

10. **Final human artifact acceptance and integration**
    - after Reviewer PASS, generate/retain under `private/exports/053_clear_writing_release_quality_hardening/` at least `Clear_Writing_0.3_Comprehensive_Acceptance_Dossier.pdf`, `Clear_Writing_Deep_Research_Final.pdf`, corresponding Markdown/source identity, and an evidence index;
    - dossier must be a reader-facing PDF, not a log dump, and include 0.2 failures; Bloom source/0.2/final; FFT source/0.2/final; representative Deep Research 051/0.2/final comparison plus complete final PDF; both fresh holdouts; unrelated regressions; Terra/Reviewer/production smoke; remaining limitations; and a concise acceptance checklist;
    - ask the user only `ACCEPT` or `REJECT` at this planned gate;
    - only `ACCEPT` authorizes latest-main integration. Then fetch current main, preserve concurrent work, run integration preflight, merge conflict-free, non-force push, verify remote main and released Clear Writing identity/ordinary routing. Only then may overall Goal be reported achieved.

## Natural-language usage / routing expectations

Ordinary users must not need internal route names or QA terms. Examples that should select the existing heavy route naturally include:

```text
把这份较长的中文科研报告重新组织成能直接给导师看的版本。数字、公式、引用、比较条件和限制都不能丢；公式要正常排版，正文用简体中文，不要留下网页模板或内部审计口吻。
```

```text
这是一份中文技术材料，请在不改变结论、条件、公式和引用的前提下重写得更清楚。表格和数学关系要能正常渲染，普通英文能用中文说清就用中文，正式方法名和代码保持原样。
```

```text
请把这份技术说明整理成繁体中文成稿。保留算法名、变量、公式、引用和代码，不要把來源網站的模板語法帶進正文。
```

Short/local Chinese polish must continue to use the light Chinese path rather than forcing the heavy route. Fidelity-only checking remains checking, not rewriting. English scientific material remains on `scientific-prose`.

Reader-facing output should state the scientific/technical subject directly. Internal evidence may record task ids, commits, Gates, audits, candidate identities, or run metadata, but normal candidate prose and final Text Review plaintext must not use those as the document's narrative frame.

## Out of scope

- Reopening, rewriting, or relabeling 051; claiming 051 was released.
- Re-proving 052 or treating its PASS as universal quality evidence.
- New top-level writing skill/plugin, slug migration, plugin identity migration, or broad cross-plugin language redesign.
- New heavy rewrite architecture, nested model runtime, second generation engine, Bridge Kit/Host Policy/execpolicy redesign, or new workflow/schema/state/ledger infrastructure.
- Renderer-only fixes that leave the Markdown candidate bad, or a new PDF renderer instead of the existing mature Chinese-math render route.
- Broad regex/postprocessor systems that mechanically rewrite source markup into prose.
- Project-specific banned-word lists, global English bans, or blanket Simplified/Traditional conversion of protected identifiers.
- Domain-semantic fact selection, new scientific claims, new literature research, or changing the source's scientific conclusions to improve readability.
- Adaptive fresh-holdout replacement, a third holdout, tuning against fresh outputs, or combining successes across multiple batches to claim generalization.
- More than two 053 replays of the exact private Deep Research source.
- More than one paid Terra Text Review, automatic paid retry, provider/credential changes, new private artifacts, or per-call worst-case cost above USD 0.25.
- User prompts for already-authorized branch/worktree/candidate-cache/same-provider private replay/CI/production-smoke/push/integration mechanics. Only genuinely expanded authorization scope, a true unrecoverable blocker, unresolved integration conflict, the planned final ACCEPT/REJECT gate, or final successful integration may notify the user.
