# 017 Medical-Imaging Research Group Meeting Benchmark — Request

## 背景

Phase C 的 statistical / biostatistical benchmark 已在用户质量纠偏后完成成熟度重构，并通过最终 Terra 视觉证据与真实 GitHub CI。当前 improvement cycle 仍缺少医学影像场景的独立 benchmark。

医学影像页不能只把 image / GT / prediction / overlay 塞进框里，也不能退化成 pastel cards、咨询 dashboard 或内部 QA fixture。真实组会需要让听众在几秒内看清模态、解剖/病灶、预测差异、定量 endpoint 与失败机制；图像本身应成为视觉中心，annotation / legend 必须直接服务于科研解释。

## 目标

建立一个 public-safe、真实可编辑并真实渲染的 5 页医学影像研究组会 benchmark。使用固定随机种子的 synthetic cardiac-MR-like lesion-segmentation story，检验 Presentation 系统是否能成熟表达：

1. imaging task / anatomy / endpoint；
2. experiment design / evaluation flow；
3. quantitative multi-center result + uncertainty；
4. same-case image / GT / prediction / overlay failure analysis；
5. endpoint disagreement / negative result + next validation experiment。

所有图像、mask、prediction 与数值必须由 deterministic script 实际生成；不得使用私有 patient image，不得把 synthetic benchmark 说成临床验证或真实算法论文结果。

## 质量标准

视觉完成度至少达到成熟 MICCAI / RSNA 风格研究汇报或强 PI 组会可直接投影的专业水平，同时保留组会需要的技术信息。必须真正使用现有 inspected medical-imaging reference pages 的 page-specific lessons；reference IDs / retrieval trace 只能存在于内部 evidence，不得进入 audience-facing slide。

本任务完成前，不启动新的 source acquisition，不做长期 `PROGRAM_MATURE` 判断，也不发布新的 Presentation plugin 版本。
