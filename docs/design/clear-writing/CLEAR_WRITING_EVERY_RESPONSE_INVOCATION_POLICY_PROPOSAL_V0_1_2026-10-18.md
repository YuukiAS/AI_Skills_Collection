# Clear Writing 每轮强制调用策略与 Web Gate 修订提案 v0.1

日期：2026-10-18  
状态：PLANNER_PROPOSAL_FOR_CRITIC  
对象：`writing-style / Clear Writing`  
当前已通过候选：`fd7a1578a5042a46a55c5b638f6d550655b1096b`  
当前独立实现审查终态：`fd0ad0603309fae52b3af0f9f7cdd7f31adea4b4`

## 1. 本轮为什么要改正常入口

当前 repo/Codex 候选已经通过九组 known regression、四组 should-not-change、full CI 和独立产品/产物审查。新的未决问题不再是 `response-clarity` 内容质量，而是 **ChatGPT Web 到底怎样稳定消费 Clear Writing**。

OpenAI 当前官方资料明确说明：已安装 Skill 通常由模型根据 metadata 与用户目标判断是否相关并加载；插件也通常在“与请求相关”时自动使用。Project instructions 则只在对应 Project 中生效，并优先于全局 custom instructions。

因此，若产品目标是“在采用 Clear Writing 的 Project 中，每一条面向用户的最终回答都经过统一阅读层”，仅把希望寄托在模型判断“这一轮是否相关”并不足以形成强正常入口。自动选择仍有价值，但它是平台 best-effort routing，不是本产品可以自行保证的 every-turn contract。

本提案判断：**在采用 Clear Writing 的 ChatGPT Project 中，正式正常入口应改为 Project-setting enforced invocation；模型自主自动选择退为辅助/诊断入口。**

该判断只针对采用该 bridge 的 Project。它不声称任意非 Project chat、其他账号、未安装插件或其他 surface 都能全局强制每轮调用。

## 2. 已验证事实与当前冻结边界

已经成立：

- `clear-writing--scientific-explanation-readability-repair` 独立 Reviewer 给出 PROCESS PASS + PRODUCT / ARTIFACT PASS；
- production implementation 为 `fd7a1578...`；
- KR-WEB-01..09 PASS；
- 四组 should-not-change PASS；
- current `response-clarity` 已明确普通解释、正式文档 sibling route、pure machine output bypass 和 exact-string preservation；
- 现有 Clear Writing 包含六个既有 skill：
  - `writing-fidelity`
  - `response-clarity`
  - `scientific-prose`
  - `product-ui-copy`
  - `scientific-rewrite`
  - `chinese-prose`

本轮不重新讨论六技能职责，不修改上述 production candidate，不改 Project setting，不改 ChatGPT 账号/插件，不碰 Mica，不碰 Research Authoring / Presentations。

## 3. 新的正常入口职责分工

### 3.1 Project setting：负责“每轮必须经过 Clear Writing”

Project setting 的职责只有 activation policy，不复制 Clear Writing 的风格规则。

拟冻结的产品语义是：

> 对每一条面向用户的最终回答，都要求调用 Clear Writing；由 Clear Writing 根据任务选择既有合适 skill，或对 pure JSON/YAML/code/raw log/verbatim/exact machine output 做精确旁路。Project setting 不重新实现 Clear Writing 规则。

这里的“每一条面向用户的最终回答”不包括纯内部 tool call / hidden reasoning / machine-to-machine intermediate payload；它只约束最终发给用户的回答。

Project setting 不能替 Clear Writing 决定具体改写，也不能声称插件未加载时“已经运行 Clear Writing”。

### 3.2 Clear Writing：负责 safe-to-invoke-on-every-user-facing-response

Clear Writing 的产品合同从“某些写作任务可调用”提升为：

> **当 Clear Writing 已被 Project setting、用户显式调用或其他合法入口加载时，它必须对任何最终用户回答做安全的 route-or-bypass 决定。**

这不等于所有任务都使用 `response-clarity`。现有六技能职责继续有效。

最小 route-or-bypass 语义：

1. **普通解释 / 诊断 / 建议 / 结果说明**  
   使用 `response-clarity`。

2. **正式中文文档 / README / 报告 / Markdown/PDF final pass**  
   使用 `chinese-prose`。

3. **中文或中文主导科研技术材料的 source-faithful 结构重写**  
   使用 `scientific-rewrite`。

4. **英文科研 prose**  
   使用 `scientific-prose`。

5. **产品 UI microcopy**  
   使用 `product-ui-copy`，前提是上游产品语义已冻结。

6. **pure JSON / YAML / code / command / raw log / verbatim / exact machine output**  
   **BYPASS_EXACT**：不润色、不加前言、不加解释、不改变空格/字段/代码；若用户只要求 exact payload，最终回答只返回 exact payload。

7. **混合任务**  
   机器 payload 原样保留，只处理其周围允许改写的解释性文字。

本提案不新增第七个 coordinator skill，不新增 router/state machine。首先用当前 frozen candidate 的真实 Web 行为验证：显式/强制加载 Clear Writing 时，模型是否能根据现有六 skill metadata 与合同完成上述 route-or-bypass。只有真实失败才允许后续提出最小 production repair。

### 3.3 不允许 Clear Writing 声称能“自我强制激活”

Skill 的正文只有在平台已经选择/加载后才有执行效力。Clear Writing 可以做到“被调用后对任何用户输出安全”，但不能在尚未加载时保证自己被调用。

因此：

- every-turn activation owner = Project setting；
- route / fidelity / bypass owner = Clear Writing；
- platform automatic selection = fallback / diagnostic；
- Mica = 完全 out of scope。

## 4. 为什么这比原 G1 更适合作为正式正常入口

原跨端设计的 G1 把“无 bridge 时模型能否自动选中 Clear Writing”作为核心 release 证据。这个测试能测 discoverability，但与新的产品目标并不一致：

- 产品真正要的是每轮 reader-facing output 都过统一阅读层；
- 模型自动选择只保证“相关时可能加载”，不是 every-turn contract；
- 如果 Project setting 本来就能明确要求调用 Clear Writing，那么把“无 bridge 自动选中”继续当 release blocker，会把平台启发式 routing 当成产品主机制。

因此修订如下：

- **原 A/E 无 bridge 自动选择保留，但降级为诊断信息，不再是正式产品成功必要条件。**
- 正式 release-critical G1 改为：**Project-enforced every-turn invocation + Clear Writing universal safe routing/bypass + matched incremental value**。

## 5. Revised Web Gate

### Gate W0 — frozen-candidate universal-invocation safety

这是第一道门，必须先于 matched comparison。

目的：证明当前已 PASS 的 frozen candidate 在“每轮都显式要求/强制调用 Clear Writing”时不会破坏合法输出。

同一 frozen candidate，不做 production edit。至少覆盖以下真实 Web 任务族：

1. 普通技术解释；
2. 复杂科研解释；
3. 陌生方法 / 多重下标对象；
4. 必要长答；
5. 临时英语回答，然后下一轮恢复默认中文；
6. 完整 executable prompt / contract；
7. 真正有分支价值的流程；
8. pure JSON exact output；
9. pure YAML exact output；
10. pure code exact output；
11. raw log / verbatim；
12. exact identities：命令、路径、字段、状态、commit、产品名。

其中 8–11 是新的关键证据。此前 pure JSON should-not-change 是通过“不加载 Clear Writing”获得 PASS；这不足以证明 universal invocation 安全。

**必须新增一组“已明确加载 Clear Writing / 明确 @Clear Writing 或等价显式调用，同时请求 exact output”的 Web 证据。** PASS 要求：

- Clear Writing 确实进入当前请求的已加载/显式调用状态；
- 最终 pure payload 与输入/要求 byte-content 等价；
- 不出现“已帮你保持原样”之类前言；
- 不因为插件被加载就错误调用 `response-clarity` 改写机器内容。

若该 Gate 失败：

- 停止 Project-setting every-turn rollout；
- 不继续 matched comparison；
- 回 Planner/Critic 只做现有六技能/metadata 内的最小 safe-invocation repair；
- 禁止新增第七 skill/router，除非新的独立设计证明现有六技能结构客观无法承担。

### Gate W1 — Project-setting enforced normal-entry proof

目的：证明真实 Project 内无需用户每轮手工 @，Project setting 能稳定触发 Clear Writing。

使用测试专用 Project setting bridge，内容只表达 invocation，不复制 style contract：

> 对每条面向用户的最终回答，调用 Clear Writing。由 Clear Writing 决定使用其现有合适写作能力或对 exact machine output 原样旁路；不要把所有任务都交给 response-clarity。

在连续多轮中覆盖 W0 的主要任务族，至少包含：

- 普通解释 -> exact JSON -> 普通解释；
- 中文 -> 临时英文 -> 中文恢复；
- 短答 -> 必要长答；
- explanation -> executable prompt/contract。

PASS 不仅看最终文字，还要看：

- surface 能提供时记录 Clear Writing/plugin invocation evidence；
- exact bypass 后下一轮仍能恢复普通 Clear Writing 路由；
- temporary English 不污染后续默认语言；
- 一个 turn 的 sibling route 不粘滞到后续不相干任务。

这道 Gate 证明“Project setting 是正常 activation owner”，不证明插件相对 Project setting 的增量。

### Gate W2 — forced-invocation matched increment

目的：证明 **Clear Writing 本身**相对于“只有 Project setting”有增量，避免把 Project setting 本身的写作效果冒充插件效果。

优先实验设计使用**完全相同的 Project setting 文本**，包含：

- 共同的短 Project reader baseline；
- 一条测试专用 availability-aware invocation bridge：

> 对每条面向用户的最终回答，如果当前已安装并可用 Clear Writing，则调用它并遵循其 route/bypass；若不可用，不得模拟或重建 Clear Writing，只按本 Project 其余规则回答。

Matched pair：

- **T — Plugin arm**：同一 Project setting + frozen Clear Writing candidate 可用；
- **C — Setting-only arm**：同一 Project setting + Clear Writing candidate 不可用；不得复制 Clear Writing skill 正文到 Project setting。

这样两边 Project setting 文字完全一致，唯一实质差异是 Clear Writing 是否真实可用/可消费。

如果 ChatGPT 当前产品面无法构造“相同 setting、仅 plugin availability 不同”的合法 matched environment，则该 Gate 不能伪装为已完成。Planner 必须改用次优但明确标注混杂的设计，或停下取得可比较环境。

评价时：

- 只把超出共同 Project baseline 的稳定改进归因于插件；
- treatment 必须在多个任务族稳定减少已知阅读失败；
- 不能以一次 prettier answer 或自报“用了 Clear Writing”算增量；
- control 如果已经同样好，说明 Project setting 可能已足够；此时不得为了证明插件价值而修改评分标准。

**停止条件**：若 Clear Writing 在 forced-invocation 模式下对 setting-only control 没有稳定可见增量，或为了增量明显伤害 exact/bypass/long-answer 控制，则停止 release，回 Planner 简化产品定位；不得移动终点。

### Gate W3 — 原 A/E 自动选择诊断

保留原“candidate 可用但无 Project bridge vs candidate 不可用且无 bridge”的自动选择试验，只回答：

- metadata discoverability 如何；
- 没有 Project enforcement 时模型是否偶尔/稳定自动选中；
- Project bridge 是否显著提高 invocation reliability。

**W3 不再是 release blocker。** 即使 W3 自动选择不稳定，只要 W0/W1/W2 和后续 G7 通过，Project-enforced normal entry 仍可成立。

## 6. Fresh G7 修订

G7 不取消，但成功问题改变。

旧问题偏向：
> 模型能否自动发现并选择 Clear Writing？

新问题变为：
> 在 frozen Project-enforced invocation policy 下，Clear Writing 对未见用户任务是否同时做到正确 route、正确 bypass、可读性增量和零语义漂移？

进入 G7 前必须冻结：

- frozen production candidate；
- frozen Project bridge 文本；
- W0/W1/W2 评分规则；
- fresh task 集与数量；
- Reviewer 输入和停止条件。

G7 fresh 集必须包含此前 known bank 没有直接出现的新任务族组合，尤其：

- exact output 与解释混合；
- 长科研解释中嵌 machine payload；
- 临时语言 override 与恢复；
- sibling writing skill 与 ordinary response 的连续切换；
- 明确“不改写”与 normal explanation 的连续切换。

所有已知 KR-WEB-01..09、旧 controls 以及本轮 W0/W1/W2 调试样本都永久排除 fresh G7。

## 7. Capability Gate revision

现有 G0–G7 不重建，仅改 G1 的 release semantics。

| Gate | 新状态/含义 | 是否 release-critical |
|---|---|---|
| G0 distribution | 候选可安装/可识别，保持原定义 | 是 |
| G1a | W0 universal-invocation safety | 是 |
| G1b | W1 Project-enforced every-turn normal entry | 是 |
| G1c | W2 plugin-vs-setting-only matched increment | 是 |
| G1d | W3 no-bridge auto-selection diagnostic | 否 |
| G2 | 已知 response readability regressions | 是，已由当前 candidate 通过 |
| G3 | fidelity / exact bypass | 是，新增“loaded Clear Writing 下 exact bypass”证据 |
| G4 | sibling writing skill ownership 不退化 | 是 |
| G5 | domain consumers | 保持原边界，不在本 revision 扩张 |
| G6 | 多轮/语言模式 | 是，W1 必须覆盖 |
| G7 | frozen forced-invocation policy 下 fresh generalization | 是 |

不新增 G8/G9，不用新的数据库、ledger、router 或 Mica。

## 8. Project setting 的最小正式角色

如果 W0/W1/W2 PASS，后续准备真实 Project-setting integration 时，bridge 应保持很薄：

- 只要求 every-turn invocation；
- 只说明由 Clear Writing 自己 route/bypass；
- 不复制 `response-clarity`、`chinese-prose` 等内部规则；
- 不复制九组回归细节；
- 不声称未加载插件时已经执行；
- 不把 Project setting 变成第二套 Clear Writing。

PIE 是否负责把该 bridge 写入 setting，是另一个项目的实现问题；**本提案只冻结 Clear Writing 的 invocation policy，不实施 PIE。**

## 9. 失败与恢复

### Clear Writing loaded 后破坏 exact output

归因：Clear Writing safe-invocation 产品缺口。  
动作：停止 rollout；只允许 bounded production repair，经 Planner/Critic 后重测 W0 全矩阵。

### Project setting 没有稳定触发插件

归因：activation / platform behavior，不自动归咎 `response-clarity`。  
动作：记录真实 Web evidence；先核查 bridge 是否实际在 Project 生效、插件是否可用。不得通过把所有 style rules 复制进 Project setting 来伪造成功。

### Plugin arm 与 setting-only 无稳定差异

归因：插件增量未证明。  
动作：停止 release；评估是否 Project setting 已足够，或 Clear Writing 只保留显式/专业写作入口。不得挑赢家样本。

### W3 自动选择失败但 W0/W1/W2 PASS

不阻塞 Project-enforced 产品路线。记录为 discoverability limitation，不移动 release target。

## 10. 替代方案比较

### A. 继续以平台自动选择为主正常入口

优点：Project setting 更短，无强制调用。  
缺点：官方合同只是“相关时自动使用”；不能支持“每轮最终回答都必须过阅读层”的产品承诺。  
结论：降为诊断/fallback，不作为主入口。

### B. Project setting 直接复制全部 Clear Writing 写作规则

优点：不依赖插件 invocation。  
缺点：重复规则、难同步、无法复用六技能路由与回归资产，Project setting 会重新变成长期膨胀的第二套产品。  
结论：拒绝。

### C. Project setting 只负责 every-turn activation，Clear Writing 负责 route/bypass

优点：职责单一；能把稳定能力留在 plugin；Project setting 很薄；可以单独比较 setting-only 与 plugin arm；不会要求 `response-clarity` 接管所有任务。  
风险：必须先证明 loaded plugin 对 exact output 等任务安全，而且 Project setting 在真实 Web 能稳定触发。  
结论：**Planner 推荐作为新的正式正常入口，前提是 W0/W1/W2 真实 PASS。**

## 11. 外部资料核查

本轮实际核查 OpenAI 当前官方文档：

1. OpenAI Help Center《Skills in ChatGPT》：安装后 ChatGPT 可以在“有帮助时”自动使用一个或多个 Skills；不同 surface 的安装/运行能力可以不同。
2. OpenAI Developers《Skills》：模型先看到 skill metadata；当用户请求匹配该 skill，或用户直接调用时，才加载完整 instructions。
3. OpenAI Help Center《Plugins in ChatGPT》：已安装插件在“与请求相关”时自动使用，也可由用户直接选择/提及。
4. OpenAI Help Center《Projects in ChatGPT》：Project instructions 只在该 Project 内生效，并覆盖 global custom instructions。

这些官方资料支持本提案的核心边界：**automatic selection 适合相关性 routing，但不能作为 every-turn 强制调用的唯一产品机制；Project instructions 是当前 Project 内更合适的 activation owner。**

## 12. 本轮不做什么

- 不修改 `fd7a157...` production candidate；
- 不改 Project setting；
- 不改个人 ChatGPT plugin/account；
- 不启动原 A/E、B/C；
- 不执行 W0/W1/W2/W3；
- 不执行 G7；
- 不实施 PIE；
- 不碰 Mica；
- 不改 Research Authoring / Presentations；
- 不新增第七 skill/router/state machine；
- 不 release/version bump；
- 不把自动选择失败解释为 response-clarity 内容失败。

## 13. Critic 需要批准的唯一设计判断

Critic 只需判断：

1. 是否应把 **Project-enforced every-turn invocation** 冻结为采用 Clear Writing 的 Project 的主正常入口；
2. Clear Writing 是否应承担 **safe-to-invoke-on-every-user-facing-response** 的 route/bypass 合同，而不是让 `response-clarity` 接管全部任务；
3. W0 -> W1 -> W2 -> W3 的顺序是否正确，其中 W3 仅诊断；
4. W2 是否足以把 Project setting 效果与 plugin 增量分开；
5. G7 是否应改为验证 frozen forced-invocation policy 的 fresh generalization；
6. 是否保持六技能架构、production candidate、PIE、Mica、Research Authoring、Presentations 全部不动直到本 proposal 独立 PASS。

Critic PASS 后，Planner 才能冻结新的 Web Gate execution package。PASS 本身不授权修改 Project setting、账号或 production candidate。
