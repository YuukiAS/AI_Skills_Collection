# Project Instructions Editor 0.1 收口 Goal

你现在负责在 `YuukiAS/AI_Skills_Collection` 把 **Project Instructions Editor（PIE）standalone Skill v0.1** 收口。用户明确要求本轮**不走新的 Critic**；这是既有方案的范围收缩与发布整理，不是新架构设计。

## 最终目标

把 PIE 0.1 诚实地发布为：

> 一个可在 ChatGPT Web / Project 场景使用的 Project instructions 编辑器，负责创建、修改、压缩、同步、重构和重置长期 Project instructions，并保护现有设置、用户已接受/删除/拒绝的决定、事实来源、权限/安全/证据边界、精确标识、有限字符预算和正确的规则归属。

PIE 0.1 **不再承担**“保证以后每一轮 ChatGPT 回答都持续自然中文、无非必要英文、无机械换行”的跨轮最终阅读层责任。C11 已证明这不是当前 PIE 单独可靠提供的能力。该能力后续归 Clear Writing 下一版；PIE 后续 0.2 只做很薄的接入，不在本轮实现。

## 第一优先级：保护用户本地未同步修改

开始前先检查所有与 PIE 相关的本地 worktree / branch / dirty files，尤其：

- 根 `README.md` 的用户已要求重排/改写但尚未同步远端的版本；
- PIE 新 SVG icon；
- 任何已经完成但尚未 push 的 README、icon、catalog/metadata 修改。

**禁止**在确认和保存这些内容前执行 `reset --hard`、清理 dirty worktree、强制 checkout 或覆盖文件。先做备份/patch/临时 commit，再继续。

远端已经有旧实现分支：

`work/project-instructions-editor--standalone-skill-implementation`

它已经严重偏离当前 `main`，**不要整分支 merge/cherry-pick**。只把它当历史来源，按文件/提交选择性取回需要的 PIE 0.1 能力和用户已认可的 README/icon。

当前用于干净收口的远端分支已经创建：

`work/project-instructions-editor--0.1-closure`

先 fetch，确认它基于最新 `main`；如 `main` 已推进，安全更新收口分支到最新 `main` 后再工作。

## PIE 0.1 冻结范围

必须保留/实现：

- explicit Project-instruction create / update / compress / sync / restructure / reset 路由；
- preservation-sensitive / greenfield / explicit reset 三类编辑模式；
- live Project setting 优先于旧候选/旧摘要；
- 只读取与当前修改相关的 history，保护用户明确接受、删除、拒绝、纠正；
- canonical source 与 Project-resident rule 的所有权/定位判断；
- bounded edit 默认优先，只有真实跨域冲突/广泛污染/预算问题等才整体重写；
- protected absence：历史里被删除/拒绝且 live setting 已不存在的规则不得自动复活；
- mandatory/optional、权限、安全、隐私、证据强度、不确定性、完成状态、当前/未来、精确机器身份等语义不变量；
- 有实际预算时做长度/余量判断；
- 缺 live baseline / source / authority 时诚实降级，不假装安全完整替换；
- 普通 ChatGPT Web 自然请求能路由到 PIE；近似普通写作/科研改写/全局 Custom Instructions 不抢路由；
- v0.1 SVG icon、catalog/registry/provenance/README/测试一致。

本轮明确移出正式能力声明：

- 跨多轮对话的最终用户阅读层保证；
- “以后每一轮都必须自然中文”的运行时保证；
- C11 reader-baseline 作为发布 Gate；
- Server+VPS 中文首答作为 PIE 0.1 release blocker；
- sibling Skill 链、MCP finalizer、外部模型、`OPENAI_API_KEY`、额外托管/付费调用；
- C12；
- 新的英文禁词表、比例评分、固定段落模板。

PIE 仍可以按用户当前语言要求写出自然、紧凑的 Project instructions，但这只是当前编辑产物质量，不得宣传为“它能保证 Project 以后所有回复跨轮都持续执行最终阅读层”。

C11 的失败证据必须保留，不能改写成 PASS；在 release notes 中把它记录为明确的能力边界/后续 Clear Writing owner。

## 实现基线

选择性参考旧实现中已经成立的简单编辑器核心；不要直接发布 C11 最终候选 `187212887bc8f7a339cd43097384df35c1e71baf`，也不要把 C10/C11 的 helper/finalizer/reader-baseline 复杂度继续带进 0.1。

需要你基于当前源码做最小收敛：删掉或改写会让 PIE 0.1 被误解为“跨轮最终阅读层 owner”的运行合同和测试；保留真正属于 instruction editor 的语义保护。

## README / icon

用户特别要求把本地已经改好的 README 与新 SVG icon 真正同步远端。

README 要基于**当前 main 最新内容**合并，不得把旧分支的过期版本号或旧插件状态覆盖回来。最终 README：

- 保留用户已认可的新版重排；
- 在“可单独安装的技能”中正式展示 Project Instructions Editor v0.1，不再写“开发中”；
- 说明它做什么，不宣传 C11 已失败的跨轮中文保证；
- 若说明 ChatGPT Web 分发，明确 personal skills-only Plugin 只是分发封装，能力来源仍是 standalone Skill；
- 普通正文使用自然中文，保留真正需要精确匹配的产品名、slug、路径、版本等字符串。

根据仓库 `AGENTS.md`，只要修改根 README，结束前必须**实际调用当前安装的 Clear Writing**检查受影响读者区域；不能只读 `SKILL.md` 或声称“已检查”。

新 SVG icon 必须成为 PIE standalone Skill 的正式 icon source，并同步所有需要引用它的 README / contact sheet / wrapper/package 元数据；不要重新设计用户已经认可的 icon，除非文件损坏或格式不合法。

## 版本与发布

读取当前：

- `AGENTS.md`
- `docs/workflows/PLUGIN_VERSIONING_AND_CHANGELOGS.md`
- 与 standalone skill release 直接相关的现有测试/生成脚本

按当前政策决定 repository release bump。PIE Skill 自身版本固定为：

`project-instructions-editor = 0.1`

不要因为历史私人 ChatGPT wrapper 已有自己的封装版本号而改变 Skill 版本。wrapper version 与 Skill version 分开处理。

同步所有真实派生面：`registry.json`、`docs/SKILL_CATALOG.md`、`docs/SKILL_PROVENANCE.md`、provenance audit、README、contact sheet、必要测试和 CHANGELOG/VERSION。优先使用仓库现有生成/校验路线，不手工制造与生成器冲突的快照。

## 验收

必须验证的是 PIE 0.1 的真实编辑器能力，不再重复 C11：

1. 自然请求能触发 PIE；近似普通写作不误触发。
2. preservation-sensitive：有 live setting 时做安全 bounded edit。
3. missing live setting：不能伪造完整替换。
4. protected absence：用户删除/拒绝内容不会从历史中复活。
5. canonical-source locator：不把易变实现细节全部复制进 Project instructions。
6. 语义保真：权限、安全、mandatory/optional、证据强度、完成状态、精确标识不漂移。
7. greenfield / explicit reset 正常工作。
8. icon、metadata、registry/catalog/provenance、README、版本完全一致。
9. README 经真实 Clear Writing 检查。
10. 不运行 Server+VPS reader-baseline Gate，不创建 C12，不用旧失败样本重新证明“终审终于稳定”。

如果当前环境能够核对已有 ChatGPT personal Project Instructions Editor wrapper，确认它与最终 0.1 source 的差异；若 Codex 本身无法调用 Plugin Creator，则在仓库生成一份简短、精确的 wrapper update handoff，列出需要同步的 source commit、文件和能力边界，但不得声称网页 Plugin 已更新。

## Git / 收口

- 所有工作在 `work/project-instructions-editor--0.1-closure` 完成。
- 不修改无关中央 Plugin 行为。
- 不碰 Clear Writing 下一版实现。
- 通过所需测试后 commit 并 push。
- 如果当前 release 流程允许且所有机械/产品验收满足，按既有仓库规则完成 PIE 0.1 的 repository release closure；不要因为“暂时不开 Critic”伪造 Critic PASS，也不要把 C11 改成 PASS。
- 更新 Issue #93：明确 PIE 0.1 已缩回编辑器职责；跨轮最终阅读层已转交 Clear Writing tracking #13。只有真实 release closure 完成后才把 PIE 0.1 标为完成。

最后只给用户一个短结果：
- final commit / branch；
- PIE 0.1 是否已正式收口；
- README/icon 是否已同步；
- repository/version 变化；
- Web wrapper 是否已同步，若没有则给唯一下一步；
- 明确“C11 reader-layer failure preserved; not reclassified as PASS”。
