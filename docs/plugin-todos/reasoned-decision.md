# Reasoned Decision — Plugin TODO

> Planned dedicated Marketplace plugin. The design is currently converged for review but not yet implemented in production. Canonical design entry: `docs/design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md`.

## 2026-11-05：现实解空间调查不能漏掉论坛、社区与本地语言长期讨论
status: NEW
source: Local Compute Infrastructure / macOS 微信自动更新真实排查
evidence: `docs/design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md`; https://www.v2ex.com/t/1176334 ; https://linux.do/t/topic/990633 ; https://github.com/sunnyyoung/WeChatTweak ; https://github.com/sunnyyoung/WeChatTweak/issues/847 ; https://github.com/sparkle-project/Sparkle/discussions/2849
problem: 冻结架构已经要求先做 Solution-Space Discovery，但真实回答仍可能把“查已有方案”执行得过窄，只看当前仓库、官方文档和普通 GitHub 代码搜索，没有主动进入该生态真正承载长期用户经验的论坛、Issue/Discussion 和本地语言社区。对于依赖未文档化产品行为、版本回归、真实兼容性或长期 workaround 的问题，这会漏掉高信号证据，并使 Agent 过早进入自行诊断或 Build。微信案例中，V2EX 与 LINUX DO 很快就出现了“设置里关闭仍自动下载/重启升级”的重复现场报告，GitHub 也存在长期维护的 WeChatTweak“阻止自动更新”能力及相关自动更新 issue；这些证据如果一开始不查，真实解空间就是残缺的。
project-specific context: 微信具体下载域名、PF 规则、缓存目录、WeChatTweak patch、App Store 版本差异都只是本案例候选证据，不应直接提升为 Reasoned Decision 的通用规则。通用要求应是：按问题生态主动覆盖高信号社区来源，包括但不限于 GitHub Issues/Discussions、V2EX、LINUX DO、Reddit、厂商论坛、Stack Exchange、专业社区、博客/配置仓库等；来源集合必须问题驱动、允许多语言，不能机械硬编码成固定站点清单。论坛经验用于发现重复现场、失败模式和成熟 workaround，关键结论仍需与官方能力、代码/实现或真实验证交叉核对。
