# Reviewed Handoff Request — 048_writing_style_product_cutover_and_readable_report

## Product objective

Finish the `writing-style` refinement as a real user-facing capability, not another architecture-only experiment.

The user requires **two concrete deliverables**:

1. A usable `writing-style` plugin whose normal installed entrypoint can automatically route long Chinese scientific/technical rewrites into a meaning-first, fidelity-constrained `scientific-rewrite` path.
2. A complete, readable rewrite of the user's existing 22-page Deep Research report titled `共享预训练医学分割模型下的极低通信联邦适应：项目事实审计、算法前沿与下一轮实验决策`, preserving the scientific content while making the report genuinely easy to read before the user starts the next experiments.

Both are required. A plugin-only PASS without the readable report is not product completion; a manually readable report without a real production `writing-style` route is also not product completion.

## Why this is a new task

Task 047 ended at `AWAIT_HUMAN_DECISION` without Product PASS. It produced a useful experimental implementation candidate at:

`ade5a1f653f88df07eb0c70edfd016c744b1611a`

and public holdout evidence suggesting the architecture is promising, but its frozen acceptance contract made a private 044 Codex/OpenAI replay a blocking gate. That replay was rejected by execution policy even after explicit user authorization, so 047 could not truthfully enter Product PASS or merge.

The user has now clarified that this private-transport gate was not the product goal. The real product goal is the usable plugin plus the readable report itself.

047 therefore remains historical experimental evidence. 048 must start from current `main`, selectively reuse the good 047 implementation where justified, and define acceptance around the actual two deliverables.

## Relationship to 044

`reviewed/044_writing_style_deep_research_chinese_replay` must not be reopened, repaired, or used as a control-plane blocker.

The **044 workflow is historical**. The underlying Deep Research report is still extremely important, but now only as the user's target deliverable / known regression artifact.

Do not require Codex to upload or send that private report to an external endpoint as a prerequisite for plugin release. The prior execution-policy failure already proved that path is unreliable in this environment.

The source report is available to the user in ChatGPT/File Library. The final private readable report may therefore be generated and reviewed on the ChatGPT-attached-source surface after the 048 rewrite contract is frozen. The private plaintext must not be committed to this public repository. Repository evidence may record only non-sensitive artifact identity, hash, acceptance status, and bounded findings.

## Existing evidence to reuse, not redo from zero

### 047 candidate implementation

Read the final 047 branch and inspect the actual diff/implementation at `ade5a1f653f88df07eb0c70edfd016c744b1611a`.

Useful candidate capabilities include:

- internal `scientific-rewrite` orchestration inside the existing `writing-style` plugin;
- meaning-first rewrite packets / Meaning Cards;
- literal-vs-semantic fidelity separation;
- metadata-selected positive transformations;
- exact literal checks;
- normal `writing-style` routing without creating another top-level plugin.

Do not blindly cherry-pick the entire 047 branch. Planner must identify which production changes are worth carrying forward from the implementation freeze commit and which task-control/evidence files stay historical.

### External source decisions already established

Keep these decisions unless new evidence proves them wrong:

- `MrGeDiao/shuorenhua@6de1fcfeca5fff6fd15b28c619c11b6d41d1f657`, MIT: `SELECTIVELY_PORTED` for positive Chinese style, scene/scope thinking, literal-vs-semantic protection, SF/SNF evaluation philosophy.
- `whh110112/human-writing-skills@2b02ae77bd1ea009ea2d7a1cc6d2dcdce1437a00`, MIT: `SELECTIVELY_PORTED` for original/reference/source authority separation, claim-ledger fidelity, bounded long-form context, deterministic exact checks.
- `AIScientists-Dev/academic-humanizer@94b88b23703bed7df507acae7d6d5876209a0cdf`, MIT: `REFERENCE_ONLY` for a later English academic-writing audit; do not expand 048 scope with its AI-tell lists or duplicate existing `scientific-prose` rules.

No new broad Source Scout is required.

## Product acceptance — plugin

The production `writing-style` candidate must satisfy all of the following:

- The only top-level user entry remains `writing-style`.
- A normal long-form Chinese scientific rewrite request automatically selects the scientific-rewrite path from an installed/generated plugin; users must not specify a hidden skill path or benchmark helper.
- Ordinary light Chinese polishing must still route to the lighter `chinese-prose` behavior.
- The scientific rewrite path must be meaning-first rather than phrase-blacklist-first.
- `writing-fidelity` must distinguish literal preservation from semantic preservation so reader-facing headings and sentence structure can be rewritten while numbers, formulas, citations, formal identifiers and scientific meaning remain protected.
- Positive examples teach transformations, not facts; they must not be allowed to leak new scientific content into the target.
- The production entrypoint must be tested in an isolated/shadow install through the normal Marketplace/plugin mechanism. Do not mutate the user's live global plugin cache merely to prove entrypoint behavior.
- Required tests, source/generated parity, install smoke, CI, and independent Reviewer evidence must pass.
- Public / non-private regression and should-not-fix evidence must show no critical fidelity damage and no systematic over-rewrite.

## Product acceptance — private readable report

The user-facing acceptance artifact is the complete Deep Research report, not an excerpt and not a summary.

The rewrite must preserve all scientifically material information from the supplied source, including:

- factual project history and current evidence;
- numbers, sample sizes, datasets, models, methods and comparisons;
- equations / notation;
- citations and bibliographic identities;
- uncertainty, caveats and evidence strength;
- negative results and STOP/GO logic;
- next-experiment recommendations and decision conditions.

But it must substantially lower reader effort. The rewritten report should explain what each section is actually saying in natural Chinese rather than keeping English abstract labels, audit jargon, repo/process language or translationese as the sentence skeleton.

The intended reader is a technically capable researcher who understands statistics / medical imaging but should not need to decode the project's internal repo/workflow language.

The report must remain long-form and information-complete. Do not achieve readability by turning it into a short executive summary.

### Private artifact generation boundary

Do not make `codex exec` external transmission of the private report a blocking requirement again.

After the 048 rewrite contract / candidate is frozen, the private report may be generated on the ChatGPT surface where the user already supplied the PDF. That artifact is then reviewed by the user. The repository should store only a non-sensitive acceptance receipt such as:

- source artifact identity/title;
- candidate artifact SHA-256;
- rewrite-contract/implementation commit used;
- user decision: ACCEPT / REJECT;
- concise non-sensitive findings.

Do not commit the private report plaintext.

## Final product gate

Product PASS requires **both**:

A. `writing-style` production candidate passes technical/behavioral validation and independent review; and

B. the user reads the private rewritten Deep Research report and explicitly accepts its readability/fidelity for actual research use.

If A passes but B fails, the task is not done; use the user's report feedback as the primary real-artifact regression and make only bounded generic repairs.

If B passes but A fails, the task is also not done; do not ship a manual one-off rewrite as a substitute for the plugin.

The task should normally stop at `AWAIT_HUMAN_DECISION` with both candidate plugin evidence and the private report acceptance request ready. Merge/version release happens only after the user's explicit acceptance.

## Scope constraints

- Do not reopen or continue 044 Reviewed Handoff.
- Do not continue 047 control-plane state; use it only as evidence/candidate implementation.
- Do not create another top-level plugin.
- Do not add Gemini, Claude routing, fine-tuning, embeddings, FAISS/Chroma/BGE, or a new vector database.
- Do not reintroduce phrase-wall / forbidden-English-count acceptance.
- Do not use AI-detector score as a product metric.
- Do not make a private external-upload path a mandatory product gate.
- Do not modify `presentations` or unrelated plugin versions.
- Do not claim production maturity solely from public holdouts; the user's actual report acceptance is required.

## Version/release planning

Do not bump versions at intake.

If the final 048 candidate changes real `writing-style` production behavior and both product gates pass, Planner/Reviewer should apply the current repository versioning policy at execution-time latest `main`: bump `writing-style` exactly once for the released batch and make only the corresponding compatible repository patch release. Do not hardcode the exact numbers now because `main` may advance.

If product acceptance fails, `NO_BUMP / NO_CUTOVER` is required.
