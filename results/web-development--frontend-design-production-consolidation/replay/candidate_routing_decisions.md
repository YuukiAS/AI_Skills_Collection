# Frontend Design 候选插件路由回放

实际入口：`web-development@ai-skills-candidate`（安装版本 `0.3`，显示名 `Frontend Design`）的 `.codex-plugin/plugin.json` → `skills/visual/SKILL.md`（`routing_mode: coordinator-first`）→ `skills/visual/_src/system/source.md` → 按场景选择委派 → 返回协调器作准入判断。

以下路径均相对于安装根目录 `/home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/`。入口与协调器已在所有委派之前完整读取；各场景复用同一份已读取的入口、协调器及适用委派内容，没有绕过协调器。没有读取无关的 refs、motion 或深层参考包。

本报告以 `inputs/01-scenarios.json` 为场景输入，仅给出生产路由和验收条件。未提供实际项目、运行实例、设计文件或渲染证据，因此下列准入条件均未被宣称已经满足。P0–P4 表示流程阶段；`P1=0/P2=0` 表示缺陷准入条件，两者不混同。

## s1_browser_tiny_spacing_fix

SCENARIO_ID: s1_browser_tiny_spacing_fix

COORDINATOR_SOURCE_CONSUMED: `skills/visual/SKILL.md` → `skills/visual/_src/system/source.md`

DELEGATE_SOURCES_CONSUMED: `skills/visual/_src/tokens/source.md`; `skills/visual/_src/responsive/source.md`; `skills/visual/_src/webapp-testing/source.md`

SCALE_DECISION: S1，仅修复主按钮图标与文字的间距和对齐。

DESIGN_AUTHORITY_DECISION: 使用当前已发布组件和产品样式规则，沿用现有 spacing/token/icon 体系；不强制补 Figma 或重做设计。

SURFACE_DECISION: browser；在真实页面的窄视口复现，并检查相关正常宽度、焦点和禁用状态。

ADMISSION_OR_REPAIR_DECISION: 将局部实现修复交给项目代码流程；协调器检查文字适配、图标尺寸、对齐及既有可访问性没有退化。未暴露更大设计缺口时不要求全产品独立评审；交付前把缺陷结论绑定到确切候选和视口。

EVIDENCE_BOUNDARY: 当前只有路由判断；需实际渲染对比证明间距修复，不能凭 CSS 修改或静态片段声称完成，截图也不证明按钮行为。

## s2_durable_authority_settings_panel

SCENARIO_ID: s2_durable_authority_settings_panel

COORDINATOR_SOURCE_CONSUMED: `skills/visual/SKILL.md` → `skills/visual/_src/system/source.md`

DELEGATE_SOURCES_CONSUMED: `skills/visual/_src/ux/source.md`; `skills/visual/_src/tokens/source.md`; `skills/visual/_src/responsive/source.md`; `skills/visual/_src/webapp-testing/source.md`

SCALE_DECISION: S2，现有管理页面中的有界面板扩展。

DESIGN_AUTHORITY_DECISION: 当前持久化 design brief 为权威，复用组件系统；先确认 saved、saving、error、disabled、permission-denied 的设计目标、动作可用性和转换，缺失目标先补 brief。

SURFACE_DECISION: browser；在完整管理页面中验证面板状态、键盘、错误提示、窄屏与周围页面关系。

ADMISSION_OR_REPAIR_DECISION: UX 明确状态与生命周期，tokens 约束组件及状态外观，再交给项目实现流程；只扩展受影响范围。F-A 状态目标齐全、F-B 组件一致、F-C 实际交互通过后，由协调器执行 F-D 自检准入，不自动升级全页重设计。

EVIDENCE_BOUNDARY: 未读取真实 brief 或运行面板。保存成功文案不等于持久化成功；若交付包含保存承诺，需实际保存及重新读取等对应证据。不得预填 `P1=0/P2=0`。

## s3_no_figma_product_redesign

SCENARIO_ID: s3_no_figma_product_redesign

COORDINATOR_SOURCE_CONSUMED: `skills/visual/SKILL.md` → `skills/visual/_src/system/source.md`

DELEGATE_SOURCES_CONSUMED: `skills/visual/_src/ux/source.md`; `skills/visual/_src/direction/source.md`; `skills/visual/_src/tokens/source.md`; `skills/visual/_src/responsive/source.md`; `skills/visual/_src/webapp-testing/source.md`

SCALE_DECISION: S3，信息架构、首屏、状态模型和导航均改变，执行完整 P0–P4。

DESIGN_AUTHORITY_DECISION: 以 product brief 为起点，形成并接受持久化的流程与设计目标；旧截图提供现状证据，不自动约束新方案。没有 Figma 不构成阻塞，也不要求创建 Figma。

SURFACE_DECISION: browser；覆盖实际多步骤流程、前进与返回、关键错误/权限/空状态，以及正常和窄屏尺寸。

ADMISSION_OR_REPAIR_DECISION: P0 冻结任务、状态和导航；P1 确定视觉方向及可访问性；P2 形成实现合同并交给官方 builder 或项目流程；P3 验证实际表面；P4 对层级、密度、可发现操作和状态转换是否协调作可观察判断，并取得独立确认。生产者自检只是进入独立评审的门槛。

EVIDENCE_BOUNDARY: 当前未生成或实现重设计，未执行独立评审。未来证据须绑定同一候选、完整流程及视口；旧截图和自检不能替代新实现的独立质量证据。没有新增动画要求，暂不加载 motion 委派。

## canonical_figma_material_change

SCENARIO_ID: canonical_figma_material_change

COORDINATOR_SOURCE_CONSUMED: `skills/visual/SKILL.md` → `skills/visual/_src/system/source.md`

DELEGATE_SOURCES_CONSUMED: `skills/visual/_src/figma/source.md`; `skills/visual/_src/ux/source.md`; `skills/visual/_src/tokens/source.md`; `skills/visual/_src/responsive/source.md`; `skills/visual/_src/webapp-testing/source.md`

SCALE_DECISION: S2，范围限定为 billing screen，但属于重大 canonical-design 收敛，触发 P4 独立确认；Figma 身份本身不是规模分类。

DESIGN_AUTHORITY_DECISION: 用户指定的最新 canonical Figma frame 为权威。实施时先定位 exact file/page/frame/node，按官方 Figma skill 流程读取当前组件、变量、资产及状态；层级、空状态、按钮分组不能由旧代码反向覆盖设计。

SURFACE_DECISION: browser；在实际完整 billing 页面、正常工作尺寸和适用断点与权威 frame 对比，同时验证动作及状态转换。

ADMISSION_OR_REPAIR_DECISION: 先检查设计状态覆盖，缺失则返回设计权威补齐；按项目组件实现既定层级与分组。记录设计变化、代码变化和有意偏差，完成 F-A 至 F-D 及重大收敛的独立确认后才能宣称生产就绪。此路由不授权收费或其他真实账单操作。

EVIDENCE_BOUNDARY: 输入未提供 Figma locator、frame 内容或应用，未调用 Figma 工具、未证明视觉一致。需当前 frame 与确切实现候选的对照和交互证据；局部截图不证明完整页面或账单/provider 行为。

## native_handoff_action_reachability

SCENARIO_ID: native_handoff_action_reachability

COORDINATOR_SOURCE_CONSUMED: `skills/visual/SKILL.md` → `skills/visual/_src/system/source.md`

DELEGATE_SOURCES_CONSUMED: `skills/visual/_src/ux/source.md`; `skills/visual/_src/responsive/source.md`

SCALE_DECISION: S2，有界 native tray 用户交接流程审查；不是因为 native 身份自动归入 S3。

DESIGN_AUTHORITY_DECISION: 依据当前 tray 的产品状态/动作合同和适用设计源；输入未指定 canonical Figma，不能假定存在。UX 明确文件夹选择器出现后的 human-only 边界。

SURFACE_DECISION: native-WebView；需要真实原生宿主与系统文件夹选择器证据，browser companion 不足以证明这条路径。

ADMISSION_OR_REPAIR_DECISION: 请求用户选文件夹前，生产者必须在安全授权范围内确认控件可见、启用，真实触发后抵达预期选择器，且无明显 P2 问题；在用户专属的文件夹选择处停下。若属于重大 native 用户流程里程碑，另需独立确认。只有到达并记录边界后才能给出已验证的用户交接。

EVIDENCE_BOUNDARY: 本次没有 native 实例，因此可达性未验证。网页截图、DOM 点击或源码检查不能替代原生证据；无法操作实际宿主时应准确报告未验证边界，不得宣称用户可以直接完成后续动作。

## competing_route_interaction_claim

SCENARIO_ID: competing_route_interaction_claim

COORDINATOR_SOURCE_CONSUMED: `skills/visual/SKILL.md` → `skills/visual/_src/system/source.md`

DELEGATE_SOURCES_CONSUMED: `skills/visual/_src/webapp-testing/source.md`

SCALE_DECISION: S1，局部交互因果验证，非重设计。

DESIGN_AUTHORITY_DECISION: 保持既定 popover 交互意图；将“outside-click 导致关闭”作为需要证据的行为合同，不以实现现状定义正确行为。

SURFACE_DECISION: browser；真实打开 popover，并在不触发导航的外部位置真实点击。

ADMISSION_OR_REPAIR_DECISION: F-C 存在竞争路径，单纯“最后关闭”不够。需记录关闭前后路由、文档/组件实例连续性，排除 remount，并用事件/处理路径证据或隔离导航的受控试验验证 outside-click 路径。若失败，按 runtime-only repair 修正运行行为并保持设计意图，再重测具体路径。

EVIDENCE_BOUNDARY: 本次未运行交互测试。普通 locator/actionability 加后置条件仅适用于没有竞争路径的普通交互；这里截图或 closed 后置状态无法证明因果，URL 未变也不能单独排除组件重挂载。

## unsupported_metric_ranking_semantic_claim

SCENARIO_ID: unsupported_metric_ranking_semantic_claim

COORDINATOR_SOURCE_CONSUMED: `skills/visual/SKILL.md` → `skills/visual/_src/system/source.md`

DELEGATE_SOURCES_CONSUMED: `skills/visual/_src/ux/source.md`; `skills/visual/_src/research/source.md`

SCALE_DECISION: S2，有界比较表的产品语义修复；虽然元素少，不能当作纯样式 S1 修复。

DESIGN_AUTHORITY_DECISION: 仓库原始指标支持展示数值，不支持自动赋予排名、“best”或指标优先级。UX 负责通用语义合同，research 在协调器之后补充单位、版本、来源、可比性与不确定性约束。

SURFACE_DECISION: browser；后续需检查实际表格的顺序、标签、颜色和图标是否隐含未经支持的优劣结论。

ADMISSION_OR_REPAIR_DECISION: 分类为 product semantic defect，返回 P0/UX，暂停该排名声明的生产准入。取得持久化、经领域确认的排序规则及适用范围前，只能采用经产品合同确认的中性展示，移除无依据的排名或 best 暗示；不得自行选择“越大越好”、加权分数或优胜模型。

EVIDENCE_BOUNDARY: 本次没有指标数据或排名规则；不能给出科学优劣结论。视觉检查无法填补语义缺口；修复实现后的 browser F-C 验证仍需另行执行，本场景没有为尚不存在的实现加载测试委派。

## implementation_drift_should_not_change_design

SCENARIO_ID: implementation_drift_should_not_change_design

COORDINATOR_SOURCE_CONSUMED: `skills/visual/SKILL.md` → `skills/visual/_src/system/source.md`

DELEGATE_SOURCES_CONSUMED: `skills/visual/_src/tokens/source.md`; `skills/visual/_src/responsive/source.md`; `skills/visual/_src/webapp-testing/source.md`

SCALE_DECISION: S1，已接受卡片边框的局部 token 漂移。

DESIGN_AUTHORITY_DECISION: 保持当前已接受且仍有效的设计源和产品状态合同；不能为迁就错误渲染而修改设计源。

SURFACE_DECISION: browser；在真实页面验证卡片边框及适用主题、状态、视口，并留意共享 token 的影响范围。

ADMISSION_OR_REPAIR_DECISION: 分类为 implementation drift，将组件绑定修回现有正确 semantic/component token；不以全局重定义 token 掩盖局部绑定错误。复核对比度与状态样式并完成最小相关回归，再由协调器作局部准入；没有新设计缺口时不扩大成独立重设计。

EVIDENCE_BOUNDARY: 未读取真实设计、代码或渲染；当前只确定修复归属。需确切候选上的设计/渲染对照证明漂移已消除，不能宣称已有 `P1=0/P2=0` 或独立验收 PASS。
