# ai-ml

Active skills: 7

## Install

Complete domain install:

```bash
python3 scripts/skills.py install --target repo --domain ai-ml --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
python3 scripts/skills.py install --target repo --skill tool/ai-ml/modal --skill tool/ai-ml/pufferlib --skill tool/ai-ml/pytorch-lightning --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `modal` (`skills/tools/ai-ml/modal`): Run Python code in the cloud with serverless containers, GPUs, and autoscaling. Use when deploying ML models, running batch processing jobs, scheduling compute-intensive tasks, or serving APIs that require GPU acceleration or dynamic scaling.
- `pufferlib` (`skills/tools/ai-ml/pufferlib`): High-performance reinforcement learning framework optimized for speed and scale. Use when you need fast parallel training, vectorized environments, multi-agent systems, or integration with game environments (Atari, Procgen, NetHack).
- `pytorch-lightning` (`skills/tools/ai-ml/pytorch-lightning`): Deep learning framework (PyTorch Lightning). Organize PyTorch code into LightningModules, configure Trainers for multi-GPU/TPU, implement data pipelines, callbacks, logging (W&B, TensorBoard), distributed training (DDP, FSDP, DeepSpeed), for scalable neural network training.
- `stable-baselines3` (`skills/tools/ai-ml/stable-baselines3`): Production-ready reinforcement learning algorithms (PPO, SAC, DQN, TD3, DDPG, A2C) with scikit-learn-like API. Use for standard RL experiments, quick prototyping, and well-documented algorithm implementations.
- `timesfm-forecasting` (`skills/tools/ai-ml/timesfm-forecasting`): Zero-shot time series forecasting with Google's TimesFM foundation model. Use for any univariate time series (sales, sensors, energy, vitals, weather) without training a custom model.
- `torch-geometric` (`skills/tools/ai-ml/torch-geometric`): Graph Neural Networks (PyG). Node/graph classification, link prediction, GCN, GAT, GraphSAGE, heterogeneous graphs, molecular property prediction, for geometric deep learning.
- `transformers` (`skills/tools/ai-ml/transformers`): This skill should be used when working with pre-trained transformer models for natural language processing, computer vision, audio, or multimodal tasks.

## Main References

- No domain references discovered yet. Add `references/source-notes.md`, checklists, or overview notes when the skill carries long-lived domain knowledge.
