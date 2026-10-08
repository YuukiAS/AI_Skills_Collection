# Project Instructions Editor 0.1 — 当前指令表面收敛修复 v0.1

Date: 2026-10-07

Status: direct bounded repair design; no new Critic round

Target branch:

```text
work/project-instructions-editor--0.1-closure
```

Current standalone Skill version remains:

```text
project-instructions-editor = 0.1
```

## 1. 这次真实失败是什么

最新 Server+VPS 实际输出没有重新暴露 C11 的同一个问题，而是暴露了 PIE 0.1 范围收缩后的另一个边界错误：

> 把“未来每一轮聊天的最终阅读层不属于 PIE”错误扩大成了“PIE 对自己这一次生成的 Project instructions 的表达、去重和语义密度也几乎不负责”。

结果是：语义保护变得更保守，但最终 Project instructions 比此前已经得到过的较好版本更长、更重复，更像把 source / audit / workflow contract 按来源顺序摊进设置，而不是把它们压缩成长期 Project 规则。

真实表现包括：

- 同一类 canonical ownership / current-source / mutation-authority 规则在多个章节重复出现；
- 用户回答顺序、用户操作、生产任务结束汇报被拆成多层重复约束；
- client completeness 与完整性检查重复；
- production authorization / canonical source / fail-closed 在不同章节重复；
- source 中的 ordinary English labels 被直接拿来组织中文 durable setting；
- 13 个章节不是因为有 13 个独立长期语义，而是因为 source 中有 13 组材料。

这个失败不能全部推给 Clear Writing。

Clear Writing 后续负责的是：

- 未来每一轮 ChatGPT 回答的最终阅读层；
- 多轮英文污染后的恢复；
- 更稳定的普通英文自然化；
- 机械换行、状态腔、日志腔等跨回复表现。

PIE 0.1 仍然必须负责它**当前交付的 Project setting 本身**：

- 不无必要膨胀；
- 不重复长期语义；
- 不把内部 source labels 直接当成 Project 概念；
- 不把易变细节复制到 Project；
- 不发明长期规则；
- 在目标 Project 已明确语言时，以该语言写当前 durable setting；
- 同时保护所有语义不变量。

## 2. 不回到 C5–C11 的错误路线

这次明确不采用：

- 不重新建立逐个 Latin token 的 mandatory exactness pass；
- 不加英文禁词表；
- 不做英文比例；
- 不做固定翻译表；
- 不继续靠“最后再检查一遍普通英文”解决所有语言问题；
- 不重新 vendoring / chaining `chinese-prose`；
- 不要求 sibling Skill 在同一个模型 turn 中形成伪阶段隔离；
- 不恢复 MCP finalizer / external model / API key / hosted service；
- 不创建 C12；
- 不把 Server+VPS 某个词写成特殊规则；
- 不固定 9 节、13 节或任何段落/标题数量。

历史证据保持原判：

- C5：no-op 可绕过真实缺陷；
- C7：历史删除信息可能被改写成新的长期规则；
- C9：更强 prompt-only final self-check 仍会漏普通英文；
- C10：同轮实际消费 chinese-prose 仍不等于真正第二阶段；
- C10-B3：真正独立 stage separation 才能稳定解决当时的 reader-layer failure；
- C11：simple-core 无法可靠承担跨轮/完整 reader-layer guarantee。

因此本次只修**PIE 自己的 instruction-editor 产品职责**，不再次冒充最终阅读层。

## 3. 新机制：先做“长期语义地图”，再写 Project setting

在 drafting 前新增一个内部步骤：

```text
Durable Meaning Map
```

这是内部推理结构，不输出给用户，不写进 Project setting，也不新建数据库/ledger。

对当前任务涉及的每个长期语义单元，至少判断：

```text
meaning
support
semantic owner
Project enforcement need
volatility
protected invariant
disposition
```

其中 `disposition` 只能是：

```text
PROJECT_DIRECT
PROJECT_BRIDGE
SOURCE_ONLY
TASK_ONLY
OMIT
```

含义：

- `PROJECT_DIRECT`：未来任务在 lookup 前就必须知道的长期规则，例如 ownership、授权、安全、隐私、证据强度、用户操作边界。
- `PROJECT_BRIDGE`：Project 只保留触发条件和 locator，详细/current truth 回 canonical source。
- `SOURCE_ONLY`：易变实现、库存、拓扑、端口、脚本、runtime status 等只留 source。
- `TASK_ONLY`：只属于本次任务/临时状态，不进入长期 Project。
- `OMIT`：重复、历史 residue、已删除、无当前支持或无长期价值。

这不是新增 schema，也不需要持久化。它只是防止模型按照 source 段落顺序直接复制。

## 4. 新机制：Semantic Consolidation Pass

在有了语义地图后，不直接逐条写入设置。先做一次语义合并。

核心原则：

> one durable meaning -> one primary home -> one durable expression

不是字符串去重，而是按“规则最终会导致什么行为”去重。

### 4.1 可以合并的情况

如果两条规则：

- 触发条件相同或高度重叠；
- mandatory / optional force 相同；
- authority / owner 相同；
- failure behavior 相同；
- 没有需要分别保留的安全或证据边界；

则优先合并成一个 durable rule。

例如：

- “动态 inventory 先读 canonical source”
- “当前 client/profile/route 不能用 Project 旧清单”
- “端口/脚本/服务名依赖 current source”

本质上可以合并为一条：

> 任务依赖可能变化的实现或运行事实时，先读取当前权威来源或只读实时状态；Project 中的历史清单不能代替当前事实。

不要在三四个章节重复。

### 4.2 不能为了短而合并的情况

以下差异存在时必须分开：

- 不同 owner；
- 不同授权条件；
- 不同 safety boundary；
- 不同 mandatory / optional force；
- 不同 evidence threshold；
- 不同 fail-closed consequence；
- 不同用户动作要求；
- 合并后会让 exact identity 或 trigger 含糊。

语义压缩不能削弱规则。

## 5. 新机制：Surface Expansion Gate

PIE 的默认不是“越完整越好”，而是“最小长期表面足够”。

对 preservation-sensitive 的 broad review / improvement：

- 如果没有新增用户授权的长期语义，candidate 默认不应因为“解释更完整”而显著扩大；
- candidate 比 live setting 更长时，内部必须能给出具体 expansion reason；
- 可接受的 expansion reason 只有：
  1. 当前用户新增了长期要求；
  2. live setting 存在真实 cross-cutting contradiction，需要显式拆开；
  3. 原 setting 缺少必须在 lookup 前生效的 authorization / safety / privacy / evidence rule；
  4. 原 setting 过度压缩到会改变 mandatory force 或 owner；
- “更清楚”“更保险”“把 source 都写进去”“方便以后看”都不是 expansion reason。

不设固定字符比例，也不设“必须更短”的机械指标。

判断问题是：

> 新增长度是否对应新增或被修复的长期语义？

如果不是，就继续合并。

## 6. 新机制：Coverage + Redundancy 双检查

draft complete replacement 后，PIE 不再做 C9/C11 那种 token-oriented reader self-check，而做两项结构检查。

### A. Semantic Coverage

每个 live / user-authorized / current-source-supported 的受影响长期语义必须满足之一：

- 在 candidate 有直接规则；
- 有等价合并规则；
- 被安全 relocation 到 canonical source，并保留必要 Project bridge；
- 用户明确删除；
- 当前任务明确不在 scope。

同时：

- 新 durable rule 必须有 current semantic support；
- deletion/rejection history 只能控制本次编辑，不能自己生成 tombstone；
- exact identities、authorization、privacy、safety、evidence strength、uncertainty、completion state 继续保护。

### B. Redundancy Review

对 candidate 每个 section / paragraph 问：

> 去掉这一段，会丢失哪个独立长期语义？

如果答案只是：

- 前文已经说过；
- 只是换一组 source terminology 重述；
- 只是解释为什么这个规则存在；
- 只是审计/实现过程；
- 只是当前 inventory/status 的一份副本；

则应合并、缩短或移出 Project。

这一步解决的是结构重复，不是固定段落数。

## 7. 当前 Project setting 的语言责任

恢复一个非常窄、不会重开 C11 的 local-artifact contract：

> PIE 不负责保证未来每一轮回答的最终语言，但它负责自己当前交付的 Project setting 不故意照抄普通 source labels。

具体：

- 如果当前 Project durable language 是中文，当前 replacement 的普通解释和普通技术/流程概念优先用自然中文；
- formal product / repository / protocol / command / path / file / field / state / version / exact UI string 等需要精确匹配的字符串保持原样；
- source heading、phase label、audit label、普通 workflow label 不因为来自英文 source 就成为 formal identity；
- 不要求逐 token 完美；
- 一个偶发普通英文 token 不单独阻断 PIE 0.1；
- 但如果 candidate 大面积以 source English labels 组织章节和规则，导致读者看到的是内部合同而不是长期 Project 规则，则属于 PIE 的 current-artifact defect，而不是 Clear Writing 可以完全兜底的问题。

判断层级从：

```text
有没有任何普通英文？
```

改为：

```text
这个 setting 是否已经把 source 的长期意义消化成目标 Project 自己的规则？
```

这样既不重走 C7–C11 的 token chase，也不允许 PIE 用“Clear Writing 以后会处理”逃避当前产物质量。

## 8. 用户可见输出也要收敛

正常 Project-instruction 编辑不默认暴露内部分析标签。

例如 `preservation-sensitive`、`PROJECT_BRIDGE`、semantic owner 等默认只用于内部判断。

用户正常请求“帮我审一下 Project instructions”时，推荐输出：

1. 一两句说明是否建议修改、为什么；
2. 需要时给完整可替换版本；
3. 只说明 2–4 个最重要变化；
4. 有真实用户动作才说明动作。

只有用户明确要求 audit / formal review 时，才输出内部 mode、完整 invariant checklist、状态字段。

这可以减少 PIE 自己的审计腔，不依赖 Clear Writing。

## 9. Server+VPS 这次应如何修

不要对真实文本做“把 13 节压成固定 9 节”的模板化修复。

正确做法是重新建立语义地图，大概率得到这些独立长期主题：

- ownership / routing；
- dynamic facts -> current canonical source；
- user-facing answer / user action contract；
- Clash_Profile 全局 client-delivery integrity + server-first；
- live network mutation authorization；
- automated validation first；
- production mutation source / backup / rollback；
- fail-closed + redundancy；
- completeness + secrets；
- closure reporting。

其中高度重叠的 ownership/current-source/mutation-source 需要合并；answer order/user action/closure reporting 也要避免重复。

最终 section 数量由实际独立语义决定，不由旧版本或新版本的标题数量决定。

## 10. 实现范围

允许修改：

```text
skills/core/codex-system/project-instructions-editor/SKILL.md
skills/core/codex-system/project-instructions-editor/references/editor-contract.md
tests/test_project_instructions_editor_contract.py
tests/fixtures/project_instructions_editor/*
results/project-instructions-editor--standalone-skill-implementation/*
docs/skill-todos/project-instructions-editor.md
必要的 wrapper update handoff / archive metadata
```

只有实际 user-facing source/metadata 改变才同步 registry/catalog/provenance 等派生文件。

不修改：

- Clear Writing production source；
- writing-style version；
- Research Authoring；
- Presentations；
- workflow-core；
- Bridge Kit；
- MCP；
- external API service。

Standalone Skill version仍是 `0.1`，因为这是 0.1 发布前 bounded repair，不提前升 0.2。

ChatGPT personal wrapper 如果需要重新发布，只 bump wrapper package version，例如当前 `0.2.2 -> 0.2.3`；不要改变 Skill version。

## 11. 回归设计

现有 C5–C11 全部只能作为 development regression，不再当 fresh evidence。

新增一个 public-safe structural regression，重点不是词汇，而是：

输入 setting 同时包含：

- 两个 canonical owners；
- 多处重复 current-source rule；
- 多处重复 authorization / user-action rule；
- 一个 volatile inventory；
- 一个 protected deletion history；
- exact machine identifiers；
- 一条 evidence-strength rule；
- 一条 privacy rule。

自然用户请求只说：

> 审一下长期 Project instructions，只做确实必要的修改；需要改就给完整版本。

期望：

- preservation-sensitive；
- 不 no-op；
- 不整体扩张成更多重复章节；
- volatile inventory -> source bridge；
- duplicate durable meanings merged；
- protected absence preserved without tombstone；
- exact identifiers preserved；
- authorization/privacy/evidence unchanged；
- no unsupported durable rules；
- current Project language used for ordinary prose；
- 不通过 exact word list / section count / English count 判 PASS。

这个 regression 的目标是抓“source-to-setting 复制 + 结构膨胀”，不是新的词汇测试。

## 12. 最终真实 Server+VPS acceptance

修复 source -> focused tests -> wrapper update 后，在真实 Server+VPS Project fresh thread 再发送普通自然请求。

只看第一条完整回复。

阻断项：

- live setting 不是 baseline；
- 无理由 full rewrite；
- no-op 漏掉真实结构缺陷；
- candidate 明显扩张但没有新增长期语义；
- 同一 ownership / current-source / authorization / reporting 语义多次重复；
- volatile detail 仍大段固化；
- deleted/rejected rule 或 deletion-history tombstone 回来；
- unsupported durable rule；
- authorization/privacy/safety/evidence/completion/exact identifiers 漂移；
- 系统性 source-label echo 使 setting 仍像内部审计合同而不是长期 Project 规则。

非阻断项，转交 Clear Writing #13：

- 单个或少量普通英文 token；
- 个别句子还不够地道；
- 未来多轮聊天是否持续中文；
- 跨轮机械换行/日志腔；
- future-answer finalization。

如果真实 candidate 在结构上与此前较好的 compact Server+VPS setting 同等级或更好，并且保真成立，则 PIE 0.1 可以 release。

## 13. Stop rule

如果这次 repair 又演变成：

- 为某几个英文词新增规则；
- 再做 mandatory Latin-token scan；
- 再加一个 final self-check；
- 再引入 chinese-prose 同轮 helper；
- 再引入外部 finalizer；
- 再针对 Server+VPS 特判；

立即停止。

这意味着实现已经偏离本次修复目标。

本次唯一要新增的真实能力是：

> PIE 能把复杂 source/history/setting 消化成更小、更少重复、语义保真的长期 Project surface；当前 setting 本身应该像一份 Project 规则，而不是 source/audit contract 的展开副本。
