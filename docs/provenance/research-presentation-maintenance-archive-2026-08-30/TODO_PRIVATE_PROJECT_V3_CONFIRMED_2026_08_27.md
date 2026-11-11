# a private research project v3 confirmed presentation-rule updates — 2026-08-27

本文件记录 v3 第一轮审阅后用户已经确认、可继续进入 v4 执行的通用规则增量。它修正 `TODO_PRIVATE_PROJECT_V3_MANDATORY_CANDIDATES_2026_08_27.md` 中仍待讨论的部分，并由 `CURRENT_RESEARCH_PRESENTATION_REVISION_RULES.md` 汇总。

## 1. Theory framing：按模型解决的问题组织，不按 formal type 组织

上一版候选里“必须给 Theorem / Corollary / Proposition 编号并与 manuscript 对齐”的要求取消。

新的确认规则：

- [CONFIRMED] Theory 主线先列 proposed model 相比 closest baselines 新解决的正式问题，再选择支撑这些能力的 formal guarantees。
- [CONFIRMED] Audience-facing slide title 不应机械使用 `Theorem`, `Corollary`, `Proposition` 作为主要叙事标签；否则容易让听众把注意力放在 formal taxonomy 和“有几个 theorem”上，而不是模型价值。
- [CONFIRMED] 不为了显得理论多，把 corollary、definition、estimand decomposition 人为升级为 theorem；也不因为它在 manuscript 中叫 corollary 就弱化它对模型闭环的必要性。
- [CONFIRMED] Slide title 应优先写成 claim / guarantee，例如：用一句直接的科学主张概括结果（具体原句留在私有项目仓库）。
- [CONFIRMED] manuscript 的 formal 类型、编号和 proof 状态可以留在 speaker/source notes；只有编号本身对现场讨论有帮助时才放主 slide。
- [CONFIRMED] 每个 formal guarantee 都必须回答：它防止什么失败、为什么当前方法需要它、已有方法的适用范围是什么。

## 2. 项目级应用不在此保存

原始理论选择、公式和科学解释留在私有项目仓库，此处不保存。可复用要求是先明确每页支撑的科学主张，再选择足够且真实的正式结果；不要为凑页数把定义或分解式包装成定理。

## 3. 其余 v3 第一轮意见

用户确认上一轮逐页审阅中除 theory 编号建议外，其余修改方向均可进入 v4。特别是以下重复失败继续作为 hard regression：

- overlay / diagram geometry / arrow size；
- 大量空白但核心内容仍小；
- repo path / audit / manuscript draft 等内部语言；
- figure-heavy slide 主图过小；
- metric direction 使用 `lower/higher` 冗余列；
- simulation 同类页 Question / Design / Metrics / Baselines 格式不闭合；
- references 字号未根据引用数量主动放大。
