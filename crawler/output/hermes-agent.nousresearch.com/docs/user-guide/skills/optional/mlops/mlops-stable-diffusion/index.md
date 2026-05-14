<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#__docusaurus_skipToContent_fallback)
On this page
State-of-the-art text-to-image generation with Stable Diffusion models via HuggingFace Diffusers. Use when generating images from text prompts, performing image-to-image translation, inpainting, or building custom diffusion pipelines.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#skill-metadata "Direct link to Skill metadata")  
| Source  | Optional — install with `hermes skills install official/mlops/stable-diffusion`  |  
| --- | --- |  
| Path  | `optional-skills/mlops/stable-diffusion`  |  
| Version  | `1.0.0`  |  
| Author  | Orchestra Research  |  
| License  | MIT  |  
| Dependencies  |  `diffusers>=0.30.0`, `transformers>=4.41.0`, `accelerate>=0.31.0`, `torch>=2.0.0`  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `Image Generation`, `Stable Diffusion`, `Diffusers`, `Text-to-Image`, `Multimodal`, `Computer Vision`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Stable Diffusion Image Generation
Comprehensive guide to generating images with Stable Diffusion using the HuggingFace Diffusers library.
## When to use Stable Diffusion[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#when-to-use-stable-diffusion "Direct link to When to use Stable Diffusion")
**Use Stable Diffusion when:**
  * Generating images from text descriptions
  * Performing image-to-image translation (style transfer, enhancement)
  * Inpainting (filling in masked regions)
  * Outpainting (extending images beyond boundaries)
  * Creating variations of existing images
  * Building custom image generation workflows


**Key features:**
  * **Text-to-Image** : Generate images from natural language prompts
  * **Image-to-Image** : Transform existing images with text guidance
  * **Inpainting** : Fill masked regions with context-aware content
  * **ControlNet** : Add spatial conditioning (edges, poses, depth)
  * **LoRA Support** : Efficient fine-tuning and style adaptation
  * **Multiple Models** : SD 1.5, SDXL, SD 3.0, Flux support


**Use alternatives instead:**
  * **DALL-E 3** : For API-based generation without GPU
  * **Midjourney** : For artistic, stylized outputs
  * **Imagen** : For Google Cloud integration
  * **Leonardo.ai** : For web-based creative workflows


## Quick start[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#quick-start "Direct link to Quick start")
### Installation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#installation "Direct link to Installation")

```
pip install diffusers transformers accelerate torchpip install xformers  # Optional: memory-efficient attention
```

### Basic text-to-image[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#basic-text-to-image "Direct link to Basic text-to-image")

```
from diffusers import DiffusionPipelineimport torch# Load pipeline (auto-detects model type)pipe = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5",    torch_dtype=torch.float16pipe.to("cuda")# Generate imageimage = pipe("A serene mountain landscape at sunset, highly detailed",    num_inference_steps=50,    guidance_scale=7.5).images[0]image.save("output.png")
```

### Using SDXL (higher quality)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#using-sdxl-higher-quality "Direct link to Using SDXL \(higher quality\)")

```
from diffusers import AutoPipelineForText2Imageimport torchpipe = AutoPipelineForText2Image.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",    torch_dtype=torch.float16,    variant="fp16"pipe.to("cuda")# Enable memory optimizationpipe.enable_model_cpu_offload()image = pipe(    prompt="A futuristic city with flying cars, cinematic lighting",    height=1024,    width=1024,    num_inference_steps=30).images[0]
```

## Architecture overview[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#architecture-overview "Direct link to Architecture overview")
### Three-pillar design[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#three-pillar-design "Direct link to Three-pillar design")
Diffusers is built around three core components:

```
Pipeline (orchestration)├── Model (neural networks)│   ├── UNet / Transformer (noise prediction)│   ├── VAE (latent encoding/decoding)│   └── Text Encoder (CLIP/T5)└── Scheduler (denoising algorithm)
```

### Pipeline inference flow[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#pipeline-inference-flow "Direct link to Pipeline inference flow")

```
Text Prompt → Text Encoder → Text EmbeddingsRandom Noise → [Denoising Loop] ← Scheduler               Predicted Noise              VAE Decoder → Final Image
```

## Core concepts[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#core-concepts "Direct link to Core concepts")
### Pipelines[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#pipelines "Direct link to Pipelines")
Pipelines orchestrate complete workflows:  
| Pipeline  | Purpose  |  
| --- | --- |  
| `StableDiffusionPipeline`  | Text-to-image (SD 1.x/2.x)  |  
| `StableDiffusionXLPipeline`  | Text-to-image (SDXL)  |  
| `StableDiffusion3Pipeline`  | Text-to-image (SD 3.0)  |  
| `FluxPipeline`  | Text-to-image (Flux models)  |  
| `StableDiffusionImg2ImgPipeline`  | Image-to-image  |  
| `StableDiffusionInpaintPipeline`  | Inpainting  |  
### Schedulers[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#schedulers "Direct link to Schedulers")
Schedulers control the denoising process:  
| Scheduler  | Steps  | Quality  | Use Case  |  
| --- | --- | --- | --- |  
| `EulerDiscreteScheduler`  | 20-50  | Good  | Default choice  |  
| `EulerAncestralDiscreteScheduler`  | 20-50  | Good  | More variation  |  
| `DPMSolverMultistepScheduler`  | 15-25  | Excellent  | Fast, high quality  |  
| `DDIMScheduler`  | 50-100  | Good  | Deterministic  |  
| `LCMScheduler`  | 4-8  | Good  | Very fast  |  
| `UniPCMultistepScheduler`  | 15-25  | Excellent  | Fast convergence  |  
### Swapping schedulers[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#swapping-schedulers "Direct link to Swapping schedulers")

```
from diffusers import DPMSolverMultistepScheduler# Swap for faster generationpipe.scheduler = DPMSolverMultistepScheduler.from_config(    pipe.scheduler.config# Now generate with fewer stepsimage = pipe(prompt, num_inference_steps=20).images[0]
```

## Generation parameters[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#generation-parameters "Direct link to Generation parameters")
### Key parameters[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#key-parameters "Direct link to Key parameters")  
| Parameter  | Default  | Description  |  
| --- | --- | --- |  
| `prompt`  | Required  | Text description of desired image  |  
| `negative_prompt`  | None  | What to avoid in the image  |  
| `num_inference_steps`  | 50  | Denoising steps (more = better quality)  |  
| `guidance_scale`  | 7.5  | Prompt adherence (7-12 typical)  |  
|  `height`, `width`  | 512/1024  | Output dimensions (multiples of 8)  |  
| `generator`  | None  | Torch generator for reproducibility  |  
| `num_images_per_prompt`  | 1  | Batch size  |  
### Reproducible generation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#reproducible-generation "Direct link to Reproducible generation")

```
import torchgenerator = torch.Generator(device="cuda").manual_seed(42)image = pipe(    prompt="A cat wearing a top hat",    generator=generator,    num_inference_steps=50).images[0]
```

### Negative prompts[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#negative-prompts "Direct link to Negative prompts")

```
image = pipe(    prompt="Professional photo of a dog in a garden",    negative_prompt="blurry, low quality, distorted, ugly, bad anatomy",    guidance_scale=7.5).images[0]
```

## Image-to-image[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#image-to-image "Direct link to Image-to-image")
Transform existing images with text guidance:

```
from diffusers import AutoPipelineForImage2Imagefrom PIL import Imagepipe = AutoPipelineForImage2Image.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5",    torch_dtype=torch.float16).to("cuda")init_image = Image.open("input.jpg").resize((512,512))image = pipe(    prompt="A watercolor painting of the scene",    image=init_image,    strength=0.75,# How much to transform (0-1)    num_inference_steps=50).images[0]
```

## Inpainting[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#inpainting "Direct link to Inpainting")
Fill masked regions:

```
from diffusers import AutoPipelineForInpaintingfrom PIL import Imagepipe = AutoPipelineForInpainting.from_pretrained("runwayml/stable-diffusion-inpainting",    torch_dtype=torch.float16).to("cuda")image = Image.open("photo.jpg")mask = Image.open("mask.png")# White = inpaint regionresult = pipe(    prompt="A red car parked on the street",    image=image,    mask_image=mask,    num_inference_steps=50).images[0]
```

## ControlNet[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#controlnet "Direct link to ControlNet")
Add spatial conditioning for precise control:

```
from diffusers import StableDiffusionControlNetPipeline, ControlNetModelimport torch# Load ControlNet for edge conditioningcontrolnet = ControlNetModel.from_pretrained("lllyasviel/control_v11p_sd15_canny",    torch_dtype=torch.float16pipe = StableDiffusionControlNetPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5",    controlnet=controlnet,    torch_dtype=torch.float16).to("cuda")# Use Canny edge image as controlcontrol_image = get_canny_image(input_image)image = pipe(    prompt="A beautiful house in the style of Van Gogh",    image=control_image,    num_inference_steps=30).images[0]
```

### Available ControlNets[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#available-controlnets "Direct link to Available ControlNets")  
| ControlNet  | Input Type  | Use Case  |  
| --- | --- | --- |  
| `canny`  | Edge maps  | Preserve structure  |  
| `openpose`  | Pose skeletons  | Human poses  |  
| `depth`  | Depth maps  | 3D-aware generation  |  
| `normal`  | Normal maps  | Surface details  |  
| `mlsd`  | Line segments  | Architectural lines  |  
| `scribble`  | Rough sketches  | Sketch-to-image  |  
## LoRA adapters[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#lora-adapters "Direct link to LoRA adapters")
Load fine-tuned style adapters:

```
from diffusers import DiffusionPipelinepipe = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5",    torch_dtype=torch.float16).to("cuda")# Load LoRA weightspipe.load_lora_weights("path/to/lora", weight_name="style.safetensors")# Generate with LoRA styleimage = pipe("A portrait in the trained style").images[0]# Adjust LoRA strengthpipe.fuse_lora(lora_scale=0.8)# Unload LoRApipe.unload_lora_weights()
```

### Multiple LoRAs[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#multiple-loras "Direct link to Multiple LoRAs")

```
# Load multiple LoRAspipe.load_lora_weights("lora1", adapter_name="style")pipe.load_lora_weights("lora2", adapter_name="character")# Set weights for eachpipe.set_adapters(["style","character"], adapter_weights=[0.7,0.5])image = pipe("A portrait").images[0]
```

## Memory optimization[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#memory-optimization "Direct link to Memory optimization")
### Enable CPU offloading[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#enable-cpu-offloading "Direct link to Enable CPU offloading")

```
# Model CPU offload - moves models to CPU when not in usepipe.enable_model_cpu_offload()# Sequential CPU offload - more aggressive, slowerpipe.enable_sequential_cpu_offload()
```

### Attention slicing[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#attention-slicing "Direct link to Attention slicing")

```
# Reduce memory by computing attention in chunkspipe.enable_attention_slicing()# Or specific chunk sizepipe.enable_attention_slicing("max")
```

### xFormers memory-efficient attention[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#xformers-memory-efficient-attention "Direct link to xFormers memory-efficient attention")

```
# Requires xformers packagepipe.enable_xformers_memory_efficient_attention()
```

### VAE slicing for large images[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#vae-slicing-for-large-images "Direct link to VAE slicing for large images")

```
# Decode latents in tiles for large imagespipe.enable_vae_slicing()pipe.enable_vae_tiling()
```

## Model variants[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#model-variants "Direct link to Model variants")
### Loading different precisions[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#loading-different-precisions "Direct link to Loading different precisions")

```
# FP16 (recommended for GPU)pipe = DiffusionPipeline.from_pretrained("model-id",    torch_dtype=torch.float16,    variant="fp16"# BF16 (better precision, requires Ampere+ GPU)pipe = DiffusionPipeline.from_pretrained("model-id",    torch_dtype=torch.bfloat16
```

### Loading specific components[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#loading-specific-components "Direct link to Loading specific components")

```
from diffusers import UNet2DConditionModel, AutoencoderKL# Load custom VAEvae = AutoencoderKL.from_pretrained("stabilityai/sd-vae-ft-mse")# Use with pipelinepipe = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5",    vae=vae,    torch_dtype=torch.float16
```

## Batch generation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#batch-generation "Direct link to Batch generation")
Generate multiple images efficiently:

```
# Multiple promptsprompts =["A cat playing piano","A dog reading a book","A bird painting a picture"images = pipe(prompts, num_inference_steps=30).images# Multiple images per promptimages = pipe("A beautiful sunset",    num_images_per_prompt=4,    num_inference_steps=30).images
```

## Common workflows[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#common-workflows "Direct link to Common workflows")
### Workflow 1: High-quality generation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#workflow-1-high-quality-generation "Direct link to Workflow 1: High-quality generation")

```
from diffusers import StableDiffusionXLPipeline, DPMSolverMultistepSchedulerimport torch# 1. Load SDXL with optimizationspipe = StableDiffusionXLPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",    torch_dtype=torch.float16,    variant="fp16"pipe.to("cuda")pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)pipe.enable_model_cpu_offload()# 2. Generate with quality settingsimage = pipe(    prompt="A majestic lion in the savanna, golden hour lighting, 8k, detailed fur",    negative_prompt="blurry, low quality, cartoon, anime, sketch",    num_inference_steps=30,    guidance_scale=7.5,    height=1024,    width=1024).images[0]
```

### Workflow 2: Fast prototyping[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#workflow-2-fast-prototyping "Direct link to Workflow 2: Fast prototyping")

```
from diffusers import AutoPipelineForText2Image, LCMSchedulerimport torch# Use LCM for 4-8 step generationpipe = AutoPipelineForText2Image.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",    torch_dtype=torch.float16).to("cuda")# Load LCM LoRA for fast generationpipe.load_lora_weights("latent-consistency/lcm-lora-sdxl")pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)pipe.fuse_lora()# Generate in ~1 secondimage = pipe("A beautiful landscape",    num_inference_steps=4,    guidance_scale=1.0).images[0]
```

## Common issues[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#common-issues "Direct link to Common issues")
**CUDA out of memory:**

```
# Enable memory optimizationspipe.enable_model_cpu_offload()pipe.enable_attention_slicing()pipe.enable_vae_slicing()# Or use lower precisionpipe = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
```

**Black/noise images:**

```
# Check VAE configuration# Use safety checker bypass if neededpipe.safety_checker =None# Ensure proper dtype consistencypipe = pipe.to(dtype=torch.float16)
```

**Slow generation:**

```
# Use faster schedulerfrom diffusers import DPMSolverMultistepSchedulerpipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)# Reduce stepsimage = pipe(prompt, num_inference_steps=20).images[0]
```

## References[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#references "Direct link to References")
  * **[Advanced Usage](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/mlops/stable-diffusion/references/advanced-usage.md)** - Custom pipelines, fine-tuning, deployment
  * **[Troubleshooting](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/mlops/stable-diffusion/references/troubleshooting.md)** - Common issues and solutions


## Resources[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#resources "Direct link to Resources")
  * **Documentation** : <https://huggingface.co/docs/diffusers>
  * **Repository** : <https://github.com/huggingface/diffusers>
  * **Model Hub** : <https://huggingface.co/models?library=diffusers>
  * **Discord** : <https://discord.gg/diffusers>


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#reference-full-skillmd)
  * [When to use Stable Diffusion](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#when-to-use-stable-diffusion)
  * [Quick start](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#quick-start)
    * [Installation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#installation)
    * [Basic text-to-image](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#basic-text-to-image)
    * [Using SDXL (higher quality)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#using-sdxl-higher-quality)
  * [Architecture overview](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#architecture-overview)
    * [Three-pillar design](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#three-pillar-design)
    * [Pipeline inference flow](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#pipeline-inference-flow)
  * [Core concepts](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#core-concepts)
    * [Swapping schedulers](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#swapping-schedulers)
  * [Generation parameters](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#generation-parameters)
    * [Key parameters](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#key-parameters)
    * [Reproducible generation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#reproducible-generation)
    * [Negative prompts](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#negative-prompts)
  * [Image-to-image](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#image-to-image)
  * [ControlNet](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#controlnet)
    * [Available ControlNets](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#available-controlnets)
  * [LoRA adapters](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#lora-adapters)
    * [Multiple LoRAs](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#multiple-loras)
  * [Memory optimization](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#memory-optimization)
    * [Enable CPU offloading](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#enable-cpu-offloading)
    * [Attention slicing](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#attention-slicing)
    * [xFormers memory-efficient attention](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#xformers-memory-efficient-attention)
    * [VAE slicing for large images](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#vae-slicing-for-large-images)
  * [Model variants](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#model-variants)
    * [Loading different precisions](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#loading-different-precisions)
    * [Loading specific components](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#loading-specific-components)
  * [Batch generation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#batch-generation)
  * [Common workflows](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#common-workflows)
    * [Workflow 1: High-quality generation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#workflow-1-high-quality-generation)
    * [Workflow 2: Fast prototyping](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#workflow-2-fast-prototyping)
  * [Common issues](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion#common-issues)


