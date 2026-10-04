# Frontend Design 0.5：原生桌面证据与低负担产品审查

status: READY_FOR_REVIEWED_HANDOFF
tracking: #97
owner_plugin: `web-development`
target_plugin_version: `0.5`
canonical_design: `docs/design/frontend-design/FRONTEND_DESIGN_NATIVE_DESKTOP_ACCEPTANCE_V0_1_2026-10-04.md`

## 一、目标

把 Lucerna、Bobbio 等真实桌面产品已经反复验证过的经验，收敛成 Frontend Design 的正式通用能力：

1. Windows 原生桌面窗口捕获与证据包不再由每个项目、每台机器重新摸索；
2. Codex 自动证明候选身份、真实交互和运行正确性；
3. GPT Work 专注整体审美、信息层级、探索性覆盖和实现者盲点；
4. S1 / S2 / S3 按改动规模决定是否需要独立产品审查；
5. 真实项目发现的通用问题能够持续写回中央 plugin，并避免项目和中央维护两份影子规则；
6. 用户不再承担普通按钮、截图、明显布局和基本状态矛盾的第一线验收。

这是一轮正式中央 plugin refinement，不是只写文档，也不是立即修改 Lucerna。Lucerna 是只读回放与行为 oracle；其正式开发可以并行继续，不以本 Goal 发布为阻塞条件。

## 二、必须使用的维护组合

执行本 Goal 时必须显式使用：

```text
workflow-core
ai-skills-core
web-development
```

其中：

- `workflow-core` 管理规划、执行、独立审查和完成门槛；
- `ai-skills-core` 管理 source authority、TODO 去重、生成层一致性、回放、版本、变更日志、CI 和正式发布；
- `web-development` 决定 Frontend Design 的专业合同、路由、证据边界和产品审查标准。

不得另造第二套状态机、工作流框架或独立设计协调器。

## 三、开始前读取

最小权威集合：

```text
AGENTS.md
TODO.md
docs/workflows/CONTINUOUS_REAL_WORLD_SKILL_REFINEMENT.md
docs/plugin-todos/web-development.md
docs/plugin-todos/ai-skills-core.md
docs/plugin-todos/workflow-core.md
docs/design/frontend-design/FRONTEND_DESIGN_NATIVE_DESKTOP_ACCEPTANCE_V0_1_2026-10-04.md
skills/tools/frontend/frontend-visual-systems/SKILL.md
skills/tools/frontend/webapp-testing/SKILL.md
scripts/codex_marketplace_config.json
```

真实项目只读来源：

```text
YuukiAS/Lucerna
  AGENTS.md
  scripts/capture-lucerna-window.ps1
  scripts/smoke-lucerna-close.ps1
  scripts/process-output-drain.ps1
  docs/workflows/LUCERNA_VISUAL_ACCEPTANCE.md
  docs/workflows/LUCERNA_INDEPENDENT_RELEASE_ACCEPTANCE.md
  results/01054_final_independent_release_acceptance/repair-harness-006.md
```

第二个桌面项目由 Planner 从当前可访问、确有原生 UI 与历史证据的项目中选择；优先 Bobbio。不得为了满足数量要求临时制造一个没有真实用户路径的合成应用。

## 四、正式范围

### 4.1 协调器

扩展现有 `frontend-visual-systems`，而不是新增并列正常入口。协调器必须在 P0 阶段判断：

- 目标表面；
- S1 / S2 / S3；
- 需要机械证明的声明；
- 需要独立产品判断的声明；
- 是否需要原生桌面证据 delegate；
- 项目是否已有可靠 adapter。

浏览器、移动端、README/docs-only、backend-only 和无 UI 的任务不得被误路由到原生桌面证据流程。

### 4.2 新能力

实现 `native-desktop-evidence` 或经 Planner 证明职责完全等价的现有层扩展。首个生产支持平台为 Windows。

建议生产源：

```text
skills/tools/frontend/native-desktop-evidence/
```

至少包含：

- 使用边界与路由说明；
- Codex / GPT Work / 用户职责矩阵；
- adapter schema；
- evidence manifest schema；
- Windows 机器诊断；
- Windows 目标窗口捕获；
- evidence pack 生成；
- 黑图、透明图、错误 PID、陈旧证据、无交互桌面和错误执行宿主的自测。

### 4.3 通用核心与项目适配

通用实现不得硬编码：

- `Lucerna`、Bobbio 或任何项目名称；
- 私有仓库路径、用户目录、机器名；
- 固定窗口标题、固定 executable、固定 HWND class；
- provider、认证、tray 状态和业务字段；
- 项目特有的启动、展开、滚动或交互语义。

项目 adapter 只负责候选定位、窗口身份、readiness、有限状态准备和捕获计划；通用工具负责 DPI、DWM bounds、窗口枚举、捕获、图像有效性和 manifest。

### 4.4 Windows 证据能力

至少支持：

- executable 规范化与 hash/mtime；
- exact process path 与 PID 绑定；
- adapter 约束下的顶层 HWND 枚举；
- DPI-aware 与 DWM extended frame bounds；
- `PrintWindow(PW_RENDERFULLCONTENT)`；
- 对同一已验证 HWND 的一次有界 `CopyFromScreen` 回退；
- 非黑、非透明、尺寸和内容有效性检查；
- `window`、`scroll-sequence`、`placement` 三类证据模式；
- 统一 failure class；
- 机器本地、Git 忽略的 doctor cache；
- PNG、metadata 和 review manifest。

普通 UI 证据默认只允许目标窗口。只有任务栏、托盘、多显示器锚定或桌面几何本身是声明对象时，才允许 placement evidence。

### 4.5 真实交互

中央能力必须明确：截图不能证明点击。

Codex 对安全、可逆、普通用户可执行的控制负责真实操作和后置条件，包括 X、Esc、tray reopen、展开/收起、Refresh、Manage、Details、Back、Cancel、文件选择器打开后取消以及本地 validation。

多个路径可产生同一最终状态时，项目 adapter 或项目测试必须提供因果证据；中央工具定义 evidence contract，不强制所有框架使用同一种自动化技术。

### 4.6 产品审查成本

冻结以下默认规则：

- S1：Codex 定向回归与真实表面验证；默认不调用 GPT Work。
- S2：Codex 覆盖受影响状态；只有明显改变整体层级、交互模型或跨组件一致性时调用 GPT Work。
- S3 / 正式 release：Codex 完成机械与原生自检后，GPT Work 做一次独立产品审查；只有 material repair 或仍有 P0/P1 时再做一次终审。

GPT Work 不重复调试截图工具、编译、hash、PID 或底层 smoke。用户不承担普通 QA。

### 4.7 持续反馈

为采用 Frontend Design 的正式任务冻结以下结果字段或语义等价输出：

```text
PROJECT_LOCAL_FINDINGS=
FRONTEND_DESIGN_GENERIC_FINDINGS=
WORKFLOW_GENERIC_FINDINGS=
PLUGIN_FEEDBACK_WRITTEN=YES|NO
PLUGIN_FEEDBACK_LOCATOR=
```

新增反馈必须遵循中央连续改进规则：项目记录真实事实，中央 maintainer 去重、抽象、决定 promotion；不得为了每次任务都“有经验”而制造空洞 TODO。

## 五、回放与验证

### 5.1 Lucerna 回放

在冻结提交上只读验证：

- 通用工具能通过 adapter 找到精确 release、PID 与目标窗口；
- 捕获不依赖私有绝对路径进入公开 source/evidence；
- Windows doctor 和 capture failure class 能复现并正确分类 Lucerna 已知问题；
- X / Esc / tray 等产品交互仍由 Lucerna 项目层测试负责；
- 新流程不会要求 S1 修复跑完整独立审查；
- GPT Work 输入可由独立 PNG + manifest 直接消费。

不得修改 Lucerna 业务代码、凭据、provider 状态或外部服务。

### 5.2 第二桌面项目回放

必须证明：

- 通用脚本未硬编码 Lucerna；
- adapter 可表达另一个窗口身份、executable 和状态计划；
- 至少完成一次真实窗口捕获和一次普通交互证据；
- 项目特有失败不会被错误提升成通用规则。

### 5.3 负向与相邻回归

至少覆盖：

- docs-only；
- backend-only；
- 普通 browser app；
- browser extension；
- Android/mobile UI；
- S1 局部修复；
- 无 Figma 的持久设计权威；
- 有 canonical Figma 的产品。

这些场景不得被错误强制进入 Windows 原生证据或 GPT Work 终审。

### 5.4 机器和缩放

Windows doctor / capture 至少在两台真实机器运行。DPI 至少覆盖两档，其中一档必须是 125% 或 150%。

无法使用第二台机器时不得伪造通过；保持该门槛待真实机器补齐，而不是用同一机器的模拟配置冒充跨机器验证。

## 六、测试与 CI

至少新增：

- schema validation；
- doctor/capture self-test；
- failure-class regression；
- adapter redaction/public-safety guard；
- coordinator routing regression；
- S1/S2/S3 review-escalation regression；
- candidate generated-plugin parity；
- Lucerna replay；
- 第二桌面项目 replay；
- unrelated full suite；
- Windows GitHub Actions 或经 Critic 批准的等价真实 Windows CI。

代码和脚本必须在没有私有路径、用户名、机器名、token、credential 和真实业务数据的情况下进入公开仓库。

## 七、版本与发布

预期中央 plugin：

```text
web-development: 0.4 -> 0.5
```

仓库版本、是否需要其他中央 plugin bump、正式 release ref 和 changelog 由 `ai-skills-core` 根据最终 diff 决定。未经真实跨层修改，不得顺手 bump `workflow-core`、`ai-skills-core` 或其他 plugin。

必须完成：

- canonical source；
- generated Marketplace payload；
- registry/catalog；
- plugin changelog；
- root changelog；
- version/parity tests；
- reviewed branch；
-独立 review；
- CI；
-正式 integration/release closure。

## 八、停止规则

- 不因单台机器截图失败而无限改造所有项目。
- 同一 failure class 没有新信息时，不重复完整构建、完整回放或 GPT Work。
- 工具链 failure 与产品 finding 分开。
- 中央能力不成熟时，项目可以继续使用已有可靠 helper；不得让 Lucerna 等真实项目等待中央 0.5。
- 用户仅在真正需要第二台真实机器、秘密/账号授权或不可逆动作时介入。

## 九、完成条件

只有全部满足才可发布：

```text
COORDINATOR_ROUTING=PASS
NATIVE_DESKTOP_EVIDENCE_SKILL=PASS
WINDOWS_DOCTOR=PASS
WINDOW_CAPTURE=PASS
EXACT_CANDIDATE_BINDING=PASS
FAIL_CLOSED_REGRESSIONS=PASS
CODEX_INTERACTION_CONTRACT=PASS
GPT_WORK_ROLE_CONTRACT=PASS
S1_S2_S3_ESCALATION=PASS
LUCERNA_REPLAY=PASS
SECOND_DESKTOP_REPLAY=PASS
UNRELATED_REGRESSION=PASS
PUBLIC_SAFETY=PASS
GENERATED_PARITY=PASS
CI=PASS
INDEPENDENT_REVIEW=PASS
RELEASE_CLOSURE=PASS
```

最终报告必须说明：普通项目如何接入 adapter、每台机器如何运行一次 doctor、Codex 如何产出 evidence pack、GPT Work 如何审查、真实项目如何写回新经验，以及哪些平台仍未支持。