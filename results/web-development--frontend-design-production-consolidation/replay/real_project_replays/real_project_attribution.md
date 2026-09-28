# 真实项目 Frontend Design 归属回放

结论：三个项目均计为项目兼容性，独立插件能力计数为 0；成熟度保持 `unclassified`。这是冻结源码路由分析，不是 UI、发布或独立验收结果。规模标签是对文档所述工作的条件分类，不是新实现任务授权。

## Bobbio

**PROJECT**

Bobbio

**FROZEN_REF**

HEAD

**FROZEN_COMMIT**

445d31e5d5408b2a39948ad1d98613f6eb31e742

**COORDINATOR_SOURCE_CONSUMED**

/home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/system/source.md

**DELEGATE_SOURCES_CONSUMED**

- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/figma/source.md
- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/ux/source.md
- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/tokens/source.md
- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/responsive/source.md
- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/webapp-testing/source.md

**ROUTE_SUMMARY**

本轮为源码归属分析。项目路径为 canonical Figma → 已有产品/状态契约 → tokens/响应式交接 → 对应实现的浏览器验证。若开展后续完整生产 UI 实现，应按 S3/P0–P4 处理；局部修复仍按实际改动另定 S1/S2，不因使用 Figma 自动升级规模。历史原型只作交互/QA 基线，不能取代 Figma 或证明后续实现已收敛。

**REPO_LOCAL_RULE_GAVE_ANSWER**

是。FIGMA_HANDOFF 已直接指定 canonical Figma、原型历史地位、阅读/检查器结构和知识就绪语义；design-qa 与 browser-qa 已记录相应历史断言。因此 Figma 权威、响应式布局与 readiness 规则属于项目答案。

**COORDINATOR_GENERIC_DECISION_OBSERVED**

已观察到协调器按 F-A/F-C/F-D 把既定权威、委托及证据范围组织起来；但这些关键判断由 handoff、历史 QA 和本轮 rubric 已直接给出。S3 条件映射与委托名称匹配只记录为路由应用，不作为独立能力增量。未观察到可单独计数的通用决策。

**COUNTS_AS_COMPATIBILITY**

true

**COUNTS_AS_PLUGIN_CAPABILITY**

false

**EVIDENCE_LOCATOR**

- `/home/yuukias/code/Bobbio @ 445d31e5d5408b2a39948ad1d98613f6eb31e742:docs/design/FIGMA_HANDOFF.md` — frozen_text_source
- `/home/yuukias/code/Bobbio @ 445d31e5d5408b2a39948ad1d98613f6eb31e742:design-qa.md` — frozen_text_source
- `/home/yuukias/code/Bobbio @ 445d31e5d5408b2a39948ad1d98613f6eb31e742:docs/design/Bobbio_Product_Design_Review.pdf` — binary_locator_hash_only
- `/home/yuukias/code/Bobbio @ 445d31e5d5408b2a39948ad1d98613f6eb31e742:docs/design/prototype/qa/browser-qa.json` — frozen_text_source

**EVIDENCE_LIMITS**

- Figma 文件的存在、完成状态和历史 connector 限制仅由冻结 handoff 报告；本轮未打开 Figma、核验节点或做 round-trip。
- browser-qa.json 含历史真实交互断言及布局结果；本轮只是读取记录，未运行浏览器、查看截图或复测当前实现。
- PDF 仅验证 Git blob 与哈希，未解析或看图；其他引用截图/brief/代码不在清单读取范围。
- 历史 pre-Figma 原型 PASS 不能升级成当前 production、native、provider、持久化或独立验收 PASS。

## Lucerna

**PROJECT**

Lucerna

**FROZEN_REF**

origin/main

**FROZEN_COMMIT**

b626c2ce998882941dba0f30a00ecf627cc740b5

**COORDINATOR_SOURCE_CONSUMED**

/home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/system/source.md

**DELEGATE_SOURCES_CONSUMED**

- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/ux/source.md
- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/tokens/source.md
- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/responsive/source.md

**ROUTE_SUMMARY**

本轮为源码归属分析。以项目 v1 产品系统及 01052 补充为非 Figma 权威，按有界 S2 状态/呈现收敛理解 01052；01051 涉及的整面板层级收敛仍须整产品验收。UX/tokens/可访问性委托只检查既定契约，不重新设计。Windows Tauri/native-WebView、真实 provider、tray 生命周期与独立验收继续由项目流程负责，浏览器委托不能替代。

**REPO_LOCAL_RULE_GAVE_ANSWER**

是。产品系统明确要求不依赖 Figma 或通用 Frontend Design 插件重新决策；v1/01052 已冻结层级、tokens、身份、聚合状态和动作。AGENTS 与视觉验收流程直接规定真实 Windows release、全展开面板、模型看图和独立审查。这些不归功于候选插件。

**COORDINATOR_GENERIC_DECISION_OBSERVED**

已观察到协调器尊重非 Figma 权威、服从更严格的项目验收并排除浏览器替代原生证明；但上述边界全部由项目规则直接规定。S2 命名及选择委托不独立证明候选插件解决了项目原本未解决的问题。未观察到可单独计数的通用决策。

**COUNTS_AS_COMPATIBILITY**

true

**COUNTS_AS_PLUGIN_CAPABILITY**

false

**EVIDENCE_LOCATOR**

- `/home/yuukias/code/Lucerna @ b626c2ce998882941dba0f30a00ecf627cc740b5:AGENTS.md` — frozen_text_source
- `/home/yuukias/code/Lucerna @ b626c2ce998882941dba0f30a00ecf627cc740b5:docs/workflows/LUCERNA_VISUAL_ACCEPTANCE.md` — frozen_text_source
- `/home/yuukias/code/Lucerna @ b626c2ce998882941dba0f30a00ecf627cc740b5:docs/design/lucerna/LUCERNA_UI_PRODUCT_SYSTEM_V1.md` — frozen_text_source
- `/home/yuukias/code/Lucerna @ b626c2ce998882941dba0f30a00ecf627cc740b5:docs/design/lucerna/LUCERNA_EXTENSION_IDENTITY_STATUS_AUTH_V1.md` — frozen_text_source

**EVIDENCE_LIMITS**

- 读取的是冻结 origin/main 对应 commit 的四份规则文件，不是脏工作树，也未拉取、检出或修改目标仓库。
- 这些文件是规范而非当前原生运行证据；未构建/启动 Windows release，未执行 view_image 预检、截图、交互、tray/DPI 或独立审查。
- 未访问任何 provider、credential、认证入口或同步功能；不推断本机认证成功、失败或需要用户操作。
- 未触发文件中描述的 Windows sandbox fallback；没有本轮失败证据，不能声称存在该 blocker。

## Asteria

**PROJECT**

Asteria

**FROZEN_REF**

HEAD

**FROZEN_COMMIT**

f2fbbc3cd2edb3f005ae939f8d30637966256098

**COORDINATOR_SOURCE_CONSUMED**

/home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/system/source.md

**DELEGATE_SOURCES_CONSUMED**

- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/direction/source.md
- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/tokens/source.md
- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/responsive/source.md
- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/webapp-testing/source.md
- /home/yuukias/.codex/plugins/cache/ai-skills-candidate/web-development/0.3/skills/visual/_src/research/source.md

**ROUTE_SUMMARY**

本轮为源码归属分析。已接受概念图是视觉/交互参考，科学事实由 README 指定的文本权威控制；先通用协调器，再视觉、tokens、可访问性与浏览器证据委托，最后叠加 research 专项约束。RC15 可视为既有产品内的 S2 有界视觉系统修复，但跨视图的重要收敛仍需要整屏和独立判断，不能按微小 S1 修补豁免。无需为该非 Figma 路径新增 Figma。

**REPO_LOCAL_RULE_GAVE_ANSWER**

是。accepted-concepts README 已明确概念图只管视觉/交互、不管公式、作者、引用和结果事实。RC15 报告已给出图形规则、自检结果及下一步截图审查。科学边界、图形修复与历史 PASS 均来自项目材料。

**COORDINATOR_GENERIC_DECISION_OBSERVED**

已观察到协调器先处理通用设计路由、再使用 research 专项委托，并保留视觉与科学权威边界；但这一案例中的实质答案及待审查状态已由项目文档给出。委托顺序符合插件契约，但单凭该一致性不能证明新增能力。未观察到可单独计数的通用决策。

**COUNTS_AS_COMPATIBILITY**

true

**COUNTS_AS_PLUGIN_CAPABILITY**

false

**EVIDENCE_LOCATOR**

- `/home/yuukias/code/Asteria @ f2fbbc3cd2edb3f005ae939f8d30637966256098:docs/design/accepted-concepts/README.md` — frozen_text_source
- `/home/yuukias/code/Asteria @ f2fbbc3cd2edb3f005ae939f8d30637966256098:results/asteria_v2_rc15_visual_system_result.md` — frozen_text_source
- `/home/yuukias/code/Asteria @ f2fbbc3cd2edb3f005ae939f8d30637966256098:docs/design/accepted-concepts/A_light_architecture.png` — binary_locator_hash_only
- `/home/yuukias/code/Asteria @ f2fbbc3cd2edb3f005ae939f8d30637966256098:docs/design/accepted-concepts/B_dark_architecture.png` — binary_locator_hash_only
- `/home/yuukias/code/Asteria @ f2fbbc3cd2edb3f005ae939f8d30637966256098:docs/design/accepted-concepts/C_symbol_trace.png` — binary_locator_hash_only
- `/home/yuukias/code/Asteria @ f2fbbc3cd2edb3f005ae939f8d30637966256098:docs/design/accepted-concepts/D_variant_diff.png` — binary_locator_hash_only
- `/home/yuukias/code/Asteria @ f2fbbc3cd2edb3f005ae939f8d30637966256098:docs/design/accepted-concepts/E1_lineage.png` — binary_locator_hash_only
- `/home/yuukias/code/Asteria @ f2fbbc3cd2edb3f005ae939f8d30637966256098:docs/design/accepted-concepts/E2_evidence.png` — binary_locator_hash_only

**EVIDENCE_LIMITS**

- 六幅 PNG 仅按 binary_locator_only 校验 blob/hash，未解码查看像素；只能依据 README 解释角色。
- RC15 的 COMPLETE、浏览器/公开部署/性能/视觉 PASS 都是历史生产者报告，本轮未运行命令、访问 URL 或复核截图。
- 该报告的下一步仍为截图审查；不能把自检等同于独立确认，也不能据其宣称当前整产品已通过验收。
- 科学文本权威只读取了 README 中的定位关系，未读取清单外论文/公式/实现；没有核实科学正确性或现有运行性能。
