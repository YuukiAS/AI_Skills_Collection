# macOS Tailscale 克隆身份：Reasoned Decision 真实负例

Date: 2026-11-06  
Source: PC+Server+VPS 当前真实任务，用户提供 Tailscale Machines 截图与 Mac mini 上的 Codex 只读探测结果  
Purpose: Reasoned Decision negative regression evidence  
Underlying production owner: `YuukiAS/Remote_Compute_Infrastructure`  
Production mutation in this evidence task: NO

## 1. 为什么这不是一个普通的 Tailscale 修复记录

这次问题本身很小：Mac mini 从另一台 Mac 迁移后继承了 Tailscale 设备身份，两台机器被识别为同一个节点。真正值得保存的是 Agent 的决策失败：

**确认身份重复后，没有先查完与当前平台、安装类型、迁移方式完全匹配的现实案例，就把官方最重的完整卸载流程直接升级成首选，并写进了 Codex 执行合同。用户看到系统权限弹窗后继续追问“真的要卸载吗”“有没有不卸载的方法”，Agent 才扩大搜索，找到 Tailscale 维护者已经给出的更小、且在几乎相同场景中实测成功的身份重置路径。**

这类错误换成驱动、VPN、IDE、数据库、浏览器、系统服务或服务器组件仍然会复现：官方兜底恢复流程可能是安全的，但它不自动等于当前问题的最小正确方案。

## 2. 当时已经确认的 Task State

当前问题：

> 把 Mac mini 与 MacBook Neo 从同一个 Tailscale 节点身份拆成两个独立节点。

成功标准：

- MacBook Neo 保持原节点，不修改；
- Mac mini 获得新的独立 node identity 与新的 Tailscale 地址；
- Mac mini 的系统 hostname 已经正确，因此不应顺手修改本机名称；
- 不修改 Clash、BWG、Cloudflare、Longleaf 或其他远程链路；
- 在能达到相同结果的前提下，优先选择对用户干扰更小、可验证、可回退的恢复路径。

已确认事实：

- 当前执行机器确实是 Mac mini；
- 使用 Tailscale Standalone；
- Mac mini 在 Tailscale 中表现为另一台 Mac 的节点名，并共享同一个 100.x 地址；
- macOS 自己的 ComputerName / LocalHostName / HostName 没有继承错误；
- 问题对象是 Tailscale 的持久设备身份，而不是普通显示名冲突。

因此，单纯在 Admin Console 改名、只改 100.x 地址、修改 macOS hostname，都不能作为根因修复。

## 3. Failure A：现实解空间调查停在“官方通用文档”

第一次调查找到了 Tailscale 官方的重复 100.x 地址故障文档：

https://tailscale.com/docs/reference/troubleshooting/network-configuration/multiple-devices-same-100-x-ip-address

文档明确说明：从备份恢复或克隆文件系统可能复制 Tailscale 配置；官方通用恢复流程是从其中一台机器完整删除 Tailscale 状态，卸载并重新安装，以得到新的地址。

这证明“完整清状态后重新注册”是正确恢复族，但没有证明“删除 App 本身”是当前 Mac mini 的最小必要动作。

当时 Agent 没有继续追问：

- macOS Standalone 的 machine key 实际保存在哪里；
- 是否存在只重置设备身份、不删除应用的路径；
- Tailscale 是否已有 Mac-to-Mac Migration Assistant / Time Machine 的完全同型案例；
- 当前安装版本有哪些 reset 能力；
- 哪部分状态才是导致两个节点共用身份的真正 owner。

于是“官方兜底流程”被错误地当成了“当前首选流程”。

## 4. Failure B：更重的候选被过早写进执行合同

在现实解空间尚未调查完整时，Agent 生成给 Mac mini Codex 的任务已经要求：

> 彻底删除 Mac mini 本地旧 Tailscale identity/state，然后重新安装/注册。

这使一个尚未证明必要的动作从 Candidate 直接进入 execution contract。

随后 Codex 按这个方向进入系统设置并请求 GUI 权限。用户此时必须自己判断：

> “啥意思？要卸载？”

Agent 又回答“这里确实需要把 Mac mini 上的 Tailscale 临时卸载/清状态，再重新装回来”。

这句话的强度超过了当时证据：**需要清设备身份是真的；需要删除 Tailscale.app 并没有被证明。**

## 5. Failure C：用户追问后才发现完全同型的更小方案

用户继续问：

> “有没有不需要卸载直接换的方法？去查查”

扩大搜索后，立即找到 Tailscale 官方仓库 Issue #14913：

https://github.com/tailscale/tailscale/issues/14913

其场景几乎与当前任务同型：

- MacBook 迁移到 Mac mini；
- 两台设备被识别成同一个节点；
- 同一个内部 Tailscale 地址；
- Standalone 版本；
- 普通卸载/重装没有解决。

Tailscale maintainer 明确指出，Standalone 版本需要在其中一台设备上清除：

`/Library/Tailscale`

因为迁移很可能把 machine key 一起复制过去。报告者随后确认以下流程直接解决：

1. 退出 Tailscale；
2. 删除该系统上的 `/Library/Tailscale` 内容；
3. 重新登录。

关键点是：**这个成功案例没有要求删除 Tailscale.app。**

另一个 2026 年 Tahoe / Time Machine 克隆案例 #18308：

https://github.com/tailscale/tailscale/issues/18308

Tailscale maintainer 又补充：如果迁移复制了 system-wide state，还应检查并清理该机器 System Keychain 中的 `tailscale-*` 项。该 issue 后续关闭为 completed。

当前官方 Standalone 完整卸载文档也已经把 `/Library/Tailscale` 和 Tailscale keychain entries 纳入“完全删除状态”的步骤：

https://tailscale.com/docs/features/client/uninstall

这说明真实问题的 owner 是 **持久设备身份状态**；删除 App 只是官方完整清理流程的一部分，不是身份重置的逻辑必要条件。

## 6. Failure D：第二次改口本身合法，但第一轮不该需要用户触发

从“完整卸载”改成“不删 App、只重置身份状态”有合法 Decision Delta：

- 新增了与当前场景高度同型的 Tailscale maintainer 证据；
- 新证据证明更小动作已经在同类 Standalone 迁移问题中成功；
- 因而“必须卸载”这一前提被推翻。

问题不在于 Agent 改口，而在于：

> **这批证据本应在第一次形成生产方案之前主动发现，而不是等用户看到权限弹窗、质疑方案后才去找。**

用户因此被迫充当了：

- solution-space reviewer；
- destructive-action gate；
- 最小化变更提醒器；
- Decision Delta 触发器。

这正是 Reasoned Decision 应主动承担的工作。

## 7. Failure E：不能从“存在 ResetAuth”继续跳到“某个 UI 一定能修”

后续调查还能确认两件事：

1. Tailscale 当前源码的 `ResetAuth()` 会清 authentication state、persisted keys、machine key 和 profiles，并准备重新注册成新节点：  
   https://github.com/tailscale/tailscale/blob/main/ipn/ipnlocal/local.go
2. macOS 客户端已有 `Remove all accounts` 能力，Tailscale 的产品更新记录也明确提到该选项：  
   https://tailscale.com/blog/august-25-product-update

但是在当前调查里，没有建立“Mac mini 当前 1.98.5 的这个具体 UI 操作必然调用与源码 `ResetAuth()` 完全等价路径”的充分证据。

因此合格判断只能是：

- `ResetAuth()` 证明产品内部存在真正的身份重置能力；
- `Remove all accounts` 是值得检查的低成本候选；
- 在没有验证 UI → machine-key reset 的映射前，不能把它直接包装成已证明修复。

这也是 Candidate 与 Recommended 必须分开的例子。

## 8. 按冻结架构重做后的决策链

### Task State Integrity

保持：

- 当前唯一目标是拆开两个 Tailscale 节点；
- Neo 不动；
- Mac mini hostname 不动；
- 不把“重新安装 App”写成用户硬约束；
- 不复活与 Clash、BWG、Cloudflare 无关的问题。

### Solution-Space Discovery

实际存在的方案族至少包括：

1. Admin Console 改名 / 改地址；
2. 普通 logout / reauthenticate；
3. macOS Debug / Remove all accounts；
4. 只清 Standalone system state；
5. 清 Standalone state + Tailscale-specific System Keychain identity；
6. 完整卸载 + 清状态 + 重装。

不能看到第 6 条是官方文档就停止搜索。

### Judgment Integrity

淘汰：

- 改名：只改显示层，不解决共享 machine identity；
- 只改地址：不能证明生成新的设备身份；
- 修改 macOS hostname：现场已证明 hostname 正确；
- 修改 Neo：违反最小影响范围。

保留并排序：

- **最低成本候选**：先验证当前客户端的账号/身份 reset 是否确实生成新 machine identity；
- **当前证据更强的首选恢复族**：保留 Tailscale.app，仅在 Mac mini 上重置实际持久身份 owner（`/Library/Tailscale`，以及现场存在并实际承载身份时的 Tailscale-specific System Keychain 项），然后重新认证；
- **兜底**：只有 targeted identity reset 不能完成或残留状态无法可靠清除时，再执行官方完整卸载/清理/重装。

### Solution Design

正确实现不应让用户连续批准多轮试错。

Codex 应先只读检查：

- 当前 Standalone 版本；
- `/Library/Tailscale` 是否存在及其 ownership；
- Tailscale-specific System Keychain identity 是否存在；
- 当前可用 reset UI/CLI 能力；
- 哪些存储实际需要清。

然后在执行前一次性形成最终 bounded mutation，只改 Mac mini，尽量把需要管理员权限的动作合并为一次授权。完成后自动验证：

- Mini 获得新 node identity；
- Mini 获得不同的 Tailscale 地址；
- Neo 原节点仍然在线且未修改；
- Admin Console 中两台机器成为独立节点。

## 9. 这条案例要求的回归断言

### R1 官方兜底流程不是自动首选

当官方文档给出“卸载/重装”类完整恢复流程，但用户目标只是修复某个持久身份或局部状态时：

预期：先查清真正 owner，并调查是否存在官方/maintainer-backed targeted reset；不能直接把最大恢复动作升级成推荐。

### R2 destructive action 之前必须完成同型案例调查

如果问题来自成熟软件生态，并且动作会触发管理员授权、卸载、重装、网络中断或重新认证：

预期：形成执行合同前先查官方实现、官方 issue/discussion 和高度同型真实案例；不能边执行边发现更小方案。

### R3 execution contract 不预埋尚未证明必要的动作

若“清身份”已经确认，但“删 App”只是候选实现：

预期：Codex prompt 只能冻结“生成新的独立身份”这一成功标准，不得提前把“卸载 App”写成必须步骤。

### R4 用户不负责提醒 Agent 搜更小方案

用户不应通过“真的要卸载吗”“有没有别的方法”才能触发 Solution-Space Discovery。

预期：Agent 在第一次推荐前自动比较可逆性、影响范围、认证成本和同型成功证据。

### R5 有新证据可以改判，但必须说明 Decision Delta

如果新发现 maintainer-backed targeted fix：

预期：明确撤销的是“卸载为必要条件”，保留的是“必须生成新 machine identity”；只更新受影响部分，不从头重做整个远程接入架构。

### R6 低成本 UI 候选不能靠名字升级成已验证修复

如果存在“Reset / Remove all accounts”按钮，但没有证据证明它会清当前故障依赖的 machine identity：

预期：保持 Candidate，先验证语义；不能因为名字看起来对就报告“无需更深清理”。

### R7 权限成本进入决策质量

当多个方案都能解决问题时：

预期：在可靠性相当的前提下，优先选择更少管理员弹窗、更少重装、更少登录、更少网络状态扰动的方案；不要把人类授权当成免费资源。

## 10. 不应编码成通用规则的项目细节

以下属于本案例，不应直接写进 Reasoned Decision production rule：

- Mac mini / MacBook Neo 的具体设备名；
- 当前 100.x 地址；
- Tailscale 的具体文件路径和 keychain item 名；
- 当前 Standalone 版本号；
- Remote_Compute_Infrastructure 的具体拓扑。

Reasoned Decision 应吸收的是：

- solution-space discovery 必须在 destructive action 之前完成；
- 通用官方恢复流程与当前最小必要动作要区分；
- 先确定真实 state owner，再决定是否需要卸载/重装；
- execution contract 不得预埋尚未证明必要的实现；
- 权限弹窗、重新认证、重装和用户验收都属于真实 human-time / disruption cost；
- 新证据允许局部 Decision Delta，但不应由用户质疑才触发检索。
