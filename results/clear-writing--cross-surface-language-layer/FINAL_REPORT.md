# Final Report

## What this task solved

本任务已经把 Clear Writing 的跨端候选从“只有规则和局部测试”推进到一个可真实回放、可完整跑 CI 的仓库候选。

已确认的成果包括：

- 新增并实际消费 `response-clarity`，用于普通面向用户的解释、诊断、建议、进度和结果说明；
- 原五项 writing-style 技能及其职责保持不变；
- 2026-10-14/15 暴露的 RW-WEB-01..05 五个真实网页失败模式已经冻结为已知回归，并在当前产品源码身份上全部通过；
- RW-WEB-03 正向控制仍保留具体例子、因果解释和不确定性，说明当前机制没有把“清晰”退化成固定短答；
- 四类 should-not-change 控制全部通过：完整合同不被压缩、真正有分支价值的流程保留结构、纯 JSON 精确旁路、正式名称和机器字符串不被错误中文化；
- 先前阻塞任务的仓库级版本/TODO/generated parity 问题已经恢复，当前完整 GitHub CI 通过。

但是，本轮第二次独立 Reviewer **没有批准产品进入最终 Web 验收**。最新真实用户反馈暴露了一个当前普通回复路线的通用合同缺口：复杂科研解释仍缺少明确的“按完整语义单元组成自然段”要求，也缺少陌生方法、数学对象和多重下标符号在公式前先建立 reader mental model 的要求。当前 5 个回放任务没有覆盖这种复杂科研解释，所以现有证据不足以支持 Product / Artifact PASS。

因此当前结论是：**仓库恢复和已知回归修复成功，但 Clear Writing 普通科研解释合同仍需一次新的有界修复。**

## What changed

Clear Writing 当前候选已经包含第六项 `response-clarity` 技能，并保持 `writing-style` 的其余技能名称和职责不变。

恢复阶段只对 `response-clarity` 做了一个有证据驱动的最小生产修复：

- 当用户的问题已经回答，后文没有增加新证据、改变决策、补充用户明确要求的实现细节或必要比较时，应停止继续扩写；
- 多来源综合先说明来源共同支持什么、关键差异是什么、哪些结论仍无支持；
- 助手自己的进一步建议必须与来源共识分开表达，不能把建议包装成来源已经共同确认的结论。

这项修复直接关闭了原 RW-WEB-05“综合回答自动膨胀成小型架构文档”的失败，同时没有破坏 RW-WEB-01..04。

仓库级恢复同时修复了此前阻塞全仓 CI 的版本断言、插件 TODO 集合假设和生成层来源一致性问题；最终 generated layer 可由正式生成器干净重建。

本轮审查没有修改 production candidate。2026-10-16/17 新增的 DII 正反例只作为 Reviewer 的真实覆盖证据使用，没有拿来调当前候选，也不会被冒充为 G7 fresh evidence。

## New capabilities / behavior

当前候选已经能够在实际 Codex candidate replay 中表现出以下行为：

- 普通状态说明先告诉用户“现在能不能做、意味着什么、是否需要动作”，而不是先堆日志、路径和内部状态；
- 当原回答判断前后矛盾时，能够指出缺失的证据并给出保留不确定性的直接改写，而不是长篇自我检讨；
- 对需要解释的概念可以保留必要类比、具体场景、因果关系和未知边界，不会因为“清晰”而机械压成三句话；
- 简单线性流程可以压成自然语言，不为展示内部模块名而制造大面积代码框/箭头结构；
- 多来源综合能够把来源共同事实、来源差异和助手建议分层；
- 完整合同、执行步骤、精确 JSON、正式产品名、命令、路径、提交号和状态值不会因为语言优化而被错误压缩或改写。

正式长 Markdown / 科研文档仍由 `chinese-prose` / `scientific-rewrite` 拥有。它们已有连贯段落、普通英文中文化、`METHOD_MENTAL_MODEL`、`FORMULA_WALKTHROUGH`、公式附近符号解释和 Reader Plan 等文档级机制；普通 ChatGPT 科研解释则仍由 `response-clarity` 负责。

## Deliberately not adopted / unchanged

本任务没有采用以下快捷方案：

- 没有禁词表、英文比例、标题数、段落数、行数、固定答案长度、箭头禁令或代码框禁令；
- 没有把五个已知网页案例重新包装成 G7 未见样本；
- 没有用缩窄测试、删除测试、允许 known failure、伪造版本提升或隐藏 generated diff 来取得 CI PASS；
- 没有让 `response-clarity` 接管正式中文报告、科研长文结构重写、产品 UI 语义或 Research Authoring / Presentations 的专业职责；
- 没有实施 PIE 0.2；
- 没有创建/更新个人 ChatGPT Clear Writing 插件，没有付费 API 调用，没有执行 G1 A/E、B/C matched comparison，也没有执行 G7；
- 没有正式发布 `writing-style 0.5`，没有把本任务合并到 `main` 或移动 `release`。

## Example usage

当前已经有真实 candidate replay 支持的普通用法包括：

- “这个任务现在能不能交付？我需要做什么？”——先给完成/未完成判断，再给必要状态和下一步。
- “这段回答前后矛盾在哪里？”——定位证据不足和判断变化，直接给更有信息量的替换表述。
- “为什么功能开关不能替代回滚方案？”——保留类比、两个场景和未知边界，而不是只给一句定义。
- “三份来源共同说明什么、差异在哪里，我现在该不该改流程？”——先综合证据，再单独给助手建议。

尚不能据本轮证据宣称已经通过的典型用法包括：

- 长篇复杂科研解释在普通 ChatGPT 回复中稳定使用自然语义段落，而不是一句一段；
- 第一次出现复杂方法、数学对象或多重下标符号时，稳定先说明“它是什么、处于哪一层、为什么需要、算出来以后做什么”，再进入正式公式；
- ChatGPT Web 在没有显式 `@Clear Writing` 时稳定自动选择并消费该能力。

这些项目当前均为 **NOT_YET_RUNTIME_VERIFIED**。

## Regression and remaining limitations

第二轮独立 Reviewer 确认：

- RW-WEB-01..05：当前候选实际 replay 全部 PASS；
- RW-WEB-03 正向控制：PASS，必要例子、因果解释和不确定性仍在；
- 四组 should-not-change：全部 PASS；
- source/generated response-clarity 身份一致；
- 全仓单元测试：342 / 342 PASS；
- Marketplace 生成、校验、freshness、skills validate/audit：PASS；
- GitHub CI run `38838231833`：全部四个 job PASS。

但 latest main 的 2026-10-16/17 DII 真实反馈暴露了当前普通回复合同中未被上述运行时证据覆盖的通用问题：

1. `response-clarity` 只有 “Prefer concise paragraphs” 和“列表只在真正并列时使用”等原则，没有明确要求相邻句子按完整语义/推理单元组成自然段，也没有整篇检查“一句一段、标题/公式碎片化造成纵向阅读负担”的合同。对真实反馈中反复出现的过度断行问题，这只是**部分概念覆盖，尚不足以作为稳定机制**。
2. `response-clarity` 没有明确规定复杂科研解释在陌生方法/术语/公式前先建立读者 mental model，也没有规定多重下标对象第一次出现时说明对象层级、各下标角色、估计/已知状态、用途和后续流向。正式文档路线已有类似能力，但普通聊天明确不由 `chinese-prose` / `scientific-rewrite` 接管，因此不能用文档技能的合同代替普通回复合同。
3. “普通英文概念应中文化、正式方法名/机器字符串保留”在当前 `response-clarity`、`chinese-prose`、`scientific-rewrite` 中已经有语义规则覆盖，不需要新增禁词表；但 DII 中 `patient structure`、`feature memory` 等真实复发样本没有本轮 candidate runtime replay，状态仍是 **NOT_YET_RUNTIME_VERIFIED**。
4. 正式长 Markdown / scientific rewrite 的段落、英文和公式解释职责归属是正确的；本轮没有证据显示需要让 `response-clarity` 接管文档重写。

最小后续修复应只补普通回复路线的两个语义要求：按完整推理单元组成自然段并检查整篇碎片化；对陌生科研对象/方法/符号先建立不越权的读者模型，再给正式术语或公式。不得将这些要求实现成固定段落长度、标题上限、公式数量、英文词表或 DII 专用规则。

由于这是第二轮 Reviewer 的 `REVISE`，Reviewed Handoff 自动审查预算已耗尽。任务进入人工决策门，不能自动开启第三轮修复。若用户选择继续，应启动一个新的、明确有界的后续修复周期，并把上述已暴露 DII 材料当作 known regression，而不是 G7。

即使该缺口以后关闭，后续仍必须完成真正的 ChatGPT Web matched comparison（A/E、B/C）、实际自动调用证据和冻结的 fresh G7；本轮 repo/CI PASS 不能替代这些产品门槛。

## Technical appendix

- Task: `clear-writing--cross-surface-language-layer`
- Reviewed branch: `reviewed/clear-writing--cross-surface-language-layer`
- Implementation commit: `c9ccd80ab428aa1b7c8679bef089f082f8fcf05f`
- Reviewer handoff head before round 2: `f5f6f5faa8c57c12bc96967a939d74ec301d3b22`
- Product source used by the post-repair runtime replay: `245d2f3f819c3dc333ee0dc6474832bf5e1ef6f1`; its `response-clarity/SKILL.md` blob is identical to the implementation commit (`13b7f6e683434c0a565386f3ce558c3decb71422`).
- Known-regression evidence: `results/clear-writing--cross-surface-language-layer/web-regression-post-repair/245d2f3/`
- Should-not-change evidence: `results/clear-writing--cross-surface-language-layer/should-not-change/245d2f3/`
- Real Web feedback source: latest `main` `docs/plugin-todos/writing-style.md`
- GitHub CI: `38838231833`, head `dcf6acef7972e0a6c6a0fa623140de683c22040d`
- CI: 342 unit tests PASS; Marketplace generation/check, generated cleanliness, skill validation/audit, Windows sparse checkout, Windows/Linux editable-install smoke all PASS.
- Review round 2 decision: `REVISE`
- Product state after review: **not released; Web automatic activation / G1 / G7 / PIE 0.2 remain unverified or out of scope**.
