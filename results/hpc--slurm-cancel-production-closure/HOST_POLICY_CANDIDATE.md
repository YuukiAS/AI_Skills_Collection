# Longleaf Codex Host Policy candidate

Task: `hpc--slurm-cancel-production-closure`

Status: CANDIDATE_ONLY / NOT_DEPLOYED / REVIEW_REQUIRED

This candidate does not modify the active Host Policy in Phase 1-3.

## Required production decisions

```python
prefix_rule(pattern=["scancel"], decision="forbidden")
prefix_rule(pattern=["/usr/bin/scancel"], decision="forbidden")
```

The production policy must also permit only the exact installed central normal entry for agent-driven cancellation:

```text
<exact-installed-slurm-routing.py> safe-cancel <bounded arguments>
```

The exact installed path is intentionally not guessed before Phase 4 deployment. Phase 4 must resolve it from the reviewed installation, bind the rule to that path, load the actual policy, and prove by read-only evaluation that both raw forms resolve to `forbidden` while the central entry remains usable.

This is not an allow rule for arbitrary Python, shell, SSH, Slurm API, holder control, or another cancellation wrapper. Existing read-only Slurm inspection rules remain unchanged. No Hook is required for completion.
