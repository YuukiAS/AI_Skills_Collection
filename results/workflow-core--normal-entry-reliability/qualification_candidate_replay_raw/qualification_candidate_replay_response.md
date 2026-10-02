# Qualification Candidate Replay 决策

- **正常入口**：优先使用场景指定的仓库任务本地 candidate replay 工具，经隔离的 `ai-skills-candidate` marketplace 加载候选插件并收集子进程 JSON 执行轨迹。先核对当前用户授权、冻结任务与仓库规范入口，再检查匹配的 specialist probe/wrapper/runner、项目声明的 runtime，最后才检查工作区通用能力。全局列表没有 production plugin id，仅能证明该列表未显示它，不能证明候选能力不可用。
- **升级判断**：在 specialist/project 路径检查前升级没有依据。先按具体 effect 区分 `required`、`optional`、`unknown`；可选清理或便利操作不能阻塞目标或推动提权，未知项先查明。只有必需 effect 确实超出所有合法正常边界时，才进入相应授权流程。冻结任务文本不能单独扩张当前用户授权。
- **审批拒绝分类**：根据证据归入①可选或非必需 effect；②选用了不必要的高权限路径；③真实权限或安全边界；④规范入口不可用或损坏，包括其 policy/runtime/transport 所属方故障。分别跳过非必需操作、改用合法低权限入口、停止依赖动作并交由授权方处理，或进行有边界的入口诊断与恢复。场景没有给出具体拒绝记录，不能预先断言属于哪类；拒绝本身也不等于能力缺失。
- **回退边界**：不允许 raw 或更宽权限的回退。自动恢复必须同时保持冻结 effect、专业质量、验收证据强度、安全与隐私、artifact identity、当前授权范围六项等价，且不增加权限。任何一项未知或变化都应停止并交还实际 owner/Planner/授权方。没有新证据时不得重试同一审批敏感路径；换 shell、Python、命令拼写或提权参数不构成新信息。
- **保留证据**：保存任务/分支/候选版本及 hash、授权范围、effect 分类、入口选择与 specialist/project 检查结果、准确命令与错误、审批拒绝理由、恢复假设和六项等价性判断，以及本地生成物、验证结果、子进程 JSON 轨迹和清理结果；不得记录秘密值。若仅 publication 或外部 transport 受阻，保留已成功的本地工作，仅将该 effect 标为受阻，不能把本地构建、QA 等已通过步骤改报失败，也不能宣称整体完成。

本次仅完成场景决策报告；未实际执行 candidate replay、审批请求、网络访问或 Git 发布。上述路径可用性来自输入场景，未作运行验证。依据为输入文件及当前安装的 workflow-core 技能规则；技能位于 `0.4` 缓存路径，不能据本报告宣称已验证 `0.5` runtime。
