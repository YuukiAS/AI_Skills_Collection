# Clear Writing 每轮调用策略与 Web Gate 修订提案 v0.2

日期：2026-10-18  
状态：PLANNER_REVISION_FOR_CRITIC  
对象：`writing-style / Clear Writing`  
design topic：`clear-writing--every-response-invocation-policy`  
source branch：`reviewed/clear-writing--scientific-explanation-readability-repair`  
上一版：`docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_1_2026-10-18.md@1dbcac9666a0c5f69edf538b25f7d7c89bbb2bac`  
Critic review：`docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_CRITIC_REVIEW_V0_1_2026-10-18.md@8e01bb693e6b8e6285f1acf0a49a85f3419cd442`  
Frozen production candidate：`fd7a1578a5042a46a55c5b638f6d550655b1096b`  
Prior implementation/product PASS terminal：`fd0ad0603309fae52b3af0f9f7cdd7f31adea4b4`

## 1. 本轮结论

本轮不重做 Clear Writing 六技能架构，也不修改已经通过独立 Reviewer 的 production candidate。

新的正式产品方向仍然是：

> 对采用 Clear Writing 的 ChatGPT Project，Project setting 作为上层调用策略来源；Clear Writing 被实际选择/加载后继续按现有六技能职责完成写作处理。平台无 bridge 的自动相关性选择保留为诊断，不再作为主要正常入口。

但 v0.2 收紧三个关键边界：

1. **every-turn 强约束不覆盖 pure exact-only machine/verbatim 输出。**  
   自然语言 final response 与 mixed final response 要求经过 Project-level invocation policy；pure JSON/YAML/code/command/raw log/verbatim/exact machine output 是 activation exemption，直接保持 exact payload。

2. **W1 只证明 Project-setting policy 下的长期行为可靠性，不单独证明 plugin 每轮真实加载。**  
   没有 load/invocation evidence 时，不得把最终文字相似性冒充 plugin causality。

3. **W2 只能用严格 matched comparison 证明 plugin incremental value。**  
   只要无法做到同 setting、同 surface/model、隔离 conversation/memory、唯一变量为 plugin availability/consumption，就必须记为 `W2=INCONCLUSIVE` 并停止 release；任何已知混杂 fallback 只能做 diagnostic。

## 2. 当前已验证事实与冻结边界

以下事实已经由现有 Reviewed Handoff 独立审查确认，不在本轮重新打开：

- `clear-writing--scientific-explanation-readability-repair` 已获 PROCESS PASS + PRODUCT / ARTIFACT PASS；
- production implementation 为 `fd7a1578...`；
- KR-WEB-01..09 PASS；
- 四组 should-not-change PASS；
- required CI PASS；
- current `response-clarity` 已明确普通解释、兄弟 writing skill ownership、exact-string preservation 和 pure machine output exclusion；
- Clear Writing 仍由六个既有 skill 构成：
  - `writing-fidelity`
  - `response-clarity`
  - `scientific-prose`
  - `product-ui-copy`
  - `scientific-rewrite`
  - `chinese-prose`

本轮禁止：

- 修改上述 production candidate；
- 新增第七 coordinator skill；
- 新增 router/state machine；
- 修改 Project setting；
- 修改 ChatGPT account / personal plugin；
- 实施 PIE；
- 触碰 Mica；
- 修改 Research Authoring / Presentations；
- 执行 W0/W1/W2/W3 或 G7；
- release/version bump。

## 3. 平台现实约束

2026-10-18 再次核对 OpenAI 当前官方资料，结论与 v0.1/Critic reality check 一致：

- 已安装 Skill 可以在模型认为有帮助时自动使用；
- 模型先看到 Skill 的 name/description metadata，只有请求匹配或用户直接调用时才读取完整 Skill instructions；
- 插件/Skill 的自动使用本质是相关性选择，不是公开承诺的 every-response hook；
- Project instructions 只在对应 Project 内生效，并覆盖 global custom instructions；
- Project memory / project chat history 可能影响后续回答，具体取决于 Project memory mode；
- 当前未发现可公开依赖的普通 ChatGPT Web every-response pre-send Skill finalizer。

因此正式产品设计必须区分：

1. **Project policy**：规定什么时候应尝试使用 Clear Writing；
2. **platform activation**：实际是否选择/加载某个 Skill；
3. **Clear Writing behavior**：在某个具体 Skill 已实际消费后如何改写或保护输出。

三者不能互相冒充。

## 4. 正常入口职责分工 v0.2

### 4.1 Project setting：自然语言与 mixed final response 的 invocation policy owner

采用 Clear Writing 的 Project，拟冻结的上层语义是：

> 对每条面向用户的自然语言最终回答，以及同时包含自然语言解释和机器 payload 的 mixed final response，要求使用 Clear Writing 的合适现有 writing skill。对 pure JSON/YAML/code/command/raw log/verbatim/exact machine output，不为满足“每轮调用”而强制激活 Clear Writing，直接保持 exact payload。

Project setting 只表达 activation policy，不复制任何 Clear Writing 规则。

Project setting 不负责：

- 选择具体 sibling skill 的专业细节；
- 重写语言；
- 模拟未安装/未加载的 Clear Writing；
- 声称某一轮已经真实加载 plugin。

### 4.2 Clear Writing：被选择后的 safe route / safe realization owner

当某个 Clear Writing skill 已经被平台实际选择、直接调用或明确消费时，仍按现有六技能职责工作：

1. 普通解释 / 诊断 / 建议 / task result -> `response-clarity`
2. 正式中文文档 / README / report / Markdown/PDF final pass -> `chinese-prose`
3. 中文或中文主导科研技术 source-faithful 结构重写 -> `scientific-rewrite`
4. English scientific prose -> `scientific-prose`
5. Product UI microcopy -> `product-ui-copy`
6. fidelity protection -> `writing-fidelity`

对于 mixed task：

- 自然语言解释可以由匹配 skill 处理；
- JSON/YAML/code/command/log/field/path/status 等机器 payload 保持精确；
- 不得为了统一风格而改机器 payload。

### 4.3 pure exact-only：activation exemption，不建立虚假的 bypass owner

pure JSON / YAML / code / command / raw log / verbatim / exact machine output：

- 不属于 every-turn invocation policy 的强制对象；
- 最终应直接返回 exact payload；
- 不要求为了“证明 Clear Writing 每轮经过”而加载某个 writing skill；
- 不把“没有加载任何 writing skill”错误记成 Clear Writing 自己执行了 `BYPASS_EXACT`。

这关闭 CW-IP-01 的 ownership 冲突。

若用户显式选择 `@Clear Writing` / plugin 后又要求 exact-only output：

- 仍必须做 should-not-change stress；
- PASS 只证明“显式选择 Clear Writing 不污染 exact output”；
- 如果 surface 没有证据证明某个具体 Skill 的 full instructions 已加载，不得声称“loaded-skill bypass PASS”。

如 Web surface 未来提供直接调用具体 Skill 且可观察 full-instruction load，可额外做 diagnostic；不新增 release Gate。

## 5. Revised Web Gate

### W0 — invocation-policy safety

W0 现在分两类证据。

#### W0-A 自然语言 / mixed response safety

在 frozen candidate 下，对明确要求使用 Clear Writing 的 Web 请求覆盖：

1. 普通技术解释；
2. 复杂科研解释；
3. 陌生方法 / 多重下标对象；
4. 必要长答；
5. 临时英文覆盖及恢复；
6. 完整 executable prompt / contract；
7. 真正有分支价值的流程；
8. mixed explanation + JSON/YAML/code/log payload；
9. exact identities：命令、路径、字段、状态、commit、产品名。

PASS 要求：

- 任务落到正确现有 writing skill；
- `response-clarity` 不越权接管 sibling route；
- mixed task 中机器 payload 精确保留；
- 长答不被机械压短；
- 临时语言覆盖不污染后续默认语言；
- 原四组 should-not-change 仍成立。

#### W0-B explicit-plugin-selection exact-only stress

至少覆盖：

- pure JSON；
- pure YAML；
- pure code；
- raw log/verbatim；
- exact command / machine payload。

测试方式可以使用 `@Clear Writing` 或当前 surface 的明确 plugin-level selection。

PASS 要求：

- exact output byte-content 等价；
- 不加自然语言前言；
- 不装饰、不解释、不重排字段/代码；
- plugin selection 本身不污染 exact output。

Claim boundary：

- 若 surface 仅证明 plugin-level selection，而不能证明具体 Skill full instructions 已加载，则结论只能是  
  **PLUGIN_SELECTION_DOES_NOT_CONTAMINATE_EXACT_OUTPUT**；
- 不得写成 loaded-skill bypass PASS。

W0 FAIL 时：

- 停止 W1/W2；
- 不修改 Project setting；
- 回 Planner/Critic 只处理现有六技能 metadata/contract 的最小问题；
- 不默认新增 coordinator。

### W1 — Project-setting policy 下的长期行为可靠性

W1 的目标不再是“证明 Project setting 每轮强制加载 plugin”。

W1 的正式 claim 是：

> 在不要求用户每轮手动 @ 的情况下，Project-setting invocation policy 是否能让多轮最终行为持续满足 Clear Writing 目标合同。

推荐测试序列至少包括：

- ordinary explanation -> pure exact JSON -> ordinary explanation；
- Chinese -> temporary English -> Chinese recovery；
- short answer -> necessary long answer；
- explanation -> executable prompt/contract；
- one sibling writing route -> unrelated next-turn ordinary response；
- mixed response -> next-turn exact-only -> ordinary response。

W1 PASS 要求：

- 多轮行为持续满足 route/bypass/语言恢复/非粘滞要求；
- exact-only activation exemption 不影响下一轮普通 Clear Writing behavior；
- temporary English 只影响当前明确范围；
- sibling route 不跨 turn 错误粘滞；
- surface 有 invocation/load evidence 时必须记录；
- 没有 evidence 时，不得靠模型自述“我用了 Clear Writing”。

W1 只支持：

**PROJECT_POLICY_BEHAVIOR_RELIABILITY=PASS**

W1 不单独支持：

**PLUGIN_LOADED_EVERY_TURN=PASS**

这关闭 CW-IP-02。

W1 FAIL 仍说明 Project-setting policy 作为 normal entry 不可靠，应停止进入 W2 release claim。

### W2 — strict matched plugin increment

W2 是唯一负责关闭“Clear Writing plugin 相对 Project setting 本身是否有稳定增量”的 release-critical Gate。

#### 5.2.1 冻结 identity

在运行前必须冻结并记录：

- treatment / control Project-setting exact bytes；
- ChatGPT surface；
- model；
- actual plugin/release identity；
- Project memory mode；
- conversation isolation structure；
- task set；
- task order policy；
- attempt budget；
- rubric；
- Reviewer input；
- stop condition。

#### 5.2.2 两 arm 必须完全 matched

两 arm 必须满足：

- Project-setting exact bytes 完全相同；
- same ChatGPT surface；
- same model；
- same pre-frozen task set；
- same task-order policy；
- same attempt budget；
- same rubric；
- same evaluation procedure；
- fresh isolated conversation context；
- 不允许一 arm 读取另一 arm 的输出、conversation 或 Project history。

若使用 ChatGPT Project：

- 必须冻结并记录 Project memory mode；
- 测试结构必须防止 cross-arm contamination；
- 不能让 treatment chat 成为 control chat 可引用的 project history，反之亦然。

#### 5.2.3 唯一实质变量

Treatment：

- frozen Clear Writing candidate 可用；
- 需要有实际 availability / consumption 证据，证据强度按 surface 能提供的真实能力记录。

Control：

- Clear Writing candidate 不可用；
- 不复制任何 Clear Writing Skill 正文；
- 不允许根据 treatment 输出人工补规则；
- 只保留与 treatment 完全相同的 Project setting bytes。

唯一允许的实质差异：

**Clear Writing candidate availability / consumption**

#### 5.2.4 禁止事项

- 不得挑最好输出；
- 不得重复到成功；
- 不得中途修改 rubric；
- 不得看完一 arm 后改另一 arm 的 task；
- 不得改变 task order policy；
- 不得用不同模型/surface；
- 不得把 plugin prose 复制到 control；
- 不得把 Project setting 自身带来的改善归因给 plugin。

#### 5.2.5 W2 结论

PASS 需要：

- treatment 在多个预冻结任务族上有稳定、可读、可归因于 plugin availability/consumption 的增量；
- 不牺牲 W0 exact/mixed/long-answer controls；
- control 若已同样好，则不能为了“证明插件有用”改 rubric。

若当前 ChatGPT 产品 surface 无法合法建立上述 matched condition：

`W2=INCONCLUSIVE`

并停止 release。

任何已知存在混杂的 fallback：

- 只能标记 `DIAGNOSTIC_ONLY`；
- 不得替代 W2 PASS；
- 不得声称 plugin incremental value 已证明。

这关闭 CW-IP-03。

### W3 — no-bridge automatic-selection diagnostic

原 A/E 自动选择实验保留，但只回答：

- metadata discoverability；
- 无 Project policy 时模型是否相关性触发；
- Project policy 是否提高行为可靠性/可用性。

W3：

- 非 release-critical；
- 不证明 every-turn；
- 不替代 W1；
- 不替代 W2 plugin increment。

## 6. Project setting bridge v0.2

若 Critic 最终批准本设计，未来 execution package 中用于 Web test 的 bridge 应保持最薄：

> 对每条面向用户的自然语言最终回答，以及自然语言与机器 payload 混合的最终回答，如果当前 Clear Writing 可用，则使用其合适的现有 writing skill；pure JSON/YAML/code/command/raw log/verbatim/exact machine output 不为此强制调用 Clear Writing，直接保持精确原样。不要模拟、重建或复制 Clear Writing 内部规则。

正式 matched W2 时 treatment/control 必须使用 exact same bytes。

该 bridge：

- 只属于测试/normal-entry policy；
- 不等于 Clear Writing 实现；
- 不复制六技能规则；
- 不声称 plugin 已真实消费；
- 本轮不写入任何真实 Project setting。

## 7. Fresh G7 v0.2

G7 保留为 final fresh generalization Gate，但 freeze identity 现在必须完整。

### 7.1 进入 G7 前冻结

至少冻结：

- frozen production candidate commit；
- actual Web plugin/release identity；
- Project bridge exact bytes；
- ChatGPT surface；
- model；
- Project memory mode；
- conversation isolation policy；
- attempt budget；
- fresh task set；
- task order policy；
- W0/W1/W2 rubric；
- Reviewer input；
- stop condition。

任一上述 identity 在运行中改变，则不能把结果拼成同一 G7 final batch。

### 7.2 fresh task 目标

G7 验证 frozen invocation policy 下的未见任务是否同时满足：

- 正确 sibling routing；
- natural/mixed response reader quality；
- exact-only activation exemption；
- mixed exact payload protection；
- temporary language override/recovery；
- sibling route switching；
- fidelity / no semantic drift；
- plugin incremental value 的既定 rubric。

### 7.3 fresh 排除

永久排除：

- KR-WEB-01..09；
- 原四组 should-not-change；
- W0 task；
- W1 task；
- W2 task；
- W2 diagnostic fallback；
- 任何开发期间看过并用于修改机制/rubric 的样本。

## 8. Capability Gate revision

不新建 G8/G9；只修改原 G1 的 release semantics。

| Gate | v0.2 含义 | release-critical |
|---|---|---|
| G0 | distribution / candidate identity | 是 |
| G1a | W0 natural/mixed safety + explicit-selection exact stress | 是 |
| G1b | W1 Project-policy multi-turn behavior reliability | 是 |
| G1c | W2 strict matched plugin increment | 是 |
| G1d | W3 no-bridge discoverability diagnostic | 否 |
| G2 | known response-readability regressions | 是，当前 candidate 已 PASS |
| G3 | fidelity / exact protection | 是，W0 补显式选择与 mixed evidence |
| G4 | sibling writing ownership 不退化 | 是 |
| G5 | domain consumer boundary | 保持原定义 |
| G6 | multi-turn / language recovery | 是，主要由 W1 |
| G7 | frozen policy 下 fresh generalization | 是 |

## 9. 失败与恢复

### W0 exact contamination

归因：explicit selection / current skill metadata 或实现边界存在安全缺口。  
动作：停止；回 Planner/Critic 做最小 bounded repair。不得继续 W1/W2。

### W1 行为不稳定

归因：Project-setting policy 不能稳定产生目标长期行为。  
动作：停止；核查 Project bridge、surface/plugin availability、memory/context 条件。不得把失败自动归咎 `response-clarity`。

### W1 行为 PASS 但无 plugin load evidence

合法结论只有：

`PROJECT_POLICY_BEHAVIOR_RELIABILITY=PASS`

不得升级成 plugin causality。

### W2 无法构造 strict matched condition

`W2=INCONCLUSIVE`

停止 release。不得用 confounded fallback 替代。

### W2 control 与 treatment 一样好

结论：

`PLUGIN_INCREMENT_NOT_PROVEN`

停止 release，回 Planner重新判断产品定位；不得移动 rubric。

### W3 自动选择弱

若 W0/W1/W2 PASS，不阻塞 Project-policy product route；记录 discoverability limitation。

## 10. 替代方案比较

### A. 继续以 no-bridge automatic selection 为主

仍不采纳。官方合同只支持 relevant/helpful auto-use，不能承担 every-turn 主承诺。

### B. pure exact-only 也强制调用 Clear Writing

不采纳。当前六 Skill 没有 coordinator owner，且 exact-only 本身不应为了证明调用而加载 writing workflow；这会制造虚假 loaded-bypass claim。

### C. Project policy 覆盖 natural/mixed，exact-only activation exemption；Clear Writing 负责被加载后的既有 sibling skill behavior

采纳。它避免新增 coordinator，同时保留用户真正关心的最终阅读层覆盖。

### D. W2 使用已知混杂 fallback 作为 release evidence

不采纳。已知混杂只能 diagnostic，不能支持 plugin causality。

## 11. 五遍预检摘要

### 产品

用户目标是采用 Clear Writing 的 Project 中，普通最终阅读层稳定受益，同时 exact machine output 不被破坏。

### 现实

当前官方平台只提供相关性 Skill activation 与 Project instructions；没有公开 every-response Skill finalizer，也没有保证每轮提供 load receipt。

### 替代

已比较 no-bridge auto-selection、复制全部规则进 Project setting、强制 exact-only invocation、strict Project-policy + matched increment。v0.2 选择最后一种。

### 反证

v0.2 明确防止三类假 PASS：

- exact-only 没加载 Skill却冒充 loaded bypass；
- W1 最终文字好看却冒充 plugin causality；
- W2 有 memory/session/plugin-availability 混杂却冒充 matched increment。

### 执行

本轮不执行 Web Gate。Critic PASS 后 Planner 才冻结 W0/W1/W2/W3 execution package；如果 W2 的合法 matched environment无法构造，release 必须停止。

## 12. 外部证据复核

2026-10-18 重新核对 OpenAI 官方资料，未发现会改变本轮三个 finding 的新事实：

- Skills in ChatGPT：安装后可在有帮助时自动使用；
- OpenAI Developers Skills：模型根据 metadata 决定是否调用，调用后读取完整 instructions；
- Plugins in ChatGPT：插件可以由相关请求自动使用，也可以直接选择/提及；
- Projects in ChatGPT：Project instructions 只在 Project 内生效；Project memory mode 会改变 conversation history 可见范围。

因此 v0.2 不把自动选择、Project instructions、Skill load 三者混成同一强机制。

## 13. 三个 Critic finding 的关闭映射

### CW-IP-01 — ACCEPT / CLOSED IN PROPOSAL

- every-turn 强约束改为 natural/mixed final response；
- pure exact-only 改为 activation exemption；
- W0 exact-only 只证明 explicit plugin selection 不污染 exact output；
- 无具体 Skill load evidence 时禁止声称 loaded-skill bypass；
- 不新增 coordinator。

### CW-IP-02 — ACCEPT / CLOSED IN PROPOSAL

- W1 正式 claim 改为 Project-policy multi-turn behavior reliability；
- load evidence 有则记录，无则不猜；
- W1 PASS alone 不证明 plugin causality；
- plugin causality 由 W2 关闭。

### CW-IP-03 — ACCEPT / CLOSED IN PROPOSAL

- W2 强制 exact same Project-setting bytes、same surface/model/tasks/order/budget/rubric；
- fresh isolated conversation context；
- freeze Project memory mode；
- 防 cross-arm contamination；
- plugin availability/consumption 是唯一实质差异；
- 无合法 matched condition -> `W2=INCONCLUSIVE`，停止 release；
- confounded fallback diagnostic-only；
- G7 freeze identity 补齐。

## 14. 本轮不做什么

- 不修改 `fd7a157...`；
- 不修改 Project setting；
- 不修改 ChatGPT account / personal plugin；
- 不执行 W0/W1/W2/W3/G7；
- 不实施 PIE；
- 不碰 Mica；
- 不改 Research Authoring / Presentations；
- 不新增 Skill/router/state machine；
- 不 release/version bump；
- 不创建新 tracking Issue。

## 15. Critic 本轮只需复核的范围

下一轮 Critic 只需优先复核：

1. CW-IP-01 是否被 activation exemption + exact-stress claim boundary 正确关闭；
2. CW-IP-02 是否被 W1 behavior-only claim + W2 causality ownership 正确关闭；
3. CW-IP-03 是否被 strict matched W2 + contamination controls + INCONCLUSIVE stop rule 正确关闭；
4. 这些改动是否意外破坏已认可方向：
   - Project-policy normal entry；
   - W0 -> W1 -> W2 -> W3；
   - W3 diagnostic-only；
   - fresh G7；
   - 六技能架构不变；
   - production candidate 不变。

Critic PASS 后，Planner 才进入 Web Gate execution package freeze；PASS 本身不授权执行任何 Web Gate 或修改真实 Project setting。
