# 共享能力产品形态决定 — 2026-11-12

本文件记录用户已经明确确认的产品边界，供后续 Planner、Critic、Codex 和维护者引用。它只冻结“能力放在哪一层、由谁消费”的产品形态，不代表相关实现已经完成，也不替代正式能力设计、验收或发布流程。

## 已确认决定

### Reasoned Decision

- 形态：独立 Plugin。
- 原因：它本身是完整用户任务，负责定义问题、调查现实解空间、核证据、比较方案、形成推荐以及决定何时停止或改判。
- 不并入 Clear Writing。

### Design Assurance

- 形态：独立 Plugin。
- 当前正式设计由其独立设计流程继续推进；本文件不重做其架构。

### Delivery Assurance

- 形态：独立 Plugin。
- 当前正式设计由其独立设计流程继续推进；本文件不重做其架构。

### Clear Writing

- 形态：保持独立 Plugin。
- 边界：负责已经决定要表达的内容如何被准确、自然、清楚地写给读者，并保持事实、科学语义和机器字符串等必要保真。
- 不接管决策、情绪关系姿态或“内容是否应该出现在作品里”的判断。

### Artifact Content Design

- 形态：共享 standalone Skill，不做独立 Plugin。
- 定位：被所有适用的产物型 Plugin / Skill 消费，而不是要求用户额外记住一个顶级入口。
- 适用对象包括但不限于报告、论文/科研文档、演示文稿、网站/UI、科研图、生成图像、项目页和其他读者可见产物。
- 制作前职责：判断哪些内容值得出现、出现到什么粒度、处于什么层级，以及应当 KEEP / COMPRESS / VISUALIZE / DEMOTE / REMOVE。
- 制作后职责：必须复审真实渲染后的整件作品。单个元素分别合理不代表组合后合理；删除内容后造成的空洞、层级失衡、重复说明、内部过程泄漏和整体过度解释都属于该复审范围。
- 它不取代领域正确性、Clear Writing、媒介专属布局/交互/视觉能力或最终领域验收。
- 未来只有在真实使用证明它已经长成多项独立用户任务时，才重新评估是否升级为更大的 Artifact Director Plugin；当前不推进该形态。

### Warm Response

- 形态：ChatGPT 全局协作指令，不做 AI_Skills Plugin，也不做 standalone Skill。
- 主要消费场景：普通 ChatGPT 网页对话中的明显人际/情绪情境。
- Codex / GPT Work 默认不需要承担同等的人际回应职责；不得为了统一产品形态把它强行注入机器执行或正式产物。
- 现有 AI_Skills warm-response seed、TODO 和真实对话继续作为失败证据与指令设计素材，不再作为独立 Plugin 的实现入口。

### Anti-Conservative

- 形态：ChatGPT 全局协作指令，不做 AI_Skills Plugin 或 Skill。
- 作用：规定默认协作姿态，例如不过度审计已足够工作的前提、不强制正反平衡、审慎程度与真实风险匹配、目标明确后完成判断和默认推荐。
- 当前候选来源继续由 `YuukiAS/AI_Instruction_Configuration` 管理。
- 若未来某个具体行为被证明属于 Reasoned Decision 或 Clear Writing，可把该局部能力下沉到对应 owner；不把整个 Anti-Conservative 产品化。

## 组合边界

正常情况下：

```text
全局协作姿态
├─ Warm Response
└─ Anti-Conservative

独立任务型能力
├─ Reasoned Decision
├─ Design Assurance
├─ Delivery Assurance
└─ Clear Writing

共享产物能力
└─ Artifact Content Design
   └─ 被 Research Authoring / Presentations / Frontend Design /
      Scientific Visualization / Documents / Image generation 等适用消费者调用
```

后续新增相近能力时，优先判断它是“完整用户任务”“跨产品共享的窄能力”还是“所有对话默认生效的协作姿态”，避免把所有好行为都堆进 Clear Writing，也避免为每条规则新增 Plugin。
