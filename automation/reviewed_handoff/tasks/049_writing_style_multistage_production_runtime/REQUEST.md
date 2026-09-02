# Reviewed Handoff Request — 049_writing_style_multistage_production_runtime

## Product objective

Recover `writing-style` from the 048 production failure and finish the capability as a real product.

The user requires two deliverables:

1. A production-usable `writing-style` plugin whose normal installed entrypoint truly executes a meaning-first multistage long-form Chinese scientific rewrite runtime rather than merely describing one in `SKILL.md`.
2. A new complete rewrite of the user's private Deep Research report that the user is willing to read for actual research and upcoming experiments.

The second deliverable is the product proof for the first. A technically correct plugin that still produces an unreadable report is not complete.

## Why 048 is rejected

Read:

`results/049_writing_style_multistage_production_runtime/FAILURE_ANALYSIS.md`

048 is historical evidence, not a branch to continue.

Its useful pieces must be preserved selectively:

- `scientific-rewrite` conceptual architecture and fidelity boundaries;
- secure private Text Transform transport in `GPT_Codex_AI_Bridge_Kit`;
- private Text Review transport;
- production routing evidence patterns;
- public regression and should-not-fix concepts.

Its Product PASS is rejected because the actual reader-facing artifact failed immediately in human use even though automated Text Review and Review 2 both said PASS.

Do not reopen 044, 047 or 048 control-plane state. Do not invent Review 3 for 048.

## Core failure to solve

The production runtime must stop treating this as one operation:

```text
full private source + full instruction bundle -> one model call -> full rewrite
```

The runtime must actually execute the meaning-first architecture with bounded responsibilities and observable intermediate contracts.

## Frozen product behavior

### Normal user entry

There remains one top-level plugin: `writing-style`.

A normal request such as:

> 把这份中文科研长报告说人话，但不要改变事实、公式、数字、引用、比较、限制条件和结论强度。

must automatically route to the heavy scientific-rewrite runtime.

Short/light Chinese polishing must remain with `chinese-prose`; fidelity-only requests must remain with `writing-fidelity`.

### Real multistage rewrite

The long-form route must execute, not merely document, this sequence:

```text
source
-> document map
-> argument-unit segmentation
-> per-unit Meaning Card + Fidelity Ledger
-> source-to-card coverage check
-> per-unit positive-example selection
-> per-unit rewrite from meaning + original
-> deterministic literal verification
-> semantic claim/relation audit
-> targeted repair
-> candidate-only reader review
-> whole-document assembly/coherence review
```

A single model call may not impersonate these stages.

### Reader Core vs Technical Trace

Fidelity must distinguish:

- `inline-critical`: material whose exact presence belongs in the reader-facing scientific argument;
- `relocatable-trace`: paths, exact implementation identities, detailed audit evidence or similar exact trace items that must remain available but may move to a clearly labeled technical/evidence appendix.

No scientific fact may disappear. The purpose is to preserve information without forcing all low-level trace material into the primary reading path.

This is a general long-form scientific-writing behavior, not a rule specific to the private Deep Research report.

### Review separation

Two different review questions are required:

1. **Source-aware fidelity review** — sees source + candidate and checks facts, claims, uncertainty, attribution, comparisons, caveats and conclusion strength.
2. **Candidate-only reader review** — sees candidate + intended audience, not the source, and judges whether the document can be understood without decoding internal workflow/audit vocabulary.

Automated reader review is supporting evidence, not a substitute for the user's acceptance.

## Mandatory style smoke before full private run

Do not generate the full private report immediately.

After implementation is frozen and production routing is validated, generate only three representative private rewrite samples:

1. opening + checkpoint interpretation;
2. ODAL vs FedFisher / FedLPA relationship;
3. next-round experiment design / GO-STOP decision.

Do not commit plaintext. Use the existing secure private transport.

The user must inspect these three samples and decide:

`STYLE_ACCEPT` or `STYLE_REJECT`.

Only `STYLE_ACCEPT` authorizes the expensive full-document generation.

If rejected, repair generic runtime/style behavior only. Do not add target-document phrase blacklists.

## Full private report acceptance

After style smoke acceptance:

- generate the complete report using the same frozen runtime;
- preserve all scientifically material content;
- allow reader-facing restructuring and relocation of trace-heavy exact material to a technical appendix;
- run deterministic exact checks;
- run source-aware semantic fidelity review;
- run candidate-only reader review;
- render the private Markdown to a readable PDF if the existing Chinese/math PDF route is available;
- give both private Markdown and PDF to the user for actual reading.

Final release requires explicit user `ACCEPT`.

## External source decisions

Keep existing decisions:

- `MrGeDiao/shuorenhua@6de1fcfeca5fff6fd15b28c619c11b6d41d1f657`, MIT: `SELECTIVELY_PORTED`.
- `whh110112/human-writing-skills@2b02ae77bd1ea009ea2d7a1cc6d2dcdce1437a00`, MIT: `SELECTIVELY_PORTED`.
- `AIScientists-Dev/academic-humanizer@94b88b23703bed7df507acae7d6d5876209a0cdf`: `REFERENCE_ONLY` for later English academic-writing review.

No new broad Source Scout, fine-tuning, embeddings/vector DB, Gemini, Claude routing or AI-detector gate.

## Ownership

Use:

`workflow-core + ai-skills-core + writing-style`

Writing-style owns scientific rewrite semantics and stage contracts.

`GPT_Codex_AI_Bridge_Kit` owns private encryption/API transport. Reuse its current secure transform/review infrastructure. If a small generic transport hook is needed to execute multiple bounded stages inside the ephemeral runner, implement only the minimum reusable Bridge Kit companion needed; do not move scientific-writing policy into Bridge Kit.

## Public regression

Reuse prior public materials as regression only, not unseen proof. Include at least:

- one rewrite-needed technical/scientific example;
- one should-not-fix example.

The decisive quality gate remains the private style smoke and final human reading.

## Scope constraints

Do not:

- modify `presentations`;
- reopen 044/047/048;
- merge 048 branch history wholesale;
- create another top-level plugin;
- add phrase-wall or specific banned-English lists;
- use English percentage or AI-detector score as quality proof;
- make `SKILL.md` documentation count as runtime execution;
- run the full private report before style smoke acceptance;
- claim Product PASS from automated Reviewer PASS alone.

## Release boundary

No version bump at intake.

If and only if the final private report is explicitly accepted and all technical gates pass, follow the latest repository versioning policy and bump `writing-style` exactly once as the compatible user-facing improvement batch.
