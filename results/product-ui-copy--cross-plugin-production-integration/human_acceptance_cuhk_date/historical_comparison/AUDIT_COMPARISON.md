# CUHK Date Historical Audit Comparison

This comparison was performed only after Phase 1 live-site capture and candidate
replay had been frozen in commit `42f92f59`. The 2026-09-26 historical audit is
used here as calibration evidence, not as candidate-generation input.

## Inputs

- Frozen Phase 1 live-site review:
  `../live_site/LIVE_SITE_COPY_REVIEW.md`
- Frozen Phase 1 capture summary:
  `../live_site/LIVE_SITE_PAGE_SUMMARY.json`
- Historical audit:
  `docs/design/product-ui-copy/evidence/CUHK_DATE_PRODUCT_COPY_NATURALNESS_AUDIT_2026-09-26.md`
- Machine-readable comparison table:
  `AUDIT_COMPARISON_TABLE.csv`

## High-Level Comparison

The historical audit contains 150 extracted lines:

- A: 53
- B: 72
- C: 15
- D: 10

Current public-site capture status:

- 113 historical strings are still exactly visible in the current public capture.
- 13 historical strings changed or were not visible in the current public capture.
- 24 historical strings came from Register/Login surfaces that are now not
  publicly comparable through the requested `/register` and `/login` routes
  because those routes returned 404 in both locales.

Phase 1 was not expected to reproduce the old 150-line grading table. It was a
page-level first pass. The useful question is whether it independently found
the same kinds of problems without seeing the historical answers.

## What The Candidate Found Without The Old Audit

The blind first pass independently found the largest historical problem
families:

- Home status and action copy are too repetitive and slogan-like.
- "先把自己说清楚 / 先把自己說清楚" is not a good student-facing line.
- "自主参加轮次 / 自主參加輪次" and "最多收到一位介绍 / 最多收到一位介紹" need user-facing wording.
- Legal and privacy pages expose internal stage labels such as "第一批真实用户前 / 第一批真實用戶前".
- "外部法律审批未完成" and equivalent public-facing legal status language should be escalated, not polished.
- "产品合同 / 產品合同" and "质量边界 / 品質邊界" are internal product or engineering language.
- Support text such as "需要隐私或删除支持 / 需要私隱或刪除支援" is unnatural.
- zh-Hans and zh-Hant-HK need separate judgment rather than mechanical conversion.

It also found a current-site issue that the historical audit cannot answer by
itself: the public Register/Login routes requested for this acceptance pass are
404, while the current page still presents account-creation CTA copy. That is a
product/site consistency issue, not a microcopy polishing issue.

## Historical 20-Line Calibration

| Historical item | Current status | Blind first-pass result |
|---|---|---|
| "这是一个私密、低频的交友流程..." / "這是一個私密、低頻的交友流程..." | Still present in How it works | Detected as product-self-definition and over-complete process copy; first pass recommends action-first page framing. |
| "先把自己说清楚..." / "先把自己說清楚..." | Still present | Detected; first pass proposes "先填写个人资料 / 先填寫個人資料" style meaning and flags the original as uncomfortable. |
| "不是刷资料..." / "不是刷資料..." | Still present | Detected as slogan-like content architecture; first pass recommends deleting rather than rewriting into another slogan. |
| "只开放注册 / 先把资料准备好" and zh-Hant-HK equivalent | Still present | Detected as status duplication near the CTA; first pass recommends consolidating the state and action message. |
| "你的资料，不会变成公开名单" | Still present | Partly covered under privacy/trust positioning, but not called out as a named microcopy item. This is a residual B-level nuance for user taste review, not an obvious candidate failure. |
| "把选择权留给你 / 把選擇權留給你" | Still present | Detected as trust wording that should not be strengthened into stronger privacy claims. First pass focuses on protected meaning rather than stylistic grade. |
| "验证学生使用范围 / 驗證學生使用範圍" | Still present | Detected; first pass proposes describing email verification and student/age declaration without implying official identity certification. |
| "没有合适介绍也是正常结果..." | Still present | Detected as a "normal result" pattern and handled in wording examples for the introduction/flow copy. |
| "第一批真实用户前..." / "第一批真實用戶前..." | Still present | Detected and screenshot-confirmed as visible internal stage copy; first pass recommends removing the public eyebrow and escalating legal/status framing. |
| "法律审批未完成" / "法律審批未完成" | Still present | Detected as legal/trust escalation; first pass refuses to hide or rewrite it as if approval exists. |
| "系统按已冻结的产品合同..." / "系統按已凍結的產品合同..." | Still present | Detected as product semantics/internal engineering language; first pass sends it back for product owner definition instead of inventing user copy. |
| Support email line with "隐私或删除支持 / 私隱或刪除支援" | Still present | Detected; first pass provides safer natural wording for the support channel while preserving scope and email address. |
| Dense registration privacy notice | Current requested `/register` route is 404 | Not comparable through this public-entry capture. First pass correctly escalates the route contradiction instead of grading unavailable copy. |

## A/B/C/D Behavior

For historical A lines, the first pass mostly behaved conservatively. It did
not try to rewrite routine navigation, brand, footer, basic CTA, photo optional
disclosure, or "联系方式只在双方同意后显示" style facts. This matches the expected
KEEP behavior.

For B/C lines, the first pass did not enumerate every old B/C item, but it did
find the main recurring families: over-complete explanatory copy, internal
state nouns, slogan-like status, "normal result" phrasing, and awkward support
wording. The missing B-level items are mostly small taste calls that should
remain open for user judgment rather than be counted as a hard failure.

For D lines, the first pass found the most important public-trust failures:
internal pre-user labels, unfinished legal-review language, and internal
product-contract language. It correctly escalated these instead of smoothing
them into polished but unsupported claims.

## Locale Judgment

The candidate did not treat zh-Hans and zh-Hant-HK as simple script variants.
It preserved Hong Kong natural choices such as "私隱", "電郵", "支援", "封鎖",
"舉報", and "上載", while separately flagging terms that are unnatural in both
locales, such as "使用范围 / 使用範圍", "产品合同 / 產品合同", and "质量边界 /
品質邊界".

For zh-Hans, the first pass noticed that "电邮 / 回报 / 支持路径" do not match
normal simplified Chinese product register as well as the Hong Kong equivalents
match zh-Hant-HK.

## Apparent Misses Or Limits

- The blind first pass did not create a full 150-line grade table. This was
  intentional: the task asked for page-level judgment, not isolated sentence
  grading.
- Some B-level historical nuances, especially "你的资料，不会变成公开名单" and
  smaller navigation phrasing such as "如何运作", were not highlighted as
  standalone top issues. They remain useful for user taste review but do not
  show an obvious routing or safety failure.
- Register/Login historical copy cannot be compared through the current public
  `/register` and `/login` routes because those routes returned 404 during this
  acceptance capture.
- The candidate replay child was text/DOM driven. Screenshot-level rendered
  acceptance was added in the frozen Phase 1 evidence by the current Codex run,
  not by changing the candidate output.

## Conclusion

No obvious candidate failure was found in the historical comparison. The first
pass independently found the main mature-product issues: when to keep clear
copy, when to rewrite wording, when to delete or merge page copy, and when to
escalate privacy/legal/product facts instead of inventing smoother text.

The remaining open questions are human product-taste decisions: how much brand
slogan the homepage should keep, whether "私密、低频" is the right positioning
tone, and how much legal/collection detail belongs on public pages versus a
separate policy surface.
