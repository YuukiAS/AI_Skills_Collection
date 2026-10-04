# Frontend Design 原生桌面验收与低负担审查架构 v0.1

status: PROPOSED_FOR_IMPLEMENTATION
owner_plugin: `web-development`
target_release: `web-development 0.5`
tracking: #97
source_projects: `YuukiAS/Lucerna`, Bobbio
prepared_at: 2026-10-04

## 一、核心决定

Frontend Design 0.4 的方向是正确的：真实桌面产品不能用浏览器 fixture 冒充原生证据，Producer 必须先完成自检，重大设计变化需要独立产品判断。当前缺口不是再增加一条原则，而是把这些原则变成一套跨项目可执行、跨机器可复用、不会持续占用用户时间的生产能力。

下一版本采用以下分工：

- **Codex 证明产品真的工作。** 它负责精确候选身份、构建与回归、原生窗口生命周期、真实点击、后置条件、安全可逆操作、截图捕获、状态覆盖和证据清单。
- **GPT Work 判断产品做得好不好。** 它负责整体审美、信息层级、密度、状态可理解性、探索性覆盖、跨区域一致性和实现者盲点，不重复调试底层截图脚本，也不重新证明已有机器事实。
- **用户不承担普通质量保证。** 只有秘密输入、账号授权、不可逆外部动作、个人选择或最终主观取舍才允许打断用户。

Frontend Design 0.5 应补充一个按需调用的原生桌面证据能力，并把审查升级规则固化到现有协调器中。Lucerna 可以立即按照本合同继续开发，不需要等待中央插件发布。

## 二、当前系统已经具备什么

Frontend Design 0.4 已经提供：

- S1 / S2 / S3 任务分级；
- Figma 与非 Figma 设计权威识别；
- 浏览器证据与 native-WebView 证据分离；
- Producer 自检与 handoff reachability；
- 设计缺陷、实现偏移、产品语义缺陷、纯运行时缺陷分类；
- 对重大重设计、正式发布和整产品层级变化要求独立确认；
- Product UI Copy 的页面级内容架构与渲染回查。

这些规则已经能回答“该验证什么”，但仍不能稳定回答“在一台新 Windows 机器或一个新 Tauri/Electron 产品上，如何不重新摸索就把原生证据做出来”。

## 三、Lucerna 暴露的真实失败模式

Lucerna 的 01054 验收过程先后重新解决了：

- 当前源码、磁盘可执行文件和实际运行进程不是同一候选；
- 旧进程仍占用同一路径，导致新构建证据绑定到旧映像；
- PowerShell 子进程与长期存活 GUI 后代继承输出句柄，外层编排无法结束；
- 参数引用、只读 `$PID` 名称冲突和旧证据复用造成假失败或假通过；
- 默认 sandbox 能启动后端，却无法提供交互桌面和 WebView2 页面事件；
- `PrintWindow` 对 WebView 返回全黑、透明或没有有效内容的位图；
- DPI、DWM frame、HWND、窗口 class/title 和屏幕坐标被临时脚本反复重做；
- 截图已经生成，但模型本地图片通道因 Windows sandbox/ACL 错误无法读取；
- 每轮 Reviewer 又重新捕获、重新证明机械事实，造成修产品、修 harness、再修 Reviewer 的循环。

这些不是 Lucerna provider 或业务逻辑问题。换成另一个 Windows 桌面产品，绝大部分仍会再次出现，因此应由中央 Frontend Design 提供可复用能力。

## 四、目标与非目标

### 4.1 目标

1. 每台机器只做一次可缓存、可重跑的原生证据环境诊断。
2. 每个项目只提供薄适配文件，不重新实现 HWND、DPI、DWM、截图和黑图校验。
3. 默认截图只包含目标窗口；整桌面、任务栏和托盘只在证据确实要求时捕获。
4. 证据始终绑定精确候选、PID、HWND、窗口状态和 readiness 来源。
5. 普通按钮、X、Esc、展开、取消、刷新等由 Codex 自己操作并检查后置条件。
6. GPT Work 每个重大里程碑最多承担一次主审和必要时一次终审，而不是每个小修都重新循环。
7. 项目经验可直接回写中央 TODO，并在中央能力发布后移除项目临时规则。

### 4.2 非目标

- 不承诺一个脚本自动操作所有桌面框架和所有自绘控件。
- 不用截图代替交互、持久化、provider 或外部服务证明。
- 不让 Frontend Design 接管项目自己的业务语义、认证、安全和不可逆动作。
- 不强迫所有项目使用 Figma、GPT Work 或完整原生审查。
- 不把 Lucerna 的窗口名、路径、provider、tray 语义或 release 目录写入通用实现。
- 不在普通 feature task 中无限调试截图或模型图片通道。

## 五、Frontend Design 0.5 架构

### 5.1 协调器扩展

继续使用 `frontend-visual-systems` 作为唯一正常入口，不新增并列设计协调器。协调器在 P0 阶段增加四个判断：

1. 目标表面是浏览器、原生桌面、移动端还是混合表面；
2. 当前改动属于 S1、S2 还是 S3；
3. 哪些声明需要机械证明，哪些需要独立产品判断；
4. 项目是否已经有可靠原生 evidence adapter。

桌面 / Tauri / Electron / native-WebView 且需要原生声明时，协调器调用新的 `native-desktop-evidence` delegate。它是证据执行伴侣，不是设计权威，也不替代项目测试。

### 5.2 新 delegate：`native-desktop-evidence`

建议源码位置：

```text
skills/tools/frontend/native-desktop-evidence/
```

建议包含：

```text
SKILL.md
references/evidence-contract.md
references/reviewer-role-matrix.md
schemas/native-evidence-adapter.schema.json
schemas/native-evidence-manifest.schema.json
scripts/windows/native-evidence-doctor.ps1
scripts/windows/capture-native-window.ps1
scripts/windows/build-native-evidence-pack.ps1
scripts/windows/native-evidence-selftest.ps1
```

Windows 首先成为生产支持平台。macOS 后续通过独立实现接入相同 manifest，不在本轮用未经验证的跨平台抽象掩盖差异。

### 5.3 通用核心与项目适配分离

通用脚本不得包含应用名称、固定安装路径、固定窗口标题或项目状态语义。每个项目只维护一个薄适配文件，例如：

```json
{
  "schema": "NATIVE_EVIDENCE_ADAPTER_V1",
  "app_id": "lucerna",
  "platform": "windows",
  "executable": "src-tauri/target/release/lucerna.exe",
  "process_names": ["lucerna"],
  "window_identity": {
    "classes": ["Tauri Window", "tray_icon_app"],
    "title_patterns": ["^Lucerna$"]
  },
  "readiness": {
    "evidence_command": "<project-owned command>",
    "required_fields": ["pid", "frontend_ready"]
  },
  "show_or_reopen": {
    "command": "<project-owned bounded command>",
    "may_restart": false
  },
  "capture_plan": [
    {"id": "normal", "mode": "window"},
    {"id": "expanded-top", "mode": "window"}
  ]
}
```

上述只是 schema 方向，最终字段由实现阶段通过 Lucerna 与第二个桌面项目回放冻结。项目适配负责“如何找到本应用和进入目标状态”；中央脚本负责“如何安全捕获、验证和记录”。

## 六、Windows 原生证据工具合同

### 6.1 一次性机器诊断

`native-evidence-doctor.ps1` 至少检查：

- 当前会话是否有交互桌面；
- PowerShell / .NET / `System.Drawing` 可用性；
- DWM、DPI awareness、窗口枚举和 `PrintWindow` 能力；
- 当前权限能否读取目标进程路径和 HWND；
- 结果目录可写；
- 一个受控自测窗口能否被捕获为非黑、非透明、具有内容的图像；
- native-host 与 sandbox 执行边界是否被正确识别。

诊断结果写入机器本地、Git 忽略的缓存。OS、显卡驱动、缩放或执行宿主变化时允许重跑。项目任务只消费 PASS 或明确 failure class，不从头发明诊断命令。

### 6.2 窗口捕获

`capture-native-window.ps1` 的通用能力至少包括：

- 解析并规范化目标 executable；
- 校验文件 hash、mtime 和可选 source/build identity；
- 只接受路径与 adapter 同时匹配的进程；
- 按 PID 枚举顶层 HWND，并按允许的 class/title 约束；
- 进程 DPI-aware；
- 使用 DWM extended frame bounds；
- 优先 `PrintWindow(PW_RENDERFULLCONTENT)`；
- 仅在同一已验证 HWND 上做一次有界 `CopyFromScreen` 回退；
- 拒绝全黑、全透明、尺寸不符、内容不足和旧文件；
- 输出 PNG 与机器可读 metadata；
- 默认不重启应用；任何重启必须由项目 adapter 明确授权且只作用于精确进程。

### 6.3 捕获模式

- `window`：默认，仅目标窗口。
- `scroll-sequence`：项目负责滚动状态，中央工具按顺序捕获 top/middle/bottom 或状态清单。
- `placement`：只有任务栏、托盘、多显示器锚定或桌面几何声明需要时才允许整屏/区域证据。
- `component-crop`：仅作补充，不能替代完整窗口或整产品判断。

禁止把任意桌面截图后手工裁剪作为普通窗口证据的默认路线。

### 6.4 统一 failure class

至少统一：

```text
WRONG_CANDIDATE
PROCESS_NOT_FOUND
WINDOW_NOT_FOUND
WINDOW_NOT_VISIBLE
NO_INTERACTIVE_DESKTOP
EXECUTION_CONTEXT_NOT_NATIVE_HOST
READINESS_NOT_PROVEN
CAPTURE_UNSUPPORTED
BLACK_CAPTURE
TRANSPARENT_CAPTURE
CONTENT_NOT_DETECTED
DIMENSION_MISMATCH
PERMISSION_MISMATCH
STALE_EVIDENCE
```

feature task 遇到工具失败时只允许一次有界重试和一次明确替代路线。没有新增信息时不得重复完整构建、完整审查或让用户接管。

## 七、交互证明由 Codex 承担

### 7.1 普通可安全操作

只要能在本机安全执行，Codex 必须自己验证：

- X、Esc、tray reopen、outside-click；
- disclosure 展开/收起；
- Refresh 与局部反馈；
- Manage / Details / Back / Cancel；
- folder chooser 打开并取消；
- 表单 validation；
- 只读导航和本地可逆设置。

每个动作至少记录：控件为何可见、是否 enabled、真实输入、预期后置条件、实际后置条件、是否存在竞争路径。

### 7.2 竞争路径

如果多个路径都能产生同一结果，例如 X、Esc、失焦都会隐藏窗口，仅观察“窗口不见了”不足以证明 X 可点击。项目 adapter 或项目测试必须提供真实 hit target、UI Automation、DOM-to-screen rect、事件原因或同等因果证据。

中央能力定义合同和 evidence shape，但不强迫所有框架采用同一底层自动化技术。

### 7.3 用户专属边界

下列动作不得为验收强行执行：

- 秘密、Recovery Key、私钥和真实凭据输入；
- OAuth / Duo / 账号授权中的真人确认；
- 付费调用或资源消耗；
- 不可逆远端写入、删除、同步和权限变更；
- 用户个人文件夹、账号或业务方向选择。

Codex 应把流程推进到安全的 user-only boundary，并证明该边界可达、可理解且无明显 P2 缺陷。

## 八、Codex / GPT Work / 用户职责矩阵

| 事项 | Codex | GPT Work | 用户 |
|---|---|---|---|
| 精确 commit / executable / PID / HWND | 负责 | 消费证据 | 不参与 |
| 单元、集成、回归、构建 | 负责 | 不重复 | 不参与 |
| X、Esc、tray、普通按钮真实操作 | 负责 | 可抽查产品逻辑 | 不参与 |
| 截图与证据 manifest | 负责 | 读取并独立判断 | 不参与 |
| 层级、密度、审美、整体一致性 | 先自检 | 主审 | 只做最终取舍 |
| 探索性浏览与实现者盲点 | 先自检 | 主审 | 不做普通 QA |
| 秘密/账号授权/个人选择 | 推进到边界 | 检查边界表达 | 必要时执行 |
| 不可逆外部动作 | 默认禁止 | 不要求 | 仅明确批准后执行 |
| 最终主观接受 | 提供完成候选 | 提供独立结论 | 决定 |

GPT Work 的稳定输入应为独立 PNG、短视频（如确有动作/动效需要）和 manifest。不得只给一张极长拼图或一个 PDF；也不得要求 GPT Work 先修底层 capture 工具才能开始产品判断。

## 九、审查升级与成本控制

### S1：局部修复

例如单一文案、间距、错误状态映射、小型按钮行为。

- Codex 定向回归 + 真实表面验证；
- 默认不调用 GPT Work；
- 若修复暴露整产品设计缺陷，升级为 S2/S3。

### S2：有界界面变化

例如一个模块、一个 setup flow、一套状态组件。

- Codex 完整覆盖受影响状态与相邻行为；
- 只有明显改变视觉层级、交互模型或跨组件一致性时调用 GPT Work；
- GPT Work 不重新跑底层机械检查。

### S3：整产品/重设计/正式发布

- Codex 完成完整机械和原生自检；
- GPT Work 做一次独立产品审查；
- Codex 修复明确 findings；
- 只有修复 materially 改变整体表面或仍有 P0/P1 时，才进行一次 GPT Work 终审。

正常目标是 GPT Work 一次主审，必要时一次终审。禁止形成 Reviewer → 修 harness → 重跑全部 → 再发现同类问题的无界循环。

## 十、证据包与审查结果

建议 manifest 至少包含：

```text
candidate_commit
executable_path
executable_sha256
pid
hwnd
window_identity
capture_platform
capture_method
capture_bounds
machine_doctor_result
readiness_evidence
state_id
interaction_ledger
screenshot_path
screenshot_sha256
captured_at
producer_visual_observation
known_limits
```

GPT Work 输出只需要：

```text
REVIEW_RESULT=PASS|FAIL
P0=<count>
P1=<count>
P2=<count>
FINDINGS=<stable IDs>
COVERAGE_GAPS=<none or list>
RE_REVIEW_REQUIRED=YES|NO
```

Codex 关闭具体 finding 时，应保留 finding ID、修复证据和受影响范围。无关状态不重复全量验收。

## 十一、真实经验持续反馈

每个采用 Frontend Design 的正式 UI 任务在结果中增加：

```text
PROJECT_LOCAL_FINDINGS=
FRONTEND_DESIGN_GENERIC_FINDINGS=
WORKFLOW_GENERIC_FINDINGS=
PLUGIN_FEEDBACK_WRITTEN=YES|NO
PLUGIN_FEEDBACK_LOCATOR=
```

处理规则：

1. 项目业务、视觉方向和特有状态留在项目仓库。
2. 换成另一个产品仍可能复现的问题写回对应中央 plugin TODO。
3. 项目 thread 先记录真实事实；中央 maintainer 负责去重、抽象、promotion 和发布。
4. 中央能力正式发布并经项目回放验证后，项目删除重复的临时通用规则，只保留薄适配和项目特例。
5. 不因为每次任务都必须“产生经验”而制造空洞 TODO；只有真实失败或明确的新通用能力才写回。

## 十二、Lucerna 迁移策略

### 立即保留

- exact release identity；
- frontend-mounted/readiness；
- tray reopen、X、Esc、process survival；
- console flash 检查；
- window-only capture；
- 黑图/透明图/内容验证；
- provider/state 定向回归。

### 从日常 feature 主路径移除

- 每次小修都要求独立 Reviewer；
- 同一候选连续两次 preflight 才允许任何视觉审查；
- Reviewer 重新复制 Producer 已经可靠证明的所有机械事实；
- 截图 helper 出错后无界修 harness；
- 每次修一处都从头重跑完整 01054；
- 让用户点击普通按钮或发现明显布局问题。

### 中央 0.5 发布前

Lucerna 继续使用现有 `capture-lucerna-window.ps1` 和原生 smoke 作为项目 oracle，并按本文件的职责矩阵和 S1/S2/S3 规则执行。中央实现完成后，把通用逻辑迁入 `native-desktop-evidence`，Lucerna 只保留 adapter、readiness 和产品特有交互测试。

## 十三、Frontend Design 0.5 验收门槛

正式发布至少满足：

1. `frontend-visual-systems` 能正确选择或跳过原生 delegate。
2. Web、移动端、docs-only、backend-only 任务不被错误强制进入原生流程。
3. Windows doctor 与 capture self-test 可在至少两台机器上运行，不依赖项目仓库的私有路径。
4. Lucerna replay 能捕获精确真实 release，并证明 X/Esc/tray 等项目交互仍由项目 adapter/测试负责。
5. 至少一个独立桌面项目 replay 证明脚本没有硬编码 Lucerna。
6. 100%、125%、150% DPI 中至少覆盖两档真实运行，并保留 bounds/scale 证据。
7. 黑图、透明图、错误 PID、旧证据、无交互桌面和 sandbox/native-host 错配均 fail closed。
8. S1 不触发不必要的 GPT Work；S3/release 能生成完整 review pack。
9. 真实项目 feedback 写回路径有回归或可审计 replay。
10. source、generated plugin、registry、版本、changelog、CI 和 candidate replay 全部闭环。

## 十四、建议实现顺序

1. 以 Lucerna helper 为 oracle，标记通用逻辑与项目特例；
2. 冻结 adapter/manifest schema；
3. 实现 Windows doctor、capture 和 self-test；
4. 建立 `native-desktop-evidence` skill 并接入协调器；
5. 加入 S1/S2/S3 的 Codex/GPT Work 分工；
6. Lucerna read-only replay；
7. 第二个桌面项目 replay；
8. unrelated web/mobile regression；
9. 独立 review、CI、版本和发布收口。

## 十五、开始实施的判定

本提案已具备进入有限范围正式实现的条件：

- 真实失败有仓库证据；
- 当前 active rule 与缺失能力已区分；
- 用户明确把它确认为长期跨项目偏好；
- 项目特例和中央通用层边界已写清；
- Lucerna 的继续开发不依赖中央版本先发布。

因此该方向在 #97 下进入 `PROMOTE_NOW`，但生产代码、版本与 Marketplace 变更仍必须走 `workflow-core + ai-skills-core + web-development` 的正式 Reviewed Handoff、回放、CI 和发布流程。