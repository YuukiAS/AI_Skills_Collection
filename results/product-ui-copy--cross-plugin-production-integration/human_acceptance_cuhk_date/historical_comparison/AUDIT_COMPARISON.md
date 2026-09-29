# CUHK Date Historical Audit Comparison

本文件是在第一阶段 live-site blind review 已冻结并提交之后生成的。旧审计只作为历史回归/校准证据；本文件没有回头修改 `live_site/LIVE_SITE_COPY_REVIEW.md`、截图、插件 replay 输出或 `CURRENT.json`。

## 输入与边界

- 冻结第一阶段：`../live_site/LIVE_SITE_COPY_REVIEW.md`、`../live_site/PHASE_1_FREEZE.md`、`../live_site/LIVE_SITE_PAGE_SUMMARY.json`。
- 历史审计：`docs/design/product-ui-copy/evidence/CUHK_DATE_PRODUCT_COPY_NATURALNESS_AUDIT_2026-09-26.md`。
- 结构化表格：`AUDIT_COMPARISON_TABLE.csv`。
- 对照口径：先看当前公开抓取是否仍可比较，再看第一阶段盲测是否自己发现同一产品问题族。旧 grade 不是 gold label。

## 1. 当前网站与旧 150 条对齐

- 旧审计总数：150 条，A 53、B 72、C 15、D 10。
- 当前仍存在：118 条，其中 109 条为精确字符串，9 条为旧表合并行在当前页面拆分显示但内容仍在。
- 已消失/已改变/本次未见：5 条，主要是旧 header/nav label、切换按钮或页面小标签表达变化。
- 当前不可比较：27 条，均来自 Register/Login 或 Register/Login 共用说明；本轮请求的 `/register` 与 `/login` 在两种语言下均为 404。

| Grade | 当前仍存在 | 已改变/未见 | Register/Login 不可比较 |
|---|---:|---:|---:|
| A | 30 | 5 | 18 |
| B | 65 | 0 | 7 |
| C | 13 | 0 | 2 |
| D | 10 | 0 | 0 |

**当前抓取中未在旧 150 表逐条列出的可见文本样本**（这表示“旧表未列为独立行”，不等同于一定是上线后新增）：
- `zh-Hans_privacy`：隐私、资料查阅、更正和删除请联系隐私与资料查阅负责人：support@cuhkdate.com。
- `zh-Hans_support`：Meet at CU / 中意 是独立学生项目，并非香港中文大学官方服务。这页说明目前可以怎样处理账户、匹配、隐私和安全问题。
- `zh-Hans_support`：资料查阅、更正、删除和正式隐私请求由隐私与资料查阅负责人通过同一邮箱处理。
- `zh-Hans_support`：此邮箱由获授权的项目负责人和支持人员处理；请不要在电邮中提交紧急求助、密码、完整身份证明文件或不必要的敏感资料。
- `zh-Hans_support`：在“隐私与安全”页，你可以检查个人资料、问卷、照片、联系方式，以及屏蔽、举报和删除账户状态。
- `zh-Hans_support`：如遇到不尊重、骚扰、冒充、疑似滥用或安全风险，可以在目前介绍相关页面屏蔽或提交举报。
- `zh-Hans_support`：删除账户与资料问题
- `zh-Hans_support`：你可以在设置页发起删除账户。删除会移除或解除使用账户、个人资料、问卷、报名和联系方式；少量最小化记录可能为安全、举报或审计需要保留。
- `zh-Hans_support`：Meet at CU 不是即时危机处理服务，也不能替代本地紧急服务、可信任人士或校方支持渠道。
- `zh-Hans_support`：如有人身安全、跟踪、勒索、自伤或即时危险，请立即联系本地紧急服务或可即时介入的人。
- `zh-Hans_terms`：Meet at CU 使用条款
- `zh-Hans_terms`：账户、个人资料与内容责任

## 2. 第一阶段盲测对仍存在条目的表现

- A 类仍存在 30 条：30/30 正确 KEEP；未发现把本来好的常规导航、品牌、CTA、基础隐私事实乱改的情况。
- B/C 类仍存在 78 条：64 条被第一阶段以逐条或页面级方式识别为自然度、内容架构、地区语感、内部词或重复结构问题；14 条属于旧审计 B 级细节但未单独列出。
- D 类仍存在 10 条：10/10 被升级到 PRODUCT SEMANTICS 或 LEGAL/TRUST/SAFETY，而不是润色。
- 明显误改：0 条。
- 明显 material 漏诊：0 条。需要人工看的分歧主要是 14 条 B 级语气/导航/小标题细节，而不是安全或法律边界。

### B/C 未单独点名但值得人工看的细节

- #13 Home / zh-Hans / Eyebrow：怎样开始
- #16 Home / zh-Hans / Step heading：验证并填写
- #22 Home / zh-Hans / Step heading：双方各自同意
- #24 Home / zh-Hans / Eyebrow：清楚的边界
- #25 Home / zh-Hans / Section heading：你的资料，不会变成公开名单
- #35 Home / zh-Hans / CTA heading：想先把流程看清楚？
- #36 Home / zh-Hans / CTA body：了解资料会如何使用、匹配轮次如何参加，以及双方同意的完整流程。
- #37 Home / zh-Hans / CTA：查看如何运作
- #38 How it works / zh-Hans / Page title：如何运作
- #82 Support / zh-Hans / Intro：这页说明目前可以怎样处理账户、匹配、隐私和安全问题。
- #86 Support / zh-Hans / Section heading：登录后的支持路径
- #87 Support / zh-Hans / Section body：如果匹配或联系方式不符合预期，先检查是否已完成个人资料、问卷、主动报名和可用联系方式。
- #113 Common header / zh-Hant-HK / Nav link：如何運作
- #127 Home / zh-Hant-HK / Section heading：你的資料，不會變成公開名單

## 3. Most Important 20 Lines 复核

旧审计 20 条重点中，第一阶段盲测清楚发现 18 条，部分覆盖但需要产品语气判断 1 条，因当前 Register/Login 公开路由 404 不可比较 1 条。

| # | 旧审计重点原文 | 盲测是否发现 | 对照判断 |
|---:|---|---|---|
| 1 | 这是一个私密、低频的交友流程。你先完成资料；固定轮次开放后，再自行决定是否参加。 | CLEARLY_FOUND | How it works 开场被第一阶段识别为产品自我定义和“你先/先后流程”模型感。 |
| 2 | 這是一個私密、低頻的交友流程。你先完成資料；固定輪次開放後，再自行決定是否參加。 | CLEARLY_FOUND | 繁中同类问题被单独记录，未当作简繁转换。 |
| 3 | 先把自己说清楚；轮次开放后，再由你决定是否参加。 | CLEARLY_FOUND | “把自己说清楚”被明确标为不适合学生产品。 |
| 4 | 先把自己說清楚；輪次開放後，再由你決定是否參加。 | CLEARLY_FOUND | 繁中“把自己說清楚”同样被识别。 |
| 5 | 不是刷资料，而是在合适的时候认真认识一个人 | CLEARLY_FOUND | 首页标语被作为内容架构问题，建议删除/合并而非再润色。 |
| 6 | 不是刷資料，是在合適的時候認真認識一個人 | CLEARLY_FOUND | 繁中标语同样被识别为品牌宣言味。 |
| 7 | 只开放注册 / 先把资料准备好 | CLEARLY_FOUND | 注册状态与 CTA 被识别为重复状态提示，并叠加当前 /register 404 产品一致性问题。 |
| 8 | 只開放註冊 / 先把資料準備好 | CLEARLY_FOUND | 繁中状态同样被识别。 |
| 9 | 你的资料，不会变成公开名单 | PARTIAL_TASTE_REVIEW | 隐私/trust 方向被覆盖，但这一句本身未作为独立微文案重点；适合用户按品牌语气决定。 |
| 10 | Meet at CU / 中意 把選擇權留給你，也把不必要的曝光降到最低。 | CLEARLY_FOUND | “把选择权/選擇權留给你”被放在 trust 文案边界中处理，未升级成更强隐私承诺。 |
| 11 | 验证学生使用范围 | CLEARLY_FOUND | “验证学生使用范围”被识别为内部合规词。 |
| 12 | 系统只在有合适人选时介绍一位；没有合适介绍也是正常结果，不代表你被拒绝。 | CLEARLY_FOUND | “正常结果/不代表你被拒绝”被识别为过度安抚和系统判定感。 |
| 13 | 第一批真实用户前的资料边界 | CLEARLY_FOUND | 公开隐私页 pre-user 阶段眉题被升级为信任问题。 |
| 14 | 第一批真實用戶前的使用邊界 | CLEARLY_FOUND | 公开条款页 pre-user 阶段眉题被升级为信任问题。 |
| 15 | 这页用普通语言说明目前产品实际收集和使用什么资料；它不是法律意见，也不代表外部法律审批已完成。 | CLEARLY_FOUND | 法律审批未完成被升级，不被润色。 |
| 16 | 正式法律审批仍需项目负责人和外部法律顾问确认。 | CLEARLY_FOUND | 正式法律审批未确认被升级为法律/信任问题。 |
| 17 | 系统按已冻结的产品合同进行周期式匹配；它不会为了填满名额而重用已发布匹配或降低质量边界。 | CLEARLY_FOUND | 产品合同/质量边界被升级为产品语义。 |
| 18 | 系統按已凍結的產品合同進行週期式配對；它不會為了填滿名額而重用已發布配對或降低品質邊界。 | CLEARLY_FOUND | 繁中产品合同/品质边界同样被升级。 |
| 19 | 如你无法登录、需要隐私或删除支持，或需要回报无法在产品内处理的安全问题，可以电邮 support@cuhkdate.com。 | CLEARLY_FOUND | Support 的“隐私或删除支持/电邮”被识别为不自然。 |
| 20 | 用途包括建立和保护账户、维持早期 CUHK 学生使用范围、提供匹配/安全/支持功能、处理资料查阅、更正和删除要求。处理者类别包括 Supabase、Cloudflare、Resend 及必要的授权支持人员。 | NOT_COMPARABLE_ROUTE_404 | 当前 Register 路由 404；第一阶段正确记录入口不可比较，没有用旧审计回填。 |

## 4. 分页面总结

### Home

- zh-Hans：KEEP_OK 8，ISSUE_DETECTED_OR_PAGE_LEVEL_COVERED 15，ESCALATION_OK 0，MINOR_NOT_SEPARATELY_CALLED_OUT 8，NO_LONGER_VISIBLE_OR_CHANGED 0。
- zh-Hant-HK：KEEP_OK 2，ISSUE_DETECTED_OR_PAGE_LEVEL_COVERED 12，ESCALATION_OK 0，MINOR_NOT_SEPARATELY_CALLED_OUT 1，NO_LONGER_VISIBLE_OR_CHANGED 0。
  - 判断：盲测自己发现状态 badge、heading、body 与 CTA 周边重复，且把普通状态 slogan 化；没有逐句美化为更多标语。

### How

- zh-Hans：KEEP_OK 5，ISSUE_DETECTED_OR_PAGE_LEVEL_COVERED 12，ESCALATION_OK 0，MINOR_NOT_SEPARATELY_CALLED_OUT 1，NO_LONGER_VISIBLE_OR_CHANGED 1。
- zh-Hant-HK：KEEP_OK 0，ISSUE_DETECTED_OR_PAGE_LEVEL_COVERED 6，ESCALATION_OK 0，MINOR_NOT_SEPARATELY_CALLED_OUT 0，NO_LONGER_VISIBLE_OR_CHANGED 0。
  - 判断：盲测自己发现“使用范围”“轮次/自主报名”“最多收到一位介绍”“正常结果”等内部或模型式表达。

### Privacy

- zh-Hans：KEEP_OK 6，ISSUE_DETECTED_OR_PAGE_LEVEL_COVERED 8，ESCALATION_OK 2，MINOR_NOT_SEPARATELY_CALLED_OUT 0，NO_LONGER_VISIBLE_OR_CHANGED 0。
- zh-Hant-HK：KEEP_OK 0，ISSUE_DETECTED_OR_PAGE_LEVEL_COVERED 2，ESCALATION_OK 2，MINOR_NOT_SEPARATELY_CALLED_OUT 0，NO_LONGER_VISIBLE_OR_CHANGED 0。
  - 判断：盲测自己把“第一批真实用户前”“法律审批未完成”“资格边界/敏感边界/匹配输入”等归到信任、法律或内部词问题。

### Terms

- zh-Hans：KEEP_OK 1，ISSUE_DETECTED_OR_PAGE_LEVEL_COVERED 3，ESCALATION_OK 3，MINOR_NOT_SEPARATELY_CALLED_OUT 0，NO_LONGER_VISIBLE_OR_CHANGED 0。
- zh-Hant-HK：KEEP_OK 0，ISSUE_DETECTED_OR_PAGE_LEVEL_COVERED 0，ESCALATION_OK 3，MINOR_NOT_SEPARATELY_CALLED_OUT 0，NO_LONGER_VISIBLE_OR_CHANGED 0。
  - 判断：盲测自己把“产品合同/质量边界”和法律审批状态升级，且保留安全/危机服务边界。

### Support

- zh-Hans：KEEP_OK 3，ISSUE_DETECTED_OR_PAGE_LEVEL_COVERED 3，ESCALATION_OK 0，MINOR_NOT_SEPARATELY_CALLED_OUT 3，NO_LONGER_VISIBLE_OR_CHANGED 0。
- zh-Hant-HK：KEEP_OK 0，ISSUE_DETECTED_OR_PAGE_LEVEL_COVERED 2，ESCALATION_OK 0，MINOR_NOT_SEPARATELY_CALLED_OUT 0，NO_LONGER_VISIBLE_OR_CHANGED 0。
  - 判断：盲测自己识别简体“电邮/回报/需要隐私或删除支持”和繁中“刪除支援/公開支援”的自然度边界，同时没有编造登录后入口。

## 5. 特别检查

- slogan 化普通状态：发现。Home 的“首批同学加入中 / 只开放注册 / 先把资料准备好”被合并处理。
- badge/heading/body 重复：发现。第一阶段建议把当前可做什么集中到一处，不逐句润色。
- “你先/由你/只有…才…”重复结构：发现。How 与 Home 的流程句被归为模型式、过度完整表达。
- 内部产品词：发现。“轮次、使用范围、资格边界、产品合同、质量边界/品质边界”均被识别。
- 法律/隐私内部状态暴露：发现。“第一批真实用户前”“外部法律审批未完成”被升级。
- 简繁机械转换：未发现候选机械处理。盲测保留 Hong Kong 用词，同时指出 zh-Hans 的“电邮、回报、支持路径”不自然。

## 6. 最值得用户人工看的分歧

1. 首页是否要保留“私密、低频”“不是刷资料”这一类品牌感，还是改成更安静的状态/流程说明。
2. “你的资料，不会变成公开名单”这类信任文案是否符合产品语气；候选没有把它当成硬失败。
3. Register/Login 当前公开 404 与页面 CTA 的矛盾应由产品方确认；旧注册文案不能替代当前入口验收。
4. Privacy / Terms 是否应该公开呈现法律审批未完成。候选正确升级，但最终公开策略不是文案工具能决定。
5. zh-Hans 是否接受“资料/电邮/回报/支持路径”这类偏港式或翻译式表达，还是要独立重写。

## 7. 结论

第二阶段没有发现明显 candidate failure。候选在第一阶段没有见过旧审计时，已经自己发现主要历史问题族：什么时候 KEEP，什么时候改自然度，什么时候删/合并页面结构，什么时候升级产品、法律、隐私和信任边界。剩余差异主要是 B 级产品语气和用户偏好，不是插件职责划分失败。
