# 059 Research Authoring — ChatGPT → Codex scope correction (Critic note)

日期：2026-10-07  
角色：独立 Critic  
Task：`research-authoring--formal-production-authoring`

## 结论

当前 C3 recovery 方向跑偏了。不要继续修“Codex 收到原始科研写作请求时，Research Authoring 与 renderer 谁先抢入口”。

用户当前要收尾的正式能力是：

```text
ChatGPT Web
-> Research Authoring 负责科研文档语义、内容、source 与生产交接
-> Codex 只消费已形成的 source/handoff
-> Codex 负责 repo-grounded production / renderer / artifact QA
-> 返回最终 PDF/DOCX/LaTeX artifact
```

当前 pinned-runtime preflight 失败只证明：

```text
Codex 作为独立原始科研写作入口时，
同名 user/global renderer 仍可先于 project-local copy 被读取。
```

它没有证明 ChatGPT → Codex production chain 做不到。

因此：

```text
PROFILE_SCOPED_EXPLICIT_DELEGATE_RECOVERY=ABANDON
P2_NOT_CREATED=CORRECT
11_CASE_MATRIX_NOT_STARTED=CORRECT
FINAL_GATES_NOT_STARTED=CORRECT

04a17...=FAILED_PROVISIONAL_DEVELOPMENT_ATTEMPT
UNCOMMITTED_EXPLICIT_ONLY_INSTALLER_ATTEMPT=DO_NOT_PROMOTE
```

## 为什么之前的验收口径错了

原批准架构本身已经把两表面职责写得很清楚：

ChatGPT surface：
- 输出稳定 Markdown/LaTeX/结构化文本；
- 带 document/artifact intent；
- 带 table/figure/formula role；
- 带 venue/project authority；
- 输出短的 Codex production/render handoff；
- 不包含 renderer runtime。

Codex surface：
- repo-grounded production；
- canonical source read/write；
- bibliography/figures/tables；
- LaTeX/DOCX/Quarto；
- renderer；
- full artifact QA；
- durable repo delivery。

这说明正常产品链原本就是：

```text
Chat 负责“写对”
Codex 负责“做出来”
```

但后续 Goal/G1 又额外要求“Codex 也必须从原始自然语言科研写作请求重新做 Research Authoring owner selection”。

这个要求比 ChatGPT → Codex 正式生产链更强，而且不是当前用户收尾这个小版本所必需。

我们把这个额外能力错误地当成主链 blocker，导致连续几轮去解决 renderer 在 Codex 原始请求里抢 owner 的问题。

## 正确的产品边界

### 1. ChatGPT Web：自然入口

自然用户请求例如：

“把这份研究更新整理成给导师的正式 PDF。”

这里必须证明：
- Research Authoring 被实际消费；
- 科研内容、证据边界、结论强度、文档结构正确；
- 形成稳定 source；
- 形成完整 Codex production handoff；
- 不在 Chat 侧自己伪装 renderer production。

### 2. Codex：生产入口

Codex 正常输入不是再次收到原始“帮我写研究报告”请求。

Codex 应收到：
- stable source/package；
- audience/purpose；
- evidence authority；
- allowed edit scope；
- table/figure/formula roles；
- citation authority；
- venue/project authority；
- required production route；
- final artifact requirement；
- post-render scientific QA requirement。

Codex 在这里做：
- repo 文件落地；
- bibliography/figure/table/package integration；
- LaTeX/DOCX/Quarto；
- renderer；
- PDF/file QA；
- 最终 artifact。

不要求它重新证明“Research Authoring 和 renderer 谁先抢原始用户请求”。

### 3. Codex standalone Research Authoring

如果以后用户直接在 Codex 输入：

“把这些研究笔记写成正式论文 PDF。”

并要求 Codex 自己从零完成 Research Authoring owner routing，这是一项独立的增强能力。

当前 user/global renderer collision 可以记录为该能力的已知缺口，但不得继续阻塞当前 ChatGPT → Codex 正式生产版本。

## Gate correction required

Planner 必须最小修订当前 Goal / Gate / development plan：

### G1

G1 的 Research Authoring 自然入口主证据应来自 ChatGPT Web 正常入口。

Codex 不再要求从原始科研写作请求重新做同一自然入口竞争。

Codex 只需做与其真实 production role匹配的 near-miss/route safety：不能在 handoff 缺失时伪造科学语义，也不能改变 frozen scientific meaning。

### G4

G4 应成为真正的端到端主链：

```text
ChatGPT wrapper natural authoring request
-> stable source + complete handoff
-> Codex consumes that exact handoff/source
-> renderer/production
-> final artifact
-> post-render scientific QA
```

必须检查：
- Chat/Codex candidate identity一致；
- handoff没有丢科学语义；
- Codex没有重新发明或改变科学内容；
- final artifact真实可读；
- renderer/file QA完整；
- final scientific QA回看 artifact。

### Development matrix

删除/退休所有只为证明“Codex raw natural authoring request中 renderer不能抢 Research Authoring”而新增的 profile explicit-only recovery。

保留真正相关的回归：
- ChatGPT Research Authoring positive/near-miss；
- standalone Chat source + handoff；
- Codex handoff consumption；
- Codex render-only / existing-PDF / existing-LaTeX production helper不破坏既有能力；
- Chat -> Codex source/handoff fidelity；
- final artifact QA。

## 不要做

- 不要继续修改 `explicit_only_skills`；
- 不要继续尝试 project-local copy 压制 user/global同名 Skill；
- 不要修改 user/global Skill 安装状态来让测试通过；
- 不要再为 Codex raw authoring owner competition添加 wording/profile/installer机制；
- 不要把当前 preflight failure 改写成当前主产品失败；
- 不要启动 final G1-G4，直到 Planner完成最小 scope correction并经独立 Critic PASS。

## 当前状态

```text
CURRENT_C3_RECOVERY_PLAN=INVALID_FOR_USER_GOAL
PROFILE_SCOPED_EXPLICIT_DELEGATE_RECOVERY=RETIRED
P2=NOT_CREATED
C3_FINAL_CANDIDATE_COMMIT=NOT_ADMITTED
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER_SCOPE_CORRECTION
```
