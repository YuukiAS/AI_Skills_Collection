# 插件使用与文件证据

本会话已使用 web-development 0.4 做页面内容判断，再使用 writing-style 0.4 的 Product UI Copy 做受保护含义下的措辞处理，并返回前端流程核对渲染证据。两者在同一回放会话中实际读取和应用；不是仅依据插件名称声明使用。截图缺失使完整视觉验收无法完成，报告已保留这一限制。

## 候选与输入边界

- 候选提交：`a06ff050bc82bb22358dfcb3e4faa885fddd285b`，由任务和捕获摘要共同指定；不把它推断为网站部署提交。
- 阶段：**Phase 1 blind live-site input**，即第一阶段盲评公开网站捕获。
- 捕获时间：`2026-09-29T13:47:43+08:00`。
- 网站事实仅来自下列 12 个输入文件。候选技能文件仅用于审阅方法，不作为网站事实来源。
- 未使用 2026-09-26 历史审计作为候选输入，也未读取或推断其结论。
- 未登录、注册、提交表单、调用私有 API、访问网站仓库或源码；未联网补充网站或法律事实。
- 未调优插件、修改源文件、创建新 holdout 或新捕获。仅生成本次要求的两个输出文件。

## 同会话的实际使用

| 插件 | 实际读取的技能与流程 | 在输出中的作用 |
|---|---|---|
| web-development 0.4 | `skills/visual/SKILL.md`、`_src/system/source.md`、`_src/ux/source.md`、`_src/responsive/source.md` | 先确定页面用途、文本角色、邻文重复和删并责任；最后区分文本证据与真实渲染验收 |
| writing-style 0.4 | `skills/product-ui-copy/SKILL.md` | 分类 KEEP、措辞、语言地区、内容架构、产品语义与信任问题；固定含义后给最小修改；事实未定时升级 |
| writing-style 0.4 | `skills/zh/SKILL.md` | 只对两份中文报告的叙述做自然表达终审，不替代产品界面文案流程 |

实际技能根路径为：

- `/home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.4/`
- `/home/yuukias/.codex/plugins/cache/ai-skills-candidate/writing-style/0.4/`

未进行插件安装、版本切换或源文件修复。本证据证明本会话消费了这些路径中的候选技能；未独立核验整套安装包与候选 Git 提交的逐文件对应关系，不把目录版本号当成该对应关系的证明。

## 输入文件身份

以下路径相对于本次工作区，SHA-256 根据实际读取的文件字节计算。

| 输入 | SHA-256 |
|---|---|
| `inputs/01-LIVE_SITE_CAPTURE.md` | `75d1bd7f197bea909310e17671d5709272fedf03efa30c05095284c7534fb624` |
| `inputs/02-LIVE_SITE_PAGE_SUMMARY.json` | `f1f92c4b4e585330e9338204fd4cce0248ca5c21f2c66b00e07e768c862d38d7` |
| `inputs/03-zh-Hant-HK_home.txt` | `d23acb4961bbb11bacc68070fef5e390c3fd525f12c6d43be27d1ee1ef7ae06e` |
| `inputs/04-zh-Hant-HK_how-it-works.txt` | `c7d84507cf9e214af59737c21c103aa53843cd618b0bb1363b6e4a4aeb89bef2` |
| `inputs/05-zh-Hant-HK_privacy.txt` | `80e2ea18774e959fec8841f1735653b274c38d9f10ce858a730ccefb4994a79b` |
| `inputs/06-zh-Hant-HK_terms.txt` | `9dda29a54dc2229f889d4273e092c391bd4e1b51cfc206b789ba8898b3f0435b` |
| `inputs/07-zh-Hant-HK_support.txt` | `e054ddcef3d296ae463480fedcf428c180e81562b52ebea65ceed96688adbd4e` |
| `inputs/08-zh-Hans_home.txt` | `196d787e22d16982c9d9f6e779810d81a1855e05b63552e6f68c1a66cbe2d438` |
| `inputs/09-zh-Hans_how-it-works.txt` | `3ae8df2b7211438b94c6e187cc74cbf616ab73aad8ce024a44131fa68974265b` |
| `inputs/10-zh-Hans_privacy.txt` | `802e1df29e257548bb6a6ef98b16ee6fa8e0148a0ace03755d9b196dc44061f0` |
| `inputs/11-zh-Hans_terms.txt` | `b3b790cc2541b9fb05fbd8cafa6640e644e92a25ec774f60e9979a0460d4a47f` |
| `inputs/12-zh-Hans_support.txt` | `6eb73d04d7c2141745c8327e4b76555d0f0f998ea45b1f645b9d2c9200c6d566` |

输入 01 提供完整捕获文本与公开 URL，输入 02 提供页面、语言、时间、状态码及资源定位，输入 03–12 提供每页的文本。摘要中的 `screenshots/`、`dom/` 和 `visible_text/` 是捕获资源定位，不等于附件中的实际文件。未发现所列截图或原始 DOM 文件，因此未声称查看了截图。

## 输出文件身份

- 工作区：`/home/yuukias/AI_Skills_Collection-product-ui-copy--cross-plugin-production-integration/.local-runtime/candidate-plugin-replay/runs/20260929T054911Z-1132248/workspace`。
- `outputs/LIVE_SITE_COPY_REVIEW.md`：页面级判断、36 个真实例子、两种语言的独立观察、未决产品事实及渲染证据限制。SHA-256：`56d29f1ff1557b1b3eed62afa3e6ab8bea8e4ba4000dca9ab94cb45d0dfdfeb8`。
- `outputs/PLUGIN_CONSUMPTION_EVIDENCE.md`：本文件，记录候选、同会话技能使用、输入和输出身份。为避免自引用哈希，不在本文件写入自身哈希。

## 完成范围

已交付要求的两份评审文件。审阅覆盖两种语言各 5 个可达公开页面；4 条注册／登录路由只按摘要记录为 404，不评审未提供的页面内容。正文列有 6 个 CONTENT ARCHITECTURE 例子，并明确区分可直接润色项和需产品／隐私／法律负责人确认的项目。升级项只指出输入内部的承诺及信息缺口，不构成法律合规结论。

这是本次候选在这批输入上的首轮评审产物，不是用户接受记录、整站上线批准、完整渲染通过或对历史版本的比较结果。
