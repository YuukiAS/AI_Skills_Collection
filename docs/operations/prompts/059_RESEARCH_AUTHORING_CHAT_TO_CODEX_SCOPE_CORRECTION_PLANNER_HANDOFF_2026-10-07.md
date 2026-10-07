# 059 Research Authoring — Planner handoff for ChatGPT → Codex scope correction

你继续处理同一个 059 / Research Authoring，不开 successor。

用户不再接受继续调试 Codex raw natural authoring routing。先读取：

- `docs/design/059_RESEARCH_AUTHORING_CHAT_TO_CODEX_SCOPE_CORRECTION_CRITIC_NOTE_2026-10-07.md`
- 原批准架构中 ChatGPT/Codex surface 与 G4 定义；
- 当前 Goal / Plan / Gate Matrix；
- 最新 main 的 Planner/Critic/Capability Gate contracts。

目标只有一个：

把 059 恢复成用户真正要的正常工作流：

```text
ChatGPT Web
-> Research Authoring authoring/source/handoff
-> Codex production/render/artifact QA
```

不要再要求 Codex 从原始科研写作自然请求重新竞争 Research Authoring vs renderer owner。

必须：
1. 明确指出原 architecture 的 Chat/Codex职责与后来 G1/Goal 的 Codex-raw-natural-entry要求之间的范围漂移；
2. 最小修订 Goal / Plan / Gate Matrix / Kickoff；
3. 退休 profile-scoped explicit-only recovery及其未提交 implementation attempt；
4. G1 改为验证 ChatGPT Research Authoring自然入口及必要边界；
5. G4 验证 ChatGPT source/handoff -> Codex production -> final artifact的真实完整链；
6. Codex standalone raw Research Authoring作为未来独立增强，不阻塞当前 0.3；
7. 保留同一 final candidate、fresh evidence、should-not-change、README/Clear Writing、wrapper identity、最终 artifact review等原有效约束；
8. 不新增 G5，不改 Bridge/shared replay，不调用 Plugin Creator，不启动 final Gate。

提交一个小而完整的 scope-correction package，交独立 Critic复核。

不要实现 production。
不要启动 Codex Executor。
不要跑 final G1-G4。
