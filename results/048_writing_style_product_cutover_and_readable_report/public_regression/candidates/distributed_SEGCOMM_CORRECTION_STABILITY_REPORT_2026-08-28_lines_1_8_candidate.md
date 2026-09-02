# CARE 分割通信 correction + stability 实验报告（2026-08-28）

## 30 秒版本

这一轮实验先修正了上一轮中最关键的两个混杂因素：whole-myocardium 的计算现在按 `{1,4,5}` 合并；FedAvg 中每个 client 的 AdamW optimizer state 也会在通信轮之间持续保留。除这两点外，实验条件保持一致：仍然使用 CARE fold-0、同一个 checkpoint、LGE-only 输入、7 个真实 center/client，并让每个 client 执行 20 次本地更新。

修正后的结果支持一个更细的判断。decoder pooled 相比原始 checkpoint 的改善最稳定；full-model pooled 也显示改善趋势，但不同 seed 之间的波动更大。decoder 设置下，FedAvg R=1/R=5 仍低于 pooled，one-shot gap 的方向稳定。full-model 设置下，R=1/R=5 的 scar Dice 反而达到或略高于 pooled 的跨 seed 平均，不过这个优势并没有在每个 seed 上都稳定出现。把通信量增加到 5 倍的 R=5 没有稳定优于 R=1，所以在当前小预算下，还看不出 few-round 通信有明确的性价比优势。
