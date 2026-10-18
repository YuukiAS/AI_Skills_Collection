# Clear Writing 每轮调用策略与 Web Gate 修订 — 独立 Critic Review v0.1

日期：2026-10-18  
审查阶段：bounded invocation-policy / Web Gate design revision  
审查对象：`docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_1_2026-10-18.md`  
Proposal commit：`1dbcac9666a0c5f69edf538b25f7d7c89bbb2bac`  
Frozen production candidate：`fd7a1578a5042a46a55c5b638f6d550655b1096b`

## Decision

**REVISE**

总体方向成立，不要求重做六技能架构，也不重开已经 PASS 的 `response-clarity` 内容质量。

本轮支持以下方向：

- 采用 Clear Writing 的 Project 可以把 Project instructions 作为“要求使用 Clear Writing”的上层策略来源；
- 平台按相关性自动选择插件/Skill 应降为 discoverability / fallback diagnostic，而不是 every-turn 产品承诺；
- `response-clarity` 不应接管 sibling writing skills；
- 不需要新增第七 coordinator skill/router/state machine；
- W0 -> W1 -> W2 -> W3 的大顺序合理，W3 可降为非 release-critical；
- fresh G7 应验证冻结后的新调用策略，而不是继续把无 bridge 自动选择当主要目标。

但当前 v0.1 有三个会直接导致 Web Gate 错判的 blocking finding。它们都是调用语义和因果设计问题，不要求现在修改 production。

## External reality check

实际核对 2026-10-18 当前 OpenAI 官方资料：

1. **Skills in ChatGPT**：安装后，ChatGPT 可以在“有帮助时”自动使用一个或多个 Skill；不同产品/surface 的 availability 与安装/同步可以不同。
2. **Developers / Skills activation**：模型先看到 Skill 的 name/description metadata；当请求匹配该 Skill，或用户直接调用时，才加载完整 `SKILL.md` instructions。
3. **Plugins in ChatGPT**：已安装插件在与请求相关时自动使用，也可以由用户通过 `@` 或 composer 明确选择。
4. **Projects in ChatGPT**：Project instructions 只在该 Project 内生效，并覆盖 global custom instructions；Project 可以引用同 Project 的其他聊天作为上下文，具体取决于 memory 设置。

在上述当前官方资料中，没有找到一个可公开依赖的普通 ChatGPT Web “every-response pre-send Skill finalizer hook”。因此，Planner 把无 bridge 自动选择从 release-critical 降为 diagnostic 是合理的；但 Project instructions 也不能被文档本身当作“已证明每轮真实加载某个 Skill”的强 hook，必须由真实 Web Gate 验证。

## Findings

### CW-IP-01 — exact-only bypass 的 ownership 与当前六 Skill 激活机制不一致

**对应要求**

Proposal 3.1/3.2、W0；用户目标是“所有面向用户阅读的自然语言回答默认必须经过 Clear Writing；明确 exact machine / verbatim 输出强制旁路”，且禁止新增 coordinator。

**Observed evidence**

当前 `writing-style` 是一个包含六个独立 Skills 的 plugin。OpenAI 当前 activation contract 是：模型先看到各 Skill metadata，只有请求匹配或直接调用某个 Skill 时才加载该 Skill 的完整 instructions。

当前 `response-clarity` body 的确写有 pure JSON/YAML/code/raw log/verbatim bypass，但 exact-only 请求本身正是它声明“不应使用”的任务。对 `@Clear Writing` 这类 plugin-level 选择，当前官方资料不能证明某个含 bypass 规则的完整 Skill body 一定已经加载。

因此，“插件被显式选择”与“某个具体 Skill 完整 instructions 已加载”不能视为同一件事。若 exact JSON 最终原样输出，它仍可能是因为没有任何 writing Skill 被完整加载，而不是“已加载 Clear Writing 后由 Clear Writing 执行了 BYPASS_EXACT”。

这会让 W0 再次用与旧 Control 03 相同的弱机制取得 PASS，却宣称证明了 stronger loaded-bypass contract。

**Causal risk**

v0.1 把一个当前没有 coordinator owner 的动作描述为“Clear Writing 被加载后自己 route-or-bypass”，容易形成循环证明，并且把 platform-level no-skill selection 冒充 Clear Writing product behavior。

**Minimum closure**

不新增第七 Skill。改清楚 ownership：

- every-turn requirement 只覆盖 **自然语言或 mixed final response**；
- **pure exact-only machine/verbatim request 是 activation exemption**：Project policy 应要求直接保持 exact payload，不必为了形式上“每轮调用”强迫加载 Clear Writing；
- mixed task 仍可加载匹配的 Clear Writing Skill，只处理解释层，机器 payload 精确保护；
- W0 仍必须测 `@Clear Writing` / explicit plugin selection + exact-only 作为 should-not-change stress，但若 surface 没有证据证明某个 Skill full instructions 已加载，不得把该样本描述为“loaded Skill bypass PASS”；只能证明“显式选择 plugin 不应污染 exact output”。
- 若当前 Web surface 真能直接调用具体 Skill 并证明 full instructions loaded，可额外做 direct-Skill exact-output diagnostic；它不是新增 release Gate。

### CW-IP-02 — W1 目前把“Project instructions 生效”误写成“Project setting 已证明触发 plugin”

**对应要求**

W1 要证明 Project setting 而不是用户每轮手工 `@` 成为真实 normal entry。

**Observed evidence**

官方 Projects 文档证明 Project instructions 在 Project 内生效并覆盖 global custom instructions；官方 Plugins/Skills 文档证明 relevant auto-use / direct invocation。没有当前官方资料承诺“Project instruction 中写了调用某 plugin”就能提供一个强制每轮 plugin invocation hook，也没有公开普通用户逐轮 Skill invocation receipt contract。

Proposal 当前只写“surface 能提供时记录 invocation evidence”。这意味着没有 invocation evidence 时，W1 仍可能只凭最终文本 PASS，却继续声称“Project setting 是 activation owner”。

**Causal risk**

最终输出看起来符合 Clear Writing，可能来自 Project baseline、本轮模型随机性、前文上下文或真正的 plugin consumption。若 W1 单独宣称 activation causality，会把行为结果与加载机制混在一起。

**Minimum closure**

把 W1 的 claim 降到它真实能证明的范围：

- W1 证明 **Project-setting policy 下，无每轮手工 @ 的长期行为可靠性**：多轮中持续得到目标 route/bypass/语言恢复结果；
- 如果 surface 有直接 invocation/load evidence，附加记录；
- 如果没有，W1 不单独声称“已证明 plugin 每轮加载”；
- plugin 的因果增量由 W2 matched comparison 关闭；只有 W2 或直接 load evidence 支持时，才能把改善归因给 plugin；
- W1 FAIL 仍可说明 Project-setting policy 不可靠，但 W1 PASS alone 不能证明 plugin causality。

### CW-IP-03 — W2 允许“有混杂的次优设计”继续，且没有冻结跨 arm memory/session 隔离

**对应要求**

W2 是本轮最关键的 plugin-vs-setting-only 因果 Gate；唯一实质差异必须是 candidate availability/consumption。

**Observed evidence**

Proposal 已正确要求两边 Project setting 文本一致，但写道：若无法构造合法 matched environment，Planner 可以改用“次优但明确标注混杂的设计，或停下”。

这对于 release-critical W2 不够严格。一个已知存在混杂的 fallback 不能证明 plugin incremental value。

此外，OpenAI 当前 Projects 文档明确说明 Project 可以使用本 Project 的聊天和文件作为后续回答上下文；Pro/Plus 等还可能引用 Project 内其他聊天，取决于 memory 设置。若 treatment/control 在同一 Project 或有交叉可见的历史中顺序执行，control 可能继承 treatment 的表达模式，反之亦然。此时“plugin availability 是唯一差异”不成立。

**Causal risk**

- confounded fallback 可能被误判为 plugin increment PASS；
- Project memory / previous chat contamination 可以把 treatment 学到的行为带进 control；
- 顺序、模型、attempt count、conversation state 的差异也可能替代 plugin availability 解释结果。

**Minimum closure**

W2 必须冻结为严格 matched evidence：

- 两 arm 使用相同 Project-setting bytes、同一模型/surface、同一预冻结任务、同一 attempt budget、同一 rubric；
- arm 之间使用 fresh isolated conversation context；不得让一 arm 读取另一 arm 的输出/聊天。若使用 Projects，必须冻结并记录 memory mode，并选择能防止 cross-arm contamination 的结构；
- plugin availability/consumption 是唯一实质变量；不得把 Skill 正文复制到 control；
- 不得挑赢家、重复到成功或改变 task order/rubric；
- 如果当前 ChatGPT 产品表面无法合法建立这个 matched condition，则 **W2=INCONCLUSIVE，release 停止**。已知混杂的替代设计只能做 diagnostic，不能替代 W2 PASS。

同一修订还应把 G7 freeze identity 补齐：至少冻结实际 Web plugin/release identity、Project bridge exact bytes、Web surface/model、Project memory mode、attempt budget、fresh task set、rubric/Reviewer input 与 stop condition，防止跨候选或跨上下文拼证据。

## Non-blocking conclusions

### A / F — 主正常入口与原 A/E 降级方向正确

OpenAI 当前公开合同确实只承诺相关时自动使用、或显式选择；没有文档支持“安装后每条请求必跑”。因此，对“采用 Clear Writing 的 Project”而言，把 no-bridge auto-selection 降为 metadata/discoverability diagnostic 是合理的。

这不代表 Project-setting every-turn policy 已经有效，只代表它值得进入后续 Web 验证。

### B — 不需要新增 coordinator

目前没有证据证明六 Skill 架构必须增加第七 coordinator。先把 activation exemption、Skill load 与 plugin selection 的语义写清，再测试现有六 Skill 足够合理。

### G — fresh G7 的问题方向正确

G7 应验证 frozen Project policy 下的 fresh routing、mixed payload protection、语言恢复、sibling switching、fidelity 和 incremental value。所有 KR-WEB-01..09、旧 controls、W0/W1/W2 开发样本均不得再算 fresh。

## Scope and claim boundary

本 REVISE：

- 不否定 `fd7a1578...`；
- 不重开 KR-WEB-01..09 / should-not-change；
- 不要求现在修改 production；
- 不授权 Project setting / ChatGPT account / plugin mutation；
- 不实施 PIE、Mica、Research Authoring 或 Presentations；
- 不新增 Skill/router/state machine；
- 不执行任何 Web Gate 或 G7。

Issue #13 已是当前 canonical tracking Issue，仍应保持 `DOING` / `area:writing-style`。本轮不创建新 tracking Issue。

下一步只允许 Planner 产出 proposal v0.2，关闭 CW-IP-01..03，再回独立 Critic 复核。