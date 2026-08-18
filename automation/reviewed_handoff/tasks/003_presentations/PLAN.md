---
schema: AI_BRIDGE_REVIEWED_PLAN_V1
task_key: 003_presentations
decision: PLAN_FROZEN
---

# 003 Presentations — Plan

## 目标

把当前研究/商业演示 skill、`presentation-desktop` profile 和共享 PPT 路由整理成一致的工作流：先做叙事和逐页设计，再按用户实际交付格式路由文件生成；对于桌面 PPT 场景，优先支持可编辑 PPTX/Slides，而不是因为内容是学术研究就自动转去 Beamer。

## 冻结决定

- 保留 `research-presentations`、`business-presentations` 和 `presentation-desktop`，不新增 presentation 顶级 plugin/skill。
- 本仓库继续负责：来源理解、叙事、deck plan、逐页信息设计、写作终审、格式路由和 QA 标准；实际 PPTX/Slides 对象创建和编辑交给官方 Presentation/Slides 执行能力。
- **取消“academic/research = 默认 Beamer”这一硬默认。** 输出格式首先由用户要求决定：
  - 用户明确说 PPT、PowerPoint、`.pptx`、editable、Slides、要后续手改 → 可编辑 Presentation/Slides 路线。
  - 用户明确说 Beamer、LaTeX slides、`.tex`、学术 PDF，或项目/venue 已锁定 TeX → Beamer/LaTeX 路线。
  - 用户只说“做组会/科研汇报”但没有指定格式，且使用 `presentation-desktop`/桌面演示场景 → 默认按可编辑演示文稿规划；不要仅凭“学术”二字切换 Beamer。
  - 用户只要提纲/故事线 → 可以只交 deck plan，不强制生成文件。
- 研究型 deck 的主叙事保持：`为什么做 → 发生了什么/核心发现 → 方法或机制 → 证据 → 局限 → 需要讨论的问题 → 下一步`。不是每份 deck 都必须机械出现全部七段，但顺序和因果要服务听众理解。
- 一页一个核心信息。页面结构由该页信息和证据决定，不能把“3 个 bullet + 一张装饰图”当默认模板。
- 保持可编辑性：除非用户明确要求 image/PDF slide，不要把整页渲染成不可编辑图片冒充 PPTX。
- 中文 slide text 必须经过 `writing-fidelity` + `chinese-prose` 的终审；英文科研 slide text 可使用 `scientific-prose`。presentation profile 已包含这些能力，路由文档必须明确这是协作关系，不是重复造写作 skill。
- 文件存在不等于完成。最终 deck 必须 render 后做视觉 QA；检查裁切、溢出、字号/密度、布局层级、图表可读性、公式、标题信息、图像用途和整套叙事连续性。

## 允许修改

主要检查并按需要修改：

- `skills/tools/documents-media/presentations/research-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/business-presentations/SKILL.md`
- `skills/tools/documents-media/presentations/shared/ppt-skill-routing.md`
- `skills/tools/documents-media/presentations/shared/deck-plan.schema.json`
- `skills/tools/documents-media/presentations/shared/source-fidelity.md`
- `skills/tools/documents-media/presentations/shared/visual-qa.md`
- `profiles/presentation-desktop.json`
- `tests/test_presentations.py`
- 必要的 marketplace/profile/生成层文件（只能通过既有生成流程产生）

不要为了有 diff 改已经正确的文件。

## 研究型演示验收案例

以下请求应稳定进入 `research-presentations` 的叙事规划，并按格式要求路由：

1. “把这周的实验进展做成 10 页组会 PPT，我后面还要自己改。” → 研究叙事 + editable PPTX/Slides。
2. “这篇论文准备讲 15 分钟，帮我做组会 slides，一页一个重点，别做成文献流水账。” → 研究叙事；未指定格式时桌面场景默认 editable deck。
3. “把当前研究路线做成可编辑 PPTX，中文，方法、证据、局限和下一步要能讲清楚。” → editable deck + 中文写作终审 + render/QA。
4. “给我一份 Beamer 版本用于 conference talk。” → LaTeX/Beamer。
5. “先别生成文件，先把 12 页故事线和每页核心结论规划出来。” → 只产 deck plan。

不应出现：

- 因为请求里有“论文、组会、conference、科研”就自动默认 Beamer。
- 用户明确要 editable PPTX，却只返回 PDF/整页图片。
- 只给一份泛泛 outline，就宣称 PPT 已完成。
- 页面内容依旧是机械三 bullet、没有主结论或图表只是装饰。
- 没有 render/视觉检查就把文件标记 complete。

## 商业演示边界

`business-presentations` 继续处理管理层、产品、市场、运营、客户、策略、pitch 和决策 deck。研究内容如果听众和目的明确是资源/产品/业务决策，可以进入 business；普通组会、论文报告不应进入。

## 视觉和文字质量门槛

- `deck-plan` 至少能表达：slide purpose、main message、source/evidence anchor、visual intent、format/editability expectation。
- 标题应承担信息而不是只写“Background / Method / Result 1”这类空标签；能写结论型标题时优先结论型标题。
- 图、表、截图、示意图必须支持该页结论；无信息价值的装饰图不作为质量要求。
- 重要图表/公式必须可读，不允许通过缩小字号或塞满页面解决空间问题。
- 中文 slide 不应充斥普通英文流程词；精确模型名、指标、文件名和代码 token 保留。
- 研究表达要准确，不为了故事性夸大证据。

## 完整验证

至少运行 presentation 测试、全库 validate/audit、marketplace 生成检查和 unittest。Planner/Reviewer 还必须直接读修改后的 routing 文档，并用上面的自然语言案例判断，不允许用关键词匹配器替代语义复核。

## 最终报告必须展示

至少给出：

- 原来的关键矛盾：学术默认 Beamer vs `presentation-desktop` 的 editable PPTX/Slides 定位；
- 修改后格式选择规则；
- 3–5 个真实 example usage，明确用户说什么、会走哪条路线、预期得到什么；
- 中文写作终审如何进入 slide workflow；
- render/visual QA 如何决定 `complete`；
- 没有采用的新 plugin/新 skill/整页图片默认方案及原因。

## Frozen decisions

对应本计划中的 `## 冻结决定`、`## 研究型演示验收案例`、`## 商业演示边界` 和 `## 不在本任务范围`。本节只补 Reviewed Handoff v0.5 validator 的英文标准章节名。

## Implementation scope

对应本计划中的 `## 允许修改`。执行范围仍以原中文章节为准。

## Acceptance and regression gates

对应本计划中的 `## 视觉和文字质量门槛`、`## 完整验证` 和 `## 最终报告必须展示`。

## Out of scope

对应本计划中的 `## 不在本任务范围`。

## 不在本任务范围

- 不实际制作某一个具体项目的 PPT 作为仓库 release artifact；可以用 fixture/示例验证路由。
- 不重做科研论文写作 routing；001 负责。
- 不把所有 visualization skill 一并重构。
- 不处理新的外部 PPT prompt/repo/Notion 候选。