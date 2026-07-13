---
name: ai-ml-imaging
description: AI/ML support for imaging workflows with PyTorch Lightning and Transformers.
status: active
provenance: generated
trusted: false
requires_network: true
writes_files: true
executes_code: false
secrets_needed:
  - HUGGINGFACE_TOKEN
last_reviewed: 2026-07-10
profile_tags:
recommended_scope: project
source_skills:
  - skills/tools/ai-ml/pytorch-lightning
  - skills/tools/ai-ml/transformers
default_prompt:
---

# ai-ml-imaging

## Trigger Boundary

AI/ML support for imaging workflows with PyTorch Lightning and Transformers.

Use this aggregate Codex App skill when the task matches one of the source workflows below.

## Source Workflows

- `pytorch-lightning`: Deep learning framework (PyTorch Lightning). Organize PyTorch code into LightningModules, configure Trainers for multi-GPU/TPU, implement data pipelines, callbacks, logging (W&B, TensorBoard), distributed training (DDP, FSDP, DeepSpeed), for scalable neural network training. Reference: `_src/lightning/source.md`
- `transformers`: This skill should be used when working with pre-trained transformer models for natural language processing, computer vision, audio, or multimodal tasks. Reference: `_src/hf/source.md`

## Workflow

1. Choose the source workflow whose trigger boundary best matches the user request.
2. Read that source workflow's `source.md` before acting.
3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.
4. Follow the source workflow unless the current project gives stricter instructions.
