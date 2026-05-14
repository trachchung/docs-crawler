<!-- Source: https://tinyhumans.gitbook.io/openhuman/features/native-tools/voice -->

OpenHuman is voice-first when you want it to be. STT, TTS, and the live Google Meet agent are part of the core, not a third-party plugin.
## 
Speech-to-text
  * **Hotkey** - push-to-talk and toggle modes.
  * **Audio capture** - cross-platform mic capture with voice-activity detection.
  * **Streaming transcription** - words appear as you speak.
  * **Hallucination filter** - strips well-known artefacts ("Thanks for watching", silence-induced phrases).
  * **Postprocess** - punctuation, capitalisation, dictation cleanup.


Dictation can replace the active text input on your desktop, or be sent straight into a chat with the agent.
## 
Text-to-speech
Reply speech routes through a hosted TTS model. The agent's responses can be spoken back in a voice you pick, with natural timing and prosody. Voice selection is configurable per user, and the mascot avatar lip-syncs to the audio stream via a viseme map.
## 
Live Google Meet agent
OpenHuman's flagship voice integration:
  * Joins a Google Meet via the embedded webview.
  * Streams audio out to STT in real time, transcribes everyone in the call, and writes structured notes into the as the meeting progresses.
  * When you ask it to speak (or it decides it has something useful to add), it generates audio through the TTS model and **plays it back into the meeting as an outbound camera/mic stream** , so other participants actually hear it.


## 
Privacy
  * Audio capture is local. Streaming STT goes through the OpenHuman backend; no recording is retained beyond the live transcript.
  * TTS audio is streamed and discarded - nothing stored.
  * Meeting transcripts land in your local memory tree, like any other source.


## 
See also
  * - where Meet transcripts and notes live.
  * - Meet's brain uses `hint:fast` for low-latency conversational turns.


[PreviousCron & Schedulingchevron-left](https://tinyhumans.gitbook.io/openhuman/features/native-tools/cron)[NextMemory Toolschevron-right](https://tinyhumans.gitbook.io/openhuman/features/native-tools/memory-tools)
Last updated 4 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
