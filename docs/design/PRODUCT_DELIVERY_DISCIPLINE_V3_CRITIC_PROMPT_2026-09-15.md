# Critic Prompt — Product Delivery Discipline v3

把下面正文原样发送给 AI Research Stack 的独立 Critic thread。该 prompt 只请求审查，不授权 implementation、paid API、repo-specific production changes 或 Bridge Kit 修改。

---

你是 AI Research Stack 的独立 Critic thread。

请审查 AI_Skills_Collection 当前这轮“跨项目产品开发交付纪律”Planner 提案。不要实现代码，不修改任何 repo，不创建 successor task，不调用 paid API，不代用户授权。

Repository:

`YuukiAS/AI_Skills_Collection`

先实际读取最新 `main`，并按当前项目合同强制读取：

- `AGENTS.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`

本轮审查对象：

- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V3_PROPOSAL_2026-09-15.md`

该 Proposal 最初提交于：

`e12abf6b9702a30923fcb43efe4bfc4ee8e21ae2`

随后只追加/修订了 evidence-side TODO，没有修改 Proposal 本体。请仍以审查时最新 `main` 的 Proposal 内容为准，并记录你实际审的 commit。

同时读取当前：

- `docs/plugin-todos/workflow-core.md`
- `docs/plugin-todos/web-development.md`
- `docs/plugin-todos/ai-skills-core.md`
- `docs/plugin-todos/scientific-visualization.md`
- `skills/core/codex-system/codex-workflow-protocol/SKILL.md`
- `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V2_2026-09-14.md`，仅用于比较 v3 是否真正改善，而不是作为权威答案

必要时只读核对这些真实 consumer/source：

- `YuukiAS/GPT_Codex_AI_Bridge_Kit` 当前 main 的 Lite / `templates/prompts/AGENT_RULES.md` / Host Policy user-input 配置
- `YuukiAS/Bobbio` 当前 active development branch 的 `AGENTS.md`、Figma/production UI source-of-truth
- `YuukiAS/Lucerna` 当前 main 的 `AGENTS.md`
- `YuukiAS/Mica-for-ChatGPT` 当前 main 的 `AGENTS.md`
- `YuukiAS/Asteria` 当前 main 的 `AGENTS.md`、`prompts/AGENT_RULES.md`、scientific graph visual rules

背景证据来自用户自己的 OpenAI 官方 Data Export。Planner 已在本地读取 private audit bundle，但没有把私有原始 conversation 上传到 GitHub。自动 audit 全量解析了 27 个 `conversations-*.json` shard、约 2,626 conversation、0 parse failure；但是自动产生的 173 个 incident 有明显分类噪声，因此 Proposal 明确只把全量 inventory 当 coverage，用人工复核的 curated thread 做机制判断。请检查这种证据使用方式是否合理，不要把“173 incidents”当真实频率。

重点用户痛点是：

- 需要用户操作时不问或静默等待；能自己完成的观察/测试反而反复要求用户做；
- 新功能/bug fix 没有抓住原故障的 targeted regression；很多测试 PASS，但真实路径仍坏；
- Mica 反复让用户跑 Atlas/live test，diagnostics/test cycle 逐渐替代真正产品目标；
- Bobbio 有 canonical Figma，却出现代码自行补设计、整屏组件语法不统一，用户被迫做逐屏 art direction；
- Lucerna 的 close/refresh 事故发生时，repo 已经有相近真实 interaction/test 规则，说明不能简单继续加文字；
- Asteria 明显 connector/card/math visual defect 能走到 late review，后来 repo 已经补了 developer visual self-QA 和 canonical visual system，需要验证实际消费，而不是继续堆同义规则。

请重点独立审查：

1. Proposal 把 15 条 raw rule 合成 8 个机制是否合理；有没有仍然重复、缺失或方向错误。
2. “Lite/AGENTS 只保留 6 条短 baseline；详细机制进入 Verified Workflow；视觉/设计进入 Frontend Design；科学图示进入 Scientific Visualization；项目不变量留 repo；Bridge Kit 只负责 template/user-input/runtime”这一职责划分是否正确。
3. 是否存在更简单方案，尤其要警惕把一次用户不满变成更重的状态机、更多审核或更多 token 消耗。
4. workflow-core 是否应该是主要 owner，还是其中某些机制已经被 Lite/Bridge Kit/现有 rules 完整覆盖，只需要消费/执行回归。
5. Frontend Design 当前 TODO 是否已经过度重复；哪些应合并成 production capability gates，哪些不应继续推广。
6. `scientific-visualization.md` 新增的 Asteria `status: NEW` 是否归属正确，还是应完全留给 Frontend Design/Asteria。
7. repo-specific 建议是否最小：
   - Bobbio：不再堆 user-prompt 规则，只补/整理 canonical design source consumption；
   - Lucerna：默认不新增 AGENTS，视为 existing-rule execution regression；
   - Mica：增加一次 live failure capture -> faithful fixture old-fail -> local repair -> one final human confirmation 的 repo-specific closure；
   - Asteria：已有 visual self-QA/visual system，不再加同义 AGENTS，只做 normal-entry replay。
8. Capability Gate Matrix 是否真正验证 normal entry、final candidate、should-not-change、human burden 和规则消费；是否还有 proxy PASS 漏洞。
9. Proposal 是否应该在执行前进一步核对某些 repo/Bridge Kit source；若需要，请给最小补证，不要无限扩大审查范围。
10. 是否同意：Critic PASS 前只允许 proposal/status:NEW evidence，不修改 production skill、Lite template、Bridge Kit 或 repo AGENTS。

本轮请做针对性网络检索，至少独立核查一个关键假设或现实替代；优先 OpenAI Codex 官方资料/成熟 agent engineering 实践，不要只复述 Planner 已引用的链接。

输出：

- `PASS` 或 `REVISE`
- 明确被审 Proposal 路径、版本与 commit
- 阻塞 finding 与非阻塞建议分开
- 每个阻塞说明：对应要求/证据、因果风险、最小关闭条件
- 明确指出 Proposal 是否过重、过简或 owner 划分错误
- 如果 PASS，只证明方案可以进入下一步 execution-plan/Goal authoring，不等于授权实现，也不等于这些 production changes 已完成

如果 `REVISE`，按当前 Critic contract 自动附一份可以直接发给长期 Planner thread 的完整 revision prompt。

如果 `PASS`，请明确说明下一步 Planner 应准备哪些 execution package；在没有审过 Canonical Goal + Kickoff Draft 前，不要给 `READY_FOR_CODEX=YES`。

---
