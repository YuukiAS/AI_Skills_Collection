# 050 Round-3 Process Diagnosis — why the reader pass can PASS while the prose still fails

## Decision

Do not immediately add another writing rule layer.

The round-3 artifact still fails the human style gate, but the current evidence no longer points first to a missing `scientific-rewrite` concept. The stronger blocker is that the smoke generation/evaluation path is not a clean production replay and the terminal Chinese reader pass can self-certify without candidate-grounded enforcement.

The next experiment should therefore separate **plugin behavior** from **executor/debug-context contamination** before changing production source again.

No private source or candidate prose is recorded here.

## Verified process facts

1. Round-3 implementation is `bac6bf37ee22b52a2894c90a385dd6ab0e8f0292`.
2. The round-3 smoke manifests explicitly record `plugin_replay_actual = not run for round-3 smoke`.
3. The smoke route is recorded as current host Codex plus generated `writing-style/scientific-rewrite` stage authoring and `validate-host-stage` validation.
4. Therefore the same executor/debugging context that read the 050 Plan, rejection analyses, repair prompt and smoke metadata can also author the private stage package and candidate.
5. SMOKE-A's public role string itself contains `checkpoint-estimand-and-next-decision`. This directly reintroduces a reader-facing English reasoning term into the generation context even though the style goal is to translate ordinary reasoning language into natural Chinese.
6. The round-3 receipts report `chinese_reader_pass = PASS` and `reader_effort_decision = PASS`, while the human-visible artifact still contains ordinary English reasoning scaffolding. Automated PASS is therefore a false positive for product style.

## Why exact fidelity is not forcing `estimand`

The current deterministic literal extractor protects formulas, code, paths, citations, numbers and formal-name-like tokens. A lowercase ordinary word such as `estimand` is not mechanically required by the exact-literal ledger.

So the recurring term is not an `inline-critical` fidelity requirement. Its survival comes from semantic/generation behavior and context anchoring, not the exact verifier.

## Source difficulty vs plugin defect vs test-harness defect

### Source difficulty

The original Deep Research report contains dense English research-process vocabulary and a memo/audit-like rhetorical skeleton. That creates a strong source-order and vocabulary anchor.

This is a real difficulty but not an excuse: the successful manual readability rewrite already proves the same scientific content can be expressed in natural Chinese without losing facts, formulas, methods, caveats or decision boundaries.

### Plugin/document contract

The active source is much better than earlier rounds: it now contains Reader Plan, structural rewrite authorization, reader-effort-not-compression, formula narrative, evidence classes and a terminal Chinese reader pass.

One remaining contract conflict should be audited if clean replay still fails: `scientific-rewrite` says ordinary reasoning language should become Chinese, but also says to preserve exact formal names including a broad category of `statistical term`. That category can be over-read as permission to preserve ordinary statistical English vocabulary that does not need exact English identity.

The seed library also remains mixed: many earlier and several manual-lesson seeds use `register = formal-technical`, while only later seeds use `reader-facing-scientific`. A clean replay should reveal whether this still biases the host toward compressed bilingual memo prose.

### Smoke/test harness

This is currently the strongest defect.

The round-3 smoke did not prove the actual isolated installed `writing-style` entrypoint. The executor session is both system maintainer and artifact writer, so the generation context is saturated with internal vocabulary and the exact words discussed during rejection/repair.

The smoke metadata itself can leak target vocabulary into generation. SMOKE-A's role contains `estimand`; B/C also carry internal English role labels.

That is not the normal user product experience.

## The current “logs” exist, but are not enough

Private stage artifacts exist: Document Map, Reader Plan, argument units, Meaning Cards, candidate units, self-audit, Chinese reader pass and final candidate.

Public Git records privacy-safe hashes/counts/receipts.

However the current receipt is mainly a dataflow/shape proof, not a semantic execution trace:

- per-unit semantic-self-audit stages and final assembly can point to the same aggregate `self_audit.json` file;
- the receipt records `host_codex_authored = true` but does not independently prove that the installed plugin invocation authored the content;
- `validate_chinese_reader_pass()` checks the host-authored PASS fields, hash binding and presence of English-classification lists, but does not enumerate the actual final candidate's English spans and prove that every surviving ordinary-reasoning span was repaired;
- the validator therefore trusts the same host that wrote the candidate to say the candidate has minimum reader inference burden.

This creates a self-certification loop: bad prose can be accompanied by a structurally valid `PASS` JSON.

## Next diagnostic before another plugin rewrite

Freeze the current implementation and run the same A/B/C through the actual isolated installed `writing-style` plugin replay with a clean, minimal user task.

The clean generation request must not include:

- 050 implementation/review history;
- previous smoke candidates;
- rejection analyses;
- project-specific style diagnoses;
- smoke role labels such as `checkpoint-estimand-and-next-decision`;
- expected wording or banned-word hints.

It should include only the exact frozen private source segment, the ordinary user rewrite request, and the installed plugin.

This is the first valid test of whether the current plugin itself still fails.

## If clean installed replay still fails

Then make one bounded production repair, not another broad rewrite:

1. Narrow exact-English preservation from broad “statistical term” wording to English identity that is genuinely needed for recognition/notation.
2. Make the terminal Chinese reader pass candidate-grounded:
   - deterministically enumerate Latin-script spans/occurrences without deciding their semantics;
   - require the host reader pass to classify every occurrence as exact identity, useful first-use recognition, or ordinary reasoning;
   - fail if any occurrence is unclassified;
   - after the pass, surviving `ordinary_reasoning` occurrences must be zero;
   - useful-recognition English must have a reader-facing Chinese explanation where applicable.
3. Record pre-pass and post-pass candidate hashes and private finding/repair counts so the reader pass proves it actually inspected/repaired the candidate rather than writing a PASS certificate.
4. Separate unit audit/global assembly evidence enough that the receipt can distinguish real stage outputs instead of mapping multiple conceptual stages to one aggregate file.
5. Change heavy-route example selection toward `reader-facing-scientific` where appropriate; do not add a vocabulary blacklist.

All semantic classification remains host-owned. Deterministic code may enumerate spans and validate coverage only; it must not decide whether a word should be translated.

## Product gate

Do not claim 050 fixed until both are true:

1. a clean actual installed-plugin replay produces the candidate; and
2. the human reader accepts A/B/C.

Schema/tests/receipt PASS remain process evidence only.
