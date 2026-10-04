# Critic Prompt — Project Instructions Editor Final Delivery Closure v0.2

你现在负责复核 project-instructions-editor standalone Skill 最终交付收口 v0.2。

这不是重新设计产品，也不是重新审已经 PASS 的 C4 implementation、G1–G4、私人 ChatGPT wrapper、icon、Server+VPS acceptance、用户负担、README 本地保护或 C4 immutability。

上一轮唯一 blocker 是 FD1。

## Active Review Context

target_repo:
YuukiAS/AI_Skills_Collection

target_plugin_or_domain:
standalone Skill / project-instructions-editor

design_topic_or_task_key:
project-instructions-editor--standalone-skill-implementation

source_branch_or_ref:
main

execution branch:
work/project-instructions-editor--standalone-skill-implementation

execution worktree:
../AI_Skills_Collection-project-instructions-editor--standalone-skill-implementation

review_stage:
final ChatGPT distribution
+ Server+VPS real user acceptance
+ integration/release closure
+ FD1 formal-release-cleanliness repair

accepted implementation:

FINAL_CANDIDATE_COMMIT=
266334ca807640b08605faddbdded7d5a6591aa1

EVIDENCE_HEAD=
34428d3db409ffc97aea36cc3776c14f33b94289

IMPLEMENTATION_OVERALL=PASS
G1=PASS
G2=PASS
G3=PASS
G4=PASS

prior final-delivery package v0.1:

Plan:
docs/design/project-instructions-editor/
PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_PLAN_V0_1_2026-10-04.md

Goal:
docs/goals/
PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_GOAL_V0_1.md

Kickoff:
docs/operations/prompts/
PROJECT_INSTRUCTIONS_EDITOR_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_1.md

prior package commit:
7bbe8d5982b9cd6abdca503ca6b12094976b92c6

prior Critic review:
docs/design/project-instructions-editor/
PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_CRITIC_REVIEW_V0_1_2026-10-04.md

prior Critic review commit:
2dd26aa17aa695a80d6eacc39afe4de4857f147a

stable blocker:
FD1

Planner disposition:
FD1=ACCEPT

v0.2 package:

Plan:
docs/design/project-instructions-editor/
PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_PLAN_V0_2_2026-10-04.md

Goal:
docs/goals/
PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_GOAL_V0_2.md

Kickoff:
docs/operations/prompts/
PROJECT_INSTRUCTIONS_EDITOR_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_2.md

PACKAGE_COMMIT:
0278c53fbb1674081a7085ee1831dc2856c9c179

tracking:
Issue #93

READY_FOR_RELEASE=NO

如果 package commit 后 main 继续因为并行开发推进，读取最新真实 main/release，不回退到旧 SHA。只要 v0.2 三个 package 文件本身未被改写，就按当前真实 release/main 状态复核 FD1。

==================================================
一、必须读取
==================================================

读取 latest main：

AGENTS.md

docs/workflows/
PLUGIN_VERSIONING_AND_CHANGELOGS.md

skills/core/codex-system/
ai-skills-repository-maintainer/SKILL.md

skills/core/codex-system/
machine-update-orchestrator/references/
formal-release-and-update-impact.md

读取：

origin/main
origin/release
VERSION
CHANGELOG.md
scripts/codex_marketplace_config.json

实际比较：

origin/release..origin/main

读取 prior Critic review v0.1。

主要审：

PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_PLAN_V0_2_2026-10-04.md

PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_GOAL_V0_2.md

PROJECT_INSTRUCTIONS_EDITOR_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_2.md

不要重审已经 PASS 的 wrapper / icon / Server+VPS / user burden / local README / C4 / G1–G4，除非 v0.2 意外破坏它们。

==================================================
二、先核对当前 formal release 状态
==================================================

Planner 修 FD1 时观察到：

origin/release =
03b0281b1f7fbd29621faa6298cd1db2578a0ffc

origin/main =
2dd26aa17aa695a80d6eacc39afe4de4857f147a

release VERSION =
5.4.3

main VERSION =
5.4.3

origin/release..origin/main
当时仍包含 unrelated Presentations
production/generated source。

这些 SHA 只是观察值，不是冻结要求。

因为用户正在大量并行开发插件，
请使用你审查时的最新真实：

origin/release
origin/main
release..main

不要因为 main 继续推进就机械 REVISE。

==================================================
三、FD1 的修复原则
==================================================

v0.2 不再使用：

“只要 main VERSION 还是 5.4.x，
并且没有直接 PIE overlap，
就可以发布”

这种过宽规则。

现在 authority 明确为：

origin/release
= formal release baseline

main VERSION
!= release cleanliness proof

正式发布前必须运行：

FORMAL_RELEASE_CLEANLINESS_PREFLIGHT

==================================================
四、检查 A / B / C 分类
==================================================

v0.2 要求：

先 resolve exact origin/release；
再 resolve exact origin/main；
比较 origin/release..origin/main。

分类：

A. FORMAL_RELEASE_BASELINE

当前 origin/release 已经正式包含的历史，
属于正式 baseline。

如果其他并行 task
已经完成自己的 formal release，
并把 origin/release 推进到新的兼容 5.4.x，
重新运行 preflight 后，
该正式内容直接成为新的 baseline。

B. NON_PRODUCTION_DRIFT

release 之后 main 上只有：

- docs；
- TODO；
- planning；
- review；
- evidence；

并且不改变：

- production source；
- generated runtime identity；
- plugin/profile exposure；
- routing；
- runtime behavior；
- install/distribution payload；
- installed user-visible behavior。

B 不阻止 PIE release。

C. UNRELEASED_PRODUCTION_DRIFT

release 之后 main 上存在
尚未进入 formal release 的：

- production source；
- generated plugin/Skill payload；
- profile；
- routing；
- runtime behavior；
- distribution/install behavior；
- 其他用户可见 release content。

C 不能因为：

- VERSION 还是 5.4.x；
- 与 PIE source 不重叠；
- 已经 commit 到 main；
- 属于别的 task；

就视为安全。

请判断这个分类是否足以关闭 FD1，
并且没有重新设计 release system。

==================================================
五、C 类 drift 的行为
==================================================

如果存在 C：

WAITING_FOR_FORMAL_RELEASE_BASELINE=YES
READY_FOR_RELEASE=NO

只停止：

final integration/release mutation

不作：

- PIE product failure；
- C4 invalidation；
- G1–G4 invalidation；
- wrapper invalidation；
- Server+VPS acceptance invalidation。

禁止：

- revert 别人的 task；
- reset/restore/stash 丢别人的改动；
- ad-hoc cherry-pick 拼 release；
- 静默把别人 production behavior
  算进 PIE 5.5.0；
- force/rebase；
- 绕过 formal release producer。

默认恢复：

等待 unrelated production work
走它自己的正式 closure，
origin/release 前进后，
重新跑同一个 cleanliness preflight。

请重点判断：
这是否既 fail closed，
又不会因为用户并行开发很多插件
导致每次 main SHA 变化都回 Planner。

==================================================
六、兼容 5.4.x 正式 baseline 漂移
==================================================

v0.2 保留原来合理的部分：

如果新的正式 origin/release
仍然属于兼容 5.4.x，
PIE 没有被其他 task 集成，
没有直接 PIE source/distribution conflict，
version policy 未改变：

PIE target 仍然是：

Repository bump decision = MINOR
target = 5.5.0

project-instructions-editor =
standalone 0.1

central plugins =
NO_BUMP for this task

无需仅因为：

5.4.3 -> 5.4.4
或
5.4.5

这样的正式 patch release
重新做 Planner/Critic。

请确认这个规则不再把
“main 上未发布 production drift”
误当作“formal patch drift”。

==================================================
七、双重 cleanliness check
==================================================

v0.2 要求至少两次：

第一次：
final integration/release mutation 前。

第二次：
真正移动 main/release ref 前。

原因：

用户正在并行开发，
第一次 preflight 后
main 仍可能出现新的 production commit。

如果第二次发现新的 C：

不吸收；
不 force；
不重写方案；
只回：

WAITING_FOR_FORMAL_RELEASE_BASELINE=YES
READY_FOR_RELEASE=NO

待对应 task 正式 release 后
继续同一已批准 contract。

请检查这种重复 preflight
是否足够应对高并发开发，
又没有引入 watcher / state machine。

==================================================
八、already-PASS 内容必须保持
==================================================

上一轮 Critic 已明确 PASS：

CHATGPT_WRAPPER_PLAN=PASS
ICON_DELIVERY_PLAN=PASS
SERVER_VPS_ACCEPTANCE_PLAN=PASS
USER_BURDEN_PLAN=PASS
LOCAL_README_PRESERVATION=PASS
C4_IMMUTABILITY_CONTRACT=PASS

请只做回归检查。

特别不要重新要求：

- 新 wrapper 架构；
- 新 icon；
- 新 Gate；
- 新 Server+VPS prompt；
- 用户手工找 Plugin ID；
- 用户手工维护 README；
- 用户多轮 acceptance。

==================================================
九、C4 immutability
==================================================

accepted runtime Skill tree hash：

c504970421c4d14ce9ac5cc1140c014cc5c7fff4ec826b5ab8c66adbe6db42c3

v0.2 仍明确：

release metadata / generated parity
可以在 integration 调整；

accepted PIE Skill tree
不得改变。

如果 Skill tree 改变：

返回 implementation review。

不能拿旧 G1–G4
给新 runtime release。

==================================================
十、Server+VPS / wrapper 不应被 FD1 拖住
==================================================

FD1 是 final release channel blocker，
不是 ChatGPT wrapper 或 user acceptance blocker。

所以 Critic PASS 后应允许：

1. assistant 创建 exact C4 private USER-scope skills-only PIE wrapper；
2. 用户做一次 Server+VPS final acceptance；
3. 如果 USER_ACCEPTANCE=PASS，
   再进入 final integration/release Kickoff；
4. 如果当时 C 类 drift 仍存在，
   Kickoff 只等待新的 formal baseline，
   不要求用户重做 acceptance。

请确认这个顺序是合理的。

==================================================
十一、正式发布 producer contract
==================================================

v0.2 继续要求：

只有 formal release closure
才能 advance origin/release。

release movement 前必须确认：

- target 是 exact validated release commit；
- release 可 fast-forward；
- push non-force；
- remote readback 等于 intended target；
- 不能因为 commit 更新就自动进 release。

请核对它与：

ai-skills-repository-maintainer

以及：

formal-release-and-update-impact.md

一致。

==================================================
十二、PASS / REVISE
==================================================

如果 FD1 已关闭，
且已经 PASS 内容无回归：

CRITIC_RESULT=PASS

FD1=CLOSED

FINAL_DELIVERY_PLAN=PASS
INTEGRATION_RELEASE_CONTRACT=PASS

CHATGPT_WRAPPER_PLAN=PASS
ICON_DELIVERY_PLAN=PASS
SERVER_VPS_ACCEPTANCE_PLAN=PASS
USER_BURDEN_PLAN=PASS
LOCAL_README_PRESERVATION=PASS
C4_IMMUTABILITY_CONTRACT=PASS

GATE_TAXONOMY_CHANGED=NO
C4_RUNTIME_CHANGE_AUTHORIZED=NO

APPROVED_PLAN_PATH=
docs/design/project-instructions-editor/
PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_PLAN_V0_2_2026-10-04.md

APPROVED_GOAL_PATH=
docs/goals/
PROJECT_INSTRUCTIONS_EDITOR_FINAL_DELIVERY_CLOSURE_GOAL_V0_2.md

APPROVED_KICKOFF_PATH=
docs/operations/prompts/
PROJECT_INSTRUCTIONS_EDITOR_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_2.md

APPROVED_PACKAGE_COMMIT=
0278c53fbb1674081a7085ee1831dc2856c9c179

NEXT_HANDOFF=
CHATGPT_WRAPPER_CREATION_AND_SERVER_VPS_ACCEPTANCE

此时仍然：

READY_FOR_RELEASE=NO

因为真正的：

- wrapper creation；
- Server+VPS acceptance；
- formal release cleanliness；
- final integration/release；

尚未执行。

PASS 后不要要求用户现在处理 release/main。
下一步先完成 wrapper + Server+VPS acceptance。

如果 REVISE：

CRITIC_RESULT=REVISE
NEXT_HANDOFF=PLANNER

只允许因 FD1 仍未关闭，
或 v0.2 自己引入新的直接 release risk 而阻塞。

每个 blocker 必须：

stable ID
direct evidence
causal risk
minimum closure

不要重新移动已经 PASS 的终点。
