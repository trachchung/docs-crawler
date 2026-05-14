<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp -->

本页总览
MCP lets Hermes Agent connect to external tool servers so the agent can use tools that live outside Hermes itself — GitHub, databases, file systems, browser stacks, internal APIs, and more.
If you have ever wanted Hermes to use a tool that already exists somewhere else, MCP is usually the cleanest way to do it.
## What MCP gives you[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#what-mcp-gives-you "What MCP gives you的直接链接")
  * Access to external tool ecosystems without writing a native Hermes tool first
  * Local stdio servers and remote HTTP MCP servers in the same config
  * Automatic tool discovery and registration at startup
  * Utility wrappers for MCP resources and prompts when supported by the server
  * Per-server filtering so you can expose only the MCP tools you actually want Hermes to see


## Quick start[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#quick-start "Quick start的直接链接")
  1. Install MCP support (already included if you used the standard install script):



```
cd ~/.hermes/hermes-agentuv pip install-e".[mcp]"
```

  1. Add an MCP server to `~/.hermes/config.yaml`:



```
mcp_servers:filesystem:command:"npx"args:["-y","@modelcontextprotocol/server-filesystem","/home/user/projects"]
```

  1. Start Hermes:



```
hermes chat
```

  1. Ask Hermes to use the MCP-backed capability.


For example:

```
List the files in /home/user/projects and summarize the repo structure.
```

Hermes will discover the MCP server's tools and use them like any other tool.
## Two kinds of MCP servers[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#two-kinds-of-mcp-servers "Two kinds of MCP servers的直接链接")
### Stdio servers[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#stdio-servers "Stdio servers的直接链接")
Stdio servers run as local subprocesses and talk over stdin/stdout.

```
mcp_servers:github:command:"npx"args:["-y","@modelcontextprotocol/server-github"]env:GITHUB_PERSONAL_ACCESS_TOKEN:"***"
```

Use stdio servers when:
  * the server is installed locally
  * you want low-latency access to local resources
  * you are following MCP server docs that show `command`, `args`, and `env`


### HTTP servers[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#http-servers "HTTP servers的直接链接")
HTTP MCP servers are remote endpoints Hermes connects to directly.

```
mcp_servers:remote_api:url:"https://mcp.example.com/mcp"headers:Authorization:"Bearer ***"
```

Use HTTP servers when:
  * the MCP server is hosted elsewhere
  * your organization exposes internal MCP endpoints
  * you do not want Hermes spawning a local subprocess for that integration


## Basic configuration reference[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#basic-configuration-reference "Basic configuration reference的直接链接")
Hermes reads MCP config from `~/.hermes/config.yaml` under `mcp_servers`.
### Common keys[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#common-keys "Common keys的直接链接")  
| Key  | Type  | Meaning  |  
| --- | --- | --- |  
| `command`  | string  | Executable for a stdio MCP server  |  
| `args`  | list  | Arguments for the stdio server  |  
| `env`  | mapping  | Environment variables passed to the stdio server  |  
| `url`  | string  | HTTP MCP endpoint  |  
| `headers`  | mapping  | HTTP headers for remote servers  |  
| `timeout`  | number  | Tool call timeout  |  
| `connect_timeout`  | number  | Initial connection timeout  |  
| `enabled`  | bool  | If `false`, Hermes skips the server entirely  |  
| `tools`  | mapping  | Per-server tool filtering and utility policy  |  
### Minimal stdio example[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#minimal-stdio-example "Minimal stdio example的直接链接")

```
mcp_servers:filesystem:command:"npx"args:["-y","@modelcontextprotocol/server-filesystem","/tmp"]
```

### Minimal HTTP example[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#minimal-http-example "Minimal HTTP example的直接链接")

```
mcp_servers:company_api:url:"https://mcp.internal.example.com"headers:Authorization:"Bearer ***"
```

## How Hermes registers MCP tools[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#how-hermes-registers-mcp-tools "How Hermes registers MCP tools的直接链接")
Hermes prefixes MCP tools so they do not collide with built-in names:

```
mcp_<server_name>_<tool_name>
```

Examples:  
| Server  | MCP tool  | Registered name  |  
| --- | --- | --- |  
| `filesystem`  | `read_file`  | `mcp_filesystem_read_file`  |  
| `github`  | `create-issue`  | `mcp_github_create_issue`  |  
| `my-api`  | `query.data`  | `mcp_my_api_query_data`  |  
In practice, you usually do not need to call the prefixed name manually — Hermes sees the tool and chooses it during normal reasoning.
## MCP utility tools[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#mcp-utility-tools "MCP utility tools的直接链接")
When supported, Hermes also registers utility tools around MCP resources and prompts:
  * `list_resources`
  * `read_resource`
  * `list_prompts`
  * `get_prompt`


These are registered per server with the same prefix pattern, for example:
  * `mcp_github_list_resources`
  * `mcp_github_get_prompt`


### Important[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#important "Important的直接链接")
These utility tools are now capability-aware:
  * Hermes only registers resource utilities if the MCP session actually supports resource operations
  * Hermes only registers prompt utilities if the MCP session actually supports prompt operations


So a server that exposes callable tools but no resources/prompts will not get those extra wrappers.
## Per-server filtering[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#per-server-filtering "Per-server filtering的直接链接")
You can control which tools each MCP server contributes to Hermes, allowing fine-grained management of your tool namespace.
### Disable a server entirely[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#disable-a-server-entirely "Disable a server entirely的直接链接")

```
mcp_servers:legacy:url:"https://mcp.legacy.internal"enabled:false
```

If `enabled: false`, Hermes skips the server completely and does not even attempt a connection.
### Whitelist server tools[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#whitelist-server-tools "Whitelist server tools的直接链接")

```
mcp_servers:github:command:"npx"args:["-y","@modelcontextprotocol/server-github"]env:GITHUB_PERSONAL_ACCESS_TOKEN:"***"tools:include:[create_issue, list_issues]
```

Only those MCP server tools are registered.
### Blacklist server tools[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#blacklist-server-tools "Blacklist server tools的直接链接")

```
mcp_servers:stripe:url:"https://mcp.stripe.com"tools:exclude:[delete_customer]
```

All server tools are registered except the excluded ones.
### Precedence rule[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#precedence-rule "Precedence rule的直接链接")
If both are present:

```
tools:include:[create_issue]exclude:[create_issue, delete_issue]
```

`include` wins.
### Filter utility tools too[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#filter-utility-tools-too "Filter utility tools too的直接链接")
You can also separately disable Hermes-added utility wrappers:

```
mcp_servers:docs:url:"https://mcp.docs.example.com"tools:prompts:falseresources:false
```

That means:
  * `tools.resources: false` disables `list_resources` and `read_resource`
  * `tools.prompts: false` disables `list_prompts` and `get_prompt`


### Full example[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#full-example "Full example的直接链接")

```
mcp_servers:github:command:"npx"args:["-y","@modelcontextprotocol/server-github"]env:GITHUB_PERSONAL_ACCESS_TOKEN:"***"tools:include:[create_issue, list_issues, search_code]prompts:falsestripe:url:"https://mcp.stripe.com"headers:Authorization:"Bearer ***"tools:exclude:[delete_customer]resources:falselegacy:url:"https://mcp.legacy.internal"enabled:false
```

## What happens if everything is filtered out?[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#what-happens-if-everything-is-filtered-out "What happens if everything is filtered out?的直接链接")
If your config filters out all callable tools and disables or omits all supported utilities, Hermes does not create an empty runtime MCP toolset for that server.
That keeps the tool list clean.
## Runtime behavior[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#runtime-behavior "Runtime behavior的直接链接")
### Discovery time[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#discovery-time "Discovery time的直接链接")
Hermes discovers MCP servers at startup and registers their tools into the normal tool registry.
### Dynamic Tool Discovery[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#dynamic-tool-discovery "Dynamic Tool Discovery的直接链接")
MCP servers can notify Hermes when their available tools change at runtime by sending a `notifications/tools/list_changed` notification. When Hermes receives this notification, it automatically re-fetches the server's tool list and updates the registry — no manual `/reload-mcp` required.
This is useful for MCP servers whose capabilities change dynamically (e.g. a server that adds tools when a new database schema is loaded, or removes tools when a service goes offline).
The refresh is lock-protected so rapid-fire notifications from the same server don't cause overlapping refreshes. Prompt and resource change notifications (`prompts/list_changed`, `resources/list_changed`) are received but not yet acted on.
### Reloading[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#reloading "Reloading的直接链接")
If you change MCP config, use:

```
/reload-mcp
```

This reloads MCP servers from config and refreshes the available tool list. For runtime tool changes pushed by the server itself, see [Dynamic Tool Discovery](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#dynamic-tool-discovery) above.
### Toolsets[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#toolsets "Toolsets的直接链接")
Each configured MCP server also creates a runtime toolset when it contributes at least one registered tool:

```
mcp-<server>
```

That makes MCP servers easier to reason about at the toolset level.
## Security model[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#security-model "Security model的直接链接")
### Stdio env filtering[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#stdio-env-filtering "Stdio env filtering的直接链接")
For stdio servers, Hermes does not blindly pass your full shell environment.
Only explicitly configured `env` plus a safe baseline are passed through. This reduces accidental secret leakage.
### Config-level exposure control[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#config-level-exposure-control "Config-level exposure control的直接链接")
The new filtering support is also a security control:
  * disable dangerous tools you do not want the model to see
  * expose only a minimal whitelist for a sensitive server
  * disable resource/prompt wrappers when you do not want that surface exposed


## Example use cases[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#example-use-cases "Example use cases的直接链接")
### GitHub server with a minimal issue-management surface[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#github-server-with-a-minimal-issue-management-surface "GitHub server with a minimal issue-management surface的直接链接")

```
mcp_servers:github:command:"npx"args:["-y","@modelcontextprotocol/server-github"]env:GITHUB_PERSONAL_ACCESS_TOKEN:"***"tools:include:[list_issues, create_issue, update_issue]prompts:falseresources:false
```

Use it like:

```
Show me open issues labeled bug, then draft a new issue for the flaky MCP reconnection behavior.
```

### Stripe server with dangerous actions removed[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#stripe-server-with-dangerous-actions-removed "Stripe server with dangerous actions removed的直接链接")

```
mcp_servers:stripe:url:"https://mcp.stripe.com"headers:Authorization:"Bearer ***"tools:exclude:[delete_customer, refund_payment]
```

Use it like:

```
Look up the last 10 failed payments and summarize common failure reasons.
```

### Filesystem server for a single project root[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#filesystem-server-for-a-single-project-root "Filesystem server for a single project root的直接链接")

```
mcp_servers:project_fs:command:"npx"args:["-y","@modelcontextprotocol/server-filesystem","/home/user/my-project"]
```

Use it like:

```
Inspect the project root and explain the directory layout.
```

## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#troubleshooting "Troubleshooting的直接链接")
### MCP server not connecting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#mcp-server-not-connecting "MCP server not connecting的直接链接")
Check:

```
# Verify MCP deps are installed (already included in standard install)cd ~/.hermes/hermes-agent && uv pip install-e".[mcp]"node--versionnpx --version
```

Then verify your config and restart Hermes.
### Tools not appearing[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#tools-not-appearing "Tools not appearing的直接链接")
Possible causes:
  * the server failed to connect
  * discovery failed
  * your filter config excluded the tools
  * the utility capability does not exist on that server
  * the server is disabled with `enabled: false`


If you are intentionally filtering, this is expected.
### Why didn't resource or prompt utilities appear?[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#why-didnt-resource-or-prompt-utilities-appear "Why didn't resource or prompt utilities appear?的直接链接")
Because Hermes now only registers those wrappers when both are true:
  1. your config allows them
  2. the server session actually supports the capability


This is intentional and keeps the tool list honest.
## MCP Sampling Support[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#mcp-sampling-support "MCP Sampling Support的直接链接")
MCP servers can request LLM inference from Hermes via the `sampling/createMessage` protocol. This allows an MCP server to ask Hermes to generate text on its behalf — useful for servers that need LLM capabilities but don't have their own model access.
Sampling is **enabled by default** for all MCP servers (when the MCP SDK supports it). Configure it per-server under the `sampling` key:

```
mcp_servers:my_server:command:"my-mcp-server"sampling:enabled:true# Enable sampling (default: true)model:"openai/gpt-4o"# Override model for sampling requests (optional)max_tokens_cap:4096# Max tokens per sampling response (default: 4096)timeout:30# Timeout in seconds per request (default: 30)max_rpm:10# Rate limit: max requests per minute (default: 10)max_tool_rounds:5# Max tool-use rounds in sampling loops (default: 5)allowed_models:[]# Allowlist of model names the server may request (empty = any)log_level:"info"# Audit log level: debug, info, or warning (default: info)
```

The sampling handler includes a sliding-window rate limiter, per-request timeouts, and tool-loop depth limits to prevent runaway usage. Metrics (request count, errors, tokens used) are tracked per server instance.
To disable sampling for a specific server:

```
mcp_servers:untrusted_server:url:"https://mcp.example.com"sampling:enabled:false
```

## Running Hermes as an MCP server[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#running-hermes-as-an-mcp-server "Running Hermes as an MCP server的直接链接")
In addition to connecting **to** MCP servers, Hermes can also **be** an MCP server. This lets other MCP-capable agents (Claude Code, Cursor, Codex, or any MCP client) use Hermes's messaging capabilities — list conversations, read message history, and send messages across all your connected platforms.
### When to use this[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#when-to-use-this "When to use this的直接链接")
  * You want Claude Code, Cursor, or another coding agent to send and read Telegram/Discord/Slack messages through Hermes
  * You want a single MCP server that bridges to all of Hermes's connected messaging platforms at once
  * You already have a running Hermes gateway with connected platforms


### Quick start[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#quick-start-1 "Quick start的直接链接")

```
hermes mcp serve
```

This starts a stdio MCP server. The MCP client (not you) manages the process lifecycle.
### MCP client configuration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#mcp-client-configuration "MCP client configuration的直接链接")
Add Hermes to your MCP client config. For example, in Claude Code's `~/.claude/claude_desktop_config.json`:

```
"mcpServers":{"hermes":{"command":"hermes","args":["mcp","serve"]
```

Or if you installed Hermes in a specific location:

```
"mcpServers":{"hermes":{"command":"/home/user/.hermes/hermes-agent/venv/bin/hermes","args":["mcp","serve"]
```

### Available tools[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#available-tools "Available tools的直接链接")
The MCP server exposes 10 tools, matching OpenClaw's channel bridge surface plus a Hermes-specific channel browser:  
| Tool  | Description  |  
| --- | --- |  
| `conversations_list`  | List active messaging conversations. Filter by platform or search by name.  |  
| `conversation_get`  | Get detailed info about one conversation by session key.  |  
| `messages_read`  | Read recent message history for a conversation.  |  
| `attachments_fetch`  | Extract non-text attachments (images, media) from a specific message.  |  
| `events_poll`  | Poll for new conversation events since a cursor position.  |  
| `events_wait`  | Long-poll / block until the next event arrives (near-real-time).  |  
| `messages_send`  | Send a message through a platform (e.g. `telegram:123456`, `discord:#general`).  |  
| `channels_list`  | List available messaging targets across all platforms.  |  
| `permissions_list_open`  | List pending approval requests observed during this bridge session.  |  
| `permissions_respond`  | Allow or deny a pending approval request.  |  
### Event system[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#event-system "Event system的直接链接")
The MCP server includes a live event bridge that polls Hermes's session database for new messages. This gives MCP clients near-real-time awareness of incoming conversations:

```
# Poll for new events (non-blocking)events_poll(after_cursor=0)# Wait for next event (blocks up to timeout)events_wait(after_cursor=42, timeout_ms=30000)
```

Event types: `message`, `approval_requested`, `approval_resolved`
The event queue is in-memory and starts when the bridge connects. Older messages are available through `messages_read`.
### Options[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#options "Options的直接链接")

```
hermes mcp serve              # Normal modehermes mcp serve --verbose# Debug logging on stderr
```

### How it works[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#how-it-works "How it works的直接链接")
The MCP server reads conversation data directly from Hermes's session store (`~/.hermes/sessions/sessions.json` and the SQLite database). A background thread polls the database for new messages and maintains an in-memory event queue. For sending messages, it uses the same `send_message` infrastructure as the Hermes agent itself.
The gateway does NOT need to be running for read operations (listing conversations, reading history, polling events). It DOES need to be running for send operations, since the platform adapters need active connections.
### Current limits[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#current-limits "Current limits的直接链接")
  * Stdio transport only (no HTTP MCP transport yet)
  * Event polling at ~200ms intervals via mtime-optimized DB polling (skips work when files are unchanged)
  * No `claude/channel` push notification protocol yet
  * Text-only sends (no media/attachment sending through `messages_send`)


## Related docs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#related-docs "Related docs的直接链接")
  * [Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/use-mcp-with-hermes)
  * [CLI Commands](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/reference/cli-commands)
  * [Slash Commands](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/reference/slash-commands)


  * [What MCP gives you](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#what-mcp-gives-you)
  * [Quick start](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#quick-start)
  * [Two kinds of MCP servers](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#two-kinds-of-mcp-servers)
    * [Stdio servers](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#stdio-servers)
    * [HTTP servers](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#http-servers)
  * [Basic configuration reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#basic-configuration-reference)
    * [Common keys](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#common-keys)
    * [Minimal stdio example](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#minimal-stdio-example)
    * [Minimal HTTP example](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#minimal-http-example)
  * [How Hermes registers MCP tools](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#how-hermes-registers-mcp-tools)
  * [MCP utility tools](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#mcp-utility-tools)
  * [Per-server filtering](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#per-server-filtering)
    * [Disable a server entirely](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#disable-a-server-entirely)
    * [Whitelist server tools](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#whitelist-server-tools)
    * [Blacklist server tools](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#blacklist-server-tools)
    * [Precedence rule](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#precedence-rule)
    * [Filter utility tools too](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#filter-utility-tools-too)
    * [Full example](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#full-example)
  * [What happens if everything is filtered out?](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#what-happens-if-everything-is-filtered-out)
  * [Runtime behavior](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#runtime-behavior)
    * [Discovery time](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#discovery-time)
    * [Dynamic Tool Discovery](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#dynamic-tool-discovery)
  * [Security model](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#security-model)
    * [Stdio env filtering](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#stdio-env-filtering)
    * [Config-level exposure control](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#config-level-exposure-control)
  * [Example use cases](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#example-use-cases)
    * [GitHub server with a minimal issue-management surface](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#github-server-with-a-minimal-issue-management-surface)
    * [Stripe server with dangerous actions removed](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#stripe-server-with-dangerous-actions-removed)
    * [Filesystem server for a single project root](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#filesystem-server-for-a-single-project-root)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#troubleshooting)
    * [MCP server not connecting](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#mcp-server-not-connecting)
    * [Tools not appearing](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#tools-not-appearing)
    * [Why didn't resource or prompt utilities appear?](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#why-didnt-resource-or-prompt-utilities-appear)
  * [MCP Sampling Support](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#mcp-sampling-support)
  * [Running Hermes as an MCP server](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#running-hermes-as-an-mcp-server)
    * [When to use this](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#when-to-use-this)
    * [MCP client configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#mcp-client-configuration)
    * [Available tools](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#available-tools)
    * [Event system](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#event-system)
    * [How it works](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#how-it-works)
    * [Current limits](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#current-limits)
  * [Related docs](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/mcp#related-docs)


