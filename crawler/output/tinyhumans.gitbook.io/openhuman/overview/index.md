<!-- Source: https://tinyhumans.gitbook.io/openhuman/overview -->

OpenHuman is an open-source AI assistant designed to be the **memory** and **doer** for everything you do across your tools. Built on Rust + Tauri and licensed under GNU GPL3, it closes the gap between what AI models can do and what they actually know about _you_.
Every model in the world, all 200+ of them, shares the same fundamental limitation: they are stateless. You type a prompt, get a response, and the context evaporates. Even the ones with "memory" store a few bullet points. A few bullet points is a sticky note, not intelligence.
OpenHuman solves this with a stack that's calmly, deliberately different:
  * **A local-first** **.** Every source you connect. Gmail, Slack, GitHub, Notion, your own notes, flows through a deterministic pipeline: canonical Markdown, ≤3k-token chunks, scored, folded into per-source / per-topic / per-day summary trees. Stored in SQLite on your machine. No vector-soup black box.
  * **An** **on top of it.** The same chunks the agent reasons over land as `.md` files in a vault you can open in [Obsidianarrow-up-right](https://obsidian.md), browse, edit, and link by hand. Inspired by [Karpathy's obsidian-wiki workflowarrow-up-right](https://x.com/karpathy/status/2039805659525644595). You can't trust a memory you can't read.
  * [**118+ third-party integrations**](https://tinyhumans.gitbook.io/openhuman/features/integrations)**.** One-click OAuth into Gmail, GitHub, Slack, Notion, Stripe, Calendar, Drive, Linear, Jira and more - no API keys to wire by hand, no plugin marketplace to navigate.
  * **.** Every twenty minutes, OpenHuman pulls fresh data from every active connection and folds it into the Memory Tree without you asking, so the agent already has tomorrow's context this morning.
  * **An agent built for big data.** [Smart token compression (TokenJuice)](https://tinyhumans.gitbook.io/openhuman/features/token-compression) compacts verbose tool output before it ever enters the model's context, so sweeping through your last six months of email costs single-digit dollars. sends each task to the right model - `hint:reasoning` to a frontier model, `hint:fast` to a cheap one, vision to vision - all under one subscription. Optional keeps embeddings and summarization on-device.
  * **.** A complete agent toolbelt is wired in by default: , a , a full (filesystem, git, lint, test, grep), [browser & computer control](https://tinyhumans.gitbook.io/openhuman/features/native-tools/browser-and-computer), , , for spawning sub-agents, and - STT in, TTS out, mascot lip-sync, and a live Google Meet agent that joins meetings, transcribes them into your Memory Tree, and can speak back into the call. No "install a plugin to read files" friction.
  * **Simple, UI-first.** A clean desktop experience and short onboarding paths take you from install to a working agent in a few clicks - no config-first setup, no terminal required. The agent has [a facearrow-up-right](https://github.com/tinyhumansai/openhuman/blob/main/gitbooks/features/mascot.md): a desktop mascot that speaks, reacts to its surroundings, joins your Google Meets as a real participant, remembers you across weeks, and keeps thinking in the background even when you've stopped typing.


Together, these turn OpenHuman into something fundamentally different from a chatbot. It is an AI agent that consumes large amounts of personal data at low cost, maintains a persistent and evolving understanding of your world, and takes proactive actions on your behalf.
circle-exclamation
OpenHuman is not AGI. But it is a meaningful architectural step closer, with better memory, better orchestration, and better tooling.
[NextGetting Startedchevron-right](https://tinyhumans.gitbook.io/openhuman/overview/getting-started)
Last updated 4 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
