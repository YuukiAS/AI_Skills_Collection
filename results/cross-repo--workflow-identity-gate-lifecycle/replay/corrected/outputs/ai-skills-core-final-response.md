我会使用已安装的 AI Skills Maintainer 能力，读取维护规则和输入案例，逐项给出分类；不修改文件，也不访问网络。


---MESSAGE---

### M1：单插件维护

- **归属与行动**：AI_Skills 内的 `writing-style` 返修；修复已有规则的实际执行，先改 source，再生成对应 payload。
- **Gate**：复用现有 writing-style Capability Gate 和 regression bank，补充失败样本，不新增同义 Gate。
- **闭环**：同一最终候选完成原失败回放、无关回归和真实全文审阅。缩小验证范围须有隔离说明及“不应改变”证据。交付时该插件版本推进一次，更新插件 changelog；正式仓库发布通常为 PATCH，并验证生成一致性、安装/升级及 CI。
- **专业判断**：`writing-style` 判断文字质量；Maintainer 不能用流程通过代替成品通过。

### M2：单仓库、多生产插件

- **归属与行动**：AI_Skills 仓库内同时涉及 `workflow-core`、`ai-skills-core`；不是单插件任务，也不是跨仓库任务。技术 scope 应反映共同维护边界。
- **Gate**：优先映射两者现有 Gate；插件数量增加本身不构成 Gate 重设计理由。跨插件行为变化要求 broad/full 回归。
- **闭环**：source-first，重新生成两个 payload；同一最终候选完成回放、回归和独立 review。两者若均形成已完成的生产行为改进，各推进一次版本并更新 changelog。仓库正式发布默认 PATCH；只有新增仓库级用户能力才考虑 MINOR。完成发布元数据、生成一致性、smoke 和 CI。
- **专业判断**：`workflow-core` 判断工作流契约，`ai-skills-core` 判断维护闭环；不涉及其他领域插件的质量改进。

### M3：AI_Skills 与 Bridge 跨仓库维护

- **归属与行动**：可写 owner 仅为 AI_Skills 与 Bridge；下游产品仓库保持只读。Bridge 拥有 task-key validation，AI_Skills 消费其契约，不另造技术 identity 规则。
- **Gate**：复用工作流、identity 和跨仓库集成回归；仅在存在现有 Gate 无法表达的能力或 owner 边界时考虑重设计。
- **闭环**：最终证据必须共同绑定精确的 AI_Skills SHA 与 Bridge SHA；任一候选变化都须重新确认相关证据。验证 semantic key、旧 key 兼容及必要绑定路径，采用 broad/full 检查。AI_Skills 按受影响插件完成生成、版本、changelog、回放和发布闭环；Bridge 按自身发布规范处理。
- **专业判断**：工作流由 `workflow-core`、identity 契约由 Bridge owner 判断；引用产品实例不授予修改权或领域质量背书。

### M4：已有能力回归

- **归属与行动**：属于目标插件的 production regression。先比对 active rule 和已有 TODO，合并重复证据，检查实际 consumer/runtime。
- **Gate**：使用已有 Capability Gate 和 regression bank；标签不同不足以新建近似 Gate。
- **闭环**：若修复生产行为，完成 source→generated、原失败回放、无关回归和独立 review；交付时插件版本推进一次并更新 changelog。仅记录 TODO、增加测试或修正评分器则 `NO_BUMP`，评分器修复不能冒充产品修复。
- **专业判断**：由目标领域 owner 验收；文字、幻灯片、统计分别归 `writing-style`、`presentations`、`statistical-modeling`。

### M5：真正的新能力

- **归属与行动**：由目标插件 owner 与 Planner 冻结能力、正常入口、证据类型及失败语义；Maintainer 负责维护边界，不直接把提案升级成永久规则。
- **Gate**：具备考虑新建或拆分 Gate 的理由。必须说明旧/新覆盖范围、历史样本去向，以及应保持不变的行为；合并或退役不得丢失历史覆盖。
- **闭环**：冻结验收样本，先改 source 再生成；同一最终候选完成新能力生产回放、已有能力回归和独立 review。入口/routing 改变应走 broad/full 检查。正式交付时受影响插件推进一次版本并更新 changelog；插件新增能力不自动等于仓库 MINOR，也不自动达到 `1.0`。
- **专业判断**：目标领域插件负责专业正确性；Maintainer 负责生成、证据、版本及发布闭环。

以上为分类判断，未修改文件或访问网络。工作区缺少版本规范全文，因此不指定具体新版本号；实际发布前须读取该规范。
