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

## 2026-11-10：推荐前必须核实会改变排序的对象级规格，不能用类别标签代替真实尺寸
status: NEW
source: PC+Server+VPS / Keychron Z6-87 Ultra 长时间办公掌托选型
evidence: 用户当前商品规格页明确给出 Z6-87 Ultra 约 329×148×42mm；Keychron 官方 Silicone Palm Rest 规格表显示 PR47/PR67 为 327.5×79.5×18mm、PR50 为 365×79.5×18mm；OSHA Computer Workstations / Wrist-Palm Supports 要求掌托与键盘前沿的宽度、高度和坡度匹配
problem: Agent 已经知道用户要为一把将长期高强度使用的键盘选择掌托，却在没有先核实该具体 Z6-87 Ultra 的真实机身尺寸时，先按“87 键 = 标准 TKL ≈ 360mm”这一类别先验排序候选，并把 365mm 的 Q3/V3 硅胶掌托和 362mm 的 HyperX TKL 提升为强推荐；甚至在关键尺寸仍未知时使用“最终推荐”“不会再改”等过强措辞。用户随后给出的当前商品规格页显示 Z6-87 Ultra 虽有 86 键，但机身宽度只有约 329mm。这个事实直接改变方案排序：此前因“75%”标签被错误排除的 327.5mm Keychron 掌托，反而在物理宽度上最接近真实键盘。这里暴露的不是单纯漏查一个数字，而是对象级关键前提没有进入 Recommendation Gate：当某个可核实规格会直接决定兼容性、人体工学、安全、成本或长期使用体验时，必须先查真实对象规格，再比较候选；类别名、配列名、行业常见尺寸和相邻型号只能用于发现候选，不能替代对象级证据。若关键前提未核实，只能给条件性推荐，不能冻结“最终选择”。
project-specific context: Z6-87 Ultra、329×148×42mm、PR47/PR67、PR50、HyperX TKL、CHERRY、TOTO、KPTE 都只是本案例对象。中央插件应吸收的是：先识别“会改变排序的关键规格”，优先从当前商品页/官方规格/真实设备获得对象级事实；比较必须按实际物理属性和用户成功标准，而不是按产品类别标签机械映射；关键规格缺失时降低结论强度；一旦新对象级证据出现，只局部重排受影响候选并明确 Decision Delta，不能假装前一轮已经足够核实。

## 2026-11-10：同一故障复发时不得复活已淘汰路线；现实解空间必须覆盖社区失败经验，并收缩到一个现场裁决点
status: NEW
source: PC+Server+VPS / ThinkPad E16 Microsoft Edge shared updater 再次绕过既有冻结
evidence: `docs/design/reasoned-decision/evidence/EDGE_WINDOWS_DECISION_FAILURE_2026-11-05.md`; `YuukiAS/Local_Compute_Infrastructure/windows/edge/` 现有治理与 2026-11-10 实机记录；本轮 2026-11-10 连续决策对话
problem: 11 月 5 日已经通过真实现场证据确认该 ThinkPad 为 Workgroup、Edge Update 日志为 `is_managed=0`，并因此淘汰依赖受管 Windows 条件的 Edge Stable 产品级 `Update{GUID}` 路线。11 月 10 日新的事故证明旧治理仍有旁路：Copilot/shared Edge Update core 可以直接启动 `MicrosoftEdgeUpdate.exe /ua /installsource core`，并把下载交给 BITS / Delivery Optimization，从而在服务、计划任务和 updater 自身出站防火墙都被冻结的情况下重新 stage Edge。Agent 面对这条新证据时，第一反应却再次提出已经被前一轮现场证据淘汰的产品级策略，违反了 `ELIMINATED_ROUTES / DO_NOT_REVIVE`；随后又把 AppLocker 提升为可能主路线，在用户要求按 Reasoned Decision 重做后才回到旧证据并撤回。继续调查时，Agent 又过度集中于微软官方文档，没有主动覆盖 GitHub Issues/Discussions、Reddit、ElevenForum、Microsoft Community、Stack Exchange 等真实长期使用与失败经验，直到用户明确指出“Reasoned Decision 没写查论坛？”才补齐社区证据。最终判断才收缩为一个真正会改变选择的未知：当前机器、当前 updater、当前真实事故命令在 updater 级自动检查关闭后，是否仍能进行检查、下载并重新 stage Edge；这个未知可以由同路径现场实验直接裁决，而不需要继续生成新的完整架构。
project-specific context: Edge 143/157、Copilot、WebView2、`MicrosoftEdgeUpdate.exe /ua /installsource core`、BITS/Delivery Optimization、`AutoUpdateCheckPeriodMinutes`、AppLocker/App Control、具体 GUID 和 Local Compute 脚本都只属于本案例。中央插件应吸收以下通用要求：1）新事故只允许重新打开被新证据直接影响的判断，不能把已经由强现场证据淘汰的路线自动复活；若确需复活，必须先写明原淘汰证据为何失效；2）现实解空间调查必须按问题生态覆盖官方资料、代码/仓库、Issue/Discussion、论坛、Reddit、Stack Exchange、本地语言社区和重复失败案例，不能把“查官网”误当成完整 prior-art；3）证据排序应保持“当前对象真实现场 > 当前 canonical/实现证据 > 官方适用范围 > 社区重复经验 > 模型推断”，社区用于发现旁路、长期失败和成熟 workaround，但不能压过当前机器已经证明的事实；4）此前已经宣称 production-worthy 的方案若被真实事故穿透，应首先做 premise correction，明确“之前验收覆盖了什么、漏了哪类真实触发路径、因此哪项结论失效”，而不是悄悄在原方案上再堆一层；5）连续两次以上改口后必须停止继续扩候选，冻结目标、已确认事实、已淘汰路线和唯一关键未知，用最小的同型真实验证裁决；6）面向用户先用人话说明“原来系统靠什么挡、为什么会漏、现在要把控制点移到哪里、成功后日常会变成什么样”，不要先交付长 prompt、策略名和审计字段让用户自己理解架构；7）一旦现场验证通过并冻结推荐，后续只有合法 Decision Delta 才允许再次改口，用户的“你确定吗”本身不构成 Decision Delta。
