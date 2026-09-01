# 047 Source Adoption

This file records external-source inspection for `047_writing_style_scientific_rewrite_architecture`.

The external repositories were cloned only into machine-local research cache:

```text
/overflow/htzhu/mingcheng_new/.ai-skills-source-scout/047-scientific-rewrite/
```

No external repository is vendored into `AI_Skills_Collection` by this intake commit. Downloading, cloning, and inspecting a source is not adoption.

## Source A: MrGeDiao/shuorenhua

- source: `https://github.com/MrGeDiao/shuorenhua.git`
- exact commit: `6de1fcfeca5fff6fd15b28c619c11b6d41d1f657`
- commit summary: `feat: v2.4.0 技术术语按词义放行与 FAQ 条件顺序`
- local checkout status at inspection: detached `HEAD`, clean
- license: MIT
- license SHA256: `d26eebf6104e9770ca097771022767da18fc07ca73a542469d2748b2e3186878`
- inspected files:
  - `SKILL.md`
  - `references/positive-style.md`
  - `references/protected-spans.md`
  - `references/operation-manual.md`
  - `references/structures.md`
  - `references/examples.md`
  - `evals/real-samples.md`
  - `evals/benchmark.md`
  - `evals/human-corpus.jsonl`
  - `evals/results-v2.4.0.md`
  - `LICENSE`

### Actual capability

`shuorenhua` is a compact Chinese-first style cleanup system. Its useful architecture is not a phrase list; it separates:

- scene detection: `chat`, `status`, `docs`, `public-writing`, plus scene packs such as README, release note, issue reply, API reference, and FAQ;
- severity tier: whether a problem is strong enough to fix;
- rewrite level: `minimal`, `standard`, or `aggressive`;
- edit scope: `structural`, `bounded`, or `in-place`.

It also defines a positive style contract: concrete actions over abstract elevation, real subjects and actions over posture, natural rhythm without forced smoothness, ordinary sentences allowed, and register matched to the scene. The protected-span guidance usefully separates exact preservation for numbers, names, commands, citations, code, and quoted text from meaning preservation for completion state, conditions, comparisons, and responsibility.

The evaluation material is also relevant. It distinguishes should-fix and should-not-fix cases, records that synthetic benchmarks are not the same as real user samples, and explicitly treats scanner counts as debugging telemetry rather than final writing quality.

### Relationship to current writing-style

This overlaps strongly with the existing `chinese-prose` role and should not become a second active Chinese trigger. The useful pieces should be routed into the current `writing-style` architecture as:

- positive Chinese style contract for `chinese-prose`;
- scene/problem classification;
- pattern-first diagnosis with phrase fallback;
- should-fix / should-not-fix guardrails;
- examples of metadata-tagged transformations, not copied facts.

It does not provide a full scientific long-report orchestration layer. Its public-writing, forum, social, FAQ, and release-note material is useful for style boundary thinking but should not dominate scientific document rewriting.

### Adoption decision

`SELECTIVELY_PORTED`

Adopt ideas and small patterns only after Planner freezes target files. Do not wholesale vendor; do not create a runtime dependency; do not import broad chat, social-media, or public-writing phrase lists into the scientific route.

## Source B: whh110112/human-writing-skills

- source: `https://github.com/whh110112/human-writing-skills.git`
- exact commit: `2b02ae77bd1ea009ea2d7a1cc6d2dcdce1437a00`
- commit summary: `fix SkillHub package plugin exclusion`
- local checkout status at inspection: detached `HEAD`, clean
- license: MIT
- license SHA256: `4683c8e7b19375dad28c8589e7b31bb67eadcc6799ce14ab9feb64f1d21e3c1a`
- inspected files:
  - `SKILL.md`
  - `docs/long-form-consistency.md`
  - `docs/protected-content.md`
  - `docs/reference-style.md`
  - `docs/audit-pipeline.md`
  - `skills/rewrite-fidelity.md`
  - `humanwriting/original.py`
  - `humanwriting/reference.py`
  - `humanwriting/source.py`
  - `humanwriting/protection.py`
  - `humanwriting/longform.py`
  - `humanwriting/compiler.py`
  - `tests/test_longform.py`
  - `tests/test_protection.py`
  - `tests/test_compiler.py`
  - `LICENSE`

### Actual capability

`human-writing-skills` has a mature separation between deterministic packaging and model-executed editorial judgment:

- `original` is the authority for rewrite meaning and activates `rewrite-fidelity`;
- `reference` is style evidence only and must not supply facts;
- `source` is factual evidence only and must not become style material;
- `protection` performs narrow automatic protected-content detection for serious document types and deterministic exact-span comparison;
- `longform` chunks a large draft into bounded bodies with read-only lead-ins, baseline/context packs, manifests, agent plans, and coverage receipts;
- `compiler` activates modules based on explicit flags and document type, keeping fidelity, sources, protection, and style matching separate.

The `rewrite-fidelity` module is especially relevant. It asks for a compact claim ledger with statuses:

```text
preserved / narrowed / broadened / reversed / invented / omitted
```

That is close to the relation-level semantic audit 047 needs.

### Relationship to current writing-style

The architecture maps well to a scientific rewrite route inside `writing-style`:

- adapt the `original` / `reference` / `source` separation into `original scientific text`, `positive transformation examples`, and optional factual sources;
- adapt the claim ledger into `writing-fidelity`;
- adapt chunk package ideas into argument/discourse unit packets rather than fixed token chunks;
- adapt deterministic exact verification for literal invariants.

The repo also contains many fiction, webnovel, character, relationship, physical-continuity, and style imitation modules. Those are out of scope for scientific long-form rewriting and must not be copied into `writing-style`.

### Adoption decision

`SELECTIVELY_PORTED`

Planner should consider a small adapter or local helper pattern if implementation later needs deterministic `prepare`, `select-examples`, or `verify-exact`. Do not vendor the package, do not create a runtime dependency, and do not copy fiction/webnovel modules.

## Cross-source synthesis for Planner

Both sources support the same product direction:

1. Positive target definitions work better than only listing bad phrases.
2. Literal preservation and semantic preservation must be separated.
3. A small deterministic outer layer can prepare packets and check exact invariants, but it cannot judge naturalness or semantic equivalence.
4. Long-form work needs bounded units, global context, local meaning cards, and explicit coverage receipts.
5. Examples must teach transformation, not facts; source/reference/original authorities must stay separate.

The first implementation should therefore be an experimental internal route inside `writing-style`, not a new plugin, not a bulk external import, and not another prompt-only ban list.
