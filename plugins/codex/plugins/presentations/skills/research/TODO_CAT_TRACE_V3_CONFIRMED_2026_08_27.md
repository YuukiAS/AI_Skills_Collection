# CAT-TRACE v3 confirmed presentation-rule updates — 2026-08-27

本文件记录 v3 第一轮审阅后用户已经确认、可继续进入 v4 执行的通用规则增量。它修正 `TODO_CAT_TRACE_V3_MANDATORY_CANDIDATES_2026_08_27.md` 中仍待讨论的部分，并由 `CURRENT_RESEARCH_PRESENTATION_REVISION_RULES.md` 汇总。

## 1. Theory framing：按模型解决的问题组织，不按 formal type 组织

上一版候选里“必须给 Theorem / Corollary / Proposition 编号并与 manuscript 对齐”的要求取消。

新的确认规则：

- [CONFIRMED] Theory 主线先列 proposed model 相比 closest baselines 新解决的正式问题，再选择支撑这些能力的 formal guarantees。
- [CONFIRMED] Audience-facing slide title 不应机械使用 `Theorem`, `Corollary`, `Proposition` 作为主要叙事标签；否则容易让听众把注意力放在 formal taxonomy 和“有几个 theorem”上，而不是模型价值。
- [CONFIRMED] 不为了显得理论多，把 corollary、definition、estimand decomposition 人为升级为 theorem；也不因为它在 manuscript 中叫 corollary 就弱化它对模型闭环的必要性。
- [CONFIRMED] Slide title 应优先写成 claim / guarantee，例如：`Group marks preserve open-tail richness calibration`、`Catalogue and open-tail richness remain finite together`、`Residual dependence preserves marginal probit interpretation`。
- [CONFIRMED] manuscript 的 formal 类型、编号和 proof 状态可以留在 speaker/source notes；只有编号本身对现场讨论有帮助时才放主 slide。
- [CONFIRMED] 每个 formal guarantee 都必须回答：它防止什么失败、为什么 CAT-TRACE 需要它、TRACE/HMSC/固定列表模型为什么没有同时解决这个问题。

## 2. v4 theory 的 CAT-TRACE 项目级应用

下面是项目级决定，不直接泛化成所有 presentation 的固定三页模板：

1. **Group marks preserve open-tail richness calibration**：把 TRACE 的单一匿名 tail 分成多个 biologically marked groups 后，每组 expected richness 仍保持有限并随 covariates 变化。
2. **Catalogue and open tail remain compatible in total richness**：有限 catalogue 与有限个 marked open tails 可以共同形成 finite expected local richness，并保留 TRACE 的单-tail special case。
3. **Residual dependence preserves marginal probit interpretation**：加入 normalized residual factor-copula 后，joint dependence 改变但 marginal occurrence probability 不变，因此不破坏 richness calibration 所依赖的边际解释。

`Delta^K + Delta^U` 继续作为重要 estimand decomposition，不包装成深 theorem。

当前 v4 不放 proof slide；proof 完整后再根据现场需要决定是否增加。

## 3. 其余 v3 第一轮意见

用户确认上一轮逐页审阅中除 theory 编号建议外，其余修改方向均可进入 v4。特别是以下重复失败继续作为 hard regression：

- overlay / diagram geometry / arrow size；
- 大量空白但核心内容仍小；
- repo path / audit / manuscript draft 等内部语言；
- figure-heavy slide 主图过小；
- metric direction 使用 `lower/higher` 冗余列；
- simulation 同类页 Question / Design / Metrics / Baselines 格式不闭合；
- references 字号未根据引用数量主动放大。
