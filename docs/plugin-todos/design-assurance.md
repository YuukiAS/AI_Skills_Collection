# Design Assurance — Plugin TODO

> Planned dedicated Marketplace plugin. Product shape is already frozen as an independent plugin in `docs/design/SHARED_CAPABILITY_PRODUCT_SHAPE_DECISIONS_2026-11-12.md`. This inbox records real design-readiness failures before the plugin is implemented.

## 2026-11-22：实现就绪审查必须单独证明“当前版本 → 第一代新版 → 后续稳态”
status: NEW
source: PC+Server+VPS / Cloudflare B 与 Longleaf_Backup_Codex 首次旧版→新版自然交接
evidence: 长期新版换代机制完成设计、仓库测试和 B-only 部署后，直到第一代新版 successor 即将自然启动才发现：当前正式 owner 仍运行旧协议，无法按新版方式签发接班许可；随后又发现旧版退场会删除新版候选仍需要的交接状态。两项都属于部署前即可通过当前运行版本与新版代码进行时序审查发现的设计缺口。
problem: 复杂设计的“实现就绪”不能只证明稳态架构、单个模块和新版→新版流程合理。只要部署会跨越旧实现与新实现，就必须把第一次迁移/接班视为独立设计对象，明确证明当前生产状态如何进入新稳态。局部函数分别正确、长期稳态设计正确，仍可能因为过渡顺序、所有权释放、状态清理和版本能力差异而无法实际到达稳态。
project-specific context: 具体 job ID、Cloudflare B、Slurm、pending/grant 文件都只属于本案例。通用设计门槛应覆盖：
1. 冻结前建立最小版本/状态过渡矩阵：当前真实版本 → 第一代新版 → 后续新版稳态；不能用“新版→新版通过”替代第一次过渡。
2. 对每条跨版本路径明确谁产生状态、谁读取、谁持有所有权、谁释放、谁清理，以及清理动作是否会删除后续步骤仍需要的证据。
3. 涉及锁、租约、owner、handoff、migration、rolling upgrade 或双版本重叠时，必须做整条时序审查，而不是只做组件清单审查。
4. Implementation Readiness 必须检查当前生产中已经运行/已经排队的旧字节是否会继续执行；“磁盘代码已更新”不能自动代表已提交或已运行实例获得新能力。
5. 如果首次过渡需要兼容层，兼容层的生命周期、退出条件和后续纯新版稳态必须在设计冻结前一起说明；不能等生产事件出现后临时补。
6. 设计审查通过的证据应能让独立执行者在不依赖用户继续补规则的情况下完成第一次真实过渡。
