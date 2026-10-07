# 059 Research Authoring C3 正常入口所有权收口 — Execution-Ready Critic Review v0.1

日期：2026-10-07  
角色：独立 Critic  
审查阶段：EXECUTION_READY_REVIEW_AFTER_C2_G1_FINAL_FAIL  
Task：`research-authoring--formal-production-authoring`

## 结论

```text
RESULT=REVISE
READY_FOR_CODEX=NO
BLOCKERS=RA-C3ER1
NEXT_HANDOFF=PLANNER
```

整体修复方向已经正确收敛，不再要求重开 Research Authoring 架构、shared replay、Bridge、G1-G4 taxonomy，也不要求现在修改 generic `pdf` Skill。

当前只剩一个执行包覆盖缺口：Planner 把 `profiles/codex-research-writing.json` 作为正式 production 修改面，并声称它会成为“authoring/source/package only，formal PDF 停在 handoff”的真实入口，但完整 development matrix 没有任何 runtime case 实际消费这个 profile。

这会让一个被本轮主动修改的正常入口在 C3 freeze 前没有真实入口证据。

## 已关闭的核心问题

### 1. C2 failure attribution

C2 G1 永久 FAIL保持不变。

直接 failure evidence证明 exact C2 Research Authoring 已消费，失败来自 renderer 在 Research Authoring handoff 前被提前选择，不是 candidate loading、replay isolation、cache/recovery 或环境问题。

### 2. 平台触发假设

当前 OpenAI 官方 Skills 文档直接支持 Planner 的关键机制判断：

- discovery 时模型先看到 Skill 的 name / description；
- description决定何时考虑该 Skill；
-完整 `SKILL.md` instructions 在匹配/选择后再读取；
- Skill metadata因此是真实的早期 discovery surface。

OpenAI 官方 metadata 指南也明确建议用正向/负向 prompt 集验证错误选择，并通过收窄 description减少 accidental activation。

当前没有官方证据支持一个可按“standalone Research Authoring vs research-main”动态切换 Skill物理可见性的硬条件 ACL。

因此选用：

```text
metadata discovery boundary
+ canonical Research Authoring owner/handoff
+ profile routing notes
+ real normal-entry runtime matrix
```

作为当前平台上最小可行机制，是合理的。

### 3. 修复层选择

批准方向：

```text
Research Authoring canonical boundary
+ render-chinese-math-pdf discovery boundary
+ existing profile routing coordination
```

不再接受 aggregate-only wording patch。

`latex-paper-authoring` 纳入范围也有直接 source依据：当前 metadata覆盖 author/organize/prepare LaTeX research papers，正文还要求 edits后 compile，因此如果不收窄，它可能在 manuscript+PDF 场景成为下一条提前 artifact-owner路径。纳入本轮不是无证据扩项。

### 4. generic pdf 暂不修改

当前 `skills/tools/documents-media/pdf/SKILL.md` metadata确实非常宽：

`If the user mentions a .pdf file or asks to produce one, use this skill.`

这是实际风险，但 C2 failure trace没有证明它已经抢 owner。

因此按照 Critic 原则，不因理论风险直接扩大 shared PDF source。允许本轮保持不改，但必须在真实 development runtime中作为 negative owner检查；一旦实际抢 owner，立即 STOP，不允许 Executor顺手扩 scope。

### 5. 版本与 Gate

`research-writing` 保持同一个未发布 0.3 candidate line合理；C2失败后修复同一 release batch不需要机械升 0.4。

`render-chinese-math-pdf` 当前已发布 standalone v0.2，本轮若实际改变 discovery/trigger behavior并完整验证，形成 v0.3 candidate符合现有 standalone Skill release历史和 README/version parity。

不新增 G5。DEV matrix是 C3 freeze 前风险匹配回归，不是最终 capability PASS；最终 G1-G4仍必须重新绑定同一 C3。

## RA-C3ER1 — 被修改的 codex-research-writing 正常入口缺少 runtime 验证

### requirement

Capability Gate / normal-entry规则要求：用户可见 routing/profile修改必须由真实 consumer证明，静态配置和字符串测试不能代替普通入口。

当前执行包主动修改：

`profiles/codex-research-writing.json`

并赋予它新的用户可见合同：

- authoring/source/package profile；
- formal research-document PDF停在 source/package + downstream handoff；
- global renderer discoverability不能把它升级成 `research-main`；
- integrated formal-PDF production改走 `research-main`。

既然这个 profile被修改并承担新的路由合同，它本身必须在 C3 freeze 前有实际 normal-entry证据。

### direct evidence

当前 `profiles/codex-research-writing.json`：

- 不安装 `render-chinese-math-pdf`；
- 但安装 broad generic `pdf` Skill；
- 当前 description仍直接提到 PDFs；
- 本轮 Proposal / Plan / Goal都要求修改其 description/routing notes。

现有 DEV-01 / DEV-03验证的是 standalone Marketplace `research-writing` candidate，不是 `codex-research-writing` profile。

DEV-04 / DEV-05验证的是 `research-main`。

DEV-06 / DEV-07是 render-only。

因此 DEV-01 至 DEV-10 没有一个 case证明新的 `codex-research-writing` routing notes真的进入 managed AGENTS并在普通请求里生效。

### causal risk

如果只做静态 profile测试，C3可能出现：

```text
codex-research-writing installed
+ generic pdf globally/profile-visible
+ manuscript/report asks for formal PDF
-> pdf/renderer-like owner selected
-> profile did not stop at handoff
```

这与刚刚导致 C2 final G1失败的“availability被误当成 owner admission”属于同一失败类别。

如果不在开发阶段验证这个被修改的入口，就仍可能把基础 routing bug留到后续真实使用或 final evidence才发现。

### minimum closure

不要改架构，不新增 Gate。

只需把现有 development matrix补一个真实 profile case，或把等价验证明确并入一个现有 case：

```text
codex-research-writing authoring-only profile
+ natural new/substantially revised manuscript + formal PDF request
+ generic pdf Skill保持真实可见
+ global renderer若机器本来可见也不得人为隐藏
```

必须证明：

```text
managed AGENTS profile routing notes actually consumed/present
Research Authoring core/paper read > 0
source/package produced
complete downstream handoff produced
generic pdf does not become new-document artifact owner
renderer does not execute
PDF mechanics commands = 0
final PDF artifact = 0
```

不要通过卸载/隐藏 generic pdf或renderer来过关。

这个 case继续属于 development matrix，不是 G5。

需要同步修改：

- Implementation Plan；
- Canonical Goal；
- Kickoff Draft；
- Capability Gate impact / package index仅在 locator或矩阵描述需要时同步。

Proposal主架构不需要重写，除非 Planner希望把该 profile case写入 Proposal的验证部分。

Owner：Planner。

## 非阻塞记录

### Maintenance tracking

Issue #99 当前 reader-facing状态仍停在早期 C0实现阶段，与当前 C2 final FAIL / C3 repair package不一致。

由于 reader-facing Issue更新按仓库政策必须先真实调用 Clear Writing，本 Critic线程不直接改写。

下一次具备合法 Clear Writing + GitHub Project/Issue mutation能力的维护动作应同步：

- 当前进度：C2 G1真实失败，正在审 C3 owner-routing修复；
- 当前执行锚点：本 C3 execution package / Critic review；
- 下一步：关闭 RA-C3ER1 后重新 execution-ready review；
- Project lifecycle继续 `DOING`，不得提前 DONE。

该 tracking copy drift不改变本轮唯一产品 blocker。

## 当前边界

```text
C2_G1_FAIL=PERMANENT
C3_NOT_CREATED=YES
PRODUCTION_MODIFICATION_AUTHORIZED=NO
FINAL_GATES_AUTHORIZED=NO
LIVE_PLUGIN_UPDATE_AUTHORIZED=NO
PAID_API_AUTHORIZED=NO
MAIN_MERGE_RELEASE_AUTHORIZED=NO
```
