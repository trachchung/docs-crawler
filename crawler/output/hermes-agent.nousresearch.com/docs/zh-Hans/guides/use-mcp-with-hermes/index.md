<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes -->

本页总览
This guide shows how to actually use MCP with Hermes Agent in day-to-day workflows.
If the feature page explains what MCP is, this guide is about how to get value from it quickly and safely.
## When should you use MCP?[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#when-should-you-use-mcp "When should you use MCP?的直接链接")
Use MCP when:
  * a tool already exists in MCP form and you do not want to build a native Hermes tool
  * you want Hermes to operate against a local or remote system through a clean RPC layer
  * you want fine-grained per-server exposure control
  * you want to connect Hermes to internal APIs, databases, or company systems without modifying Hermes core


Do not use MCP when:
  * a built-in Hermes tool already solves the job well
  * the server exposes a huge dangerous tool surface and you are not prepared to filter it
  * you only need one very narrow integration and a native tool would be simpler and safer


## Mental model[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#mental-model "Mental model的直接链接")
Think of MCP as an adapter layer:
  * Hermes remains the agent
  * MCP servers contribute tools
  * Hermes discovers those tools at startup or reload time
  * the model can use them like normal tools
  * you control how much of each server is visible


That last part matters. Good MCP usage is not just “connect everything.” It is “connect the right thing, with the smallest useful surface.”
## Step 1: install MCP support[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#step-1-install-mcp-support "Step 1: install MCP support的直接链接")
If you installed Hermes with the standard install script, MCP support is already included (the installer runs `uv pip install -e ".[all]"`).
If you installed without extras and need to add MCP separately:

```
cd ~/.hermes/hermes-agentuv pip install-e".[mcp]"
```

For npm-based servers, make sure Node.js and `npx` are available.
For many Python MCP servers, `uvx` is a nice default.
## Step 2: add one server first[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#step-2-add-one-server-first "Step 2: add one server first的直接链接")
Start with a single, safe server.
Example: filesystem access to one project directory only.

```
mcp_servers:project_fs:command:"npx"args:["-y","@modelcontextprotocol/server-filesystem","/home/user/my-project"]
```

Then start Hermes:

```
hermes chat
```

Now ask something concrete:

```
Inspect this project and summarize the repo layout.
```

## Step 3: verify MCP loaded[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#step-3-verify-mcp-loaded "Step 3: verify MCP loaded的直接链接")
You can verify MCP in a few ways:
  * Hermes banner/status should show MCP integration when configured
  * ask Hermes what tools it has available
  * use `/reload-mcp` after config changes
  * check logs if the server failed to connect


A practical test prompt:

```
Tell me which MCP-backed tools are available right now.
```

## Step 4: start filtering immediately[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#step-4-start-filtering-immediately "Step 4: start filtering immediately的直接链接")
Do not wait until later if the server exposes a lot of tools.
### Example: whitelist only what you want[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#example-whitelist-only-what-you-want "Example: whitelist only what you want的直接链接")

```
mcp_servers:github:command:"npx"args:["-y","@modelcontextprotocol/server-github"]env:GITHUB_PERSONAL_ACCESS_TOKEN:"***"tools:include:[list_issues, create_issue, search_code]
```

This is usually the best default for sensitive systems.
## WSL2: bridge Hermes in WSL to Windows Chrome[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#wsl2-bridge-hermes-in-wsl-to-windows-chrome "WSL2: bridge Hermes in WSL to Windows Chrome的直接链接")
This is the practical setup when:
  * Hermes runs inside WSL2
  * the browser you want to control is your normal signed-in Chrome on Windows
  * `/browser connect` is awkward or unreliable from WSL


In this setup, Hermes does **not** connect to Chrome directly. Instead:
  * Hermes runs in WSL
  * Hermes starts a local stdio MCP server
  * that MCP server is launched through Windows interop (`cmd.exe` or `powershell.exe`)
  * the MCP server attaches to your live Windows Chrome session


Mental model:

```
Hermes (WSL) -> MCP stdio bridge -> Windows Chrome
```

### Why this mode is useful[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#why-this-mode-is-useful "Why this mode is useful的直接链接")
  * you keep your real Windows browser profile, cookies, and logins
  * Hermes stays in its supported Unix environment (WSL2)
  * browser control is exposed as MCP tools instead of relying on Hermes core browser transport


### Recommended server[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#recommended-server "Recommended server的直接链接")
Use `chrome-devtools-mcp`.
If your Windows Chrome already has live remote debugging enabled from `chrome://inspect/#remote-debugging`, add it like this from WSL:

```
hermes mcp add chrome-devtools-win --command cmd.exe --args /c npx -y chrome-devtools-mcp@latest --autoConnect --no-usage-statistics
```

After saving the server:

```
hermes mcp test chrome-devtools-win
```

Then start a fresh Hermes session or run:

```
/reload-mcp
```

### Typical prompt[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#typical-prompt "Typical prompt的直接链接")
Once loaded, Hermes can use the MCP-prefixed browser tools directly. For example:

```
调用 MCP 工具 mcp_chrome_devtools_win_list_pages，列出当前浏览器标签页。
```

### When `/browser connect` is the wrong tool[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#when-browser-connect-is-the-wrong-tool "when-browser-connect-is-the-wrong-tool的直接链接")
If Hermes runs in WSL and Chrome runs on Windows, `/browser connect` may fail even though Chrome is open and debuggable.
Common reasons:
  * WSL cannot reach the same host-local endpoint Chrome exposes to Windows tools
  * newer Chrome live-debugging flows are not the same as a classic `ws://localhost:9222`
  * the browser is easier to attach to from a Windows-side helper like `chrome-devtools-mcp`


In those cases, keep `/browser connect` for same-environment setups and use MCP for WSL-to-Windows browser bridging.
### Known pitfalls[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#known-pitfalls "Known pitfalls的直接链接")
  * Start Hermes from a Windows-mounted path like `/mnt/c/Users/<you>` or `/mnt/c/workspace/...` when using Windows stdio executables through MCP.
  * If you start Hermes from `/root` or `/home/...`, Windows may emit a `UNC` current-directory warning before the MCP server starts.
  * If `chrome-devtools-mcp --autoConnect` times out while enumerating pages, reduce background/frozen tabs in Chrome and retry.


### Example: blacklist dangerous actions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#example-blacklist-dangerous-actions "Example: blacklist dangerous actions的直接链接")

```
mcp_servers:stripe:url:"https://mcp.stripe.com"headers:Authorization:"Bearer ***"tools:exclude:[delete_customer, refund_payment]
```

### Example: disable utility wrappers too[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#example-disable-utility-wrappers-too "Example: disable utility wrappers too的直接链接")

```
mcp_servers:docs:url:"https://mcp.docs.example.com"tools:prompts:falseresources:false
```

## What does filtering actually affect?[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#what-does-filtering-actually-affect "What does filtering actually affect?的直接链接")
There are two categories of MCP-exposed functionality in Hermes:
  1. Server-native MCP tools


  * filtered with: 
    * `tools.include`
    * `tools.exclude`


  1. Hermes-added utility wrappers


  * filtered with: 
    * `tools.resources`
    * `tools.prompts`


### Utility wrappers you may see[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#utility-wrappers-you-may-see "Utility wrappers you may see的直接链接")
Resources:
  * `list_resources`
  * `read_resource`


Prompts:
  * `list_prompts`
  * `get_prompt`


These wrappers only appear if:
  * your config allows them, and
  * the MCP server session actually supports those capabilities


So Hermes will not pretend a server has resources/prompts if it does not.
## Common patterns[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#common-patterns "Common patterns的直接链接")
### Pattern 1: local project assistant[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#pattern-1-local-project-assistant "Pattern 1: local project assistant的直接链接")
Use MCP for a repo-local filesystem or git server when you want Hermes to reason over a bounded workspace.

```
mcp_servers:fs:command:"npx"args:["-y","@modelcontextprotocol/server-filesystem","/home/user/project"]git:command:"uvx"args:["mcp-server-git","--repository","/home/user/project"]
```

Good prompts:

```
Review the project structure and identify where configuration lives.
```


```
Check the local git state and summarize what changed recently.
```

### Pattern 2: GitHub triage assistant[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#pattern-2-github-triage-assistant "Pattern 2: GitHub triage assistant的直接链接")

```
mcp_servers:github:command:"npx"args:["-y","@modelcontextprotocol/server-github"]env:GITHUB_PERSONAL_ACCESS_TOKEN:"***"tools:include:[list_issues, create_issue, update_issue, search_code]prompts:falseresources:false
```

Good prompts:

```
List open issues about MCP, cluster them by theme, and draft a high-quality issue for the most common bug.
```


```
Search the repo for uses of _discover_and_register_server and explain how MCP tools are registered.
```

### Pattern 3: internal API assistant[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#pattern-3-internal-api-assistant "Pattern 3: internal API assistant的直接链接")

```
mcp_servers:internal_api:url:"https://mcp.internal.example.com"headers:Authorization:"Bearer ***"tools:include:[list_customers, get_customer, list_invoices]resources:falseprompts:false
```

Good prompts:

```
Look up customer ACME Corp and summarize recent invoice activity.
```

This is the sort of place where a strict whitelist is far better than an exclude list.
### Pattern 4: documentation / knowledge servers[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#pattern-4-documentation--knowledge-servers "Pattern 4: documentation / knowledge servers的直接链接")
Some MCP servers expose prompts or resources that are more like shared knowledge assets than direct actions.

```
mcp_servers:docs:url:"https://mcp.docs.example.com"tools:prompts:trueresources:true
```

Good prompts:

```
List available MCP resources from the docs server, then read the onboarding guide and summarize it.
```


```
List prompts exposed by the docs server and tell me which ones would help with incident response.
```

## Tutorial: end-to-end setup with filtering[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#tutorial-end-to-end-setup-with-filtering "Tutorial: end-to-end setup with filtering的直接链接")
Here is a practical progression.
### Phase 1: add GitHub MCP with a tight whitelist[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#phase-1-add-github-mcp-with-a-tight-whitelist "Phase 1: add GitHub MCP with a tight whitelist的直接链接")

```
mcp_servers:github:command:"npx"args:["-y","@modelcontextprotocol/server-github"]env:GITHUB_PERSONAL_ACCESS_TOKEN:"***"tools:include:[list_issues, create_issue, search_code]prompts:falseresources:false
```

Start Hermes and ask:

```
Search the codebase for references to MCP and summarize the main integration points.
```

### Phase 2: expand only when needed[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#phase-2-expand-only-when-needed "Phase 2: expand only when needed的直接链接")
If you later need issue updates too:

```
tools:include:[list_issues, create_issue, update_issue, search_code]
```

Then reload:

```
/reload-mcp
```

### Phase 3: add a second server with different policy[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#phase-3-add-a-second-server-with-different-policy "Phase 3: add a second server with different policy的直接链接")

```
mcp_servers:github:command:"npx"args:["-y","@modelcontextprotocol/server-github"]env:GITHUB_PERSONAL_ACCESS_TOKEN:"***"tools:include:[list_issues, create_issue, update_issue, search_code]prompts:falseresources:falsefilesystem:command:"npx"args:["-y","@modelcontextprotocol/server-filesystem","/home/user/project"]
```

Now Hermes can combine them:

```
Inspect the local project files, then create a GitHub issue summarizing the bug you find.
```

That is where MCP gets powerful: multi-system workflows without changing Hermes core.
## Safe usage recommendations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#safe-usage-recommendations "Safe usage recommendations的直接链接")
### Prefer allowlists for dangerous systems[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#prefer-allowlists-for-dangerous-systems "Prefer allowlists for dangerous systems的直接链接")
For anything financial, customer-facing, or destructive:
  * use `tools.include`
  * start with the smallest set possible


### Disable unused utilities[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#disable-unused-utilities "Disable unused utilities的直接链接")
If you do not want the model browsing server-provided resources/prompts, turn them off:

```
tools:resources:falseprompts:false
```

### Keep servers scoped narrowly[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#keep-servers-scoped-narrowly "Keep servers scoped narrowly的直接链接")
Examples:
  * filesystem server rooted to one project dir, not your whole home directory
  * git server pointed at one repo
  * internal API server with read-heavy tool exposure by default


### Reload after config changes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#reload-after-config-changes "Reload after config changes的直接链接")

```
/reload-mcp
```

Do this after changing:
  * include/exclude lists
  * enabled flags
  * resources/prompts toggles
  * auth headers / env


## Troubleshooting by symptom[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#troubleshooting-by-symptom "Troubleshooting by symptom的直接链接")
### "The server connects but the tools I expected are missing"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#the-server-connects-but-the-tools-i-expected-are-missing ""The server connects but the tools I expected are missing"的直接链接")
Possible causes:
  * filtered by `tools.include`
  * excluded by `tools.exclude`
  * utility wrappers disabled via `resources: false` or `prompts: false`
  * server does not actually support resources/prompts


### "The server is configured but nothing loads"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#the-server-is-configured-but-nothing-loads ""The server is configured but nothing loads"的直接链接")
Check:
  * `enabled: false` was not left in config
  * command/runtime exists (`npx`, `uvx`, etc.)
  * HTTP endpoint is reachable
  * auth env or headers are correct


### "Why do I see fewer tools than the MCP server advertises?"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#why-do-i-see-fewer-tools-than-the-mcp-server-advertises ""Why do I see fewer tools than the MCP server advertises?"的直接链接")
Because Hermes now respects your per-server policy and capability-aware registration. That is expected, and usually desirable.
### "How do I remove an MCP server without deleting the config?"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#how-do-i-remove-an-mcp-server-without-deleting-the-config ""How do I remove an MCP server without deleting the config?"的直接链接")
Use:

```
enabled:false
```

That keeps the config around but prevents connection and registration.
## Recommended first MCP setups[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#recommended-first-mcp-setups "Recommended first MCP setups的直接链接")
Good first servers for most users:
  * filesystem
  * git
  * GitHub
  * fetch / documentation MCP servers
  * one narrow internal API


Not-great first servers:
  * giant business systems with lots of destructive actions and no filtering
  * anything you do not understand well enough to constrain


## Related docs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#related-docs "Related docs的直接链接")
  * [MCP (Model Context Protocol)](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/mcp)
  * [Slash Commands](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/reference/slash-commands)


  * [When should you use MCP?](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#when-should-you-use-mcp)
  * [Mental model](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#mental-model)
  * [Step 1: install MCP support](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#step-1-install-mcp-support)
  * [Step 2: add one server first](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#step-2-add-one-server-first)
  * [Step 3: verify MCP loaded](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#step-3-verify-mcp-loaded)
  * [Step 4: start filtering immediately](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#step-4-start-filtering-immediately)
    * [Example: whitelist only what you want](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#example-whitelist-only-what-you-want)
  * [WSL2: bridge Hermes in WSL to Windows Chrome](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#wsl2-bridge-hermes-in-wsl-to-windows-chrome)
    * [Why this mode is useful](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#why-this-mode-is-useful)
    * [Recommended server](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#recommended-server)
    * [Typical prompt](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#typical-prompt)
    * [When `/browser connect` is the wrong tool](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#when-browser-connect-is-the-wrong-tool)
    * [Known pitfalls](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#known-pitfalls)
    * [Example: blacklist dangerous actions](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#example-blacklist-dangerous-actions)
    * [Example: disable utility wrappers too](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#example-disable-utility-wrappers-too)
  * [What does filtering actually affect?](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#what-does-filtering-actually-affect)
    * [Utility wrappers you may see](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#utility-wrappers-you-may-see)
  * [Common patterns](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#common-patterns)
    * [Pattern 1: local project assistant](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#pattern-1-local-project-assistant)
    * [Pattern 2: GitHub triage assistant](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#pattern-2-github-triage-assistant)
    * [Pattern 3: internal API assistant](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#pattern-3-internal-api-assistant)
    * [Pattern 4: documentation / knowledge servers](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#pattern-4-documentation--knowledge-servers)
  * [Tutorial: end-to-end setup with filtering](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#tutorial-end-to-end-setup-with-filtering)
    * [Phase 1: add GitHub MCP with a tight whitelist](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#phase-1-add-github-mcp-with-a-tight-whitelist)
    * [Phase 2: expand only when needed](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#phase-2-expand-only-when-needed)
    * [Phase 3: add a second server with different policy](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#phase-3-add-a-second-server-with-different-policy)
  * [Safe usage recommendations](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#safe-usage-recommendations)
    * [Prefer allowlists for dangerous systems](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#prefer-allowlists-for-dangerous-systems)
    * [Disable unused utilities](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#disable-unused-utilities)
    * [Keep servers scoped narrowly](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#keep-servers-scoped-narrowly)
    * [Reload after config changes](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#reload-after-config-changes)
  * [Troubleshooting by symptom](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#troubleshooting-by-symptom)
    * ["The server connects but the tools I expected are missing"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#the-server-connects-but-the-tools-i-expected-are-missing)
    * ["The server is configured but nothing loads"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#the-server-is-configured-but-nothing-loads)
    * ["Why do I see fewer tools than the MCP server advertises?"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#why-do-i-see-fewer-tools-than-the-mcp-server-advertises)
    * ["How do I remove an MCP server without deleting the config?"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#how-do-i-remove-an-mcp-server-without-deleting-the-config)
  * [Recommended first MCP setups](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#recommended-first-mcp-setups)
  * [Related docs](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-mcp-with-hermes#related-docs)


