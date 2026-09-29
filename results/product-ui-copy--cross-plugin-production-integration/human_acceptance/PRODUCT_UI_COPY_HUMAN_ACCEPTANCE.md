---
title: "Product UI Copy 最终验收"
subtitle: "Frontend Design + Clear Writing 的产品界面文案协作"
date: "2026-09-29"
---

# 1. 现在实际怎么工作

这套能力做的不是“把界面文字润色得更像人”，而是把产品界面里 **该不该说、说什么、谁来负责、最后在页面上是否成立** 分开处理。

\vspace{0.6em}

\begin{center}
\Large
用户界面任务\\[0.4em]
$\downarrow$\\[0.4em]
Frontend Design 判断内容架构\\[0.4em]
$\downarrow$\\[0.4em]
Product UI Copy 写自然文案\\[0.4em]
$\downarrow$\\[0.4em]
Frontend Design 做最终页面验收
\end{center}

\vspace{0.8em}

Frontend Design 先判断这段文字是不是应该出现在这个位置：它是状态、说明、按钮、错误、隐私披露，还是重复信息。如果页面结构本身有问题，先调整内容架构，不急着逐句润色。

Clear Writing 里的 Product UI Copy 只处理已经冻住的产品含义：让短文案自然、符合语言地区习惯，同时保护删除、隐私、同意、价格、安全、恢复能力这些真实后果。

最后回到 Frontend Design，看真实页面里的层级、换行、按钮关系和披露位置是否可读。换句话说：不是“写一句漂亮话”，而是让界面能正常告诉用户下一步会发生什么。

\newpage

# 2. 这次到底新增了什么

这次新增的是一个中央插件之间的协作流程，而不是给某个项目硬写一批固定文案。

**Frontend Design 0.4**

- 新增产品界面内容架构判断：先看页面角色、重复信息、用户后果和相邻文案。
- 能识别 web、browser extension、desktop/WebView、mobile/Compose 等用户界面任务。
- 仍然保留原有 Frontend coordinator-first 架构；不接管项目自己的平台实现。

**Clear Writing 0.4**

- 新增 `product-ui-copy` 能力，专门处理产品界面微文案。
- `zh-Hans` 与 `zh-Hant-HK` 分开实现，不把香港繁体当成机械转换。
- 删除、隐私、同意、价格、安全、恢复能力等事实不清楚时，不硬写最终文案。

**新的 product-ui-copy Skill**

- 支持 KEEP、自然度改写、语言地区适配、产品语义升级、法律/隐私升级。
- 与 `writing-fidelity` 配合，保护产品状态和用户后果。

**旧能力保持不变**

- `chinese-prose` 仍然主要负责报告、README、技术文档和普通中文表达，不变成万能 UI 文案工具。
- backend/runtime/data-only 任务不会因为出现“刷新”“日志”“重试”就误触发 Frontend。
- 其他中央插件不升版本，成熟度不提升。

\newpage

# 3. 真实例子：KEEP、香港繁体、普通自然度

这些例子来自已经通过的代表性批次。这里直接展示输入、处理结果和为什么这样处理。

## KEEP：清楚的完成态不硬改

**原文**

- 状态：邮箱地址已更新。
- 按钮：完成

**处理结果**

- 状态：邮箱地址已更新。
- 按钮：完成

**为什么**

这是一处简单完成态，文字已经清楚。按钮只关闭确认状态，不触发额外操作。系统没有为了显示“做了优化”而加上同步、安全、通知之类不存在的承诺。

## zh-Hant-HK：不是简繁替换

**原文**

- 標題：驗證完成
- 正文：你的個人資料已經保存到帳號中。你可以繼續下一步。
- 按鈕：繼續下一步

**处理结果**

- 標題：身份驗證完成
- 正文：你的個人資料已儲存至帳戶。
- 按鈕：繼續

**为什么**

保留了 3 个产品事实：身份验证已完成、资料已保存到该账户、下一步是继续 onboarding。改动集中在香港产品界面的自然表达，例如“儲存至帳戶”和更短的“繼續”。

## 普通 wording：把后台错误改成用户能处理的问题

**原文**

- 标题：Upload rejected
- 正文：payload exceeds configured max_size=10485760; request aborted
- 按钮：Retry

**处理结果**

- 标题：上传失败
- 正文：当前文件为 14 MB，超过 10 MB 上限。请选择不超过 10 MB 的文件重新上传。
- 按钮：更换文件

**为什么**

用户需要知道发生了什么、限制是多少、下一步能做什么。这里保留了 14 MB、10 MB 和换文件重试这几个事实，同时去掉实现参数和后台报错口吻。

\newpage

# 4. 真实例子：内容架构与产品语义

## CONTENT ARCHITECTURE：不是每一句都润色

**原文**

- 徽标：自动备份已开启
- 标题：自动备份已开启
- 正文：当前已开启自动备份。系统会按照已开启的自动备份设置进行备份。
- 主按钮：管理已开启的自动备份
- 辅助说明：你可以在这里管理当前已经开启的自动备份。

**处理结果**

保留标题“自动备份已开启”和按钮“管理自动备份”；移除重复徽标、重复正文和重复辅助说明。两项核心信息都保留：当前是开启状态，用户可以进入管理。

**为什么**

这里的问题不在某一句中文生硬，而在整页反复说同一件事。如果逐句润色，页面会更“顺”，但仍然啰嗦。Frontend Design 先处理内容架构，再决定是否需要 Product UI Copy 定稿。

## PRODUCT SEMANTICS：事实没定，不写最终删除文案

**原文**

- 标题：删除工作区？
- 正文：删除后无法恢复，所有文件都会永久删除。
- 按钮：永久删除

**处理结果**

不提供最终弹窗文案，先交回产品负责人确认。当前唯一已知事实是：操作会立即移除当前工作区入口。还不能断言底层文件是否删除、是否存在恢复窗口、管理员是否能恢复。

**为什么**

“无法恢复”和“永久删除”不是语气问题，是产品后果。如果事实未定，写得再自然也会误导用户。这里正确动作是升级给产品 owner，而不是把风险包装成更委婉的文案。

\newpage

# 5. 真实例子：法律、隐私与信任边界

**场景**

浏览器扩展准备增加个性化推荐。当前只知道会分析使用记录来调整推荐，但还没有正式决定保存多久、是否上传服务器、之后能否删除。

**原文**

- 标题：開啟個人化推薦
- 正文：我們只會安全使用你的活動資料來改善推薦，不會造成任何私隱風險。
- 按钮：同意並開啟

**处理结果**

不定稿同意说明或按钮，先交给产品、隐私及法务负责人确认。已知事实只有“开启后会使用某些使用记录调整推荐”。保存期限、是否上传、删除或撤回后的处理方式、可承诺到什么程度的隐私风险，都需要先明确。

**为什么**

“不会造成任何私隐风险”没有依据，不能保留，也不能换一种更自然的说法继续使用。Product UI Copy 的职责不是替产品补政策，而是在政策和产品事实明确之后，把用户需要知道的后果说清楚。

**这类升级的价值**

它能阻止两种危险输出：一种是把未定政策说成已定事实；另一种是为了显得亲切，把用户真正需要判断的隐私和同意范围藏起来。

\newpage

# 6. 实际渲染结果：wide desktop

这张图检查桌面宽屏页面的整体节奏、层级、状态说明和主要按钮关系。它是最终版 `wide-desktop.png`。

\vspace{0.5em}

\begin{center}
\includegraphics[width=0.96\linewidth,height=0.78\textheight,keepaspectratio]{/home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration/results/product-ui-copy--cross-plugin-production-integration/human_acceptance/assets/wide-desktop.png}
\end{center}

\newpage

# 7. 实际渲染结果：narrow mobile

这张图检查 390px 窄屏页面的堆叠顺序、移动端删除确认和按钮关系。为保证文字可读，下面使用同一张最终版 `narrow-mobile.png` 按上、中、下三段带重叠展示。

\vspace{0.4em}

\begin{center}
\includegraphics[width=0.31\linewidth,trim=0 1120bp 0 0,clip]{/home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration/results/product-ui-copy--cross-plugin-production-integration/human_acceptance/assets/narrow-mobile.png}
\hfill
\includegraphics[width=0.31\linewidth,trim=0 560bp 0 560bp,clip]{/home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration/results/product-ui-copy--cross-plugin-production-integration/human_acceptance/assets/narrow-mobile.png}
\hfill
\includegraphics[width=0.31\linewidth,trim=0 0 0 1120bp,clip]{/home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration/results/product-ui-copy--cross-plugin-production-integration/human_acceptance/assets/narrow-mobile.png}
\end{center}

\newpage

# 8. 实际渲染结果：trust disclosure

这张图检查隐私/保留规则说明是否靠近主要操作，避免把用户需要判断的信任信息藏到页面角落。它是最终版 `trust-disclosure.png`。

\vspace{0.5em}

\begin{center}
\includegraphics[width=0.86\linewidth,height=0.78\textheight,keepaspectratio]{/home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration/results/product-ui-copy--cross-plugin-production-integration/human_acceptance/assets/trust-disclosure.png}
\end{center}

\newpage

# 9. 实际渲染结果：KEEP control

这张图检查已经清楚的文案是否保持不变，也检查中间宽度下的标题换行。下面先放完整最终版 `keep-control.png`，再放大底部 KEEP 区域，确认“置”没有孤立成行。

\vspace{0.4em}

\begin{center}
\includegraphics[width=0.62\linewidth,height=0.42\textheight,keepaspectratio]{/home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration/results/product-ui-copy--cross-plugin-production-integration/human_acceptance/assets/keep-control.png}

\vspace{0.5em}

\includegraphics[width=0.92\linewidth,trim=0 0 0 1400bp,clip]{/home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration/results/product-ui-copy--cross-plugin-production-integration/human_acceptance/assets/keep-control.png}
\end{center}

\newpage

# 10. 真实项目兼容结果

兼容检查的重点不是“这些项目已经接入”，而是中央插件遇到真实项目材料时，会不会把职责分错。

**Lucerna 会进入 Frontend Design**

Lucerna 的桌面紧凑面板、菜单栏/托盘入口、WidgetKit 快照和资源状态都是用户看得见的界面。Frontend Design 可以判断信息层级、状态说明和面板宽度风险；但它不能接管 Tauri、WidgetKit、网络检测或监控实现。比如 “Healthy” 不能在未确认检查范围时被写成全面业务健康。

**Mica 会进入 Frontend Design**

Mica 是浏览器扩展弹窗，包含 Active、Native virtualization、Degraded、Disabled、诊断、复制等用户可见状态和操作。Frontend Design 可以组织弹窗层级和动作反馈；但不能凭 host permissions 断言“不会上传聊天内容”，也不能替产品确认 Reset 的影响范围。

**SeminarArc Compose 会进入 Frontend Design**

Compose 页面包含列表筛选、现场采集、录音状态、删除确认、OCR 任务等界面。Frontend Design 可以协调页面结构和文案，但 Android、Compose、TalkBack、录音状态、任务状态变化仍由项目平台 owner 负责。

**SeminarArc Room / WorkManager 不会进入**

Room 迁移和 WorkManager 重试是数据与后台任务问题。如果 UI 明确不变，Frontend Design 和 Product UI Copy 都不激活。只有迁移实际改变了用户可见状态或动作后果，才重新进入界面评审。

\newpage

# 11. 这套能力不会做什么

**不会把 `chinese-prose` 变成万能 UI 文案工具。**  
长文中文润色仍然服务报告、README、技术文档和普通中文表达。产品界面微文案走独立的 Product UI Copy。

**不会乱改产品、隐私、删除、价格等事实。**  
如果产品后果未定，它会停止定稿并升级给产品、隐私、法务或领域负责人，而不是写一句听起来更顺的话。

**不会把 browser fixture 冒充 native runtime。**  
这次截图证明的是中央插件代表性浏览器渲染 fixture：层级、换行、按钮和披露位置可检查。它不证明 Lucerna 原生桌面、Mica 扩展运行时或 SeminarArc Compose 原生行为。

**不会声称 Lucerna / Mica / SeminarArc 已完成项目级硬绑定。**  
当前验证的是中央插件遇到真实项目材料时的路由和责任边界。项目级接入、原生运行、项目代码修改和后续适配不在这份验收产物里。

\vspace{0.8em}

\footnotesize
技术附录：当前生产候选为 `a06ff050bc82bb22358dfcb3e4faa885fddd285b`；独立 Reviewer 第二轮结论为 PASS；当前 reviewed branch 状态为 `AWAIT_HUMAN_DECISION`。这些信息只用于定位，不是用户验收的替代。

\newpage

# 12. 给用户的验收问题

请只按你看到的能力和边界判断，不需要接受候选之外的后续发布动作。

1. 这套职责划分是否符合预期？  
   Frontend 先判断内容架构，Clear Writing 再写自然文案，最后回到 Frontend 做页面验收。

2. 文案质量是否达到正常产品水平？  
   特别是 KEEP、香港繁体、上传错误和首页节奏这些场景。

3. KEEP / 产品语义升级 / 法律隐私升级是否符合预期？  
   已经清楚的文案不硬改；事实没定的删除、隐私和同意不硬写。

4. Frontend 与 Clear Writing 的协作是否自然？  
   是否看起来像一条产品工作流，而不是两个插件各自改一遍。

5. 是否可以进入 main integration / release？  
   如果可以，后续仍需要单独授权 main integration 和 release 动作。
