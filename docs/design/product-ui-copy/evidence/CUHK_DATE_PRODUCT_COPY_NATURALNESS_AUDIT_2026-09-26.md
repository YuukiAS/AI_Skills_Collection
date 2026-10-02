# Meet at CU / 中意 Product Copy Naturalness Audit

Evidence: current anonymous production rendered UI from `https://cuhkdate.com`, captured through the in-app browser accessibility tree. No login, no account creation, no form submission, no staging, no source/repo/internal docs, no DevTools/Network/Console. Repeated duplicated headings from the accessibility tree are deduped when they appear to be the same visible heading repeated by layout/semantics. Common header/footer items are recorded once per locale.

## Full Extraction Table

| # | PAGE | LOCALE | UI_ROLE | EXACT_COPY | GRADE | WHY | REWRITE_NEEDED |
|---:|---|---|---|---|---|---|---|
| 1 | Common header | zh-Hans | Brand link | Meet at CU 中意 | A | 品牌名直接、自然。 | NO |
| 2 | Common header | zh-Hans | Nav group label | 公开页面 | A | 功能性标签，虽略后台感但不别扭。 | NO |
| 3 | Common header | zh-Hans | Nav link | 如何运作 | B | 能懂，但简中产品更常写“使用流程”“怎么玩/怎么开始”；“运作”略翻译腔。 | YES |
| 4 | Common header | zh-Hans | Locale switch | 切换至繁体 | A | 明确自然。 | NO |
| 5 | Common header | zh-Hans | CTA | 创建账户 | A | 标准产品用语。 | NO |
| 6 | Common footer | zh-Hans | Footer links | 隐私 / 条款 / 支持 | A | 简洁自然。 | NO |
| 7 | Home | zh-Hans | Badge | 首批同学加入中 | B | 真实产品可用，但“加入中”带轻营销状态口号感。 | YES |
| 8 | Home | zh-Hans | Hero subtitle | 给 CUHK 在读学生的私密交友方式 | A | 定位清楚，句式自然。 | NO |
| 9 | Home | zh-Hans | Hero body | 不公开浏览同学资料，也不用不停滑动。现在可以创建账户并完成资料；未来每个固定轮次仍由你自行决定是否参加。 | B | 解释很完整，且“未来每个固定轮次仍由你自行决定”偏说明书/模型式补足。 | YES |
| 10 | Home | zh-Hans | Status label | 只开放注册 | B | 信息准确，但把普通状态压成 slogan，少了“目前”。 | YES |
| 11 | Home | zh-Hans | Status heading | 先把资料准备好 | B | 可读，但像把状态包装成品牌短句。 | YES |
| 12 | Home | zh-Hans | Status body | 目前不会自动加入任何匹配；第一轮开放后仍需由你主动报名。 | B | 清楚，但“由你主动报名”与分号结构略工整。 | YES |
| 13 | Home | zh-Hans | Eyebrow | 怎样开始 | B | 简中里“怎么开始”更口语；“怎样”略书面。 | YES |
| 14 | Home | zh-Hans | Section heading | 不是刷资料，而是在合适的时候认真认识一个人 | B | 文案漂亮，但“不是 X，而是 Y”是典型生成式对照句，像品牌宣言多于 UI 标题。 | YES |
| 15 | Home | zh-Hans | Section body | 先把自己说清楚；轮次开放后，再由你决定是否参加。 | C | “把自己说清楚”对用户偏生硬，有被要求自我交代的感觉。 | YES |
| 16 | Home | zh-Hans | Step heading | 验证并填写 | B | 能懂，但“填写”宾语省略得有点机械。 | YES |
| 17 | Home | zh-Hans | Step body | 用 CUHK @Link 邮箱创建账户，完成基本资料和问卷。 | A | 任务明确，真实产品会这样写。 | NO |
| 18 | Home | zh-Hans | Step heading | 自主参加轮次 | B | “轮次”偏产品内部词，搭配“自主参加”稍硬。 | YES |
| 19 | Home | zh-Hans | Step body | 固定轮次开放后，由你主动报名；完成资料不等于自动参加。 | B | 清楚，但“由你主动”“不等于”解释感较强。 | YES |
| 20 | Home | zh-Hans | Step heading | 每轮最多一位 | A | 短、清楚、像真实 UI。 | NO |
| 21 | Home | zh-Hans | Step body | 只在有合适人选时介绍一位；没有合适介绍也是正常结果。 | B | 信息好，但“正常结果”偏产品/实验语气。 | YES |
| 22 | Home | zh-Hans | Step heading | 双方各自同意 | B | 准确但略抽象，像原则而非用户任务。 | YES |
| 23 | Home | zh-Hans | Step body | 只有两个人都愿意认识，才会显示彼此主动提供的联系方式。 | B | “只有 X，才 Y”清楚但完整得偏模型式。 | YES |
| 24 | Home | zh-Hans | Eyebrow | 清楚的边界 | B | 抽象定位词，像内部原则标题。 | YES |
| 25 | Home | zh-Hans | Section heading | 你的资料，不会变成公开名单 | B | 安心感明确，但“你的”加逗号有轻英文 UX copy 映射感。 | YES |
| 26 | Home | zh-Hans | Section body | Meet at CU / 中意 把选择权留给你，也把不必要的曝光降到最低。 | B | “把 X 留给你”很工整、广告化，像生成式润色。 | YES |
| 27 | Home | zh-Hans | Trust bullet | 没有公开学生目录或滑动匹配 | A | 简洁说明差异点。 | NO |
| 28 | Home | zh-Hans | Trust bullet | 没有合适介绍是正常结果 | B | “正常结果”对用户有点冷，像系统结论。 | YES |
| 29 | Home | zh-Hans | Trust bullet | 照片选填，通过审核前不会向匹配对象展示 | A | 清楚、具体。 | NO |
| 30 | Home | zh-Hans | Trust bullet | 联系方式只在双方同意后显示 | A | 清楚自然。 | NO |
| 31 | Home | zh-Hans | Section heading | 为 CUHK 学生而设，但不是大学官方服务 | A | 必要边界表达自然。 | NO |
| 32 | Home | zh-Hans | Eyebrow | 使用范围 | B | 准确但像政策分类，不像首页小标题。 | YES |
| 33 | Home | zh-Hans | Trust body | @Link 邮箱用于维持 CUHK 学生使用范围；当前在读身份由用户自行声明。 | B | “维持使用范围”偏制度化；后半句清楚但正式。 | YES |
| 34 | Home | zh-Hans | Trust body | 用户须确认自己年满 18 岁。Meet at CU / 中意 由学生独立运营，不代表大学认可、赞助或背书。 | A | 合规边界清楚，语气可接受。 | NO |
| 35 | Home | zh-Hans | CTA heading | 想先把流程看清楚？ | B | 可读，但“先把…看清楚”重复了全站“先”句式。 | YES |
| 36 | Home | zh-Hans | CTA body | 了解资料会如何使用、匹配轮次如何参加，以及双方同意的完整流程。 | B | 信息完整但偏目录式，像自动摘要。 | YES |
| 37 | Home | zh-Hans | CTA | 查看如何运作 | B | 与“如何运作”同样略翻译腔。 | YES |
| 38 | How it works | zh-Hans | Page title | 如何运作 | B | 能懂但偏翻译腔。 | YES |
| 39 | How it works | zh-Hans | Hero body | 这是一个私密、低频的交友流程。你先完成资料；固定轮次开放后，再自行决定是否参加。 | B | 典型“定义产品 + 你先 + 先后流程”模型腔，文法没问题但不像自然 UI 起手。 | YES |
| 40 | How it works | zh-Hans | Section label | 完整流程 | A | 清楚自然。 | NO |
| 41 | How it works | zh-Hans | Step heading | 验证学生使用范围 | C | “使用范围”不是用户自然说法，像内部合规概念。 | YES |
| 42 | How it works | zh-Hans | Step body | 用 CUHK @Link 邮箱创建账户，并自行声明当前为在读学生且已年满 18 岁。@Link 验证不等于大学身份背书。 | B | 准确但太完整，且“大学身份背书”偏法律/内部表达。 | YES |
| 43 | How it works | zh-Hans | Step body | 你可以说明自己的生活、价值观和认识偏好。照片选填，未通过审核前不会向匹配对象展示。 | B | “说明自己的生活、价值观”像问卷设计说明，不像学生端文案。 | YES |
| 44 | How it works | zh-Hans | Step heading | 轮次开放后自主报名 | B | “轮次/自主报名”产品经理味较重。 | YES |
| 45 | How it works | zh-Hans | Step body | 完成资料不会让你自动加入匹配。每个固定轮次都需要由你主动选择参加。 | B | 清楚但“每个固定轮次都需要由你主动”过度显式第二人称。 | YES |
| 46 | How it works | zh-Hans | Step heading | 最多收到一位介绍 | B | 可懂，但“收到一位介绍”不够口语。 | YES |
| 47 | How it works | zh-Hans | Step body | 系统只在有合适人选时介绍一位；没有合适介绍也是正常结果，不代表你被拒绝。 | B | 安抚意图好，但“正常结果/不代表你被拒绝”像模型补全心理解释。 | YES |
| 48 | How it works | zh-Hans | Section heading | 两个人都说愿意，才会交换联系方式 | B | 自然度尚可，但“X 才 Y”结构与全站重复。 | YES |
| 49 | How it works | zh-Hans | Section body | 每个人都独立作出决定。只有双方都愿意认识，系统才会显示彼此主动提供的联系方式；一方不同意时，另一方不会看到其决定内容。 | B | 解释完整可靠，但句子过长，像政策说明压进产品页。 | YES |
| 50 | How it works | zh-Hans | Section heading | 不公开浏览，不无限匹配 | B | 对偶清楚，但 slogan 化。 | YES |
| 51 | How it works | zh-Hans | Bullet | 没有可供搜索或滑动的学生名单 | A | 简洁自然。 | NO |
| 52 | How it works | zh-Hans | Bullet | 原始问卷答案不会自动公开 | A | 明确自然。 | NO |
| 53 | How it works | zh-Hans | Bullet | 每轮最多介绍一位对象 | A | 明确自然。 | NO |
| 54 | How it works | zh-Hans | Bullet | 你可以不参加任何轮次 | A | 第二人称在这里自然。 | NO |
| 55 | How it works | zh-Hans | Section heading | 目前开放到哪一步，以首页为准 | A | 状态说明清楚，真实产品会这样写。 | NO |
| 56 | How it works | zh-Hans | Section body | 注册、轮次报名和结果公布是三个分开的阶段。首页会按当前公开状态清楚显示你现在可以做什么。Meet at CU / 中意 是独立学生项目，不是 CUHK 官方服务。 | B | 可读但很像把状态机解释给用户，略过度完整。 | YES |
| 57 | Privacy | zh-Hans | Page title | Meet at CU 隐私说明 | A | 标准自然。 | NO |
| 58 | Privacy | zh-Hans | Subtitle | 第一批真实用户前的资料边界 | D | 公共隐私页直接暴露“第一批真实用户前”像内部阶段说明，可能削弱信任。 | YES |
| 59 | Privacy | zh-Hans | Notice | Meet at CU / 中意 是独立学生项目，并非香港中文大学运营、认可、赞助或背书的服务。 | A | 合规边界自然。 | NO |
| 60 | Privacy | zh-Hans | Notice | 这页用普通语言说明目前产品实际收集和使用什么资料；它不是法律意见，也不代表外部法律审批已完成。 | D | “外部法律审批未完成”面向消费者显得未准备好，是产品信任问题。 | YES |
| 61 | Privacy | zh-Hans | Section heading | 目前不会发生的事 | A | 简明自然。 | NO |
| 62 | Privacy | zh-Hans | Section body | 没有公开浏览名单、滑动式匹配或公开个人目录。原始问卷答案不会自动公开，也不会完整显示给匹配对象。已验证的 CUHK @Link 不会自动成为匹配联系方式。 | A | 信息具体，隐私页可接受。 | NO |
| 63 | Privacy | zh-Hans | Section heading | @Link、身份与年龄声明 | A | 准确。 | NO |
| 64 | Privacy | zh-Hans | Section body | CUHK @Link 用于确认你控制一个 CUHK @Link 邮箱，帮助把早期账户范围限定在 CUHK 社群。这不等于我们替 CUHK 作官方身份证明，也不代表校方批准或运营本服务。 | B | 内容必要，但“控制一个邮箱/范围限定”偏法律化。 | YES |
| 65 | Privacy | zh-Hans | Section body | 目前在读学生身份和 18+ 由用户自行声明。若资料不实、滥用或出现安全问题，账户和参与资格可以被暂停或移除。 | B | “18+”和“参与资格”偏内部/合规表述。 | YES |
| 66 | Privacy | zh-Hans | Section body | 身份资料包括 @Link、身份验证账户、验证时间和账户状态，只用于登录、资格边界、支持和防滥用。 | B | “资格边界”不像普通用户语言。 | YES |
| 67 | Privacy | zh-Hans | Section body | 可被匹配对象看到的个人资料只限昵称、概括学业背景、兴趣、校园节奏、简介和你选择上传并通过审核的照片等资料。 | B | “校园节奏”抽象，整体像字段清单。 | YES |
| 68 | Privacy | zh-Hans | Section body | 问卷、偏好、敏感边界、匹配输入，以及安全和运营记录，会与可见的个人资料分开处理。匹配说明只展示安全的概括原因，不展示原始敏感答案。 | C | “敏感边界/匹配输入/安全的概括原因”内部系统词明显。 | YES |
| 69 | Privacy | zh-Hans | Section body | 微信号、WhatsApp 和你主动填写的联系邮箱存放在受保护的联系方式存储区，只会在同一介绍中的双方都明确同意后显示。 | B | 准确但“存储区/同一介绍”偏系统语言。 | YES |
| 70 | Privacy | zh-Hans | Section body | 个人照片是选填。照片审核只判断是否适合作为单人照片，不是身份验证、真人验证、脸部识别或吸引力评分。 | A | 具体且能建立信任。 | NO |
| 71 | Privacy | zh-Hans | Section body | 删除账户会移除或解除使用你的账户、个人资料、问卷、报名和联系方式；为防滥用、处理举报或保留审计完整性，少量最小化记录可能按需要保留。 | C | “解除使用你的账户”不自然，“审计完整性/最小化记录”较硬。 | YES |
| 72 | Privacy | zh-Hans | Section body | 首次提交 @Link 前会显示版本化个人资料收集声明，并只记录必要的版本、语言、显示和确认时间证据。 | C | “版本化/确认时间证据”明显合规实现语言。 | YES |
| 73 | Terms | zh-Hans | Subtitle | 第一批真实用户前的使用边界 | D | 公共条款暴露内测法律状态，像内部草稿。 | YES |
| 74 | Terms | zh-Hans | Notice | 这页说明目前初期版本的产品规则；正式法律审批仍需项目负责人和外部法律顾问确认。 | D | 直接说明法律审批未确认，影响用户信任，不只是文风。 | YES |
| 75 | Terms | zh-Hans | Rule body | 注册、报名和匹配发布可因安全或运营需要保持暂停。 | B | 信息重要，但“匹配发布/保持暂停”像内部状态。 | YES |
| 76 | Terms | zh-Hans | Section heading | 产品不是什么 | B | “不是 X”结构可读，但公共条款里略像 pitch deck。 | YES |
| 77 | Terms | zh-Hans | Rule body | 没有匹配是有效且正常的结果；平台不保证你一定会获得介绍、对方一定回复，或产生任何关系结果。 | B | 合理免责声明，但“有效且正常的结果”偏系统评价。 | YES |
| 78 | Terms | zh-Hans | Rule body | 系统按已冻结的产品合同进行周期式匹配；它不会为了填满名额而重用已发布匹配或降低质量边界。 | D | “已冻结的产品合同”是内部工程/规格语言，普通用户难以理解且显得草稿化。 | YES |
| 79 | Terms | zh-Hans | Rule body | Meet at CU 不是即时危机处理服务；如有人身安全或紧急风险，请立即联系本地紧急服务、可信任人士或校方支持渠道。 | A | 安全边界清楚自然。 | NO |
| 80 | Support | zh-Hans | Page title | 支持与安全 | A | 标准自然。 | NO |
| 81 | Support | zh-Hans | Subtitle | 需要协助 | A | 清楚自然。 | NO |
| 82 | Support | zh-Hans | Intro | 这页说明目前可以怎样处理账户、匹配、隐私和安全问题。 | B | 能懂，但“目前可以怎样处理”略翻译/说明书感。 | YES |
| 83 | Support | zh-Hans | Guidance | 如果你已能登录，请优先使用产品内的设置、屏蔽、举报和删除账户功能。 | A | 任务导向明确。 | NO |
| 84 | Support | zh-Hans | Section heading | 公开支持与隐私联系方式 | C | “公开支持”不像自然中文，像 direct translation of public support. | YES |
| 85 | Support | zh-Hans | Section body | 如你无法登录、需要隐私或删除支持，或需要回报无法在产品内处理的安全问题，可以电邮 support@cuhkdate.com。 | C | “需要隐私或删除支持/可以电邮”不自然。 | YES |
| 86 | Support | zh-Hans | Section heading | 登录后的支持路径 | B | 可懂，但“路径”产品流程味强。 | YES |
| 87 | Support | zh-Hans | Section body | 如果匹配或联系方式不符合预期，先检查是否已完成个人资料、问卷、主动报名和可用联系方式。 | B | 有帮助，但“主动报名和可用联系方式”像状态字段。 | YES |
| 88 | Support | zh-Hans | Section body | 删除会移除或解除使用账户、个人资料、问卷、报名和联系方式；少量最小化记录可能为安全、举报或审计需要保留。 | C | “解除使用账户”语义不顺，“最小化记录/审计”很硬。 | YES |
| 89 | Register | zh-Hans | Page title | 创建 Meet at CU / 中意 账户 | A | 标准自然。 | NO |
| 90 | Register | zh-Hans | Subtitle | 首次注册 | A | 自然。 | NO |
| 91 | Register | zh-Hans | Intro | 使用 CUHK @Link 邮箱建立账户；推荐码或推广码可以留空。 | A | 明确自然。 | NO |
| 92 | Register | zh-Hans | Form label | CUHK @Link 邮箱 | A | 自然。 | NO |
| 93 | Register | zh-Hans | Placeholder | 例如 student-id@link.cuhk.edu.hk | A | 标准。 | NO |
| 94 | Register | zh-Hans | Form label | 推荐码 / 推广码（选填） | A | 标准。 | NO |
| 95 | Register | zh-Hans | Help text | 只用于来源或以后奖励资格记录，不影响注册或匹配资格。 | B | 准确但“以后奖励资格记录”不像成熟产品正式文案。 | YES |
| 96 | Register | zh-Hans | Legal heading | 个人资料收集声明 | A | 标准。 | NO |
| 97 | Register | zh-Hans | Legal intro | 在你第一次提交 @Link 前，请先阅读此收集声明。@Link 只用作邮箱控制验证；当前学生身份和 18+ 会在后续流程另行由你自行声明。 | B | 信息清楚，但“邮箱控制验证/18+/另行由你自行声明”偏合规系统语。 | YES |
| 98 | Register | zh-Hans | Legal bullet | 必须资料包括 @Link 邮箱、验证/登录状态和基本账户安全记录；匹配资料、联系方式和个人相片只在你后续自愿填写或上传时收集。 | B | 法务信息合理，但句子密度高。 | YES |
| 99 | Register | zh-Hans | Legal bullet | 用途包括建立和保护账户、维持早期 CUHK 学生使用范围、提供匹配/安全/支持功能、处理资料查阅、更正和删除要求。处理者类别包括 Supabase、Cloudflare、Resend 及必要的授权支持人员。 | C | “处理者类别/授权支持人员”在入口页很硬，像合规模板直出。 | YES |
| 100 | Register | zh-Hans | Legal bullet | 交易/验证邮件不是市场推广同意。Meet at CU / 中意 是独立学生项目，并非 CUHK 官方运营、认可、赞助或背书。 | B | 内容必要，但“交易/验证邮件不是市场推广同意”不像自然中文。 | YES |
| 101 | Register | zh-Hans | Checkbox | 我已阅读个人资料收集声明 | A | 标准。 | NO |
| 102 | Register | zh-Hans | Button | 验证邮箱 | A | 标准。 | NO |
| 103 | Register | zh-Hans | Switch prompt | 已经有账户？ | A | 自然。 | NO |
| 104 | Register | zh-Hans | Switch button | 返回登录 | A | 自然。 | NO |
| 105 | Register/Login | zh-Hans | Info heading | 为什么需要 @Link | A | 自然。 | NO |
| 106 | Register/Login | zh-Hans | Info body | 首次注册会使用 CUHK @Link 邮箱，让早期社区保持在 CUHK 学生范围内。 | B | “早期社区保持在…范围内”偏项目说明。 | YES |
| 107 | Login | zh-Hans | Page title | 欢迎回来 | A | 自然。 | NO |
| 108 | Login | zh-Hans | Subtitle/Button | 登录 | A | 标准。 | NO |
| 109 | Login | zh-Hans | Intro | 使用你的 CUHK @Link 邮箱和密码登录。 | A | 第二人称在登录说明中自然。 | NO |
| 110 | Login | zh-Hans | Form/control | 密码 / 显示密码 / 忘记密码？ / 第一次使用？ / 注册 | A | 标准界面文案。 | NO |
| 111 | Common header | zh-Hant-HK | Brand link | Meet at CU 中意 | A | 品牌名直接、自然。 | NO |
| 112 | Common header | zh-Hant-HK | Nav group label | 公開頁面 | A | 可接受。 | NO |
| 113 | Common header | zh-Hant-HK | Nav link | 如何運作 | B | 港式繁中可懂，但仍有英式 how it works 直譯感。 | YES |
| 114 | Common header | zh-Hant-HK | Locale switch | 切換至簡體 | A | 自然。 | NO |
| 115 | Common header/footer | zh-Hant-HK | Links | 建立帳戶 / 私隱 / 條款 / 支援 | A | 港式用詞基本自然。 | NO |
| 116 | Home | zh-Hant-HK | Badge | 首批同學加入中 | B | 与简中一样，状态口号感略重。 | YES |
| 117 | Home | zh-Hant-HK | Hero subtitle | 給 CUHK 在讀學生的私密交友方式 | A | 自然。 | NO |
| 118 | Home | zh-Hant-HK | Hero body | 不公開瀏覽同學資料，也不用不停滑動。現在可以建立帳戶並完成資料；未來每個固定輪次仍由你自行決定是否參加。 | B | 过度完整，像把全部规则塞进 hero。 | YES |
| 119 | Home | zh-Hant-HK | Status heading | 只開放註冊 / 先把資料準備好 | B | 可读但 slogan 化，普通状态被包装得过于有设计感。 | YES |
| 120 | Home | zh-Hant-HK | Status body | 目前不會自動加入任何配對；第一輪開放後仍需由你主動報名。 | B | 清楚但“由你主動”重复英文 UX you 映射。 | YES |
| 121 | Home | zh-Hant-HK | Section heading | 不是刷資料，是在合適的時候認真認識一個人 | B | 对偶句漂亮，但模型式修辞明显。 | YES |
| 122 | Home | zh-Hant-HK | Section body | 先把自己說清楚；輪次開放後，再由你決定是否參加。 | C | “把自己說清楚”在繁中也别扭，有审问/自证感。 | YES |
| 123 | Home | zh-Hant-HK | Step/body group | 驗證並填寫 / 用 CUHK @Link 電郵建立帳戶，完成基本資料和問卷。 | A | 港式“電郵”自然，任务清楚。 | NO |
| 124 | Home | zh-Hant-HK | Step/body group | 自主參加輪次 / 固定輪次開放後，由你主動報名；完成資料不等於自動參加。 | B | “自主/輪次/由你主動”偏内部流程语。 | YES |
| 125 | Home | zh-Hant-HK | Step/body group | 每輪最多一位 / 只在有合適人選時介紹一位；沒有合適介紹也是正常結果。 | B | 标题自然，正文“正常結果”偏系统语气。 | YES |
| 126 | Home | zh-Hant-HK | Step/body group | 雙方各自同意 / 只有兩個人都願意認識，才會顯示彼此主動提供的聯絡方式。 | B | 合理但“只有 X 才 Y”与“主動提供”显得工整。 | YES |
| 127 | Home | zh-Hant-HK | Section heading | 你的資料，不會變成公開名單 | B | 安心感好，但“你的…”和逗号节奏略生成式。 | YES |
| 128 | Home | zh-Hant-HK | Section body | Meet at CU / 中意 把選擇權留給你，也把不必要的曝光降到最低。 | B | “把 X 留給你”广告化、模型润色感强。 | YES |
| 129 | Home | zh-Hant-HK | Trust bullets | 沒有公開學生目錄或滑動配對 / 沒有合適介紹是正常結果 / 相片選填，通過審核前不會向配對對象展示 / 聯絡方式只在雙方同意後顯示 | B | 大多自然，但“正常結果”仍偏系统语；整体可简化。 | YES |
| 130 | Home | zh-Hant-HK | Trust body | @Link 電郵用於維持 CUHK 學生使用範圍；現時在讀身份由用戶自行聲明。 | B | “維持…使用範圍”不太像学生端自然话。 | YES |
| 131 | How it works | zh-Hant-HK | Hero body | 這是一個私密、低頻的交友流程。你先完成資料；固定輪次開放後，再自行決定是否參加。 | B | 用户校准例句本身：产品自我定义、你先、先后结构都偏模型腔。 | YES |
| 132 | How it works | zh-Hant-HK | Step heading | 驗證學生使用範圍 | C | “使用範圍”是内部合规概念，不像用户任务。 | YES |
| 133 | How it works | zh-Hant-HK | Step body | 以 CUHK @Link 電郵建立帳戶，並自行聲明現時為在讀學生及已年滿 18 歲。@Link 驗證不等於大學身份背書。 | B | 港式用词自然，但“身份背書”仍很法律化。 | YES |
| 134 | How it works | zh-Hant-HK | Step body | 你可以說明自己的生活、價值觀和認識偏好。相片選填，未通過審核前不會向配對對象展示。 | B | 问卷说明味强，不太像学生面 UI。 | YES |
| 135 | How it works | zh-Hant-HK | Step body | 系統只在有合適人選時介紹一位；沒有合適介紹也是正常結果，不代表你被拒絕。 | B | 安抚意图明确，但“正常結果/不代表你被拒絕”显得过度解释。 | YES |
| 136 | How it works | zh-Hant-HK | Section body | 每個人都獨立作出決定。只有雙方都願意認識，系統才會顯示彼此主動提供的聯絡方式；一方不同意時，另一方不會看到其決定內容。 | B | 规则清楚但太完整，像政策页。 | YES |
| 137 | Privacy | zh-Hant-HK | Subtitle | 第一批真實用戶前的資料邊界 | D | 公开隐私页不应像内部 prelaunch 标记。 | YES |
| 138 | Privacy | zh-Hant-HK | Notice | 這頁用普通語言說明目前產品實際收集和使用甚麼資料；它不是法律意見，也不代表外部法律審批已完成。 | D | “法律審批未完成”是信任/状态问题。 | YES |
| 139 | Privacy | zh-Hant-HK | Section body | 問卷、偏好、敏感邊界、配對輸入，以及安全和營運記錄，會與可見的個人資料分開處理。配對說明只展示安全的概括原因，不展示原始敏感答案。 | C | “敏感邊界/配對輸入/安全的概括原因”内部词明显。 | YES |
| 140 | Privacy | zh-Hant-HK | Section body | 刪除帳戶會移除或解除使用你的帳戶、個人資料、問卷、報名和聯絡資料；為防濫用、處理舉報或保留審計完整性，少量最小化記錄可能按需要保留。 | C | “解除使用你的帳戶”不顺，“審計完整性/最小化記錄”硬。 | YES |
| 141 | Terms | zh-Hant-HK | Subtitle | 第一批真實用戶前的使用邊界 | D | 同简中，像内部草稿阶段。 | YES |
| 142 | Terms | zh-Hant-HK | Notice | 這頁說明目前初期版本的產品規則；正式法律審批仍需項目負責人和外部法律顧問確認。 | D | 公共条款呈现未完成法律审批，非单纯文风。 | YES |
| 143 | Terms | zh-Hant-HK | Rule body | 系統按已凍結的產品合同進行週期式配對；它不會為了填滿名額而重用已發布配對或降低品質邊界。 | D | “已凍結的產品合同/品質邊界”完全像内部规格语言。 | YES |
| 144 | Support | zh-Hant-HK | Section heading | 公開支援與私隱聯絡方式 | B | 港式“支援/私隱”自然，但“公開支援”仍略硬。 | YES |
| 145 | Support | zh-Hant-HK | Section body | 如你無法登入、需要私隱或刪除支援，或需要回報無法在產品內處理的安全問題，可以電郵 support@cuhkdate.com。 | C | “需要私隱或刪除支援”不自然。 | YES |
| 146 | Register | zh-Hant-HK | Intro | 使用 CUHK @Link 電郵地址建立帳戶；推薦碼或推廣碼可以留空。 | A | 港式自然。 | NO |
| 147 | Register | zh-Hant-HK | Help text | 只用於來源或日後獎勵資格記錄，不影響註冊或配對資格。 | B | “日後獎勵資格記錄”像内部字段说明。 | YES |
| 148 | Register | zh-Hant-HK | Legal intro | 在你第一次提交 @Link 前，請先閱讀此收集聲明。@Link 只用作郵箱控制驗證；現時學生身份和 18+ 會在後續流程另行由你自行聲明。 | B | 信息必要，但“郵箱控制驗證/18+/另行由你自行聲明”偏合规系统语。 | YES |
| 149 | Register | zh-Hant-HK | Legal bullet | 用途包括建立和保護帳戶、維持早期 CUHK 學生使用範圍、提供配對/安全/支援功能、處理資料查閱、更正和刪除要求。處理者類別包括 Supabase、Cloudflare、Resend 及必要的授權支援人員。 | C | 合规模板感强，入口页负担重。 | YES |
| 150 | Login | zh-Hant-HK | Login group | 歡迎回來 / 登入 / 使用你的 CUHK @Link 電郵地址和密碼登入。 / 顯示密碼 / 忘記密碼？ / 第一次使用？ / 註冊 | A | 登录页常规文案，第二人称自然。 | NO |

## Counts

A_COUNT = 53
B_COUNT = 72
C_COUNT = 15
D_COUNT = 10

## Top Recurring Modelish Patterns

1. Product self-definition before action: “这是/這是一個私密、低頻的交友流程” starts from concept framing, not user action.
2. Repeated explicit second person: “你先 / 由你 / 你的 / 你可以” appears where Chinese UI could often use neutral task phrasing.
3. Over-balanced contrast structures: “不是 X，是/而是 Y”, “只有 X，才 Y”, “先 X，再 Y” repeat across pages.
4. Ordinary status as slogan: “只开放注册 / 先把资料准备好” reads more designed than useful.
5. Internal product-state nouns: “轮次/輪次”, “资格边界”, “使用范围”, “产品合同”, “质量边界/品質邊界”.
6. Legally necessary content is often over-complete in consumer surfaces, especially registration privacy notice.
7. Trust copy sometimes over-explains emotional interpretation: “不代表你被拒绝”, “正常结果”.
8. zh-Hans sometimes reads like converted zh-Hant-HK rather than mainland-native product copy, especially “如何运作 / 资料 / 支持路径 / 电邮”.

## Most Important 20 Lines To Review

| # | LOCALE | EXACT ORIGINAL COPY | WHY WORTH DISCUSSING |
|---:|---|---|---|
| 1 | zh-Hans | 这是一个私密、低频的交友流程。你先完成资料；固定轮次开放后，再自行决定是否参加。 | 最典型 B 类：清楚但产品自我定义 + 你先 + 先后结构。 |
| 2 | zh-Hant-HK | 這是一個私密、低頻的交友流程。你先完成資料；固定輪次開放後，再自行決定是否參加。 | 繁中同样成立，是本轮模型腔校准样本。 |
| 3 | zh-Hans | 先把自己说清楚；轮次开放后，再由你决定是否参加。 | “把自己说清楚”可能让学生觉得被审问。 |
| 4 | zh-Hant-HK | 先把自己說清楚；輪次開放後，再由你決定是否參加。 | 繁中也不自然，不只是简繁转换问题。 |
| 5 | zh-Hans | 不是刷资料，而是在合适的时候认真认识一个人 | 漂亮但像 LLM slogan；需 founder 判断品牌是否真要这种语气。 |
| 6 | zh-Hant-HK | 不是刷資料，是在合適的時候認真認識一個人 | 同上，繁中版本还省了“而”，更像标语。 |
| 7 | zh-Hans | 只开放注册 / 先把资料准备好 | 普通状态被 slogan 化，可能不如直说当前可做什么。 |
| 8 | zh-Hant-HK | 只開放註冊 / 先把資料準備好 | 用户给的校准例子，值得人工定调。 |
| 9 | zh-Hans | 你的资料，不会变成公开名单 | 安心感强，但第二人称 + 逗号节奏略像生成式 UX 文案。 |
| 10 | zh-Hant-HK | Meet at CU / 中意 把選擇權留給你，也把不必要的曝光降到最低。 | “把 X 留给你”是高频模型式润色结构。 |
| 11 | zh-Hans | 验证学生使用范围 | 用户任务不像用户任务，像合规/权限模型。 |
| 12 | zh-Hans | 系统只在有合适人选时介绍一位；没有合适介绍也是正常结果，不代表你被拒绝。 | 过度安抚，“正常结果/不代表你被拒绝”像模型补全。 |
| 13 | zh-Hans | 第一批真实用户前的资料边界 | 公开隐私页出现 pre-user 阶段语，影响信任。 |
| 14 | zh-Hant-HK | 第一批真實用戶前的使用邊界 | 条款页同类 D 问题。 |
| 15 | zh-Hans | 这页用普通语言说明目前产品实际收集和使用什么资料；它不是法律意见，也不代表外部法律审批已完成。 | “法律审批未完成”不适合消费者公开页。 |
| 16 | zh-Hans | 正式法律审批仍需项目负责人和外部法律顾问确认。 | 明显内部状态/风险披露，需产品决策。 |
| 17 | zh-Hans | 系统按已冻结的产品合同进行周期式匹配；它不会为了填满名额而重用已发布匹配或降低质量边界。 | “产品合同/质量边界”是内部工程语言，普通用户不应看到。 |
| 18 | zh-Hant-HK | 系統按已凍結的產品合同進行週期式配對；它不會為了填滿名額而重用已發布配對或降低品質邊界。 | 繁中同样严重，且“品質邊界”更像 PRD。 |
| 19 | zh-Hans | 如你无法登录、需要隐私或删除支持，或需要回报无法在产品内处理的安全问题，可以电邮 support@cuhkdate.com。 | “需要隐私或删除支持/可以电邮”不自然。 |
| 20 | zh-Hans | 用途包括建立和保护账户、维持早期 CUHK 学生使用范围、提供匹配/安全/支持功能、处理资料查阅、更正和删除要求。处理者类别包括 Supabase、Cloudflare、Resend 及必要的授权支持人员。 | 注册入口法律说明密度过高，像合规模板，可能压过注册任务。 |

## Naturalness Hypotheses

1. 首页和 How it works 应优先回答“现在能做什么、下一步是什么”，少用“这是一个…”定义产品。
2. 中文 UI 里第二人称要更克制；登录/表单说明可用“你”，状态说明可改成无主语或“请先/完成后/目前”。
3. “轮次/資格邊界/使用范围/质量边界/产品合同”这类内部概念应替换成用户能感知的事件或状态。
4. 普通状态不要过度 slogan 化；“目前只开放注册”往往比“只开放注册 / 先把资料准备好”更像成熟产品。
5. 安全/隐私页可以精确，但应把实现细节和合规模板语言降到用户真正需要知道的程度。
6. “没有合适介绍也是正常结果”这类安抚可以保留含义，但语气应更人性，少像系统判定。
7. zh-Hans 不应只是 zh-Hant-HK 的字形转换；“如何运作、资料、支持路径、电邮”需要按内地学生语感重审。
8. zh-Hant-HK 的“私隱/支援/電郵/配對”基本自然，但“產品合同/品質邊界/公開支援”仍明显不属于消费者语域。
9. 一页中如果连续出现多组“不是 X，是 Y / 只有 X，才 Y / 先 X，再 Y”，单句都可读，整体也会显得像模型持续润色。
10. Founder 人工判断应优先定调：产品想要“安静、可信、普通学生产品”，还是“带一点品牌宣言感”；这会决定 B 类文案要不要改。