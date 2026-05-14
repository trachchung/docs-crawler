<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations -->

本页总览
Hermes Agent connects to external systems for AI inference, tool servers, IDE workflows, programmatic access, and more. These integrations extend what Hermes can do and where it can run.
## AI Providers & Routing[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#ai-providers--routing "AI Providers & Routing的直接链接")
Hermes supports multiple AI inference providers out of the box. Use `hermes model` to configure interactively, or set them in `config.yaml`.
  * **[AI Providers](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/provider-routing)** — OpenRouter, Anthropic, OpenAI, Google, and any OpenAI-compatible endpoint. Hermes auto-detects capabilities like vision, streaming, and tool use per provider.
  * **[Provider Routing](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/provider-routing)** — Fine-grained control over which underlying providers handle your OpenRouter requests. Optimize for cost, speed, or quality with sorting, whitelists, blacklists, and explicit priority ordering.
  * **[Fallback Providers](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/fallback-providers)** — Automatic failover to backup LLM providers when your primary model encounters errors. Includes primary model fallback and independent auxiliary task fallback for vision, compression, and web extraction.


## Tool Servers (MCP)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#tool-servers-mcp "Tool Servers \(MCP\)的直接链接")
  * **[MCP Servers](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/mcp)** — Connect Hermes to external tool servers via Model Context Protocol. Access tools from GitHub, databases, file systems, browser stacks, internal APIs, and more without writing native Hermes tools. Supports both stdio and SSE transports, per-server tool filtering, and capability-aware resource/prompt registration.


## Web Search Backends[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#web-search-backends "Web Search Backends的直接链接")
The `web_search` and `web_extract` tools support four backend providers, configured via `config.yaml` or `hermes tools`:  
| Backend  | Env Var  | Search  | Extract  | Crawl  |  
| --- | --- | --- | --- | --- |  
|  **Firecrawl** (default)  | `FIRECRAWL_API_KEY`  | ✔  | ✔  | ✔  |  
| **Parallel**  | `PARALLEL_API_KEY`  | ✔  | ✔  | —  |  
| **Tavily**  | `TAVILY_API_KEY`  | ✔  | ✔  | ✔  |  
| **Exa**  | `EXA_API_KEY`  | ✔  | ✔  | —  |  
Quick setup example:

```
web:backend: firecrawl    # firecrawl | parallel | tavily | exa
```

If `web.backend` is not set, the backend is auto-detected from whichever API key is available. Self-hosted Firecrawl is also supported via `FIRECRAWL_API_URL`.
## Browser Automation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#browser-automation "Browser Automation的直接链接")
Hermes includes full browser automation with multiple backend options for navigating websites, filling forms, and extracting information:
  * **Browserbase** — Managed cloud browsers with anti-bot tooling, CAPTCHA solving, and residential proxies
  * **Browser Use** — Alternative cloud browser provider
  * **Local Chrome via CDP** — Connect to your running Chrome instance using `/browser connect`
  * **Local Chromium** — Headless local browser via the `agent-browser` CLI


See [Browser Automation](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/browser) for setup and usage.
## Voice & TTS Providers[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#voice--tts-providers "Voice & TTS Providers的直接链接")
Text-to-speech and speech-to-text across all messaging platforms:  
| Provider  | Quality  | Cost  | API Key  |  
| --- | --- | --- | --- |  
|  **Edge TTS** (default)  | Good  | Free  | None needed  |  
| **ElevenLabs**  | Excellent  | Paid  | `ELEVENLABS_API_KEY`  |  
| **OpenAI TTS**  | Good  | Paid  | `VOICE_TOOLS_OPENAI_KEY`  |  
| **MiniMax**  | Good  | Paid  | `MINIMAX_API_KEY`  |  
| **NeuTTS**  | Good  | Free  | None needed  |  
Speech-to-text supports six providers: local faster-whisper (free, runs on-device), a local command wrapper, Groq, OpenAI Whisper API, Mistral, and xAI. Voice message transcription works across Telegram, Discord, WhatsApp, and other messaging platforms. See [Voice & TTS](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/tts) and [Voice Mode](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/voice-mode) for details.
## IDE & Editor Integration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#ide--editor-integration "IDE & Editor Integration的直接链接")
  * **[IDE Integration (ACP)](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/acp)** — Use Hermes Agent inside ACP-compatible editors such as VS Code, Zed, and JetBrains. Hermes runs as an ACP server, rendering chat messages, tool activity, file diffs, and terminal commands inside your editor.


## Programmatic Access[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#programmatic-access "Programmatic Access的直接链接")
  * — Expose Hermes as an OpenAI-compatible HTTP endpoint. Any frontend that speaks the OpenAI format — Open WebUI, LobeChat, LibreChat, NextChat, ChatBox — can connect and use Hermes as a backend with its full toolset.


## Memory & Personalization[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#memory--personalization "Memory & Personalization的直接链接")
  * **[Built-in Memory](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/memory)** — Persistent, curated memory via `MEMORY.md` and `USER.md` files. The agent maintains bounded stores of personal notes and user profile data that survive across sessions.
  * **[Memory Providers](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/memory-providers)** — Plug in external memory backends for deeper personalization. Eight providers are supported: Honcho (dialectic reasoning), OpenViking (tiered retrieval), Mem0 (cloud extraction), Hindsight (knowledge graphs), Holographic (local SQLite), RetainDB (hybrid search), ByteRover (CLI-based), and Supermemory.


## Messaging Platforms[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#messaging-platforms "Messaging Platforms的直接链接")
Hermes runs as a gateway bot on 19+ messaging platforms, all configured through the same `gateway` subsystem:
  * , , , , , , , , , , **[Feishu/Lark](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/feishu)** , , **[WeCom Callback](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/wecom-callback)** , , , , , **[Home Assistant](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/homeassistant)** , **[Microsoft Teams](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/teams)** , 


See the [Messaging Gateway overview](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging) for the platform comparison table and setup guide.
## Home Automation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#home-automation "Home Automation的直接链接")
  * **[Home Assistant](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/homeassistant)** — Control smart home devices via four dedicated tools (`ha_list_entities`, `ha_get_state`, `ha_list_services`, `ha_call_service`). The Home Assistant toolset activates automatically when `HASS_TOKEN` is configured.


## Plugins[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#plugins "Plugins的直接链接")
  * **[Plugin System](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/plugins)** — Extend Hermes with custom tools, lifecycle hooks, and CLI commands without modifying core code. Plugins are discovered from `~/.hermes/plugins/`, project-local `.hermes/plugins/`, and pip-installed entry points.
  * **[Build a Plugin](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/build-a-hermes-plugin)** — Step-by-step guide for creating Hermes plugins with tools, hooks, and CLI commands.


## Training & Evaluation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#training--evaluation "Training & Evaluation的直接链接")
  * **[RL Training](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/rl-training)** — Generate trajectory data from agent sessions for reinforcement learning and model fine-tuning. Supports Atropos environments with customizable reward functions.
  * **[Batch Processing](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/batch-processing)** — Run the agent across hundreds of prompts in parallel, generating structured ShareGPT-format trajectory data for training data generation or evaluation.


  * [AI Providers & Routing](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#ai-providers--routing)
  * [Tool Servers (MCP)](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#tool-servers-mcp)
  * [Web Search Backends](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#web-search-backends)
  * [Browser Automation](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#browser-automation)
  * [Voice & TTS Providers](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#voice--tts-providers)
  * [IDE & Editor Integration](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#ide--editor-integration)
  * [Programmatic Access](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#programmatic-access)
  * [Memory & Personalization](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#memory--personalization)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#messaging-platforms)
  * [Home Automation](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#home-automation)
  * [Training & Evaluation](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations#training--evaluation)


