# C3 G4 reused task decision

Candidate: `9e88d7eda1749c09bac0ed97562909a90810ccdb`

G4 reuses the G2 report task after G2 full PASS. It evaluates the corrected product chain:

```text
ChatGPT natural Research Authoring request
-> Research Authoring stable source
-> complete Codex production handoff
-> Codex consumes exact source/handoff
-> production/render/file QA
-> final artifact
-> post-render scientific QA
```

G4 does not test raw Codex authoring owner competition.

## Frozen natural request

> 把这份已经通过科学审核的研究更新整理成给导师的正式 PDF。先在 ChatGPT 侧保持科学内容不变，生成稳定的 Markdown/LaTeX source 和完整的 Codex production handoff；再由 Codex 用正式科研文档生产路线生成最终 PDF。不要把它改写成 PPT，也不要改变结论强度。

## Preconditions

- G2 Phase 1 PASS and Phase 2 PASS exist for exact C3 final evidence.
- The ChatGPT wrapper is exact C3 and skills-only.
- Before the first ChatGPT wrapper final evidence is collected, obtain one fresh bounded user authorization for the exact hash-bound C3 wrapper.
- If wrapper identity, scope, discoverability, and archive hash remain unchanged, the same bounded authorization covers both G1 and G4.
- Live Plugin mutation remains unauthorized in this pre-final packet and must not occur in this evidence-only repair.

## Failure conditions

- ChatGPT renders or claims to render the PDF itself.
- ChatGPT handoff is incomplete.
- Codex ignores exact source/handoff or changes scientific meaning.
- Codex bypasses Research Authoring and only renders.
- Final artifact is missing, unreadable, or lacks post-render scientific QA.
