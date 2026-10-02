# G1 normal entry evidence

Status: `PASS`

## Positive Trigger

Fresh Codex session:

`01a0fbc5-47c1-74a2-a857-b7cc31565a12`

Prompt shape:

- Did not name the skill.
- Asked to update ChatGPT Project instructions / Project settings.
- Included a live setting baseline.
- Requested adding an `AGENTS.md` locator.
- Included a hard budget of 700 characters.

Skill loading evidence:

- Session loaded `.agents/skills/core-codex-system-project-instructions-editor/SKILL.md`.
- Session loaded `.agents/skills/core-codex-system-project-instructions-editor/references/editor-contract.md`.

Runtime output:

```text
安全编辑：在现有设置末尾追加一句，不改写前三条语义。

可复制设置如下，216 字符，低于 700 字符预算：

This Project helps maintain a research codebase. Preserve user-approved decisions. Do not claim completion without current evidence. In implementation notes, point to AGENTS.md for detailed repository workflow rules.
```

G1 positive assessment:

- The skill triggered without being named.
- The answer treated Project instructions as a durable setting, not ordinary prose.
- The answer preserved existing setting semantics and made a bounded append.
- The answer respected the budget.

## Near Miss

Fresh Codex session:

`01a0fbc5-c809-75d1-9615-f08a79696223`

Prompt shape:

- Asked for ordinary Chinese polish.
- Did not ask to edit ChatGPT Project instructions, Custom Instructions, Project settings, AGENTS.md, or repository policy.

Runtime output:

```text
这个项目主要是帮助我们把各类工作做扎实，避免随意改动已经确定的内容，也避免在没有证据的情况下声称任务已经完成。
```

Near-miss assessment:

- The project-instructions-editor skill did not trigger.
- The response stayed in ordinary prose-polishing mode.

Conclusion: `G1=PASS`
