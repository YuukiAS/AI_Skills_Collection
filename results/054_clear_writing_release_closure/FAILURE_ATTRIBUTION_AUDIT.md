# 054 Clear Writing Failure Attribution Audit

054 不能在当前冻结合同下合法转成 release PASS：唯一授权的最终 Terra review 已经消费且返回 `REVISE`，fresh batch 已经被评审，不能通过改写历史 evidence、追加 H4、重跑 fresh、增加第二次 Terra 或弱化 canonical Goal 来补 PASS。这个结论只说明 054 本轮 release closure 已经终止，不等于 051-054 的 Clear Writing 架构必须推倒。

本次归因结论是：F1/F2 暴露了部分真实的读者成稿质量与 pre-Terra 质检缺口；F3 主要是 Terra rubric 把合法读者代码示例误判成 raw source code；F4 是源文本外部事实质量问题与 reviewer 越界的混合，而不是 candidate 在重写中新增或加强错误归因。后续若仍要 release，应走 successor product-repair 合同，重点收紧 repo-local qualitative critic，而不是重做 heavy rewrite 架构或修改 Bridge Kit。

## 证据范围

已按 critic contract 读取并核对：

- 054 canonical Goal、frozen Plan、CURRENT、paid review policy、FINAL_REPORT 和 Terra `TEXT_REVIEW.json`。
- repo-local private Deep Research source/task/final Markdown/PDF text extraction：`private/exports/054_clear_writing_release_closure/inputs/source_extracted_layout.txt`、`inputs/K3_054_REWRITE_TASK.md`、`deep_research_attempt1/Clear_Writing_Deep_Research_Final.md`、`.txt` 及对应 audits。
- Deep Research intermediate evidence：`.local-runtime/candidate-plugin-replay/runs/20260913T041508Z-2639148/workspace/outputs/.evidence/meaning_map.json`、`reader_plan.json`、`semantic_audit.json`、`final_candidate.md`。
- H1/H2/H3 frozen TASK/source/final/local audit/stage semantic audit under `results/054_clear_writing_release_closure/fresh_holdouts/`。
- current Clear Writing source for contract understanding only: `skills/writing/core/scientific-rewrite/SKILL.md`、`skills/writing/core/chinese-prose/SKILL.md`、`skills/writing/core/writing-fidelity/SKILL.md`。未修改这些文件。

## Legality

054 Goal and Plan froze exactly one final Terra Text Review, exactly three fresh holdouts, no H4/replacement, no second Terra, no Bridge Kit change, and no mutation of historical review evidence. `CURRENT.json` records that the single Terra review returned `REVISE`, consumed one paid call, and moved 054 to `AWAIT_HUMAN_DECISION`. The critic contract further states that an existing paid-review campaign cannot be enlarged in place and a Plan revision cannot weaken the canonical Goal.

Therefore there is no repository-supported legal path for 054 itself to become release PASS without mutating the frozen paid/fresh contract or rewriting review history.

## F1: Deep Research still reads like research memo / execution plan

Terra finding F1 cited phrases such as "下一轮最小实验", "本项目未验证", and "下载后应先建立", under requirement `R6_无工作流或来源过程框架`.

Source trace:

- The raw Deep Research source is itself a project-facing scientific audit and next-experiment decision document. It contains a "下一轮最小实验" section, method-status caveats equivalent to "本项目未验证", and M&Ms manifest instructions before training.
- The frozen Deep Research TASK required a finished Simplified Chinese document for a mentor/professional reader, but also required preserving facts, methods, datasets, metrics, limitations, uncertainties, and GO/STOP boundaries. It explicitly forbade workflow/repository/candidate/process metadata, not legitimate scientific future-work or experiment-boundary content.
- The Reader Plan created a dedicated `experiment` bundle: "如何用最小实验分清机制与资源？" and a `data` bundle for M&Ms provenance and initialization. The semantic audit passed because it treated GO/STOP, independent initialization, method limitations, and M&Ms verification conditions as substantive scientific boundaries.
- The final candidate preserved and reorganized the content rather than introducing it: it includes a "下一轮最小实验：三种聚合机制与局部漂移" section, method entries noting public code but no local validation, and a M&Ms manifest step before training.

Attribution:

The challenged material is not merely source packaging or workflow metadata. Much of it is legitimate future-work / research-plan content that a mentor-facing research decision report needs: which baselines to run, what uncertainty remains, and what data manifest must exist before claims are made. Removing it wholesale would violate the frozen task's GO/STOP and limitation-preservation requirements.

However, F1 is not pure Terra overreach. The final candidate still keeps the report's next-experiment framing in the main narrative, and the pre-Terra QA did not independently ask whether this was now a polished finished document or still too close to a campaign memo. The local semantic audit was mostly fidelity-oriented and self-certified by the host model; it did not provide an independent whole-document reader-quality judgment.

Classification: `MIXED` = `TRUE_CLEAR_WRITING_PRODUCT_DEFECT` + `CONTRACT_AMBIGUITY` + `PRE_TERRA_QUALITATIVE_QA_FALSE_PASS`.

Product repair needed: partial. Clear Writing should better distinguish "reader-useful future-work section" from "execution-plan voice" in mentor/professional reports, without deleting scientific decision boundaries.

## F2: Deep Research internal paths and file references

Terra finding F2 cited `Dataset501_CAREMyoPS/.../fold_0/checkpoint_best.pth` and `mms_data_contract.md`, under requirement `R3_无不必要来源元数据或原始平台标记`.

Source trace:

- The raw source uses the CARE checkpoint path and fold split to support a central scientific conclusion: the current experiment is better interpreted as same-domain/same-cohort federated re-adaptation rather than federation replacing never-centralized training.
- The raw source also uses `mms_data_contract.md` to describe a conservative data-contract check before M&Ms training.
- The Deep Research TASK explicitly allowed formal method/model/dataset/metric/code/path/citation acronym preservation when needed, and warned not to delete necessary reproduction information, technical identities, limitations, or evidence.
- The current Clear Writing source says paths, commands, config keys, code identifiers, and reproduction tokens remain reader-facing when they support technical identity or reproducibility. It also distinguishes task-local workflow paths from scientific reproduction details.
- The semantic audit explicitly excluded internal repository/control-process narrative "with scientific limitations and necessary checkpoint/data paths retained."

Attribution:

The checkpoint path is not merely arbitrary internal metadata: it is evidence for fold/provenance and directly supports the source's estimand limitation. Preserving it, or at least a concise version of it, is contract-supported. `mms_data_contract.md` is more ambiguous: it points to project-local data-contract machinery, but the surrounding paragraph uses it to prevent overclaiming M&Ms metadata before official download verification. A reader-facing version could probably say "当前数据契约" or move the literal file name to a technical note, but deleting the underlying constraint would damage fidelity.

Terra correctly identified a reader-relevance risk, but its finding overstates the case by treating all internal-looking file names as reader-irrelevant source metadata. The frozen contract did not ban all paths; it banned unnecessary source/platform/process metadata.

Classification: `MIXED` = `CONTRACT_AMBIGUITY` + `PRE_TERRA_QUALITATIVE_QA_FALSE_PASS` + limited `TRUE_CLEAR_WRITING_PRODUCT_DEFECT`, with reviewer overreach on the checkpoint example.

Product repair needed: partial. The product should classify scientific provenance paths as inline-critical, relocatable trace, or internal workflow trace, and should avoid leaving project-local filenames in the main prose when a human-readable formulation preserves the same constraint.

## F3: H1 Python code blocks

Terra finding F3 rejected the H1 Feature hashing output because it contained Python fenced blocks such as `def token_features(...)`, under `R4_无原始源代码或平台标记`.

Source trace:

- H1 TASK required preserving `FeatureHasher`, `MurmurHash3`, `signed 32-bit variant`, `alternate_sign`, `scipy.sparse`, `HashingVectorizer`, core use, input/output, benefits, limitations, and attribution. It asked to clean RST/source wrappers such as anchors, `:class:`, `:ref:`, rubric, prompts, and duplicate navigation references.
- H1 source includes the Python generator and `FeatureHasher.transform` usage examples as the substantive explanation of how the API is used.
- The final candidate keeps two Python code examples as reader-facing examples and removes the RST wrappers. H1 local audit explicitly passed them: "Python API/code examples are required technical content; no formula-like text/plain fence is present."
- The 054 Goal/Plan protects reader-useful code/path/config/command when needed for understanding or reproducibility. The final Terra rubric prohibited raw source/platform markup and formula text fences; it did not explicitly prohibit legitimate code examples in a technical API explanation.

Attribution:

The code examples were necessary or at least helpful to explain `FeatureHasher` input and use. The frozen task did not prohibit them. A blanket no-code rule would conflict with the Goal's protection for reader-useful code/path/config/command. Terra appears to have collapsed "raw source/platform markup" and "legitimate reader-facing Python examples" into one category.

Classification: `REVIEW_RUBRIC_OVERREACH`.

Product repair needed: no for this item. A future evaluator should distinguish raw source scaffolding from legitimate code examples.

## F4: H3 2015 deep-learning attribution

Terra finding F4 rejected the H3 neural-network output for the claim that in 2015 LeCun, Bengio and Hinton formally proposed the concept of deep learning.

Source trace:

- The tracked H3 source itself states that after AlexNet, "LeCun、Bengio和Hinton在2015年正式提出深度学习的概念".
- H3 TASK required preserving the thread about common neural networks and the origin of deep learning, plus formulas, conditions, references, and attribution.
- The final candidate faithfully preserves the same 2015 attribution in clearer prose. It does not materially introduce the claim, reassign it to new people, or strengthen it beyond the source.
- H3 semantic audit explicitly says "不作外部历史核查；网络深度效果与历史叙述沿既有论述范围重组."

Attribution:

The challenged statement is likely externally wrong or misleading, but it is a source-quality issue under the default source-faithful rewrite contract. Clear Writing was not silently authorized to perform external historical/citation fact-checking, and the frozen task prioritized preserving source attribution rather than correcting it from outside knowledge. Terra used a real factual concern, but applied an external factual-truth requirement that the product contract had not made part of the rewrite task.

Classification: `MIXED` = `SOURCE_QUALITY_ISSUE_OUTSIDE_DEFAULT_REWRITE_SCOPE` + `REVIEW_RUBRIC_OVERREACH`.

Product repair needed: no default production rewrite change for this item. A successor evaluation contract may add an explicit source-quality/fact-check preflight for public educational material, but that is a different capability boundary from source-faithful Clear Writing.

## Pre-Terra QA attribution

054 could record known/stress, Deep Research, and fresh local evidence as PASS because the local gates mainly proved mechanical and fidelity properties:

- Markdown/PDF audits checked code fences, formula fences, raw markup, table shape, source-process strings, workflow leakage, and ordinary internal English counts.
- Semantic audits checked proposition preservation against Meaning Map / Reader Plan, not whether the Meaning Map had selected the best reader-facing content.
- Deep Research semantic audit was `host_codex_self_check` with `independent_review=false`, so the same reasoning system that generated the candidate effectively certified its qualitative reader suitability.
- H1 local audit had a deliberate code-fence allowance; Terra later applied a broader interpretation.
- H3 local semantic audit explicitly chose no external historical fact-checking; Terra later applied an external factual truth bar.

The gap is therefore not "add more keyword tests." The observed failures would be prevented by a zero-paid repo-local critic checkpoint that reads the whole artifact before irreversible fresh/final paid gates and answers: whether the planned reviewer rubric matches the product contract; whether code/path/future-work/fact-check requirements are explicit; whether local qualitative QA is independent enough; and whether the campaign leaves a legal recovery path after final paid review.

## Architecture decision

The evidence does not show that Meaning Map, Reader Plan, REALIZE_MEANING, or fidelity ownership is inherently wrong. The strongest product issues are narrower: insufficient qualitative reader-facing review for F1/F2, ambiguous treatment of project-local scientific traces, and evaluator/rubric mismatch for F3/F4. The architecture should be kept and hardened.

Decision: `ARCHITECTURE_KEEP_AND_HARDEN`.

## Successor scope

Because 054 itself cannot legally become PASS, any future release validation needs a successor contract. The successor should not start by drafting new holdouts or authorizing paid review. It should first repair the product/evaluation boundary exposed here:

- bounded product repair for F1/F2: future-work/research-plan framing and path/file-name placement in finished reader documents;
- corrected evaluation rubric: distinguish source-faithful rewrite from external fact-checking, and distinguish raw source markup from legitimate code examples;
- zero-paid independent repo-local critic before fresh freeze/final Terra.

This is a `SUCCESSOR_PRODUCT_REPAIR`, not `SUCCESSOR_ARCHITECTURE_REDESIGN`.

## Bridge Kit

No Bridge Kit change is justified. The failure is specific to AI_Skills Clear Writing release evaluation, repo-local QA, and frozen campaign design. Bridge Kit Text Review delivered the Terra evidence; the issue is how AI_Skills used and staged that evidence.

054_RELEASE_PASS_STILL_LEGAL=NO
F1_CLASSIFICATION=MIXED
F2_CLASSIFICATION=MIXED
F3_CLASSIFICATION=REVIEW_RUBRIC_OVERREACH
F4_CLASSIFICATION=MIXED
PRODUCT_REPAIR_NEEDED=PARTIAL
EVALUATION_CONTRACT_DEFECT=YES
PRE_TERRA_QUALITATIVE_QA_GAP=YES
ARCHITECTURE_DECISION=ARCHITECTURE_KEEP_AND_HARDEN
SUCCESSOR_TYPE=SUCCESSOR_PRODUCT_REPAIR
RECOMMEND_REPO_LOCAL_CRITIC_CHECKPOINT=YES
NEED_BRIDGE_KIT_CHANGE=NO
AUDIT_COMMIT=TO_BE_REPORTED_AFTER_COMMIT
