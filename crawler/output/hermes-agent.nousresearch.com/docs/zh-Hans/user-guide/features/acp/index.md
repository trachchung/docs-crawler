<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp -->

本页总览
Hermes Agent can run as an ACP server, letting ACP-compatible editors talk to Hermes over stdio and render:
  * chat messages
  * tool activity
  * file diffs
  * terminal commands
  * approval prompts
  * streamed thinking / response chunks


ACP is a good fit when you want Hermes to behave like an editor-native coding agent instead of a standalone CLI or messaging bot.
## What Hermes exposes in ACP mode[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#what-hermes-exposes-in-acp-mode "What Hermes exposes in ACP mode的直接链接")
Hermes runs with a curated `hermes-acp` toolset designed for editor workflows. It includes:
  * file tools: `read_file`, `write_file`, `patch`, `search_files`
  * terminal tools: `terminal`, `process`
  * web/browser tools
  * memory, todo, session search
  * skills
  * execute_code and delegate_task
  * vision


It intentionally excludes things that do not fit typical editor UX, such as messaging delivery and cronjob management.
## Installation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#installation "Installation的直接链接")
Install Hermes normally, then add the ACP extra:

```
pip install-e'.[acp]'
```

This installs the `agent-client-protocol` dependency and enables:
  * `hermes acp`
  * `hermes-acp`
  * `python -m acp_adapter`


## Launching the ACP server[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#launching-the-acp-server "Launching the ACP server的直接链接")
Any of the following starts Hermes in ACP mode:

```
hermes acp
```


```
hermes-acp
```


```
python -m acp_adapter
```

Hermes logs to stderr so stdout remains reserved for ACP JSON-RPC traffic.
## Editor setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#editor-setup "Editor setup的直接链接")
### VS Code[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#vs-code "VS Code的直接链接")
Install the [ACP Client](https://marketplace.visualstudio.com/items?itemName=formulahendry.acp-client) extension.
To connect:
  1. Open the ACP Client panel from the Activity Bar.
  2. Select **Hermes Agent** from the built-in agent list.
  3. Connect and start chatting.


If you want to define Hermes manually, add it through VS Code settings under `acp.agents`:

```
"acp.agents":{"Hermes Agent":{"command":"hermes","args":["acp"]
```

### Zed[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#zed "Zed的直接链接")
Example settings snippet:

```
"agent_servers":{"hermes-agent":{"type":"custom","command":"hermes","args":["acp"],
```

### JetBrains[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#jetbrains "JetBrains的直接链接")
Use an ACP-compatible plugin and point it at:

```
/path/to/hermes-agent/acp_registry
```

## Registry manifest[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#registry-manifest "Registry manifest的直接链接")
The ACP registry manifest lives at:

```
acp_registry/agent.json
```

It advertises a command-based agent whose launch command is:

```
hermes acp
```

## Configuration and credentials[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#configuration-and-credentials "Configuration and credentials的直接链接")
ACP mode uses the same Hermes configuration as the CLI:
  * `~/.hermes/.env`
  * `~/.hermes/config.yaml`
  * `~/.hermes/skills/`
  * `~/.hermes/state.db`


Provider resolution uses Hermes' normal runtime resolver, so ACP inherits the currently configured provider and credentials.
## Session behavior[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#session-behavior "Session behavior的直接链接")
ACP sessions are tracked by the ACP adapter's in-memory session manager while the server is running.
Each session stores:
  * session ID
  * working directory
  * selected model
  * current conversation history
  * cancel event


The underlying `AIAgent` still uses Hermes' normal persistence/logging paths, but ACP `list/load/resume/fork` are scoped to the currently running ACP server process.
## Working directory behavior[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#working-directory-behavior "Working directory behavior的直接链接")
ACP sessions bind the editor's cwd to the Hermes task ID so file and terminal tools run relative to the editor workspace, not the server process cwd.
## Approvals[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#approvals "Approvals的直接链接")
Dangerous terminal commands can be routed back to the editor as approval prompts. ACP approval options are simpler than the CLI flow:
  * allow once
  * allow always
  * deny


On timeout or error, the approval bridge denies the request.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#troubleshooting "Troubleshooting的直接链接")
### ACP agent does not appear in the editor[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#acp-agent-does-not-appear-in-the-editor "ACP agent does not appear in the editor的直接链接")
Check:
  * the editor is pointed at the correct `acp_registry/` path
  * Hermes is installed and on your PATH
  * the ACP extra is installed (`pip install -e '.[acp]'`)


### ACP starts but immediately errors[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#acp-starts-but-immediately-errors "ACP starts but immediately errors的直接链接")
Try these checks:

```
hermes doctorhermes statushermes acp
```

### Missing credentials[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#missing-credentials "Missing credentials的直接链接")
ACP mode does not have its own login flow. It uses Hermes' existing provider setup. Configure credentials with:

```
hermes model
```

or by editing `~/.hermes/.env`.
## See also[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#see-also "See also的直接链接")
  * [ACP Internals](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/acp-internals)
  * [Provider Runtime Resolution](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/provider-runtime)
  * [Tools Runtime](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/tools-runtime)


  * [What Hermes exposes in ACP mode](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#what-hermes-exposes-in-acp-mode)
  * [Installation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#installation)
  * [Launching the ACP server](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#launching-the-acp-server)
  * [Editor setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#editor-setup)
  * [Registry manifest](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#registry-manifest)
  * [Configuration and credentials](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#configuration-and-credentials)
  * [Session behavior](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#session-behavior)
  * [Working directory behavior](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#working-directory-behavior)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#troubleshooting)
    * [ACP agent does not appear in the editor](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#acp-agent-does-not-appear-in-the-editor)
    * [ACP starts but immediately errors](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#acp-starts-but-immediately-errors)
    * [Missing credentials](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/acp#missing-credentials)


