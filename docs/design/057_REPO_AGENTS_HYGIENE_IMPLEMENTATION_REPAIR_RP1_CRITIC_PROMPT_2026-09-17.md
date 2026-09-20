# 057 Repo AGENTS Hygiene — RP1 Repair Prompt Short Critic Review

你是 AI Research Stack 的长期独立 Critic thread。

继续：

TASK_KEY = `057_repo_agents_hygiene`

当前阶段：bounded same-task implementation repair prompt short re-review。

本轮只复核一个 stable blocker：

`C057-RP1-H8-RAW-BYTE-NEWLINE-PRESERVATION`

不要重新设计 057，不修改任何目标 repo，不创建 branch/worktree，不启动 Executor，不 merge，不开始 056，不运行 paid API。

## Review object

`docs/operations/prompts/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_REPAIR_PROMPT_2026-09-17.md`

Revised repair-prompt commit:

`1507ad53a1e5a6a3bd30e16483c67d99acf852c0`

## Frozen authority

读取最新 AI_Skills main，并至少实际读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md` v0.2
- `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md` v0.2
- `docs/design/057_LITE_VERSIONING_DEFAULT_AMENDMENT_2026-09-17.md`
- current revised repair prompt

按需核对 failed Bridge candidate：

`a5c4fe61dc9ab0e228822e854ace5c7e50a4d967`

特别读取其 `ai_bridge_kit/cli.py::install_agents_snippet()`，确认原实现确实通过默认 text-mode read/write 和 `rstrip()` / `lstrip()` 编辑 existing root `AGENTS.md`。

## 只复核 C057-RP1

判断 revised repair prompt 是否明确并充分要求：

1. H8 的 `exact preservation` 是 **raw-byte-equivalent preservation**，不是 decoded-string 等价；
2. existing root 的 managed marker span 之外，原始 project-owned bytes 必须完全一致，包括 CRLF/CR/LF 表示和 irregular whitespace；
3. 禁止默认 text-mode universal-newline normalization 静默把 CRLF/CR 改成 LF；
4. 不硬编码实现方式，但允许 bytes-level splice 或任何 Bridge Python >=3.9 范围内可证明 raw-byte preservation 的等价实现；
5. 不新增 migration engine / alternate init path / state / schema / ledger / controller；
6. focused fixtures 至少覆盖：
   - CRLF existing root、无 managed block；
   - CRLF existing root、managed block 前后都有 project prose；
   - irregular blank lines / trailing whitespace；
   - mixed-newline fixture 若实现声称支持 arbitrary existing files；
7. fixtures 通过真实 normal init、`--force`、repeated/second init 验证；
8. verification 比较 raw bytes，不能只用 decoded string、`startswith(...)`、strip/normalize 后内容或关键词；
9. 该修订仍属于 H8，不新增 H10。

## Scope-drift check

同时只做一个机械检查：确认 Section 2–9 的既有 repair scope 没有被本轮意外实质改写。

不要重新审已经正确的：

- C057-I2 Bridge version closure / Lite versioning repair；
- C057-I3 Mica testing consolidation；
- C057-I4 Asteria map conversion；
- C057-I5 SeminarArc map conversion；
- Bobbio approved consolidation；
- Lucerna LIGHT_EDIT boundary；
- CUHK Date inspect-only；
- H1–H9；
- existing task branches；
- old E/M immutable history；
- E2 -> M2 closure；
- unreleased Bridge `0.8.3` candidate；
- 057 -> implementation review -> integration -> bounded 056 revalidation。

## Output

若 RP1 仍未关闭：

```text
RESULT = REVISE
TASK_KEY = 057_repo_agents_hygiene
REVIEW_OBJECT = docs/operations/prompts/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_REPAIR_PROMPT_2026-09-17.md
C057-RP1 = OPEN
REPAIR_PROMPT = REVISE
READY_FOR_CODEX_REPAIR = NO
NEXT_HANDOFF = PLANNER
```

只给 RP1 对应的稳定 blocker 和最小关闭条件，不扩大审查范围。

若 RP1 已关闭且其余 repair scope 未漂移：

先用正常中文简短解释为什么 raw-byte/newline 风险已经被真正覆盖，以及本轮没有重新设计 057。

然后给：

```text
RESULT = PASS
TASK_KEY = 057_repo_agents_hygiene
REVIEW_OBJECT = docs/operations/prompts/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_REPAIR_PROMPT_2026-09-17.md
C057-RP1 = CLOSED
REPAIR_PROMPT = PASS
READY_FOR_CODEX_REPAIR = YES
NEXT_HANDOFF = USER_SENDS_APPROVED_REPAIR_PROMPT
```

最后逐字返回你实际审过的 revised repair prompt：

```text
=== APPROVED 057 REPAIR PROMPT BEGIN ===
<verbatim current revised repair prompt>
=== APPROVED 057 REPAIR PROMPT END ===
```

不要 PASS 后再写一个不同的“改进版” prompt。
