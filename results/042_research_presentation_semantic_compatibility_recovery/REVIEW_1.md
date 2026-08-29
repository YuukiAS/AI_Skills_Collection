---
schema: AI_BRIDGE_REVIEWED_REVIEW_V1
task_key: 042_research_presentation_semantic_compatibility_recovery
review_round: 1
decision: REVISE
implementation_commit: efc9d40e23dfa00cc9cba709c31f80f86044b5b0
---

# GPT Review

## Decision

REVISE。

042 的共享语义层本身已经取得真实进展：独立 diff 显示 selector 与 deck quality loop 共同消费同一个 `scientific_object_semantics.py`，shared 与 Codex plugin mirror 的该文件内容一致；mature gold index 没有被改动，page-function / domain / panel / capacity 等原有硬约束仍在 selector 中。真实 GitHub CI 对包含 implementation 的已发布 control tip 全部通过。Fresh task-local Terra 也与 implementation `efc9d40e23dfa00cc9cba709c31f80f86044b5b0`、当前 manifest、render-input identity 和 rendered-pixel identity绑定；六张 substantive page 全部逐项 PASS，说明当前 semantic-normalization 改动没有把已通过的模型、结果、流程、负结果、下一实验或医学影像页面直接破坏。

但冻结 Plan 的两个明确 acceptance gate 仍未关闭，所以当前不能 PASS：第一，042 必须真实证明“现有 bounded quality loop 能在这个独立 stress deck 上执行且只执行一次 safe repair，并产生新的 render-input / rendered-pixel identity”，而当前 quality-loop state 仍是 `repair_cycle_count=0`、`WAITING_FOR_DECK_VISUAL_REVIEW`、没有 selected repair、没有 repaired identity；第二，最新 Terra 对完整 contact sheet 给出 BLOCKED，因为标题页把 `Synthetic Semantic-Alias Research Presentation Stress Deck` 暴露给听众，仍是明显的测试/benchmark 制作语言。

## Blocking findings

### 1. 冻结要求的真实 single-cycle repair / pixel-effect 证据尚不存在

**Plan / regression basis**

- 042 Acceptance Gate 6 明确要求：至少一个独立 non-holdout stress deck 必须真实执行且只执行一次 safe repair，repair 前后 render-input 与 rendered-pixel identity 都不同；只让 selector / mapper 单元测试通过不够。
- Implementation Scope 5 要求 repair 来自 task-local structured visual finding；若 finding 无安全唯一映射必须 fail closed，不允许手工往 finding JSON 塞内部 intent。
- single-cycle 上限和现有 repair vocabulary 都是冻结边界，不能为了拿到证据增加第二次 repair 或新造宽泛修复类型。

**Observed evidence**

- `quality_loop_state.json` 当前为 `repair_cycle_count=0`，`selected_repair_directives=[]`，`repair_allowed=false`，`repaired_render_input_identity=null`，`repaired_rendered_pixel_identity=null`，`final_decision=null`。
- `RESULT.md` 也明确把当前状态记录为等待 deck visual review，而不是已经执行过 bounded repair。
- 最新 Terra 的六张 substantive page 全部 PASS，因此当前这次 review 并没有自然产生一个可用于验证 alias-aware page repair 的 substantive-page blocker；唯一 blocker 在标题页/contact sheet。

**Minimal repair**

保持现有 production semantic normalizer、mature gold set、repair vocabulary 和 single-cycle 上限不扩大，只修 task-owned non-holdout validation path：

1. 先让 current fresh Terra evidence 经过现有 bounded quality-loop consumer；若它不能安全映射到现有 page-level repair family，必须保留 fail-closed，不得伪造 directive。
2. 为满足冻结的 live pixel-effect gate，可以调整 042 自己的 non-holdout/public-safe stress fixture，使其中一个**已有支持的 substantive page**稳定暴露一个结构清楚、唯一属于现有 repair family 的问题，例如 aliased quantitative primary object 的 projection-scale 问题、caption/support collision 或 process-layout collision。fixture 仍必须与 041 四篇完全无关，且不得修改 production quality bar 来制造/消除 finding。
3. 该 structured finding 必须通过现有 task-local Visual Review contract获得，再由现有 quality-loop consumer选择已有 directive，最多执行一次，真实重渲染并记录新的 render-input / rendered-pixel identity。
4. 如果本地 Executor 因“新像素必须先发布后才能取得云端 Terra”而无法在同一次执行中完成这条链，不要绕过 Reviewed Handoff，也不要人工伪造 review evidence；按既有 control-plane contract返回 `NEEDS_GPT_PLANNER`，由 Planner做最小 staging publication 路由。

**Required closure evidence**

- `repair_cycle_count=1` 且不能超过 1；selected directive属于冻结的现有 vocabulary。
- repair 前后 render-input identity、rendered-pixel identity以及至少一个 affected-page hash真实变化。
- source bundle / scientific claims / exact CUHK identity保持，shared/plugin parity继续通过。
- fresh task-local Terra 与 repaired identities重新绑定，被修改页面和完整 contact sheet均无 blocking finding。
- unknown / ambiguous role与 incompatible page-function/domain/panel/capacity case继续 no-winner / fail closed。

### 2. 当前完整 deck 仍把 stress/benchmark 术语暴露给听众

**Plan / regression basis**

- Program Goal 明确禁止 audience-facing workflow / QA / benchmark / implementation 制作语言。
- 042 Acceptance Gate 7要求最终目标页与完整 contact sheet均达到 mature doctoral group-meeting / strong paper-talk bar。

**Observed evidence**

- 最新 Terra 的唯一 blocking finding `F-001` 指向 `deck_contact_sheet`：标题缩略图可见 `Synthetic Semantic-Alias Research Presentation Stress Deck`。
- Terra 同时确认整套 substantive sequence 的模型→结果→设计→失败→下一实验节奏、构图变化和独立医学影像 workstream切换都成立；因此当前不要重做已经通过的六张 substantive page。

**Minimal repair**

只修改 042 自己的 non-holdout stress fixture audience-facing metadata，把标题改成由现有 clustered-calibration / segmentation 内容直接支持的正常科研汇报标题；不得出现 `Synthetic`、`Semantic-Alias`、`Stress Deck`、workflow、QA、fixture等制作词。不要为此新增新的 production title sanitizer、状态机或 holdout 特例。

**Required closure evidence**

- 新 title 来自 stress bundle现有科研主题，不引入新的 unsupported claim。
- 六张当前 Terra PASS 的 substantive page不得因标题返修而回归。
- fresh contact-sheet item-level review必须 PASS，并明确无 audience-facing benchmark/test/process language。

## Non-blocking notes

- 当前 semantic normalizer 的角色集合是有限的，selector仍先执行 page-function/domain/panel等硬约束；从真实 diff看，没有出现 unconditional general-card fallback，也没有改 `research_gold_composition_index.json`。这一点符合 042 的边界，本轮不要求为了“更优雅”继续扩 ontology。
- fresh Terra 对模型、定量结果、实验设计、负结果、下一实验和医学影像六页全部 PASS；返修应保护这些已通过像素，而不是重新设计整套 deck。
- 042 即使下一轮 PASS，也只代表 041 后的 generic recovery完成；根据 Program Goal，在冻结下一批 fresh four-paper holdout前仍必须进入用户人工门，不能自动继续 Stage 5。
