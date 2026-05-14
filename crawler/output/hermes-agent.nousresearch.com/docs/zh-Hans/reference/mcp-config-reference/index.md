<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference -->

本页总览
This page is the compact reference companion to the main MCP docs.
For conceptual guidance, see:
  * [MCP (Model Context Protocol)](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/mcp)
  * [Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/use-mcp-with-hermes)


## Root config shape[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#root-config-shape "Root config shape的直接链接")

```
mcp_servers:<server_name>:command:"..."# stdio serversargs:[]env:{}# ORurl:"..."# HTTP serversheaders:{}enabled:truetimeout:120connect_timeout:60tools:include:[]exclude:[]resources:trueprompts:true
```

## Server keys[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#server-keys "Server keys的直接链接")  
| Key  | Type  | Applies to  | Meaning  |  
| --- | --- | --- | --- |  
| `command`  | string  | stdio  | Executable to launch  |  
| `args`  | list  | stdio  | Arguments for the subprocess  |  
| `env`  | mapping  | stdio  | Environment passed to the subprocess  |  
| `url`  | string  | HTTP  | Remote MCP endpoint  |  
| `headers`  | mapping  | HTTP  | Headers for remote server requests  |  
| `enabled`  | bool  | both  | Skip the server entirely when false  |  
| `timeout`  | number  | both  | Tool call timeout  |  
| `connect_timeout`  | number  | both  | Initial connection timeout  |  
| `tools`  | mapping  | both  | Filtering and utility-tool policy  |  
| `auth`  | string  | HTTP  | Authentication method. Set to `oauth` to enable OAuth 2.1 with PKCE  |  
| `sampling`  | mapping  | both  | Server-initiated LLM request policy (see MCP guide)  |  
##  `tools` policy keys[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#tools-policy-keys "tools-policy-keys的直接链接")  
| Key  | Type  | Meaning  |  
| --- | --- | --- |  
| `include`  | string or list  | Whitelist server-native MCP tools  |  
| `exclude`  | string or list  | Blacklist server-native MCP tools  |  
| `resources`  | bool-like  | Enable/disable `list_resources` + `read_resource`  |  
| `prompts`  | bool-like  | Enable/disable `list_prompts` + `get_prompt`  |  
## Filtering semantics[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#filtering-semantics "Filtering semantics的直接链接")
###  `include`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#include "include的直接链接")
If `include` is set, only those server-native MCP tools are registered.

```
tools:include:[create_issue, list_issues]
```

###  `exclude`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#exclude "exclude的直接链接")
If `exclude` is set and `include` is not, every server-native MCP tool except those names is registered.

```
tools:exclude:[delete_customer]
```

### Precedence[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#precedence "Precedence的直接链接")
If both are set, `include` wins.

```
tools:include:[create_issue]exclude:[create_issue, delete_issue]
```

Result:
  * `create_issue` is still allowed
  * `delete_issue` is ignored because `include` takes precedence


## Utility-tool policy[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#utility-tool-policy "Utility-tool policy的直接链接")
Hermes may register these utility wrappers per MCP server:
Resources:
  * `list_resources`
  * `read_resource`


Prompts:
  * `list_prompts`
  * `get_prompt`


### Disable resources[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#disable-resources "Disable resources的直接链接")

```
tools:resources:false
```

### Disable prompts[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#disable-prompts "Disable prompts的直接链接")

```
tools:prompts:false
```

### Capability-aware registration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#capability-aware-registration "Capability-aware registration的直接链接")
Even when `resources: true` or `prompts: true`, Hermes only registers those utility tools if the MCP session actually exposes the corresponding capability.
So this is normal:
  * you enable prompts
  * but no prompt utilities appear
  * because the server does not support prompts


##  `enabled: false`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#enabled-false "enabled-false的直接链接")

```
mcp_servers:legacy:url:"https://mcp.legacy.internal"enabled:false
```

Behavior:
  * no connection attempt
  * no discovery
  * no tool registration
  * config remains in place for later reuse


## Empty result behavior[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#empty-result-behavior "Empty result behavior的直接链接")
If filtering removes all server-native tools and no utility tools are registered, Hermes does not create an empty MCP runtime toolset for that server.
## Example configs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#example-configs "Example configs的直接链接")
### Safe GitHub allowlist[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#safe-github-allowlist "Safe GitHub allowlist的直接链接")

```
mcp_servers:github:command:"npx"args:["-y","@modelcontextprotocol/server-github"]env:GITHUB_PERSONAL_ACCESS_TOKEN:"***"tools:include:[list_issues, create_issue, update_issue, search_code]resources:falseprompts:false
```

### Stripe blacklist[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#stripe-blacklist "Stripe blacklist的直接链接")

```
mcp_servers:stripe:url:"https://mcp.stripe.com"headers:Authorization:"Bearer ***"tools:exclude:[delete_customer, refund_payment]
```

### Resource-only docs server[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#resource-only-docs-server "Resource-only docs server的直接链接")

```
mcp_servers:docs:url:"https://mcp.docs.example.com"tools:include:[]resources:trueprompts:false
```

## Reloading config[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#reloading-config "Reloading config的直接链接")
After changing MCP config, reload servers with:

```
/reload-mcp
```

## Tool naming[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#tool-naming "Tool naming的直接链接")
Server-native MCP tools become:

```
mcp_<server>_<tool>
```

Examples:
  * `mcp_github_create_issue`
  * `mcp_filesystem_read_file`
  * `mcp_my_api_query_data`


Utility tools follow the same prefixing pattern:
  * `mcp_<server>_list_resources`
  * `mcp_<server>_read_resource`
  * `mcp_<server>_list_prompts`
  * `mcp_<server>_get_prompt`


### Name sanitization[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#name-sanitization "Name sanitization的直接链接")
Hyphens (`-`) and dots (`.`) in both server names and tool names are replaced with underscores before registration. This ensures tool names are valid identifiers for LLM function-calling APIs.
For example, a server named `my-api` exposing a tool called `list-items.v2` becomes:

```
mcp_my_api_list_items_v2
```

Keep this in mind when writing `include` / `exclude` filters — use the **original** MCP tool name (with hyphens/dots), not the sanitized version.
## OAuth 2.1 authentication[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#oauth-21-authentication "OAuth 2.1 authentication的直接链接")
For HTTP servers that require OAuth, set `auth: oauth` on the server entry:

```
mcp_servers:protected_api:url:"https://mcp.example.com/mcp"auth: oauth
```

Behavior:
  * Hermes uses the MCP SDK's OAuth 2.1 PKCE flow (metadata discovery, dynamic client registration, token exchange, and refresh)
  * On first connect, a browser window opens for authorization
  * Tokens are persisted to `~/.hermes/mcp-tokens/<server>.json` and reused across sessions
  * Token refresh is automatic; re-authorization only happens when refresh fails
  * Only applies to HTTP/StreamableHTTP transport (`url`-based servers)


  * [Root config shape](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#root-config-shape)
  * [Server keys](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#server-keys)
  * [`tools` policy keys](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#tools-policy-keys)
  * [Filtering semantics](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#filtering-semantics)
  * [Utility-tool policy](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#utility-tool-policy)
    * [Disable resources](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#disable-resources)
    * [Disable prompts](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#disable-prompts)
    * [Capability-aware registration](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#capability-aware-registration)
  * [`enabled: false`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#enabled-false)
  * [Empty result behavior](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#empty-result-behavior)
  * [Example configs](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#example-configs)
    * [Safe GitHub allowlist](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#safe-github-allowlist)
    * [Stripe blacklist](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#stripe-blacklist)
    * [Resource-only docs server](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#resource-only-docs-server)
  * [Reloading config](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#reloading-config)
  * [Tool naming](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#tool-naming)
    * [Name sanitization](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#name-sanitization)
  * [OAuth 2.1 authentication](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/mcp-config-reference#oauth-21-authentication)


