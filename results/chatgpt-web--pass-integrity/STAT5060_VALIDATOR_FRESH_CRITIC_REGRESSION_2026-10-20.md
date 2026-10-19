# STAT5060 validator fresh Critic regression — 2026-10-20

Task: `chatgpt-web--pass-integrity`  
Purpose: final real-world regression for Planner/Critic 1.7 and Capability Gate Policy 1.2  
Source: user-forwarded independent Critic review, preserved in the ChatGPT project conversation  
Reviewed governance: `YuukiAS/AI_Skills_Collection@89d740f03863f8ab1351a4865a1e78dc37f75998`  
Target repo current main observed by Critic: `YuukiAS/STAT5060-TA@c4885af5108316e90d40852502c432745eb84893`

## Result

`VERDICT=REVISE`

This is a successful governance regression even though the validator architecture was rejected for revision.

The Critic preserved the already-supported architecture decisions:

- Tutorial / HW1 / Project keep 4 / 5 / 5 validators;
- the 104 instructor Study Pack annotations remain explicitly excluded from student-deck release-history coverage;
- those 104 raw objects must not be recovered as a student-validator prerequisite and must not create student-slide requirements;
- model-backed judgments remain blocked when the approved evaluator runtime is unavailable.

It nevertheless found three substantive blockers that the prior frozen design had missed:

1. 213 / 46 / 32 rows having an owner did not prove an executable semantic chain from historical requirement to enforcing validator, exact rule, control, normal entry, candidate-bound evidence, receipt, and scoped verdict;
2. the two existing implementation handoffs were not safe GPT Work execution packages because branch identity, worktree, path authority, protected rubric/tests, recovery semantics, and a Tutorial branch AGENTS conflict were unresolved;
3. the historical three-page Project Guide control was actually recoverable from a known commit/path/hash, while anti-shortcut controls for two-page deletion/compression and the HW1 Q6 full-covariance positive control were not yet closed.

The review required three independent GPT Work prompts for Tutorial, HW1, and Project rather than letting one executor infer cross-branch architecture.

## Governance behavior demonstrated

- the Critic corrected stale prompt assumptions using current repository facts;
- zero-orphan mappings were not accepted as proof of semantic correctness;
- explicit user scope exclusions were preserved instead of reopened;
- known gaps were converted into bounded recovery/control tasks;
- missing runtime capability stayed blocked rather than receiving a fallback PASS;
- execution prompts were reviewed as part of the architecture, not treated as clerical handoff;
- the user-facing summary explained the practical decision before detailed findings;
- the next Planner work was explicit and did not authorize GPT Work prematurely.

This behavior is the expected standard for future substantial Critic reviews.
