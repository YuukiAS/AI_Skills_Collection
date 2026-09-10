# 待核对文本

FedAvg 在同一划分设置下得到 Dice=0.81，HD95=7.4 mm。训练脚本是 `scripts/train_fedavg.py`，配置文件是 `configs/fedavg.yaml`。当前损失函数写作 $\mathcal{L}=\mathcal{L}_{seg}+0.1\mathcal{L}_{reg}$，但这个正则项只用于 FedAvg 消融实验，不能写成所有方法共享设置。
