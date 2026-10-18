# Goal — Clear Writing 最终 Web 收尾最小验收 v0.1

日期：2026-10-19  
任务：`clear-writing--final-web-closure-minimal-gate`  
仓库：`YuukiAS/AI_Skills_Collection`  
分支：`reviewed/clear-writing--scientific-explanation-readability-repair`

## 目标

在不修改 production candidate、不重跑旧 W2、不扩充人工测试数量的前提下，
用严格冻结的 4 个真实 ChatGPT Web 回答完成最终用户侧验收。

冻结 production candidate：

`fd7a1578a5042a46a55c5b638f6d550655b1096b`

真实 PRIVATE plugin：

- `writing-style / Clear Writing`
- `plugin_id=plugins_6ad4fc9abae08191a9ecd81879b2c919`
- `current_release_id=pluginrel_6ad4fc9c33888191b33350e50ac92b5d`
- 显示版本：`0.4.0`

## 已有证据

本 Goal 不重复要求用户人工重做已经通过的：

- KR-WEB-01..09；
- 四组 should-not-change；
- focused/full tests；
- required CI；
- source/generated parity；
- independent PROCESS + PRODUCT / ARTIFACT review；
- PRIVATE plugin source/release parity。

## 最终 Web Gate

唯一人工 Web Gate 是：

`docs/operations/prompts/CLEAR_WRITING_FINAL_WEB_CLOSURE_TEST_PROTOCOL_V0_1_2026-10-19.md`

严格 4 个回答：

1. 显式 `@Clear Writing` 普通技术状态解释；
2. Project Turn 1：新的 `scientific-rewrite` source-faithful 科研技术重写；
3. Project Turn 2：pure exact JSON；
4. Project Turn 3：新的复杂科研普通解释 + exact 后恢复。

不得增加第五个回答。

## Claim boundary

如果 4 个回答全部 PASS，只能声称：

- 显式真实 Clear Writing 入口工作正常；
- 薄 Project policy + 已安装 Clear Writing 下连续用户行为达到预期；
- exact-only 输出不受污染；
- 至少一个兄弟写作任务族在真实 Web normal entry 下行为正确；
- 当前复杂科研解释关键修复在真实 Web 得到直接观察。

不得声称：

- `PLUGIN_LOADED_EVERY_TURN=PASS`；
- 每轮后台必然加载 Clear Writing；
- 已证明插件相对于相同 Project setting 的独立因果增量。

## W2

历史：

`W2=INCONCLUSIVE`

保留为诊断证据，不重跑、不改判、不构造 control arm、不做盲评。

它不再是当前收窄 release claim 的 release blocker。

## 收尾条件

如果且仅如果 4 个回答全部按冻结协议 PASS：

`READY_FOR_RELEASE_CLOSURE=YES`

此后只允许进入 release closure：

- repository/plugin version；
- README；
- changelog；
- release branch；
- source/generated/release identity；
- final CI；
- actual released plugin identity/parity。

除非 4 个真实回答暴露此前合同未覆盖的新产品失败，否则不得新增 Web release Gate。

## 本轮边界

当前只冻结方案和执行合同：

- 不执行 4 个回答；
- 不改 production candidate；
- 不改真实 Project setting；
- 不改真实 PRIVATE plugin；
- 不启动 Codex；
- 不做 version/release；
- 不做 PIE/Mica/Research Authoring/Presentations。
