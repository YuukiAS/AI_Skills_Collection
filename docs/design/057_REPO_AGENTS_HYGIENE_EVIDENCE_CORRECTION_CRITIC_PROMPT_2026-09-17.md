# 057 Repo AGENTS Hygiene — Evidence-only Correction Critic Review

继续：

TASK_KEY = `057_repo_agents_hygiene`

当前阶段：independent implementation review -> evidence-only same-task correction review。

本轮只核对 provenance locator 修正；不要重新设计 057，不修改 target repo/Bridge candidate，不创建 branch/worktree，不 merge/release，不开始 056，不运行 paid API。

## Review target

AI_Skills reviewed branch:

`reviewed/057_repo_agents_hygiene`

New evidence commit `E3`:

`745281b70322b8508e43e59a5bdef70529749ea5`

New manifest closure commit `M3`:

`24051588d13f07e7f71e0edf5a723aca36754ed5`

Historical reviewed-but-revised tuple that must remain immutable:

- E2: `626147445166b2afc1648837830b283015bdc4cb`
- M2: `e10d18083d9b5b098045b6fb374dc241d0b11198`

Correct historical failed M locator:

`0a7198277dd9575010904f05b642deefffd00009`

Final repo candidates must remain exactly:

- Bridge: `e1d6b781ad7e56d567bed419001069baf439d0a5`
- Bobbio: `ab5dccb6b8b87c49671aa097233ce1bcc38be004`
- Lucerna: `41cd1297af6901531d3135593bc9806bffc38829`
- Mica: `e49416f874f633aedc7521734ee5b0f441aae970`
- Asteria: `0ce1d4daca1e410ce551570578dd563d4ef67e90`
- SeminarArc: `74caaa4ecec16f1bc90987979458d1a4e93f52be`
- CUHK Date: `711fab75f044b7ad31e5ff8610c076f902ccc949`

只复核四点：

1. `RESULT.md` 中 historical M 是否已从错误 SHA 修正为 `0a7198277dd9575010904f05b642deefffd00009`，且 historical E / current tuple / H1-H9 / EXECUTED_UNAUDITED boundary 没有其它漂移；
2. `E3` 是否只包含该 evidence locator 修正；
3. `M3` 是否只把 `AI_SKILLS_RESULT_COMMIT` 更新为 `E3`，保持所有 repo candidate/version/H1-H9 locator 不变，并继续不写自身 M3 SHA；
4. 是否没有 target repo、Bridge candidate、056、version、gate 或 workflow scope drift。

不要要求重跑 Bridge 363 tests、H7/H8 smoke 或产品 repo tests，因为 implementation candidate tuple 没有变化。

若通过：

```text
RESULT = PASS
TASK_KEY = 057_repo_agents_hygiene
REVIEW_TARGET = 24051588d13f07e7f71e0edf5a723aca36754ed5
EVIDENCE_COMMIT = 745281b70322b8508e43e59a5bdef70529749ea5
MANIFEST_COMMIT = 24051588d13f07e7f71e0edf5a723aca36754ed5
C057-I6-HISTORICAL-M-SHA-MISMATCH = CLOSED
READY_FOR_INTEGRATION = YES | NO
NEXT_HANDOFF = <按现有057流程>
```

若不通过，只给与这次 evidence correction 直接相关的 stable blocker；不要重开已经关闭的 I1-I5 / Bobbio / H1-H9。
