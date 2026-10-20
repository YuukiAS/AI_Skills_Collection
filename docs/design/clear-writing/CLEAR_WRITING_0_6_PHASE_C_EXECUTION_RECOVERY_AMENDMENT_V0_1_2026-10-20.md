# Clear Writing 0.6 Phase C 执行职责最小修订草案 v0.1

日期：2026-10-20  
状态：DRAFT_PENDING_REPAIRED_CANDIDATE_AND_CRITIC_REVIEW  
任务：`clear-writing--single-entry-artifact-finalization`  
原批准包：`d7b810d194ead881303aaca9c2e4f1d59a97c1f1`  
本草案不改变产品架构、G1-G6质量标准、GitHub-only external-finalization claim、模型或 attempt budget。

## 1. 为什么需要修订

原 Runbook 将 Phase C 的 Plugin Creator mutation 和所有 fresh ChatGPT Web gates 都写给“长期 Planner thread”。

真实执行证明：

- 长期 Planner 可以调用当前会话中的 Plugin Creator / GitHub connector；
- 但当前 Planner 模型没有创建新 ChatGPT conversation、切换模型和在新 conversation 中点选 Clear Writing 的 UI 操作；
- Plugin Creator live archive 还需要一个能把 signed archive 下载为实际本地文件的执行入口。

把这些动作要求在同一个 Planner surface 完成没有必要，也没有被 execution-ready PASS 真实证明。

## 2. 不变部分

完全保留：

- frozen single `clear-writing` Personal Plugin architecture；
- six canonical writing routes；
- Codex six-skill direct exposure；
- GitHub UTF-8 text external-finalization claim；
- G1-G6任务和质量标准；
- G3 Reader Guide；
- G6 fresh holdout；
- `GPT-5.6 Sol`；
- explicit Clear Writing selection；
- one-answer / infra-only retry policy；
- forward restore语义；
- 版本、Issue #13、README/changelog closure。

## 3. Phase C owner 拆分

### Phase C-A：archive / mutation owner

责任：

- live P0 account readback；
- 保存真实 current 0.5 archive；
- 重建 frozen 0.6 candidate；
- prepare and verify forward restore；
- update same Personal Plugin identity；
- G1-A Plugin Creator full readback；
- terminal failure 时执行 forward restore。

这个 owner 必须同时具备：

1. Plugin Creator 当前账户写权限；
2. 把 Plugin Creator archive 和 candidate archive materialize 为本地/host-uploadable bytes 的能力；
3. 运行批准 builder 的能力。

在这些能力通过无副作用 preflight 前不得 mutation。

### Phase C-B：fresh Web gate sessions

G1-B、G2、G3 继续使用真正 fresh ChatGPT Web conversation。

对每个冻结 Web task：

- model = `GPT-5.6 Sol`；
- user/UI 显式选择当前 Clear Writing；
- exact frozen prompt；
- product failure 不 reroll；
- 不使用当前 Planner chat、本地 replay、Codex helper替代。

当前平台若没有让 Planner自动创建这些 fresh chats 的动作，则“新建聊天 + 选择模型 + 选择 Clear Writing + 发送 Planner 已准备好的 exact prompt”属于 user-only UI action。

Planner不得要求用户寻找路径、生成 prompt、判断 Gate 或设计证据。

## 4. 跨入口保持同一候选的办法

Phase C-A 和 Phase C-B 不需要是同一个 surface，但必须绑定同一：

- `FINAL_CANDIDATE.json` source commit；
- wrapper archive SHA-256；
- installed Personal Plugin current release ID；
- version `0.6.0`；
- Gate rule version；
- exact prompt hash/source identity。

任何 candidate-defining source 或 live release identity drift，按原 Runbook失效并停止。

## 5. 失败恢复

恢复 owner 始终是执行 live 0.6 mutation 的 Phase C-A owner。

Web Gate 若出现 terminal PRODUCT FAIL：

1. 后续 Gate停止；
2. Gate结果回到同一 task evidence；
3. Phase C-A owner使用已准备的 0.6.1 forward restore；
4. central writing-style 0.6不发布。

这不改变原恢复语义，只明确实际 owner。

## 6. 审查边界

builder 的 ZIP/tar.gz输入兼容属于普通实现 bug，由同一 Codex task修复，不需要为代码 bug单独重开架构审查。

本文件改变的是 Phase C execution responsibility / user handoff，因此必须在新的 repaired candidate identity形成后，由原独立 Critic做最小复核。

Critic只需要判断：

- 两个合法执行入口是否保持同一 candidate/release/Gate identity；
- user-only Web UI动作是否已经缩到最小；
- restore owner是否明确且能在 terminal failure后执行；
- 是否有任何 G1-G6定义被偷偷降低。

Critic通过前不得 live mutation。
