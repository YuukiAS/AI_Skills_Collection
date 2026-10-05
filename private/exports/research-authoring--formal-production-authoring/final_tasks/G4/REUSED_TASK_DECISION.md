# G4 Reused Task Decision

G4 will reuse **G2**, not G3.

## Why

The user's normal ChatGPT workflow for Research Authoring is report authoring in Chat, followed by formal production in Codex. Reusing the already-reviewed G2 report minimizes extra scientific content evaluation and directly tests the intended cross-surface handoff.

G3 is reserved for the richer manuscript-package capability; using it again for G4 would add unnecessary submission complexity to the cross-surface integration Gate.

## Exact reused content

G4 may start only after G2 is fully PASS.

Semantic baseline:
- G2 Phase 2 final approved document;
- exact source/evidence identity already reviewed in G2.

G4 natural request:

> 把这份已经通过科学审核的研究更新整理成给导师的正式 PDF。先在 ChatGPT 侧保持科学内容不变，生成稳定的 Markdown/LaTeX source 和完整的 Codex production handoff；再由 Codex 用正式科研文档生产路线生成最终 PDF。不要把它改写成 PPT，也不要改变结论强度。

Chat stage is not asked to rediscover or re-evaluate the science. It must preserve G2-approved semantics and produce the approved handoff contract.

Codex stage must use exact Research Authoring final candidate `C` through `research-main`, then delegate PDF mechanics to the installed renderer. A renderer-only path without Research Authoring consumption is G4 FAIL.

No fourth scientific content task is introduced.
