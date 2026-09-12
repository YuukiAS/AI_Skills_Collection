# Karatsuba 算法（卡拉楚巴乘法）

Karatsuba 算法是一种用于大整数乘法的快速算法。它把两个大数分别拆成高位和低位两部分，通过 3 次较小规模的乘法，再配合加法、减法和移位，得到原来的乘积。对较小的乘法继续采用同样的分解，就形成了递归计算。

该算法由阿纳托利·阿列克谢耶维奇·卡拉楚巴（Anatoly Karatsuba）于 1960 年提出，并于 1962 年发表，俄文名称为 Алгоритм Карацубы。[1–3] 它是第一个在渐进复杂度上优于小学长乘法的算法。

## 用三次乘法完成一次分解

设采用的进制为 $B$，在低位保留 $m$ 位，把两个整数写成

$$
x=x_1B^m+x_0,\qquad y=y_1B^m+y_0.
$$

其中，$x_1$、$y_1$ 是高位部分，$x_0$、$y_0$ 是低位部分；通常在位数的中间附近拆分，使每部分约有原来一半的位数。直接展开可得

$$
xy=x_1y_1B^{2m}+(x_1y_0+x_0y_1)B^m+x_0y_0.
$$

如果逐项计算，需要做 4 次乘法。Karatsuba 算法利用两部分之和的乘积，求出中间的交叉项：

$$
\begin{aligned}
z_2&=x_1y_1,\\
z_0&=x_0y_0,\\
z_1&=(x_1+x_0)(y_1+y_0)-z_2-z_0.
\end{aligned}
$$

因为 $z_1=x_1y_0+x_0y_1$，最终乘积就是

$$
xy=z_2B^{2m}+z_1B^m+z_0.
$$

这样只需计算高位乘积、低位乘积以及两部分之和的乘积，共 3 次乘法。乘以 $B^m$ 或 $B^{2m}$，对应在 $B$ 进制下向左移 $m$ 位或 $2m$ 位。

这 3 次乘法都可以继续递归分解，直到数足够小，直接相乘即可。例如，采用十进制时，只要某个因子小于 10，就可以直接计算；若输入带负号，可先处理符号，再递归计算非负整数的乘积。

## 计算 $12345\times6789$

取 $B=10$、$m=3$，也就是用 $B^m=1000$ 拆分：

$$
\begin{aligned}
12345&=12\times1000+345,\\
6789&=6\times1000+789.
\end{aligned}
$$

先求高位和低位的乘积：

$$
\begin{aligned}
z_2&=12\times6=72,\\
z_0&=345\times789=272205.
\end{aligned}
$$

第三次乘法使用各自高低两部分的和，再减去已经算出的两个乘积：

$$
\begin{aligned}
z_1&=(12+345)(6+789)-z_2-z_0\\
&=357\times795-72-272205\\
&=283815-72-272205\\
&=11538.
\end{aligned}
$$

把三部分放回各自的位置，便得到

$$
\begin{aligned}
12345\times6789
&=z_2\times1000^2+z_1\times1000+z_0\\
&=72\times1000^2+11538\times1000+272205\\
&=83810205.
\end{aligned}
$$

第三次乘法的因子是高低两部分之和，其输入范围不到前两次乘法输入范围的 2 倍，乘积的范围不到相应的 4 倍。若按基数 1000 分块保存中间结果，计算 $z_1$ 的两次减法时，必须计入前两次乘法产生的进位。

## 递归带来的复杂度改进

每层递归把一次大整数乘法转化为 3 次约一半位数的乘法，另加线性规模的加减和移位。按这种半规模分解分析，时间递归关系可写为

$$
T(n)=3T(n/2)+O(n),
$$

由此得到时间复杂度

$$
T(n)=O\!\left(n^{\log_2 3}\right)\approx O(n^{1.585}).
$$

对于两个 $n$ 位数，Karatsuba 算法所需的一位数乘法次数至多为

$$
3n^{\log_2 3}\approx3n^{1.585}.
$$

当 $n$ 是 2 的幂时，这一次数恰为 $n^{\log_2 3}$。普通长乘法则需要 $n^2$ 次一位数乘法。例如，两个 1024 位的数相乘时，$n=1024=2^{10}$，Karatsuba 算法需要

$$
3^{10}=59049
$$

次一位数乘法，而普通长乘法需要

$$
(2^{10})^2=1048576
$$

次。这里比较的是一位数乘法的次数。

Toom–Cook 算法是 Karatsuba 算法的更快推广。对于充分大的 $n$（$n\gg1$），Schönhage–Strassen 算法还要更快，其时间复杂度为

$$
O(n\log n\log\log n).
$$

## 参考文献与延伸阅读

1. A. Karatsuba and Yu. Ofman. “Multiplication of Many-Digital Numbers by Automatic Computers.” *Proceedings of the USSR Academy of Sciences*, 145, 1962, pp. 293–294.
2. A. A. Karatsuba. “[The Complexity of Computations](http://www.ccas.ru/personal/karatsuba/divcen.pdf).” *Proceedings of the Steklov Institute of Mathematics*, 211, 1995, pp. 169–183。另有 [2020 年 3 月 26 日的网页存档](https://web.archive.org/web/20200326194847/http://www.ccas.ru/personal/karatsuba/divcen.pdf)。
3. D. E. Knuth. *The Art of Computer Programming*, Vol. 2. Addison-Wesley, 1969, 724 页。

以下资料提供了进一步说明：

- [Karatsuba's Algorithm for Polynomial Multiplication](http://www.cs.pitt.edu/~kirk/cs1501/animations/Karatsuba.html)：卡拉楚巴多项式乘法的动画演示，另有 [2012 年 9 月 11 日的网页存档](https://web.archive.org/web/20120911081709/http://www.cs.pitt.edu/~kirk/cs1501/animations/Karatsuba.html)。
- [Karatsuba Multiplication](https://mathworld.wolfram.com/KaratsubaMultiplication.html)：MathWorld 的卡拉楚巴乘法条目。
- D. J. Bernstein, “[Multidigit multiplication for mathematicians](http://cr.yp.to/papers/m3.pdf)”：介绍 Karatsuba 及其他多种乘法算法，另有 [2006 年 7 月 21 日的网页存档](https://web.archive.org/web/20060721035521/http://cr.yp.to/papers/m3.pdf)。
