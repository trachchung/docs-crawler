<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#__docusaurus_skipToContent_fallback)
On this page
Simple Preference Optimization for LLM alignment. Reference-free alternative to DPO with better performance (+6.4 points on AlpacaEval 2.0). No reference model needed, more efficient than DPO. Use for preference alignment when want simpler, faster training than DPO/PPO.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#skill-metadata "Direct link to Skill metadata")  
| Source  | Optional — install with `hermes skills install official/mlops/simpo`  |  
| --- | --- |  
| Path  | `optional-skills/mlops/simpo`  |  
| Version  | `1.0.0`  |  
| Author  | Orchestra Research  |  
| License  | MIT  |  
| Dependencies  |  `torch`, `transformers`, `datasets`, `trl`, `accelerate`  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `Post-Training`, `SimPO`, `Preference Optimization`, `Alignment`, `DPO Alternative`, `Reference-Free`, `LLM Alignment`, `Efficient Training`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# SimPO - Simple Preference Optimization
## Quick start[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#quick-start "Direct link to Quick start")
SimPO is a reference-free preference optimization method that outperforms DPO without needing a reference model.
**Installation** :

```
# Create environmentconda create -n simpo python=3.10&& conda activate simpo# Install PyTorch 2.2.2# Visit: https://pytorch.org/get-started/locally/# Install alignment-handbookgit clone https://github.com/huggingface/alignment-handbook.gitcd alignment-handbookpython -m pip install.# Install Flash Attention 2python -m pip install flash-attn --no-build-isolation
```

**Training** (Mistral 7B):

```
ACCELERATE_LOG_LEVEL=info accelerate launch \--config_file accelerate_configs/deepspeed_zero3.yaml \  scripts/run_simpo.py \  training_configs/mistral-7b-base-simpo.yaml
```

## Common workflows[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#common-workflows "Direct link to Common workflows")
### Workflow 1: Train from base model (Mistral 7B)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#workflow-1-train-from-base-model-mistral-7b "Direct link to Workflow 1: Train from base model \(Mistral 7B\)")
**Config** (`mistral-7b-base-simpo.yaml`):

```
# Modelmodel_name_or_path: mistralai/Mistral-7B-v0.1torch_dtype: bfloat16# Datasetdataset_mixer:HuggingFaceH4/ultrafeedback_binarized:1.0dataset_splits:- train_prefs- test_prefs# SimPO hyperparametersbeta:2.0# Reward scaling (2.0-10.0)gamma_beta_ratio:0.5# Target margin (0-1)loss_type: sigmoid          # sigmoid or hingesft_weight:0.0# Optional SFT regularization# Traininglearning_rate:5e-7# Critical: 3e-7 to 1e-6num_train_epochs:1per_device_train_batch_size:1gradient_accumulation_steps:8# Outputoutput_dir: ./outputs/mistral-7b-simpo
```

**Launch training** :

```
accelerate launch --config_file accelerate_configs/deepspeed_zero3.yaml \  scripts/run_simpo.py training_configs/mistral-7b-base-simpo.yaml
```

### Workflow 2: Fine-tune instruct model (Llama 3 8B)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#workflow-2-fine-tune-instruct-model-llama-3-8b "Direct link to Workflow 2: Fine-tune instruct model \(Llama 3 8B\)")
**Config** (`llama3-8b-instruct-simpo.yaml`):

```
model_name_or_path: meta-llama/Meta-Llama-3-8B-Instructdataset_mixer:argilla/ultrafeedback-binarized-preferences-cleaned:1.0beta:2.5gamma_beta_ratio:0.5learning_rate:5e-7sft_weight:0.1# Add SFT loss to preserve capabilitiesnum_train_epochs:1per_device_train_batch_size:2gradient_accumulation_steps:4output_dir: ./outputs/llama3-8b-simpo
```

**Launch** :

```
accelerate launch --config_file accelerate_configs/deepspeed_zero3.yaml \  scripts/run_simpo.py training_configs/llama3-8b-instruct-simpo.yaml
```

### Workflow 3: Reasoning-intensive tasks (lower LR)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#workflow-3-reasoning-intensive-tasks-lower-lr "Direct link to Workflow 3: Reasoning-intensive tasks \(lower LR\)")
**For math/code tasks** :

```
model_name_or_path: deepseek-ai/deepseek-math-7b-basedataset_mixer:argilla/distilabel-math-preference-dpo:1.0beta:5.0# Higher for stronger signalgamma_beta_ratio:0.7# Larger marginlearning_rate:3e-7# Lower LR for reasoningsft_weight:0.0num_train_epochs:1per_device_train_batch_size:1gradient_accumulation_steps:16
```

## When to use vs alternatives[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#when-to-use-vs-alternatives "Direct link to When to use vs alternatives")
**Use SimPO when** :
  * Want simpler training than DPO (no reference model)
  * Have preference data (chosen/rejected pairs)
  * Need better performance than DPO
  * Limited compute resources
  * Single-node training sufficient


**Algorithm selection** :
  * **SimPO** : Simplest, best performance, no reference model
  * **DPO** : Need reference model baseline, more conservative
  * **PPO** : Maximum control, need reward model, complex setup
  * **GRPO** : Memory-efficient RL, no critic


**Use alternatives instead** :
  * **OpenRLHF** : Multi-node distributed training, PPO/GRPO
  * **TRL** : Need multiple methods in one framework
  * **DPO** : Established baseline comparison


## Common issues[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#common-issues "Direct link to Common issues")
**Issue: Loss divergence**
Reduce learning rate:

```
learning_rate:3e-7# Reduce from 5e-7
```

Reduce beta:

```
beta:1.0# Reduce from 2.0
```

**Issue: Model forgets capabilities**
Add SFT regularization:

```
sft_weight:0.1# Add SFT loss component
```

**Issue: Poor preference separation**
Increase beta and margin:

```
beta:5.0# Increase from 2.0gamma_beta_ratio:0.8# Increase from 0.5
```

**Issue: OOM during training**
Reduce batch size:

```
per_device_train_batch_size:1gradient_accumulation_steps:16# Maintain effective batch
```

Enable gradient checkpointing:

```
gradient_checkpointing:true
```

## Advanced topics[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#advanced-topics "Direct link to Advanced topics")
**Loss functions** : See [references/loss-functions.md](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/mlops/simpo/references/loss-functions.md) for sigmoid vs hinge loss, mathematical formulations, and when to use each.
**Hyperparameter tuning** : See [references/hyperparameters.md](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/mlops/simpo/references/hyperparameters.md) for beta, gamma, learning rate selection guide, and model-size-specific recommendations.
**Dataset preparation** : See [references/datasets.md](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/mlops/simpo/references/datasets.md) for preference data formats, quality filtering, and custom dataset creation.
## Hardware requirements[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#hardware-requirements "Direct link to Hardware requirements")
  * **GPU** : NVIDIA A100/H100 recommended
  * **VRAM** : 
    * 7B model: 1× A100 40GB (DeepSpeed ZeRO-3)
    * 8B model: 2× A100 40GB
    * 70B model: 8× A100 80GB
  * **Single-node** : DeepSpeed ZeRO-3 sufficient
  * **Mixed precision** : BF16 recommended


**Memory optimization** :
  * DeepSpeed ZeRO-3 (default config)
  * Gradient checkpointing
  * Flash Attention 2


## Resources[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#resources "Direct link to Resources")
  * Paper: <https://arxiv.org/abs/2405.14734> (NeurIPS 2024)
  * GitHub: <https://github.com/princeton-nlp/SimPO>
  * Models: <https://huggingface.co/princeton-nlp>
  * Alignment Handbook: <https://github.com/huggingface/alignment-handbook>


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#reference-full-skillmd)
  * [Quick start](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#quick-start)
  * [Common workflows](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#common-workflows)
    * [Workflow 1: Train from base model (Mistral 7B)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#workflow-1-train-from-base-model-mistral-7b)
    * [Workflow 2: Fine-tune instruct model (Llama 3 8B)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#workflow-2-fine-tune-instruct-model-llama-3-8b)
    * [Workflow 3: Reasoning-intensive tasks (lower LR)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#workflow-3-reasoning-intensive-tasks-lower-lr)
  * [When to use vs alternatives](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#when-to-use-vs-alternatives)
  * [Common issues](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#common-issues)
  * [Advanced topics](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#advanced-topics)
  * [Hardware requirements](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo#hardware-requirements)


