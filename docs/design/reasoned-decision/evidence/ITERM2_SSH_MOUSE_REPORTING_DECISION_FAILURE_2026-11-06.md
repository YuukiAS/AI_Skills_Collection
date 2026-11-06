# iTerm2 SSH 断线后残留鼠标报告：Reasoned Decision 真实负例

Date: 2026-11-06
Source: PC+Server+VPS 真实任务
Purpose: Reasoned Decision negative regression evidence
Underlying owner: `YuukiAS/Local_Compute_Infrastructure`

## 失败

现场已经确认：SSH 异常结束后，iTerm2 残留 mouse reporting 状态，回到本地 zsh 后鼠标事件以 SGR mouse 序列进入命令行。

第一次回答正确识别了故障族，但在现实解空间调查尚未完成时，就把本地 zsh `precmd` 中主动关闭 1000/1002/1003/1006 mouse modes 的 hook 升级成长期推荐。

这个方案可能有效，但决策流程不合格：当前 iTerm2 的原生 Profile 能力还没有查完，就提前进入了自建 shell workaround。

## 新证据与 Decision Delta

继续开放式调查后，当前 iTerm2 官方文档明确提供：

`Restrict mouse reporting to alternate screen mode`

官方说明：启用后，鼠标移动或点击只在 interactive application / alternate screen 中上报。同一官方文档把 `tmux`、`vim`、`less` 等列为 alternate-screen 使用者。

证据：
- https://iterm2.com/documentation-preferences-profiles-terminal.html
- https://iterm2.com/feature-reporting/
- https://iterm2.com/documentation-tmux-integration.html
- https://iterm2.com/documentation-shell-integration.html

因此出现合法 Decision Delta：存在一个更小、原生、直接覆盖当前成功标准的候选。原 zsh hook 从 Recommended 降级为 Extend fallback。

## 重做后的排序

1. Adopt：启用 iTerm2 原生 `Restrict mouse reporting to alternate screen mode`，保持 `Enable mouse reporting` 开启。
2. Shell Integration：继续保留和核对，但不能单独视为已经解决当前复发。
3. `Session > Reset`：仅作为单次人工恢复。
4. 全局关闭 mouse reporting：违反保留 tmux/TUI 鼠标能力的约束，淘汰。
5. Extend：只有原生限制经过无损验证仍不足时，才考虑 zsh `precmd` DECRST hook。

## 回归断言

- 成熟产品问题在 shell hook、wrapper、launchd、patch 之前，必须先查当前版本原生设置。
- “逻辑可行”不等于“当前首选”；只要更小原生能力尚未调查，自建 workaround 只能保持 Candidate。
- 修复 stuck mouse reporting 不能顺手关闭用户需要的 tmux/TUI mouse reporting。
- 用户不愿主动破坏健康连接时，第一轮验证必须使用无损、局部、可控的方法。
- fallback 必须有明确升级条件，不能和原生方案一起默认叠加，否则无法判断谁真正解决问题。
