<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything -->

本页总览
SAM: zero-shot image segmentation via points, boxes, masks.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#skill-metadata "Skill metadata的直接链接")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/mlops/models/segment-anything`  |  
| Version  | `1.0.0`  |  
| Author  | Orchestra Research  |  
| License  | MIT  |  
| Dependencies  |  `segment-anything`, `transformers>=4.30.0`, `torch>=1.7.0`  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `Multimodal`, `Image Segmentation`, `Computer Vision`, `SAM`, `Zero-Shot`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Segment Anything Model (SAM)
Comprehensive guide to using Meta AI's Segment Anything Model for zero-shot image segmentation.
## When to use SAM[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#when-to-use-sam "When to use SAM的直接链接")
**Use SAM when:**
  * Need to segment any object in images without task-specific training
  * Building interactive annotation tools with point/box prompts
  * Generating training data for other vision models
  * Need zero-shot transfer to new image domains
  * Building object detection/segmentation pipelines
  * Processing medical, satellite, or domain-specific images


**Key features:**
  * **Zero-shot segmentation** : Works on any image domain without fine-tuning
  * **Flexible prompts** : Points, bounding boxes, or previous masks
  * **Automatic segmentation** : Generate all object masks automatically
  * **High quality** : Trained on 1.1 billion masks from 11 million images
  * **Multiple model sizes** : ViT-B (fastest), ViT-L, ViT-H (most accurate)
  * **ONNX export** : Deploy in browsers and edge devices


**Use alternatives instead:**
  * **YOLO/Detectron2** : For real-time object detection with classes
  * **Mask2Former** : For semantic/panoptic segmentation with categories
  * **GroundingDINO + SAM** : For text-prompted segmentation
  * **SAM 2** : For video segmentation tasks


## Quick start[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#quick-start "Quick start的直接链接")
### Installation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#installation "Installation的直接链接")

```
# From GitHubpip install git+https://github.com/facebookresearch/segment-anything.git# Optional dependenciespip install opencv-python pycocotools matplotlib# Or use HuggingFace transformerspip install transformers
```

### Download checkpoints[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#download-checkpoints "Download checkpoints的直接链接")

```
# ViT-H (largest, most accurate) - 2.4GBwget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth# ViT-L (medium) - 1.2GBwget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth# ViT-B (smallest, fastest) - 375MBwget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth
```

### Basic usage with SamPredictor[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#basic-usage-with-sampredictor "Basic usage with SamPredictor的直接链接")

```
import numpy as npfrom segment_anything import sam_model_registry, SamPredictor# Load modelsam = sam_model_registry["vit_h"](https://github.com/NousResearch/hermes-agent/blob/main/skills/mlops/models/segment-anything/checkpoint="sam_vit_h_4b8939.pth")sam.to(device="cuda")# Create predictorpredictor = SamPredictor(sam)# Set image (computes embeddings once)image = cv2.imread("image.jpg")image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)predictor.set_image(image)# Predict with point promptsinput_point = np.array([[500,375]])# (x, y) coordinatesinput_label = np.array([1])# 1 = foreground, 0 = backgroundmasks, scores, logits = predictor.predict(    point_coords=input_point,    point_labels=input_label,    multimask_output=True# Returns 3 mask options# Select best maskbest_mask = masks[np.argmax(scores)]
```

### HuggingFace Transformers[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#huggingface-transformers "HuggingFace Transformers的直接链接")

```
import torchfrom PIL import Imagefrom transformers import SamModel, SamProcessor# Load model and processormodel = SamModel.from_pretrained("facebook/sam-vit-huge")processor = SamProcessor.from_pretrained("facebook/sam-vit-huge")model.to("cuda")# Process image with point promptimage = Image.open("image.jpg")input_points =[[[450,600]]]# Batch of pointsinputs = processor(image, input_points=input_points, return_tensors="pt")inputs ={k: v.to("cuda")for k, v in inputs.items()}# Generate maskswith torch.no_grad():    outputs = model(**inputs)# Post-process masks to original sizemasks = processor.image_processor.post_process_masks(    outputs.pred_masks.cpu(),    inputs["original_sizes"].cpu(),    inputs["reshaped_input_sizes"].cpu()
```

## Core concepts[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#core-concepts "Core concepts的直接链接")
### Model architecture[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#model-architecture "Model architecture的直接链接")

```
SAM Architecture:┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐│  Image Encoder  │────▶│ Prompt Encoder  │────▶│  Mask Decoder   ││     (ViT)       │     │ (Points/Boxes)  │     │ (Transformer)   │└─────────────────┘     └─────────────────┘     └─────────────────┘        │                       │                       │   Image Embeddings      Prompt Embeddings         Masks + IoU   (computed once)       (per prompt)             predictions
```

### Model variants[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#model-variants "Model variants的直接链接")  
| Model  | Checkpoint  | Size  | Speed  | Accuracy  |  
| --- | --- | --- | --- | --- |  
| ViT-H  | `vit_h`  | 2.4 GB  | Slowest  | Best  |  
| ViT-L  | `vit_l`  | 1.2 GB  | Medium  | Good  |  
| ViT-B  | `vit_b`  | 375 MB  | Fastest  | Good  |  
### Prompt types[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#prompt-types "Prompt types的直接链接")  
| Prompt  | Description  | Use Case  |  
| --- | --- | --- |  
| Point (foreground)  | Click on object  | Single object selection  |  
| Point (background)  | Click outside object  | Exclude regions  |  
| Bounding box  | Rectangle around object  | Larger objects  |  
| Previous mask  | Low-res mask input  | Iterative refinement  |  
## Interactive segmentation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#interactive-segmentation "Interactive segmentation的直接链接")
### Point prompts[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#point-prompts "Point prompts的直接链接")

```
# Single foreground pointinput_point = np.array([[500,375]])input_label = np.array([1])masks, scores, logits = predictor.predict(    point_coords=input_point,    point_labels=input_label,    multimask_output=True# Multiple points (foreground + background)input_points = np.array([[500,375],[600,400],[450,300]])input_labels = np.array([1,1,0])# 2 foreground, 1 backgroundmasks, scores, logits = predictor.predict(    point_coords=input_points,    point_labels=input_labels,    multimask_output=False# Single mask when prompts are clear
```

### Box prompts[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#box-prompts "Box prompts的直接链接")

```
# Bounding box [x1, y1, x2, y2]input_box = np.array([425,600,700,875])masks, scores, logits = predictor.predict(    box=input_box,    multimask_output=False
```

### Combined prompts[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#combined-prompts "Combined prompts的直接链接")

```
# Box + points for precise controlmasks, scores, logits = predictor.predict(    point_coords=np.array([[500,375]]),    point_labels=np.array([1]),    box=np.array([400,300,700,600]),    multimask_output=False
```

### Iterative refinement[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#iterative-refinement "Iterative refinement的直接链接")

```
# Initial predictionmasks, scores, logits = predictor.predict(    point_coords=np.array([[500,375]]),    point_labels=np.array([1]),    multimask_output=True# Refine with additional point using previous maskmasks, scores, logits = predictor.predict(    point_coords=np.array([[500,375],[550,400]]),    point_labels=np.array([1,0]),# Add background point    mask_input=logits[np.argmax(scores)][None,:,:],# Use best mask    multimask_output=False
```

## Automatic mask generation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#automatic-mask-generation "Automatic mask generation的直接链接")
### Basic automatic segmentation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#basic-automatic-segmentation "Basic automatic segmentation的直接链接")

```
from segment_anything import SamAutomaticMaskGenerator# Create generatormask_generator = SamAutomaticMaskGenerator(sam)# Generate all masksmasks = mask_generator.generate(image)# Each mask contains:# - segmentation: binary mask# - bbox: [x, y, w, h]# - area: pixel count# - predicted_iou: quality score# - stability_score: robustness score# - point_coords: generating point
```

### Customized generation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#customized-generation "Customized generation的直接链接")

```
mask_generator = SamAutomaticMaskGenerator(    model=sam,    points_per_side=32,# Grid density (more = more masks)    pred_iou_thresh=0.88,# Quality threshold    stability_score_thresh=0.95,# Stability threshold    crop_n_layers=1,# Multi-scale crops    crop_n_points_downscale_factor=2,    min_mask_region_area=100,# Remove tiny masksmasks = mask_generator.generate(image)
```

### Filtering masks[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#filtering-masks "Filtering masks的直接链接")

```
# Sort by area (largest first)masks =sorted(masks, key=lambda x: x['area'], reverse=True)# Filter by predicted IoUhigh_quality =[m for m in masks if m['predicted_iou']>0.9]# Filter by stability scorestable_masks =[m for m in masks if m['stability_score']>0.95]
```

## Batched inference[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#batched-inference "Batched inference的直接链接")
### Multiple images[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#multiple-images "Multiple images的直接链接")

```
# Process multiple images efficientlyimages =[cv2.imread(f"image_{i}.jpg")for i inrange(10)]all_masks =[]for image in images:    predictor.set_image(image)    masks, _, _ = predictor.predict(        point_coords=np.array([[500,375]]),        point_labels=np.array([1]),        multimask_output=True    all_masks.append(masks)
```

### Multiple prompts per image[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#multiple-prompts-per-image "Multiple prompts per image的直接链接")

```
# Process multiple prompts efficiently (one image encoding)predictor.set_image(image)# Batch of point promptspoints =[    np.array([[100,100]]),    np.array([[200,200]]),    np.array([[300,300]])all_masks =[]for point in points:    masks, scores, _ = predictor.predict(        point_coords=point,        point_labels=np.array([1]),        multimask_output=True    all_masks.append(masks[np.argmax(scores)])
```

## ONNX deployment[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#onnx-deployment "ONNX deployment的直接链接")
### Export model[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#export-model "Export model的直接链接")

```
python scripts/export_onnx_model.py \--checkpoint sam_vit_h_4b8939.pth \    --model-type vit_h \--output sam_onnx.onnx \    --return-single-mask
```

### Use ONNX model[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#use-onnx-model "Use ONNX model的直接链接")

```
import onnxruntime# Load ONNX modelort_session = onnxruntime.InferenceSession("sam_onnx.onnx")# Run inference (image embeddings computed separately)masks = ort_session.run(None,"image_embeddings": image_embeddings,"point_coords": point_coords,"point_labels": point_labels,"mask_input": np.zeros((1,1,256,256), dtype=np.float32),"has_mask_input": np.array([0], dtype=np.float32),"orig_im_size": np.array([h, w], dtype=np.float32)
```

## Common workflows[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#common-workflows "Common workflows的直接链接")
### Workflow 1: Annotation tool[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#workflow-1-annotation-tool "Workflow 1: Annotation tool的直接链接")

```
import cv2# Load modelpredictor = SamPredictor(sam)predictor.set_image(image)defon_click(event, x, y, flags, param):if event == cv2.EVENT_LBUTTONDOWN:# Foreground point        masks, scores, _ = predictor.predict(            point_coords=np.array([[x, y]]),            point_labels=np.array([1]),            multimask_output=True# Display best mask        display_mask(masks[np.argmax(scores)])
```

### Workflow 2: Object extraction[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#workflow-2-object-extraction "Workflow 2: Object extraction的直接链接")

```
defextract_object(image, point):"""Extract object at point with transparent background."""    predictor.set_image(image)    masks, scores, _ = predictor.predict(        point_coords=np.array([point]),        point_labels=np.array([1]),        multimask_output=True    best_mask = masks[np.argmax(scores)]# Create RGBA output    rgba = np.zeros((image.shape[0], image.shape[1],4), dtype=np.uint8)    rgba[:,:,:3]= image    rgba[:,:,3]= best_mask *255return rgba
```

### Workflow 3: Medical image segmentation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#workflow-3-medical-image-segmentation "Workflow 3: Medical image segmentation的直接链接")

```
# Process medical images (grayscale to RGB)medical_image = cv2.imread("scan.png", cv2.IMREAD_GRAYSCALE)rgb_image = cv2.cvtColor(medical_image, cv2.COLOR_GRAY2RGB)predictor.set_image(rgb_image)# Segment region of interestmasks, scores, _ = predictor.predict(    box=np.array([x1, y1, x2, y2]),# ROI bounding box    multimask_output=True
```

## Output format[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#output-format "Output format的直接链接")
### Mask data structure[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#mask-data-structure "Mask data structure的直接链接")

```
# SamAutomaticMaskGenerator output"segmentation": np.ndarray,# H×W binary mask"bbox":[x, y, w, h],# Bounding box"area":int,# Pixel count"predicted_iou":float,# 0-1 quality score"stability_score":float,# 0-1 robustness score"crop_box":[x, y, w, h],# Generation crop region"point_coords":[[x, y]],# Input point
```

### COCO RLE format[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#coco-rle-format "COCO RLE format的直接链接")

```
from pycocotools import mask as mask_utils# Encode mask to RLErle = mask_utils.encode(np.asfortranarray(mask.astype(np.uint8)))rle["counts"]= rle["counts"].decode("utf-8")# Decode RLE to maskdecoded_mask = mask_utils.decode(rle)
```

## Performance optimization[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#performance-optimization "Performance optimization的直接链接")
### GPU memory[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#gpu-memory "GPU memory的直接链接")

```
# Use smaller model for limited VRAMsam = sam_model_registry["vit_b"](https://github.com/NousResearch/hermes-agent/blob/main/skills/mlops/models/segment-anything/checkpoint="sam_vit_b_01ec64.pth")# Process images in batches# Clear CUDA cache between large batchestorch.cuda.empty_cache()
```

### Speed optimization[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#speed-optimization "Speed optimization的直接链接")

```
# Use half precisionsam = sam.half()# Reduce points for automatic generationmask_generator = SamAutomaticMaskGenerator(    model=sam,    points_per_side=16,# Default is 32# Use ONNX for deployment# Export with --return-single-mask for faster inference
```

## Common issues[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#common-issues "Common issues的直接链接")  
| Issue  | Solution  |  
| --- | --- |  
| Out of memory  | Use ViT-B model, reduce image size  |  
| Slow inference  | Use ViT-B, reduce points_per_side  |  
| Poor mask quality  | Try different prompts, use box + points  |  
| Edge artifacts  | Use stability_score filtering  |  
| Small objects missed  | Increase points_per_side  |  
## References[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#references "References的直接链接")
  * **[Advanced Usage](https://github.com/NousResearch/hermes-agent/blob/main/skills/mlops/models/segment-anything/references/advanced-usage.md)** - Batching, fine-tuning, integration
  * **[Troubleshooting](https://github.com/NousResearch/hermes-agent/blob/main/skills/mlops/models/segment-anything/references/troubleshooting.md)** - Common issues and solutions


## Resources[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#resources "Resources的直接链接")
  * **GitHub** : <https://github.com/facebookresearch/segment-anything>
  * **Paper** : <https://arxiv.org/abs/2304.02643>
  * **Demo** : <https://segment-anything.com>
  * **SAM 2 (Video)** : <https://github.com/facebookresearch/segment-anything-2>
  * **HuggingFace** : <https://huggingface.co/facebook/sam-vit-huge>


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#reference-full-skillmd)
  * [When to use SAM](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#when-to-use-sam)
  * [Quick start](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#quick-start)
    * [Installation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#installation)
    * [Download checkpoints](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#download-checkpoints)
    * [Basic usage with SamPredictor](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#basic-usage-with-sampredictor)
    * [HuggingFace Transformers](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#huggingface-transformers)
  * [Core concepts](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#core-concepts)
    * [Model architecture](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#model-architecture)
    * [Model variants](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#model-variants)
    * [Prompt types](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#prompt-types)
  * [Interactive segmentation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#interactive-segmentation)
    * [Point prompts](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#point-prompts)
    * [Box prompts](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#box-prompts)
    * [Combined prompts](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#combined-prompts)
    * [Iterative refinement](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#iterative-refinement)
  * [Automatic mask generation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#automatic-mask-generation)
    * [Basic automatic segmentation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#basic-automatic-segmentation)
    * [Customized generation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#customized-generation)
    * [Filtering masks](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#filtering-masks)
  * [Batched inference](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#batched-inference)
    * [Multiple images](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#multiple-images)
    * [Multiple prompts per image](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#multiple-prompts-per-image)
  * [ONNX deployment](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#onnx-deployment)
    * [Export model](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#export-model)
    * [Use ONNX model](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#use-onnx-model)
  * [Common workflows](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#common-workflows)
    * [Workflow 1: Annotation tool](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#workflow-1-annotation-tool)
    * [Workflow 2: Object extraction](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#workflow-2-object-extraction)
    * [Workflow 3: Medical image segmentation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#workflow-3-medical-image-segmentation)
  * [Output format](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#output-format)
    * [Mask data structure](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#mask-data-structure)
    * [COCO RLE format](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#coco-rle-format)
  * [Performance optimization](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#performance-optimization)
    * [Speed optimization](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#speed-optimization)
  * [Common issues](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-models-segment-anything#common-issues)


