# H4 留出批次答复

按冻结顺序处理全部 8 个场景。已有清楚文案保持不变；产品与隐私事实未定的场景先交回负责人确认。以下判定只覆盖文本与路由，不包含真实界面渲染验收。

候选提交：`a06ff050bc82bb22358dfcb3e4faa885fddd285b`（批次绑定）。

## H3-01

- route: `product-ui-copy`
- outcome_class: `KEEP`
- decision: KEEP；状态和关闭动作已清楚，不作修改。

最终文案：

- 状态：邮箱地址已更新。
- 按钮：完成

## H3-02

- route: `product-ui-copy`
- outcome_class: `LOCALE/REGISTER`
- decision: 按香港界面用语调整，保留验证完成、资料已存入账户和继续引导三项含义。

最终文案（zh-Hant-HK）：

- 标题：身份驗證完成
- 正文：你的個人資料已儲存至帳戶。
- 按钮：繼續

## H3-03

- route: `frontend-content-architecture`
- outcome_class: `CONTENT ARCHITECTURE`
- decision: 五处文字重复传达状态和管理入口，先由 Frontend 合并内容。

内容架构建议：保留标题“自动备份已开启”和按钮“管理自动备份”；移除重复徽标、正文及辅助说明。两项核心信息都保留，无需分别润色五处文字。由 Frontend 确认实际页面层级和阅读节奏后，再交 Product UI Copy 定稿。

## H3-04

- route: `product-domain-authority`
- outcome_class: `PRODUCT SEMANTICS`
- decision: 暂不提供最终弹窗文案；由产品负责人先确定操作后果。

唯一已知后果是立即移除当前工作区入口，不能据此断言底层文件被删除。现有“无法恢复”“所有文件都会永久删除”和按钮“永久删除”均缺少依据，不可作为已确认文案使用。产品负责人需确认文件是否保留、是否存在恢复窗口及其时长、管理员能否恢复，再冻结标题、说明和操作按钮的含义。

## H3-05

- route: `legal-trust-product-authority`
- outcome_class: `LEGAL/TRUST/SAFETY`
- decision: 暂不定稿同意说明或按钮；交产品、隐私及法务负责人确认。

已知仅为开启后使用某些使用记录调整推荐。“只会安全使用”和“不会造成任何隐私风险”的承诺没有依据，不能保留或换种说法继续使用。需先明确使用记录的范围、保存期限、是否上传服务器、删除或撤回后的数据处理，以及可支持的隐私风险说明。确认同意范围后，再用香港界面用语撰写披露与操作文案；当前“同意並開啟”不视为已批准。

## H3-06

- route: `product-ui-copy`
- outcome_class: `WORDING/NATURALNESS`
- decision: 用上传结果、具体限制和可执行下一步替换后台报错。

最终文案：

- 标题：上传失败
- 正文：当前文件为 14 MB，超过 10 MB 上限。请选择不超过 10 MB 的文件重新上传。
- 按钮：更换文件

## H3-07

- route: `product-ui-copy`
- outcome_class: `WORDING/NATURALNESS`
- decision: 将整页作为一组文案处理，保留现有位置；标题说明产品，正文依次说明优先级、关注重点和团队协作，按钮保持直接。

最终文案：

- hero：团队协作工作台
- block_1：看清工作优先级。
- block_2：把注意力放在当前重要的工作上。
- block_3：与团队一起推进工作。
- primary_action：开始使用

不增加功能或效果承诺。以上完成语言节奏调整；实际页面的密度、相邻文字关系及最终渲染节奏仍由 Frontend 验证。

## H3-08

- route: `non-frontend-runtime-owner`
- outcome_class: `NO_FRONTEND_OR_PRODUCT_UI_COPY`
- decision: 交后台/runtime 负责人处理，不激活 Frontend Design 或 Product UI Copy。

将每 30 秒轮询改为事件触发，同时保留失败重试和现有日志字段，属于后台机制修改。UI 和用户可见文案保持不变；本次仅确认路由，不修改实现。
