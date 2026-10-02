# G4 complete task independent review

Date: 2026-10-02  
Reviewer result: `REVISE`

Reviewed identities:

```text
FINAL_CANDIDATE_COMMIT=227bb9dbc5e35d546822d27d7985d4d81c371d1c
EXECUTOR_EVIDENCE_HEAD=c5dafa5db724bae2533587fc64f4d68722b1c67d
```

Reviewed:

- final Skill source at `FINAL_CANDIDATE_COMMIT`;
- `G1_NORMAL_ENTRY.md`;
- `G2_CORE_SEMANTICS.md`;
- `G3_FIDELITY.md`;
- `G4_COMPLETE_TASK_PACKET.md`;
- `MANIFEST.md`;
- candidate/evidence immutability proof.

## Qualitative judgment

The visible G4 output is coherent and, against the source excerpts actually included in the packet, it shows several desired behaviors:

- keeps the package/API scope separate from teaching notebooks;
- keeps release history behind `CHANGELOG.md`;
- keeps course-policy detail behind a locator;
- preserves a private-data redistribution boundary;
- does not revive the disclosed nightly-build rule;
- stays within the stated 1200-character planning budget;
- presents a complete replacement rather than a clause-only fragment.

However, G4 cannot receive PASS because the packet does not contain the complete inputs that the independent Reviewer is required to compare against the output.

## R1 — G4 packet does not expose the full preservation-sensitive input

Requirement:

The approved implementation contract requires the independent Reviewer to see the complete representative input, baseline/source, and complete output. A preservation-sensitive full replacement especially requires a directly inspectable live baseline and the relevant decision history used to protect deletions/corrections.

Direct evidence:

`G4_COMPLETE_TASK_PACKET.md` includes:

- three source-fixture excerpts (`README.md`, `CHANGELOG.md`, `docs/course-policy.md`);
- a statement that a generated `AGENTS.md` also existed;
- the final runtime output.

It does not include the exact user request, the actual live Project-setting baseline, the relevant history/deletion input, the exact 1200-character budget input, or the contents/hash of the `AGENTS.md` source used by the run.

The runtime output itself claims it was based on “live setting、相关历史和四个 canonical sources”, but those missing inputs are not independently inspectable from the review packet.

Causal risk:

Without the baseline/history, the Reviewer cannot determine whether the complete replacement:

- preserved all unrelated live semantics;
- correctly treated the nightly-build rule as a previously removed rule rather than an invented test condition;
- omitted or weakened any mandatory/authorization/safety/evidence rule;
- correctly balanced the two scopes relative to the actual request;
- used the disclosed budget and source authority rather than an executor summary.

Therefore the central G4 claim—complete qualitative review of a preservation-sensitive final artifact—cannot be established.

Minimum closure:

Do not change the Skill candidate merely to close this finding if the original run inputs still exist.

Add an evidence-only G4 packet (or addendum) that contains or points to public-safe, directly inspectable versions of:

1. the exact natural user request used for the G4 run;
2. the full live Project-setting baseline;
3. the relevant targeted-history input, including the nightly-build deletion/rejection evidence;
4. the exact budget/headroom input;
5. all canonical-source contents used by the run, including the actual `AGENTS.md`, or stable hashes plus repository-safe copies;
6. the complete runtime output and session identity already recorded.

If those exact inputs were not preserved, rerun the G4 representative task from the same candidate commit using a frozen public-safe complete input packet and save all input/source/output material.

Then return for independent G4 review.

```text
G4=REVISE
IMPLEMENTATION_OVERALL=NOT_DECIDED_BY_G4_REVIEW_ALONE
BLOCKER=R1
```
