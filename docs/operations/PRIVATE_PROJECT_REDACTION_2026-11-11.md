# 公开仓库私有项目信息清理记录

可编辑文本和重新生成的插件文件已清除本次指定的项目名称及私有定位；另有 42 份历史构建记录、字体配置按要求原样保留，等待协调者决定。因此当前工作树尚未完全清零。改动后的 406 项测试全部通过，生成一致性检查通过，原本有效的 Markdown 相对文件链接未因本次改名断开。

本次仅修改指定清理工作树，未提交、推送、切换分支或修改 Git 历史。原始私有材料不写入这份记录。

## 删除和内容清理

删除了 2026-11-11 的整篇被拒技术讲解，共 730 行。原文留在私有项目仓库，此处不保存。以下 4 个维护入口仅保留写作或版式问题：

- `docs/plugin-todos/research-writing.md`：定义和说明分散、实现记录挤占正文、常规章节被写成问答。
- `docs/plugin-todos/scientific-visualization.md`：通用方框串掩盖分支、关系语义和阅读路径。
- `docs/plugin-todos/writing-style.md`：中英混杂、未解释缩写、机械否定句与过度独立排版。
- `docs/skill-todos/artifact-content-design.md`：内部记录占据首页，读者需要的对照与结构不足。

旧讲解之外的相关写作示例、图稿反馈和逐页批注，也已移除私有计算过程、参数、结果及模型结构，只保留通用的表达与版式反馈。原先进入写作参考的私有数学示例改成明确标注的合成骰子算例。

## 改名映射

旧路径中的项目标识在下表用 `〈已隐去标识〉` 代替，避免清理记录再次暴露名称；每行与改名前路径一一对应。Git 元数据只读，实际尝试 `git mv` 时无法创建 `index.lock`，错误为 `Read-only file system`。已完成文件系统改名及引用更新，协调者暂存时需纳入旧文件删除与新文件，Git 才能记录重命名。

| 旧路径（已遮蔽项目标识） | 新路径 |
| --- | --- |
| `docs/provenance/RESEARCH_PRESENTATION_〈已隐去标识〉_ITERATION_2026_08_25.md` | `docs/provenance/RESEARCH_PRESENTATION_PRIVATE_PROJECT_ITERATION_2026_08_25.md` |
| `docs/provenance/RESEARCH_PRESENTATION_〈已隐去标识〉_V2_REVIEW_2026_08_27.md` | `docs/provenance/RESEARCH_PRESENTATION_PRIVATE_PROJECT_V2_REVIEW_2026_08_27.md` |
| `docs/provenance/RESEARCH_PRESENTATION_〈已隐去标识〉_V3_REVIEW_2026_08_27.md` | `docs/provenance/RESEARCH_PRESENTATION_PRIVATE_PROJECT_V3_REVIEW_2026_08_27.md` |
| `docs/provenance/research-presentation-maintenance-archive-2026-08-30/TODO_〈已隐去标识〉_V2_CANDIDATES_2026_08_27.md` | `docs/provenance/research-presentation-maintenance-archive-2026-08-30/TODO_PRIVATE_PROJECT_V2_CANDIDATES_2026_08_27.md` |
| `docs/provenance/research-presentation-maintenance-archive-2026-08-30/TODO_〈已隐去标识〉_V3_CONFIRMED_2026_08_27.md` | `docs/provenance/research-presentation-maintenance-archive-2026-08-30/TODO_PRIVATE_PROJECT_V3_CONFIRMED_2026_08_27.md` |
| `docs/provenance/research-presentation-maintenance-archive-2026-08-30/TODO_〈已隐去标识〉_V3_MANDATORY_CANDIDATES_2026_08_27.md` | `docs/provenance/research-presentation-maintenance-archive-2026-08-30/TODO_PRIVATE_PROJECT_V3_MANDATORY_CANDIDATES_2026_08_27.md` |

已删除的整篇讲解没有新路径。源码、测试、清单、历史记录及归档目录中的相关文件名引用均已同步。

## 替换与测试夹具

中文正文首次使用“某私有统计研究项目”，之后可称“该项目”；英文使用“a private research project”。标识符和文件名按用途使用 `private_project`、`PRIVATE_PROJECT`、`private-project`。仓库地址、本机项目目录、相关私有提交与分支定位已删除或替换为 `<private repository>` 等占位。独立出现且指向已发表方法的 `TRACE` 保留。其他项目按用户要求只盘点，不擅自清理。

防泄漏断言保留，并改用合成名称 `PRIVATE-PROJECT-X`。演示文稿测试将合成私有内容写入临时维护文件，调用真实打包复制函数，确认公开说明仍会复制、维护文件及私有标记不会进入产物；线程交接夹具使用合成项目名，仍检查项目专属名称不得进入通用技能正文。

本次没有新增功能或发布版本。Repository bump decision: NONE；相关插件均为 NO_BUMP。原因是隐私清理与公开安全示例替换，不是一次正式功能发布。

## 验证结果

改动前与改动后均运行：

```bash
python3 -m unittest discover -s tests
```

改动前基线为 `2bac8f609d1f11e8f1a3fa44a371d116af4132bf`。写入任何清理改动前，实际运行结果如下：

```text
FAIL: test_generated_layer_matches_source_config
      (test_codex_marketplace.CodexMarketplaceTests)
AssertionError: ['publication layer is not current (3 differences)'] != []
Ran 406 tests in 273.313s
FAILED (failures=1)
```

这是唯一已有失败：writing-style 的两个参考文件尚未生成，`response-clarity/SKILL.md` 也与源文件不一致。原始基线日志保存在本机 `/tmp/redact-baseline-tests.log`；以上保留了公开安全的运行证据。重新生成时这 3 处已有差异随源文件同步，没有手改生成文件。

改动后：`Ran 406 tests in 269.131s`，`OK`，退出码 0。另单独运行过线程交接合同 11 项和防泄漏打包测试 1 项，均通过。

以下检查均通过：

```bash
python3 scripts/build_codex_marketplace.py --validate --check --path-report
python3 scripts/skills.py validate
python3 scripts/skills.py audit --all
git diff --check
```

有效技能 156 个、profile 18 个；生成层含 10 个插件、30 个 active skills、73 个源快照。Windows 路径最大 140 字符，无超限；audit 给出的预算提示是建议，不是失败。

生成命令 `python3 scripts/build_codex_marketplace.py --write` 已重新生成插件文件，但在最后重写受保护的 `.agents/plugins/marketplace.json` 时退出 1。随后实际调用同一现有生成器的 `generate_layer`，在临时输出目录完成整套生成，错误和警告均为 0；生成清单与工作树只读清单逐字节相同。最终 `--validate --check` 通过，证明工作树产物与源文件一致。未修改生成器，也未手改生成文件。

逐文件检查 JSON/JSONL 均可解析。对改名前已有且存在目标的 Markdown 相对文件链接逐一更新并核对，新增断链为 0。扫描也遇到 182 个原有未解析的链接或文档示例，未将其计为本次新增问题，未扩展修复。

名称检查同时覆盖受跟踪内容和新增文件。原始 `git grep -n -i -E` 名称扫描仍有 42 行，全部对应下表的 42 份例外；排除这些例外后为 0，现存文件名中也无目标名称。为了避免再次写入待清除名称，此处不复写扫描表达式。

## 留给协调者决定的历史产物

初始 `git grep -l -i -E` 扫描命中 126 个文件，随后逐个按类型核对。额外检查了 536 个 PNG、40 个 PDF、8 个 PPTX、54 个 TTF 和 1 个 ZIP：检查原始字节，提取 PDF 文本，并解包检查 PPTX/ZIP 成员，均未发现本次目标名称。不据此推断图像像素内的文字已通过 OCR。

以下 42 个文件是 14 组旧构建产物：JSON 中的 `times_font_dir`、XML 中的 `<dir>` 都保留了同一私有字体目录。已检查 14 份依赖记录中的原字体目录，当前机器可用数量为 0。它们虽可按文本读取，却记录当时的构建环境；当前生成插件的命令不会重建这些记录。用当前程序重跑归档任务也不能还原原来那次环境证据，因此未改写或删除。逐个 SHA-256 已与改动前比较，全部相同。协调者需决定是否删除、遮蔽这些历史记录，或另行批准重新构建。

| 文件 | 行 | 类型 | 出现方式 |
| --- | --- | --- | --- |
| `docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated/BUILD_MANIFEST.json` | 28 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated/cuhk_stage3_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/031_research_presentation_one_call_production_entry/generated/BUILD_MANIFEST.json` | 34 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/031_research_presentation_one_call_production_entry/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/031_research_presentation_one_call_production_entry/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/032_research_presentation_storyline_coherence_recovery/generated/BUILD_MANIFEST.json` | 35 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/032_research_presentation_storyline_coherence_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/032_research_presentation_storyline_coherence_recovery/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/033_research_presentation_deck_rhythm_quality_loop/generated/BUILD_MANIFEST.json` | 303 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/033_research_presentation_deck_rhythm_quality_loop/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/033_research_presentation_deck_rhythm_quality_loop/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/034_research_presentation_render_identity_ci_recovery/generated/BUILD_MANIFEST.json` | 560 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/034_research_presentation_render_identity_ci_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/034_research_presentation_render_identity_ci_recovery/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/035_research_presentation_generic_model_support_recovery/generated/BUILD_MANIFEST.json` | 560 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/035_research_presentation_generic_model_support_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/035_research_presentation_generic_model_support_recovery/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/036_research_presentation_process_page_projection_recovery/generated/BUILD_MANIFEST.json` | 560 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/036_research_presentation_process_page_projection_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/036_research_presentation_process_page_projection_recovery/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/037_research_presentation_audience_transition_copy_recovery/generated/BUILD_MANIFEST.json` | 559 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/037_research_presentation_audience_transition_copy_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/037_research_presentation_audience_transition_copy_recovery/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/038_research_presentation_two_real_paper_holdouts/medical/generated/BUILD_MANIFEST.json` | 509 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/038_research_presentation_two_real_paper_holdouts/medical/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/038_research_presentation_two_real_paper_holdouts/medical/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/BUILD_MANIFEST.json` | 439 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/039_research_presentation_quality_loop_execution_recovery/generated/BUILD_MANIFEST.json` | 693 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/039_research_presentation_quality_loop_execution_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/039_research_presentation_quality_loop_execution_recovery/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated/BUILD_MANIFEST.json` | 618 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/BUILD_MANIFEST.json` | 675 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/042_research_presentation_semantic_compatibility_recovery/generated/BUILD_MANIFEST.json` | 741 | JSON 构建记录 | times_font_dir 私有字体目录字段 |
| `results/042_research_presentation_semantic_compatibility_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 4 | XML 字体配置 | XML 字体目录字段 |
| `results/042_research_presentation_semantic_compatibility_recovery/generated/dependency_probe.json` | 56 | JSON 构建记录 | times_font_dir 私有字体目录字段 |

## 其他项目信息盘点（只报告）

以下是当前内容的候选盘点，共 861 个文件。这里只记录仓库内相对文件、行号和内容类型，不重复抄录数据、完整仓库地址或本机路径值。DII、CARE、MoSAiC、实验室名称及其他项目名的出现，不自动证明相关内容未公开；其隐私属性仍需协调者确认。本次未据此替换其他项目内容。

该表覆盖文本中出现的项目名、仓库地址和 `/users`、`/overflow`、`/home`、`/nas`、`/work`、`/scratch` 路径；通用工具路径也会作为候选列出。行号按清理后的工作树计算，不包含本记录自身。

| 文件 | 行号与内容类型 |
| --- | --- |
| `.github/workflows/ai-bridge-text-review.yml` | 其他仓库地址或项目名（隐私属性待确认）：35 |
| `.github/workflows/ai-bridge-visual-review.yml` | 其他仓库地址或项目名（隐私属性待确认）：35 |
| `.github/workflows/research-presentation-candidate-visual-finish-review.yml` | 其他仓库地址或项目名（隐私属性待确认）：19 |
| `.github/workflows/research-presentation-comparative-visual-review.yml` | 其他仓库地址或项目名（隐私属性待确认）：19 |
| `.gitignore` | 其他仓库地址或项目名（隐私属性待确认）：16–18 |
| `CHANGELOG.md` | DII 项目标识或研究记录：34；CARE 名称或数据相关描述（候选）：34；本机绝对路径：912；其他仓库地址或项目名（隐私属性待确认）：912 |
| `archive/legacy-bundles/cmr.json` | 其他仓库地址或项目名（隐私属性待确认）：3 |
| `automation/reviewed_handoff/tasks/014_presentation_phase_a_recovery/PLAN.md` | 本机绝对路径：32 |
| `automation/reviewed_handoff/tasks/015_presentation_terra_blocker_repair/PLAN.md` | 本机绝对路径：51 |
| `automation/reviewed_handoff/tasks/018_presentation_external_method_audit/PLAN.md` | 本机绝对路径：204 |
| `automation/reviewed_handoff/tasks/019_research_presentation_exemplar_composition_representation/PLAN.md` | 本机绝对路径：350 |
| `automation/reviewed_handoff/tasks/020_research_presentation_reference_calibrated_candidate_search/PLAN.md` | 本机绝对路径：338 |
| `automation/reviewed_handoff/tasks/021_research_presentation_comparative_reference_calibrated_visual_review/PLAN.md` | 本机绝对路径：285 |
| `automation/reviewed_handoff/tasks/022_research_presentation_candidate_visual_finish_repair/PLAN.md` | 本机绝对路径：279 |
| `automation/reviewed_handoff/tasks/044_writing_style_deep_research_chinese_replay/PLAN.md` | CARE 名称或数据相关描述（候选）：166 |
| `automation/reviewed_handoff/tasks/052_writing_style_reader_facing_generalization_closure/REQUEST.md` | 本机绝对路径：32 |
| `automation/reviewed_handoff/tasks/055_clear_writing_release_convergence/REQUEST.md` | 本机绝对路径：24 |
| `automation/reviewed_handoff/tasks/documents-media--pdf-save-as-delivery/PLAN.md` | 本机绝对路径：30 |
| `automation/reviewed_handoff/tasks/documents-media--pdf-save-as-delivery/REQUEST.md` | 本机绝对路径：15 |
| `automation/reviewed_handoff/tasks/hpc--slurm-cancel-production-closure/PLAN.md` | DII 项目标识或研究记录：35、129；CARE 名称或数据相关描述（候选）：35、129；实验室标识：48、108、128 |
| `automation/reviewed_handoff/tasks/hpc--slurm-cancel-production-closure/REQUEST.md` | 本机绝对路径：13 |
| `automation/reviewed_handoff/tasks/hpc--slurm-race-policy-bounded-opt-in/REQUEST.md` | DII 项目标识或研究记录：20 |
| `automation/reviewed_handoff/tasks/infra_paid_review_safety_migration_20260903/REQUEST.md` | 其他仓库地址或项目名（隐私属性待确认）：45 |
| `automation/reviewed_handoff/tasks/product-ui-copy--cross-plugin-production-integration/PLAN.md` | 本机绝对路径：38 |
| `automation/reviewed_handoff/tasks/product-ui-copy--cross-plugin-production-integration/REQUEST.md` | 本机绝对路径：13 |
| `automation/reviewed_handoff/tasks/web-development--frontend-design-production-consolidation/PLAN.md` | 本机绝对路径：25 |
| `automation/reviewed_handoff/tasks/web-development--frontend-design-production-consolidation/REQUEST.md` | 本机绝对路径：13 |
| `automation/reviewed_handoff/tasks/workflow-core--reviewed-first-bootstrap-normal-entry/REQUEST.md` | 本机绝对路径：13 |
| `docs/LOCAL_CONFIGURATION.md` | 本机绝对路径：77；其他仓库地址或项目名（隐私属性待确认）：77 |
| `docs/PLUGIN_MATURITY.md` | DII 项目标识或研究记录：29 |
| `docs/REPOSITORY_BOUNDARY.md` | 其他仓库地址或项目名（隐私属性待确认）：8 |
| `docs/SKILL_CATALOG.md` | CARE 名称或数据相关描述（候选）：109、112 |
| `docs/audits/ACTIVE_SKILL_CALLING_AUDIT.json` | 其他仓库地址或项目名（隐私属性待确认）：575、1708、1756、1803、1881、1928、3166、3308、3422、3561、3632、4025、4955、5037、5587、5675；CARE 名称或数据相关描述（候选）：1951–1952、2046–2047 |
| `docs/audits/ACTIVE_SKILL_CAPABILITY_MAP.md` | 其他仓库地址或项目名（隐私属性待确认）：160、164、198–200、202–203、211、213、220、226、230、232、241、294、305；CARE 名称或数据相关描述（候选）：172、175 |
| `docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated/BUILD_MANIFEST.json` | 本机绝对路径：22、25、28；其他仓库地址或项目名（隐私属性待确认）：22、28 |
| `docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated/cuhk_stage3_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、63、65、69、71、74；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、63、65、69、71、74 |
| `docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated/cuhk_stage3_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated/cuhk_stage3_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1202、1206；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1202、1206 |
| `docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `docs/audits/research_presentation_cuhk_scientific_layout_stage3/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `docs/design/056_DELIVERY_WORKFLOW_RELIABILITY_BASELINE_V0_4_CRITIC_PROMPT_2026-09-21.md` | 其他仓库地址或项目名（隐私属性待确认）：11 |
| `docs/design/056_DELIVERY_WORKFLOW_RELIABILITY_BASELINE_V0_5_CRITIC_PROMPT_2026-09-21.md` | 其他仓库地址或项目名（隐私属性待确认）：17 |
| `docs/design/056_DELIVERY_WORKFLOW_RELIABILITY_BASELINE_V6_AMENDMENT_2026-09-21.md` | 其他仓库地址或项目名（隐私属性待确认）：9 |
| `docs/design/056_FINAL_INTEGRATION_RELEASE_CRITIC_PROMPT_V0_1_2026-09-22.md` | 其他仓库地址或项目名（隐私属性待确认）：58；本机绝对路径：198–199、208、219、224、242 |
| `docs/design/056_FINAL_INTEGRATION_RELEASE_CRITIC_PROMPT_V0_2_2026-09-22.md` | 其他仓库地址或项目名（隐私属性待确认）：60 |
| `docs/design/056_FINAL_INTEGRATION_RELEASE_PLAN_V0_1_2026-09-22.md` | 本机绝对路径：108、111、241、246、262、267 |
| `docs/design/056_FINAL_INTEGRATION_RELEASE_PLAN_V0_2_2026-09-22.md` | 本机绝对路径：127、130、260、265、281、286 |
| `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_IMPLEMENTATION_PLAN.md` | CARE 名称或数据相关描述（候选）：205 |
| `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_POST_057_SOURCE_DRIFT_REVALIDATION_2026-09-18.md` | 其他仓库地址或项目名（隐私属性待确认）：31、123 |
| `docs/design/056_PRODUCT_DELIVERY_DISCIPLINE_V0_3_POST_057_CRITIC_PROMPT_2026-09-18.md` | 其他仓库地址或项目名（隐私属性待确认）：44 |
| `docs/design/056_REAL_HOST_INTEGRATION_AUTHORIZATION_PLAN_2026-09-22.md` | 本机绝对路径：21、35–36、54、57、72、76、81、90、122 |
| `docs/design/056_REAL_HOST_INTEGRATION_CRITIC_PROMPT_2026-09-22.md` | 其他仓库地址或项目名（隐私属性待确认）：38；本机绝对路径：54–55、74–75 |
| `docs/design/056_REAL_HOST_INTEGRATION_REVIEW_PACKAGE_2026-09-22.md` | 本机绝对路径：22、34–35 |
| `docs/design/057_REPO_AGENTS_HYGIENE_IMPLEMENTATION_PLAN.md` | 其他仓库地址或项目名（隐私属性待确认）：69、116、128–133、138；CARE 名称或数据相关描述（候选）：142 |
| `docs/design/057_REPO_AGENTS_HYGIENE_INTEGRATION_RECOVERY_V1_PROPOSAL_2026-09-17.md` | 其他仓库地址或项目名（隐私属性待确认）：221、224、231、254、257、264、285、288、295、316、319、326、347、351、358、380、384、393 |
| `docs/design/057_REPO_AGENTS_HYGIENE_PROPOSAL_2026-09-17.md` | 其他仓库地址或项目名（隐私属性待确认）：37–41、45；CARE 名称或数据相关描述（候选）：54 |
| `docs/design/057_REPO_AGENTS_HYGIENE_V0_2_EXECUTION_CRITIC_PROMPT_2026-09-17.md` | 其他仓库地址或项目名（隐私属性待确认）：116 |
| `docs/design/057_REPO_AGENTS_HYGIENE_V2_PROPOSAL_2026-09-17.md` | 其他仓库地址或项目名（隐私属性待确认）：64–69；CARE 名称或数据相关描述（候选）：71 |
| `docs/design/058_ACTIVE_REPO_AGENTS_ADAPTATION_CRITIC_PROMPT_2026-09-18.md` | DII 项目标识或研究记录：38、81、101–102、117、218；其他仓库地址或项目名（隐私属性待确认）：41、44、55、103；CARE 名称或数据相关描述（候选）：104、141 |
| `docs/design/058_ACTIVE_REPO_AGENTS_ADAPTATION_PROPOSAL_2026-09-18.md` | DII 项目标识或研究记录：36、40、43–44、156、326、363、365；其他仓库地址或项目名（隐私属性待确认）：56、62、199、242、253；CARE 名称或数据相关描述（候选）：238、365 |
| `docs/design/058_ACTIVE_REPO_AGENTS_ADAPTATION_REVIEW_PACKAGE.md` | DII 项目标识或研究记录：21；CARE 名称或数据相关描述（候选）：22 |
| `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_2_CRITIC_REVIEW_2026-10-04.md` | DII 项目标识或研究记录：21、79、97、101 |
| `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_2_PLANNER_PROPOSAL_2026-10-04.md` | DII 项目标识或研究记录：87、410、417、429 |
| `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_ARCHITECTURE_V0_3_PLANNER_PROPOSAL_2026-10-04.md` | DII 项目标识或研究记录：90、452 |
| `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_EXECUTION_READY_CRITIC_REVIEW_V0_1_2026-10-04.md` | DII 项目标识或研究记录：34 |
| `docs/design/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_IMPLEMENTATION_PLAN_V0_1_2026-10-04.md` | DII 项目标识或研究记录：307、318 |
| `docs/design/AI_BRIDGE_KIT_0_7_1_AI_SKILLS_ADAPTATION_PROMPT_2026-09-06.md` | 其他仓库地址或项目名（隐私属性待确认）：5 |
| `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_CRITIC_PROMPT_V1_2026-09-22.md` | 其他仓库地址或项目名（隐私属性待确认）：75 |
| `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_CRITIC_PROMPT_V2_1_2026-09-23.md` | 其他仓库地址或项目名（隐私属性待确认）：72、116 |
| `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_CRITIC_PROMPT_V2_2026-09-23.md` | 其他仓库地址或项目名（隐私属性待确认）：87 |
| `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_CRITIC_REVIEW_PACKAGE_V2_1_2026-09-23.md` | 其他仓库地址或项目名（隐私属性待确认）：82 |
| `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_1_2026-09-23.md` | 其他仓库地址或项目名（隐私属性待确认）：123；本机绝对路径：199、207 |
| `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_GOAL_V2_2026-09-23.md` | 本机绝对路径：190、198 |
| `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_KICKOFF_DRAFT_V1_2026-09-22.md` | 其他仓库地址或项目名（隐私属性待确认）：65、76 |
| `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_KICKOFF_DRAFT_V2_1_2026-09-23.md` | 本机绝对路径：30；其他仓库地址或项目名（隐私属性待确认）：79、81、123 |
| `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_KICKOFF_DRAFT_V2_2026-09-23.md` | 其他仓库地址或项目名（隐私属性待确认）：79、114 |
| `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PLANNER_RESPONSE_V2_1_2026-09-23.md` | 其他仓库地址或项目名（隐私属性待确认）：35 |
| `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_1_2026-09-23.md` | 其他仓库地址或项目名（隐私属性待确认）：220、252 |
| `docs/design/AI_SKILLS_MAINTAINER_MACHINE_UPDATE_PROPOSAL_V2_2026-09-23.md` | 其他仓库地址或项目名（隐私属性待确认）：220 |
| `docs/design/PRESENTATIONS_CUMULATIVE_HUMAN_FEEDBACK_AND_TEACHING_DECK_AUTHORING_TODO_2026-10-06.md` | 其他仓库地址或项目名（隐私属性待确认）：5 |
| `docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_0_2026-09-29.md` | 本机绝对路径：64、73、292 |
| `docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_1_2026-09-29.md` | 本机绝对路径：66、78、399 |
| `docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_2_2026-09-29.md` | 本机绝对路径：348、360、457 |
| `docs/design/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_EXECUTION_PLAN_V1_3_2026-09-29.md` | 本机绝对路径：61–62、332、477、489、821；其他仓库地址或项目名（隐私属性待确认）：61–62 |
| `docs/design/PRESENTATIONS_STAT5060_REVIEWER_EXTRACTION_PLAN_2026-09-29.md` | 其他仓库地址或项目名（隐私属性待确认）：10 |
| `docs/design/PRESENTATIONS_STAT5060_RICH_V1_TEMPLATE_PARITY_AND_DELIVERY_QA_TODO_2026-10-04.md` | 其他仓库地址或项目名（隐私属性待确认）：12 |
| `docs/design/PRIVATE_ARTIFACT_DURABILITY_HARDENING_CRITIC_REVIEW_2026-09-15.md` | 本机绝对路径：64 |
| `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V3_CRITIC_PROMPT_2026-09-15.md` | 其他仓库地址或项目名（隐私属性待确认）：43–47 |
| `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V4_CRITIC_PROMPT_2026-09-15.md` | 其他仓库地址或项目名（隐私属性待确认）：34、39–42 |
| `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V5_CRITIC_PROMPT_2026-09-15.md` | 其他仓库地址或项目名（隐私属性待确认）：41–45 |
| `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V5_PROPOSAL_2026-09-15.md` | CARE 名称或数据相关描述（候选）：351 |
| `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_CUHK_DATE_REAL_FEEDBACK_2026-09-17.md` | 其他仓库地址或项目名（隐私属性待确认）：5、38 |
| `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_ADDENDUM_2026-09-17.md` | 其他仓库地址或项目名（隐私属性待确认）：147 |
| `docs/design/PRODUCT_DELIVERY_DISCIPLINE_V6_POST_PROBE_CRITIC_PROMPT_2026-09-17.md` | 其他仓库地址或项目名（隐私属性待确认）：15、32、118、157 |
| `docs/design/PROJECT_THREAD_HANDOFF_EXECUTION_CRITIC_PROMPT_V0_1_2026-09-21.md` | CARE 名称或数据相关描述（候选）：94、182、197；DII 项目标识或研究记录：151、178、182、197、225、265；其他仓库地址或项目名（隐私属性待确认）：151、193、265 |
| `docs/design/PROJECT_THREAD_HANDOFF_IMPLEMENTATION_PLAN_V0_1_2026-09-21.md` | DII 项目标识或研究记录：91、118、249、251、258、291、342、350、374、439；其他仓库地址或项目名（隐私属性待确认）：118、284、374、439；CARE 名称或数据相关描述（候选）：259–260、291、350 |
| `docs/design/PROJECT_THREAD_HANDOFF_IMPLEMENTATION_PLAN_V0_2_2026-09-21.md` | DII 项目标识或研究记录：106、133、345、347、354、387、442、450、474、531；其他仓库地址或项目名（隐私属性待确认）：133、380、474、531；CARE 名称或数据相关描述（候选）：355–356、387、450 |
| `docs/design/PROJECT_THREAD_HANDOFF_RECOVERY_EXECUTION_CRITIC_PROMPT_V0_1_2026-09-24.md` | DII 项目标识或研究记录：177；CARE 名称或数据相关描述（候选）：177 |
| `docs/design/PROJECT_THREAD_HANDOFF_RECOVERY_IMPLEMENTATION_PLAN_V0_1_2026-09-24.md` | 其他仓库地址或项目名（隐私属性待确认）：298、390；DII 项目标识或研究记录：299、349–350；CARE 名称或数据相关描述（候选）：299、349–350 |
| `docs/design/PROJECT_THREAD_HANDOFF_V2_CRITIC_PROMPT_2026-09-21.md` | 其他仓库地址或项目名（隐私属性待确认）：15；DII 项目标识或研究记录：62；CARE 名称或数据相关描述（候选）：62–63 |
| `docs/design/PROJECT_THREAD_HANDOFF_V2_PROPOSAL_2026-09-21.md` | 其他仓库地址或项目名（隐私属性待确认）：9、42、260、343；DII 项目标识或研究记录：42、113–114、231、237、241、243、268、342；CARE 名称或数据相关描述（候选）：113–114、237、241、244–245、268、342 |
| `docs/design/PROJECT_THREAD_HANDOFF_V3_CRITIC_PROMPT_2026-09-21.md` | 其他仓库地址或项目名（隐私属性待确认）：42、249；DII 项目标识或研究记录：47、216、228、254；CARE 名称或数据相关描述（候选）：47、229–230、254 |
| `docs/design/PROJECT_THREAD_HANDOFF_V3_PROPOSAL_2026-09-21.md` | 其他仓库地址或项目名（隐私属性待确认）：11、60、523、600、725；DII 项目标识或研究记录：41、60、343–344、346、476、489、493、528、600、611、724；CARE 名称或数据相关描述（候选）：41、343、345–346、489、494–495、528、706、724 |
| `docs/design/PROJECT_THREAD_HANDOFF_V4_RECOVERY_CRITIC_PROMPT_2026-09-24.md` | 其他仓库地址或项目名（隐私属性待确认）：294 |
| `docs/design/PROJECT_THREAD_HANDOFF_V4_RECOVERY_PROPOSAL_2026-09-24.md` | DII 项目标识或研究记录：188、282、411；CARE 名称或数据相关描述（候选）：188、232、411、552；其他仓库地址或项目名（隐私属性待确认）：443 |
| `docs/design/PROJECT_THREAD_HANDOFF_V5_RECOVERY_PROPOSAL_2026-09-24.md` | DII 项目标识或研究记录：420；CARE 名称或数据相关描述（候选）：420；其他仓库地址或项目名（隐私属性待确认）：471 |
| `docs/design/READER_FACING_COMMUNICATION_PLUGIN_BOUNDARIES.md` | CARE 名称或数据相关描述（候选）：196 |
| `docs/design/RESEARCH_WRITING_PRODUCTION_REDESIGN_PLAN_V0_1_2026-09-07.md` | DII 项目标识或研究记录：882；其他仓库地址或项目名（隐私属性待确认）：882 |
| `docs/design/RESEARCH_WRITING_PRODUCTION_REDESIGN_PLAN_V0_2_2026-09-07.md` | DII 项目标识或研究记录：807；其他仓库地址或项目名（隐私属性待确认）：807 |
| `docs/design/SHARED_CAPABILITY_PRODUCT_SHAPE_DECISIONS_2026-11-12.md` | 其他仓库地址或项目名（隐私属性待确认）：50 |
| `docs/design/clear-writing/NEXT_RELEASE_PROPOSAL.md` | DII 项目标识或研究记录：223 |
| `docs/design/frontend-design/FRONTEND_DESIGN_NATIVE_DESKTOP_ACCEPTANCE_V0_1_2026-10-04.md` | 其他仓库地址或项目名（隐私属性待确认）：7 |
| `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_PROMPT_V0_2_2026-09-28.md` | 其他仓库地址或项目名（隐私属性待确认）：66；本机绝对路径：96、121–122、193、354 |
| `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_PROMPT_V0_3_2026-09-28.md` | 本机绝对路径：76、324；其他仓库地址或项目名（隐私属性待确认）：101 |
| `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md` | 其他仓库地址或项目名（隐私属性待确认）：8；本机绝对路径：17、53、114 |
| `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_CRITIC_REVIEW_V0_3_2026-09-28.md` | 其他仓库地址或项目名（隐私属性待确认）：8、127；本机绝对路径：20、86、127 |
| `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_2_2026-09-28.md` | 本机绝对路径：10、46、51、699 |
| `docs/design/frontend-design/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_EXECUTION_PLAN_V0_3_2026-09-28.md` | 本机绝对路径：10、48、53、705 |
| `docs/design/pdf-artifact-delivery/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_ISOLATION_CRITIC_PROMPT_V0_1_2026-10-17.md` | 本机绝对路径：14；其他仓库地址或项目名（隐私属性待确认）：56 |
| `docs/design/pdf-artifact-delivery/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_ISOLATION_PROPOSAL_PLAN_V0_1_2026-10-17.md` | 本机绝对路径：12、83 |
| `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_CRITIC_PROMPT_V0_1_2026-09-28.md` | 其他仓库地址或项目名（隐私属性待确认）：82、86、92 |
| `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_CRITIC_PROMPT_V0_2_2026-09-28.md` | 其他仓库地址或项目名（隐私属性待确认）：95–97、240 |
| `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_PROMPT_V0_1_2026-09-28.md` | 其他仓库地址或项目名（隐私属性待确认）：62；本机绝对路径：103、106、127、131、482 |
| `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_PROMPT_V0_2_2026-09-28.md` | 其他仓库地址或项目名（隐私属性待确认）：97；本机绝对路径：236、305 |
| `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_REVIEW_V0_1_2026-09-28.md` | 本机绝对路径：22、40、46 |
| `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-28.md` | 本机绝对路径：22 |
| `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_PLAN_V0_1_2026-09-28.md` | 本机绝对路径：22、24、37；其他仓库地址或项目名（隐私属性待确认）：45 |
| `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_EXECUTION_PLAN_V0_2_2026-09-28.md` | 本机绝对路径：24、26、39；其他仓库地址或项目名（隐私属性待确认）：47 |
| `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_1_2026-09-28.md` | 其他仓库地址或项目名（隐私属性待确认）：114、143 |
| `docs/design/product-ui-copy/PRODUCT_UI_COPY_CROSS_PLUGIN_PROPOSAL_V0_2_2026-09-28.md` | 其他仓库地址或项目名（隐私属性待确认）：128、157、1017 |
| `docs/design/product-ui-copy/evidence/PROJECT_ATLAS_COPY_REVIEW_HISTORY_2026-11-03.md` | 其他仓库地址或项目名（隐私属性待确认）：237–242、753、843；DII 项目标识或研究记录：327–344、559、624、626、629、631–632、761 |
| `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_3_AGENTS_ARCHITECTURE_CRITIC_PROMPT_V0_1_2026-10-20.md` | 其他仓库地址或项目名（隐私属性待确认）：58、68 |
| `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_3_AGENTS_ARCHITECTURE_CRITIC_PROMPT_V0_2_2026-10-22.md` | 其他仓库地址或项目名（隐私属性待确认）：24、47、49、51 |
| `docs/design/project-instructions-editor/PROJECT_INSTRUCTIONS_EDITOR_0_3_AGENTS_ARCHITECTURE_PROPOSAL_V0_2_2026-10-22.md` | 其他仓库地址或项目名（隐私属性待确认）：54–57、219–220、223–226 |
| `docs/design/reasoned-decision/REASONED_DECISION_PRIOR_ART_AND_HUMAN_BASELINE_2026-11-05.md` | 其他仓库地址或项目名（隐私属性待确认）：22–23 |
| `docs/design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md` | 其他仓库地址或项目名（隐私属性待确认）：643–644 |
| `docs/design/reasoned-decision/evidence/EDGE_WINDOWS_DECISION_FAILURE_2026-11-05.md` | 其他仓库地址或项目名（隐私属性待确认）：6 |
| `docs/design/reasoned-decision/evidence/ITERM2_SSH_MOUSE_REPORTING_DECISION_FAILURE_2026-11-06.md` | 其他仓库地址或项目名（隐私属性待确认）：6 |
| `docs/design/reasoned-decision/evidence/TAILSCALE_MACOS_CLONED_IDENTITY_DECISION_FAILURE_2026-11-06.md` | 其他仓库地址或项目名（隐私属性待确认）：6 |
| `docs/design/reasoned-decision/evidence/UU_REMOTE_KARABINER_DECISION_FAILURE_2026-11-07.md` | 其他仓库地址或项目名（隐私属性待确认）：28 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_G4_RESOURCE_AMENDMENT_CRITIC_PROMPT_V3_1_2026-10-20.md` | 实验室标识：21、29、38、40；DII 项目标识或研究记录：44；CARE 名称或数据相关描述（候选）：44 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_G4_RESOURCE_AMENDMENT_V3_1_2026-10-20.md` | 实验室标识：14、23、29、37、41、56；DII 项目标识或研究记录：93；CARE 名称或数据相关描述（候选）：93 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_EXECUTION_CRITIC_PROMPT_V3_2026-10-19.md` | DII 项目标识或研究记录：5、68、197；CARE 名称或数据相关描述（候选）：5、68、197；其他仓库地址或项目名（隐私属性待确认）：44；实验室标识：134、180、235；本机绝对路径：161、163、176、178 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_EXECUTION_CRITIC_PROMPT_V3_R1_2026-10-19.md` | 其他仓库地址或项目名（隐私属性待确认）：51；本机绝对路径：75、87、96、153、155；DII 项目标识或研究记录：124、191；CARE 名称或数据相关描述（候选）：124、191；实验室标识：125、176 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_EXECUTION_PLAN_V3_2026-10-19.md` | 本机绝对路径：35、37、231–232；实验室标识：258、356；DII 项目标识或研究记录：374；CARE 名称或数据相关描述（候选）：375 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_KICKOFF_DRAFT_V3_2026-10-19.md` | 本机绝对路径：28、32、105、111、113；DII 项目标识或研究记录：76；CARE 名称或数据相关描述（候选）：76；实验室标识：124 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_CANCEL_PORTABLE_RUNTIME_PROPOSAL_V3_2026-10-19.md` | 实验室标识：23、163；DII 项目标识或研究记录：44、150、152、223；CARE 名称或数据相关描述（候选）：44、150、152、223；其他仓库地址或项目名（隐私属性待确认）：150 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_EXECUTION_PLAN_V2_1_2026-10-18.md` | 实验室标识：64、836、1001；本机绝对路径：104、115、119、128、139、143、152、163、167、238、941、944、947；DII 项目标识或研究记录：123、128、139、143、250、636、762、861、926、943–944、991、1003、1014、1043、1067、1105；CARE 名称或数据相关描述（候选）：147、152、163、167、248、736、762、772、861、864、918、926、946–947、991、1003、1014、1043、1067、1105、1125 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_EXECUTION_PLAN_V2_2026-10-18.md` | 实验室标识：23、407、518；本机绝对路径：57、63、71、77、85、91；DII 项目标识或研究记录：65、71、77、130、318、342、356、360、429、473、483、485–486、514、519、558、583；CARE 名称或数据相关描述（候选）：79、85、91、130、318、342、356、371、429、433、473、483、485–486、514、519、558、583 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_KICKOFF_DRAFT_V2_1_2026-10-18.md` | CARE 名称或数据相关描述（候选）：15、77、80、89、92、269、271、273、349、394–395、469；本机绝对路径：46、55、58、63、72、75、80、89、92、173、389、392、395；DII 项目标识或研究记录：60、63、72、75、269、350、391–392、469 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_KICKOFF_DRAFT_V2_2026-10-18.md` | 本机绝对路径：28、30、34、36、40、42；DII 项目标识或研究记录：32、34、36、52、81、101、152、193；CARE 名称或数据相关描述（候选）：38、40、42、52、81、108、152、193；实验室标识：199 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_1_2026-10-18.md` | DII 项目标识或研究记录：341、343、411、512；CARE 名称或数据相关描述（候选）：341、343、345、411、512 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_CHAT_CONFIRMATION_PROPOSAL_V2_2026-10-18.md` | 其他仓库地址或项目名（隐私属性待确认）：8；实验室标识：42、48、54、337、437、473；DII 项目标识或研究记录：362、364、458、542；CARE 名称或数据相关描述（候选）：362、364、392、458、542 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_FRESH_CONFIRMATION_EXECUTION_PLAN_V1_2026-10-17.md` | 实验室标识：19、162、283–284、345、403；DII 项目标识或研究记录：42、55、57、59、182、192、194、299、332、353、375、394；CARE 名称或数据相关描述（候选）：43、61、63、65、182、192、206、234、299、332、353、375、394；本机绝对路径：51、53、57、59、63、65、247–248 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_FRESH_CONFIRMATION_KICKOFF_DRAFT_V1_2026-10-17.md` | 本机绝对路径：24、26、30、32、36、38、68；DII 项目标识或研究记录：28、30、32、47、73；CARE 名称或数据相关描述（候选）：34、36、38、48、73；实验室标识：58 |
| `docs/design/slurm-workflows/SLURM_PROTECTED_PARTITION_FRESH_CONFIRMATION_PROPOSAL_V1_2026-10-17.md` | DII 项目标识或研究记录：7、13、22、194、257、259、291、299、303、308、339、400、428；CARE 名称或数据相关描述（候选）：7、14、22、133、151、153、180、194、251、257、260、291、299、304、309、314、318、320、337、339、364、400、428；实验室标识：28、94、379 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_EXECUTION_PLAN_V0_3_2026-10-13.md` | 本机绝对路径：8、15、23、27；DII 项目标识或研究记录：9、57、102、104、116、132；CARE 名称或数据相关描述（候选）：9、57、102、104、116、132；实验室标识：83、120 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_KICKOFF_DRAFT_V0_3_2026-10-13.md` | 本机绝对路径：10–11；DII 项目标识或研究记录：29、34；CARE 名称或数据相关描述（候选）：29、34；实验室标识：34 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_CANCEL_PROTECTION_PROPOSAL_V0_3_2026-10-13.md` | DII 项目标识或研究记录：19、25、92、110、152；CARE 名称或数据相关描述（候选）：19、78、92、110；实验室标识：50、52；其他仓库地址或项目名（隐私属性待确认）：152–155 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_PRODUCTION_CLOSURE_KICKOFF_DRAFT_V0_1_2026-10-16.md` | DII 项目标识或研究记录：17、25–26、28、39、49、66、98、114、131、139、150–151；CARE 名称或数据相关描述（候选）：18、29–30、32、40、50、71、98、114、131、139、150–151；本机绝对路径：22、24、26、28、30、32、52；实验室标识：96、121、129、157 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_PRODUCTION_CLOSURE_PLAN_V0_1_2026-10-16.md` | DII 项目标识或研究记录：14、22、54、71、73、77、96、142、144、193、199、210、214、224、238、241–242、252、264；CARE 名称或数据相关描述（候选）：14、22、54、79、81、85、97、142、156、158、193、199、210、214、224、238、241–242、252、264；实验室标识：18、116、123、140、182、254；本机绝对路径：66–67、73、77、81、85、95 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_PROMPT_V0_3_2026-09-24.md` | 其他仓库地址或项目名（隐私属性待确认）：107 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_PROMPT_V0_5_2026-09-24.md` | 实验室标识：352 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_1_2026-09-24.md` | 实验室标识：55 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_4_2026-09-24.md` | 实验室标识：291 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_CRITIC_REVIEW_V0_5_2026-09-24.md` | 实验室标识：215 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_CRITIC_REVIEW_V0_2_2026-09-24.md` | 其他仓库地址或项目名（隐私属性待确认）：285 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PLAN_V0_2_2026-09-24.md` | CARE 名称或数据相关描述（候选）：119 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_EXECUTION_PLAN_V0_6_2026-09-24.md` | 其他仓库地址或项目名（隐私属性待确认）：222；CARE 名称或数据相关描述（候选）：224 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_1_2026-09-24.md` | 实验室标识：41、43、102–103、209、240、246、250、354、383、519；CARE 名称或数据相关描述（候选）：505 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_2_2026-09-24.md` | 实验室标识：119、121、258、300；CARE 名称或数据相关描述（候选）：488 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_3_2026-09-24.md` | 其他仓库地址或项目名（隐私属性待确认）：819 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_5_2026-09-24.md` | 实验室标识：644 |
| `docs/design/slurm-workflows/SLURM_WORKFLOWS_ROUTING_REFACTOR_PROPOSAL_V0_6_2026-09-24.md` | 实验室标识：291 |
| `docs/design/warm-response/TODO.md` | 其他仓库地址或项目名（隐私属性待确认）：5 |
| `docs/design/warm-response/WARM_RESPONSE_PLUGIN_SEED_2026-10-30.md` | 其他仓库地址或项目名（隐私属性待确认）：257 |
| `docs/design/warm-response/evidence/BWG_GFW_thread_full_history_2026-10-29_to_2026-11-01.md` | 其他仓库地址或项目名（隐私属性待确认）：223、227、818、832、838、895、907、971、1653、1659、1678 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_CRITIC_PROMPT_V0_1_2026-09-30.md` | 其他仓库地址或项目名（隐私属性待确认）：49 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_CRITIC_PROMPT_V0_2_2026-09-30.md` | 其他仓库地址或项目名（隐私属性待确认）：53 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_1_2026-10-01.md` | 本机绝对路径：55、58、183；其他仓库地址或项目名（隐私属性待确认）：66 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_2_2026-10-01.md` | 本机绝对路径：114、120、133 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_3_2026-10-01.md` | 本机绝对路径：33、35、434 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_PLAN_V0_4_2026-10-01.md` | 本机绝对路径：40、336、347、349 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_READY_CRITIC_PROMPT_V0_1_2026-10-01.md` | 其他仓库地址或项目名（隐私属性待确认）：41；本机绝对路径：81、84 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_READY_CRITIC_PROMPT_V0_2_2026-10-01.md` | 其他仓库地址或项目名（隐私属性待确认）：47；本机绝对路径：80 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_READY_CRITIC_PROMPT_V0_3_2026-10-01.md` | 本机绝对路径：102、106 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_EXECUTION_READY_CRITIC_PROMPT_V0_4_2026-10-01.md` | 本机绝对路径：75、128、130 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_1_2026-10-01.md` | 本机绝对路径：11、13 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_2_2026-10-01.md` | 本机绝对路径：11、18 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_3_2026-10-01.md` | 本机绝对路径：12 |
| `docs/design/workflow-core/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_KICKOFF_V0_4_2026-10-01.md` | 本机绝对路径：11、24 |
| `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_EXECUTION_CRITIC_PROMPT_V0_1_2026-10-02.md` | 本机绝对路径：146、192、275–276 |
| `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_IMPLEMENTATION_PLAN_V0_1_2026-10-02.md` | 本机绝对路径：60、64、81、87、313、367 |
| `docs/design/workflow-governance/AI_SKILLS_MAINTENANCE_BOARD_V1_PROPOSAL_2026-09-22.md` | DII 项目标识或研究记录：133 |
| `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_CRITIC_REVIEW_2026-09-20.md` | 其他仓库地址或项目名（隐私属性待确认）：303 |
| `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V1_PROPOSAL_2026-09-20.md` | 其他仓库地址或项目名（隐私属性待确认）：7 |
| `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_EXECUTION_CRITIC_PROMPT_2026-09-20.md` | 其他仓库地址或项目名（隐私属性待确认）：90 |
| `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_EXECUTION_CRITIC_REVIEW_2026-09-20.md` | 其他仓库地址或项目名（隐私属性待确认）：109 |
| `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_EXECUTION_CRITIC_REVIEW_R2_2026-09-20.md` | 其他仓库地址或项目名（隐私属性待确认）：36 |
| `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_IMPLEMENTATION_PLAN_2026-09-20.md` | 其他仓库地址或项目名（隐私属性待确认）：14、124 |
| `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_PLAN_R2_2026-09-21.md` | 其他仓库地址或项目名（隐私属性待确认）：354 |
| `docs/design/workflow-governance/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_PROPOSAL_2026-09-20.md` | 其他仓库地址或项目名（隐私属性待确认）：13、111 |
| `docs/domains/medical-knowledge.md` | CARE 名称或数据相关描述（候选）：29、32 |
| `docs/domains/medicine-clinical.md` | CARE 名称或数据相关描述（候选）：29、32 |
| `docs/goals/056_FINAL_INTEGRATION_RELEASE_CLOSURE_GOAL_V0_1.md` | 本机绝对路径：31–32 |
| `docs/goals/056_FINAL_INTEGRATION_RELEASE_CLOSURE_GOAL_V0_2.md` | 本机绝对路径：48–49 |
| `docs/goals/056_PRODUCT_DELIVERY_DISCIPLINE_GOAL.md` | CARE 名称或数据相关描述（候选）：154 |
| `docs/goals/056_REAL_HOST_INTEGRATION_GOAL.md` | 本机绝对路径：23、26–27、53 |
| `docs/goals/057_REPO_AGENTS_HYGIENE_GOAL.md` | CARE 名称或数据相关描述（候选）：265 |
| `docs/goals/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_GOAL_V0_1.md` | DII 项目标识或研究记录：120 |
| `docs/goals/AI_SKILLS_MAINTENANCE_BOARD_FINAL_CLOSURE_GOAL_V0_1.md` | 本机绝对路径：54、150 |
| `docs/goals/DOCUMENTS_MEDIA_PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_RECOVERY_GOAL_V0_1.md` | 本机绝对路径：55 |
| `docs/goals/FRONTEND_DESIGN_NATIVE_DESKTOP_ACCEPTANCE_GOAL_V0_1.md` | 其他仓库地址或项目名（隐私属性待确认）：60 |
| `docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_2.md` | 本机绝对路径：14、21、47、378 |
| `docs/goals/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_GOAL_V0_3.md` | 本机绝对路径：14、21、46、377 |
| `docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_0.md` | 本机绝对路径：26、38、88、315 |
| `docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_1.md` | 本机绝对路径：41、53、156、440 |
| `docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_2.md` | 本机绝对路径：159、171 |
| `docs/goals/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_GOAL_V1_3.md` | 本机绝对路径：132 |
| `docs/goals/PRODUCT_UI_COPY_CROSS_PLUGIN_GOAL_V0_1.md` | 本机绝对路径：14、16、21、365 |
| `docs/goals/PRODUCT_UI_COPY_CROSS_PLUGIN_GOAL_V0_2.md` | 本机绝对路径：15、17、22、382 |
| `docs/goals/PROJECT_THREAD_HANDOFF_GOAL_V0_1.md` | DII 项目标识或研究记录：23、74、97、99、104、125、158、161、194；CARE 名称或数据相关描述（候选）：23、74、105–106、125；其他仓库地址或项目名（隐私属性待确认）：124、194 |
| `docs/goals/PROJECT_THREAD_HANDOFF_GOAL_V0_2.md` | DII 项目标识或研究记录：26、120、175、177、182、203、237、240、275；CARE 名称或数据相关描述（候选）：26、120、183–184、203；其他仓库地址或项目名（隐私属性待确认）：202、275 |
| `docs/goals/PROJECT_THREAD_HANDOFF_RECOVERY_GOAL_V0_1.md` | DII 项目标识或研究记录：138；CARE 名称或数据相关描述（候选）：138 |
| `docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_1_2026-10-01.md` | 本机绝对路径：21、24 |
| `docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_2_2026-10-01.md` | 本机绝对路径：25 |
| `docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_3_2026-10-01.md` | 本机绝对路径：28–29 |
| `docs/goals/WORKFLOW_CORE_0_5_NORMAL_ENTRY_RELIABILITY_GOAL_V0_4_2026-10-01.md` | 本机绝对路径：27、144 |
| `docs/goals/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_GOAL.md` | 其他仓库地址或项目名（隐私属性待确认）：66 |
| `docs/goals/hpc--slurm-cancel-human-confirmation-goal-draft-v0_3.md` | 本机绝对路径：8、17；实验室标识：13、40；DII 项目标识或研究记录：32、42、48、54；CARE 名称或数据相关描述（候选）：32、42、48、54 |
| `docs/goals/hpc--slurm-cancel-production-closure-goal-v0_1.md` | 实验室标识：20、149、160、221；DII 项目标识或研究记录：26、40–42、44、76、133、141、162、170、192–193、205、215；CARE 名称或数据相关描述（候选）：26、46、48、50、85、133、141、162、170、192–193、205、215；本机绝对路径：37–38、42、44、48、50；其他仓库地址或项目名（隐私属性待确认）：41、47 |
| `docs/goals/hpc--slurm-cancel-production-closure-goal-v3.md` | 实验室标识：34、93、111；DII 项目标识或研究记录：51；CARE 名称或数据相关描述（候选）：51；本机绝对路径：72、74、105、108 |
| `docs/goals/hpc--slurm-protected-partition-chat-confirmation-goal-v2.md` | 实验室标识：28、403；本机绝对路径：62、64、69、71、76、78；DII 项目标识或研究记录：67、69、71、96、163、254、295、299、388、404、423；CARE 名称或数据相关描述（候选）：74、76、78、96、163、254、295、309、368、388、404、423 |
| `docs/goals/hpc--slurm-protected-partition-chat-confirmation-goal-v2_1.md` | 实验室标识：33、538、679；本机绝对路径：77、86、89、94、103、106、111、120、123；DII 项目标识或研究记录：91、94、103、106、156、447、449、567、618、651、672、680、733；CARE 名称或数据相关描述（候选）：108、111、120、123、156、466、468、497、566、618、651、672、680、733 |
| `docs/goals/hpc--slurm-protected-partition-fresh-confirmation-goal-v1.md` | 实验室标识：23、219–220、271、294、355；本机绝对路径：50、52、56、58、62、64、199–200；DII 项目标识或研究记录：54、56、58、140、145、235、275、298、324；CARE 名称或数据相关描述（候选）：60、62、64、148、235、275、298、324 |
| `docs/operations/prompts/056_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_1.md` | 其他仓库地址或项目名（隐私属性待确认）：27；本机绝对路径：33–34、39、51、53、151、170、175–176 |
| `docs/operations/prompts/056_FINAL_INTEGRATION_RELEASE_KICKOFF_V0_2.md` | 其他仓库地址或项目名（隐私属性待确认）：29；本机绝对路径：35–36、41、53、55、153、172、177–178 |
| `docs/operations/prompts/056_PRODUCT_DELIVERY_DISCIPLINE_KICKOFF.md` | CARE 名称或数据相关描述（候选）：211 |
| `docs/operations/prompts/056_REAL_HOST_INTEGRATION_KICKOFF.md` | 本机绝对路径：15、21、28、31–32、57、86、153 |
| `docs/operations/prompts/057_REPO_AGENTS_HYGIENE_KICKOFF.md` | 其他仓库地址或项目名（隐私属性待确认）：19–25；CARE 名称或数据相关描述（候选）：26 |
| `docs/operations/prompts/059_RESEARCH_AUTHORING_FORMAL_PRODUCTION_KICKOFF_V0_1.md` | DII 项目标识或研究记录：54 |
| `docs/operations/prompts/AI_SKILLS_MAINTENANCE_BOARD_FINAL_REMAINING_CONSUMER_CUHK_WSL_V0_1.md` | 本机绝对路径：16、22、34、77、140 |
| `docs/operations/prompts/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_KICKOFF_V0_2.md` | 本机绝对路径：28、75 |
| `docs/operations/prompts/FRONTEND_DESIGN_PRODUCTION_CONSOLIDATION_KICKOFF_V0_3.md` | 本机绝对路径：28、79、161 |
| `docs/operations/prompts/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_RECOVERY_KICKOFF_V0_1.md` | 本机绝对路径：7 |
| `docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_0.md` | 本机绝对路径：32、41、74、189 |
| `docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_1.md` | 本机绝对路径：51、63、219、373 |
| `docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_2.md` | 本机绝对路径：70、82、231 |
| `docs/operations/prompts/PRESENTATIONS_STAGE1_FRONT_DOOR_TWO_TEMPLATE_KICKOFF_V1_3.md` | 本机绝对路径：53、65、287、297、405 |
| `docs/operations/prompts/PRODUCT_UI_COPY_CROSS_PLUGIN_KICKOFF_V0_1.md` | 本机绝对路径：39、42；其他仓库地址或项目名（隐私属性待确认）：200–202 |
| `docs/operations/prompts/PRODUCT_UI_COPY_CROSS_PLUGIN_KICKOFF_V0_2.md` | 本机绝对路径：45、48；其他仓库地址或项目名（隐私属性待确认）：206–208 |
| `docs/operations/prompts/PRODUCT_UI_COPY_CROSS_PLUGIN_PLANNER_2026-09-28.md` | 其他仓库地址或项目名（隐私属性待确认）：50、150、472、637–638 |
| `docs/operations/prompts/PROJECT_THREAD_HANDOFF_KICKOFF_V0_1.md` | DII 项目标识或研究记录：81、92、106、187、190；其他仓库地址或项目名（隐私属性待确认）：81、110；CARE 名称或数据相关描述（候选）：92；本机绝对路径：106 |
| `docs/operations/prompts/PROJECT_THREAD_HANDOFF_KICKOFF_V0_2.md` | DII 项目标识或研究记录：88、167、182、269、272；其他仓库地址或项目名（隐私属性待确认）：88、186；CARE 名称或数据相关描述（候选）：167；本机绝对路径：182 |
| `docs/operations/prompts/SLURM_WORKFLOWS_ROUTING_REFACTOR_KICKOFF_V0_2.md` | CARE 名称或数据相关描述（候选）：118 |
| `docs/operations/prompts/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_INTEGRATION_KICKOFF_R2.md` | 其他仓库地址或项目名（隐私属性待确认）：126 |
| `docs/operations/prompts/WORKFLOW_IDENTITY_AND_GATE_LIFECYCLE_V2_1_KICKOFF.md` | 其他仓库地址或项目名（隐私属性待确认）：28、123 |
| `docs/plugin-changelogs/presentations.md` | 本机绝对路径：21；其他仓库地址或项目名（隐私属性待确认）：21 |
| `docs/plugin-todos/README.md` | CARE 名称或数据相关描述（候选）：5 |
| `docs/plugin-todos/medical-imaging.md` | 其他仓库地址或项目名（隐私属性待确认）：24、35、37、47 |
| `docs/plugin-todos/presentations.md` | CARE 名称或数据相关描述（候选）：5；其他仓库地址或项目名（隐私属性待确认）：195、242、269、425、438、658、741、743 |
| `docs/plugin-todos/reasoned-decision.md` | 其他仓库地址或项目名（隐私属性待确认）：57 |
| `docs/plugin-todos/research-writing-student-audience-and-pre-render-approval.md` | 其他仓库地址或项目名（隐私属性待确认）：4、8、10 |
| `docs/plugin-todos/research-writing.md` | DII 项目标识或研究记录：164–165、183–184、190、192–193、200、206–207、222、227、230–231、234、236、238–239、244–245、265、294–295、309、324–325、341–342、358–359、378–379；其他仓库地址或项目名（隐私属性待确认）：184、193、227、239、397、438、536；CARE 名称或数据相关描述（候选）：187、199–200、230；MoSAiC 名称（候选）：200、230、294–295；本机绝对路径：459、503 |
| `docs/plugin-todos/web-development.md` | 其他仓库地址或项目名（隐私属性待确认）：21、237、258、294、330、364、382；DII 项目标识或研究记录：385 |
| `docs/plugin-todos/workflow-core.md` | 本机绝对路径：12；其他仓库地址或项目名（隐私属性待确认）：38、57、243、292 |
| `docs/plugin-todos/writing-style.md` | DII 项目标识或研究记录：284、286、288、294–295、329、388、390、397、399、401、403、407、409、414、424、426、430、439、442、444、462、541–542、544、558、611；CARE 名称或数据相关描述（候选）：407、414、439、481、631；MoSAiC 名称（候选）：431、435、439、453、541、546、549、559；其他仓库地址或项目名（隐私属性待确认）：664、683 |
| `docs/provenance/INTEGRATION_HISTORY.md` | 其他仓库地址或项目名（隐私属性待确认）：7；CARE 名称或数据相关描述（候选）：61、64；MoSAiC 名称（候选）：61；本机绝对路径：61 |
| `docs/provenance/LOCAL_USER_REPO_WRITING_LESSONS_2026_07_28.md` | CARE 名称或数据相关描述（候选）：4、9、14、23；MoSAiC 名称（候选）：4、10、14、23；本机绝对路径：4、9–10 |
| `docs/provenance/RESEARCH_GROUP_MEETING_WRITING_REVIEW_2026_08_29.md` | DII 项目标识或研究记录：7；CARE 名称或数据相关描述（候选）：95、111、131 |
| `docs/provenance/RESEARCH_PRESENTATION_REFERENCE_LIBRARY_2026_08_17.md` | CARE 名称或数据相关描述（候选）：47 |
| `docs/provenance/RESEARCH_PRESENTATION_REVIEWED_HANDOFF_REVIEW_2026_08_17.md` | CARE 名称或数据相关描述（候选）：42 |
| `docs/skill-todos/artifact-content-design.md` | DII 项目标识或研究记录：16–17、21、45、254、361；其他仓库地址或项目名（隐私属性待确认）：17、36、41 |
| `docs/skill-todos/course-assessment-authoring-student-audience-gate.md` | 其他仓库地址或项目名（隐私属性待确认）：4、153 |
| `docs/skill-todos/course-assessment-authoring.md` | 其他仓库地址或项目名（隐私属性待确认）：13、15、35 |
| `docs/skill-todos/project-instructions-editor.md` | 其他仓库地址或项目名（隐私属性待确认）：87、95、142、813、826；CARE 名称或数据相关描述（候选）：95 |
| `docs/skill-todos/render-chinese-math-pdf.md` | 本机绝对路径：74 |
| `docs/skill-todos/slurm-workflows.md` | DII 项目标识或研究记录：20–21、36、38；CARE 名称或数据相关描述（候选）：20–21；实验室标识：20 |
| `docs/skill_provenance_audit.json` | 其他仓库地址或项目名（隐私属性待确认）：39、267、749 |
| `docs/workflows/CHATGPT_WEB_COLLABORATION_REGRESSIONS_2026-10-17.md` | DII 项目标识或研究记录：12 |
| `docs/workflows/CHATGPT_WEB_CRITIC_GOOD_REVIEW_EXAMPLES_2026-10-20.md` | CARE 名称或数据相关描述（候选）：24 |
| `plugins/codex/plugins/ai-skills-core/skills/bridge/SKILL.md` | 其他仓库地址或项目名（隐私属性待确认）：66、82 |
| `plugins/codex/plugins/ai-skills-core/skills/bridge/references/bridge-release-channel.md` | 其他仓库地址或项目名（隐私属性待确认）：35 |
| `plugins/codex/plugins/ai-skills-core/skills/orchestrator/references/formal-release-and-update-impact.md` | 其他仓库地址或项目名（隐私属性待确认）：3 |
| `plugins/codex/plugins/ai-skills-core/skills/proj/SKILL.md` | 本机绝对路径：41；其他仓库地址或项目名（隐私属性待确认）：66 |
| `plugins/codex/plugins/medical-imaging/skills/med/_src/classic/source.md` | 其他仓库地址或项目名（隐私属性待确认）：18 |
| `plugins/codex/plugins/medical-imaging/skills/med/_src/cmr/evals/trigger_queries.json` | 其他仓库地址或项目名（隐私属性待确认）：12–13、21 |
| `plugins/codex/plugins/medical-imaging/skills/med/_src/cmr/source.md` | 其他仓库地址或项目名（隐私属性待确认）：25 |
| `plugins/codex/plugins/presentations/shared/compatibility/openai-latex.md` | 本机绝对路径：17；其他仓库地址或项目名（隐私属性待确认）：17 |
| `plugins/codex/plugins/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py` | 本机绝对路径：31；其他仓库地址或项目名（隐私属性待确认）：31 |
| `plugins/codex/plugins/presentations/skills/research/SKILL.md` | 本机绝对路径：69；其他仓库地址或项目名（隐私属性待确认）：69 |
| `plugins/codex/plugins/research-writing/shared/student-assessment-end-to-end-pre-execution-runbook.md` | 本机绝对路径：1150 |
| `plugins/codex/plugins/research-writing/skills/litcite/_src/lit/source.md` | CARE 名称或数据相关描述（候选）：77 |
| `plugins/codex/plugins/research-writing/skills/paper/_src/write/source.md` | CARE 名称或数据相关描述（候选）：166 |
| `plugins/codex/plugins/scientific-visualization/skills/figures/_src/mpl/source.md` | MoSAiC 名称（候选）：124 |
| `plugins/codex/plugins/statistical-modeling/skills/bayes/_src/diag/references/reference.md` | 本机绝对路径：20 |
| `plugins/codex/plugins/statistical-modeling/skills/bayes/_src/diag/source.md` | 其他仓库地址或项目名（隐私属性待确认）：18 |
| `plugins/codex/plugins/statistical-modeling/skills/viz/_src/mpl/source.md` | MoSAiC 名称（候选）：124 |
| `profiles/README.md` | 其他仓库地址或项目名（隐私属性待确认）：23、39、43 |
| `profiles/codex-cardiacnexus.json` | 其他仓库地址或项目名（隐私属性待确认）：2–3 |
| `profiles/medical-imaging-project.json` | 其他仓库地址或项目名（隐私属性待确认）：3 |
| `registry.json` | CARE 名称或数据相关描述（候选）：1968、2082 |
| `results/004_current_library_acceptance/RESULT.md` | 本机绝对路径：78–80 |
| `results/011_round_handoff/RESULT.md` | CARE 名称或数据相关描述（候选）：27 |
| `results/013_presentation_todo_consolidation/RESULT.md` | 本机绝对路径：33；其他仓库地址或项目名（隐私属性待确认）：33 |
| `results/014_presentation_phase_a_recovery/RESULT.md` | 本机绝对路径：42；其他仓库地址或项目名（隐私属性待确认）：42 |
| `results/015_presentation_terra_blocker_repair/RESULT.md` | 本机绝对路径：60；其他仓库地址或项目名（隐私属性待确认）：60 |
| `results/016_statistical_method_group_meeting_benchmark/RESULT.md` | 本机绝对路径：94；其他仓库地址或项目名（隐私属性待确认）：94 |
| `results/017_medical_imaging_group_meeting_benchmark/RESULT.md` | 本机绝对路径：91；其他仓库地址或项目名（隐私属性待确认）：91 |
| `results/018_presentation_external_method_audit/RESULT.md` | 本机绝对路径：75；其他仓库地址或项目名（隐私属性待确认）：75 |
| `results/019_research_presentation_exemplar_composition_representation/RESULT.md` | 本机绝对路径：54；其他仓库地址或项目名（隐私属性待确认）：54 |
| `results/020_research_presentation_reference_calibrated_candidate_search/RESULT.md` | 本机绝对路径：109；其他仓库地址或项目名（隐私属性待确认）：109 |
| `results/021_research_presentation_comparative_reference_calibrated_visual_review/RESULT.md` | 本机绝对路径：92；其他仓库地址或项目名（隐私属性待确认）：92 |
| `results/022_research_presentation_candidate_visual_finish_repair/RESULT.md` | 本机绝对路径：138；其他仓库地址或项目名（隐私属性待确认）：138 |
| `results/023_research_presentation_deck_design_system_integration/RESULT.md` | 本机绝对路径：111；其他仓库地址或项目名（隐私属性待确认）：111 |
| `results/023_research_presentation_deck_design_system_integration/generated/medical_design_system_fixture/RENDER_STATUS.json` | 本机绝对路径：3 |
| `results/023_research_presentation_deck_design_system_integration/generated/medical_design_system_fixture/SOURCE_GENERATED_IDENTITY_MANIFEST.json` | 本机绝对路径：690 |
| `results/023_research_presentation_deck_design_system_integration/generated/profile_mutation_regression/statistical_design_system_fixture_mutated_profile/RENDER_STATUS.json` | 本机绝对路径：3 |
| `results/023_research_presentation_deck_design_system_integration/generated/profile_mutation_regression/statistical_design_system_fixture_mutated_profile/SOURCE_GENERATED_IDENTITY_MANIFEST.json` | 本机绝对路径：522 |
| `results/023_research_presentation_deck_design_system_integration/generated/statistical_design_system_fixture/RENDER_STATUS.json` | 本机绝对路径：3 |
| `results/023_research_presentation_deck_design_system_integration/generated/statistical_design_system_fixture/SOURCE_GENERATED_IDENTITY_MANIFEST.json` | 本机绝对路径：522 |
| `results/024_research_presentation_product_contract_reset/RESULT.md` | 本机绝对路径：42；其他仓库地址或项目名（隐私属性待确认）：42 |
| `results/025_research_presentation_gold_scientific_composition_library/RESULT.md` | 本机绝对路径：117、298；其他仓库地址或项目名（隐私属性待确认）：117、298 |
| `results/026_research_presentation_discussion_next_experiment_gold_recovery/RESULT.md` | 本机绝对路径：68 |
| `results/027_research_presentation_executable_cuhk_scientific_layout_system/RESULT.md` | 本机绝对路径：60；其他仓库地址或项目名（隐私属性待确认）：60 |
| `results/028_research_presentation_stage3_visual_review_dispatch_recovery/RESULT.md` | 本机绝对路径：100；其他仓库地址或项目名（隐私属性待确认）：100 |
| `results/029_reviewed_handoff_visual_contract_adaptation/RESULT.md` | 本机绝对路径：50 |
| `results/030_stage3_visual_recovery/RESULT.md` | 本机绝对路径：72 |
| `results/031_research_presentation_one_call_production_entry/RESULT.md` | 本机绝对路径：106 |
| `results/031_research_presentation_one_call_production_entry/generated/BUILD_MANIFEST.json` | 本机绝对路径：28、31、34；其他仓库地址或项目名（隐私属性待确认）：28、34 |
| `results/031_research_presentation_one_call_production_entry/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、63、65、69、71、74；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、63、65、69、71、74 |
| `results/031_research_presentation_one_call_production_entry/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/031_research_presentation_one_call_production_entry/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214 |
| `results/031_research_presentation_one_call_production_entry/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/031_research_presentation_one_call_production_entry/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/032_research_presentation_storyline_coherence_recovery/RESULT.md` | 本机绝对路径：101 |
| `results/032_research_presentation_storyline_coherence_recovery/generated/BUILD_MANIFEST.json` | 本机绝对路径：29、32、35；其他仓库地址或项目名（隐私属性待确认）：29、35 |
| `results/032_research_presentation_storyline_coherence_recovery/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、63、65、69、71、74；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、63、65、69、71、74 |
| `results/032_research_presentation_storyline_coherence_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/032_research_presentation_storyline_coherence_recovery/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214 |
| `results/032_research_presentation_storyline_coherence_recovery/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/032_research_presentation_storyline_coherence_recovery/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/033_research_presentation_deck_rhythm_quality_loop/RESULT.md` | 本机绝对路径：64 |
| `results/033_research_presentation_deck_rhythm_quality_loop/generated/BUILD_MANIFEST.json` | 本机绝对路径：297、300、303；其他仓库地址或项目名（隐私属性待确认）：297、303 |
| `results/033_research_presentation_deck_rhythm_quality_loop/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、63、65、69、71、74；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、63、65、69、71、74 |
| `results/033_research_presentation_deck_rhythm_quality_loop/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/033_research_presentation_deck_rhythm_quality_loop/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214 |
| `results/033_research_presentation_deck_rhythm_quality_loop/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/033_research_presentation_deck_rhythm_quality_loop/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/034_research_presentation_render_identity_ci_recovery/RESULT.md` | 本机绝对路径：87 |
| `results/034_research_presentation_render_identity_ci_recovery/generated/BUILD_MANIFEST.json` | 本机绝对路径：554、557、560；其他仓库地址或项目名（隐私属性待确认）：554、560 |
| `results/034_research_presentation_render_identity_ci_recovery/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、63、65、69、71、74；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、63、65、69、71、74 |
| `results/034_research_presentation_render_identity_ci_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/034_research_presentation_render_identity_ci_recovery/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214 |
| `results/034_research_presentation_render_identity_ci_recovery/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/034_research_presentation_render_identity_ci_recovery/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/035_research_presentation_generic_model_support_recovery/RESULT.md` | 本机绝对路径：39、43 |
| `results/035_research_presentation_generic_model_support_recovery/generated/BUILD_MANIFEST.json` | 本机绝对路径：554、557、560；其他仓库地址或项目名（隐私属性待确认）：554、560 |
| `results/035_research_presentation_generic_model_support_recovery/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、66、68、72、74、77；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、66、68、72、74、77 |
| `results/035_research_presentation_generic_model_support_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/035_research_presentation_generic_model_support_recovery/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214 |
| `results/035_research_presentation_generic_model_support_recovery/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/035_research_presentation_generic_model_support_recovery/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/036_research_presentation_process_page_projection_recovery/RESULT.md` | 本机绝对路径：44–45 |
| `results/036_research_presentation_process_page_projection_recovery/generated/BUILD_MANIFEST.json` | 本机绝对路径：554、557、560；其他仓库地址或项目名（隐私属性待确认）：554、560 |
| `results/036_research_presentation_process_page_projection_recovery/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、66、68、72、74、77；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、66、68、72、74、77 |
| `results/036_research_presentation_process_page_projection_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/036_research_presentation_process_page_projection_recovery/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214 |
| `results/036_research_presentation_process_page_projection_recovery/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/036_research_presentation_process_page_projection_recovery/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/037_research_presentation_audience_transition_copy_recovery/RESULT.md` | 本机绝对路径：51–52 |
| `results/037_research_presentation_audience_transition_copy_recovery/generated/BUILD_MANIFEST.json` | 本机绝对路径：553、556、559；其他仓库地址或项目名（隐私属性待确认）：553、559 |
| `results/037_research_presentation_audience_transition_copy_recovery/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、66、68、72、74、77；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、66、68、72、74、77 |
| `results/037_research_presentation_audience_transition_copy_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/037_research_presentation_audience_transition_copy_recovery/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214 |
| `results/037_research_presentation_audience_transition_copy_recovery/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/037_research_presentation_audience_transition_copy_recovery/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/038_research_presentation_two_real_paper_holdouts/RESULT.md` | 本机绝对路径：151 |
| `results/038_research_presentation_two_real_paper_holdouts/medical/generated/BUILD_MANIFEST.json` | 本机绝对路径：503、506、509；其他仓库地址或项目名（隐私属性待确认）：503、509 |
| `results/038_research_presentation_two_real_paper_holdouts/medical/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、60、62、66、68、71；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、60、62、66、68、71 |
| `results/038_research_presentation_two_real_paper_holdouts/medical/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/038_research_presentation_two_real_paper_holdouts/medical/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214 |
| `results/038_research_presentation_two_real_paper_holdouts/medical/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/038_research_presentation_two_real_paper_holdouts/medical/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/BUILD_MANIFEST.json` | 本机绝对路径：433、436、439；其他仓库地址或项目名（隐私属性待确认）：433、439 |
| `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、64、66、70、72、75；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、64、66、70、72、75 |
| `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214 |
| `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/038_research_presentation_two_real_paper_holdouts/statistics/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/039_research_presentation_quality_loop_execution_recovery/RESULT.md` | 本机绝对路径：41–42 |
| `results/039_research_presentation_quality_loop_execution_recovery/generated/BUILD_MANIFEST.json` | 本机绝对路径：687、690、693；其他仓库地址或项目名（隐私属性待确认）：687、693 |
| `results/039_research_presentation_quality_loop_execution_recovery/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、66、68、72、74、77；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、66、68、72、74、77 |
| `results/039_research_presentation_quality_loop_execution_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/039_research_presentation_quality_loop_execution_recovery/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214 |
| `results/039_research_presentation_quality_loop_execution_recovery/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/039_research_presentation_quality_loop_execution_recovery/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/RESULT.md` | 本机绝对路径：198–199 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated/BUILD_MANIFEST.json` | 本机绝对路径：612、615、618；其他仓库地址或项目名（隐私属性待确认）：612、618 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、63、65、69、71、74；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、63、65、69、71、74 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/biostatistics_deseq2/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/BUILD_MANIFEST.json` | CARE 名称或数据相关描述（候选）：493；本机绝对路径：669、672、675；其他仓库地址或项目名（隐私属性待确认）：669、675 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、63、65、69、71、74；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、63、65、69、71、74 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/deck_plan.json` | CARE 名称或数据相关描述（候选）：159 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/deck_sequence_summary.json` | CARE 名称或数据相关描述（候选）：376 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_cardiac_ultrasound/source_bundle.json` | CARE 名称或数据相关描述（候选）：277 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/medical_retfound/production_attempt_failure.log` | 本机绝对路径：2、5、11、13、16、19 |
| `results/041_research_presentation_frozen_four_paper_generalization_batch/statistics_tmb/production_attempt_failure.log` | 本机绝对路径：2、5、11、13、16、19 |
| `results/042_research_presentation_semantic_compatibility_recovery/RESULT.md` | 本机绝对路径：98、103 |
| `results/042_research_presentation_semantic_compatibility_recovery/generated/BUILD_MANIFEST.json` | 本机绝对路径：735、738、741；其他仓库地址或项目名（隐私属性待确认）：735、741 |
| `results/042_research_presentation_semantic_compatibility_recovery/generated/cuhk_production_build/compile.log` | 本机绝对路径：8、10、14、16、23、25、66、68、72、74、77；其他仓库地址或项目名（隐私属性待确认）：8、10、14、16、23、25、66、68、72、74、77 |
| `results/042_research_presentation_semantic_compatibility_recovery/generated/cuhk_production_build/fontconfig/fonts.conf` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/042_research_presentation_semantic_compatibility_recovery/generated/cuhk_production_build/main.log` | 本机绝对路径：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214；其他仓库地址或项目名（隐私属性待确认）：9、11、18、25、71、77、79、94、98、100、102、105、107、120、127、129、131、133、135、137、141、146、168、172、174、176、180、184、186、188、192、201、203、219、223、227、233、236、241、243、245、247、250、255、257、260、262、264、266、268、272、275、277、279、281、283、285、287、293、295、297、299、301、305、311、313、317、331、337、339、359、366、368、372、374、382、384、388、394、409、411、417、420、422、424、436、445、447、452、454、458、461、511、524、527、548、550、559、575、577、579、581、584、586、590、592、598、600、621、628、630、632、634、636、638、645、728、975、1052、1058、1060、1125、1127、1129、1131、1133、1135、1210、1214 |
| `results/042_research_presentation_semantic_compatibility_recovery/generated/dependency_probe.json` | 本机绝对路径：7、12、17、48、50、52、54、56、58；其他仓库地址或项目名（隐私属性待确认）：7、12、17、48、50、52、54、56、58、61–63 |
| `results/042_research_presentation_semantic_compatibility_recovery/generated/render_chinese_math_pdf_probe.json` | 本机绝对路径：8、10、15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293；其他仓库地址或项目名（隐私属性待确认）：15、75、200、207、211–212、215–216、225、227、232、234、240–242、246–247、251–252、259、262、265、270、272–273、292–293 |
| `results/052_writing_style_reader_facing_generalization_closure/RESULT.md` | 本机绝对路径：244、266、274 |
| `results/052_writing_style_reader_facing_generalization_closure/fresh_holdouts/holdout_1_python_re_docs/replay/candidate_replay_run.json` | 本机绝对路径：9、16 |
| `results/052_writing_style_reader_facing_generalization_closure/fresh_holdouts/holdout_2_fft_wikipedia/replay/candidate_replay_run.json` | 本机绝对路径：9、16 |
| `results/052_writing_style_reader_facing_generalization_closure/known_regression/replay/candidate_replay_run.json` | 本机绝对路径：9、16 |
| `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/after_restore_marketplaces.json` | 本机绝对路径：5、8、13、17、20 |
| `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/after_restore_plugins.json` | 本机绝对路径：12、16、30、34、48、62、76、90、104、108、122、126、140、144、158、162、176、180、194、198、212、216 |
| `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/before_marketplaces.json` | 本机绝对路径：5、8、13、17、20 |
| `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/before_plugins.json` | 本机绝对路径：12、16、30、34、48、62、76、90、104、108、122、126、140、144、158、162、176、180、194、198、212、216 |
| `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/candidate_add_writing_style.json` | 本机绝对路径：6 |
| `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/candidate_marketplaces.json` | 本机绝对路径：5、8、13 |
| `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/candidate_plugins.json` | 本机绝对路径：12、16、30、34、48、62、76、90 |
| `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/ordinary_production_routing.jsonl` | 本机绝对路径：2、5–12 |
| `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/restore_add_marketplace.json` | 本机绝对路径：3 |
| `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/restore_add_writing_style.json` | 本机绝对路径：6 |
| `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/smoke_verification.json` | 本机绝对路径：2、15、17 |
| `results/052_writing_style_reader_facing_generalization_closure/production_smoke/20260910T155228Z/smoke_verification_pre_restore.json` | 本机绝对路径：2 |
| `results/052_writing_style_reader_facing_generalization_closure/release_identity_verification/20260911T004351Z/RELEASE_IDENTITY_ADJUDICATION.md` | 本机绝对路径：24 |
| `results/052_writing_style_reader_facing_generalization_closure/release_identity_verification/20260911T004351Z/after_restore_marketplaces.json` | 本机绝对路径：10 |
| `results/052_writing_style_reader_facing_generalization_closure/release_identity_verification/20260911T004351Z/after_restore_plugins.json` | 本机绝对路径：9 |
| `results/052_writing_style_reader_facing_generalization_closure/release_identity_verification/20260911T004351Z/before_marketplaces.json` | 本机绝对路径：10 |
| `results/052_writing_style_reader_facing_generalization_closure/release_identity_verification/20260911T004351Z/before_plugins.json` | 本机绝对路径：9 |
| `results/052_writing_style_reader_facing_generalization_closure/release_identity_verification/20260911T004351Z/candidate_add_writing_style.json` | 本机绝对路径：10 |
| `results/052_writing_style_reader_facing_generalization_closure/release_identity_verification/20260911T004351Z/candidate_marketplaces.json` | 本机绝对路径：10 |
| `results/052_writing_style_reader_facing_generalization_closure/release_identity_verification/20260911T004351Z/candidate_plugins.json` | 本机绝对路径：9 |
| `results/052_writing_style_reader_facing_generalization_closure/release_identity_verification/20260911T004351Z/ordinary_production_routing.jsonl` | 本机绝对路径：2 |
| `results/052_writing_style_reader_facing_generalization_closure/release_identity_verification/20260911T004351Z/release_identity_verification.json` | 本机绝对路径：4、6、16、18 |
| `results/052_writing_style_reader_facing_generalization_closure/release_identity_verification/20260911T004351Z/restore_add_marketplace.json` | 本机绝对路径：7、11 |
| `results/052_writing_style_reader_facing_generalization_closure/release_identity_verification/20260911T004351Z/restore_add_writing_style.json` | 本机绝对路径：10 |
| `results/052_writing_style_reader_facing_generalization_closure/unrelated_regressions/english_scientific_prose/replay/candidate_replay_run.json` | 本机绝对路径：9、16 |
| `results/052_writing_style_reader_facing_generalization_closure/unrelated_regressions/fidelity_only/replay/candidate_replay_run.json` | 本机绝对路径：9、16 |
| `results/052_writing_style_reader_facing_generalization_closure/unrelated_regressions/light_chinese_polish/replay/candidate_replay_run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/DEEP_RESEARCH_REPRESENTATIVE_REPLAY_BLOCKER_C6.md` | 本机绝对路径：40、47、54、61、64 |
| `results/055_clear_writing_release_convergence/DEEP_RESEARCH_REPRESENTATIVE_REPLAY_C6_SUCCESS.md` | 本机绝对路径：48–54 |
| `results/055_clear_writing_release_convergence/FINAL_TERRA_CONTRACT_NARROWING_RECOVERY.md` | 本机绝对路径：96 |
| `results/055_clear_writing_release_convergence/FINAL_TERRA_REVIEW_BLOCKER_C6.md` | 本机绝对路径：61 |
| `results/055_clear_writing_release_convergence/G7_FRESH_EXECUTION_C6.md` | 本机绝对路径：100 |
| `results/055_clear_writing_release_convergence/PHASE4_PRIVATE_ARTIFACT_GAP.md` | 本机绝对路径：75、78、80 |
| `results/055_clear_writing_release_convergence/PREFINAL_CRITIC_REVIEW_C6.md` | CARE 名称或数据相关描述（候选）：65、81、87 |
| `results/055_clear_writing_release_convergence/PRODUCTION_SMOKE_RESTORE_C6.md` | 本机绝对路径：19、22、39、65–66、88、99、102 |
| `results/055_clear_writing_release_convergence/RESULT.md` | 本机绝对路径：44 |
| `results/055_clear_writing_release_convergence/compatibility_replay/english_scientific_prose/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/compatibility_replay/english_scientific_prose/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/compatibility_replay/fidelity_only/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/compatibility_replay/fidelity_only/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/compatibility_replay/light_chinese_polish/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/compatibility_replay/light_chinese_polish/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/compatibility_replay_c6/english_scientific_prose/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/compatibility_replay_c6/english_scientific_prose/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/compatibility_replay_c6/fidelity_only/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/compatibility_replay_c6/fidelity_only/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/compatibility_replay_c6/light_chinese_polish/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/compatibility_replay_c6/light_chinese_polish/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/compatibility_replay_c6/python_re_docs/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/compatibility_replay_c6/python_re_docs/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/g1_candidate_replay/RESULT.md` | 本机绝对路径：29 |
| `results/055_clear_writing_release_convergence/g1_candidate_replay/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/g1_candidate_replay/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/g7_fresh_batch/F1_noisy_code_repro/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/g7_fresh_batch/F1_noisy_code_repro/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/g7_fresh_batch/F2_formula_table/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/g7_fresh_batch/F2_formula_table/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/g7_fresh_batch/F3_long_future_limitations/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/g7_fresh_batch/F3_long_future_limitations/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/known_regressions/bloom_c6_replay/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/known_regressions/bloom_c6_replay/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/known_regressions/fft_c1_failure/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/known_regressions/fft_c1_failure/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/known_regressions/fft_c2_replay/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/known_regressions/fft_c2_replay/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/known_regressions/fft_c3_replay/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/known_regressions/fft_c3_replay/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/known_regressions/fft_c6_replay/artifacts/plugin-add.json` | 本机绝对路径：3 |
| `results/055_clear_writing_release_convergence/known_regressions/fft_c6_replay/artifacts/run.json` | 本机绝对路径：9、16 |
| `results/055_clear_writing_release_convergence/production_smoke/after_restore_marketplaces.json` | 本机绝对路径：5、8、13、17、20 |
| `results/055_clear_writing_release_convergence/production_smoke/after_restore_plugins.json` | 本机绝对路径：12、16、30、34、48、62、76、90、104、108、122、126、140、144、158、162、176、180、194、198、212、216 |
| `results/055_clear_writing_release_convergence/production_smoke/before_marketplaces.json` | 本机绝对路径：5、8、13、17、20 |
| `results/055_clear_writing_release_convergence/production_smoke/before_plugins.json` | 本机绝对路径：12、16、30、34、48、62、76、90、104、108、122、126、140、144、158、162、176、180、194、198、212、216 |
| `results/055_clear_writing_release_convergence/production_smoke/installed_smoke_marketplaces.json` | 本机绝对路径：5、8、13 |
| `results/055_clear_writing_release_convergence/production_smoke/installed_smoke_plugins.json` | 本机绝对路径：12、16、30、34、48、62、76、90 |
| `results/055_clear_writing_release_convergence/production_smoke/smoke_events.jsonl` | 本机绝对路径：2、5–8、10–13 |
| `results/055_clear_writing_release_convergence/text_review/TEXT_REVIEW.json` | CARE 名称或数据相关描述（候选）：65 |
| `results/056_product_delivery_discipline/FINAL_INTEGRATION_RELEASE_CLOSURE.md` | 本机绝对路径：58、60–63、69–72 |
| `results/056_product_delivery_discipline/RESULT.md` | 本机绝对路径：81 |
| `results/056_product_delivery_discipline/evidence_manifest.json` | 本机绝对路径：40、42 |
| `results/056_product_delivery_discipline/final_integration_release_closure.json` | 本机绝对路径：29、31–34、39–40 |
| `results/056_product_delivery_discipline/real_host_smoke/FINAL_SUMMARY.json` | 本机绝对路径：9–10、24–32、37 |
| `results/056_product_delivery_discipline/real_host_smoke/FINAL_SUMMARY.md` | 本机绝对路径：10–11、24、27 |
| `results/056_product_delivery_discipline/real_host_smoke/REAL_USER_HUMAN_GATE_FINAL_SUMMARY.json` | 本机绝对路径：26–31、33–37、39–41 |
| `results/056_product_delivery_discipline/real_host_smoke/REAL_USER_HUMAN_GATE_FINAL_SUMMARY.md` | 本机绝对路径：24、27 |
| `results/056_product_delivery_discipline/real_host_smoke/agent_resolvable.stdout.jsonl` | 本机绝对路径：13 |
| `results/056_product_delivery_discipline/real_host_smoke/agent_resolvable_last_message.txt` | 本机绝对路径：3 |
| `results/056_product_delivery_discipline/real_host_smoke/agent_resolvable_meta.json` | 本机绝对路径：7、9–10、14 |
| `results/056_product_delivery_discipline/real_host_smoke/agent_resolvable_prompt.txt` | 本机绝对路径：1 |
| `results/056_product_delivery_discipline/real_host_smoke/backup_manifest_copy.json` | 本机绝对路径：4、9、19 |
| `results/056_product_delivery_discipline/real_host_smoke/backup_manifest_locator.txt` | 本机绝对路径：1 |
| `results/056_product_delivery_discipline/real_host_smoke/candidate_host_install_output.txt` | 本机绝对路径：1–4、6、18 |
| `results/056_product_delivery_discipline/real_host_smoke/candidate_host_status_output.txt` | 本机绝对路径：1、13 |
| `results/056_product_delivery_discipline/real_host_smoke/candidate_host_validate_output.txt` | 本机绝对路径：1、13、19–20 |
| `results/056_product_delivery_discipline/real_host_smoke/default_human_only_first_attempt_path_miss.json` | 本机绝对路径：2 |
| `results/056_product_delivery_discipline/real_host_smoke/default_human_only_initial_meta.json` | 本机绝对路径：7、9 |
| `results/056_product_delivery_discipline/real_host_smoke/default_human_only_path_bound_initial_meta.json` | 本机绝对路径：7、9–10 |
| `results/056_product_delivery_discipline/real_host_smoke/default_human_only_path_bound_prompt.txt` | 本机绝对路径：1 |
| `results/056_product_delivery_discipline/real_host_smoke/default_human_only_path_bound_resume.stdout.jsonl` | 本机绝对路径：9–10、18 |
| `results/056_product_delivery_discipline/real_host_smoke/default_human_only_path_bound_resume_last_message.txt` | 本机绝对路径：3 |
| `results/056_product_delivery_discipline/real_host_smoke/default_human_only_path_bound_resume_meta.json` | 本机绝对路径：8、15 |
| `results/056_product_delivery_discipline/real_host_smoke/default_human_only_resume.stdout.jsonl` | 其他仓库地址或项目名（隐私属性待确认）：6；本机绝对路径：10、13、24、30–31、39 |
| `results/056_product_delivery_discipline/real_host_smoke/default_human_only_resume_last_message.txt` | 本机绝对路径：1 |
| `results/056_product_delivery_discipline/real_host_smoke/default_human_only_resume_meta.json` | 本机绝对路径：8 |
| `results/056_product_delivery_discipline/real_host_smoke/plan_mode_appserver_probe_messages.json` | 本机绝对路径：35、53、101–102、115、117、120、151、179、202–203、241、428、456、522、532 |
| `results/056_product_delivery_discipline/real_host_smoke/post_restore_host_status.txt` | 本机绝对路径：1、13 |
| `results/056_product_delivery_discipline/real_host_smoke/pre_host_status.txt` | 本机绝对路径：1、13 |
| `results/056_product_delivery_discipline/real_host_smoke/preflight_identity_and_hashes.json` | 本机绝对路径：5–6、76、82、88、136、141、155 |
| `results/056_product_delivery_discipline/real_host_smoke/r2_backup_manifest_copy.json` | 本机绝对路径：4、9、19 |
| `results/056_product_delivery_discipline/real_host_smoke/r2_backup_manifest_locator.txt` | 本机绝对路径：1 |
| `results/056_product_delivery_discipline/real_host_smoke/r2_candidate_host_install_output.txt` | 本机绝对路径：1、4–7、9、21 |
| `results/056_product_delivery_discipline/real_host_smoke/r2_candidate_host_status_output.txt` | 本机绝对路径：1、4、16 |
| `results/056_product_delivery_discipline/real_host_smoke/r2_candidate_host_validate_output.txt` | 本机绝对路径：1、4、16、22–23 |
| `results/056_product_delivery_discipline/real_host_smoke/r2_candidate_install_bundle.json` | 本机绝对路径：3–5、12–13、15、20、25、32、37、42 |
| `results/056_product_delivery_discipline/real_host_smoke/r2_plan_mode_appserver_probe_messages.json` | 本机绝对路径：32、52、102–103、116、118、121–122、154、196–197、237 |
| `results/056_product_delivery_discipline/real_host_smoke/r2_plan_mode_appserver_probe_result.json` | 本机绝对路径：7、9、39、47；CARE 名称或数据相关描述（候选）：39 |
| `results/056_product_delivery_discipline/real_host_smoke/r2_post_restore_host_status.txt` | 本机绝对路径：1、13 |
| `results/056_product_delivery_discipline/real_host_smoke/r2_pre_host_status.txt` | 本机绝对路径：1、4、16 |
| `results/056_product_delivery_discipline/real_host_smoke/r2_pre_managed_hashes.json` | 本机绝对路径：3、5、10、15 |
| `results/056_product_delivery_discipline/real_host_smoke/r2_restore_precheck_and_result.json` | 本机绝对路径：3、7、12、22、27、32、37、47、49、52、56、58、62、67、72 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_backup_manifest_copy.json` | 本机绝对路径：4、9、19 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_backup_manifest_locator.txt` | 本机绝对路径：1 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_candidate_host_install_output.txt` | 本机绝对路径：1、4–7、9、21 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_candidate_host_status_output.txt` | 本机绝对路径：1、4、16 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_candidate_host_validate_output.txt` | 本机绝对路径：1、4、16、22–23 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_candidate_install_bundle.json` | 本机绝对路径：6–7、9、14、19 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_child_initial_meta.json` | 本机绝对路径：8、10–11 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_child_initial_prompt.txt` | 本机绝对路径：2 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_child_resume.stdout.jsonl` | 本机绝对路径：7–8 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_child_resume_meta.json` | 本机绝对路径：9 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_post_restore_host_status.txt` | 本机绝对路径：1、4、16 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_restore_precheck_and_result.json` | 本机绝对路径：3、7、12、22、27、32、37、47、49、52、56、58、62、67、72、81 |
| `results/056_product_delivery_discipline/real_host_smoke/real_user_resume_preflight.json` | 本机绝对路径：6–7、10、15、20、36–37 |
| `results/056_product_delivery_discipline/real_host_smoke/restore_conservative_result.json` | 本机绝对路径：2、44 |
| `results/056_product_delivery_discipline/real_host_smoke/restore_precheck_and_result.json` | 本机绝对路径：2、6、11、21、27、33、39、49 |
| `results/056_product_delivery_discipline/replay_evidence/ai_skills_core/candidate_replay_run.json` | 本机绝对路径：9、16、19–20 |
| `results/056_product_delivery_discipline/replay_evidence/ai_skills_core/plugin-add.json` | 本机绝对路径：3 |
| `results/056_product_delivery_discipline/replay_evidence/web_development/candidate_replay_run.json` | 本机绝对路径：9、16、19–20 |
| `results/056_product_delivery_discipline/replay_evidence/web_development/plugin-add.json` | 本机绝对路径：3 |
| `results/056_product_delivery_discipline/replay_evidence/workflow_core/candidate_replay_run.json` | 本机绝对路径：9、16、19–20 |
| `results/056_product_delivery_discipline/replay_evidence/workflow_core/plugin-add.json` | 本机绝对路径：3 |
| `results/056_product_delivery_discipline/replay_evidence_unbiased/ai_skills_core/candidate_replay_run.json` | 本机绝对路径：9、16、19–20 |
| `results/056_product_delivery_discipline/replay_evidence_unbiased/ai_skills_core/child.stdout.jsonl` | 本机绝对路径：4–5 |
| `results/056_product_delivery_discipline/replay_evidence_unbiased/ai_skills_core/plugin-add.json` | 本机绝对路径：3 |
| `results/056_product_delivery_discipline/replay_evidence_unbiased/ai_skills_core/raw_evidence_manifest.json` | 本机绝对路径：9、16、20–21 |
| `results/056_product_delivery_discipline/replay_evidence_unbiased/web_development/candidate_replay_run.json` | 本机绝对路径：9、16、19–20 |
| `results/056_product_delivery_discipline/replay_evidence_unbiased/web_development/child.stdout.jsonl` | 本机绝对路径：4–5、8–9、11–12、15–16 |
| `results/056_product_delivery_discipline/replay_evidence_unbiased/web_development/plugin-add.json` | 本机绝对路径：3 |
| `results/056_product_delivery_discipline/replay_evidence_unbiased/web_development/raw_evidence_manifest.json` | 本机绝对路径：9、16、20–21 |
| `results/056_product_delivery_discipline/replay_evidence_unbiased/workflow_core/candidate_replay_run.json` | 本机绝对路径：9、16、19–20 |
| `results/056_product_delivery_discipline/replay_evidence_unbiased/workflow_core/child.stdout.jsonl` | 本机绝对路径：4–5、8–9、12–13 |
| `results/056_product_delivery_discipline/replay_evidence_unbiased/workflow_core/plugin-add.json` | 本机绝对路径：3 |
| `results/056_product_delivery_discipline/replay_evidence_unbiased/workflow_core/raw_evidence_manifest.json` | 本机绝对路径：9、16、20–21 |
| `results/057_repo_agents_hygiene/MANIFEST.md` | 其他仓库地址或项目名（隐私属性待确认）：15 |
| `results/057_repo_agents_hygiene/RESULT.md` | 其他仓库地址或项目名（隐私属性待确认）：16、30、110 |
| `results/057_repo_agents_hygiene/SEMANTIC_PRESERVATION.md` | 其他仓库地址或项目名（隐私属性待确认）：18、67、69 |
| `results/057_repo_agents_hygiene/SIZE_REPORT.md` | 其他仓库地址或项目名（隐私属性待确认）：36、44 |
| `results/ai-skills-core--machine-update-orchestration/ADAPTING_CONSUMER_STATUS.json` | 本机绝对路径：34–35、63–64、106–107；其他仓库地址或项目名（隐私属性待确认）：107 |
| `results/ai-skills-core--machine-update-orchestration/ADAPTING_CONSUMER_STATUS.md` | 本机绝对路径：65–67；其他仓库地址或项目名（隐私属性待确认）：67 |
| `results/ai-skills-core--machine-update-orchestration/BRIDGE_REVALIDATION_SNAPSHOT.md` | 其他仓库地址或项目名（隐私属性待确认）：14 |
| `results/ai-skills-core--machine-update-orchestration/CODEX_EXECUTOR_REPAIR_PROMPT.md` | 其他仓库地址或项目名（隐私属性待确认）：75 |
| `results/ai-skills-core--machine-update-orchestration/CODEX_EXECUTOR_REPAIR_PROMPT_2.md` | 本机绝对路径：36 |
| `results/ai-skills-core--machine-update-orchestration/CUHK_WORKSTATION_WSL_CODEX_MACHINE_SYNC_2026-09-29.json` | 本机绝对路径：13–15、26、86–87、95、109；其他仓库地址或项目名（隐私属性待确认）：14–15、26、86–88、95、109 |
| `results/ai-skills-core--machine-update-orchestration/CUHK_WORKSTATION_WSL_CODEX_MACHINE_SYNC_2026-09-29.md` | 本机绝对路径：17–19、31、68–69、77、105；其他仓库地址或项目名（隐私属性待确认）：18–19、31、68–70、77、105 |
| `results/ai-skills-core--machine-update-orchestration/FINAL_ADAPTATION_CLOSURE.json` | 本机绝对路径：26、43、61、115；其他仓库地址或项目名（隐私属性待确认）：61、115 |
| `results/ai-skills-core--machine-update-orchestration/FINAL_ADAPTATION_CLOSURE.md` | 本机绝对路径：25–27；其他仓库地址或项目名（隐私属性待确认）：27 |
| `results/ai-skills-core--machine-update-orchestration/FINAL_CLOSURE_FREEZE.json` | 本机绝对路径：10–11；其他仓库地址或项目名（隐私属性待确认）：21 |
| `results/ai-skills-core--machine-update-orchestration/G2_POST_REVIEW_PROMOTION_EVIDENCE.md` | 本机绝对路径：87、119、136；其他仓库地址或项目名（隐私属性待确认）：87、119 |
| `results/ai-skills-core--machine-update-orchestration/IMPLEMENTATION_EVIDENCE.md` | 其他仓库地址或项目名（隐私属性待确认）：24、33、70；本机绝对路径：70 |
| `results/ai-skills-core--machine-update-orchestration/INDEPENDENT_REVIEWER_PROMPT.md` | 其他仓库地址或项目名（隐私属性待确认）：20 |
| `results/ai-skills-core--machine-update-orchestration/LEGION_FINAL_CLOSURE_REFRESH_2026-09-29.json` | 其他仓库地址或项目名（隐私属性待确认）：28、75、78 |
| `results/ai-skills-core--machine-update-orchestration/LEGION_FINAL_CLOSURE_REFRESH_2026-09-29.md` | 其他仓库地址或项目名（隐私属性待确认）：23、104 |
| `results/ai-skills-core--machine-update-orchestration/LONGLEAF_BACKUP_CODEX_FINAL_CLOSURE_REFRESH_2026-09-29.json` | 其他仓库地址或项目名（隐私属性待确认）：28、81；本机绝对路径：36–37、82–83、94、99 |
| `results/ai-skills-core--machine-update-orchestration/LONGLEAF_BACKUP_CODEX_FINAL_CLOSURE_REFRESH_2026-09-29.md` | 其他仓库地址或项目名（隐私属性待确认）：23；本机绝对路径：36–37、98、113、120、142 |
| `results/ai-skills-core--machine-update-orchestration/LONGLEAF_CODEX_FINAL_CLOSURE_REFRESH_2026-09-29.json` | 本机绝对路径：21–22、62；其他仓库地址或项目名（隐私属性待确认）：61、63 |
| `results/ai-skills-core--machine-update-orchestration/LONGLEAF_CODEX_FINAL_CLOSURE_REFRESH_2026-09-29.md` | 本机绝对路径：26–27、84、96–99 |
| `results/ai-skills-core--machine-update-orchestration/WORKSTATION_WINDOWS_CODEX_MACHINE_SYNC_2026-09-29.json` | 其他仓库地址或项目名（隐私属性待确认）：29、80、82 |
| `results/ai-skills-core--machine-update-orchestration/WORKSTATION_WINDOWS_CODEX_MACHINE_SYNC_2026-09-29.md` | 其他仓库地址或项目名（隐私属性待确认）：72 |
| `results/ai-skills-core--machine-update-orchestration/candidate_replay/CANDIDATE_REPLAY_EVIDENCE.md` | 本机绝对路径：13；其他仓库地址或项目名（隐私属性待确认）：13、20 |
| `results/ai-skills-core--machine-update-orchestration/candidate_replay/public_machine_state.md` | 其他仓库地址或项目名（隐私属性待确认）：8 |
| `results/ai-skills-core--machine-update-orchestration/cuhk_workstation_wsl_fresh_normal_entry_last_message.txt` | 本机绝对路径：5；其他仓库地址或项目名（隐私属性待确认）：5 |
| `results/ai-skills-core--machine-update-orchestration/fixture_execution/G4_G5_FIXTURE_EVIDENCE.md` | 本机绝对路径：6–7 |
| `results/ai-skills-core--machine-update-orchestration/fixture_execution/candidate_g4_g5_manifest.json` | 本机绝对路径：7、16、25、33、42、50、59 |
| `results/ai-skills-core--machine-update-orchestration/fixture_execution/g4_g5_fixture_evidence.json` | 本机绝对路径：3、16、38、60、80、102、123、147、161、168、171–172、174；其他仓库地址或项目名（隐私属性待确认）：161、168 |
| `results/ai-skills-core--machine-update-orchestration/fresh_longleaf_backup_final_direct_codex_last_message.txt` | 本机绝对路径：7 |
| `results/ai-skills-core--machine-update-orchestration/fresh_longleaf_users_direct_codex_last_message.txt` | 本机绝对路径：3 |
| `results/chatgpt-web--pass-integrity/DELIVERY_ASSURANCE_FRESH_CRITIC_REGRESSION_2026-10-20.md` | CARE 名称或数据相关描述（候选）：17；其他仓库地址或项目名（隐私属性待确认）：17 |
| `results/chatgpt-web--pass-integrity/STAT5060_VALIDATOR_FRESH_CRITIC_REGRESSION_2026-10-20.md` | 其他仓库地址或项目名（隐私属性待确认）：7 |
| `results/cross-repo--workflow-identity-gate-lifecycle/replay/artifacts/ai-skills-core-run.json` | 本机绝对路径：9、16 |
| `results/cross-repo--workflow-identity-gate-lifecycle/replay/artifacts/workflow-core-run.json` | 本机绝对路径：9、16 |
| `results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/artifacts/ai-skills-core-run.json` | 本机绝对路径：9、16 |
| `results/cross-repo--workflow-identity-gate-lifecycle/replay/corrected/artifacts/workflow-core-run.json` | 本机绝对路径：9、16 |
| `results/documents-media--pdf-save-as-delivery/CI_BASELINE_DIFFERENTIAL.md` | 本机绝对路径：40 |
| `results/documents-media--pdf-save-as-delivery/CRITIC_CI_BASELINE_RECOVERY_PROMPT_V0_1.md` | 本机绝对路径：12 |
| `results/documents-media--pdf-save-as-delivery/D1_DELIVERY_EVENT.md` | 本机绝对路径：7 |
| `results/documents-media--pdf-save-as-delivery/INTEGRATION_RELEASE_PREFLIGHT.md` | 本机绝对路径：42 |
| `results/documents-media--pdf-save-as-delivery/PDF_SAVE_AS_DELIVERY_FORMAL_RELEASE_ISOLATION_PLANNER_HANDOFF_R0_2026-10-17.md` | 本机绝对路径：11 |
| `results/documents-media--pdf-save-as-delivery/PLANNER_HANDOFF.md` | 本机绝对路径：12 |
| `results/documents-media--pdf-save-as-delivery/PREFLIGHT.md` | 本机绝对路径：31 |
| `results/documents-media--scientific-pdf-rendering-reliability/EVIDENCE.md` | 本机绝对路径：263 |
| `results/documents-media--scientific-pdf-rendering-reliability/g7_release_reconciliation/profile_smokes/presentation-desktop.json` | 本机绝对路径：69、76；其他仓库地址或项目名（隐私属性待确认）：69、76 |
| `results/documents-media--scientific-pdf-rendering-reliability/g7_release_reconciliation/profile_smokes/research-main.json` | 本机绝对路径：69、76；其他仓库地址或项目名（隐私属性待确认）：69、76 |
| `results/documents-media--scientific-pdf-rendering-reliability/g7_release_reconciliation/profile_smokes/server-research-baseline.json` | 本机绝对路径：69、76；其他仓库地址或项目名（隐私属性待确认）：69、76 |
| `results/documents-media--scientific-pdf-rendering-reliability/renders/g5_research_authoring/evidence/consumption_summary.json` | 本机绝对路径：163；其他仓库地址或项目名（隐私属性待确认）：163 |
| `results/documents-media--scientific-pdf-rendering-reliability/renders/g5_research_authoring/evidence/render_receipt.json` | 本机绝对路径：31、38、43、50、71、274、279、299、307、312、317、322、327、332、337、342、347、352、365、369、373、377、381、385、389、393、397、401、406、413；其他仓库地址或项目名（隐私属性待确认）：31、38、43、50、71、274、279、299、307、312、317、322、327、332、337、342、347、352、365、369、373、377、381、385、389、393、397、401、406、413 |
| `results/documents-media--scientific-pdf-rendering-reliability/renders/g5_research_authoring_replay_96c0546/evidence/child.stdout.jsonl` | 本机绝对路径：7、16、20、25；其他仓库地址或项目名（隐私属性待确认）：16、20、25 |
| `results/documents-media--scientific-pdf-rendering-reliability/renders/g5_research_authoring_replay_96c0546/evidence/render_receipt.json` | 本机绝对路径：31、38、43、50、71、287、292、312、320、325、330、335、340、345、350、355、360、365、378、382、386、390、394、398、402、406、410、414、419、426；其他仓库地址或项目名（隐私属性待确认）：31、38、43、50、71、287、292、312、320、325、330、335、340、345、350、355、360、365、378、382、386、390、394、398、402、406、410、414、419、426 |
| `results/documents-media--scientific-pdf-rendering-reliability/renders/initial/direct_tex_note.receipt.json` | 本机绝对路径：10、13、22、25、46、90、95、100、105、110、115、120、125、130、135、180、184–185、190、194 |
| `results/documents-media--scientific-pdf-rendering-reliability/renders/initial/math_regression.receipt.json` | 本机绝对路径：13、23、35–36、38、47–48、50、71、76、306、311、316、321、326、331、336、341、346、351、396、400–401、406、410 |
| `results/documents-media--scientific-pdf-rendering-reliability/renders/initial/representative_formal_note.receipt.json` | 本机绝对路径：13、23、35–36、38、47–48、50、71、76、166、171、176、181、186、191、196、201、206、211、256、260–261、266、270 |
| `results/documents-media--scientific-pdf-rendering-reliability/renders/recovery_v0_2/direct_tex_note.receipt.json` | 本机绝对路径：6、10、13、18、22、25、41、52、57、77、85、90、95、100、105、110、115、120、125、130、143、147、151、155、159、163、167、171、175、179、184、188；其他仓库地址或项目名（隐私属性待确认）：6、13、18、25、41、52、57、77、85、90、95、100、105、110、115、120、125、130、143、147、151、155、159、163、167、171、175、179、184、188 |
| `results/documents-media--scientific-pdf-rendering-reliability/renders/recovery_v0_2/math_regression.receipt.json` | 本机绝对路径：13、23、31、35–36、38、43、47–48、50、71、76、268、273、293、301、306、311、316、321、326、331、336、341、346、359、363、367、371、375、379、383、387、391、395、400、404；其他仓库地址或项目名（隐私属性待确认）：31、38、43、50、71、268、273、293、301、306、311、316、321、326、331、336、341、346、359、363、367、371、375、379、383、387、391、395、400、404 |
| `results/documents-media--scientific-pdf-rendering-reliability/renders/recovery_v0_2/project_venue_note.receipt.json` | 本机绝对路径：9 |
| `results/documents-media--scientific-pdf-rendering-reliability/renders/recovery_v0_2/representative_formal_note.receipt.json` | 本机绝对路径：13、23、31、35–36、38、43、47–48、50、71、76、135、140、160、168、173、178、183、188、193、198、203、208、213、226、230、234、238、242、246、250、254、258、262、267、271；其他仓库地址或项目名（隐私属性待确认）：31、38、43、50、71、135、140、160、168、173、178、183、188、193、198、203、208、213、226、230、234、238、242、246、250、254、258、262、267、271 |
| `results/documents-media--scientific-pdf-rendering-reliability/renders/stability/representative_formal_note_retry.receipt.json` | 本机绝对路径：13、23、35–36、38、47–48、50、71、76、166、171、176、181、186、191、196、201、206、211、256、260–261、266、270 |
| `results/documents-media--scientific-pdf-rendering-reliability/work/direct_tex/direct_tex_note.log` | 本机绝对路径：112、150、162 |
| `results/documents-media--scientific-pdf-rendering-reliability/work/initial_math/canonical-header.tex` | 本机绝对路径：15、24、29、35、43、51 |
| `results/documents-media--scientific-pdf-rendering-reliability/work/initial_math/math_regression.generated.log` | 本机绝对路径：6、10、487、503、562、591、600、604、608、612、616、620、624、628、635、644、648、652、656、660、664、668、672、691、698、709、716、718、754、772、777、821、833、838、866、873、875、893、902、907、912、920、1091、1103 |
| `results/documents-media--scientific-pdf-rendering-reliability/work/initial_math/math_regression.generated.tex` | 本机绝对路径：77、86、91、97、105、113 |
| `results/documents-media--scientific-pdf-rendering-reliability/work/initial_representative/canonical-header.tex` | 本机绝对路径：15、24、29、35、43、51 |
| `results/documents-media--scientific-pdf-rendering-reliability/work/initial_representative/representative_formal_note.generated.log` | 本机绝对路径：6、10、487、503、562、591、600、604、608、612、616、620、624、628、635、644、648、652、656、660、664、668、672、691、698、709、716、718、754、772、777、821、833、838、866、873、875、893、902、907、912、920、1095、1107 |
| `results/documents-media--scientific-pdf-rendering-reliability/work/initial_representative/representative_formal_note.generated.tex` | 本机绝对路径：77、86、91、97、105、113 |
| `results/documents-media--scientific-pdf-rendering-reliability/work/stability_retry/canonical-header.tex` | 本机绝对路径：15、24、29、35、43、51 |
| `results/documents-media--scientific-pdf-rendering-reliability/work/stability_retry/representative_formal_note.generated.log` | 本机绝对路径：6、10、487、503、562、591、600、604、608、612、616、620、624、628、635、644、648、652、656、660、664、668、672、691、698、709、716、718、754、772、777、821、833、838、866、873、875、893、902、907、912、920、1095、1107 |
| `results/documents-media--scientific-pdf-rendering-reliability/work/stability_retry/representative_formal_note.generated.tex` | 本机绝对路径：77、86、91、97、105、113 |
| `results/hpc--slurm-cancel-production-closure/AMENDED_G4_EVIDENCE.md` | 实验室标识：10、26、34；本机绝对路径：19、53、70 |
| `results/hpc--slurm-cancel-production-closure/EXECUTION_EVIDENCE.md` | DII 项目标识或研究记录：16；CARE 名称或数据相关描述（候选）：16；本机绝对路径：31–32、49；实验室标识：62 |
| `results/hpc--slurm-cancel-production-closure/FINAL_RELEASE_CLOSURE.md` | DII 项目标识或研究记录：24、128；CARE 名称或数据相关描述（候选）：24、128；本机绝对路径：127 |
| `results/hpc--slurm-cancel-production-closure/LIVE_CONFIRMATION_EVIDENCE.md` | 实验室标识：12、29 |
| `results/hpc--slurm-cancel-production-closure/MAINTENANCE_ISSUE_COPY.md` | DII 项目标识或研究记录：13、29；CARE 名称或数据相关描述（候选）：13、29；本机绝对路径：15、31 |
| `results/hpc--slurm-cancel-production-closure/MCP_VERTICAL_EVIDENCE.md` | 本机绝对路径：14；实验室标识：41 |
| `results/hpc--slurm-cancel-production-closure/NATIVE_SCHEMA_REPAIR_EVIDENCE.md` | DII 项目标识或研究记录：12；CARE 名称或数据相关描述（候选）：12；实验室标识：12；本机绝对路径：29、32 |
| `results/hpc--slurm-cancel-production-closure/P0_FAILURE_ISOLATION_EVIDENCE.md` | DII 项目标识或研究记录：5；CARE 名称或数据相关描述（候选）：5 |
| `results/hpc--slurm-cancel-production-closure/PENDING_BINDING_REPAIR_EVIDENCE.md` | DII 项目标识或研究记录：3；CARE 名称或数据相关描述（候选）：3 |
| `results/hpc--slurm-cancel-production-closure/RELEASE_CANDIDATE_IDENTITY.md` | DII 项目标识或研究记录：20；CARE 名称或数据相关描述（候选）：20 |
| `results/hpc--slurm-cancel-production-closure/REPLACEMENT_G4_EVIDENCE.md` | 实验室标识：10、21、29 |
| `results/hpc--slurm-cancel-production-closure/RESULT.md` | 实验室标识：35、74、98、104；DII 项目标识或研究记录：91；CARE 名称或数据相关描述（候选）：91；本机绝对路径：129 |
| `results/hpc--slurm-cancel-production-closure/SESSION_AB_EVIDENCE.md` | 本机绝对路径：11、14–15、30、46、49、100；DII 项目标识或研究记录：64；CARE 名称或数据相关描述（候选）：64；实验室标识：79、86 |
| `results/hpc--slurm-race-policy-bounded-opt-in/CENTRAL_RELEASE_CLOSURE_2026-10-04.md` | DII 项目标识或研究记录：82、91、100–101 |
| `results/hpc--slurm-race-policy-bounded-opt-in/FINAL_CRITIC_REVIEW_2026-10-04.md` | DII 项目标识或研究记录：36、240 |
| `results/hpc--slurm-race-policy-bounded-opt-in/FINAL_CRITIC_REVIEW_R3_2026-10-04.md` | DII 项目标识或研究记录：141、173 |
| `results/hpc--slurm-race-policy-bounded-opt-in/RESULT.md` | DII 项目标识或研究记录：71、173 |
| `results/hpc--slurm-race-policy-bounded-opt-in/issue_96_central_release_clear_writing_input.md` | DII 项目标识或研究记录：38、41 |
| `results/hpc--slurm-race-policy-bounded-opt-in/issue_96_central_release_clear_writing_task.md` | DII 项目标识或研究记录：9–10 |
| `results/hpc--slurm-workflows-routing-refactor/tracking/clear-writing-final-update-receipt.md` | 本机绝对路径：8 |
| `results/hpc--slurm-workflows-routing-refactor/tracking/clear-writing-r2-receipt.md` | 本机绝对路径：8 |
| `results/hpc--slurm-workflows-routing-refactor/tracking/clear-writing-r3-receipt.md` | 本机绝对路径：8 |
| `results/hpc--slurm-workflows-routing-refactor/tracking/clear-writing-r4-receipt.md` | 本机绝对路径：8 |
| `results/hpc--slurm-workflows-routing-refactor/tracking/clear-writing-receipt.md` | 本机绝对路径：8 |
| `results/hpc--slurm-workflows-routing-refactor/tracking/clear-writing-recovery-receipt.md` | 本机绝对路径：8 |
| `results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REQUEST_V1.md` | 其他仓库地址或项目名（隐私属性待确认）：78；本机绝对路径：143、152、269 |
| `results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REQUEST_V2.md` | 其他仓库地址或项目名（隐私属性待确认）：77 |
| `results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REQUEST_V3.md` | 其他仓库地址或项目名（隐私属性待确认）：85 |
| `results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REQUEST_V5.md` | 其他仓库地址或项目名（隐私属性待确认）：116；本机绝对路径：186 |
| `results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V1.md` | 其他仓库地址或项目名（隐私属性待确认）：54 |
| `results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V2.md` | 其他仓库地址或项目名（隐私属性待确认）：115、265 |
| `results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V3_F03.md` | 其他仓库地址或项目名（隐私属性待确认）：34；本机绝对路径：214、226、382、536 |
| `results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V4.md` | 本机绝对路径：156、166、180、182；其他仓库地址或项目名（隐私属性待确认）：180、182 |
| `results/presentations--stage1-front-door-two-template-foundation/CRITIC_EXECUTION_READY_REVIEW_V5.md` | 本机绝对路径：25 |
| `results/presentations--stage1-front-door-two-template-foundation/EXECUTION_PACKAGE_V1_0.md` | 本机绝对路径：82、91 |
| `results/presentations--stage1-front-door-two-template-foundation/PLANNER_VALIDATION_V1_3.md` | 本机绝对路径：81、86 |
| `results/product-ui-copy--cross-plugin-production-integration/candidate_replay/dev_inputs/compatibility_sources.md` | 本机绝对路径：10、12；其他仓库地址或项目名（隐私属性待确认）：10、12、172–176 |
| `results/product-ui-copy--cross-plugin-production-integration/candidate_replay/dev_same_session/SAME_SESSION_REPLAY_PASS.json` | 本机绝对路径：24、31；其他仓库地址或项目名（隐私属性待确认）：24、31 |
| `results/product-ui-copy--cross-plugin-production-integration/candidate_replay/h2_compatibility_actual_output/G6_COMPATIBILITY_REPLAY_RUN.json` | 本机绝对路径：24、30、42、48、54–55；其他仓库地址或项目名（隐私属性待确认）：24、30、42、48 |
| `results/product-ui-copy--cross-plugin-production-integration/h2_release_candidate/H2_SAME_SESSION_REPLAY_PASS.json` | 本机绝对路径：25、33；其他仓库地址或项目名（隐私属性待确认）：25、33 |
| `results/product-ui-copy--cross-plugin-production-integration/h4_one_shot/H4_CANDIDATE_REPLAY_RUN.json` | 本机绝对路径：24、30、42、48、54–55；其他仓库地址或项目名（隐私属性待确认）：24、30、42、48 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance/PRODUCT_UI_COPY_HUMAN_ACCEPTANCE.md` | 本机绝对路径：192、204、206、208、220、232、236 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance/RENDER_CHECK.md` | 本机绝对路径：14；其他仓库地址或项目名（隐私属性待确认）：14 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/CUHK_DATE_PRODUCT_UI_COPY_ACCEPTANCE.md` | 本机绝对路径：242、252、262、272、282；其他仓库地址或项目名（隐私属性待确认）：242、252、262、272、282 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/RENDER_CHECK.md` | 其他仓库地址或项目名（隐私属性待确认）：5–6、11、13–15；本机绝对路径：13 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/header.tex` | 本机绝对路径：15、24、29、35、43、51；其他仓库地址或项目名（隐私属性待确认）：15、24、29、35、43、51 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/historical_comparison/AUDIT_COMPARISON.md` | 其他仓库地址或项目名（隐私属性待确认）：8 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/input.md` | 本机绝对路径：242、252、262、272、282；其他仓库地址或项目名（隐私属性待确认）：242、252、262、272、282 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/LIVE_SITE_PAGE_SUMMARY.json` | 其他仓库地址或项目名（隐私属性待确认）：2 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/PHASE_1_FREEZE.md` | 其他仓库地址或项目名（隐私属性待确认）：27 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/PLUGIN_CONSUMPTION_EVIDENCE.md` | 本机绝对路径：25–26、53；其他仓库地址或项目名（隐私属性待确认）：25–26 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/dom/zh-Hans_home.screenshot.log` | 其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/dom/zh-Hans_how-it-works.screenshot.log` | 其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/dom/zh-Hans_privacy.screenshot.log` | 其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/dom/zh-Hans_support.screenshot.log` | 其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/dom/zh-Hans_terms.screenshot.log` | 其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/dom/zh-Hant-HK_home.screenshot.log` | 其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/dom/zh-Hant-HK_how-it-works.screenshot.log` | 其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/dom/zh-Hant-HK_privacy.screenshot.log` | 其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/dom/zh-Hant-HK_support.screenshot.log` | 其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/dom/zh-Hant-HK_terms.screenshot.log` | 其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/plugin_replay_output/CANDIDATE_REPLAY_RUN.json` | 本机绝对路径：24、30、42、48、54–55；其他仓库地址或项目名（隐私属性待确认）：24、30、42、48 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/plugin_replay_output/child.stdout.jsonl` | 本机绝对路径：4–5、8–9、15–16、21–22；其他仓库地址或项目名（隐私属性待确认）：4–5、7–9、15–16、21–22 |
| `results/product-ui-copy--cross-plugin-production-integration/human_acceptance_cuhk_date/live_site/plugin_replay_output/plugin-add.json` | 本机绝对路径：4、12；其他仓库地址或项目名（隐私属性待确认）：4、12 |
| `results/repo--maintenance-board-issue-maturity/METADATA_AUDIT.json` | 本机绝对路径：2149；其他仓库地址或项目名（隐私属性待确认）：2149 |
| `results/repo--maintenance-board-issue-maturity/PRE_MIGRATION_ISSUE_METADATA.json` | 本机绝对路径：124、173、222、271、320、369、418、467、516、565、614、663、712、761、810、859、908、957、1006、1055、1104、1153、1202、1251、1300、1349、1398、1447、1496、1545、1594、1643、1692、1741、1790、1839、1888、1937、1986、2035、2084、2133、2182、2231、2280、2334、2388、2442、2491、2550、2604、2683、2737、2791、2860、2914、2963、3012、3061、3120、3179、3233、3282、3331、3380、3429、3478、3527、3576、3625、3674、3723、3772、3821、3870、3919、3972、4025、4078、4127、4176、4225、4278、4327、4376、4419、4433；其他仓库地址或项目名（隐私属性待确认）：124、173、222、271、320、369、418、467、516、565、614、663、712、761、810、859、908、957、1006、1055、1104、1153、1202、1251、1300、1349、1398、1447、1496、1545、1594、1643、1692、1741、1790、1839、1888、1937、1986、2035、2084、2133、2182、2231、2280、2334、2388、2442、2491、2550、2604、2683、2737、2791、2860、2914、2963、3012、3061、3120、3179、3233、3282、3331、3380、3429、3478、3527、3576、3625、3674、3723、3772、3821、3870、3919、3972、4025、4078、4127、4176、4225、4278、4327、4376、4419、4433 |
| `results/repo--maintenance-board-issue-maturity/STAGE_B_DUPLICATE_REPAIR_V0_4.json` | 本机绝对路径：205、239、273、307、341、375、409、443、477、511、545；其他仓库地址或项目名（隐私属性待确认）：205、239、273、307、341、375、409、443、477、511、545 |
| `results/repo--maintenance-board-issue-maturity/STAGE_B_RECOVERY_V0_4_POST_REMOVE_SNAPSHOT.json` | 本机绝对路径：17、62、107、152、197、242、287、332、377、422、467、512、557、602、835；其他仓库地址或项目名（隐私属性待确认）：17、62、107、152、197、242、287、332、377、422、467、512、557、602、835 |
| `results/repo--maintenance-board-issue-maturity/STAGE_B_RECOVERY_V0_4_POST_SETTLING_SNAPSHOT.json` | 本机绝对路径：17、62、107、152、197、242、287、332、377、422、467、512、557、602、835；其他仓库地址或项目名（隐私属性待确认）：17、62、107、152、197、242、287、332、377、422、467、512、557、602、835 |
| `results/repo--maintenance-board-issue-maturity/STAGE_B_RECOVERY_V0_4_PRE_DUPLICATE_SNAPSHOT.json` | 本机绝对路径：17、62、107、152、197、242、287、332、377、422、467、512、557、602、649、683、717、751、785、819、853、887、921、955、989、1022；其他仓库地址或项目名（隐私属性待确认）：17、62、107、152、197、242、287、332、377、422、467、512、557、602、649、683、717、751、785、819、853、887、921、955、989、1022 |
| `results/repo--maintenance-board-issue-maturity/STAGE_B_SENTINEL_52_PROBE_V0_4.json` | 本机绝对路径：18、63、108、153、198、243、288、333、378、423、468、513、558、603、835、906、951、996、1041、1086、1131、1176、1221、1266、1311、1356、1401、1446、1491、1724、1795、1840、1885、1930、1975、2020、2065、2110、2155、2200、2245、2290、2335、2380、2613、2686、2731、2776、2821、2866、2911、2956、3001、3046、3091、3136、3181、3226、3271、3504；其他仓库地址或项目名（隐私属性待确认）：18、63、108、153、198、243、288、333、378、423、468、513、558、603、835、906、951、996、1041、1086、1131、1176、1221、1266、1311、1356、1401、1446、1491、1724、1795、1840、1885、1930、1975、2020、2065、2110、2155、2200、2245、2290、2335、2380、2613、2686、2731、2776、2821、2866、2911、2956、3001、3046、3091、3136、3181、3226、3271、3504 |
| `results/repo--maintenance-board-lifecycle/CONSUMER_HANDOFFS.md` | 本机绝对路径：53、79 |
| `results/repo--maintenance-board-lifecycle/METADATA_AUDIT_CURRENT_2026-10-02.json` | 本机绝对路径：2149；其他仓库地址或项目名（隐私属性待确认）：2149 |
| `results/repo--maintenance-board-lifecycle/PROJECT_CONFIG_READBACK.md` | 本机绝对路径：14；其他仓库地址或项目名（隐私属性待确认）：14 |
| `results/repo--maintenance-board-lifecycle/PROJECT_SURFACE_READBACK_AFTER_UI_AND_BACKFILL.md` | 本机绝对路径：11；其他仓库地址或项目名（隐私属性待确认）：11 |
| `results/repository--formal-release-5.5.0/presentations/PRESENTATIONS_RELEASE_ACCEPTANCE.md` | 本机绝对路径：57 |
| `results/repository--formal-release-5.5.0/presentations/normal-entry/compile-status.json` | 本机绝对路径：8、10、13、18、23、28、33、39、54、56 |
| `results/repository--formal-release-5.5.0/presentations/normal-entry/deck-plan.yaml` | 本机绝对路径：33、44、55、66、77、88、99、110、121、132、148、170、180、202、212、234、244、266、276、298 |
| `results/repository--formal-release-5.5.0/presentations/normal-entry/dependency_probe.json` | 本机绝对路径：50、52、55、60、65、70、75、82；其他仓库地址或项目名（隐私属性待确认）：82 |
| `results/repository--formal-release-5.5.0/presentations/normal-entry/deterministic-qa.json` | 本机绝对路径：25 |
| `results/repository--formal-release-5.5.0/presentations/normal-entry/render-status.json` | 本机绝对路径：6、10、14、18、22 |
| `results/repository--formal-release-5.5.0/presentations/normal-entry/render_chinese_math_pdf_probe.json` | 本机绝对路径：4、8、10–15、17–24、27、69、102、107、112、117、122、127、132、137、142、147 |
| `results/repository--formal-release-5.5.0/presentations/normal-entry/rendered-review-input.json` | 本机绝对路径：23、45、67、89、111 |
| `results/repository--formal-release-5.5.0/presentations/normal-entry/replay-run.json` | 本机绝对路径：16、23、34、40、46–47 |
| `results/science-communication--project-thread-handoff-recovery/target-surface-acceptance.md` | DII 项目标识或研究记录：30；CARE 名称或数据相关描述（候选）：34 |
| `results/science-communication--project-thread-handoff/MANIFEST.md` | DII 项目标识或研究记录：66；其他仓库地址或项目名（隐私属性待确认）：66 |
| `results/science-communication--project-thread-handoff/result.md` | 其他仓库地址或项目名（隐私属性待确认）：83–84；DII 项目标识或研究记录：84、123；CARE 名称或数据相关描述（候选）：84 |
| `results/science-communication--project-thread-handoff/review.md` | DII 项目标识或研究记录：23 |
| `results/science-communication--project-thread-handoff/target-surface-acceptance.md` | DII 项目标识或研究记录：53 |
| `results/web-development--frontend-design-production-consolidation/final_candidate_identity.json` | 本机绝对路径：8、23；其他仓库地址或项目名（隐私属性待确认）：23 |
| `results/web-development--frontend-design-production-consolidation/replay/candidate_plugin_replay_run.json` | 本机绝对路径：9、16、19–20；其他仓库地址或项目名（隐私属性待确认）：9、16 |
| `results/web-development--frontend-design-production-consolidation/replay/candidate_plugin_replay_status.md` | 本机绝对路径：40；其他仓库地址或项目名（隐私属性待确认）：40 |
| `results/web-development--frontend-design-production-consolidation/replay/candidate_routing_decisions.md` | 本机绝对路径：5；其他仓库地址或项目名（隐私属性待确认）：5 |
| `results/web-development--frontend-design-production-consolidation/replay/candidate_source_evidence.json` | 本机绝对路径：4；其他仓库地址或项目名（隐私属性待确认）：4 |
| `results/web-development--frontend-design-production-consolidation/replay/real_project_replay_preflight.md` | 本机绝对路径：9、34、68；其他仓库地址或项目名（隐私属性待确认）：9、34、68 |
| `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_attribution.json` | 本机绝对路径：6、8–12、21、27、33、39、56、58–60、69、75、81、87、104、106–110、119、125、131、137、143、149、155、161；其他仓库地址或项目名（隐私属性待确认）：6、8–12、21、27、33、39、56、58–60、69、75、81、87、104、106–110、119、125、131、137、143、149、155、161 |
| `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_attribution.md` | 本机绝对路径：21、25–29、53–56、81、85–87、111–114、139、143–147、171–178；其他仓库地址或项目名（隐私属性待确认）：21、25–29、53–56、81、85–87、111–114、139、143–147、171–178 |
| `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_freeze_manifest.json` | 本机绝对路径：14、18、41、45、68、72；其他仓库地址或项目名（隐私属性待确认）：14、18、41、45、68、72 |
| `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_replay_run.json` | 本机绝对路径：9、16、19–20；其他仓库地址或项目名（隐私属性待确认）：9、16 |
| `results/web-development--frontend-design-production-consolidation/replay/real_project_replays/real_project_source_consumption.json` | 本机绝对路径：14、19–20、24、30、36、42、48、54、60、66、72、128、132、137、142、147、152、204、208、213、218、302、306、311、316、321、326；其他仓库地址或项目名（隐私属性待确认）：14、19–20、24、30、36、42、48、54、60、66、72、128、132、137、142、147、152、204、208、213、218、302、306、311、316、321、326 |
| `results/workflow-core--normal-entry-reliability/G1_G6_RESULT.md` | 本机绝对路径：31 |
| `results/workflow-core--normal-entry-reliability/G4_NORMAL_ENTRY_TRACE.md` | 本机绝对路径：39 |
| `results/workflow-core--normal-entry-reliability/G6_NORMAL_ENTRY_TRACE.md` | 本机绝对路径：33 |
| `results/workflow-core--normal-entry-reliability/G6_ROUTE_IDENTITY.md` | 本机绝对路径：13、16、24 |
| `results/workflow-core--normal-entry-reliability/g1_hard_negative_raw/child.stdout.jsonl` | 本机绝对路径：5–8 |
| `results/workflow-core--normal-entry-reliability/g1_hard_negative_raw/plugin-add.json` | 本机绝对路径：4、12 |
| `results/workflow-core--normal-entry-reliability/g1_hard_negative_raw/run.json` | 本机绝对路径：5–6、25、31、43、49、55–56 |
| `results/workflow-core--normal-entry-reliability/g1_positive_contextual_raw/child.stdout.jsonl` | 本机绝对路径：7–8 |
| `results/workflow-core--normal-entry-reliability/g1_positive_contextual_raw/plugin-add.json` | 本机绝对路径：4 |
| `results/workflow-core--normal-entry-reliability/g1_positive_contextual_raw/run.json` | 本机绝对路径：16、23、34、40、46–47 |
| `results/workflow-core--normal-entry-reliability/g1_positive_implicit_raw/child.stdout.jsonl` | 本机绝对路径：7–8、12–13、17、19–21 |
| `results/workflow-core--normal-entry-reliability/g1_positive_implicit_raw/plugin-add.json` | 本机绝对路径：4 |
| `results/workflow-core--normal-entry-reliability/g1_positive_implicit_raw/run.json` | 本机绝对路径：16、23、34、40、46–47 |
| `results/workflow-core--normal-entry-reliability/g1_simple_negative_raw/plugin-add.json` | 本机绝对路径：4 |
| `results/workflow-core--normal-entry-reliability/g1_simple_negative_raw/run.json` | 本机绝对路径：25、31、37–38 |
| `results/workflow-core--normal-entry-reliability/g4_absent_contrast_input.md` | 本机绝对路径：14、16 |
| `results/workflow-core--normal-entry-reliability/g4_absent_contrast_raw/child.stdout.jsonl` | 本机绝对路径：6–11、13–14、17–20 |
| `results/workflow-core--normal-entry-reliability/g4_absent_contrast_raw/plugin-add.json` | 本机绝对路径：4 |
| `results/workflow-core--normal-entry-reliability/g4_absent_contrast_raw/run.json` | 本机绝对路径：7–12、14–15、17–20、41、47、53–54、56 |
| `results/workflow-core--normal-entry-reliability/g4_absent_contrast_raw/workspace/inputs/01-g4_absent_contrast_input.md` | 本机绝对路径：14、16 |
| `results/workflow-core--normal-entry-reliability/g4_absent_contrast_raw/workspace/outputs/absent_probe/capability_report.json` | 本机绝对路径：5 |
| `results/workflow-core--normal-entry-reliability/g4_absent_contrast_raw/workspace/outputs/g4_absent_contrast_manifest.json` | 本机绝对路径：77、87、91、99、103 |
| `results/workflow-core--normal-entry-reliability/g4_candidate_replay_raw/child.stdout.jsonl` | 本机绝对路径：6–11、13–14 |
| `results/workflow-core--normal-entry-reliability/g4_candidate_replay_raw/plugin-add.json` | 本机绝对路径：4 |
| `results/workflow-core--normal-entry-reliability/g4_candidate_replay_raw/run.json` | 本机绝对路径：16、23、34、40、46–47 |
| `results/workflow-core--normal-entry-reliability/g4_candidate_replay_raw_v2/child.stdout.jsonl` | 本机绝对路径：6、8–10、12–23、25、27–28 |
| `results/workflow-core--normal-entry-reliability/g4_candidate_replay_raw_v2/g4_normal_entry_decision.md` | 本机绝对路径：9–10、17、27、31、34 |
| `results/workflow-core--normal-entry-reliability/g4_candidate_replay_raw_v2/g4_render_env.json` | 本机绝对路径：2、4–5、16、195–196、199–200、204–205、209–210、214–215、218–219、228、230、235、237、243–245、249–250、254–255、262、265、268、273、275–276、280–281、284–285、294、296、301、303、309–311、315–316、320–321、328、331、334、339、341–342、362–363 |
| `results/workflow-core--normal-entry-reliability/g4_candidate_replay_raw_v2/plugin-add.json` | 本机绝对路径：4 |
| `results/workflow-core--normal-entry-reliability/g4_candidate_replay_raw_v2/run.json` | 本机绝对路径：16、23、34、40、46–47 |
| `results/workflow-core--normal-entry-reliability/g4_capability_discovery_input_v2.md` | 本机绝对路径：13、15 |
| `results/workflow-core--normal-entry-reliability/g6_candidate_replay_raw/child.stdout.jsonl` | 本机绝对路径：5–6、10–11 |
| `results/workflow-core--normal-entry-reliability/g6_candidate_replay_raw/g6_normal_entry_decision.md` | 本机绝对路径：6 |
| `results/workflow-core--normal-entry-reliability/g6_candidate_replay_raw/plugin-add.json` | 本机绝对路径：4 |
| `results/workflow-core--normal-entry-reliability/g6_candidate_replay_raw/run.json` | 本机绝对路径：16、23、34、40、46–47 |
| `results/workflow-core--normal-entry-reliability/g6_candidate_replay_raw_v4/child.stdout.jsonl` | 本机绝对路径：6–12、16–17、19、21 |
| `results/workflow-core--normal-entry-reliability/g6_candidate_replay_raw_v4/plugin-add.json` | 本机绝对路径：4 |
| `results/workflow-core--normal-entry-reliability/g6_candidate_replay_raw_v4/run.json` | 本机绝对路径：7–12、15–16、59、65、71–72 |
| `results/workflow-core--normal-entry-reliability/g6_candidate_replay_raw_v4/workspace/inputs/01-g6_publication_boundary_input_v3.md` | 本机绝对路径：5 |
| `results/workflow-core--normal-entry-reliability/g6_publication_boundary_input_v3.md` | 本机绝对路径：5 |
| `results/workflow-core--normal-entry-reliability/qualification_candidate_replay_raw/child.stdout.jsonl` | 本机绝对路径：7–8 |
| `results/workflow-core--normal-entry-reliability/qualification_candidate_replay_raw/plugin-add.json` | 本机绝对路径：4 |
| `results/workflow-core--normal-entry-reliability/qualification_candidate_replay_raw/run.json` | 本机绝对路径：16、23、34、40、46–47 |
| `results/workflow-core--reviewed-first-bootstrap-normal-entry/FB_GATES.md` | 其他仓库地址或项目名（隐私属性待确认）：5、7；本机绝对路径：7、22–23、25 |
| `results/workflow-core--reviewed-first-bootstrap-normal-entry/RESULT.md` | 本机绝对路径：34 |
| `scripts/audit_skill_runtime_text.py` | MoSAiC 名称（候选）：13 |
| `shared/reference-packs/frontend-ui-ux/ui-ux-pro-max-data/_sync_all.py` | CARE 名称或数据相关描述（候选）：152 |
| `shared/reference-packs/frontend-ui-ux/ui-ux-pro-max-data/colors.csv` | CARE 名称或数据相关描述（候选）：58、135 |
| `shared/reference-packs/frontend-ui-ux/ui-ux-pro-max-data/google-fonts.csv` | MoSAiC 名称（候选）：1305 |
| `shared/reference-packs/frontend-ui-ux/ui-ux-pro-max-data/products.csv` | CARE 名称或数据相关描述（候选）：58、63、135 |
| `shared/reference-packs/frontend-ui-ux/ui-ux-pro-max-data/stacks/laravel.csv` | 本机绝对路径：39 |
| `shared/reference-packs/frontend-ui-ux/ui-ux-pro-max-data/stacks/nextjs.csv` | 本机绝对路径：29 |
| `shared/reference-packs/frontend-ui-ux/ui-ux-pro-max-data/styles.csv` | CARE 名称或数据相关描述（候选）：81 |
| `shared/reference-packs/frontend-ui-ux/ui-ux-pro-max-data/ui-reasoning.csv` | CARE 名称或数据相关描述（候选）：58、63、135 |
| `site-profiles/local-overrides.example.toml` | 本机绝对路径：19；其他仓库地址或项目名（隐私属性待确认）：19 |
| `skills/README.md` | 其他仓库地址或项目名（隐私属性待确认）：11、39 |
| `skills/archive/documents-media/pptx/scripts/office/schemas/ISO-IEC29500-4_2016/wml.xsd` | MoSAiC 名称（候选）：344 |
| `skills/core/codex-system/bridge-kit-maintainer/SKILL.md` | 其他仓库地址或项目名（隐私属性待确认）：66、82 |
| `skills/core/codex-system/bridge-kit-maintainer/references/bridge-release-channel.md` | 其他仓库地址或项目名（隐私属性待确认）：35 |
| `skills/core/codex-system/machine-update-orchestrator/references/formal-release-and-update-impact.md` | 其他仓库地址或项目名（隐私属性待确认）：3 |
| `skills/core/codex-system/mcp-builder/SKILL.md` | CARE 名称或数据相关描述（候选）：187 |
| `skills/core/codex-system/mcp-builder/reference/evaluation.md` | CARE 名称或数据相关描述（候选）：90 |
| `skills/core/codex-system/mcp-builder/reference/node_mcp_server.md` | 本机绝对路径：516、522 |
| `skills/core/codex-system/project-skill-installer/SKILL.md` | 本机绝对路径：41；其他仓库地址或项目名（隐私属性待确认）：66 |
| `skills/core/codex-system/system-skills/imagegen/references/codex-network.md` | CARE 名称或数据相关描述（候选）：30 |
| `skills/core/codex-system/system-skills/skill-creator/SKILL.md` | 本机绝对路径：318 |
| `skills/domains/bayesian/bayesian-ppl-diagnostics/SKILL.md` | 其他仓库地址或项目名（隐私属性待确认）：18 |
| `skills/domains/bayesian/bayesian-ppl-diagnostics/references/reference.md` | 本机绝对路径：20 |
| `skills/domains/bioinformatics/gtex-database/SKILL.md` | 本机绝对路径：28–29、323 |
| `skills/domains/medical-imaging/cardiac-mri/SKILL.md` | 其他仓库地址或项目名（隐私属性待确认）：25 |
| `skills/domains/medical-imaging/cardiac-mri/evals/trigger_queries.json` | 其他仓库地址或项目名（隐私属性待确认）：12–13、21 |
| `skills/domains/medical-imaging/medical-imaging-classical-features/SKILL.md` | 其他仓库地址或项目名（隐私属性待确认）：18 |
| `skills/domains/medicine-clinical/clinical-decision-support/SKILL.md` | CARE 名称或数据相关描述（候选）：3、25 |
| `skills/domains/medicine-clinical/clinical-decision-support/references/evidence-checklist.md` | CARE 名称或数据相关描述（候选）：6 |
| `skills/domains/medicine-clinical/clinical-decision-support/references/legacy-full-skill.md` | CARE 名称或数据相关描述（候选）：110、324–325、327–328、333 |
| `skills/domains/medicine-clinical/clinical-reports/SKILL.md` | CARE 名称或数据相关描述（候选）：31、40 |
| `skills/domains/medicine-clinical/clinical-reports/references/clinical-report-checklist.md` | CARE 名称或数据相关描述（候选）：5 |
| `skills/domains/medicine-clinical/clinical-reports/references/legacy-full-skill.md` | CARE 名称或数据相关描述（候选）：3、30、85、87、177、607、673、745、801–802、923、988、1050、1061、1076、1138 |
| `skills/domains/medicine-clinical/medical-literature-evidence-review/SKILL.md` | CARE 名称或数据相关描述（候选）：3 |
| `skills/domains/medicine-clinical/pyhealth/SKILL.md` | CARE 名称或数据相关描述（候选）：236 |
| `skills/domains/medicine-clinical/treatment-plans/references/legacy-full-skill.md` | CARE 名称或数据相关描述（候选）：3、23、26、35、39、42、51、73、104、129、239、260、273、277、342、392、581、597–598、600、606、608、619、621、642、646、745、758、780、782–783、805、809、888、904、1019、1034、1085、1291、1499–1500 |
| `skills/science/communication/project-thread-handoff/evals/trigger_queries.json` | DII 项目标识或研究记录：4 |
| `skills/tools/documents-media/docx/scripts/office/schemas/ISO-IEC29500-4_2016/wml.xsd` | MoSAiC 名称（候选）：344 |
| `skills/tools/documents-media/presentations/research-presentations/SKILL.md` | 本机绝对路径：69；其他仓库地址或项目名（隐私属性待确认）：69 |
| `skills/tools/documents-media/presentations/shared/compatibility/openai-latex.md` | 本机绝对路径：17；其他仓库地址或项目名（隐私属性待确认）：17 |
| `skills/tools/documents-media/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py` | 本机绝对路径：31；其他仓库地址或项目名（隐私属性待确认）：31 |
| `skills/tools/documents-media/xlsx/scripts/office/schemas/ISO-IEC29500-4_2016/wml.xsd` | MoSAiC 名称（候选）：344 |
| `skills/tools/frontend/brand-creative-assets/references/messaging-framework.md` | CARE 名称或数据相关描述（候选）：84 |
| `skills/tools/frontend/implementation-react-tailwind/references/canvas-design-system.md` | CARE 名称或数据相关描述（候选）：59 |
| `skills/tools/visualization/canvas-design/SKILL.md` | CARE 名称或数据相关描述（候选）：76、94、125 |
| `skills/tools/visualization/matplotlib/SKILL.md` | MoSAiC 名称（候选）：124 |
| `skills/writing/core/chinese-prose/TODO.md` | CARE 名称或数据相关描述（候选）：9 |
| `skills/writing/research/academic-paper-writer-pro/docx/scripts/office/schemas/ISO-IEC29500-4_2016/wml.xsd` | MoSAiC 名称（候选）：344 |
| `skills/writing/research/literature-review/SKILL.md` | CARE 名称或数据相关描述（候选）：77 |
| `skills/writing/research/scientific-writing/SKILL.md` | CARE 名称或数据相关描述（候选）：166 |
| `skills/writing/research/shared/student-assessment-end-to-end-pre-execution-runbook.md` | 本机绝对路径：1150 |
| `tests/fixtures/056_product_delivery_discipline_gates.json` | 其他仓库地址或项目名（隐私属性待确认）：8 |
| `tests/fixtures/presentations/research_group_meeting/build_visual_review_pages.py` | CARE 名称或数据相关描述（候选）：114 |
| `tests/fixtures/presentations/research_group_meeting/generate_research_group_meeting_regression.py` | CARE 名称或数据相关描述（候选）：481、579 |
| `tests/fixtures/presentations/research_group_meeting/visual_review_packet_source/EVIDENCE_MANIFEST.json` | CARE 名称或数据相关描述（候选）：4、82、164、251、340 |
| `tests/fixtures/presentations/research_group_meeting/visual_review_packet_source/MECHANICAL_VISUAL_REVIEW.json` | CARE 名称或数据相关描述（候选）：81、127、174、220、223 |
| `tests/fixtures/presentations/statistical_method_group_meeting/generate_statistical_method_group_meeting_benchmark.py` | CARE 名称或数据相关描述（候选）：867、1027 |
| `tests/fixtures/presentations/statistical_method_group_meeting/visual_review_packet_source/EVIDENCE_MANIFEST.json` | CARE 名称或数据相关描述（候选）：5、707、913、1122、1326、1532 |
| `tests/fixtures/presentations/statistical_method_group_meeting/visual_review_packet_source/MECHANICAL_VISUAL_REVIEW.json` | CARE 名称或数据相关描述（候选）：84、130、176、222、267、270 |
| `tests/fixtures/project_thread_handoff/g3_regressions.json` | 其他仓库地址或项目名（隐私属性待确认）：14 |
| `tests/test_codex_marketplace.py` | 其他仓库地址或项目名（隐私属性待确认）：502、505–507、529 |
| `tests/test_project_thread_handoff_contract.py` | 其他仓库地址或项目名（隐私属性待确认）：169、183；DII 项目标识或研究记录：180；CARE 名称或数据相关描述（候选）：181 |
| `tests/test_render_chinese_math_pdf.py` | 其他仓库地址或项目名（隐私属性待确认）：64 |
| `tests/test_scientific_rewrite.py` | CARE 名称或数据相关描述（候选）：56–57、81、83、88、129、153、168–169、177、611–612 |
| `tests/test_slurm_workflows.py` | 实验室标识：81 |

本轮交付停在工作树修改与验证。42 份例外未处理前，不能宣称整个公开仓库已彻底清零；Git 历史清理、提交和推送由协调者另行处理。

## 协调者补充（2026-11-11）

上文留给协调者的 42 份构建记录与字体配置，只含同一个本机字体目录路径。协调者已把它统一替换为 `<local-font-dir>`。替换后全部 406 项测试通过，`build_codex_marketplace.py --validate --check` 通过，当前工作树中目标名称为零。被清除内容的原文已存入该私有项目自己的仓库，本公开仓库不保存。
