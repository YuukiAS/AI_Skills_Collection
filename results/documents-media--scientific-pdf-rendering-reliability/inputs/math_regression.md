# Scientific PDF Math Regression

这是一份公开安全的中文/英文/数学混合渲染回归输入，用于验证默认正式笔记路线是否保留数学语义和可读排版。

Inline math next to Chinese text: 估计量 $\hat{x}_i$ should keep the hat and subscript. Greek notation $\alpha_i + \beta^2$ should remain mathematical text, not plain prose.

Display sum and integral:

$$
\sum_{i=1}^{n} w_i y_i + \int_0^1 f(t)\,dt = \mu
$$

Gradient and operators:

$$
\nabla_\theta \mathcal{L}(\theta) = X^\top (X\theta - y) + \lambda \theta
$$

Matrix and blackboard symbols:

$$
A =
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix},
\quad
v \in \mathbb{R}^{2}
$$

Long formula:

$$
\operatorname{argmin}_{\theta \in \mathbb{R}^{p}}
\left[
\frac{1}{2n}\sum_{i=1}^{n}(y_i - x_i^\top \theta)^2
+ \lambda \sum_{j=1}^{p}|\theta_j|
\right]
$$

| 指标 | 数值 | 说明 |
| --- | ---: | --- |
| Dice | 0.83 | 表格行应保留为可读列 |
| Error | 1.20 | 不应因为表格存在而缩小普通段落 |

The closing paragraph is ordinary prose. It should not be classified as a table line, and it should keep the same body-text identity as the earlier paragraphs.
