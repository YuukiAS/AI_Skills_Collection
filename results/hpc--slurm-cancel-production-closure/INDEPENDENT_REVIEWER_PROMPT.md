# Independent Reviewer prompt

Review the cross-repository implementation for task `hpc--slurm-cancel-production-closure`.

Do not redesign the approved architecture. Review the actual diffs and evidence bound to these exact commits:

- AI Skills product candidate: `b4815a35f708078184bff27b34f185fea6938cc3`
- DII consumer candidate: `e04f6a8da729c05a9e286b38c2c14cfd9ab13d31`
- CARE consumer candidate: `74d2948def67502070c06336866638f0869d9481`

Repositories and branches:

- `YuukiAS/AI_Skills_Collection`, `work/hpc--slurm-cancel-production-closure`
- `YuukiAS/Distributed_Imaging_Inference`, `work/hpc--slurm-cancel-production-closure`
- `YuukiAS/CARE_Challenge`, `work/hpc--slurm-cancel-production-closure`

Read the production Plan, canonical Goal, `results/hpc--slurm-cancel-production-closure/RESULT.md`, and `results/hpc--slurm-cancel-production-closure/HOST_POLICY_CANDIDATE.md` from the AI Skills branch.

Review requirements:

1. Confirm central `safe-cancel` is the only supported normal execution entry and that only exact current-run, live-revalidated, unprotected targets can reach internal `scancel`.
2. Confirm protected, old, non-current, incomplete, malformed, cross-cluster, scheduler-owner-mismatched, or policy-mismatched targets execute nothing.
3. Confirm the second snapshot and binding equality close target/state/policy changes before execution, and readback follows a successful execution.
4. Confirm no model/chat confirmation, Goal text, race opt-in, `auto_review`, Hook output, or receipt representation can execute protected cancellation.
5. Confirm DII binds the exact central product candidate and changes only standing race cancellation semantics.
6. Confirm all listed CARE authority and reachable consumer paths route through the central entry, retain on human/deny/unknown outcomes, and have no direct fallback.
7. Confirm CARE model/loss/split, budget, resource compatibility, lane order, takeover order, candidate gates, and atomic claims are unchanged.
8. Confirm the historical wave2 watcher is not routed from current authority or reachable scripts.
9. Review the Host Policy candidate: raw `scancel` and `/usr/bin/scancel` must become `forbidden` in Phase 4, only the exact installed central entry may remain usable, and existing read-only Slurm rules remain unchanged.
10. Treat G3 dangerous replay as explicitly incomplete: `BLOCKED_BY_ISOLATION`. Do not accept static tests as fake execution evidence, and do not request real Longleaf mutation as a substitute.
11. Confirm the claim remains normal-entry protection, not hard same-UID OS isolation.
12. Confirm repository `5.4.4` and `slurm-workflows 0.4` remain unchanged before production deployment/release closure.

Return exactly one verdict:

- `PASS`: the three exact candidates are approved for the already-authorized Phase 4 production deployment and read-only validation; or
- `REVISE`: list only concrete bounded blockers, with file/line evidence and the smallest required repair.

If PASS, include:

```text
RESULT = PASS
READY_FOR_PHASE_4 = YES
AI_SKILLS_CANDIDATE = b4815a35f708078184bff27b34f185fea6938cc3
DII_CANDIDATE = e04f6a8da729c05a9e286b38c2c14cfd9ab13d31
CARE_CANDIDATE = 74d2948def67502070c06336866638f0869d9481
G3_DANGEROUS_REPLAY = BLOCKED_BY_ISOLATION_ACCEPTED_AS_LIMITATION
REAL_SLURM_MUTATION = NO
```

Do not deploy, merge main, modify private Longleaf policy/Host Policy, bump versions, or release while reviewing.
