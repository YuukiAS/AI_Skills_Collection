# CAT-TRACE 框架技术导读

更新日期：2026-11-11  
用途：把 CAT-TRACE 当前冻结模型、现行计算路线、已经实现的算法与仍未闭合的计算问题整理成一份可以脱离历史讨论独立阅读的中文技术导读。  
模型权威基线：<code>main@c407ceb564952b0b5724cb049a4a9e367c63420b</code> 的 FROZEN V2。  
实现状态补充来源：<code>impl/finland-q1-explore-20261110</code>、<code>impl/catalogue-v1-20261110</code>、<code>impl/malagasy-pilot-20261110</code>。  

> 本文没有重新运行统计程序或性能测试。文中的“已通过”“失败”“耗时”等实现状态均来自仓库中已经保存的代码、测试结果和运行记录。本文负责解释现状，不重新设计模型，也不把实现分支上的候选修复写成已经合入 <code>main</code> 的事实。

---

# 第一部分：CAT-TRACE 到底在建模什么

## 1. 从 TRACE 到 CAT-TRACE：科学问题的变化

TRACE 的出发点是一个开放的物种空间。普通联合物种分布模型先固定一个有限物种列表，再对每一列建模；TRACE 允许计算截断 \(p\) 增大，同时通过截距分布的特殊校准，让单个样本中预期出现的物种数保持有限。因此，“未来还会出现新列”从工程异常变成模型的一部分。

CAT-TRACE 在这个基础上增加两层结构。

第一层是**身份状态**。一个未来出现的对象可能已经属于外部有限目录，只是当前样本尚未检测到；也可能真正落在目录之外。两类发现的科学含义不同，因此分别记为有限目录 \(\mathcal K\) 与开放尾部 \(\mathcal U\)。

第二层是**生物分组**。每个目录对象和开放尾部特征都可以属于同一个粗粒度组 \(g\in\{1,\ldots,G\}\)，例如目、科或功能类群。身份状态回答“它是否有已知目录身份”，分组回答“它属于哪一类生态或分类单元”。这两个维度彼此正交。

当前第一篇论文的最小主线可以概括为：

> 有限目录 + 按组标记并校准的开放尾部 + 保持边际解释的 probit 回归 + 有限工作集合上的结构化残差依赖。

## 2. 从原始特征到目录、开放尾部和分组

前 \(n\) 个采样单元中的原始响应特征集合记为 \(\mathcal F_n\)。原始二元矩阵 \(Y^{raw}\) 的元素 \(y^{raw}_{if}=1\) 表示样本 \(i\) 中检测到特征 \(f\)。这里“检测到”是当前调查或测序流程下的观测状态；第一版没有额外引入占据—检测潜变量。

样本协变量记为 \(x_i\in\mathbb R^q\)。连续协变量只用训练集均值和标准差进行标准化，分类变量使用冻结编码。\(x_i\) 本身不含截距列，因为物种层截距单独建模。

有限分析目录记为 \(\mathcal K=\{1,\ldots,K\}\)。它的含义是：在当前身份分辨率和参考流程下，可以稳定表示、匹配并复现的一组候选身份。它不等于“区域内理论上存在的所有物种”。若流程只能稳定到 OTU、ASV、UNITE species hypothesis 等分辨率，目录身份也必须保持在该分辨率。

第一版使用确定性映射 \(c(f)\in\mathcal K\cup\{\varnothing\}\) 和 \(g(f)\in\{1,\ldots,G\}\)。\(c(f)=j\) 表示原始特征可匹配到目录身份 \(j\)；\(c(f)=\varnothing\) 表示它进入开放尾部；\(g(f)\) 给出共享的粗粒度分组。无法进一步分类的特征进入预先定义的 other/unresolved 组，而不是被丢弃。

多个原始特征若映射到同一目录身份，目录出现状态采用“或”聚合，即只要其中任意一个原始特征出现，该目录身份在该样本中就记为出现。目录中完全没有原始特征映射到的身份仍保留为全零列，它表示“当前训练样本尚未检测到该已知身份”。

## 3. 开放尾部的有限计算表示

理论上的开放尾部 \(\mathcal U\) 可以无限增长，但计算必须有限。对每个组 \(g\)，使用截断 \(p_g\)。训练期已经出现过的目录外列数记为 \(p_g^*\)，因此还有 \(p_g-p_g^*\) 个匿名全零槽位。

这些槽位代表“当前尚未出现、但未来可能出现的目录外特征”。它们没有物种身份、性状向量或树端点。它们也不是残差因子。\(p_g\) 是计算截断，不是生态学上的物种数硬上限。

这一区分带来四类计算对象：

1. 已出现的目录列；
2. 目录中已知但训练期全零的具名列；
3. 已出现的开放尾部列；
4. 匿名开放尾部全零槽位。

其中第 2 类和第 4 类数据向量都可能是全零，但统计含义不同：前者具有已知身份并服从有限目录层级；后者没有身份并服从 TRACE 尾部校准。

## 4. 边际 probit 是整套模型的锚点

无论目录还是开放尾部，观测层都使用潜在高斯表示。目录列的基本形式是

\[
y^{\mathcal K}_{ij}=1\{z^{\mathcal K}_{ij}>0\},\qquad
z^{\mathcal K}_{ij}=\alpha^{\mathcal K}_j+x_i^\top\beta^{\mathcal K}_j+\epsilon^{\mathcal K}_{ij}.
\]

开放尾部第 \(g\) 组第 \(h\) 列对应

\[
y^{\mathcal U}_{igh}=1\{z^{\mathcal U}_{igh}>0\},\qquad
z^{\mathcal U}_{igh}=\alpha^{\mathcal U}_{gh}+x_i^\top\beta^{\mathcal U}_{gh}+\epsilon^{\mathcal U}_{igh}.
\]

只要每个残差坐标的边际方差保持为 1，就有 \(\Pr(y=1\mid x,\alpha,\beta)=\Phi(\alpha+x^\top\beta)\)。

实际含义很直接：\(\beta\) 始终解释“环境协变量变化如何改变该列的边际发生倾向”。后续残差依赖层可以改变不同物种一起出现的方式和丰富度方差，但不重定义这个边际回归系数。

## 5. 目录与开放尾部怎样共享信息

当前冻结参数化把环境响应拆成总体、分组和物种特异三层。分组偏移满足 \(\sum_{g=1}^G a_g=0\)，使总体响应 \(\nu\) 有明确中心。

目录物种 \(j\) 的斜率为

\[
\beta^{\mathcal K}_j
=
\nu+a_{g_j}+\Gamma^\top t_j+b^{phy}_j+v^{\mathcal K}_j.
\]

其中 \(\nu\) 是总体环境响应，\(a_{g_j}\) 是组平均偏移，\(\Gamma^\top t_j\) 是有完整性状时的性状解释项，\(b^{phy}_j\) 是有可靠带枝长系统发育位置时的借力项，\(v^{\mathcal K}_j\) 是物种特异残差响应。

开放尾部使用更简单的结构：\(\beta^{\mathcal U}_{gh}=\nu+a_g+v^{\mathcal U}_{gh}\)。

两边共享 \(\nu\)、\(a_g\) 和响应异质性 \(\Psi\)。因此目录中有数据的物种可以帮助同组开放尾部学习“这一组总体如何响应环境”；目录规模本身并不会直接决定未知尾部有多大。

第一版使用共享对角协方差 \(\Psi=\mathrm{diag}(\psi_1^2,\ldots,\psi_q^2)\)，并令 \(v^{\mathcal K}_j\) 与 \(v^{\mathcal U}_{gh}\) 都服从均值为 0、协方差为 \(\Psi\) 的高斯分布。分开的 \(\Psi^{\mathcal K}\)、\(\Psi^{\mathcal U}\) 或组特异尺度留给错设模拟和敏感性分析。

## 6. 目录截距与开放尾部截距为什么采用两套机制

有限目录的大小固定，因此目录截距使用普通有限层级：\(\alpha^{\mathcal K}_j\mid\mu_\alpha,\sigma_\alpha\sim N(\mu_\alpha,\sigma_\alpha^2)\)。这里的 \(\mu_\alpha\) 描述目录物种整体常见程度，\(\sigma_\alpha\) 描述目录物种之间的基线异质性。

开放尾部需要随 \(p_g\) 增大而保持有限丰富度，所以采用 TRACE 校准。对组 \(g\)，

\[
\alpha^{\mathcal U}_{gh}\mid\gamma_g,p_g
\sim
N\{\mu_{p_g}(\gamma_g),\tau_{p_g}^2\},
\]

其中 \(\tau_p=\sqrt{2\log p}\)，并且

\[
\mu_p(\gamma)
=
\sqrt{1+\tau_p^2}\,
\Phi^{-1}\!\left(\frac{\gamma}{\gamma+p}\right).
\]

直觉是：\(p\) 越大，潜在尾部列越多，单列截距必须整体向更罕见的方向移动。每列出现概率因此降到 \(O(p^{-1})\)，而 \(p\) 列加总后的期望保持有限。

在无协变量的基线情形，每列边际出现概率正好对应 \(\gamma/(\gamma+p)\)，所以 \(p\) 列的期望丰富度趋向 \(\gamma\)。若列之间独立，稀有事件定律进一步给出 Poisson 极限。这与 Indian buffet process（IBP）“无限潜在特征、每个样本只激活有限个特征”的直觉相连，但 CAT-TRACE 保留了 probit 回归、环境协变量、分组标记以及目录/开放尾部的身份分解。

组强度写为 \(\gamma_g=\gamma_0\pi_g\)，其中 \(\gamma_0\) 控制总体开放尾部强度，\(\pi=(\pi_1,\ldots,\pi_G)\) 控制中心化协变量条件下的组组成，且 \(\sum_g\pi_g=1\)。环境协变量通过 \(\nu+a_g\) 继续改变不同组在具体样本中的实际丰富度，因此 \(\pi_g\) 不是所有环境下固定的发现比例。

## 7. 分组丰富度与总丰富度

在冻结的共享斜率层级下，第 \(g\) 组开放尾部的渐近期望丰富度为

\[
\lim_{p_g\to\infty}
E\{N^{\mathcal U}_{ig}(p_g)\}
=
\gamma_0\pi_g
\exp\!\left\{
x_i^\top(\nu+a_g)+\frac12 x_i^\top\Psi x_i
\right\}.
\]

这条式子说明三件事：\(\gamma_0\pi_g\) 决定中心位置的尾部规模；\(\nu+a_g\) 控制组平均环境响应；\(\Psi\) 通过系数异质性带来指数型的边际放大。有限 \(G\) 下各组相加仍然有限，再加有限目录丰富度后总期望仍有限。

\(G=1\) 且 \(\mathcal K=\varnothing\) 时，模型退化回 TRACE。第一篇论文的真实数据主分析要求用于“分组开放尾部”主张的数据具有冻结的 \(G>1\)；\(G=1\) 主要承担退化检查和消融。

## 8. 性状、分类相关结构与真正系统发育

性状矩阵只作用于具名目录身份。只有每个纳入物种都有完整、对齐并冻结预处理的性状向量时，才启用 \(\Gamma^\top t_j\)。第一版性状解释环境响应斜率，不直接改变开放尾部基线稀有程度。

相关结构必须区分两类来源：

- \(C^{tax}\)：由 name、family、order、class、phylum 等分类层级构造的相似性或相关性代理；
- \(C^{phy}\)：由真正带分支长度的系统发育树导出的相关矩阵。

South-West Australia plants 当前可以复现 \(C^{tax}\)，但没有确认可用于主分析的带枝长 \(C^{phy}\)。因此分类代理可以用于结构化借力比较，但不能写成分支层面的系统发育推断。

当存在真正 \(C^{phy}\) 时，目录中有可靠树端点的子集 \(\mathcal P\) 可以使用矩阵正态借力。匿名开放尾部槽位没有身份，因此不会被虚构性状或树端点。

## 9. 残差依赖层

残差依赖只在有限工作集合 \(\mathcal W\) 上显式建模。当前冻结结构是标准化因子 copula：

\[
\Omega_{\mathcal W}=\Lambda_{\mathcal W}\Lambda_{\mathcal W}^\top+I,
\qquad
\Sigma_{\mathcal W}
=
D_{\mathcal W}^{-1/2}\Omega_{\mathcal W}D_{\mathcal W}^{-1/2},
\]

其中 \(D_{\mathcal W}=\mathrm{diag}(\Omega_{\mathcal W})\)。标准化后 \(\mathrm{diag}(\Sigma_{\mathcal W})=1\)，所以依赖层改变联合分布和丰富度方差，却保持单列 probit 边际。

匿名开放尾部零槽位不进入物种特异残差网络，因为没有数据识别它们与具体已知物种之间的相关性。第一版计算架构还采用切断反馈：残差依赖读取第一阶段的边际摘要，但不反向重估 \(\beta\)。这保护了边际解释，也让几十万列的边际推断不被完整高维相关结构阻塞。

因子载荷使用乘性 Gamma 过程收缩。对工作集合坐标 \(w\) 和因子 \(d\)，
\(\lambda_{wd}\mid\phi_{wd},\vartheta_d\sim N\{0,(\phi_{wd}\vartheta_d)^{-1}\}\)，其中 \(\phi_{wd}\sim\mathrm{Gamma}(3/2,3/2)\)，\(\vartheta_d=\prod_{u=1}^d\delta_u\)，\(\delta_1\sim\mathrm{Gamma}(2.1,1)\)，后续 \(\delta_u\sim\mathrm{Gamma}(3.1,1)\)。后续因子的累计精度倾向更大，因此载荷会逐渐收缩；预设因子数 \(H\) 是计算上限，不是生态参数。

标准化因子 copula 的方向已经冻结，完整 C09 生产推断仍未闭合，因此当前不能把残差依赖写成已完成模块。

## 10. 当前先验与超参数默认

外部目录、分类、性状和系统发育是输入结构，不是参数先验。第一版主要默认如下。

| 对象 | 当前默认 | 实际含义 |
|---|---|---|
| 总体斜率 \(\nu\) | \(N_q(0,1.5^2I_q)\) | 标准化 probit 尺度上的弱信息总体环境响应 |
| 分组偏移 \(a_g\) | 先生成独立高斯再中心化，\(\sigma_a\sim\mathrm{half}\text{-}N(0,0.75^2)\) | 组间环境响应差异，并强制和为零 |
| 物种响应尺度 \(\psi_k\) | \(\mathrm{half}\text{-}N(0,1^2)\) | 物种对同一协变量反应的异质性 |
| 目录截距中心 \(\mu_\alpha\) | \(N(m_{\alpha,K},1^2)\) | \(m_{\alpha,K}\) 由训练目录发生率做弱经验定心 |
| 目录截距尺度 \(\sigma_\alpha\) | \(\mathrm{half}\text{-}N(0,1^2)\) | 目录物种基线常见程度的异质性 |
| 开放尾部总强度 \(\gamma_0\) | 若 \(\bar R_U>0\)，形状—率参数化 \(\mathrm{Gamma}(2,2/\bar R_U)\) | 训练数据内弱经验定心；不是 \(\gamma_0\) 的无偏估计 |
| 无已见尾部时 \(\gamma_0\) | \(\mathrm{Gamma}(1,1)\) | 预先规定的弱信息备用先验，并要求敏感性分析 |
| 组份额 \(\pi\) | \(\mathrm{Dirichlet}(1,\ldots,1)\) | 开放尾部总强度在组间的组成 |
| 性状系数 \(\Gamma_{\ell k}\) | \(N(0,\sigma_\Gamma^2)\)，\(\sigma_\Gamma\sim\mathrm{half}\text{-}N(0,0.5^2)\) | 性状对环境响应差异的解释 |
| 系统发育尺度 \(\kappa_{phy}\) | \(\mathrm{half}\text{-}N(0,0.5^2)\) | 真正 \(C^{phy}\) 上的剩余系统发育借力 |
| 因子载荷 | 上述乘性 Gamma 过程 | 让后续因子逐渐更强地收缩，避免有效秩完全靠人工固定 |

目录截距的经验中心来自训练集目录矩阵。若目录总发生次数为 \(\sum_{i,j}y^{\mathcal K}_{ij}\)，先用连续性修正得到
\(\tilde p_K=\{\sum_{i,j}y^{\mathcal K}_{ij}+1/2\}/(nK+1)\)，再令 \(m_{\alpha,K}=\Phi^{-1}(\tilde p_K)\)。测试集和未来样本不能参与这个校准。

开放尾部的训练经验中心使用 \(\bar R_U\)，即训练样本中已观测开放尾部的平均丰富度。它只决定一个弱经验先验中心；有协变量时 \(E(\bar R_U)\) 一般不等于 \(\gamma_0\)，所以不能把 \(\bar R_U\) 当成 \(\gamma_0\) 的无偏或一致估计。主模拟还要求与固定弱信息先验、不同 Gamma 形状以及不同对称 Dirichlet 浓度做敏感性比较。

## 11. 分组规则也是模型合同的一部分

\(G\) 不是响应模型自动学出的聚类数。第一版从数据自带的分类或功能注释中预先冻结分组。当前建议流程是：选择能覆盖至少 80% 已观测开放尾部特征的最细层级；每组至少包含 \(\max(20,5q)\) 个已观测开放尾部特征；小组和未解析对象合并到预定义组；最终保持 \(2\le G\le20\)。

这样做的目的，是让“按组发现”有可复现的生物学含义，同时避免用拟合结果反向挑分组。

## 12. 当前真实数据角色

第一篇论文当前固定三项主数据：

- Finland fungi：与原 TRACE 衔接、分组开放尾部、残差结构诊断；当前主分析 \(\mathcal K=\varnothing\)。
- Malagasy arthropods：极端稀有尾部与大规模计算压力测试；已有分类表，适合粗粒度分组；正式外部目录尚未冻结。
- South-West Australia plants：有限目录的主要候选案例，同时承担性状、\(C^{tax}\) 和结构化依赖解释；真实区域目录仍需来源链核实后才能冻结。

GSMc 已后置为外部验证或工程压力测试，不是第一篇论文当前实现的完成门槛。

---

# 第二部分：从数据到预测的完整计算链

## 13. 一眼看懂生产路线与参考路线

~~~mermaid
flowchart TD
    A["训练数据：Y、X、目录映射、组标记"] --> B["冻结身份与分组"]
    B --> K1["目录：训练期已见列"]
    B --> K0["目录：具名全零列"]
    B --> U1["开放尾部：训练期已见列"]
    B --> U0["开放尾部：匿名全零槽位"]

    K1 --> C01["C01 单列 Newton–Laplace"]
    U1 --> C01
    K0 --> K0A["同组同先验时：一个目录零列原型 × 重数"]
    K0A --> C01
    U0 --> ZS["匿名零槽积分：每组一个积分 × m_g"]

    C01 --> P["共享参数剖面目标"]
    ZS --> P
    P --> GR["数值梯度：参考档 Richardson；探索档中心差分"]
    GR --> BFGS["BFGS 搜索共享参数众数"]
    BFGS --> H["最终数值 Hessian + Cholesky 稳定性检查"]
    H --> HD["共享参数高斯抽样"]
    HD --> CD["条件列重拟合与列参数抽样"]
    CD --> PR["目录重新检出 + 开放尾部首次发现"]
    ZS --> PR

    A -. "小规模独立参照" .-> AC["Albert–Chib 参考 MCMC"]
    AC --> REF["Rhat / ESS / MCSE + 与 Laplace 路线对照"]

    C01 -. "有限工作集合" .-> DEP["C09 残差依赖：方向已定，生产算法未闭合"]
~~~

这张图有两个中心思想。第一，显式列和匿名零槽位都要贡献后验信息，只是计算表示不同。第二，Albert–Chib 不在生产链上，它是小规模独立参考，用不同算法检查近似推断是否可信。

## 14. 各计算块的输入、输出和仓库落点

| 计算块 | 主要输入 | 主要输出 | 当前函数/文件 | 状态 |
|---|---|---|---|---|
| 身份与分组 | 原始特征、目录、组规则、训练划分 | 目录矩阵、尾部已见列、\(p_g^*\)、\(m_g=p_g-p_g^*\) | <code>cat-trace-data.R</code>；目录分支 <code>cat-trace-catalogue-v1-data.R</code> | 基础合同已实现；真实数据目录仍按数据集冻结 |
| C01 单列积分 | 二元列、\(X\)、高斯先验均值与精度 | 众数、协方差、Laplace 对数积分、数值诊断 | <code>src/ct_probit.cpp::ct_probit_laplace</code> | <code>main</code> 已实现；芬兰舍入平台修复仅在实现分支 |
| 匿名零槽 | \(X,\gamma_g,p_g,\nu+a_g,\Psi,m_g\) | \(A_g\)、\(\log I_{0g}\)、\(m_g\log I_{0g}\)、误差估计 | <code>R/cat-trace-zero-slot.R</code> | <code>main</code> 仅 q=0/q=1、value-only 参考后端 |
| 目录全零列 | 具名目录零列、组、有限目录先验 | 同组原型的列积分与重数贡献 | <code>cat-trace-catalogue-v1-fit.R</code> | 目录/马达加斯加实现分支已有 q=1 精确重用 |
| 共享参数剖面 | 超参数自由坐标、显式列积分、零槽积分、超先验 | 低维目标值和误差账 | <code>R/cat-trace-fit.R</code> | <code>main</code> q=0/q=1 reference-only C03 |
| 数值梯度 | 剖面目标 | 梯度与数值误差诊断 | <code>.ct_r_c03_profile_gradient</code>；探索档 <code>cat-trace-numerics.R</code> | 参考档已实现；探索档分支已实现 |
| BFGS | 剖面目标、数值梯度、初值 | 共享参数候选众数 | <code>stats::optim(method="BFGS")</code> 包装于 <code>cat-trace-fit.R</code> | 已实现；极端试探点仍暴露尾参数数值问题 |
| 最终 Hessian | 最终点周围剖面目标 | \(\widehat H\)、Cholesky、曲率稳定性、共享参数局部高斯 | <code>.ct_r_c03_hessian_at_steps</code> | 已实现 |
| 共享参数抽样 | 众数与最终 Hessian | 2000 个共享参数高斯抽样 | <code>cat-trace-fit.R</code>；目录分支 <code>.ct_v1_hyper_draws</code> | 已实现于当前有限路线 |
| 条件列抽样 | 每个共享抽样、每列数据 | 列众数、协方差、列参数抽样 | 目录分支 <code>.ct_v1_conditional_draws</code>；马达加斯加 <code>cat-trace-conditional-batch.R</code> | 分支实现 |
| 显式目录预测 | 列参数抽样、未来 \(X\) | 累积重新检出概率与期望 | <code>R/cat-trace-predict.R</code> | <code>main</code> 已实现显式目录部分 |
| 匿名尾部首次发现 | 零槽训练条件后验、未来 \(X\)、\(m_g\) | 分组首次发现累计曲线 | 目录分支 <code>.ct_v1_integrate</code> / <code>.ct_v1_tail_discovery</code> | q=1 分支实现，尚非 <code>main</code> 通用 API |
| Albert–Chib 参考 | 小型有限 \(p\) 数据、冻结先验、随机流 | MCMC 抽样、Rhat、ESS、MCSE | <code>R/cat-trace-reference.R</code> | 正确性门已过；固定 F1 可靠性门仍差两个 bulk ESS |
| 残差依赖 | 第一阶段边际摘要、有限 \(\mathcal W\) | 合法单位对角 PSD 相关结构与联合预测 | C09 设计文档 | 方向冻结，生产算法未闭合 |

---

# 第三部分：关键算法逐个讲清楚

## 15. C01：为什么每一列先做 Laplace

### 15.1 直觉

CAT-TRACE 的高维来自“列非常多”，而不是“每列参数维度很高”。给定共享参数后，一列通常只有截距和少量环境系数。生产计算因此先把每列的条件后验压成“一个中心 + 一块局部曲率”。

对列参数 \(\theta=(\alpha,\beta^\top)^\top\)，对数后验写成 \(h(\theta)\)。C01 找到后验众数 \(\hat\theta\)，再用负 Hessian \(H=-\nabla^2h(\hat\theta)\) 构造 \(q(\theta)\approx N(\hat\theta,H^{-1})\)。

Laplace 对数积分把这一列对共享参数的证据压成

\[
\log I
\approx
h(\hat\theta)+\frac d2\log(2\pi)-\frac12\log|H|,
\]

其中 \(d=q+1\)。它保留局部后验中心、曲率和整列对上层共享参数的积分证据，后续不需要为每列保存一条长 MCMC 链。

### 15.2 仓库实现

<code>package/TRACE/src/ct_probit.cpp</code> 同时计算稳定的 probit 似然、score、负 Hessian、Newton 方向、局部协方差和 Laplace 积分。上层目录列、已见尾部列和若干原型列都复用这一数值核。

Laplace 是生产近似，不是“精确后验”的同义词。Albert–Chib 参考引擎正是为了在小问题上独立检查这种局部高斯近似。

## 16. Newton：为什么用二阶信息直接找列众数

对当前点 \(\theta\)，记 score 为 \(g=\nabla h(\theta)\)，负 Hessian 为 \(H=-\nabla^2h(\theta)\)。最大化问题的 Newton 方向满足 \(H\delta=g\)。

若局部二次近似准确，\(\theta+\delta\) 会直接走向局部众数。probit 单列后验在正定高斯先验下具有良好的凹性结构，因此 Newton 比完全黑盒的一阶方法更能利用已知数学结构。

当前 C01 的停止判据使用 Newton decrement、参数变化和目标变化三类量。Newton decrement 本质上测量“按当前曲率标准化以后，离驻点还有多远”。

## 17. Cholesky：一套分解同时做求解、正定检查和抽样

### 17.1 直觉

如果 \(H\) 对称正定，可以写成 \(H=R^\top R\)，其中 \(R\) 是上三角矩阵。C01 不显式求 \(H^{-1}\)，而是先解 \(R^\top y=g\)，再解 \(R\delta=y\)。这样得到的 \(\delta\) 与 \(H^{-1}g\) 相同，但数值更稳。

Newton decrement 为 \(D=\|y\|_2=\sqrt{g^\top H^{-1}g}\)。这个量天然非负，还等于 Newton 方向的一阶方向导数平方根，因此后面的 Armijo 检查可以直接复用 \(D^2\)。

### 17.2 一个 2×2 手算例子

取

\[
H=
\begin{pmatrix}
4&1\\
1&3
\end{pmatrix},
\qquad
g=
\begin{pmatrix}
1\\2
\end{pmatrix}.
\]

一个上三角 Cholesky 因子是

\[
R=
\begin{pmatrix}
2&0.5\\
0&\sqrt{2.75}
\end{pmatrix},
\qquad H=R^\top R.
\]

先解 \(R^\top y=g\)，得到 \(y_1=0.5\)，\(y_2=1.75/\sqrt{2.75}\)；再解 \(R\delta=y\)，得到 \(\delta=(1/11,7/11)^\top\)。这与直接计算 \(H^{-1}g\) 完全一致。

同一个 \(R\) 还给出 \(\log|H|=2\sum_k\log R_{kk}\)，并能通过两次三角求解得到局部协方差 \(H^{-1}\)。共享参数高斯抽样也使用同样的“用 Cholesky 方向生成正确协方差”思想。

### 17.3 失败意味着什么

冻结设计把 Cholesky 失败视为需要显式暴露的数值或合同异常。当前路线不靠 jitter、特征值裁剪或 nearest-PD 静默把矩阵修成可分解，因为理论上合法的单列高斯先验已经应当提供正定曲率。这样 Cholesky 既是计算工具，也是结构检查。

## 18. Armijo：Newton 方向正确以后，步长仍要受控

### 18.1 充分上升条件

Newton 给出方向 \(\delta\)，Armijo 决定走多远。当前 C01 从完整步长 \(s=1\) 开始，回溯取 \(1,1/2,1/4,\ldots\)，最多 25 次。接受条件是

\[
h(\theta+s\delta)
\ge
h(\theta)+c_1 sD^2,
\]

其中 \(c_1=10^{-4}\)，\(D^2=g^\top H^{-1}g\)。左边是实际新目标，右边是根据当前方向导数要求的最低上升量。它防止 Newton 在局部二次近似较差时一步走过头。

### 18.2 芬兰 q=1 暴露的浮点平台问题

芬兰探索分支找到的原失败并非 Hessian 非正定，而是准分离列在接近众数时进入浮点平台：步长已经缩得极小，新旧目标在 double 表示中完全相等，但 score 仍略高于 \(10^{-8}\)。原 Armijo 表达式右侧的增量也可能被舍入为 0，于是“目标相等”被当成有效上升；随后算法用很多几乎没有信息的微小步消耗迭代。

<code>impl/finland-q1-explore-20261110</code> 的最小修复在 score 门尚未通过时拒绝这种 rounded plateau。若 25 次回溯都失败，则使用已经存在的方向导数下界保护：检查先验正定、完整步确实改变坐标、完整步和中点目标/曲率有限，再用 Neumaier 补偿的方向导数构造下界。只有该下界仍满足 Armijo 要求时才接受完整 Newton 步。

固定回归点修复前触及 100 次上限；修复后 8 次迭代收敛，702 列在该点全部返回成功。这个修复目前位于实现分支，尚不能写成 <code>main</code> 已经合并的行为。

## 19. 匿名开放尾部零槽：为什么“很多全零列”只算一次

### 19.1 统计对象

对某组匿名槽位，训练期全零似然为 \(L_{0g}(\alpha,\beta)=\prod_{i=1}^n\Phi(-\alpha-x_i^\top\beta)\)。

把该组尾部先验积分掉，得到单个匿名槽位在训练数据下保持全零的概率 \(I_{0g}=E\{L_{0g}(\alpha,\beta)\}\)。定义“至少被发现一次”的补量 \(A_g=1-I_{0g}\)，代码直接计算 \(A_g\) 再用稳定的 \(\log(1-A_g)\) 得到 \(\log I_{0g}\)。

同组的 \(m_g=p_g-p_g^*\) 个匿名槽位有完全相同的数据和条件先验，因此总贡献精确等于 \(m_g\log I_{0g}\)。

这里的“乘重数”是代数等价，不是把 \(m_g\) 个物种近似成一个物种。计算成本因此不随 \(m_g\) 线性增长。

### 19.2 q=0 的参考积分

没有协变量时，\(\alpha=\mu_p(\gamma_g)+\tau_p Z_\alpha\)，所以 \(A_g=E_{Z_\alpha}[1-\Phi(-\alpha)^n]\)。<code>.ct_r_zero_slot_evaluate_q0</code> 用一维自适应积分直接算这个正补量。

### 19.3 q=1 的参考积分

一个协变量时，令 \(\beta=b_g+\psi Z_\beta\)。条件于 \(Z_\beta\) 后对 \(Z_\alpha\) 做内层积分，再对 \(Z_\beta\) 做外层积分：

\[
A_g
=
E_{Z_\beta}E_{Z_\alpha}
\left[
1-\prod_{i=1}^n
\Phi\{-\alpha-x_i\beta\}
\right].
\]

<code>.ct_r_zero_slot_evaluate_q1</code> 当前用嵌套 <code>integrate()</code> 实现，并单独传播内外层数值误差。

### 19.4 与原 TRACE 的“零填充”有什么不同

原 TRACE 的有限截断概念上保留所有潜在列，包括训练期全零列。CAT-TRACE 没有改变这项统计信息；变化在计算表示：同组匿名槽位共享同一积分，所以只保留一个原型和重数。这样节省的是存储和重复积分，不是零信息。

当前 <code>main</code> 的零槽后端只支持 q=0/q=1 且只返回函数值。q>1、生产级梯度/Hessian 兼容积分仍属于后续计算设计。

## 20. 目录全零列：和匿名零槽相似，但身份先验不同

目录零列是“已知身份、训练期没检测到”的有限列。它们服从目录截距层级，而不是 TRACE 尾部截距校准。因此不能因为响应都是 \(0^n\) 就直接套匿名零槽积分器。

在当前 q=1 目录第一版与马达加斯加试点中，如果同一组目录零列具有完全相同的有限高斯截距先验和组斜率先验，那么它们的条件积分完全相同。<code>.ct_v1_catalogue_terms()</code> 因此在**同组内部**选一个代表零列求 C01/Laplace，再按该组零列数展开回贡献；代码同时拒绝把不同组的零列错误合并。

这条加速在当前简化目录模型下是精确等价。以后若某个具名目录物种启用不同性状、relatedness 或其他物种特异先验，两列条件目标就不再相同，届时必须按实际先验分组，不能继续仅凭“同组且全零”复用。

## 21. Helmert 坐标：怎样表示和为零的组偏移

\(G\) 个组偏移满足 \(\sum_g a_g=0\)，所以实际自由维度只有 \(G-1\)。实现用 Helmert 正交基 \(Q_G\in\mathbb R^{G\times(G-1)}\) 写成 \(A=Q_GA^*\)。

这样自由参数 \(A^*\) 无约束，而映射回自然空间后自动满足和为零。相比“每轮更新后再减均值”，正交坐标把约束直接写进参数化，梯度和 Hessian 也在真正自由的空间中计算。

组份额 \(\pi\) 同样只需 \(G-1\) 个自由坐标。代码使用 reference-logit/softmax，从自由 logits 恢复完整 simplex。数值上先减最大值再指数化，避免大坐标溢出。

当 \(G=1\) 时，Helmert 自由块、组尺度和份额 logits 都消失；模型只剩总体响应和单组尾部强度。这是退化回 TRACE 的关键实现边界之一。

## 22. 剖面目标：为什么共享参数可以变成一个低维优化问题

给定共享参数自由坐标 \(u\)，每个显式列先在自己的低维参数空间求众数并做 Laplace 积分；每组匿名零槽做一个积分。随后把所有贡献加起来：

\[
\widetilde\ell(u)
=
\log p_{trans}(u)
+
\sum_{c\in\mathcal C_{explicit}}\log I_c(u)
+
\sum_{g=1}^G m_g\log I_{0g}(u).
\]

\(\log p_{trans}(u)\) 是变换后坐标中的超先验，包括正尺度的 log 变换 Jacobian，以及从份额自由坐标到 simplex 的 Jacobian。目录版本还加入 \(\mu_\alpha,\sigma_\alpha\) 两个共享坐标和全部目录列积分。

“剖面”在这里指计算结构：每给一个共享参数点，就重新解决内层列问题，把列参数压缩掉，只留下共享参数上的低维目标。它不是把列参数简单固定在某个历史众数，也不是声称获得完整多元 probit 的精确联合后验。

## 23. 数值梯度：当前最大的计算乘数

### 23.1 参考档 Richardson 梯度

<code>main</code> 的 reference 路线对每个自由坐标使用三个尺度 \(h,h/2,h/4\) 的中心差分。每个尺度需要正负两个完整剖面求值，因此每坐标一轮梯度最多需要 6 次完整求值。Richardson 外推用较粗与较细差分消掉主导截断误差，第三个尺度用于步长稳定性检查；同时把零槽积分误差传播进梯度误差账。

这比普通中心差分昂贵得多，但目的明确：先建立一个可审计的数值基线。

### 23.2 为什么它成为主成本

2026-11-10 的 Longleaf 单线程实测显示：

- 目录第一版合成场景单次完整求值约 30 秒，其中三个 q=1 匿名零槽积分各约 8 秒；7 个共享坐标的一轮参考梯度要 42 次完整求值，约 21 分钟。
- Finland q=1、G=1 的单次完整求值约 10–12 秒。
- Finland q=1、G=3 的单次完整求值约 50 秒，一轮梯度约 25 分钟。
- Malagasy 三目探索档 1977 个训练样本、4593 列时，单次完整求值约 393 秒；按约 150 次求值估算超过 16 小时。
- 单个 C01 列在 \(n=1977\) 时冷启动约 0.038 秒、热启动约 0.002 秒。

这些数字说明扩展瓶颈首先是“完整目标被重复算多少次”，其次才是单列核有多快。

### 23.3 探索档

马达加斯加分支增加 <code>control$numerics="exploratory"</code>：每个坐标只做一次中心差分，也就是 2 次完整求值；该模式明确标记 <code>gradient_error_checked=FALSE</code>，因为没有 Richardson 步长比较。探索档用于预算内试点，不替代 reference 数值门。

## 24. BFGS：外层为什么不用 Newton

共享参数的剖面目标本身需要重新拟合许多列、计算零槽积分，而且目前没有解析 Hessian。若外层每一步都直接构造精确 Hessian，代价会更高。

BFGS 使用函数值和梯度差逐步构造曲率近似。它不需要每个迭代都计算完整 Hessian，因此适合低维共享参数搜索。当前 R 实现通过 <code>stats::optim(method="BFGS", fnscale=-1)</code> 最大化剖面目标；reference 档 <code>reltol=1e-12</code>，探索档 <code>reltol=1e-10</code>，最大迭代数 150。

R 的 BFGS 内部线搜索可能提出离当前点很远的候选坐标。Finland G1 的真实重跑中，优化器曾走到 \(\log\gamma_0\approx547.76\)，同时 \(\nu\approx-364\)、\(\log\psi\approx95\)。这些数仍是有限 double，但尾部映射中的 \(\gamma/(\gamma+p)\) 被舍入成 1，随后 \(\Phi^{-1}(1)=+\infty\)，目标评估在进入 C01 前失败。

马达加斯加探索分支增加了超先验上界拒绝：先利用“所有归一化列积分和匿名零槽对数概率都不大于 0”构造一个保守的目标上界。如果这个上界已经低于当前已接受目标，就直接拒绝该候选点，不再支付显式列和零槽的完整计算成本。这个机制不改变目标，只是更早证明“该点不可能更好”。

## 25. 最终 Hessian 与共享参数抽样

BFGS 停止只给出一个候选众数。正式局部高斯近似还需要独立重新计算剖面 Hessian。

当前实现用中心有限差分分别构造整步 \(H_h\) 与半步 \(H_{h/2}\)，最终唯一采用半步矩阵 \(\widehat H=H_{h/2}\)。随后用 \(\widehat H\) 的 Cholesky 做几何白化，把 \(H_h\) 放进 \(\widehat H\) 的自然曲率坐标中比较特征值；所有广义曲率都必须在预定乘法误差带内。这样检查的是“每一个曲率方向的相对变化”，而不是只比较矩阵最大元素。

共享参数抽样也在这个自由坐标空间完成。若 \(\widehat H=R^\top R\)，标准正态 \(z\) 通过 <code>backsolve(R,z)</code> 生成协方差为 \(\widehat H^{-1}\) 的扰动。方向写反会得到错误协方差，因此 Cholesky orientation 在 C04 和共享参数抽样中都被作为明确合同。

当前 C03 路线固定生成 2000 个共享参数高斯抽样，再把 log、softmax 等变换映射回自然参数。

## 26. 发现预测：目录重新检出和开放尾部首次发现必须分开

### 26.1 目录中已知但训练未见的物种

给定一份列参数抽样，对目录身份 \(j\)，未来第 \(i\) 个样本发生概率为 \(\pi_{ij}=\Phi(\alpha_j+x_i^\top\beta_j)\)。未来前 \(m\) 个样本至少出现一次的概率是 \(\rho_{j,m|n}=1-\prod_{i=n+1}^{n+m}(1-\pi_{ij})\)。

代码用累计 log-zero 概率和 <code>-expm1()</code> 计算，避免很多接近 1 的乘积失去精度。训练期已经出现的目录物种在“新目录发现”中置零，因此得到的量真的是“已知目录内、过去未见、未来重新检出”。

### 26.2 匿名开放尾部首次发现

匿名尾部需要先条件在“训练期一直全零”。对一个槽位，未来发现概率可以写成

\[
q_{g,m|n}
=
\frac{
E\!\left[
L_{train}(\alpha,\beta)
\{1-L_{future,m}(\alpha,\beta)\}
\right]
}{
E\{L_{train}(\alpha,\beta)\}
}.
\]

分子直接积分一个非负量，比分别算两个接近的积分再相减稳定。目录第一版分支的二维后验适应 Gauss–Hermite 积分按未来样本逐步累积这个正分子，再乘 \(m_g\) 得到该组匿名槽位的首次发现期望。

### 26.3 合并

目录和开放尾部必须使用**同一批共享参数抽样**后再相加，这样共享层级的不确定性能够一致传播。目录分支 <code>.ct_v1_combine_discovery()</code> 正是用相同 draw identity 合并两部分；尾部积分失败的抽样保留为 NA 并报告失败比例，而不是只对成功子集重新归一化。

<code>main</code> 的通用 <code>cat-trace-predict.R</code> 当前明确声明 <code>includes_anonymous_open_tail=FALSE</code>，因此匿名尾部首次发现目前属于目录/真实数据实现分支，而不是主线已经完成的公开预测 API。

## 27. Albert–Chib：为什么需要一套完全不同的参考 MCMC

### 27.1 基本思想

probit 本来就可以写成潜在高斯变量：\(y_i=1\{z_i>0\}\)。Albert–Chib 数据增广在给定 \(y\) 和参数时从对应半轴的截断正态抽 \(z\)；给定 \(z\) 后，回归参数变成高斯条件问题，因此许多参数块可以直接 Gaussian 抽样。

它的价值不是速度，而是与“众数 + 局部曲率”的 Laplace 路线足够不同。两条路线在小型有限 \(p\) 问题上相互核对，可以区分实现错误、Laplace 近似误差和 MCMC 自身混合不充分。

### 27.2 当前一次 sweep 实际做什么

当前 <code>ref_ct_one_sweep()</code> 的顺序是：

1. 按当前状态抽 latent \(Z\)；
2. 给定 \(Z\)，联合 Gaussian 更新每列 \((\alpha,\beta)\)；
3. 更新共享 Gaussian 位置块；
4. 对 \(\log\psi\)、可用时的 \(\log\sigma_{group}\)、\(\log\gamma_0\) 与份额 logits 做中心化 slice 更新；
5. 在非中心化斜率坐标下交织更新 \(\psi\)；
6. 在非中心化位置坐标下联合更新 \(\nu\) 与组偏移；
7. 在固定当前 \(Z\) 的非中心化截距坐标下更新 \(\eta_g=\log\gamma_g\)；
8. 最后进行 \(Z\)-collapsed 的 Helmert 组成更新，直接使用观测 probit 似然而不条件于旧 \(Z\)；
9. 保存抽样和诊断。

最后一步必须放在 sweep 末尾，因为它已经改变组成和截距；旧 \(Z\) 随后丢弃，下一 sweep 从新状态重新抽 \(Z\)。两 sweep stale-Z 回归测试专门锁定了这条顺序。

### 27.3 为什么需要 interweaving 和 Z-collapsed 组成更新

原中心化参数化中，共享位置、尺度、组份额和大量列参数可能强耦合。交织更新在保持同一目标分布的前提下，换一套坐标移动同一状态，使原本很窄的条件方向变宽。

v0.1.1 的诊断发现组成方向 \(c_2\) 在固定 \(Z\) 时条件宽度只有边际尺度的一小部分；把 \(Z\) 积分掉以后，该条件宽度约增大 3.8 倍。v0.1.2 因此用精确观测 probit likelihood 的 \(Z\)-collapsed Helmert block 替换原生产 augmented contrast slot。

C1–C7 的观测似然、目标差、写回、单 sweep、双 sweep stale-Z、\(G=1\) 边界和继承门全部通过。固定 F1 正式运行到每链 40000 个保留抽样时，Rhat、tail ESS 和 MCSE 等大部分门已经通过，但 <code>group_share[g3]</code> 与 <code>share_logit[g2]</code> 的 bulk ESS 分别约为 690 和 632，低于 1000 的冻结门槛。因此 C04 是**正确性证据充分、混合可靠性尚未完全通过**的参考引擎。

### 27.4 Rhat、ESS 和 MCSE 各自回答什么

Rhat 比较链内和链间尺度；接近 1 表示多链的整体位置/尺度相容。当前门槛是 Rhat < 1.01。

ESS 是把自相关 MCMC 换算成“相当于多少个独立样本”。bulk ESS 主要反映分布主体位置和均值类量的有效信息，tail ESS 更关注尾部和分位数。当前两项都要求至少 1000。

MCSE 是蒙特卡洛均值误差。当前门要求 mean MCSE 不超过后验标准差的 5%。因此“链很长”本身不构成通过；自相关强时，40000 个保留抽样仍可能只有几百个有效独立样本。

## 28. 其他数值机制

### 28.1 有限截断 \(p_g\)

\(p_g\) 是计算截断。判断截断是否足够必须区分三件事：

1. 当前实际拟合的 finite-\(p\) estimand；
2. 固定参数下 finite-\(p\) 与渐近公式的数学差；
3. 每个 \(p\) 重新拟合后科学预测是否稳定。

后续 C06 已明确撤销“不断倍增 \(p\) 总能达到统一 1%”的普遍自动门。具体接受标准需要按正式模拟实验预注册。

### 28.2 log-sum-exp 和 log 概率

极稀有事件下直接先算概率再取对数会下溢。当前代码大量使用 <code>pnorm(..., log.p=TRUE)</code>、<code>log1p</code>、<code>expm1</code> 和稳定 log-sum-exp。它们解决的是同一个数学目标的浮点表达问题，不改变概率模型。

### 28.3 L'Ecuyer-CMRG 随机流

参考引擎和合成目录示例使用 L'Ecuyer-CMRG，把 DGP、参考 MCMC、后验抽样、bootstrap 等用途分成独立子流。key 按用途/场景/重复/链固定，任务重排和并行调度不会通过线程顺序改变科学随机流。

### 28.4 reference 与 exploratory 两档

reference 档保留严格积分容差、Richardson 梯度和完整数值稳定性检查，目标是可审计基线。exploratory 档由 2026-11-10 马达加斯加试点授权，用较宽积分容差、单步中心差分和有限并行快速判断真实数据可行性，同时在结果对象中明确标记梯度截断误差未核对。

两档计算同一模型目标；exploratory 是降低数值验证强度换取速度，不应被写成新的统计模型。

---

# 第四部分：当前实现状态

## 29. 状态表

| 模块 | 当前状态 | 已有证据 / gate | 主要位置 |
|---|---|---|---|
| C00 软件与测试基线 | 已实现 | 构建、testthat、R CMD check、固定环境记录已有历史证据 | <code>docs/implementation/03_C00_C04_ALGORITHMS.md</code> |
| C01 稳定 probit + Newton–Laplace | <code>main</code> 已实现；舍入平台修复在分支 | 单列 oracle、梯度/Hessian、q=0/q=1 数值积分历史门；芬兰修复后 702 列成功 | <code>src/ct_probit.cpp</code>；<code>impl/finland-q1-explore-20261110</code> |
| C02 合成数据合同 | 已实现 | 身份、排序、稀疏、训练配方、指纹等检查 | <code>R/cat-trace-data.R</code> |
| 真实数据身份/分组合同 | 部分实现 | Finland/Malagasy 数据任务已有专门口径；真实目录仍逐数据冻结 | 数据决策与实现分支 |
| 匿名零槽 q=0 | 已实现为 reference backend | 直接一维积分、误差估计 | <code>R/cat-trace-zero-slot.R</code> |
| 匿名零槽 q=1 | 已实现为 reference backend | 嵌套积分、误差传播；Task 021/022 历史审计 | 同上 |
| 匿名零槽 q>1 / 生产梯度 | 未实现 | Blueprint 正在设计；<code>main</code> 对 q>1 返回 unsupported | 同上 |
| C03 共享参数 profile–Laplace | 部分实现 | q=0/q=1 reference-only 路线、Richardson、最终 Hessian、2000 hyper draws | <code>R/cat-trace-fit.R</code> |
| C03 极端优化点保护 | 分支实现 | 解析超先验上界拒绝、部分目标上界拒绝 | <code>impl/malagasy-pilot-20261110</code> |
| C04 Albert–Chib reference MCMC | 已实现，可靠性门未全过 | C1–C7 全过；F1 40k 后两项 bulk ESS 未过 | <code>R/cat-trace-reference.R</code>；<code>results/c04-ref--z-collapsed-composition-repair/</code> |
| 有限目录 q=1 合成闭环 | 实现分支完成代码，正式作业状态以结果记录为准 | 目录身份、全零列、有限截距层级、条件列抽样、发现曲线 | <code>impl/catalogue-v1-20261110</code> |
| 同组目录零列精确聚合 | 分支实现 | 同组一原型×重数；错组拒绝 | <code>impl/malagasy-pilot-20261110/package/TRACE/R/cat-trace-catalogue-v1-fit.R</code> |
| 显式目录重新检出 | <code>main</code> 已实现 | 累积至少一次概率；训练已见列排除 | <code>R/cat-trace-predict.R</code> |
| 匿名尾部首次发现 | q=1 分支实现 | 正分子积分；与目录使用同一共享抽样合并 | <code>cat-trace-catalogue-v1-integrate.R</code> / <code>predict.R</code> |
| Trait | 模型冻结，生产实现后置 | 需要完整对齐性状；当前不隐藏插补 | Canonical §8.7 / Code Plan stage 6 |
| \(C^{tax}\) relatedness | 数据构造方向已定，生产联合推断未闭合 | SW Australia 可复现 taxonomy proxy；需 overlap report | Canonical §8.8 / C08 |
| 真正 \(C^{phy}\) | 未进入真实主分析 | 当前三个核心真实数据尚无已冻结带枝长树 | Canonical / C08 |
| C09 残差因子 copula | 未闭合 | cut architecture、PSD/单位对角方向冻结；具体 pairwise/factor 推断仍需设计 | C09 设计文件 |
| 大 \(p\) 扩展 | 探索性部分实现，正式路线未证明 | 稀疏存储、分块/并行适配器、实测成本；Malagasy 三目预算超限 | <code>impl/malagasy-pilot-20261110</code>、实测成本文档 |
| 第一篇论文三项真实数据 | 数据角色冻结，端到端方法尚未全部完成 | Finland、Malagasy、SW Australia | Canonical §13 |

## 30. 已经可以放心讲的部分

目前最稳固的是模型语义和底层数值结构：目录/开放尾部的身份区分、共享分组响应、TRACE 尾部校准、边际 probit 解释、C01 Cholesky–Newton–Laplace、q=0/q=1 匿名零槽参考积分、共享参数低维 profile 结构，以及 Albert–Chib 作为小规模独立参照的定位。

实现证据也已经说明一个重要事实：零槽重数本身不是大数据瓶颈。匿名槽位和同组目录零列都可以在保持统计目标的前提下聚合。当前主要成本来自“为了得到共享参数梯度，重复执行大量完整 profile 求值”。

## 31. 仍属于“部分完成”的部分

目录第一版、匿名尾部首次发现和真实数据加速已经在 11 月实现分支中出现，但它们还没有统一回到 <code>main</code> 的公开 API。q>1 零槽、C09 残差依赖和真正可扩展的大 \(p\) 生产路线也还没有完成。

因此当前 CAT-TRACE 已经具备相当完整的模型定义和一条可运行的小/中规模计算骨架，但还没有形成“任意 q、完整目录、残差依赖、几十万列”一次性通用的最终生产引擎。

---

# 第五部分：术语表

## 32. 模型与数据对象

**\(\mathcal K\)（目录）**：有限、具名、可复现匹配的分析用身份集合。  
**\(\mathcal U\)（开放尾部）**：目录之外、理论上可以继续增长的特征空间。  
**\(g\)（组）**：分类或功能上的粗粒度生物标记，与目录/开放尾部身份状态正交。  
**\(p_g\)**：第 \(g\) 组开放尾部的有限计算截断。  
**\(p_g^*\)**：训练期已经出现过的第 \(g\) 组开放尾部列数。  
**\(m_g=p_g-p_g^*\)**：匿名全零槽位重数。  
**目录零列**：目录身份已知，但训练期观测全为零的具名列。  
**匿名零槽**：身份未知、训练期全零、用于容纳未来目录外发现的潜在尾部列。  
**\(\nu\)**：所有组共享的总体环境响应。  
**\(a_g\)**：第 \(g\) 组相对总体的环境响应偏移，和为零。  
**\(\Psi\)**：物种层环境响应残差的协方差；第一版为共享对角矩阵。  
**\(\gamma_0\)**：总体开放尾部强度。  
**\(\pi_g\)**：中心化协变量条件下的尾部组份额。  
**\(\gamma_g=\gamma_0\pi_g\)**：第 \(g\) 组开放尾部基线强度。  
**\(T\) / trait**：具名目录物种的性状输入。  
**\(C^{tax}\)**：分类体系构造的 relatedness proxy。  
**\(C^{phy}\)**：真正带分支长度系统发育树导出的相关矩阵。  
**\(\mathcal W\)**：显式估计残差依赖的有限工作集合。

## 33. 数值与推断术语

**Laplace 近似**：在后验众数附近用二次曲面近似积分和局部后验。  
**Newton 法**：利用梯度和 Hessian 的局部二阶信息直接计算参数更新方向。  
**Cholesky 分解**：把正定矩阵写成 \(R^\top R\)，用于稳定求解、log-determinant、协方差和高斯抽样。  
**Newton decrement**：\(\sqrt{g^\top H^{-1}g}\)，按局部曲率标准化后的驻点距离。  
**Armijo 回溯**：要求候选步取得足够目标上升，不满足时逐步缩短步长。  
**剖面目标**：给定共享参数后重新解决所有低层列问题，再把列贡献压缩成共享参数上的低维目标。  
**Richardson 外推**：用不同差分步长组合，降低有限差分主导截断误差。  
**BFGS**：用连续梯度差逐步近似曲率的准 Newton 外层优化器。  
**Hessian 白化比较**：在一个 Hessian 的自然曲率坐标中比较另一个 Hessian 的广义特征值，检查所有方向的相对稳定性。  
**Helmert 基**：把和为零的 \(G\) 组效应表示成 \(G-1\) 个正交自由坐标。  
**softmax / share logits**：把无约束自由坐标映射到和为 1 的组份额。  
**Albert–Chib**：probit 的潜在高斯数据增广 MCMC。  
**interweaving**：在保持同一目标分布的前提下切换中心化/非中心化参数化，提高耦合参数的移动效率。  
**Z-collapsed 组成更新**：对组份额更新时把 latent \(Z\) 精确积分掉，直接使用观测 probit 似然。  
**Rhat**：多链位置/尺度一致性诊断。  
**bulk ESS**：分布主体的有效独立样本数。  
**tail ESS**：尾部/分位数的有效独立样本数。  
**MCSE**：有限 MCMC 抽样造成的蒙特卡洛误差。  
**finite-\(p\) estimand**：固定当前截断 \(p_g\) 后实际拟合的统计目标。  
**cut architecture**：第二阶段依赖模块读取第一阶段边际结果，但不把信息反向更新回边际回归。

---

# 第六部分：当前真正需要关注的疑点

以下只列问题和证据位置，不在本文中替项目做新设计。

## 34. C01 的芬兰舍入平台修复尚未合入 main

<code>main:package/TRACE/src/ct_probit.cpp:181-184</code> 仍直接按 Armijo 不等式接受 trial；<code>impl/finland-q1-explore-20261110:package/TRACE/src/ct_probit.cpp:223-229</code> 增加了 rounded plateau 拒绝。实测修复使原失败列从 100 次上限转为 8 次收敛，并通过完整测试，但写作基线的 <code>main</code> 还没有这段修复。

这意味着“当前仓库主线 C01”与“已经验证的最新 C01 行为”存在分支差异。后续合并时需要保持回归夹具和失败语义一致。

## 35. 极端 \(\gamma\) 的 TRACE 尾参数映射仍有浮点边界

<code>main:package/TRACE/R/cat-trace-reference.R:1-4</code> 直接计算 <code>qnorm(gamma/(gamma+p_tail))</code>。芬兰 G1 重跑在 <code>results/finland_q1_explore/C01_FIX_ZH.md:113-117</code> 实际走到 \(\log\gamma_0=547.756\ldots\)，此时 double 中 \(\gamma/(\gamma+p)=1\)，导致 <code>qnorm(1)=Inf</code>，最终返回 <code>CT_INPUT_INVALID</code>。

马达加斯加分支的 <code>cat-trace-optimizer-bound.R:1-14</code> 已增加上界拒绝以避免明显不可能改进的极端试探点，但这属于优化器保护；尾参数映射本身的稳定表达仍需要单独冻结合同。

## 36. FROZEN V2 中的 1%/2% 截断建议已经被后续 C06 合同修正

Canonical 文件 <code>CAT_TRACE_CANONICAL_NOTATION_AND_ARCHITECTURE_20260909.md:794</code> 仍写着 95% 后验分位数约 1%、相邻截断摘要约 2% 的建议。后续权威实现合同 <code>11_R1_TRUNCATION_CATALOGUE_SCALABILITY_GATES.md:28-35</code> 已明确“1% 不再是普遍自动通过线”，正式 S1B/C06 接受标准必须预注册。

模型定义没有冲突，但文档层存在旧默认仍留在 Canonical 的风险。论文或最终用户文档应采用“finite-\(p\) / fixed-parameter asymptotic gap / refit stability 三分”的新口径。

## 37. 旧 C01 收敛合同与当前代码的实际指标已经不同

<code>docs/implementation/09_R1_EXECUTION_LEVEL_NUMERICAL_CONTRACTS.md:167-195</code> 把梯度门写成逐坐标标准化 \(G\)，并把目标变化 \(F\) 写成相对变化。当前 <code>main:package/TRACE/src/ct_probit.cpp:202-204</code> 使用 Newton decrement \(D\)、相对参数变化 \(P\) 和**绝对**目标变化 \(|h_{new}-h_{old}|\)。

这是算法演变留下的文档漂移。最新代码和后续架构记录已经采用 Cholesky-whitened Newton decrement，但 09 文档仍容易让读者或实现者误以为旧合同是现行机器规格。

## 38. 匿名零槽的通用生产算法仍没有落地到 main

<code>main:package/TRACE/R/cat-trace-zero-slot.R:94-95</code> 明确只接受 q=0/q=1，<code>:116-117</code> 只接受 <code>derivative_order=0</code>。这已经足够支撑 reference-only C03 和当前 q=1 探索，但不能承担一般 \(q>1\) 的生产共享参数梯度/Hessian。

实测又显示数值梯度是当前最大成本乘数，因此 q>1 零槽积分与其解析/半解析导数路线会直接决定 C10 是否真正可扩展。

## 39. Albert–Chib 参考引擎尚未通过冻结的完整可靠性门

<code>main:results/c04-ref--z-collapsed-composition-repair/result.md:3</code> 记录 C1–C7 正确性门全部通过，但 40000 retained draws/chain 后 combined reliability 仍失败。具体 <code>group_share[g3]</code> 的 bulk ESS 为 690.34（<code>:86-88</code>），<code>share_logit[g2]</code> 也只有约 632。

因此它目前适合做“小问题上的独立计算参照”，但不能无条件把每个共享参数都当成已经达到冻结精度的 MCMC 金标准。

## 40. main 的公开预测语义还没有包含匿名尾部首次发现

<code>main:package/TRACE/R/cat-trace-predict.R:52-54</code> 明确写着 <code>includes_anonymous_open_tail=FALSE</code>。目录第一版分支已经实现 q=1 条件零槽首次发现正积分和同共享抽样合并，但尚未形成 <code>main</code> 通用预测接口。

这不是模型缺口，而是实现整合边界：论文若开始直接引用匿名尾部未来发现结果，需要绑定到明确的实现分支/版本，避免把分支原型当成主线公开 API。

---

## 41. 最后用一句话串起来

CAT-TRACE 的模型主线已经稳定：用有限目录表示“身份已知但可能尚未见”的对象，用 TRACE 校准的分组开放尾部表示真正目录外的新发现，二者共享可解释的环境响应层级，再把残差依赖放到不改变边际 probit 的第二阶段。当前工程工作的主要难点已经从“模型是什么”转成“如何在保持这个统计目标不变的前提下，把共享参数梯度、零槽积分、目录全零列和几十万显式列算得足够稳、足够快，并由独立参考路线证明近似没有悄悄改变答案”。
