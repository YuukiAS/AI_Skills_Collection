# 056 Real Host Integration — Critic Prompt r1

你是 AI Research Stack 的长期独立 Critic thread。

继续 historical task：

`056_product_delivery_discipline`

人类可读名称：

交付工作流可靠性基线

当前只审：

`REAL_HOST_INTEGRATION_AUTHORIZATION_PACKAGE_R1`

Reviewed package commit：

`1f6d50a0df734534ed7215e5754017fc5ce24cdb`

不是重新设计 056。

## 必须读取

AI_Skills 最新 main：
- AGENTS.md
- docs/workflows/PLANNER_ROLE_CONTRACT.md
- docs/workflows/CRITIC_ROLE_CONTRACT.md
- docs/workflows/PLUGIN_CAPABILITY_GATE_POLICY.md

本轮 package（以 reviewed package commit 为审查对象）：
- docs/design/056_REAL_HOST_INTEGRATION_AUTHORIZATION_PLAN_2026-09-22.md
- docs/goals/056_REAL_HOST_INTEGRATION_GOAL.md
- docs/operations/prompts/056_REAL_HOST_INTEGRATION_KICKOFF.md
- docs/design/056_REAL_HOST_INTEGRATION_REVIEW_PACKAGE_2026-09-22.md

核对 Bridge exact candidate：
- repo: YuukiAS/GPT_Codex_AI_Bridge_Kit
- branch: reviewed/056_product_delivery_discipline
- candidate: `96a8ea1b58ebe6f9b7c5c46c43995666251911fe`
- version: 0.8.5

核对 AI identities：
- production candidate: `33c30bbe0dd528031a23d379905cd00d6b65bc1f`
- reviewed evidence HEAD: `b4adf85bafe29b20de2c2fbeb95668150642f5ae`

不要重开已经通过的 architecture/G1-G8/version/defer/C056-E1/E2/E3/C056-I1。

## 已验证真实 Host preflight

```text
HOSTNAME=c0824.ll.unc.edu
USER=aereinh
HOME=/overflow/htzhu/mingcheng_new
CODEX_HOME=/overflow/htzhu/mingcheng_new/.codex

approval_policy="on-request" configured
sandbox_mode="workspace-write" configured
approvals_reviewer="auto_review" configured
sandbox_workspace_write.network_access=true configured
features.memories=true configured
features.default_mode_request_user_input=true drifted
global Bridge Host AGENTS managed block=missing
narrative managed state=missing
ai-bridge-global.rules=drifted
AI worktree project config override=ABSENT
AI worktree project rules override=ABSENT
backup root=ABSENT
```

Current normal installed Bridge：

```text
executable=/overflow/htzhu/mingcheng_new/.local/bin/ai-bridge
root=/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit
HEAD=cb77b1cc5a1fce097a38066d2db452291e359852
version=0.8.2
```

Planner 没有把正常安装永久切到 reviewed candidate。

## 本 package 的关键策略

1. 从 exact reviewed worktree 直接运行 0.8.5 candidate；
2. 对 exact real CODEX_HOME 临时应用 candidate Host desired state；
3. 用 candidate source 做 status/validate；
4. fresh Default session 做 genuine HUMAN_ONLY live smoke；
5. fresh Default 做 agent-resolvable no-false-prompt smoke；
6. fresh Plan session确认 native blocking request_user_input 不回归；
7. 保存真实 evidence；
8. 因 0.8.5 尚未 merge/release 且 normal installed Bridge 仍是 0.8.2，smoke 后按本轮 backup manifest 安全恢复 pre-smoke Host state；
9. 不永久 rebind normal ai-bridge 到 reviewed worktree。

## 重点审查

A. 临时 apply + real smoke + restore 是否足以证明 frozen final real-host G1 gate；还是必须永久保持 candidate Host state才算 PASS？不要因为“更保险”要求永久绑定未发布 worktree。

B. official 0.8.5 host install 在当前 Host 上的 mutation envelope 是否准确：
- config.toml 预期只把 default_mode_request_user_input true -> false；
- AGENTS managed block当前缺失，因此正式 installer 会加入完整 0.8.5 managed block；
- rules 当前 drifted；
- tracked rules template 从 active 0.8.2 `cb77b1cc...` 到 candidate 0.8.5 `96a8ea1b...` 没有 source diff；
- package 禁止扩大 execpolicy allowlist；
- pre-mutation drift guard 是否足以保护 user customization。

C. backup/restoration 是否安全：
- 使用现有 timestamped backup manifest；
- 不新增产品级 restore command/state machine；
- 只恢复 manifest-listed paths；
- concurrent drift fail closed；
- post-restore hash/state必须回到 pre-state；
- 是否会误覆盖 smoke期间的新用户变化。

D. live G1 smoke 是否真正覆盖：
- Default genuine HUMAN_ONLY -> plain-text question；
- no native Default card；
- unanswered dependent execution不继续；
- no infer/poll/repeat/timeout-continuation；
- user reply `W2_RESUME_056_FINAL`；
- same Goal exact-once resume；
- post-action closure；
- agent-resolvable不误问；
- Plan-mode native request_user_input blocking behavior不回归。

E. 是否不必要地要求 Terra、paid API、product repo write、完整 suite rerun。
Planner判断都不需要。

F. 是否需要永久升级 current normal ai-bridge 0.8.2 -> reviewed 0.8.5。
Planner判断本阶段不应这样做：main/release尚未授权，永久指向 reviewed worktree会留下 pre-release runtime binding。

## 外部 reality

当前 OpenAI Codex Default-mode官方模板仍规定：若显式用户输入是继续安全执行的必要条件，应直接用一条 concise plain-text question，而不是 Default request_user_input；公开 upstream issue 仍报告 Default request_user_input会 auto-resolve/non-blocking，而 Plan mode是 blocking。

这些只支持 smoke设计，不替代真实 Host PASS。

## 输出

如果 REVISE：
- 只提出本 Host authorization/recovery/smoke object 的直接真实风险；
- stable blocker ID；
- requirement；
- direct evidence；
- causal risk；
- minimum closure；
- 自动附完整 COPY TO PLANNER prompt。

如果 PASS：
先自然中文解释：
- 用户实际授权后会修改哪个 exact Host/CODEX_HOME；
- 哪些文件会被 candidate installer碰到；
- backup如何产生；
- 为什么 normal installed 0.8.2 不永久升级；
- 为什么 smoke完成后恢复；
- Default模式与Plan模式最终用户体验分别是什么；
- PASS不授权哪些动作。

随后输出：

```text
APPROVED_PACKAGE_COMMIT=1f6d50a0df734534ed7215e5754017fc5ce24cdb
APPROVED_PLAN_PATH=docs/design/056_REAL_HOST_INTEGRATION_AUTHORIZATION_PLAN_2026-09-22.md
APPROVED_GOAL_PATH=docs/goals/056_REAL_HOST_INTEGRATION_GOAL.md
APPROVED_KICKOFF_PATH=docs/operations/prompts/056_REAL_HOST_INTEGRATION_KICKOFF.md
APPROVED_REVIEW_PACKAGE_PATH=docs/design/056_REAL_HOST_INTEGRATION_REVIEW_PACKAGE_2026-09-22.md
READY_FOR_CODEX=YES
NEXT_HANDOFF=CODEX
```

最后逐字输出 reviewed package commit 中的 Kickoff，不要自行重写。

PASS 不执行 056，也不授权 main merge/release/paid/product write。
