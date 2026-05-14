<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper -->

本页总览
OpenAI's general-purpose speech recognition model. Supports 99 languages, transcription, translation to English, and language identification. Six model sizes from tiny (39M params) to large (1550M params). Use for speech-to-text, podcast transcription, or multilingual audio processing. Best for robust, multilingual ASR.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#skill-metadata "Skill metadata的直接链接")  
| Source  | Optional — install with `hermes skills install official/mlops/whisper`  |  
| --- | --- |  
| Path  | `optional-skills/mlops/whisper`  |  
| Version  | `1.0.0`  |  
| Author  | Orchestra Research  |  
| License  | MIT  |  
| Dependencies  |  `openai-whisper`, `transformers`, `torch`  |  
| Platforms  | linux, macos  |  
| Tags  |  `Whisper`, `Speech Recognition`, `ASR`, `Multimodal`, `Multilingual`, `OpenAI`, `Speech-To-Text`, `Transcription`, `Translation`, `Audio Processing`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Whisper - Robust Speech Recognition
OpenAI's multilingual speech recognition model.
## When to use Whisper[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#when-to-use-whisper "When to use Whisper的直接链接")
**Use when:**
  * Speech-to-text transcription (99 languages)
  * Podcast/video transcription
  * Meeting notes automation
  * Translation to English
  * Noisy audio transcription
  * Multilingual audio processing


**Metrics** :
  * **72,900+ GitHub stars**
  * 99 languages supported
  * Trained on 680,000 hours of audio
  * MIT License


**Use alternatives instead** :
  * **AssemblyAI** : Managed API, speaker diarization
  * **Deepgram** : Real-time streaming ASR
  * **Google Speech-to-Text** : Cloud-based


## Quick start[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#quick-start "Quick start的直接链接")
### Installation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#installation "Installation的直接链接")

```
# Requires Python 3.8-3.11pip install-U openai-whisper# Requires ffmpeg# macOS: brew install ffmpeg# Ubuntu: sudo apt install ffmpeg# Windows: choco install ffmpeg
```

### Basic transcription[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#basic-transcription "Basic transcription的直接链接")

```
import whisper# Load modelmodel = whisper.load_model("base")# Transcriberesult = model.transcribe("audio.mp3")# Print textprint(result["text"])# Access segmentsfor segment in result["segments"]:print(f"[{segment['start']:.2f}s - {segment['end']:.2f}s] {segment['text']}")
```

## Model sizes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#model-sizes "Model sizes的直接链接")

```
# Available modelsmodels =["tiny","base","small","medium","large","turbo"]# Load specific modelmodel = whisper.load_model("turbo")# Fastest, good quality
```
  
| Model  | Parameters  | English-only  | Multilingual  | Speed  | VRAM  |  
| --- | --- | --- | --- | --- | --- |  
| tiny  | 39M  | ✓  | ✓  | ~32x  | ~1 GB  |  
| base  | 74M  | ✓  | ✓  | ~16x  | ~1 GB  |  
| small  | 244M  | ✓  | ✓  | ~6x  | ~2 GB  |  
| medium  | 769M  | ✓  | ✓  | ~2x  | ~5 GB  |  
| large  | 1550M  | ✗  | ✓  | 1x  | ~10 GB  |  
| turbo  | 809M  | ✗  | ✓  | ~8x  | ~6 GB  |  
**Recommendation** : Use `turbo` for best speed/quality, `base` for prototyping
## Transcription options[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#transcription-options "Transcription options的直接链接")
### Language specification[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#language-specification "Language specification的直接链接")

```
# Auto-detect languageresult = model.transcribe("audio.mp3")# Specify language (faster)result = model.transcribe("audio.mp3", language="en")# Supported: en, es, fr, de, it, pt, ru, ja, ko, zh, and 89 more
```

### Task selection[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#task-selection "Task selection的直接链接")

```
# Transcription (default)result = model.transcribe("audio.mp3", task="transcribe")# Translation to Englishresult = model.transcribe("spanish.mp3", task="translate")# Input: Spanish audio → Output: English text
```

### Initial prompt[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#initial-prompt "Initial prompt的直接链接")

```
# Improve accuracy with contextresult = model.transcribe("audio.mp3",    initial_prompt="This is a technical podcast about machine learning and AI."# Helps with:# - Technical terms# - Proper nouns# - Domain-specific vocabulary
```

### Timestamps[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#timestamps "Timestamps的直接链接")

```
# Word-level timestampsresult = model.transcribe("audio.mp3", word_timestamps=True)for segment in result["segments"]:for word in segment["words"]:print(f"{word['word']} ({word['start']:.2f}s - {word['end']:.2f}s)")
```

### Temperature fallback[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#temperature-fallback "Temperature fallback的直接链接")

```
# Retry with different temperatures if confidence lowresult = model.transcribe("audio.mp3",    temperature=(0.0,0.2,0.4,0.6,0.8,1.0)
```

## Command line usage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#command-line-usage "Command line usage的直接链接")

```
# Basic transcriptionwhisper audio.mp3# Specify modelwhisper audio.mp3 --model turbo# Output formatswhisper audio.mp3 --output_format txt     # Plain textwhisper audio.mp3 --output_format srt     # Subtitleswhisper audio.mp3 --output_format vtt     # WebVTTwhisper audio.mp3 --output_format json    # JSON with timestamps# Languagewhisper audio.mp3 --language Spanish# Translationwhisper spanish.mp3 --task translate
```

## Batch processing[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#batch-processing "Batch processing的直接链接")

```
import osaudio_files =["file1.mp3","file2.mp3","file3.mp3"]for audio_file in audio_files:print(f"Transcribing {audio_file}...")    result = model.transcribe(audio_file)# Save to file    output_file = audio_file.replace(".mp3",".txt")withopen(output_file,"w")as f:.write(result["text"])
```

## Real-time transcription[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#real-time-transcription "Real-time transcription的直接链接")

```
# For streaming audio, use faster-whisper# pip install faster-whisperfrom faster_whisper import WhisperModelmodel = WhisperModel("base", device="cuda", compute_type="float16")# Transcribe with streamingsegments, info = model.transcribe("audio.mp3", beam_size=5)for segment in segments:print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
```

## GPU acceleration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#gpu-acceleration "GPU acceleration的直接链接")

```
import whisper# Automatically uses GPU if availablemodel = whisper.load_model("turbo")# Force CPUmodel = whisper.load_model("turbo", device="cpu")# Force GPUmodel = whisper.load_model("turbo", device="cuda")# 10-20× faster on GPU
```

## Integration with other tools[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#integration-with-other-tools "Integration with other tools的直接链接")
### Subtitle generation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#subtitle-generation "Subtitle generation的直接链接")

```
# Generate SRT subtitleswhisper video.mp4 --output_format srt --language English# Output: video.srt
```

### With LangChain[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#with-langchain "With LangChain的直接链接")

```
from langchain.document_loaders import WhisperTranscriptionLoaderloader = WhisperTranscriptionLoader(file_path="audio.mp3")docs = loader.load()# Use transcription in RAGfrom langchain_chroma import Chromafrom langchain_openai import OpenAIEmbeddingsvectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())
```

### Extract audio from video[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#extract-audio-from-video "Extract audio from video的直接链接")

```
# Use ffmpeg to extract audioffmpeg -i video.mp4 -vn-acodec pcm_s16le audio.wav# Then transcribewhisper audio.wav
```

## Best practices[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#best-practices "Best practices的直接链接")
  1. **Use turbo model** - Best speed/quality for English
  2. **Specify language** - Faster than auto-detect
  3. **Add initial prompt** - Improves technical terms
  4. **Use GPU** - 10-20× faster
  5. **Batch process** - More efficient
  6. **Convert to WAV** - Better compatibility
  7. **Split long audio** - <30 min chunks
  8. **Check language support** - Quality varies by language
  9. **Use faster-whisper** - 4× faster than openai-whisper
  10. **Monitor VRAM** - Scale model size to hardware


## Performance[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#performance "Performance的直接链接")  
| Model  | Real-time factor (CPU)  | Real-time factor (GPU)  |  
| --- | --- | --- |  
| tiny  | ~0.32  | ~0.01  |  
| base  | ~0.16  | ~0.01  |  
| turbo  | ~0.08  | ~0.01  |  
| large  | ~1.0  | ~0.05  |  
_Real-time factor: 0.1 = 10× faster than real-time_
## Language support[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#language-support "Language support的直接链接")
Top-supported languages:
  * English (en)
  * Spanish (es)
  * French (fr)
  * German (de)
  * Italian (it)
  * Portuguese (pt)
  * Russian (ru)
  * Japanese (ja)
  * Korean (ko)
  * Chinese (zh)


Full list: 99 languages total
## Limitations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#limitations "Limitations的直接链接")
  1. **Hallucinations** - May repeat or invent text
  2. **Long-form accuracy** - Degrades on >30 min audio
  3. **Speaker identification** - No diarization
  4. **Accents** - Quality varies
  5. **Background noise** - Can affect accuracy
  6. **Real-time latency** - Not suitable for live captioning


## Resources[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#resources "Resources的直接链接")
  * **GitHub** : <https://github.com/openai/whisper> ⭐ 72,900+
  * **Paper** : <https://arxiv.org/abs/2212.04356>
  * **Model Card** : <https://github.com/openai/whisper/blob/main/model-card.md>
  * **Colab** : Available in repo
  * **License** : MIT


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#reference-full-skillmd)
  * [When to use Whisper](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#when-to-use-whisper)
  * [Quick start](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#quick-start)
    * [Installation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#installation)
    * [Basic transcription](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#basic-transcription)
  * [Model sizes](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#model-sizes)
  * [Transcription options](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#transcription-options)
    * [Language specification](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#language-specification)
    * [Task selection](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#task-selection)
    * [Initial prompt](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#initial-prompt)
    * [Temperature fallback](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#temperature-fallback)
  * [Command line usage](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#command-line-usage)
  * [Batch processing](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#batch-processing)
  * [Real-time transcription](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#real-time-transcription)
  * [GPU acceleration](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#gpu-acceleration)
  * [Integration with other tools](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#integration-with-other-tools)
    * [Subtitle generation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#subtitle-generation)
    * [With LangChain](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#with-langchain)
    * [Extract audio from video](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#extract-audio-from-video)
  * [Best practices](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#best-practices)
  * [Performance](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#performance)
  * [Language support](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#language-support)
  * [Limitations](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/mlops/mlops-whisper#limitations)


