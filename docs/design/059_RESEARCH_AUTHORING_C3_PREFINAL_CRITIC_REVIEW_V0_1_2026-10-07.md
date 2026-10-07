# 059 Research Authoring C3 pre-final Critic review v0.1

日期：2026-10-07  
角色：独立 Critic  
Task：`research-authoring--formal-production-authoring`  
Candidate：`9e88d7eda1749c09bac0ed97562909a90810ccdb`  
Evidence HEAD reviewed：`ac1f518ed816166b17dccc2af2fdc2778b600432`

## 结论

```text
RESULT=REVISE
C3_PRODUCT_CANDIDATE=ACCEPTED_FOR_PREFINAL_REVIEW
C3_FINAL_CANDIDATE_COMMIT=9e88d7eda1749c09bac0ed97562909a90810ccdb
PRODUCT_SOURCE_DRIFT=NO

DETERMINISTIC_VALIDATION=PASS
README_CLEAR_WRITING_EVIDENCE=PASS
CODEX_HANDOFF_CONSUMER_SMOKE=PASS
PRODUCTION_HELPER_REGRESSION=PASS
C3_OFFLINE_WRAPPER_READY=YES

PREFINAL_PACKET=REVISE
FINAL_GATES_AUTHORIZED=NO
BLOCKERS=RA-C3PF1
NEXT_HANDOFF=PLANNER
```

产品候选本身没有发现新的实现问题。当前只剩一个 final packet 一致性 blocker；不需要修改 Research Authoring production source，也不需要再做任何 Codex raw-authoring owner competition。

## 已通过部分

### Candidate identity / no drift

从失败 provisional attempt `04a17a904ce522cb4a517cb33f22e062f2bcbc09` 到 C3 candidate `9e88d7eda1749c09bac0ed97562909a90810ccdb`：

- Research Authoring / renderer / profile / Marketplace production source无语义变化；
- candidate新增的是 README Clear Writing最小读者层修正、generated timestamp parity与 pre-final evidence；
- `explicit_only_skills` 失败实现没有进入 candidate。

因此不追认 04a17，但可接受 9e88d7ed 作为新的 exact candidate identity。

### README Clear Writing

已验证真实 installed `writing-style:chinese-prose` 被读取，README从 hash `55cf41fe...` 经最小中文可读性修正到 `3dbef5f0...`，版本、slug与 renderer边界未改变。

### Deterministic validation

precommit evidence记录完整 canonical validation全部 PASS。第一次 full unittest因 sandbox写边界失败，随后在已授权 exact worktree写边界内同一命令 PASS；该失败归因为环境权限而不是产品失败，处理合理。

### Corrected product-chain smoke

Codex smoke实际读取 stable source + production handoff，并产生 source、PDF与 post-render scientific QA。数值 `0.781` / `0.806`、非结论性解释、three-seed follow-up与 boundary-touching error review均保持。

该 smoke符合当前真实职责：
ChatGPT/Research Authoring先稳定科学内容，Codex消费 handoff后做生产；不再测试 Codex raw natural authoring owner competition。

### Wrapper

Offline wrapper绑定 exact candidate `9e88d7ed...`：

- PRIVATE / USER；
- skills-only；
- Research Authoring payload与 Clear Writing support来自同一 candidate；
- renderer runtime / MCP / connector / database / watcher / state machine均排除；
- archive SHA256 = `4783abc0b95c1a0775b9d801825d822819fa5426a8a38a418ad16759a028b388`。

当前 OpenAI官方文档仍支持 skills-only plugin，并明确 skills可作为 ChatGPT/Codex共享的工作流层；本 packet不再依赖 project-local Skill覆盖 user/global Skill的失败假设。

### Frozen G2/G3 sources

独立读取并核对了 G2 DII exact input blobs与 G3 MoSAIC authority/source blobs；当前 packet记录的 blob SHA与真实冻结 refs一致。

## RA-C3PF1 — final packet还存在三处小的一致性缺口

### requirement

Pre-final packet必须在 final evidence开始前完整冻结：

- corrected Gate Matrix要求的 case coverage；
- exact final candidate identity；
- ChatGPT wrapper live mutation/authorization边界。

这些都必须在看到 final output前固定，避免最终 Gate过程中临时补 case、换 candidate或重复索权。

### direct evidence

1. Scope-corrected Gate Matrix明确要求 G1 near-miss继续覆盖：
   - citation verification；
   - paper lookup；
   - sentence polish；
   - **README / email**；
   - PPT / Beamer；
   - render-only；
   - ordinary research Q&A。

   但冻结的 `G1/G1_CASE_BANK.md` 只列了 citation、lookup、sentence polish、render-only、PPT/Beamer、ordinary Q&A，**遗漏 README / email**。

2. `G2/G2_RUBRIC.md` 仍明确写：

   ```text
   Candidate before pre-final promotion:
   C0 1c37c0715aca0096606f24e56192b7857e72bbd6
   ```

   当前 packet manifest与所有新 final evidence应绑定的 candidate已经是：

   ```text
   9e88d7eda1749c09bac0ed97562909a90810ccdb
   ```

   这是 stale candidate locator，不能留进 final rubric。

3. G1 rubric要求“exact C3 wrapper payload is active”；但 G4 reused-task文件把新的 live Plugin授权写成“at the G4 boundary”。如果 G1在G4之前执行，这个授权点太晚。当前 packet没有明确一次授权如何覆盖 G1/G4同一个 exact wrapper。

### causal risk

如果现在直接开始 final Gates：

- G1可能少测一个已经冻结要求的 near-miss family；
- G2 Reviewer可能面对两个不同 candidate locator，破坏 same-final-candidate证据；
- G1可能首次需要 live wrapper时才发现授权合同写在G4之后，造成不必要的停机/重复用户往返。

这三项都是 packet问题，不是产品问题。

### minimum closure

不改 candidate `9e88d7ed...`，不改 production source，不新增 Gate，不重跑 development。

只修改 evidence/pre-final packet：

1. G1 case bank补回冻结合同已有的 README / email near-miss，使用自然请求，不改变 G1 rubric语义；
2. G2 rubric把 stale C0 candidate locator机械重绑到 exact C3 `9e88d7ed...`；rubric内容、G2 task、Phase1 manifest、Phase2 delta全部保持不变；
3. 明确 live wrapper授权为：
   - 在**第一次需要 ChatGPT wrapper final evidence之前**取得一次新的 bounded user authorization；
   - exact wrapper固定为当前 hash-bound C3 wrapper；
   - 同一次授权可覆盖 G1与G4，除非 wrapper identity/scope发生变化；
   - 当前仍不执行 Plugin Creator/live update；
4. 重新生成 packet hash/manifest一致性文件；
5. `git diff --check`，提交并发布 evidence-only repair；
6. 不启动 final G1-G4，返回 Critic。

Owner：Planner / packet-preparation Executor。

## 非阻塞项

未跟踪旧运行缓存目录不需要清理，只要不进入 candidate/evidence identity且不影响 final runtime。

## 当前边界

```text
C3_FINAL_CANDIDATE_COMMIT=9e88d7eda1749c09bac0ed97562909a90810ccdb
CANDIDATE_CHANGE_REQUIRED=NO
PREFINAL_PACKET_CHANGE_REQUIRED=YES
FINAL_GATES_NOT_STARTED=YES
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO
```
