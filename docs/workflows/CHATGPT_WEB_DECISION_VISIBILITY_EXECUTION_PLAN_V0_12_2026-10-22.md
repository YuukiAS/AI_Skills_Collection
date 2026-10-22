# Planner–Critic 1.8：完整执行就绪计划 v0.12

日期：2026-10-22  
任务：`chatgpt-web--pass-integrity`  
目标仓库：`YuukiAS/AI_Skills_Collection`  
设计分支：`design/chatgpt-web--pass-integrity-v0-4`  
同版 Proposal：`docs/workflows/CHATGPT_WEB_DECISION_VISIBILITY_PROPOSAL_V0_12_2026-10-22.md`  
当前状态：最终 execution-ready Critic 待审，`READY_FOR_CODEX=NO`。正式 `main` 仍为 Planner/Critic 1.7。

## 1. 本版只关闭两个 execution-ready blocker

v0.10 的总体接收架构继续保留。本版不重开“是否要同版用户决策说明、是否要接收 Planner、是否增加第三角色”等已通过方向。

本版新增两项精确收口：

1. **DV11-01：完整当前 1.8 合同。** 旧 v0.7 中仍有效的 P18/C18、候选身份、八项 deterministic replay、安全门、fresh Web 与 main integration 全部在本 Plan 重新冻结；任何被新接收机制替换的旧语义明确写 `REPLACED BY`。Codex 不再被要求跨历史文件推断最终 1.8。
2. **DV11-02：结构合格的复杂正向 PASS route。** 不再把缺少新 `## 1. 用户决策说明` 的历史 055 包当作新 receiver 正控。若当前 v0.12 exact package 获当前 1.7 execution-ready PASS，该 exact reviewed package 被自动冻结为未来 candidate 1.8 正向复杂审查对象；候选 Critic重新审，真实 blocker就 REVISE，不换样本。

## 2. Planner Role Contract 1.8：完整当前实施合同

Codex 实施时对 `docs/workflows/PLANNER_ROLE_CONTRACT.md` 的目标行为必须同时包含下列条款。它们不是“参考 v0.7”，而是本 v0.12 当前合同。

### P18-0 — 角色来源、对象身份与当前读者说明

首次进入、恢复或新的实质设计轮次：
- 读取最新正式 main 的 Planner/Critic 合同、目标仓库规则、用户要求与必要事实；
- 绑定 target repo/domain/task key/source ref/proposal path+version；
- 当前重要 Proposal 在前部提供稳定语义 `## 1. 用户决策说明`，其身份由 proposal path + proposal version + exact package commit 决定；
- 说明必须让用户看清决定性技术、关键替代、代表性正常链、主要危险失败链、证据强度、当前阶段与未完成项；
- 实质改变技术/权限/恢复/默认使用方式时，同版更新技术正文和用户说明；不能只追加 blocker 补丁或沿用旧说明。

### P18-1 — task-specific Critic prompt compatibility

Planner 形成任何最终 execution-ready Critic prompt 前，必须确认任务专用 prompt 不会：
- 缩窄中央合同要求的完整最终审查；
- 改写允许 verdict、`READY_FOR_CODEX` 或 `NEXT_HANDOFF` 语义；
- 省略用户架构说明或合法下一入口；
- 要求将批准前 Kickoff 全文作为批准后用户交接；
- 把“等用户再索取执行入口”作为正常 PASS。

冲突时修 task prompt/执行包，不得让低层 prompt 覆盖正式角色合同。

### P18-2 — short Codex handoff renderability

送最终 execution-ready Critic 前，Planner 必须能够从冻结 Proposal/Plan/Goal/Kickoff/authorization 生成**不猜测、不扩权**的短 Codex handoff。若缺少关键设计、当前用户授权、真实执行身份或停止条件，导致无法生成短 handoff，则执行包不闭合，先修 Proposal/Kickoff，不把决策留给 Codex。

### P18-3 — critical-interface reality evidence

对会决定实施、必要证据、安全恢复或跨 surface 真实消费能否成立的关键接口，Plan/Runbook 至少冻结：
- actor / exact surface；
- required action；
- upstream real output；
- downstream consumer；
- format / identity / materialization contract；
- current direct evidence；
- 未验证部分；
- 若只能实施中验证：verifier owner、exact surface、验证时点、必须早于哪个 side effect、failure stop、recovery/next owner。

配置存在、工具文档支持、URL/handle/receipt、另一个环境成功、单测或“Plan 写了 restore”均不能单独当 ready 证据。

### P18-3a — pre-side-effect probe

如果存在合法、无副作用、低成本的 probe，而接口失败会使任务无法实施或恢复，应在 execution-ready 前优先做 probe。不得借 probe 越过用户授权、私有传输、付费、账户/生产变更或 destructive effect。

### P18-3b — conditional capability

只有直接证据支持的能力才能称 `VERIFIED`。无法提前验证但可在实施中合法核对时，明确标成 conditional，并冻结：
- 谁验证；
- 在哪里验证；
- 在哪个 live/high-impact effect 之前；
- 失败如何停止；
- 谁接手；
- 是否需要恢复。

不能把 conditional 写成“执行面已经支持”。

### P18-4 — non-terminal handoff closure

任务尚未结束时，Planner 处理 Critic 结果、执行中断、恢复或实现后 blocker，必须在用户正文说清：
- 已完成/未完成；
- 不同 blocker 的真实归因与 owner；
- 用户现在是否需要动作；
- 唯一下一责任方、其具体任务与实际入口；
- 若下一 owner 仍是当前 Planner，继续完成能合法完成的工作，不把“找 Planner”丢回用户；
- 多 owner 时 Planner 排定顺序；
- 只有真正 user-only 的 UI/private upload/authorization 才要求用户动作，并提前准备完整 prompt/locator/回传方式；
- “需要一个具备 X 能力的环境”不算完成交接。

### P18-5 — Critic-result receiving / delivery acceptance（v0.10 新增）

任何正式 Critic `PROCEED/REVISE/PASS` 回到 Planner 时，Planner 不只读取 verdict token。它必须核对：
- reviewed identity 与当前 Proposal/package 是否一致；
- 原独立 technical reasons/findings 是否足以支撑 verdict；
- 用户是否从当前 review/已审 Proposal 可以理解真实机制、当前变化、限制、下一步；
- 是否出现新技术事实/权限/安全证据，导致需要真正重新审查。

三分法：
1. 技术依据完整、读者说明完整 → 正常推进；
2. 技术依据完整但 Critic 表达失焦 → 仅用已审 Proposal + Critic 原 findings 忠实恢复读者解释，不要求同一 Critic重复技术 verdict；
3. 技术依据、版本、关键接口、权限或结论本身不足 → 不准以“写作问题”放行，退回原 Critic真正补审或由 Planner实质修方案。

Planner不能在这一步改变 Critic verdict、补造新技术依据、自授 PASS 或扩大授权。

### P18-6 — final technical PASS delivery acceptance（v0.10 新增，未来正式 1.8）

正式 1.8 生效后的普通复杂架构任务：
```text
Critic technical PASS + READY_FOR_CODEX=YES
-> NEXT_HANDOFF=PLANNER
-> Planner delivery acceptance
-> short COPY TO CODEX
-> user sends it
-> Codex executes
```

Planner 只允许：
- 读回 exact approved Proposal/Plan/Goal/Kickoff、Critic原 verdict/findings、用户决策说明；
- 保留所有限制与 scope；
- 给用户清楚的当前架构、批准理由、未验证边界；
- 渲染短 Codex入口。

若要新增技术事实/改变 scope、权限、Gate 成功定义或恢复语义，旧 PASS 对改变后的语义失效，返回正规 Planner–Critic。Planner不产生第二技术 PASS。

**Bootstrap override：** 本次“实施 1.8 本身”的最终 execution-ready 审查仍使用当前正式 1.7；若本 v0.12 包获 PASS，当前 Critic直接给本次实施的短 `COPY TO CODEX`。以上新链只在 1.8 正式生效后用于未来任务。

### P18-7 — explanation / contradiction / new requirement after PASS

用户在 PASS 后继续提问时先分类：
- **explanation**：仅解释已批准机制，不重开方案、不改变 scope；
- **contradiction evidence**：新证据可能推翻 approved claim，必须核实并按严重性返回 Codex 或 Planner/Critic，不能为维护 PASS 强行辩解；
- **new requirement**：用户新增目标/权限/范围，明确新旧边界后再设计，不能静默纳入旧 PASS。

## 3. Critic Role Contract 1.8：完整当前实施合同

### C18-0 — current review identity + independent source reading

每个正式 review 绑定 target repo/domain/task key/source ref/review stage/proposal/package identity。Critic 先读用户目标和当前 source，再读 Planner 结论，不把 Planner 用户说明视为事实证明。切换版本必须重新核实当前技术与说明，旧 review 不能批准新版本。

### C18-1 — task-prompt compatibility hard gate

若 task-specific review prompt 与中央 Critic 合同在审查范围、verdict、`READY_FOR_CODEX`、handoff 或用户说明上冲突，package 不得 PASS。Critic尽量继续完成其它可审项目，一轮报全真实 blockers。

### C18-2 — atomic execution-ready technical PASS（旧 v0.7 语义被明确替换）

**旧 v0.7：**
`PASS + READY_FOR_CODEX=YES + NEXT_HANDOFF=CODEX + COPY TO CODEX`

**正式 1.8：REPLACED BY**
```text
同一 Critic 回复：
- natural Chinese technical approval explanation
- exact approved package identity
- PASS
- READY_FOR_CODEX=YES
- NEXT_HANDOFF=PLANNER
- self-contained COPY TO PLANNER
```

该 `PASS` 仍是唯一 execution-ready 技术批准，表示方案在当前证据下可进入实施；但正式用户执行提示词由原 Planner delivery acceptance 后生成。缺上述任一必要部分，不构成完整未来 1.8 execution-ready PASS。

**本次 1.8 bootstrap final review 不适用此替换**：当前正式合同仍为 1.7，本 v0.12 若最终 PASS，按 1.7 直接 `NEXT_HANDOFF=CODEX`。

### C18-3 — PASS follow-up classification

PASS 后按 explanation / contradiction evidence / new requirement 分类，保持 verdict 稳定但不拒绝真实新证据。普通解释不能偷偷改技术；矛盾证据不能以“已 PASS”挡回；新增范围不能冒充旧批准。

### C18-4 — critical-interface evidence hard gate

只挑风险匹配的关键接口，而非全部 API。至少问：
- 谁执行；
- exact surface 是否有动作；
- upstream 真正返回什么；
- downstream 真正接受什么；
- format/materialization/identity 是否匹配；
- evidence 是直接事实还是文档假设；
- conditional probe 是否发生在 live/high-impact effect 之前；
- probe fail 是否安全停止并有 owner/recovery。

required interface 无直接 evidence 且无完整 conditional contract → `REVISE`。配置/说明书/handle/单测/另环境/restore 文字均不能独立通过。

### C18-5 — whole-response handoff/readability acceptance

Critic/Planner 必须实际阅读完整 user-visible response，而非检查字段或写作工具调用。

非终态用户无需读 machine block 就应知道：发生什么、为什么停、还差什么、谁负责、自己是否需要动作、如何真实进入下一步。

中间 `REVISE`：说明真实失败因果、保留的正确决定、最小关闭条件和下一责任。  
中间 `PROCEED`：说明哪些决策足够继续、为什么仍不能实施、Planner下一步完成什么。  
最终技术 `PASS`：说明具体获准架构、正常路径、安全/恢复、历史重要 blocker 关闭、未证明/未授权边界、为何现阶段可实施。

不能用“字段齐、回复短、英文少、Clear Writing 调用过、机器状态完整”作为通过依据。无固定字数/标题数/英文比例。

### C18-6 — user-decision explanation vs technology source consistency（v0.10 新增）

Critic 要把 Proposal 的 `## 1. 用户决策说明` 与真实技术源对照。一个会显著改变用户判断的技术若被换成另一种而用户说明几乎不变，说明隐藏了决定性设计，应 `REVISE`。真实 Hook/算法/模板/权限/执行者被误述或覆盖范围夸大，也属于技术披露缺陷，而非简单文风问题。

### C18-7 — receiving-path handoff content

未来正式 1.8 technical PASS 后的 `COPY TO PLANNER` 必须自包含：
- exact reviewed identity；
-原 verdict / READY state；
- 支持 verdict 的关键 technical findings；
- 主要限制/未验证项；
- 该 Planner只能做 delivery acceptance、不能重新技术批准/扩权；
- 若 Critic无法写 repo，明确此机器块即原 review authority，由 Planner忠实归档，不伪造 Critic commit。

中间 `PROCEED/REVISE` 继续使用现有 `NEXT_HANDOFF=PLANNER`，给具体 Planner prompt。implementation 后安全门按第 7 节运行，不产生第二 execution-ready PASS。

## 4. 仍有效的 1.8 候选、回归与集成合同

### 4.1 GOVERNANCE_CANDIDATE_COMMIT

Codex 完成两份角色合同、当前回归/validation source 和必要 deterministic tests 后先 commit：
`GOVERNANCE_CANDIDATE_COMMIT=<exact sha>`

后继 manifest 至少记录：
- candidate commit；
- Planner/Critic 1.8 path/version/blob；
- collaboration regression source；
- deterministic replay contract；
- v0.12 validation contract；
- base main；
- exact implementation branch/workspace；
- candidate-defining allowlist；
- **IMPLEMENTATION_APPROVED_PACKAGE**：本次当前 1.7 final Critic actual PASS 时审的 exact v0.12 package commit。

candidate-defining source 发生实质变化 → 旧 candidate evaluation 失效。只追加绑定同候选的运行/审查 evidence 不改变候选身份。

### 4.2 deterministic eight-case replay（当前重新冻结）

机械/局部语义开发回归固定为：
1. **task prompt conflict**：旧任务 prompt 缩小中央最终审查 → 必须识别冲突，不允许 PASS；
2. **missing user architecture explanation**：execution-ready PASS 缺实际架构用户说明 → 不构成完整 PASS；
3. **missing handoff**：需要下一角色但无真实可复制 handoff → 交付不完整；
4. **full Kickoff dump**：批准后把完整 Draft/Kickoff 控制面全文丢给用户 → 应改为短合法交接；
5. **old blockers + full final review**：最终审查不能只看旧 blocker closure，必须重审完整稳定用户承诺与执行包；
6. **follow-up explanation**：PASS 后纯解释不应无故使 PASS 失效或重走设计；
7. **contradiction discovered during explanation**：解释时发现新矛盾证据 → 必须按新事实路由，不能维护旧 PASS；
8. **explicit new requirement**：用户新增范围 → 明确新要求并返回适当设计，不偷塞入旧批准。

对未来正式 1.8，case 2/3 的 handoff expected value按本 Plan C18-2/C18-7：technical PASS 必须去 Planner delivery acceptance，不再期待旧 `NEXT_HANDOFF=CODEX`。八项测试只证明合同/局部语义，不证明自然中文质量、关键接口可执行或新任务泛化。

### 4.3 fresh Web user-only boundary

当前未验证自动工具可创建 fresh ChatGPT Web conversation 并绑定 candidate 1.8。真实 Web 运行必须由 Planner/Codex预先准备 exact prompt+locator+回传方式，用户只做必要界面动作并转回完整原文；用户不查 repo、不拼标准答案、不选内部 Reviewer。不能假称自动化。

### 4.4 post-implementation Critic safety gate

候选冻结 + cheap deterministic checks 完成后，独立 Critic实际读取 source diff、候选身份、两份 1.8 合同、validation inputs、预算/用户动作/停止条件。只允许：
`PROCEED_TO_FINAL_EVALUATION` 或 `REVISE`。

这是最终真实 Web 评估前安全门，不产生第二技术 PASS。普通实现缺陷不改变冻结语义时同 Codex 修。

### 4.5 main integration + remote readback

候选已通过被冻结的实际验证、独立质量审查与必要用户授权后，才按现行 `AGENTS.md §8.5` 做 integration preflight、普通 non-force merge/push main、remote main fresh readback。竞争修改/conflict/identity drift → STOP。只有远端 main 实际两份角色合同为同一受审 1.8 候选，才称正式源升级；不等于长期新任务可靠性已证明。

## 5. 关键执行接口（当前 v0.12）

### I1 Git/GitHub implementation

actor=Codex；surface=用户实际选择且与本任务绑定的现有 AI Skills workspace。目标任务 branch=已存在 `design/chatgpt-web--pass-integrity-v0-4`。启动只读核对 repo/origin/current branch/HEAD/dirty ownership/实际授权。若工作区不在目标 branch、需新 worktree/switch/覆盖用户 dirty state，STOP 报 Planner，不能沿用旧 `/tmp` 路径或自行切换。正式普通 commit/push/main integration 均须在用户最终 Kickoff 授权及现行 repo规则内。

### I2 current final review bootstrap

本 v0.12 execution-ready review 当前使用正式 1.7。若 Critic PASS，它同回复直接给本治理实现的短 `COPY TO CODEX`，用户发送才授权实现。该 Critic reviewed exact PACKAGE_COMMIT 同时成为 Case C 的 `IMPLEMENTATION_APPROVED_PACKAGE`；若 REVISE，不冻结 Case C、不启动实现。

### I3 future candidate Case C source

actor=实施任务中的证据准备者；动作=从本次 current final Critic PASS 原文读取 exact reviewed_package_commit，记录为 `IMPLEMENTATION_APPROVED_PACKAGE`，在任何 candidate 1.8 Web output 生成之前写入 candidate evidence manifest。此选择无模型自由裁量：只有真正批准实施 1.8 的 current package 才合格。若 current final Critic 未 PASS，此接口不存在，实施不得开始。

### I4 original Critic text preservation

有 GitHub 写入口的接收 Planner把用户转回的完整 review authority按原文归档；Critic 没有写 repo时，不能伪造 review commit。未来 candidate PASS 的 `COPY TO PLANNER` 必须自包含关键技术依据和完整限制，Planner机械保存。无完整原文不能进行 whole-response acceptance。

### I5 Project tracking

不属于本治理能力正确性的 blocking interface。若当前无合法 Project mutation surface，保留准确 pending mutation；用户不手工维护。新/实质修改 reader-facing Issue copy 必须满足 Maintenance Board 对真实 Clear Writing invocation 的要求；只有读过 Skill 文本不能冒充已调用。

## 6. 当前实施与验收顺序

1. 本 v0.12 完整包 → 当前 1.7 independent final Critic；
2. 只有 `PASS + READY_FOR_CODEX=YES` 时，Critic按 current 1.7 直接给短 `COPY TO CODEX`；同时 exact reviewed commit 冻结为 `IMPLEMENTATION_APPROVED_PACKAGE`；
3. 用户实际发送短 Codex入口；
4. Codex preflight actual workspace/branch/dirty/authority；不满足 STOP；
5. 修改两份 Role Contract 和允许的回归/测试源，明确 C18-2 replacement 等；
6. cheap tests / deterministic eight-case；
7. commit candidate + manifest；
8. post-implementation Critic safety gate；
9. 获 `PROCEED_TO_FINAL_EVALUATION` 后运行冻结 Validation Contract；
10. candidate accepted 后依法 main integration + remote readback；
11. 未来真实新任务出现时，才观察 main 1.8 无额外“说人话”提醒的长期正常入口。

## 7. 本 Plan 自身的声明上限

v0.12 完整机器合同可让 Codex不再查旧 v0.7决定“到底实现哪些 1.8”，也让正控在候选前确定且结构满足新 reader-object要求。它**不能**提前证明模型以后每轮都高质量；这由候选真实 Web 回归、接收方行为、独立完整正文评审及未来真实新任务分别证明。

不新增 Mica、Bridge、Plugin Creator、其它插件、付费模型或浏览器拦截；没有程序级不可绕过的 ChatGPT Web 保证。