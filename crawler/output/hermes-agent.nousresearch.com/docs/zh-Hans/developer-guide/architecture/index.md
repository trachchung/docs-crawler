<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture -->

本页总览
This page is the top-level map of Hermes Agent internals. Use it to orient yourself in the codebase, then dive into subsystem-specific docs for implementation details.
## System Overview[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#system-overview "System Overview的直接链接")

```
┌─────────────────────────────────────────────────────────────────────┐│                        Entry Points                                  ││                                                                      ││  CLI (cli.py)    Gateway (gateway/run.py)    ACP (acp_adapter/)     ││  Batch Runner    API Server                  Python Library          │└──────────┬──────────────┬───────────────────────┬───────────────────┘           │              │                       │           ▼              ▼                       ▼┌─────────────────────────────────────────────────────────────────────┐│                     AIAgent (run_agent.py)                          ││                                                                     ││  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               ││  │ Prompt       │  │ Provider     │  │ Tool         │               ││  │ Builder      │  │ Resolution   │  │ Dispatch     │               ││  │ (prompt_     │  │ (runtime_    │  │ (model_      │               ││  │  builder.py) │  │  provider.py)│  │  tools.py)   │               ││  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘               ││         │                 │                 │                       ││  ┌──────┴───────┐  ┌──────┴───────┐  ┌──────┴───────┐               ││  │ Compression  │  │ 3 API Modes  │  │ Tool Registry│               ││  │ & Caching    │  │ chat_compl.  │  │ (registry.py)│               ││  │              │  │ codex_resp.  │  │ 70+ tools    │               ││  │              │  │ anthropic    │  │ 28 toolsets  │               ││  └──────────────┘  └──────────────┘  └──────────────┘               │└─────────┴─────────────────┴─────────────────┴───────────────────────┘           │                                    │           ▼                                    ▼┌───────────────────┐              ┌──────────────────────┐│ Session Storage   │              │ Tool Backends         ││ (SQLite + FTS5)   │              │ Terminal (7 backends) ││ hermes_state.py   │              │ Browser (5 backends)  ││ gateway/session.py│              │ Web (4 backends)      │└───────────────────┘              │ MCP (dynamic)         │                                   │ File, Vision, etc.    │                                   └──────────────────────┘
```

## Directory Structure[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#directory-structure "Directory Structure的直接链接")

```
hermes-agent/├── run_agent.py              # AIAgent — core conversation loop (large file)├── cli.py                    # HermesCLI — interactive terminal UI (large file)├── model_tools.py            # Tool discovery, schema collection, dispatch├── toolsets.py               # Tool groupings and platform presets├── hermes_state.py           # SQLite session/state database with FTS5├── hermes_constants.py       # HERMES_HOME, profile-aware paths├── batch_runner.py           # Batch trajectory generation├── agent/                    # Agent internals│   ├── prompt_builder.py     # System prompt assembly│   ├── context_engine.py     # ContextEngine ABC (pluggable)│   ├── context_compressor.py # Default engine — lossy summarization│   ├── prompt_caching.py     # Anthropic prompt caching│   ├── auxiliary_client.py   # Auxiliary LLM for side tasks (vision, summarization)│   ├── model_metadata.py     # Model context lengths, token estimation│   ├── models_dev.py         # models.dev registry integration│   ├── anthropic_adapter.py  # Anthropic Messages API format conversion│   ├── display.py            # KawaiiSpinner, tool preview formatting│   ├── skill_commands.py     # Skill slash commands│   ├── memory_manager.py    # Memory manager orchestration│   ├── memory_provider.py   # Memory provider ABC│   └── trajectory.py         # Trajectory saving helpers├── hermes_cli/               # CLI subcommands and setup│   ├── main.py               # Entry point — all `hermes` subcommands (large file)│   ├── config.py             # DEFAULT_CONFIG, OPTIONAL_ENV_VARS, migration│   ├── commands.py           # COMMAND_REGISTRY — central slash command definitions│   ├── auth.py               # PROVIDER_REGISTRY, credential resolution│   ├── runtime_provider.py   # Provider → api_mode + credentials│   ├── models.py             # Model catalog, provider model lists│   ├── model_switch.py       # /model command logic (CLI + gateway shared)│   ├── setup.py              # Interactive setup wizard (large file)│   ├── skin_engine.py        # CLI theming engine│   ├── skills_config.py      # hermes skills — enable/disable per platform│   ├── skills_hub.py         # /skills slash command│   ├── tools_config.py       # hermes tools — enable/disable per platform│   ├── plugins.py            # PluginManager — discovery, loading, hooks│   ├── callbacks.py          # Terminal callbacks (clarify, sudo, approval)│   └── gateway.py            # hermes gateway start/stop├── tools/                    # Tool implementations (one file per tool)│   ├── registry.py           # Central tool registry│   ├── approval.py           # Dangerous command detection│   ├── terminal_tool.py      # Terminal orchestration│   ├── process_registry.py   # Background process management│   ├── file_tools.py         # read_file, write_file, patch, search_files│   ├── web_tools.py          # web_search, web_extract│   ├── browser_tool.py       # 10 browser automation tools│   ├── code_execution_tool.py # execute_code sandbox│   ├── delegate_tool.py      # Subagent delegation│   ├── mcp_tool.py           # MCP client (large file)│   ├── credential_files.py   # File-based credential passthrough│   ├── env_passthrough.py    # Env var passthrough for sandboxes│   ├── ansi_strip.py         # ANSI escape stripping│   └── environments/         # Terminal backends (local, docker, ssh, modal, daytona, singularity)├── gateway/                  # Messaging platform gateway│   ├── run.py                # GatewayRunner — message dispatch (large file)│   ├── session.py            # SessionStore — conversation persistence│   ├── delivery.py           # Outbound message delivery│   ├── pairing.py            # DM pairing authorization│   ├── hooks.py              # Hook discovery and lifecycle events│   ├── mirror.py             # Cross-session message mirroring│   ├── status.py             # Token locks, profile-scoped process tracking│   ├── builtin_hooks/        # Extension point for always-registered hooks (none shipped)│   └── platforms/            # 20 adapters: telegram, discord, slack, whatsapp,│                             #   signal, matrix, mattermost, email, sms,│                             #   dingtalk, feishu, wecom, wecom_callback, weixin,│                             #   bluebubbles, qqbot, homeassistant, webhook, api_server,│                             #   yuanbao├── acp_adapter/              # ACP server (VS Code / Zed / JetBrains)├── cron/                     # Scheduler (jobs.py, scheduler.py)├── plugins/memory/           # Memory provider plugins├── plugins/context_engine/   # Context engine plugins├── environments/             # RL training environments (Atropos)├── skills/                   # Bundled skills (always available)├── optional-skills/          # Official optional skills (install explicitly)├── website/                  # Docusaurus documentation site└── tests/                    # Pytest suite (~3,000+ tests)
```

## Data Flow[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#data-flow "Data Flow的直接链接")
### CLI Session[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#cli-session "CLI Session的直接链接")

```
User input → HermesCLI.process_input()  → AIAgent.run_conversation()    → prompt_builder.build_system_prompt()    → runtime_provider.resolve_runtime_provider()    → API call (chat_completions / codex_responses / anthropic_messages)    → tool_calls? → model_tools.handle_function_call() → loop    → final response → display → save to SessionDB
```

### Gateway Message[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#gateway-message "Gateway Message的直接链接")

```
Platform event → Adapter.on_message() → MessageEvent  → GatewayRunner._handle_message()    → authorize user    → resolve session key    → create AIAgent with session history    → AIAgent.run_conversation()    → deliver response back through adapter
```

### Cron Job[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#cron-job "Cron Job的直接链接")

```
Scheduler tick → load due jobs from jobs.json  → create fresh AIAgent (no history)  → inject attached skills as context  → run job prompt  → deliver response to target platform  → update job state and next_run
```

## Recommended Reading Order[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#recommended-reading-order "Recommended Reading Order的直接链接")
If you are new to the codebase:
  1. **This page** — orient yourself
  2. **[Agent Loop Internals](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/agent-loop)** — how AIAgent works
  3. **[Prompt Assembly](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/prompt-assembly)** — system prompt construction
  4. **[Provider Runtime Resolution](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/provider-runtime)** — how providers are selected
  5. **[Adding Providers](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-providers)** — practical guide to adding a new provider
  6. **[Tools Runtime](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/tools-runtime)** — tool registry, dispatch, environments
  7. **[Session Storage](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage)** — SQLite schema, FTS5, session lineage
  8. **[Gateway Internals](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/gateway-internals)** — messaging platform gateway
  9. **[Context Compression& Prompt Caching](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/context-compression-and-caching)** — compression and caching
  10. **[ACP Internals](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/acp-internals)** — IDE integration
  11. **[Environments, Benchmarks& Data Generation](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/environments)** — RL training


## Major Subsystems[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#major-subsystems "Major Subsystems的直接链接")
### Agent Loop[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#agent-loop "Agent Loop的直接链接")
The synchronous orchestration engine (`AIAgent` in `run_agent.py`). Handles provider selection, prompt construction, tool execution, retries, fallback, callbacks, compression, and persistence. Supports three API modes for different provider backends.
→ [Agent Loop Internals](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/agent-loop)
### Prompt System[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#prompt-system "Prompt System的直接链接")
Prompt construction and maintenance across the conversation lifecycle:
  * **`prompt_builder.py`**— Assembles the system prompt from: personality (SOUL.md), memory (MEMORY.md, USER.md), skills, context files (AGENTS.md, .hermes.md), tool-use guidance, and model-specific instructions
  * **`prompt_caching.py`**— Applies Anthropic cache breakpoints for prefix caching
  * **`context_compressor.py`**— Summarizes middle conversation turns when context exceeds thresholds


→ [Prompt Assembly](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/prompt-assembly), [Context Compression & Prompt Caching](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/context-compression-and-caching)
### Provider Resolution[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#provider-resolution "Provider Resolution的直接链接")
A shared runtime resolver used by CLI, gateway, cron, ACP, and auxiliary calls. Maps `(provider, model)` tuples to `(api_mode, api_key, base_url)`. Handles 18+ providers, OAuth flows, credential pools, and alias resolution.
→ [Provider Runtime Resolution](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/provider-runtime)
### Tool System[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#tool-system "Tool System的直接链接")
Central tool registry (`tools/registry.py`) with 70+ registered tools across ~28 toolsets. Each tool file self-registers at import time. The registry handles schema collection, dispatch, availability checking, and error wrapping. Terminal tools support 7 backends (local, Docker, SSH, Daytona, Modal, Singularity, Vercel Sandbox).
→ [Tools Runtime](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/tools-runtime)
### Session Persistence[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#session-persistence "Session Persistence的直接链接")
SQLite-based session storage with FTS5 full-text search. Sessions have lineage tracking (parent/child across compressions), per-platform isolation, and atomic writes with contention handling.
→ [Session Storage](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage)
### Messaging Gateway[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#messaging-gateway "Messaging Gateway的直接链接")
Long-running process with 20 platform adapters, unified session routing, user authorization (allowlists + DM pairing), slash command dispatch, hook system, cron ticking, and background maintenance.
→ [Gateway Internals](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/gateway-internals)
### Plugin System[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#plugin-system "Plugin System的直接链接")
Three discovery sources: `~/.hermes/plugins/` (user), `.hermes/plugins/` (project), and pip entry points. Plugins register tools, hooks, and CLI commands through a context API. Two specialized plugin types exist: memory providers (`plugins/memory/`) and context engines (`plugins/context_engine/`). Both are single-select — only one of each can be active at a time, configured via `hermes plugins` or `config.yaml`.
→ [Plugin Guide](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/build-a-hermes-plugin), [Memory Provider Plugin](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/memory-provider-plugin)
### Cron[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#cron "Cron的直接链接")
First-class agent tasks (not shell tasks). Jobs store in JSON, support multiple schedule formats, can attach skills and scripts, and deliver to any platform.
→ [Cron Internals](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/cron-internals)
### ACP Integration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#acp-integration "ACP Integration的直接链接")
Exposes Hermes as an editor-native agent over stdio/JSON-RPC for VS Code, Zed, and JetBrains.
→ [ACP Internals](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/acp-internals)
### RL / Environments / Trajectories[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#rl--environments--trajectories "RL / Environments / Trajectories的直接链接")
Full environment framework for evaluation and RL training. Integrates with Atropos, supports multiple tool-call parsers, and generates ShareGPT-format trajectories.
→ [Environments, Benchmarks & Data Generation](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/environments), [Trajectories & Training Format](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/trajectory-format)
## Design Principles[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#design-principles "Design Principles的直接链接")  
| Principle  | What it means in practice  |  
| --- | --- |  
| **Prompt stability**  | System prompt doesn't change mid-conversation. No cache-breaking mutations except explicit user actions (`/model`).  |  
| **Observable execution**  | Every tool call is visible to the user via callbacks. Progress updates in CLI (spinner) and gateway (chat messages).  |  
| **Interruptible**  | API calls and tool execution can be cancelled mid-flight by user input or signals.  |  
| **Platform-agnostic core**  | One AIAgent class serves CLI, gateway, ACP, batch, and API server. Platform differences live in the entry point, not the agent.  |  
| **Loose coupling**  | Optional subsystems (MCP, plugins, memory providers, RL environments) use registry patterns and check_fn gating, not hard dependencies.  |  
| **Profile isolation**  | Each profile (`hermes -p <name>`) gets its own HERMES_HOME, config, memory, sessions, and gateway PID. Multiple profiles run concurrently.  |  
## File Dependency Chain[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#file-dependency-chain "File Dependency Chain的直接链接")

```
tools/registry.py  (no deps — imported by all tool files)tools/*.py  (each calls registry.register() at import time)model_tools.py  (imports tools/registry + triggers tool discovery)run_agent.py, cli.py, batch_runner.py, environments/
```

This chain means tool registration happens at import time, before any agent instance is created. Any `tools/*.py` file with a top-level `registry.register()` call is auto-discovered — no manual import list needed.
  * [System Overview](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#system-overview)
  * [Directory Structure](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#directory-structure)
  * [Data Flow](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#data-flow)
    * [CLI Session](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#cli-session)
    * [Gateway Message](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#gateway-message)
  * [Recommended Reading Order](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#recommended-reading-order)
  * [Major Subsystems](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#major-subsystems)
    * [Prompt System](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#prompt-system)
    * [Provider Resolution](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#provider-resolution)
    * [Tool System](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#tool-system)
    * [Session Persistence](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#session-persistence)
    * [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#messaging-gateway)
    * [Plugin System](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#plugin-system)
    * [ACP Integration](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#acp-integration)
    * [RL / Environments / Trajectories](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#rl--environments--trajectories)
  * [Design Principles](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#design-principles)
  * [File Dependency Chain](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture#file-dependency-chain)


