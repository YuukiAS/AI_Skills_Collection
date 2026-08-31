# presentations — Long-Term TODO

这是 `presentations` plugin 的长期问题清单。

以后在 TRACE、CARE 或其他真实项目里调用 `presentations` 时，如果问题本质上来自 plugin 的生成、返修、布局、检查或路由行为，直接把这次真实问题写到这里，状态先用 `NEW`。不要先在项目 repo 再维护一份 Presentation 插件问题副本。

Current capability status: `baseline`.

## Incoming real-use feedback

目前没有尚未整理的 `NEW` 条目。

真实项目 thread 新增时只需要最小格式：

```text
### <简短的问题标题>
status: NEW
source: <真实项目 / 当前任务>
evidence: <实际 PDF / render / commit / task 路径>
problem: <用户实际看到的问题>
project-specific context: <哪些细节只属于当前项目>
```

此时先记事实，不要直接发明通用规则。后续由 AI_Skills Planner / maintainer 去重、整理并决定是否变成下面的长期候选。

## Open candidates

### Diagram geometry and canonical edge/node treatment
status: BLOCKED_NEEDS_EVIDENCE
source: repeated TRACE visual feedback
evidence: presentation maintenance archive + CAT-TRACE real deck revisions
target layer: rendering/qa
problem: diagram 的语义规则已经有了，但实际箭头、节点、对齐、连接路径和层级几何仍然可能做坏。
candidate action: 只有新的真实 deck 再次暴露问题时，才补 renderer-level primitive 和 QA，不为了历史 TODO 预先造一整套几何系统。
promotion gate: 新的真实 CAT-TRACE 或 unrelated deck 用实际 render 重现问题，并能证明修改真的改善输出且不会过度限制其他 diagram。

### Deck-wide style system and terminology hierarchy
status: CANDIDATE_GENERIC
source: repeated real research deck revisions
evidence: presentation maintenance archive
 target layer: reasoning/rendering/qa
problem: 一整套 deck 里，标题大小写、术语首次解释、dataset/simulation 编号、小标题、metric label、caption 和 references 容易逐页漂移。
candidate action: 只有真实返修再次证明这是当前问题时，才增加最小 deck-wide consistency contract，不把所有页面强行做成同一种布局。
promotion gate: independent rendered deck 证明 consistency check 能抓到真实问题且不会压平不同科研页面。

### Math and theory slide hierarchy
status: CANDIDATE_GENERIC
source: repeated statistics and theory deck feedback
evidence: presentation maintenance archive + CAT-TRACE review docs
target layer: reasoning/rendering/qa
problem: definition、design setting、estimand、theorem、derivation 容易都被做成同一种“居中大公式”，科学角色没有层次。
candidate action: 在新的 math-heavy real deck 再次出现时，才进一步加强公式层级、首次语义解释和 theory-page QA。
promotion gate: theorem/statistical-method real deck replay + unrelated math-heavy deck regression。

### Simulation, metric and structured-fact presentation
status: CANDIDATE_GENERIC
source: repeated real statistics deck feedback
evidence: presentation maintenance archive
target layer: reasoning/rendering/qa
problem: DGP、estimand、baseline、metric direction、dataset facts、seed/reproducibility 信息容易混成段落或弱表格，读起来很累。
candidate action: 新的 simulation-heavy / real-data deck 再次出现时，再提炼更稳定的 table/list patterns 和 QA。
promotion gate: 至少一个 simulation-heavy 和一个 real-data deck 的真实 render 都证明改善了可读性。

### Natural scientific slide language
status: CANDIDATE_GENERIC
source: repeated presentation and writing-style feedback
evidence: presentation maintenance archive + `docs/plugin-todos/writing-style.md`
target layer: writing/qa
problem: slides 仍可能出现内部流程词、模板化对比句、面向作者而不是面向听众的说法。
candidate action: 真实失败出现后再决定应该改 `research-presentations`、`scientific-prose`，还是两者的交接；不要重复造一套写作规则。
promotion gate: 多个独立英文科研 slide 的真实证据。

## Current real-use focus

现在不继续做 synthetic challenge chain。

下一步就是用已安装的 `presentations` plugin 继续返修**现有 CAT-TRACE deck**。新的 plugin 问题直接作为 `NEW` 写到本文件，再由中央 Planner 整理。

这不是一个需要单独“完成”的 TODO，也不需要为了证明 workflow PASS 重启 043。

## Recently promoted / established

- `0.1` 已修掉 normal-production validator 对 Stage-4 固定六类页面和固定 storyline 的硬编码。
- `0.1` 已加固 existing-deck revision：用户要求继续返修已有 deck 时，不应重新生成一套；已接受页面/元素要作为约束保留，并和用户真正看过的上一版 render 对比。
- Presentation maintenance 历史已从普通 runtime 中移出；普通安装只保留已经确认有用的规则。
- Evidence-first research-group-meeting routing 和 scientific-object page archetypes 已建立。
- Exact CUHK Beamer/PDF 仍是默认 desktop research route。
- Source fidelity、scientific layout、真实 render/contact-sheet review 和 bounded repair contract 已建立。
- Theory 页面按“解决了什么问题 / 提供什么保证”组织，而不是按 theorem 数量炫技。

## Do not do

- 不要为了 workflow PASS 重启已经暂停的 043 synthetic challenge。
- 不要把已经用来调过系统的 holdout 再说成 unseen。
- 不要把 CAT-TRACE 页码、论文名、theorem 名称写成 selector/layout 特例。
- 不要每出现一个视觉问题就新建 skill；优先修已有 reasoning/rendering/QA 层。
- 用户说“继续完善现有 CAT-TRACE PPT”时，不要从头重新生成。
