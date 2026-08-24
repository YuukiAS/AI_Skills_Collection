---
schema: AI_BRIDGE_REVIEWED_REQUEST_V1
task_key: 027_research_presentation_executable_cuhk_scientific_layout_system
---

# 027 Executable CUHK Scientific Layout System — Request

## Why this task exists

Stage 1 已把普通科研组会默认 production route 切到 canonical exact CUHK Beamer；Stage 2 已建立并验证 production gold composition library，当前 gold records 有真实 rendered-pixel mature-bar evidence、语义兼容 selector、renderer-neutral composition recipe，并覆盖主要 scientific jobs，包括 discussion / next experiment。

但 Stage 2 的 recipe 目前仍只是 renderer-neutral constraints。系统尚未证明这些 source-derived geometry / hierarchy / reading-flow / panel relations 可以稳定落成 **exact CUHK Beamer content area 内的 native scientific layouts**。如果直接进入普通 one-call production entry，模型仍可能在最后一步重新自由画布局、退回 generic cards/box-arrow、缩小真实 figure，或仅把 gold record 当 provenance 而没有真正改变 TeX 页面。

## Product outcome

本任务完成后，应存在一个可复用的 Stage 3 scientific-layout layer：正常 Stage 2 selector / recipe 产生的 composition constraints 可以被映射到 canonical CUHK Beamer 的安全内容区，并生成可编译的 native LaTeX / TikZ / figure / image-panel frame content。

该层至少要覆盖最终真实 holdout 会需要的主要页面类型：

- equation / statistical model / theorem / proof-intuition；
- quantitative result / uncertainty / comparison；
- method / experiment design；
- negative result / failure / model check；
- medical-image aligned comparison / overlay / error / zoom；
- discussion / next experiment。

目标不是做一个新的万能模板，而是让不同 scientific jobs 在 exact CUHK identity 下继续保留各自不同、由 gold composition 约束的页面几何与科学对象层级。

## Scope

本任务只允许：

- 复用 Stage 2 现有 gold selector / recipe builder，不创建第二套 reference/gold 体系；
- 建立从 renderer-neutral recipe 到 CUHK content-space 的确定性映射与兼容性校验；
- 增加可复用 native LaTeX/TikZ/figure/image scientific layout primitives / macros / adapters；
- 用有界的非 holdout scientific fixtures / existing regression assets 生成 Stage 3 integration deck，证明上述主要 page jobs 都能真实编译和渲染；
- 保存每页 `selected gold -> recipe -> resolved CUHK layout -> emitted TeX objects` 的 trace；
- 对真实 rendered pages 做机械 QA 与当前 gpt-5.6-terra item/page-level visual review，必要时使用已验证的 gold reference pixels 做匿名相对成熟度校准；
- 增加 deterministic tests / validation / source-plugin mirror。

本任务不允许：

- 改写 Stage 2 gold admission / Terra history 或为了布局方便降低 gold mature bar；
- 使用 donor slide pixels、logo、branding 或许可受限 figure 作为 runtime layout asset；
- 用 derived CUHK PPTX、design-tokens 或 023 renderer 模拟 exact CUHK；
- 把所有 scientific jobs 压成同一个 card/dashboard/box-arrow layout；
- 把公式 rasterize 成图片或把公式源码字符串直接当 audience text；
- 接入普通 `research-presentations` one-call production entry、自动 source ingestion、deck-level repair loop；这些属于 Stage 4；
- 使用最终 Stage 5 holdout paper 或任何 holdout-specific hardcode；
- 宣告 `ONE_SHOT_QUALITY_PASS` 或 `PROGRAM_MATURE`。

027 PASS 只表示 Stage 3 的可执行布局层成立。之后 Planner 才可创建 Stage 4 — One-Call Production Entry + Bounded Quality Loop。
