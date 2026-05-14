<!-- Source: https://tinyhumans.gitbook.io/openhuman/overview/getting-started -->

This page walks you through installing OpenHuman, going through the in-app onboarding, and running your first request.
OpenHuman is open source under the GNU GPL3 license. The codebase is at [github.com/tinyhumansai/openhumanarrow-up-right](https://github.com/tinyhumansai/openhuman).
## 
System requirements
OpenHuman runs on **macOS, Windows and Linux** desktops. 4 GB+ RAM is recommended; 16 GB+ if you intend to ingest very large mailboxes or repos, or run a on the same machine.
### 
Permissions
The first time you launch OpenHuman, the OS will prompt for the permissions the app needs (Accessibility on macOS, Input Monitoring for the voice hotkey, Camera/Microphone if you plan to use the ). You can review and adjust these any time under **Settings → Automation & Channels**.
## 
1. Download and install
Get the OpenHuman desktop app from <http://tinyhumans.ai/openhuman>[arrow-up-right](http://tinyhumans.ai/openhuman) or via your platform's package manager. Open the app once it's installed.
## 
2. Sign in
The first screen is **"Sign in! Let's Cook"**. Multiple sign-in options are available, including social login. There's also an **Advanced** panel for pointing the app at a custom core RPC URL if you're running your own backend; most users can ignore it.
circle-info
**No permanent lock-in.** Signing in does not grant OpenHuman ongoing access to anything. All third-party access requires explicit OAuth approval per integration in the steps below.
## 
3. Run your first request
Once Gmail has been ingested (the first auto-fetch tick happens within twenty minutes), try prompts like:
**Briefings**
  * "What do I need to know from the last 12 hours?"
  * "What's waiting on me?"


**Cross-source queries**
  * "Summarize what I missed today."
  * "What are the key decisions from this week?"
  * "Extract action items from my recent conversations."
  * "What did Sarah say about the project across email and chat?"


OpenHuman picks the right model for each task automatically. See .
## 
4. Open the Obsidian vault
The Memory tab has a **View vault in Obsidian** button. Click it to open `<workspace>/wiki/` in [Obsidianarrow-up-right](https://obsidian.md). You can browse the agent's summaries, drop in your own notes, and even build manual links - the agent will pick up your edits on the next ingest. See .
## 
5. Let the mascot do more
Now that the agent has memory and a model, the rest of the product is about giving it more surfaces:
  * - drop a Google Meet link in and the mascot joins as a real participant: it listens, takes notes into the Memory Tree, speaks back into the call, and uses tools live.
  * [**Auto-fetch from Integrations**](https://tinyhumans.gitbook.io/openhuman/features/obsidian-wiki/auto-fetch) - connect more sources from **Settings** ; every twenty minutes the scheduler pulls fresh data into your tree.
  * - push-to-talk dictation and TTS replies so you can talk to OpenHuman instead of typing.
  * - let the mascot keep working on standing tasks while you're away.


## 
Join the community
OpenHuman is in early beta. Feedback and contributions make a real difference at this stage.
  * **GitHub:** [github.com/tinyhumansai/openhumanarrow-up-right](https://github.com/tinyhumansai/openhuman)
  * **Discord:** [discord.tinyhumans.aiarrow-up-right](https://discord.tinyhumans.ai)


[PreviousWelcome to OpenHumanchevron-left](https://tinyhumans.gitbook.io/openhuman)[NextRealtime Mascotchevron-right](https://tinyhumans.gitbook.io/openhuman/features/mascot)
Last updated 0 minutes ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
