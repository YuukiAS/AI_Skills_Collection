# PDF Save-as Delivery — Formal Release Isolation Critic Review R0

日期：2026-10-17  
角色：AI Research Stack 独立 Critic  
审查阶段：`FORMAL_RELEASE_ISOLATION_REVIEW_R0`

## Active Review Context

- target_repo: `YuukiAS/AI_Skills_Collection`
- target_plugin_or_domain: standalone `render-chinese-math-pdf`
- design_topic_or_task_key: `documents-media--pdf-save-as-delivery`
- source_branch_or_ref: `reviewed/documents-media--pdf-save-as-delivery`
- Proposal / Plan: `docs/design/pdf-artifact-delivery/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_ISOLATION_PROPOSAL_PLAN_V0_1_2026-10-17.md`
- Goal: `docs/goals/DOCUMENTS_MEDIA_PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_RECOVERY_GOAL_V0_1.md`
- Kickoff: `docs/operations/prompts/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_RECOVERY_KICKOFF_V0_1.md`
- frozen package commit: `5b71d8ccec98fe29111d9e1c59170a5f5f459a74`
- accepted PDF implementation: `5c92bf4f599d378ff68444b0fa85f5d56bbbd628`
- existing implementation review: `results/documents-media--pdf-save-as-delivery/REVIEW_2.md` = PASS
- formal release baseline: `06d135d8a6ee62cd41abb40fc5771fcef7f8db25` = repository `5.4.4`, PDF `0.2`
- latest main independently checked in this review: `db948045acc816323799cf86974bd92ce9bba22a`
- tracking Issue: #101

## 结论

`CRITIC_VERDICT=REVISE`

5.4.5 的 **release-line isolation 主方案是正确的**，不需要推翻，也不需要重新审 PDF 产品。版本选择、从正式 `release` 而不是当前 `main` 建候选、显式 allowlist、PDF product byte identity、全绿 isolated release validation、fast-forward-only producer、发布后再合回最新 main、以及 #101 最后关闭的顺序都成立。

唯一需要补的是一个与当前用户明确目标直接对应的最终发布 smoke：**正式 5.4.5 候选实际加载后，必须再有一次正常入口完成回复直接给出可打开/可另存的 PDF，而不是只证明 skill 文件装进去了。**

这不是重新跑 D1–D3，也不是 REVIEW_3；只是把已经通过的 D1 能力绑定到最终要发布的安装身份，并让用户在本轮收口时真实看到一次可另存文件。

## 已独立核实的通过项

### 1. 版本与隔离路线成立

当前 `origin/release` 仍是 `06d135d8...`，repository `5.4.4`，`render-chinese-math-pdf 0.2`。当前 main 为 `db948045...`，相对 release 已前进 243 commits，因此不能把整棵 main 当成 PDF release candidate。

`5.4.4 -> 5.4.5` 属于已有 standalone capability 的兼容改进，按仓库版本政策应为 PATCH；`render-chinese-math-pdf 0.2 -> 0.3` 也与已完成的 user-facing improvement batch 一致。中央 plugins 无需 bump。

Slurm 5.4.4 的真实历史已证明同样的 release isolation 拓扑可以工作：从 formal release line 构造只含已批准能力的 release target，fast-forward `release`，再把正式 release commit 整合回包含其他未发布工作的最新 main。PDF 方案没有发明第二套 producer。

### 2. PDF 产品 byte identity 正确

冻结 Plan 声明的 blob identity 已独立核对：

```text
SKILL.md
37109d885448a96d423bf664ebf9925714b57a0a

references/checklists.md
49dbbdc2cc2283cc2824ed6b32b49716b0a0a7c3

tests/test_render_chinese_math_pdf.py
ae5261e2b10258a7b94ea2a52cfb5b7523461614

render_scientific_pdf.py
0598dea9e034b6abd36336e5cf3ba455a81fa27a
```

renderer 在 formal 5.4.4 与 accepted implementation 上的 blob 完全相同。因此 release isolation 本身不应重开渲染器、数学、字体、模板或 D2/D3。

### 3. 生成层、CI、安装与 producer 边界合理

候选从 5.4.4 formal release source 构建、只允许 PDF/release metadata 差异，并要求：

- full unittest 全绿；
- canonical source/generated parity；
- exact-SHA GitHub CI PASS；
- fresh install / 5.4.4 -> 5.4.5 upgrade smoke；
- installed `SKILL.md` byte identity；
- publication 前重新读取 `origin/release`；
- fast-forward-only、non-force；
- remote ref exact readback；
- 发布后再合回 then-latest main。

Git 官方 `git-push` 文档确认：branch 的 fast-forward update 要求新 target 是旧 target 的 descendant；这种更新保留旧历史。该外部核对支持当前 producer safety，未发现需要更重机制的理由。

### 4. main reintegration 与维护关闭顺序合理

Proposal/Goal 明确要求先完成正式 5.4.5，再合回最新 main；只允许版本/README/CHANGELOG/registry/catalog/version assertions/#101 TODO 等共享 metadata 做有界 reconciliation。若出现 PDF production、PIE、Research Authoring、Presentations、shared runtime 或 generator 语义冲突则停止，而不是猜。

Issue #101 当前仍 OPEN，source backlink 为 `tracking: #101`。只有 release + main readback 后才关闭 Issue / Project DONE，这个生命周期顺序正确。

## Blocking finding

### PDF-REL-B1 — 缺少 final-release normal-entry 可另存文件 smoke

**对应要求**

用户当前明确要求：本 skill 收尾发布前，要实际看到一次测试，证明 PDF 做完后第一次完成回复给的是可以打开/下载/另存为本地的最终 PDF，而不是服务器路径。Issue #101 的 canonical problem 同样写明“每次 PDF 渲染成功后的最终回复都直接提供实际可获取、可另存为的完整成品文件或经验证可下载的链接”。

Capability Gate Policy / Critic contract 还要求 release gate 证明 normal entry 和真实用户输出，不能只用 install identity、tests、receipt 或文件存在替代。

**直接证据**

当前 Proposal/Goal 的 R4/G4 只要求：

- target/full tests；
- generated parity；
- GitHub CI；
- fresh install；
- 5.4.4 -> 5.4.5 upgrade；
- installed `SKILL.md` byte identity。

同时 Proposal §3D、R2 和 Goal 明确规定 product bytes 不变时“不重跑 D1/D2/D3”。

REVIEW_2 确实已经证明旧 accepted candidate 的 D1：第一次完成回复给出真实 PDF file entry，用户无需第二次追问。但当前 release package 没有把一次正常入口交付 smoke 绑定到最终 5.4.5 安装身份，也不会让用户在这次正式收口中看到一个新的可另存 PDF。

**因果风险**

如果 5.4.5 的安装/加载/正常入口在分发层发生问题，仅比较安装后的 `SKILL.md` bytes 可以证明文件一致，却不能直接证明最终正常完成回复仍执行了“交付文件而不是报路径”的用户行为。

更重要的是，这正是本 task 的原始 failure。若正式收口完全没有一次 final-distribution normal-entry delivery smoke，release 可以在用户最关心的行为没有被最终安装身份直接观察的情况下关闭 #101。

**最小关闭条件**

只增加 **一次** release delivery smoke，不重开 D1–D3，不创建 REVIEW_3：

1. 在 exact 5.4.5 / `render-chinese-math-pdf 0.3` release candidate 完成 fresh install/upgrade identity check 后，使用一个公开安全、最小的中英/数学输入，通过已安装 candidate 的正常 PDF production route 生成一份测试 PDF。
2. renderer/QA 必须通过，记录该 PDF 的 path/size/hash 仅用于 identity。
3. 本 release Goal 的最终用户可见完成回复必须**以这份测试 PDF 的真实 host file entry 开头**，使用户可以直接打开/下载/另存；服务器路径、hash、receipt、preview、文字说“文件在某处”都不能算 PASS。
4. 不允许用户再追问第二次“PDF 呢”才出现文件。
5. file entry 必须对应这次 QA 通过的同一 PDF。
6. 该 smoke 只验证最终安装身份 + delivery channel；D2/D3、renderer、数学、字体、模板不重跑。
7. 如果 candidate product blobs 仍与 REVIEW_2 exact-match，本 smoke 失败首先按 installation/normal-entry/delivery failure 处理；只有需要修改 product bytes 时才回 Planner/Critic 重开产品变更。
8. 在这个 smoke PASS 之前不得推进 `release` 或关闭 #101。

这是一条 release gate 补强，不是新的产品架构，也不要求用户额外点击确认；此前同一 Codex host-local file entry 已由用户确认可打开和另存。

## 非阻塞说明

- 不要求修改 Research Authoring、Presentations、PIE、Bridge Kit 或任何中央 plugin。
- 不要求重新生成正式 D1 fixture 或重新跑整套 D1–D3。
- 不要求新增 reviewer、第三轮 Reviewed Handoff review、付费调用或新的 upload service。
- package commit `5b71d8c...` 之后的 task branch 变化只增加了 Critic prompt / control next-action，没有改变冻结 Proposal/Goal/Kickoff 的实质内容，因此本 review object 仍然稳定。
- formal release isolation、5.4.5 PATCH、PDF 0.3、fast-forward-only producer、main reintegration、maintenance closure 其余部分均可保留原样。

## Critic final fields

```text
CRITIC_VERDICT=REVISE
BLOCKER=PDF-REL-B1_RELEASED_NORMAL_ENTRY_DELIVERY_SMOKE
PRODUCT_REVIEW_REOPENED=NO
D1_D2_D3_RERUN_REQUIRED=NO
REVIEW_3_REQUIRED=NO
RESEARCH_AUTHORING_CHANGE_REQUIRED=NO
PRESENTATIONS_CHANGE_REQUIRED=NO
BRIDGE_CHANGE_REQUIRED=NO
```

本轮只要求 Planner 将上述一次 release delivery smoke 同步加入 Proposal/Plan、Goal、Kickoff 和 Positive Completion。其余批准边界不要改。
