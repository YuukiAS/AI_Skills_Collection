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
