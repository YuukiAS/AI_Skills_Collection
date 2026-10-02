# G2 core semantics evidence

Status: `PASS`

Fresh Codex session:

`01a0fbc6-1b43-7ec3-85e7-1459228f008b`

Skill loading evidence:

- Session loaded `.agents/skills/core-codex-system-project-instructions-editor/SKILL.md`.
- Session loaded `.agents/skills/core-codex-system-project-instructions-editor/references/editor-contract.md`.

## Runtime Cases

The session evaluated six mode/semantics cases.

### Case 1: Preservation-sensitive bounded edit

Runtime decision:

```text
模式：preservation-sensitive
决策：做 bounded edit，保留原文，只追加一条 locator/bridge。
候选：This Project maintains DataTool. Keep accepted user decisions. Evidence must come from current tests. Check AGENTS.md for the detailed build workflow before implementation.
```

Assessment: preserved existing setting and made a bounded addition.

### Case 2: Missing Live Baseline

Runtime decision:

```text
模式：preservation-sensitive
决策：不能安全压缩整份 Project setting，因为缺少 live setting baseline。
建议：安全降级输出只能是压缩原则或待插入条款；完整压缩需用户提供当前 live Project setting。
```

Assessment: correctly degraded instead of inventing a replacement.

### Case 3: Greenfield

Runtime decision:

```text
模式：greenfield
决策：可创建初始设置。
候选：This Project maintains a public data-cleaning library. Prefer clear, tested changes that preserve public API stability. Check repository instructions before implementation. Base claims on current tests and source files, and call out behavior-changing decisions explicitly.
```

Assessment: correctly created a new initial setting.

### Case 4: Explicit Reset

Runtime decision:

```text
模式：explicit reset
决策：用户明确允许丢弃旧设置，可从零替换。
候选：This Project maintains a public documentation site. Prioritize accurate, readable docs and preserve stable URLs unless a change is explicitly requested. Check repository guidance before editing. Verify examples, links, and build output when relevant, and clearly flag unverified claims.
```

Assessment: correctly allowed replacement only because reset authority was explicit.

### Case 5: Protected Absence

Runtime decision:

```text
模式：preservation-sensitive
决策：不重新引入 always publish nightly builds；它只在旧 candidate 中出现，live setting 缺席，当前请求也未重新采用。
候选：Use README.md as the primary locator for project overview, setup, and repository-specific guidance.
```

Assessment: preserved a removed rule by absence.

### Case 6: No-op

Runtime decision:

```text
模式：preservation-sensitive
决策：no-op。live setting 已经覆盖“repo workflow actions 前使用 AGENTS.md”，重复添加会制造冗余。
建议：Project setting 不变；如需更强执行，只能改写现有句子而不是新增重复规则。
```

Assessment: correctly avoided duplicate instruction accumulation.

Conclusion: `G2=PASS`
