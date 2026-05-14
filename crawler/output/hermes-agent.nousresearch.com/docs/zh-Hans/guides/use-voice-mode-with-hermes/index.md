<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes -->

本页总览
This guide is the practical companion to the [Voice Mode feature reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/voice-mode).
If the feature page explains what voice mode can do, this guide shows how to actually use it well.
## What voice mode is good for[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#what-voice-mode-is-good-for "What voice mode is good for的直接链接")
Voice mode is especially useful when:
  * you want a hands-free CLI workflow
  * you want spoken responses in Telegram or Discord
  * you want Hermes sitting in a Discord voice channel for live conversation
  * you want quick idea capture, debugging, or back-and-forth while walking around instead of typing


## Choose your voice mode setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#choose-your-voice-mode-setup "Choose your voice mode setup的直接链接")
There are really three different voice experiences in Hermes.  
| Mode  | Best for  | Platform  |  
| --- | --- | --- |  
| Interactive microphone loop  | Personal hands-free use while coding or researching  | CLI  |  
| Voice replies in chat  | Spoken responses alongside normal messaging  | Telegram, Discord  |  
| Live voice channel bot  | Group or personal live conversation in a VC  | Discord voice channels  |  
A good path is:
  1. get text working first
  2. enable voice replies second
  3. move to Discord voice channels last if you want the full experience


## Step 1: make sure normal Hermes works first[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#step-1-make-sure-normal-hermes-works-first "Step 1: make sure normal Hermes works first的直接链接")
Before touching voice mode, verify that:
  * Hermes starts
  * your provider is configured
  * the agent can answer text prompts normally



```
hermes
```

Ask something simple:

```
What tools do you have available?
```

If that is not solid yet, fix text mode first.
## Step 2: install the right extras[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#step-2-install-the-right-extras "Step 2: install the right extras的直接链接")
### CLI microphone + playback[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#cli-microphone--playback "CLI microphone + playback的直接链接")

```
pip install"hermes-agent[voice]"
```

### Messaging platforms[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#messaging-platforms "Messaging platforms的直接链接")

```
pip install"hermes-agent[messaging]"
```

### Premium ElevenLabs TTS[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#premium-elevenlabs-tts "Premium ElevenLabs TTS的直接链接")

```
pip install"hermes-agent[tts-premium]"
```

### Local NeuTTS (optional)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#local-neutts-optional "Local NeuTTS \(optional\)的直接链接")

```
python -m pip install-U neutts[all]
```

### Everything[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#everything "Everything的直接链接")

```
pip install"hermes-agent[all]"
```

## Step 3: install system dependencies[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#step-3-install-system-dependencies "Step 3: install system dependencies的直接链接")
### macOS[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#macos "macOS的直接链接")

```
brew install portaudio ffmpeg opusbrew install espeak-ng
```

### Ubuntu / Debian[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#ubuntu--debian "Ubuntu / Debian的直接链接")

```
sudoaptinstall portaudio19-dev ffmpeg libopus0sudoaptinstall espeak-ng
```

Why these matter:
  * `portaudio` → microphone input / playback for CLI voice mode
  * `ffmpeg` → audio conversion for TTS and messaging delivery
  * `opus` → Discord voice codec support
  * `espeak-ng` → phonemizer backend for NeuTTS


## Step 4: choose STT and TTS providers[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#step-4-choose-stt-and-tts-providers "Step 4: choose STT and TTS providers的直接链接")
Hermes supports both local and cloud speech stacks.
### Easiest / cheapest setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#easiest--cheapest-setup "Easiest / cheapest setup的直接链接")
Use local STT and free Edge TTS:
  * STT provider: `local`
  * TTS provider: `edge`


This is usually the best place to start.
### Environment file example[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#environment-file-example "Environment file example的直接链接")
Add to `~/.hermes/.env`:

```
# Cloud STT options (local needs no key)GROQ_API_KEY=***VOICE_TOOLS_OPENAI_KEY=***# Premium TTS (optional)ELEVENLABS_API_KEY=***
```

### Provider recommendations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#provider-recommendations "Provider recommendations的直接链接")
#### Speech-to-text[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#speech-to-text "Speech-to-text的直接链接")
  * `local` → best default for privacy and zero-cost use
  * `groq` → very fast cloud transcription
  * `openai` → good paid fallback


#### Text-to-speech[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#text-to-speech "Text-to-speech的直接链接")
  * `edge` → free and good enough for most users
  * `neutts` → free local/on-device TTS
  * `elevenlabs` → best quality
  * `openai` → good middle ground
  * `mistral` → multilingual, native Opus


### If you use `hermes setup`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#if-you-use-hermes-setup "if-you-use-hermes-setup的直接链接")
If you choose NeuTTS in the setup wizard, Hermes checks whether `neutts` is already installed. If it is missing, the wizard tells you NeuTTS needs the Python package `neutts` and the system package `espeak-ng`, offers to install them for you, installs `espeak-ng` with your platform package manager, and then runs:

```
python -m pip install-U neutts[all]
```

If you skip that install or it fails, the wizard falls back to Edge TTS.
## Step 5: recommended config[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#step-5-recommended-config "Step 5: recommended config的直接链接")

```
voice:record_key:"ctrl+b"max_recording_seconds:120auto_tts:falsebeep_enabled:truesilence_threshold:200silence_duration:3.0stt:provider:"local"local:model:"base"tts:provider:"edge"edge:voice:"en-US-AriaNeural"
```

This is a good conservative default for most people.
If you want local TTS instead, switch the `tts` block to:

```
tts:provider:"neutts"neutts:ref_audio:''ref_text:''model: neuphonic/neutts-air-q4-ggufdevice: cpu
```

## Use case 1: CLI voice mode[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#use-case-1-cli-voice-mode "Use case 1: CLI voice mode的直接链接")
## Turn it on[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#turn-it-on "Turn it on的直接链接")
Start Hermes:

```
hermes
```

Inside the CLI:

```
/voice on
```

### Recording flow[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#recording-flow "Recording flow的直接链接")
Default key:
  * `Ctrl+B`


Workflow:
  1. press `Ctrl+B`
  2. speak
  3. wait for silence detection to stop recording automatically
  4. Hermes transcribes and responds
  5. if TTS is on, it speaks the answer
  6. the loop can automatically restart for continuous use


### Useful commands[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#useful-commands "Useful commands的直接链接")

```
/voice/voice on/voice off/voice tts/voice status
```

### Good CLI workflows[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#good-cli-workflows "Good CLI workflows的直接链接")
#### Walk-up debugging[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#walk-up-debugging "Walk-up debugging的直接链接")
Say:

```
I keep getting a docker permission error. Help me debug it.
```

Then continue hands-free:
  * "Read the last error again"
  * "Explain the root cause in simpler terms"
  * "Now give me the exact fix"


#### Research / brainstorming[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#research--brainstorming "Research / brainstorming的直接链接")
Great for:
  * walking around while thinking
  * dictating half-formed ideas
  * asking Hermes to structure your thoughts in real time


#### Accessibility / low-typing sessions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#accessibility--low-typing-sessions "Accessibility / low-typing sessions的直接链接")
If typing is inconvenient, voice mode is one of the fastest ways to stay in the full Hermes loop.
## Tuning CLI behavior[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#tuning-cli-behavior "Tuning CLI behavior的直接链接")
### Silence threshold[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#silence-threshold "Silence threshold的直接链接")
If Hermes starts/stops too aggressively, tune:

```
voice:silence_threshold:250
```

Higher threshold = less sensitive.
### Silence duration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#silence-duration "Silence duration的直接链接")
If you pause a lot between sentences, increase:

```
voice:silence_duration:4.0
```

### Record key[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#record-key "Record key的直接链接")
If `Ctrl+B` conflicts with your terminal or tmux habits:

```
voice:record_key:"ctrl+space"
```

## Use case 2: voice replies in Telegram or Discord[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#use-case-2-voice-replies-in-telegram-or-discord "Use case 2: voice replies in Telegram or Discord的直接链接")
This mode is simpler than full voice channels.
Hermes stays a normal chat bot, but can speak replies.
### Start the gateway[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#start-the-gateway "Start the gateway的直接链接")

```
hermes gateway
```

### Turn on voice replies[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#turn-on-voice-replies "Turn on voice replies的直接链接")
Inside Telegram or Discord:

```
/voice on
```

or

```
/voice tts
```

### Modes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#modes "Modes的直接链接")  
| Mode  | Meaning  |  
| --- | --- |  
| `off`  | text only  |  
| `voice_only`  | speak only when the user sent voice  |  
| `all`  | speak every reply  |  
### When to use which mode[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#when-to-use-which-mode "When to use which mode的直接链接")
  * `/voice on` if you want spoken replies only for voice-originating messages
  * `/voice tts` if you want a full spoken assistant all the time


### Good messaging workflows[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#good-messaging-workflows "Good messaging workflows的直接链接")
#### Telegram assistant on your phone[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#telegram-assistant-on-your-phone "Telegram assistant on your phone的直接链接")
Use when:
  * you are away from your machine
  * you want to send voice notes and get quick spoken replies
  * you want Hermes to function like a portable research or ops assistant


#### Discord DMs with spoken output[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#discord-dms-with-spoken-output "Discord DMs with spoken output的直接链接")
Useful when you want private interaction without server-channel mention behavior.
## Use case 3: Discord voice channels[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#use-case-3-discord-voice-channels "Use case 3: Discord voice channels的直接链接")
This is the most advanced mode.
Hermes joins a Discord VC, listens to user speech, transcribes it, runs the normal agent pipeline, and speaks replies back into the channel.
## Required Discord permissions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#required-discord-permissions "Required Discord permissions的直接链接")
In addition to the normal text-bot setup, make sure the bot has:
  * Connect
  * Speak
  * preferably Use Voice Activity


Also enable privileged intents in the Developer Portal:
  * Presence Intent
  * Server Members Intent
  * Message Content Intent


## Join and leave[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#join-and-leave "Join and leave的直接链接")
In a Discord text channel where the bot is present:

```
/voice join/voice leave/voice status
```

### What happens when joined[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#what-happens-when-joined "What happens when joined的直接链接")
  * users speak in the VC
  * Hermes detects speech boundaries
  * transcripts are posted in the associated text channel
  * Hermes responds in text and audio
  * the text channel is the one where `/voice join` was issued


### Best practices for Discord VC use[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#best-practices-for-discord-vc-use "Best practices for Discord VC use的直接链接")
  * keep `DISCORD_ALLOWED_USERS` tight
  * use a dedicated bot/testing channel at first
  * verify STT and TTS work in ordinary text-chat voice mode before trying VC mode


## Voice quality recommendations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#voice-quality-recommendations "Voice quality recommendations的直接链接")
### Best quality setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#best-quality-setup "Best quality setup的直接链接")
  * STT: local `large-v3` or Groq `whisper-large-v3`
  * TTS: ElevenLabs


### Best speed / convenience setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#best-speed--convenience-setup "Best speed / convenience setup的直接链接")
  * STT: local `base` or Groq
  * TTS: Edge


### Best zero-cost setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#best-zero-cost-setup "Best zero-cost setup的直接链接")
  * STT: local
  * TTS: Edge


## Common failure modes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#common-failure-modes "Common failure modes的直接链接")
### "No audio device found"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#no-audio-device-found ""No audio device found"的直接链接")
Install `portaudio`.
### "Bot joins but hears nothing"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#bot-joins-but-hears-nothing ""Bot joins but hears nothing"的直接链接")
Check:
  * your Discord user ID is in `DISCORD_ALLOWED_USERS`
  * you are not muted
  * privileged intents are enabled
  * the bot has Connect/Speak permissions


### "It transcribes but does not speak"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#it-transcribes-but-does-not-speak ""It transcribes but does not speak"的直接链接")
Check:
  * TTS provider config
  * API key / quota for ElevenLabs or OpenAI
  * `ffmpeg` install for Edge conversion paths


### "Whisper outputs garbage"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#whisper-outputs-garbage ""Whisper outputs garbage"的直接链接")
Try:
  * quieter environment
  * higher `silence_threshold`
  * different STT provider/model
  * shorter, clearer utterances


### "It works in DMs but not in server channels"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#it-works-in-dms-but-not-in-server-channels ""It works in DMs but not in server channels"的直接链接")
That is often mention policy.
By default, the bot needs an `@mention` in Discord server text channels unless configured otherwise.
## Suggested first-week setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#suggested-first-week-setup "Suggested first-week setup的直接链接")
If you want the shortest path to success:
  1. get text Hermes working
  2. install `hermes-agent[voice]`
  3. use CLI voice mode with local STT + Edge TTS
  4. then enable `/voice on` in Telegram or Discord
  5. only after that, try Discord VC mode


That progression keeps the debugging surface small.
## Where to read next[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#where-to-read-next "Where to read next的直接链接")
  * [Voice Mode feature reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/voice-mode)
  * [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging)
  * [Discord setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/discord)
  * [Telegram setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/telegram)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/configuration)


  * [What voice mode is good for](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#what-voice-mode-is-good-for)
  * [Choose your voice mode setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#choose-your-voice-mode-setup)
  * [Step 1: make sure normal Hermes works first](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#step-1-make-sure-normal-hermes-works-first)
  * [Step 2: install the right extras](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#step-2-install-the-right-extras)
    * [CLI microphone + playback](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#cli-microphone--playback)
    * [Messaging platforms](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#messaging-platforms)
    * [Premium ElevenLabs TTS](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#premium-elevenlabs-tts)
    * [Local NeuTTS (optional)](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#local-neutts-optional)
  * [Step 3: install system dependencies](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#step-3-install-system-dependencies)
    * [Ubuntu / Debian](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#ubuntu--debian)
  * [Step 4: choose STT and TTS providers](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#step-4-choose-stt-and-tts-providers)
    * [Easiest / cheapest setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#easiest--cheapest-setup)
    * [Environment file example](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#environment-file-example)
    * [Provider recommendations](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#provider-recommendations)
    * [If you use `hermes setup`](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#if-you-use-hermes-setup)
  * [Step 5: recommended config](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#step-5-recommended-config)
  * [Use case 1: CLI voice mode](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#use-case-1-cli-voice-mode)
  * [Turn it on](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#turn-it-on)
    * [Recording flow](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#recording-flow)
    * [Useful commands](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#useful-commands)
    * [Good CLI workflows](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#good-cli-workflows)
  * [Tuning CLI behavior](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#tuning-cli-behavior)
    * [Silence threshold](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#silence-threshold)
    * [Silence duration](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#silence-duration)
  * [Use case 2: voice replies in Telegram or Discord](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#use-case-2-voice-replies-in-telegram-or-discord)
    * [Start the gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#start-the-gateway)
    * [Turn on voice replies](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#turn-on-voice-replies)
    * [When to use which mode](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#when-to-use-which-mode)
    * [Good messaging workflows](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#good-messaging-workflows)
  * [Use case 3: Discord voice channels](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#use-case-3-discord-voice-channels)
  * [Required Discord permissions](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#required-discord-permissions)
  * [Join and leave](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#join-and-leave)
    * [What happens when joined](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#what-happens-when-joined)
    * [Best practices for Discord VC use](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#best-practices-for-discord-vc-use)
  * [Voice quality recommendations](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#voice-quality-recommendations)
    * [Best quality setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#best-quality-setup)
    * [Best speed / convenience setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#best-speed--convenience-setup)
    * [Best zero-cost setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#best-zero-cost-setup)
  * [Common failure modes](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#common-failure-modes)
    * ["No audio device found"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#no-audio-device-found)
    * ["Bot joins but hears nothing"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#bot-joins-but-hears-nothing)
    * ["It transcribes but does not speak"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#it-transcribes-but-does-not-speak)
    * ["Whisper outputs garbage"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#whisper-outputs-garbage)
    * ["It works in DMs but not in server channels"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#it-works-in-dms-but-not-in-server-channels)
  * [Suggested first-week setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#suggested-first-week-setup)
  * [Where to read next](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-voice-mode-with-hermes#where-to-read-next)


