# Design Assurance：Claude / GPT Astra 角色决定

日期：2026-11-04  
状态：PHASE_A_DECISION — 用于后续 Design Assurance v0.1 收敛  
依据：AI_Research_Toolkit 的 `AI_RELIABILITY_SYSTEM_REFERENCE.md` 与 `docs/research/design-assurance/GRILL_AND_ASTERIA_BLUEPRINT_INPUT_20261102.md`，以及两轮 Asteria GPT Pro 复盘。

## 1. Design Assurance 当前具体链路

现有设计输入已经明确，Design Assurance 负责“复杂构思到实施前冻结”，不是前端制作插件本身。

实际步骤应收敛为：

1. **任务分级 / 进入条件**
   - 判断是否是需要 Design Assurance 的复杂设计；
   - 普通局部任务不升级成重流程。

2. **事实恢复**
   - 仓库、文档、现有实现、外部事实可自行核实时，优先 GPT/Codex 调查；
   - 事实问题不问用户。

3. **关键未决问题暴露**
   - 只有会改变产品行为、架构、失败/恢复、权限、成本或不可逆边界的问题进入 Grill；
   - Grill 的目标是得到“已解决决定与理由”，不是长聊天。

4. **专业设计波次**
   - 主 Design Assurance Planner/Pro 负责整体问题建模与方案空间；
   - 按任务调用专业 specialist：科学/数学、系统架构、前端视觉/产品等；
   - 可以并行第二 Pro / Work，但按风险触发，不固定排班。

5. **唯一方案收敛**
   - 综合事实、用户已确认决定和 specialist 输入，形成唯一推荐方案；
   - 明确保留项、放弃项、OPEN 项和理由。

6. **Implementation Readiness**
   - 检查 Codex 是否仍需自行猜核心行为；
   - 检查真实任务、对象/关系/机制、失败路径、依赖、验收与回滚是否足够明确。

7. **Architecture Freeze**
   - 只有重大 OPEN 已关闭、实现不再需要代替用户/设计者做产品决定时才 Freeze；
   - Freeze 形成唯一实施权威与 NEXT_ACTION。

8. **Asteria Blueprint 映射 / Codex handoff**
   - Blueprint 保存/展示冻结后的系统结构、机制、实现、证据、修订与漂移；
   - Codex 开始实施；
   - Freeze 后若出现反证或关键空洞，再回 Design Assurance 开新 revision。

## 2. Claude API 最适合的唯一正式角色

对于**有重要前端/可视化界面**的复杂设计，Claude API 应作为：

> **Frontend Product & Visual Design Specialist**

它放在第 4 步“专业设计波次”，不是放在 Grill、事实恢复、最终 PASS 或 Codex 实施。

职责：
- 读取已经收敛的产品目标、用户决定、静态视觉证据和真实内容；
- 独立判断信息组织、空间关系、视觉层级、交互连续性；
- 至少对重要前端产品完成一次真实设计 pass，而不是只做文字审稿；
- 产出少量可比较的关键场景/候选与明确设计理由；
- 用户选定后，维护该视觉方向的连续性，并在后续真实实现上做高价值视觉返修。

Claude 不负责：
- 全仓检索和资料整理；
- 打开 Obsidian/浏览器做现场操作；
- 机械截图、构建、测试；
- 事实核查；
- Grill 式连续盘问；
- 给自己做最终 Design Assurance PASS；
- Delivery Assurance。

## 3. GPT Astra 的替代规则

当 Claude API 不可用、额度不值得投入、或中转无法可靠读取图片时：

> **GPT Astra 可以替代同一个 Frontend Product & Visual Design Specialist 槽位。**

替代的是角色，不是另起一条流程。

规则：
- 同一任务默认只运行 Claude 或 Astra 一个主 specialist，不双跑烧成本；
- 高价值、争议明显的方向才考虑独立对照；
- Claude/Astra 都必须读取同一静态证据包和用户已确认设计决定；
- 任一模型的产物都不能因为模型档次自动获得 ACCEPTED；
- 若 Claude 已经确立并被用户接受视觉方向，切换 Astra 时默认继承，不允许重新设计整个产品。

当前偏好：前端重要任务至少让 Claude 真实设计一次；Claude不可用时 Astra 是主要替代。这个偏好是当前生产策略，不写成“Claude 永远更强”的永久事实。

## 4. Asteria Blueprint 与这个角色的关系

Asteria Blueprint **不替代** Claude/Astra specialist，因为它是系统结构、机制、实现、证据和演进的长期载体，不是视觉/产品判断模型。

Asteria Blueprint 也**不替代** Design Assurance：它可以帮助第 6–8 步检查结构完整性并保存 Freeze 后的长期真相，但不能决定方案是否应该 Freeze。

未来理想关系：
- Design Assurance 决定“是否充分、是否 Freeze”；
- Claude/Astra specialist 解决“前端产品/视觉怎样设计”；
- Frontend Design 提供领域设计方法与返修规则；
- Asteria Blueprint 让复杂设计的结构、机制、实现和证据可见并长期维护；
- Codex 实施；
- Delivery Assurance 负责 Freeze 后交付不失真。

## 5. 对 Asteria 当前恢复工作的直接影响

Asteria Phase B 的 Claude Stage 1 不是 Design Assurance 的最终形态，而是对该 specialist 角色的一次真实试验：
- Phase A 已先把历史证据静态化；
- Claude Stage 1 独立看历史、找可能保留资产、提出真正未决问题；
- 用户确认；
- Claude Stage 2 做真实设计 pass；
- Design Assurance 再检查设计是否足够实施。

这次试验结果会决定 Design Assurance v0.1 中该 specialist 的触发条件、输入规模和输出合同，但不会新增一个 Claude 专属框架。
