# Reasoned Decision — Plugin TODO

> Planned dedicated Marketplace plugin. The design is currently converged for review but not yet implemented in production. Canonical design entry: `docs/design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md`.

## 2026-11-05：现实解空间调查不能漏掉论坛、社区与本地语言长期讨论
status: NEW
source: Local Compute Infrastructure / macOS 微信自动更新真实排查
evidence: `docs/design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md`; https://www.v2ex.com/t/1176334 ; https://linux.do/t/topic/990633 ; https://github.com/sunnyyoung/WeChatTweak ; https://github.com/sunnyyoung/WeChatTweak/issues/847 ; https://github.com/sparkle-project/Sparkle/discussions/2849
problem: 冻结架构已经要求先做 Solution-Space Discovery，但真实回答仍可能把“查已有方案”执行得过窄，只看当前仓库、官方文档和普通 GitHub 代码搜索，没有主动进入该生态真正承载长期用户经验的论坛、Issue/Discussion 和本地语言社区。对于依赖未文档化产品行为、版本回归、真实兼容性或长期 workaround 的问题，这会漏掉高信号证据，并使 Agent 过早进入自行诊断或 Build。微信案例中，V2EX 与 LINUX DO 很快就出现了“设置里关闭仍自动下载/重启升级”的重复现场报告，GitHub 也存在长期维护的 WeChatTweak“阻止自动更新”能力及相关自动更新 issue；这些证据如果一开始不查，真实解空间就是残缺的。
project-specific context: 微信具体下载域名、PF 规则、缓存目录、WeChatTweak patch、App Store 版本差异都只是本案例候选证据，不应直接提升为 Reasoned Decision 的通用规则。通用要求应是：按问题生态主动覆盖高信号社区来源，包括但不限于 GitHub Issues/Discussions、V2EX、LINUX DO、Reddit、厂商论坛、Stack Exchange、专业社区、博客/配置仓库等；来源集合必须问题驱动、允许多语言，不能机械硬编码成固定站点清单。论坛经验用于发现重复现场、失败模式和成熟 workaround，关键结论仍需与官方能力、代码/实现或真实验证交叉核对。


## 2026-11-06：破坏性恢复前必须先找到真实 state owner 与更小同型修复
status: NEW
source: PC+Server+VPS / macOS Tailscale 迁移后重复设备身份真实排查
evidence: `docs/design/reasoned-decision/evidence/TAILSCALE_MACOS_CLONED_IDENTITY_DECISION_FAILURE_2026-11-06.md`; https://tailscale.com/docs/reference/troubleshooting/network-configuration/multiple-devices-same-100-x-ip-address ; https://github.com/tailscale/tailscale/issues/14913 ; https://github.com/tailscale/tailscale/issues/18308 ; https://tailscale.com/docs/features/client/uninstall
problem: Agent 已确认 Mac mini 与另一台 Mac 共用 Tailscale node identity，却在只读调查尚未覆盖 macOS Standalone 的同型迁移案例和持久身份实际存储位置时，就把官方“完整卸载、清状态、重装”的通用兜底流程升级成首选，并写进 Codex 执行合同，导致系统权限请求已经出现。用户必须继续追问“真的要卸载吗”“有没有不卸载的方法”，Agent 才找到 Tailscale maintainer 已验证的更小恢复路径：保留 App，只重置 Standalone 的 system-wide identity state，必要时再清该机 Tailscale-specific System Keychain identity 后重新认证。新证据足以合法撤销“卸载是必要条件”，但这些证据本应在第一次形成生产方案前由 Agent 主动发现。这里暴露的是 Solution-Space Discovery、方案状态强度、execution contract 中立性和 human-time/disruption cost 的共同缺口：官方兜底流程不能自动等于当前最小必要动作，管理员授权、重装、重新登录和网络中断也不能被当成免费成本。
project-specific context: Mac mini / MacBook Neo 名称、Tailscale 具体 100.x 地址、`/Library/Tailscale`、具体 keychain item、Standalone 版本和 Remote Compute 拓扑只属于本案例，不应直接编码成通用规则。中央插件后续只需要吸收“先定位真实 state owner、在 destructive action 前完成同型现实解空间调查、不要把尚未证明必要的卸载/重装预埋进执行合同、用合法 Decision Delta 局部改判、把用户授权与中断成本纳入方案排序”这些跨项目能力。

## 2026-11-06：成熟产品的原生能力调查必须先于 shell/dotfile workaround
status: NEW
source: PC+Server+VPS / iTerm2 SSH 异常断开后残留 mouse reporting 真实排查
evidence: `docs/design/reasoned-decision/evidence/ITERM2_SSH_MOUSE_REPORTING_DECISION_FAILURE_2026-11-06.md`; https://iterm2.com/documentation-preferences-profiles-terminal.html ; https://iterm2.com/feature-reporting/ ; https://iterm2.com/documentation-tmux-integration.html ; https://iterm2.com/documentation-shell-integration.html
problem: Agent 正确识别 SSH/tmux/TUI 异常结束后 iTerm2 mouse reporting 状态残留这一故障族，却在没有完成当前 iTerm2 原生 Profile 能力调查时，直接把本地 zsh `precmd` 中发送 DECRST 1000/1002/1003/1006 的 hook 升级为长期推荐。继续开放式调查后发现 iTerm2 已提供 `Restrict mouse reporting to alternate screen mode`，它能在保留 tmux/TUI alternate-screen mouse reporting 的同时，把普通 shell prompt 排除在 mouse report 注入之外。新证据构成合法 Decision Delta：原生设置应先作为 Adopt 方案验证，zsh hook 只能降级为原生方案不足时的 Extend fallback。该案例要求插件把“当前产品版本的原生设置/恢复能力”明确纳入成熟产品问题的早期 Solution-Space Discovery，并要求 fallback 有明确升级条件，避免把用户不需要维护的 workaround 提前固化。
project-specific context: MX Master 3S、Mac mini、当前 iTerm2 Profile、Longleaf 和具体 SGR 坐标串只属于本案例。通用规则应是：成熟产品先查原生能力；逻辑可行的 workaround 在原生能力未调查完前不能升级为推荐；修局部状态不能顺手关闭用户仍需要的正常能力；用户拒绝主动破坏健康系统时使用无损验证。

## 2026-11-07：连续追着局部症状换方案，导致“能不能实现整体体验”一直没有被真正回答
status: NEW
source: PC+Server+VPS / Legion Y9000P 通过 UU Remote 操作 Mac mini 的键盘体验对齐
evidence: `docs/design/reasoned-decision/evidence/UU_REMOTE_KARABINER_DECISION_FAILURE_2026-11-07.md`
problem: 用户真正要的是“Legion 远控 Mac mini 时，键盘体验尽量与直接使用 Mac mini 上的 Dell Windows 键盘一致，同时不把现有 Karabiner 搞成两套难维护配置”。Agent 前几轮却依次把问题缩成 ChatGPT 的 `Ctrl+Enter`、建议 UU 全局 `Ctrl -> Command`、再转向“只开 CGEventTap fallback”，每轮都抓住了一个局部机制，却没有先冻结整体成功标准，也没有在连续方案被新事实推翻后收缩到唯一关键未知。用户因此必须不断补充 `Ctrl+A`、Terminal 语义和“我要和实体操作一样”的要求，最后显式要求按 Reasoned Decision 重做。重新读取 Local Compute canonical、调查 Karabiner 原生能力和设备身份限制后，才收敛为“优先复用现有 Windows 键盘语义，只解决 UU 输入如何进入同一处理体系以及无设备身份的残余差距”，并正确把它保持为待现场验证的候选，而不是已经完成的长期方案。该案例要求 Reasoned Decision 在非平凡故障中把用户的整体体验目标当作 Task State，而不是让最新症状接管问题；连续两次路线被推翻后必须停止继续生成完整新方案，先找唯一真正改变选择的未知；成熟产品和已有 canonical 必须先做能力映射，再决定 Extend；用户可见结论必须先回答“能不能做到、能做到多接近、为什么、还差什么验证”，不能用实现细节代替决策。
project-specific context: Legion Y9000P、UU Remote、Mac mini、Dell/Xiaomi VID/PID、ChatGPT bundle、具体 Karabiner 规则、CGEventTap 和未来可能采用的会话检测方式都属于本案例技术背景。中央插件应吸收的是“整体成功标准优先于局部症状、连续失败后收缩关键未知、先复用当前 canonical/原生能力、候选状态不能冒充 production、最终回答必须让用户直接知道能否实现及边界”这些通用判断行为。


### 2026-11-07 follow-up：多入口任务先形成“场景 → 期望行为”矩阵，再决定自动化方式
status: NEW
source: 同一 UU Remote + Karabiner 案例的后续正向收敛
evidence: docs/design/reasoned-decision/evidence/UU_REMOTE_KARABINER_DECISION_FAILURE_2026-11-07.md
problem: 在主键位方案已经通过验证后，Agent 一度把“Karabiner 重启后恢复 UU 模式”理解成单一持久状态问题，先后考虑手工开关、永久开启和 LaunchAgent 恢复。用户继续说明自己会从 Legion、ThinkPad、MacBook Neo、Universal Control 和本地实体键盘多种入口操作同一台 Mac mini 后，才暴露出真正的长期成功标准：不同入口需要不同语义。这个新约束构成合法 Decision Delta，推翻的是“永久单一模式”，而不是已经成立的底层输入路径和规则复用。开放式调查又发现现有 UUyc-companion 已能读取当前控制端设备名和平台，因此最终应优先 Compose：Windows 控制端自动进入 Windows 语义，macOS 控制端和 Universal Control 保持 Mac 语义，本地实体键盘继续按设备身份处理。插件应吸收一个通用要求：只要任务涉及多个设备、身份、入口、环境或角色，且自动化行为可能因入口不同而变化，形成方案前必须先构造最小“场景/来源 → 期望行为”矩阵；不要先把一个状态开关固化成全局默认，再让用户用追问补齐遗漏场景。用户本轮还明确反馈按 Reasoned Decision 推进后更容易理解，这可作为 reader-facing judgment stability 的正向证据，但不能替代技术验证。

### 2026-11-08 follow-up：只读状态问题先找数据面，GUI / TCC 权限必须有 Gap Proof
status: NEW
source: PC+Server+VPS / UU Remote 控制端平台自动识别最终收敛
evidence: docs/design/reasoned-decision/evidence/UU_REMOTE_KARABINER_DECISION_FAILURE_2026-11-07.md
problem: 用户已经明确希望低侵入、尽量不用 GUI 和新增权限，Agent 也已经找到 UUyc-companion，却先沿用其 Accessibility + 主窗口读取路线，甚至准备让后台 helper 显示 UU 主界面并请求辅助功能授权。直到用户再次指出“最好不用 GUI、可以用代码看”，Agent 才继续调查 UU 的真实数据面，并找到客户端实际使用的只读设备接口 `GET /api/v1/device/groups/of/my`；响应中的 `participants_info` 已直接包含当前控制端平台和角色，最终因此实现了无 GUI、无 TCC 新权限的自动切换。插件应加入通用搜索优先级：对状态读取、连接识别、当前配置等只读任务，先查配置/状态文件、缓存数据库、日志、CLI、IPC/socket、客户端实际使用的只读 API，再考虑 GUI / Accessibility / Computer Use。GUI 自动化和 TCC 权限同样需要 Gap Proof；“现成开源项目通过 GUI 做”不能停止调查，必须继续追到其底层 state owner。两条路线都可行时，优先无权限、无焦点变化、只读、可 fail-closed 的数据面。用户已经明确低侵入偏好时，这个约束必须进入后续执行 prompt，不能等权限弹窗出现后才回头优化。
