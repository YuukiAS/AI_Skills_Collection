# Clear Writing 下一次正式发布收口 — Critic Review

- Review round: `1`
- Date: `2026-09-15`
- Critic role: independent design review
- Reviewed proposal: `docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md`
- Proposal version: `v0.1`
- Reviewed proposal commit: `d32124586b2b860ee58ec621b2c31d1f33428735`
- Decision: `PASS`
- Scope of PASS: architecture / capability-gate / reviewer-rubric / recovery design only. This does **not** authorize implementation, paid API use, Executor start, release, merge, maturity promotion, or Bridge Kit changes.

## 1. 结论

本轮 `PASS`。

Planner 的核心判断值得进入下一步可执行 Plan 设计：Clear Writing 当前不需要推倒 051–054 建立的 heavy rewrite 主架构，也不应该继续靠禁词、正则、字段或更多局部 validator 修补。054 的实际失败更支持在现有 `Meaning Map -> Reader Plan -> REALIZE_MEANING -> assembly -> fidelity/audit` 上做有限职责重划：让 Reader Plan 明确承担 reader-facing disposition，让 realization 保持主体/时态/语气/认识状态，让 assembly 真正负责完整成稿，而 fidelity/audit 继续只做保真与处置一致性检查。

这个方向有清楚的因果链：054 F1/F2 说明“内容都在、局部审计都能过”仍不足以产生完成态读者文档；F3/F4 又说明 Reviewer 若把代码、路径、外部事实正确性与 source fidelity 混在一起，会制造假 blocker。Proposal 没有用新增 runtime、第二模型、state/ledger 或 Bridge Kit 来解决这些问题，而是修正生成职责和评审职责，复杂度总体合适。

## 2. 实际读取范围

本轮实际读取了最新 `main` 的：

- `AGENTS.md`
- `docs/workflows/CRITIC_ROLE_CONTRACT.md`
- `docs/workflows/PLANNER_ROLE_CONTRACT.md`
- `docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md`
- `docs/PLUGIN_MATURITY.md`
- `docs/workflows/PAID_EXTERNAL_REVIEW_POLICY.md`
- `docs/plugin-todos/writing-style.md`
- `skills/writing/core/scientific-rewrite/SKILL.md`
- `skills/writing/core/chinese-prose/SKILL.md`
- `skills/writing/core/writing-fidelity/SKILL.md`
- `docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md`

并直接读取了 051–054 的必要原始 evidence，包括：

- 051/052/053 `FINAL_REPORT.md`
- 053 known-regression、完整 Deep Research status、fresh-holdout status
- 054 Goal / PLAN / CURRENT / `FINAL_REPORT.md`
- 054 `FAILURE_ATTRIBUTION_AUDIT.md`
- 054 Terra `text_review/TEXT_REVIEW.json`

当前连接没有直接呈现 repo-local private Deep Research 全文/全部 render，因此本轮没有声称亲自逐页复审该私有成稿。设计阶段的关键判断仍有足够直接证据：054 Terra 给出了具体 F1–F4 成稿位置，failure-attribution audit 对照了 source/task/Reader Plan/semantic audit 并逐项归因；到最终候选放行阶段，Critic 仍必须实际拿到完整 source + artifact + render 才能做第二次阶段放行。

## 3. 独立外部研究

本轮没有沿用 Planner 的引用作为默认结论，而是独立核对了四个假设。

### 3.1 Source fidelity 必须与一般“事实正确”分开

Maynez et al. (ACL 2020), *On Faithfulness and Factuality in Abstractive Summarization*：大规模人工评估显示生成文本很容易出现相对输入文档的不忠实内容，常规表面指标不足以证明 faithfulness。

- https://aclanthology.org/2020.acl-main.173/

这支持 Proposal 的 A/source-fidelity 独立维度：Clear Writing 默认首先证明“有没有改变 source meaning”，而不是让 Reviewer 擅自把整个任务升级为 web fact-check。

### 3.2 Reader quality 不能由 fidelity 或单一机械指标推出

Fabbri et al. (TACL 2021), *SummEval: Re-evaluating Summarization Evaluation*：评价体系需要综合自动指标与人工判断，且 coherence / consistency / fluency / relevance 属于不同质量维度。

- https://aclanthology.org/2021.tacl-1.24/

这支持 Proposal 把 source fidelity 与 reader-facing coherence/relevance 分开，也支持在最终付费 reviewer 前先做完整 artifact 的独立定性阅读。

### 3.3 长上下文“能装下”不等于“可靠使用”

Liu et al. (TACL 2024), *Lost in the Middle: How Language Models Use Long Contexts*：相关信息处于长上下文中间位置时，模型表现可显著下降，即使模型名义上支持长上下文。

- https://aclanthology.org/2024.tacl-1.9/

这说明 G6 的完整长文能力是独立风险，不能由短段 fidelity、bundle PASS 或 token-window 足够来代替。

### 3.4 结构化技术对象不应该靠正则/字符外观判断

Pandoc 官方 filters 文档把输入解析成 AST，再在 reader 与 writer 之间做结构级变换；code/math/table/link 等对象有结构身份，而不是普通 prose 中“长得奇怪的字符”。

- https://pandoc.org/filters.html

这支持 Proposal 的原则：合法 code/path/table/math 是否保留要看角色和结构，而不是 blanket fence/path/英文统计。它并不构成引入 Pandoc runtime dependency 的理由；当前没有证据表明更换成外部 document framework 能替代 Clear Writing 的语义重写职责。

## 4. Product / Architecture assessment

### Product

产品边界清楚而且不过度扩张：目标是“已有中文/中文主导科研技术材料的 source-faithful reader-facing structural rewrite”，不是自动事实核查、Research Authoring、任意文档解析器或所有语言的通用重写器。这个边界与当前 `scientific-rewrite` / `chinese-prose` / `writing-fidelity` 分工一致。

### Architecture

`PARTIAL_REDESIGN` 合理。

1. **Meaning Map 保留**：需要一个 source-auditable 层证明“source 到底要求保留什么”。
2. **Reader Plan 升级而非另建系统**：reader disposition 解决的是 054 F1/F2 的真实语义问题——同一个 path/code/future-work 可能是必要科学内容，也可能是内部过程垃圾。Proposal 已明确若现有字段能表达就不要新增 runtime schema/state machine。
3. **REALIZE_MEANING 增加 modality preservation**：这是直接对应 054 “future work 被写成当前执行计划”风险，不是词表规则。
4. **assembly 承担 whole-document finish**：当前 source 的 assembly 主要允许排序、过渡、去重和结构对象放置；054 证明这还不足以保证整篇从“研究备忘录”转成完成态读者文档。将完整文档 voice/coherence 放到 assembly/final pass 是合理的职责补全。
5. **fidelity/audit 不升级成生成器**：只检查 proposition/evidence 和 disposition 是否一致，避免 verifier 反过来决定文风。

没有发现需要推翻当前架构、引入第二生成 runtime、付费分阶段生成、Bridge Kit 机制或大型外部框架的证据。

## 5. Complexity assessment

复杂度合适，没有明显过重。

Proposal 新增的是“已有阶段应该判断什么”，不是新的角色、服务、持久状态或 ledger。8 个 gate 数量虽然不小，但风险维度基本独立；合并成一个综合 PASS 反而会重新产生 053/054 那种“局部证据很多、真实能力不可定位”的问题。

也没有明显过简。特别是完整长文、fresh、real render、normal-entry production identity 和 independent qualitative review 都没有被 mechanical CI 替代。

## 6. Capability Gate Matrix assessment

整体 `PASS`。逐 gate 判断如下：

- **G1 ordinary routing / install / compatibility：有效。** 证明 normal entry 与 should-not-change，不允许 direct-skill helper 冒充 production route；明确要求 exact release candidate。
- **G2 source fidelity / attribution：有效。** 与 reader quality 独立，覆盖 claim/evidence/polarity/condition/caveat/citation 等真实保真风险。
- **G3 structured technical / reproducibility：有效。** formula/table/code/path/config/API/citation 共同属于“结构化技术对象按语义角色处置”的能力，但 Proposal 要求各类型有独立 case，避免一个 fence count 冒充整体 PASS。
- **G4 dirty source / markup cleanup：有效。** 与 G3 方向相反：G3 防误删必要结构，G4 防 wrapper 垃圾进入正文，因此不重复。
- **G5 reader relevance / Chinese quality / voice / script：有效且关键。** 直接覆盖 054 F1/F2 与真实中文可读性，不允许 banned-word / English-count 作为 PASS 代理。
- **G6 complete long-document structure / coherence / real render：有效且不可合并。** 053 的 clipped table / glyph render、054 的整篇 memo-like failure 都证明局部 PASS 不能替代完整 artifact；Proposal 还明确要求在最终付费 review 前已有 whole-artifact qualitative PASS。
- **G7 fresh generalization：有效。** candidate 必须先冻结；曝光后不得换题、补赢家或针对 holdout 调 production；candidate 改动后旧 fresh 不再是 unseen release proof。
- **G8 same-candidate production certification + independent qualitative verification：有效。** 它是 release certification 层，不是“再造一个质量 gate”；同时明确所有 release-critical evidence 绑定同一 final candidate，避免拼接多个版本的 PASS。

覆盖了用户要求检查的 source fidelity、自然中文、结构、math、table、code、citation、noisy source、reader relevance、long document、compatibility、fresh generalization、render 和 production routing。未发现 synthetic/test/receipt 代替用户能力的 gate，也没有发现明显重复 gate 需要删除。

## 7. Reviewer / Terra rubric assessment

`PASS`。

把 Reviewer 标准拆成：

- A：source fidelity；
- B：reader-facing quality；
- C：external factual truth；

是 054 证据直接要求的修正，而不是理论偏好。054 F3 证明 fenced Python code 不能因为“是 code”就 blanket block；F4 证明 source 自带的历史事实问题不能自动归类为 rewrite hallucination；F2 证明 path 必须区分 reproducibility/provenance 与 internal trace；F1 证明 source 的 future-work 科学内容可以保留，但不能继续以 executor/project-plan voice 出现在完成态成稿里。

Proposal 还要求 blocking finding 必须回指 frozen requirement、candidate 位置、必要时 source 位置、归因与最小关闭条件。这个约束能防止 Terra 临场发明新的 release 条件。

## 8. Gate order / recovery assessment

`PASS`。

顺序正确：已知修复与完整回归 -> 独立 whole-artifact qualitative review -> freeze candidate -> freeze fresh batch -> fresh execution -> failure attribution -> final independent/paid verification -> production entry/release closure。

这修正了 054 最关键的流程问题：最终 Terra 不再是第一位真正完整阅读全文的人，同时又没有把 fresh holdout 变成可反复调参 benchmark。

Recovery 也保持测试诚信：

- pre-freeze product defect 可以正常返修；
- fresh 真 product failure 后旧 item 永久降级为 regression；
- reviewer 越界保留原 review，以独立裁定追加说明，不伪造新模型 PASS；
- evaluation-source defect 不静默换题；
- infrastructure failure 只有在 candidate/source/rubric 不变时才允许恢复；
- paid final review 发现真 product defect 后进入新的 candidate certification，而不是把同一个 final candidate 修后继续叫 PASS。

没有新增 successor 自动链、无限 retry 或额外控制系统。

## 9. Release claim assessment

Proposal 的 release claim 在这些 gates 全部由同一 final candidate 直接通过后是可接受的，且应保持现在的边界：

> Clear Writing 可从普通安装入口，在已验证边界内正常用于中文/中文主导的 source-faithful 科研与技术重写。

它不能由本轮设计 PASS 直接升级成 `alpha/stable`；`docs/PLUGIN_MATURITY.md` 要求真实 production task + user acceptance 才能改变长期能力状态。Proposal 已明确这一点。

## 10. 非阻塞修正 / 执行 Plan 约束

这些不阻塞 v0.1 方案进入 execution-Plan 设计，但 Planner 在下一版 Plan 应吸收：

- **N1 — 历史表述精确化。** Proposal 对 052 写“没有完成完整 release”容易与 052 `FINAL_REPORT.md` 中的 release CI、production smoke、user ACCEPT 和 main integration 产生歧义。更准确的说法是：052 完成了其 bounded reader-facing closure，但并未证明跨任务长期成熟度。不要用“未 release”抹掉它已经完成的 task closure。
- **N2 — 053 俄文案例归因精确化。** 053 fresh H1 的正式 failure 是 PDF 中 Cyrillic glyph 缺失的真实 render failure；“俄文 alias 是否 reader-relevant”可以作为后续语义问题，但不应把 053 原始 gate failure 改写成 reader-relevance failure。Reader relevance 的强证据应主要引用 054 F1/F2 和后续真实反馈。
- **N3 — 不复制现有语义 ledger。** execution Plan 应把新的 reader disposition 明确实现为现有 Meaning Map / Reader Plan / `inline-critical | relocatable-trace | internal-workflow-trace` 语义的扩展或映射，并证明它被 REALIZE_MEANING / assembly 实际消费、改变 normal output；不要再建平行持久 ledger/schema。
- **N4 — Paid Terra 仍是独立授权项。** 本轮 PASS 不授权 paid review。若 execution Plan 仍包含 Terra，必须按 `PAID_EXTERNAL_REVIEW_POLICY.md` 单独给出必要性、call 上限、worst-case 预算、冻结时点和停止/恢复条件，并取得用户明确授权；也允许未来证明无付费 reviewer 仍能满足最终独立证据需求。

这些是执行约束和史实清理，不是当前设计 blocker。

## 11. Final decision

```text
REVIEWED_PROPOSAL_PATH=docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md
REVIEWED_PROPOSAL_COMMIT=d32124586b2b860ee58ec621b2c31d1f33428735
DECISION=PASS
ARCHITECTURE_ASSESSMENT=PASS — keep main architecture, partial semantic responsibility redesign is justified; no new runtime/state/Bridge mechanism needed
GATE_MATRIX_ASSESSMENT=PASS — G1–G8 cover distinct real capabilities and bind release-critical evidence to the same final candidate
REVIEW_RUBRIC_ASSESSMENT=PASS — source fidelity, reader-facing quality, and external factual truth are correctly separated; legitimate code/path/future-work cases are no longer blanket blockers
RECOVERY_DESIGN_ASSESSMENT=PASS — pre-freeze repair remains legal, fresh integrity is preserved, reviewer/source/environment failures are separately adjudicated, no automatic successor/retry chain
BLOCKERS=NONE
READY_FOR_EXECUTION_PLAN=YES
```
