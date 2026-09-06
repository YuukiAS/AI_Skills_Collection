# 050 Round 6 — local failure recovery

Status: task-local recovery note after the user stopped the Round-6 attempt.

## Verified remote state

The remote task branch still points to `741828ce0a6d8614ae9c0f3cc3feb9acb7643c2e` (`Record 050 round-6 reader-effort repair scope`). No Round-6 implementation or candidate commit is present on GitHub. `CURRENT.json` on the remote branch still records the Round-5 Final3 human gate with implementation `590502f5a78b2032f2238380aa68ea8287d50b9c`.

Therefore the failed Round-6 implementation, tests and `STYLE_SMOKE_A_B_C_ROUND6_REPAIR2.md` are local-only evidence and must be inspected on the execution host before any reset, checkout, clean, overwrite or new implementation attempt.

## Human decision

The user stopped the Round-6 attempt because the produced text remained poor and the implementation did not reach a passing local test state.

This is not authorization to discard the local failure. The failure is valuable diagnostic evidence.

## Recovery rule

Before generating any new A/B/C candidate, the next executor must first inspect the local Round-6 worktree and answer:

1. exactly which production files were changed;
2. exactly which tests fail and why;
3. whether the failed implementation added another mechanical proxy for semantic readability;
4. whether the candidate-only reader gate actually rejected the poor prose, and if not, why not;
5. whether QA/classification/protected-formula behavior leaked into reader-facing prose;
6. whether the writer prompt/skill contract itself is producing awkward formula/label-preserving prose even when the validator is stricter.

Do not continue with PDF rendering. Markdown is sufficient for this style task.

## Strong anti-degradation constraints

- Do not repair by adding phrase-specific banned words.
- Do not add another regex/readability-score proxy for abstraction burden.
- Do not weaken fidelity/exact/formula checks to make tests pass.
- Do not hand-edit A/B/C outputs.
- Do not regenerate A/B/C until the local test failures and the poor-prose acceptance path are explained.
- Do not reset or clean the local worktree until the local diff and failed test output are captured in a privacy-safe diagnostic.
- Do not mark any Round-6 artifact as product evidence while tests fail or the human-readable output is clearly poor.

## Likely decision point

If the local changes show that the executor tried to encode semantic reader effort as another deterministic gate, revert that direction and keep deterministic code limited to observable integrity/escape-path checks. The final abstraction-burden judgment must remain a real host-Codex semantic reader decision.

If the semantic reader decision itself still passes obviously awkward prose, the next repair should target the host writer/reader contract and invocation context rather than adding more mechanical rules.

## Required next state

The next run is diagnosis/recovery first, implementation second, replay last.

Do not start another open-ended style-rule round.