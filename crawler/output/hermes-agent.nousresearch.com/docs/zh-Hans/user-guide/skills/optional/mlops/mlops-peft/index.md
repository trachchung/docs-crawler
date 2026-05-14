<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft -->

本页总览
Parameter-efficient fine-tuning for LLMs using LoRA, QLoRA, and 25+ methods. Use when fine-tuning large models (7B-70B) with limited GPU memory, when you need to train <1% of parameters with minimal accuracy loss, or for multi-adapter serving. HuggingFace's official library integrated with transformers ecosystem.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#skill-metadata "Skill metadata的直接链接")  
| Source  | Optional — install with `hermes skills install official/mlops/peft`  |  
| --- | --- |  
| Path  | `optional-skills/mlops/peft`  |  
| Version  | `1.0.0`  |  
| Author  | Orchestra Research  |  
| License  | MIT  |  
| Dependencies  |  `peft>=0.13.0`, `transformers>=4.45.0`, `torch>=2.0.0`, `bitsandbytes>=0.43.0`  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `Fine-Tuning`, `PEFT`, `LoRA`, `QLoRA`, `Parameter-Efficient`, `Adapters`, `Low-Rank`, `Memory Optimization`, `Multi-Adapter`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# PEFT (Parameter-Efficient Fine-Tuning)
Fine-tune LLMs by training <1% of parameters using LoRA, QLoRA, and 25+ adapter methods.
## When to use PEFT[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#when-to-use-peft "When to use PEFT的直接链接")
**Use PEFT/LoRA when:**
  * Fine-tuning 7B-70B models on consumer GPUs (RTX 4090, A100)
  * Need to train <1% parameters (6MB adapters vs 14GB full model)
  * Want fast iteration with multiple task-specific adapters
  * Deploying multiple fine-tuned variants from one base model


**Use QLoRA (PEFT + quantization) when:**
  * Fine-tuning 70B models on single 24GB GPU
  * Memory is the primary constraint
  * Can accept ~5% quality trade-off vs full fine-tuning


**Use full fine-tuning instead when:**
  * Training small models (<1B parameters)
  * Need maximum quality and have compute budget
  * Significant domain shift requires updating all weights


## Quick start[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#quick-start "Quick start的直接链接")
### Installation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#installation "Installation的直接链接")

```
# Basic installationpip install peft# With quantization support (recommended)pip install peft bitsandbytes# Full stackpip install peft transformers accelerate bitsandbytes datasets
```

### LoRA fine-tuning (standard)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#lora-fine-tuning-standard "LoRA fine-tuning \(standard\)的直接链接")

```
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainerfrom peft import get_peft_model, LoraConfig, TaskTypefrom datasets import load_dataset# Load base modelmodel_name ="meta-llama/Llama-3.1-8B"model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")tokenizer = AutoTokenizer.from_pretrained(model_name)tokenizer.pad_token = tokenizer.eos_token# LoRA configurationlora_config = LoraConfig(    task_type=TaskType.CAUSAL_LM,    r=16,# Rank (8-64, higher = more capacity)    lora_alpha=32,# Scaling factor (typically 2*r)    lora_dropout=0.05,# Dropout for regularization    target_modules=["q_proj","v_proj","k_proj","o_proj"],# Attention layers    bias="none"# Don't train biases# Apply LoRAmodel = get_peft_model(model, lora_config)model.print_trainable_parameters()# Output: trainable params: 13,631,488 || all params: 8,043,307,008 || trainable%: 0.17%# Prepare datasetdataset = load_dataset("databricks/databricks-dolly-15k", split="train")deftokenize(example):    text =f"### Instruction:\n{example['instruction']}\n\n### Response:\n{example['response']}"return tokenizer(text, truncation=True, max_length=512, padding="max_length")tokenized = dataset.map(tokenize, remove_columns=dataset.column_names)# Trainingtraining_args = TrainingArguments(    output_dir="./lora-llama",    num_train_epochs=3,    per_device_train_batch_size=4,    gradient_accumulation_steps=4,    learning_rate=2e-4,    fp16=True,    logging_steps=10,    save_strategy="epoch"trainer = Trainer(    model=model,    args=training_args,    train_dataset=tokenized,    data_collator=lambda data:{"input_ids": torch.stack([f["input_ids"]for f in data]),"attention_mask": torch.stack([f["attention_mask"]for f in data]),"labels": torch.stack([f["input_ids"]for f in data])}trainer.train()# Save adapter only (6MB vs 16GB)model.save_pretrained("./lora-llama-adapter")
```

### QLoRA fine-tuning (memory-efficient)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#qlora-fine-tuning-memory-efficient "QLoRA fine-tuning \(memory-efficient\)的直接链接")

```
from transformers import AutoModelForCausalLM, BitsAndBytesConfigfrom peft import get_peft_model, LoraConfig, prepare_model_for_kbit_training# 4-bit quantization configbnb_config = BitsAndBytesConfig(    load_in_4bit=True,    bnb_4bit_quant_type="nf4",# NormalFloat4 (best for LLMs)    bnb_4bit_compute_dtype="bfloat16",# Compute in bf16    bnb_4bit_use_double_quant=True# Nested quantization# Load quantized modelmodel = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.1-70B",    quantization_config=bnb_config,    device_map="auto"# Prepare for training (enables gradient checkpointing)model = prepare_model_for_kbit_training(model)# LoRA config for QLoRAlora_config = LoraConfig(    r=64,# Higher rank for 70B    lora_alpha=128,    lora_dropout=0.1,    target_modules=["q_proj","v_proj","k_proj","o_proj","gate_proj","up_proj","down_proj"],    bias="none",    task_type="CAUSAL_LM"model = get_peft_model(model, lora_config)# 70B model now fits on single 24GB GPU!
```

## LoRA parameter selection[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#lora-parameter-selection "LoRA parameter selection的直接链接")
### Rank (r) - capacity vs efficiency[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#rank-r---capacity-vs-efficiency "Rank \(r\) - capacity vs efficiency的直接链接")  
| Rank  | Trainable Params  | Memory  | Quality  | Use Case  |  
| --- | --- | --- | --- | --- |  
| 4  | ~3M  | Minimal  | Lower  | Simple tasks, prototyping  |  
| ~7M  | Low  | Good  | **Recommended starting point**  |  
| **16**  | ~14M  | Medium  | Better  | **General fine-tuning**  |  
| 32  | ~27M  | Higher  | High  | Complex tasks  |  
| 64  | ~54M  | High  | Highest  | Domain adaptation, 70B models  |  
### Alpha (lora_alpha) - scaling factor[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#alpha-lora_alpha---scaling-factor "Alpha \(lora_alpha\) - scaling factor的直接链接")

```
# Rule of thumb: alpha = 2 * rankLoraConfig(r=16, lora_alpha=32)# StandardLoraConfig(r=16, lora_alpha=16)# Conservative (lower learning rate effect)LoraConfig(r=16, lora_alpha=64)# Aggressive (higher learning rate effect)
```

### Target modules by architecture[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#target-modules-by-architecture "Target modules by architecture的直接链接")

```
# Llama / Mistral / Qwentarget_modules =["q_proj","v_proj","k_proj","o_proj","gate_proj","up_proj","down_proj"]# GPT-2 / GPT-Neotarget_modules =["c_attn","c_proj","c_fc"]# Falcontarget_modules =["query_key_value","dense","dense_h_to_4h","dense_4h_to_h"]# BLOOMtarget_modules =["query_key_value","dense","dense_h_to_4h","dense_4h_to_h"]# Auto-detect all linear layerstarget_modules ="all-linear"# PEFT 0.6.0+
```

## Loading and merging adapters[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#loading-and-merging-adapters "Loading and merging adapters的直接链接")
### Load trained adapter[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#load-trained-adapter "Load trained adapter的直接链接")

```
from peft import PeftModel, AutoPeftModelForCausalLMfrom transformers import AutoModelForCausalLM# Option 1: Load with PeftModelbase_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.1-8B")model = PeftModel.from_pretrained(base_model,"./lora-llama-adapter")# Option 2: Load directly (recommended)model = AutoPeftModelForCausalLM.from_pretrained("./lora-llama-adapter",    device_map="auto"
```

### Merge adapter into base model[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#merge-adapter-into-base-model "Merge adapter into base model的直接链接")

```
# Merge for deployment (no adapter overhead)merged_model = model.merge_and_unload()# Save merged modelmerged_model.save_pretrained("./llama-merged")tokenizer.save_pretrained("./llama-merged")# Push to Hubmerged_model.push_to_hub("username/llama-finetuned")
```

### Multi-adapter serving[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#multi-adapter-serving "Multi-adapter serving的直接链接")

```
from peft import PeftModel# Load base with first adaptermodel = AutoPeftModelForCausalLM.from_pretrained("./adapter-task1")# Load additional adaptersmodel.load_adapter("./adapter-task2", adapter_name="task2")model.load_adapter("./adapter-task3", adapter_name="task3")# Switch between adapters at runtimemodel.set_adapter("task1")# Use task1 adapteroutput1 = model.generate(**inputs)model.set_adapter("task2")# Switch to task2output2 = model.generate(**inputs)# Disable adapters (use base model)with model.disable_adapter():    base_output = model.generate(**inputs)
```

## PEFT methods comparison[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#peft-methods-comparison "PEFT methods comparison的直接链接")  
| Method  | Trainable %  | Memory  | Speed  | Best For  |  
| --- | --- | --- | --- | --- |  
| **LoRA**  | 0.1-1%  | Low  | Fast  | General fine-tuning  |  
| **QLoRA**  | 0.1-1%  | Very Low  | Medium  | Memory-constrained  |  
| AdaLoRA  | 0.1-1%  | Low  | Medium  | Automatic rank selection  |  
| IA3  | 0.01%  | Minimal  | Fastest  | Few-shot adaptation  |  
| Prefix Tuning  | 0.1%  | Low  | Medium  | Generation control  |  
| Prompt Tuning  | 0.001%  | Minimal  | Fast  | Simple task adaptation  |  
| P-Tuning v2  | 0.1%  | Low  | Medium  | NLU tasks  |  
### IA3 (minimal parameters)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#ia3-minimal-parameters "IA3 \(minimal parameters\)的直接链接")

```
from peft import IA3Configia3_config = IA3Config(    target_modules=["q_proj","v_proj","k_proj","down_proj"],    feedforward_modules=["down_proj"]model = get_peft_model(model, ia3_config)# Trains only 0.01% of parameters!
```

### Prefix Tuning[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#prefix-tuning "Prefix Tuning的直接链接")

```
from peft import PrefixTuningConfigprefix_config = PrefixTuningConfig(    task_type="CAUSAL_LM",    num_virtual_tokens=20,# Prepended tokens    prefix_projection=True# Use MLP projectionmodel = get_peft_model(model, prefix_config)
```

## Integration patterns[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#integration-patterns "Integration patterns的直接链接")
### With TRL (SFTTrainer)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#with-trl-sfttrainer "With TRL \(SFTTrainer\)的直接链接")

```
from trl import SFTTrainer, SFTConfigfrom peft import LoraConfiglora_config = LoraConfig(r=16, lora_alpha=32, target_modules="all-linear")trainer = SFTTrainer(    model=model,    args=SFTConfig(output_dir="./output", max_seq_length=512),    train_dataset=dataset,    peft_config=lora_config,# Pass LoRA config directlytrainer.train()
```

### With Axolotl (YAML config)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#with-axolotl-yaml-config "With Axolotl \(YAML config\)的直接链接")

```
# axolotl config.yamladapter: loralora_r:16lora_alpha:32lora_dropout:0.05lora_target_modules:- q_proj- v_proj- k_proj- o_projlora_target_linear:true# Target all linear layers
```

### With vLLM (inference)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#with-vllm-inference "With vLLM \(inference\)的直接链接")

```
from vllm import LLMfrom vllm.lora.request import LoRARequest# Load base model with LoRA supportllm = LLM(model="meta-llama/Llama-3.1-8B", enable_lora=True)# Serve with adapteroutputs = llm.generate(    prompts,    lora_request=LoRARequest("adapter1",1,"./lora-adapter")
```

## Performance benchmarks[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#performance-benchmarks "Performance benchmarks的直接链接")
### Memory usage (Llama 3.1 8B)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#memory-usage-llama-31-8b "Memory usage \(Llama 3.1 8B\)的直接链接")  
| Method  | GPU Memory  | Trainable Params  |  
| --- | --- | --- |  
| Full fine-tuning  | 60+ GB  | 8B (100%)  |  
| LoRA r=16  | 18 GB  | 14M (0.17%)  |  
| QLoRA r=16  | 6 GB  | 14M (0.17%)  |  
| IA3  | 16 GB  | 800K (0.01%)  |  
### Training speed (A100 80GB)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#training-speed-a100-80gb "Training speed \(A100 80GB\)的直接链接")  
| Method  | Tokens/sec  | vs Full FT  |  
| --- | --- | --- |  
| Full FT  | 2,500  | 1x  |  
| LoRA  | 3,200  | 1.3x  |  
| QLoRA  | 2,100  | 0.84x  |  
### Quality (MMLU benchmark)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#quality-mmlu-benchmark "Quality \(MMLU benchmark\)的直接链接")  
| Model  | Full FT  | LoRA  | QLoRA  |  
| --- | --- | --- | --- |  
| Llama 2-7B  | 45.3  | 44.8  | 44.1  |  
| Llama 2-13B  | 54.8  | 54.2  | 53.5  |  
## Common issues[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#common-issues "Common issues的直接链接")
### CUDA OOM during training[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#cuda-oom-during-training "CUDA OOM during training的直接链接")

```
# Solution 1: Enable gradient checkpointingmodel.gradient_checkpointing_enable()# Solution 2: Reduce batch size + increase accumulationTrainingArguments(    per_device_train_batch_size=1,    gradient_accumulation_steps=16# Solution 3: Use QLoRAfrom transformers import BitsAndBytesConfigbnb_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4")
```

### Adapter not applying[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#adapter-not-applying "Adapter not applying的直接链接")

```
# Verify adapter is activeprint(model.active_adapters)# Should show adapter name# Check trainable parametersmodel.print_trainable_parameters()# Ensure model in training modemodel.train()
```

### Quality degradation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#quality-degradation "Quality degradation的直接链接")

```
# Increase rankLoraConfig(r=32, lora_alpha=64)# Target more modulestarget_modules ="all-linear"# Use more training data and epochsTrainingArguments(num_train_epochs=5)# Lower learning rateTrainingArguments(learning_rate=1e-4)
```

## Best practices[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#best-practices "Best practices的直接链接")
  1. **Start with r=8-16** , increase if quality insufficient
  2. **Use alpha = 2 * rank** as starting point
  3. **Target attention + MLP layers** for best quality/efficiency
  4. **Enable gradient checkpointing** for memory savings
  5. **Save adapters frequently** (small files, easy rollback)
  6. **Evaluate on held-out data** before merging
  7. **Use QLoRA for 70B+ models** on consumer hardware


## References[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#references "References的直接链接")
  * **[Advanced Usage](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/mlops/peft/references/advanced-usage.md)** - DoRA, LoftQ, rank stabilization, custom modules
  * **[Troubleshooting](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/mlops/peft/references/troubleshooting.md)** - Common errors, debugging, optimization


## Resources[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#resources "Resources的直接链接")
  * **GitHub** : <https://github.com/huggingface/peft>
  * **Docs** : <https://huggingface.co/docs/peft>
  * **LoRA Paper** : arXiv:2106.09685
  * **QLoRA Paper** : arXiv:2305.14314
  * **Models** : <https://huggingface.co/models?library=peft>


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#reference-full-skillmd)
  * [When to use PEFT](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#when-to-use-peft)
  * [Quick start](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#quick-start)
    * [Installation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#installation)
    * [LoRA fine-tuning (standard)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#lora-fine-tuning-standard)
    * [QLoRA fine-tuning (memory-efficient)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#qlora-fine-tuning-memory-efficient)
  * [LoRA parameter selection](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#lora-parameter-selection)
    * [Rank (r) - capacity vs efficiency](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#rank-r---capacity-vs-efficiency)
    * [Alpha (lora_alpha) - scaling factor](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#alpha-lora_alpha---scaling-factor)
    * [Target modules by architecture](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#target-modules-by-architecture)
  * [Loading and merging adapters](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#loading-and-merging-adapters)
    * [Load trained adapter](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#load-trained-adapter)
    * [Merge adapter into base model](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#merge-adapter-into-base-model)
    * [Multi-adapter serving](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#multi-adapter-serving)
  * [PEFT methods comparison](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#peft-methods-comparison)
    * [IA3 (minimal parameters)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#ia3-minimal-parameters)
    * [Prefix Tuning](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#prefix-tuning)
  * [Integration patterns](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#integration-patterns)
    * [With TRL (SFTTrainer)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#with-trl-sfttrainer)
    * [With Axolotl (YAML config)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#with-axolotl-yaml-config)
    * [With vLLM (inference)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#with-vllm-inference)
  * [Performance benchmarks](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#performance-benchmarks)
    * [Memory usage (Llama 3.1 8B)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#memory-usage-llama-31-8b)
    * [Training speed (A100 80GB)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#training-speed-a100-80gb)
    * [Quality (MMLU benchmark)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#quality-mmlu-benchmark)
  * [Common issues](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#common-issues)
    * [CUDA OOM during training](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#cuda-oom-during-training)
    * [Adapter not applying](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#adapter-not-applying)
    * [Quality degradation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#quality-degradation)
  * [Best practices](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-peft#best-practices)


