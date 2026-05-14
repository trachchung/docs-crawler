<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#__docusaurus_skipToContent_fallback)
On this page
The API server exposes hermes-agent as an OpenAI-compatible HTTP endpoint. Any frontend that speaks the OpenAI format — Open WebUI, LobeChat, LibreChat, NextChat, ChatBox, and hundreds more — can connect to hermes-agent and use it as a backend.
Your agent handles requests with its full toolset (terminal, file operations, web search, memory, skills) and returns the final response. When streaming, tool progress indicators appear inline so frontends can show what the agent is doing.
## Quick Start[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#quick-start "Direct link to Quick Start")
### 1. Enable the API server[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#1-enable-the-api-server "Direct link to 1. Enable the API server")
Add to `~/.hermes/.env`:

```
API_SERVER_ENABLED=trueAPI_SERVER_KEY=change-me-local-dev# Optional: only if a browser must call Hermes directly# API_SERVER_CORS_ORIGINS=http://localhost:3000
```

### 2. Start the gateway[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#2-start-the-gateway "Direct link to 2. Start the gateway")

```
hermes gateway
```

You'll see:

```
[API Server] API server listening on http://127.0.0.1:8642
```

### 3. Connect a frontend[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#3-connect-a-frontend "Direct link to 3. Connect a frontend")
Point any OpenAI-compatible client at `http://localhost:8642/v1`:

```
# Test with curlcurl http://localhost:8642/v1/chat/completions \-H"Authorization: Bearer change-me-local-dev"\-H"Content-Type: application/json"\-d'{"model": "hermes-agent", "messages": [{"role": "user", "content": "Hello!"}]}'
```

Or connect Open WebUI, LobeChat, or any other frontend — see the [Open WebUI integration guide](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/open-webui) for step-by-step instructions.
## Endpoints[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#endpoints "Direct link to Endpoints")
### POST /v1/chat/completions[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-v1chatcompletions "Direct link to POST /v1/chat/completions")
Standard OpenAI Chat Completions format. Stateless — the full conversation is included in each request via the `messages` array.
**Request:**

```
"model":"hermes-agent","messages":[{"role":"system","content":"You are a Python expert."},{"role":"user","content":"Write a fibonacci function"}"stream":false
```

**Response:**

```
"id":"chatcmpl-abc123","object":"chat.completion","created":1710000000,"model":"hermes-agent","choices":[{"index":0,"message":{"role":"assistant","content":"Here's a fibonacci function..."},"finish_reason":"stop"}],"usage":{"prompt_tokens":50,"completion_tokens":200,"total_tokens":250}
```

**Inline image input:** user messages may send `content` as an array of `text` and `image_url` parts. Both remote `http(s)` URLs and `data:image/...` URLs are supported:

```
"model":"hermes-agent","messages":["role":"user","content":[{"type":"text","text":"What is in this image?"},{"type":"image_url","image_url":{"url":"https://example.com/cat.png","detail":"high"}}
```

Uploaded files (`file` / `input_file` / `file_id`) and non-image `data:` URLs return `400 unsupported_content_type`.
**Streaming** (`"stream": true`): Returns Server-Sent Events (SSE) with token-by-token response chunks. For **Chat Completions** , the stream uses standard `chat.completion.chunk` events plus Hermes' custom `hermes.tool.progress` event for tool-start UX. For **Responses** , the stream uses OpenAI Responses event types such as `response.created`, `response.output_text.delta`, `response.output_item.added`, `response.output_item.done`, and `response.completed`.
**Tool progress in streams** :
  * **Chat Completions** : Hermes emits `event: hermes.tool.progress` for tool-start visibility without polluting persisted assistant text.
  * **Responses** : Hermes emits spec-native `function_call` and `function_call_output` output items during the SSE stream, so clients can render structured tool UI in real time.


### POST /v1/responses[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-v1responses "Direct link to POST /v1/responses")
OpenAI Responses API format. Supports server-side conversation state via `previous_response_id` — the server stores full conversation history (including tool calls and results) so multi-turn context is preserved without the client managing it.
**Request:**

```
"model":"hermes-agent","input":"What files are in my project?","instructions":"You are a helpful coding assistant.","store":true
```

**Response:**

```
"id":"resp_abc123","object":"response","status":"completed","model":"hermes-agent","output":[{"type":"function_call","name":"terminal","arguments":"{\"command\": \"ls\"}","call_id":"call_1"},{"type":"function_call_output","call_id":"call_1","output":"README.md src/ tests/"},{"type":"message","role":"assistant","content":[{"type":"output_text","text":"Your project has..."}]}"usage":{"input_tokens":50,"output_tokens":200,"total_tokens":250}
```

**Inline image input:** `input[].content` can contain `input_text` and `input_image` parts. Both remote URLs and `data:image/...` URLs are supported:

```
"model":"hermes-agent","input":["role":"user","content":[{"type":"input_text","text":"Describe this screenshot."},{"type":"input_image","image_url":"data:image/png;base64,iVBORw0K..."}
```

Uploaded files (`input_file` / `file_id`) and non-image `data:` URLs return `400 unsupported_content_type`.
#### Multi-turn with previous_response_id[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#multi-turn-with-previous_response_id "Direct link to Multi-turn with previous_response_id")
Chain responses to maintain full context (including tool calls) across turns:

```
"input":"Now show me the README","previous_response_id":"resp_abc123"
```

The server reconstructs the full conversation from the stored response chain — all previous tool calls and results are preserved. Chained requests also share the same session, so multi-turn conversations appear as a single entry in the dashboard and session history.
#### Named conversations[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#named-conversations "Direct link to Named conversations")
Use the `conversation` parameter instead of tracking response IDs:

```
{"input":"Hello","conversation":"my-project"}{"input":"What's in src/?","conversation":"my-project"}{"input":"Run the tests","conversation":"my-project"}
```

The server automatically chains to the latest response in that conversation. Like the `/title` command for gateway sessions.
### GET /v1/responses/{id}[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-v1responsesid "Direct link to GET /v1/responses/{id}")
Retrieve a previously stored response by ID.
### DELETE /v1/responses/{id}[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#delete-v1responsesid "Direct link to DELETE /v1/responses/{id}")
Delete a stored response.
### GET /v1/models[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-v1models "Direct link to GET /v1/models")
Lists the agent as an available model. The advertised model name defaults to the [profile](https://hermes-agent.nousresearch.com/docs/user-guide/profiles) name (or `hermes-agent` for the default profile). Required by most frontends for model discovery.
### GET /v1/capabilities[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-v1capabilities "Direct link to GET /v1/capabilities")
Returns a machine-readable description of the API server's stable surface for external UIs, orchestrators, and plugin bridges.

```
"object":"hermes.api_server.capabilities","platform":"hermes-agent","model":"hermes-agent","auth":{"type":"bearer","required":true},"features":{"chat_completions":true,"responses_api":true,"run_submission":true,"run_status":true,"run_events_sse":true,"run_stop":true
```

Use this endpoint when integrating dashboards, browser UIs, or control planes so they can discover whether the running Hermes version supports runs, streaming, cancellation, and session continuity without depending on private Python internals.
### GET /health[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-health "Direct link to GET /health")
Health check. Returns `{"status": "ok"}`. Also available at **GET /v1/health** for OpenAI-compatible clients that expect the `/v1/` prefix.
### GET /health/detailed[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-healthdetailed "Direct link to GET /health/detailed")
Extended health check that also reports active sessions, running agents, and resource usage. Useful for monitoring/observability tooling.
## Runs API (streaming-friendly alternative)[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#runs-api-streaming-friendly-alternative "Direct link to Runs API \(streaming-friendly alternative\)")
In addition to `/v1/chat/completions` and `/v1/responses`, the server exposes a **runs** API for long-form sessions where the client wants to subscribe to progress events instead of managing streaming themselves.
### POST /v1/runs[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-v1runs "Direct link to POST /v1/runs")
Create a new agent run. Returns a `run_id` that can be used to subscribe to progress events.

```
"run_id":"run_abc123","status":"started"
```

Runs accept a simple `input` string and optional `session_id`, `instructions`, `conversation_history`, or `previous_response_id`. When `session_id` is provided, Hermes surfaces it in the run status so external UIs can correlate runs with their own conversation IDs.
### GET /v1/runs/{run_id}[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-v1runsrun_id "Direct link to GET /v1/runs/{run_id}")
Poll the current run state. This is useful for dashboards that need status without holding an SSE connection open, or for UIs that reconnect after navigation.

```
"object":"hermes.run","run_id":"run_abc123","status":"completed","session_id":"space-session","model":"hermes-agent","output":"Done.","usage":{"input_tokens":50,"output_tokens":200,"total_tokens":250}
```

Statuses are retained briefly after terminal states (`completed`, `failed`, or `cancelled`) for polling and UI reconciliation.
### GET /v1/runs/{run_id}/events[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-v1runsrun_idevents "Direct link to GET /v1/runs/{run_id}/events")
Server-Sent Events stream of the run's tool-call progress, token deltas, and lifecycle events. Designed for dashboards and thick clients that want to attach/detach without losing state.
### POST /v1/runs/{run_id}/stop[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-v1runsrun_idstop "Direct link to POST /v1/runs/{run_id}/stop")
Interrupt a running agent turn. The endpoint returns immediately with `{"status": "stopping"}` while Hermes asks the active agent to stop at the next safe interruption point.
## Jobs API (background scheduled work)[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#jobs-api-background-scheduled-work "Direct link to Jobs API \(background scheduled work\)")
The server exposes a lightweight jobs CRUD surface for managing scheduled / background agent runs from a remote client. All endpoints are gated behind the same bearer auth.
### GET /api/jobs[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-apijobs "Direct link to GET /api/jobs")
List all scheduled jobs.
### POST /api/jobs[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-apijobs "Direct link to POST /api/jobs")
Create a new scheduled job. Body accepts the same shape as `hermes cron` — prompt, schedule, skills, provider override, delivery target.
### GET /api/jobs/{job_id}[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-apijobsjob_id "Direct link to GET /api/jobs/{job_id}")
Fetch a single job's definition and last-run state.
### PATCH /api/jobs/{job_id}[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#patch-apijobsjob_id "Direct link to PATCH /api/jobs/{job_id}")
Update fields on an existing job (prompt, schedule, etc.). Partial updates are merged.
### DELETE /api/jobs/{job_id}[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#delete-apijobsjob_id "Direct link to DELETE /api/jobs/{job_id}")
Remove a job. Also cancels any in-flight run.
### POST /api/jobs/{job_id}/pause[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-apijobsjob_idpause "Direct link to POST /api/jobs/{job_id}/pause")
Pause a job without deleting it. Next-scheduled-run timestamps are suspended until resumed.
### POST /api/jobs/{job_id}/resume[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-apijobsjob_idresume "Direct link to POST /api/jobs/{job_id}/resume")
Resume a previously paused job.
### POST /api/jobs/{job_id}/run[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-apijobsjob_idrun "Direct link to POST /api/jobs/{job_id}/run")
Trigger the job to run immediately, out of schedule.
## System Prompt Handling[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#system-prompt-handling "Direct link to System Prompt Handling")
When a frontend sends a `system` message (Chat Completions) or `instructions` field (Responses API), hermes-agent **layers it on top** of its core system prompt. Your agent keeps all its tools, memory, and skills — the frontend's system prompt adds extra instructions.
This means you can customize behavior per-frontend without losing capabilities:
  * Open WebUI system prompt: "You are a Python expert. Always include type hints."
  * The agent still has terminal, file tools, web search, memory, etc.


## Authentication[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#authentication "Direct link to Authentication")
Bearer token auth via the `Authorization` header:

```
Authorization: Bearer ***
```

Configure the key via `API_SERVER_KEY` env var. If you need a browser to call Hermes directly, also set `API_SERVER_CORS_ORIGINS` to an explicit allowlist.
The API server gives full access to hermes-agent's toolset, **including terminal commands**. When binding to a non-loopback address like `0.0.0.0`, `API_SERVER_KEY` is **required**. Also keep `API_SERVER_CORS_ORIGINS` narrow to control browser access.
The default bind address (`127.0.0.1`) is for local-only use. Browser access is disabled by default; enable it only for explicit trusted origins.
## Configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#configuration "Direct link to Configuration")
### Environment Variables[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#environment-variables "Direct link to Environment Variables")  
| Variable  | Default  | Description  |  
| --- | --- | --- |  
| `API_SERVER_ENABLED`  | `false`  | Enable the API server  |  
| `API_SERVER_PORT`  | `8642`  | HTTP server port  |  
| `API_SERVER_HOST`  | `127.0.0.1`  | Bind address (localhost only by default)  |  
| `API_SERVER_KEY`  | _(none)_  | Bearer token for auth  |  
| `API_SERVER_CORS_ORIGINS`  | _(none)_  | Comma-separated allowed browser origins  |  
| `API_SERVER_MODEL_NAME`  | _(profile name)_  | Model name on `/v1/models`. Defaults to profile name, or `hermes-agent` for default profile.  |  
### config.yaml[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#configyaml "Direct link to config.yaml")

```
# Not yet supported — use environment variables.# config.yaml support coming in a future release.
```

## Security Headers[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#security-headers "Direct link to Security Headers")
All responses include security headers:
  * `X-Content-Type-Options: nosniff` — prevents MIME type sniffing
  * `Referrer-Policy: no-referrer` — prevents referrer leakage


## CORS[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#cors "Direct link to CORS")
The API server does **not** enable browser CORS by default.
For direct browser access, set an explicit allowlist:

```
API_SERVER_CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

When CORS is enabled:
  * **Preflight responses** include `Access-Control-Max-Age: 600` (10 minute cache)
  * **SSE streaming responses** include CORS headers so browser EventSource clients work correctly
  * **`Idempotency-Key`**is an allowed request header — clients can send it for deduplication (responses are cached by key for 5 minutes)


Most documented frontends such as Open WebUI connect server-to-server and do not need CORS at all.
## Compatible Frontends[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#compatible-frontends "Direct link to Compatible Frontends")
Any frontend that supports the OpenAI API format works. Tested/documented integrations:  
| Frontend  | Stars  | Connection  |  
| --- | --- | --- |  
| 126k  | Full guide available  |  
| LobeChat  | 73k  | Custom provider endpoint  |  
| LibreChat  | 34k  | Custom endpoint in librechat.yaml  |  
| AnythingLLM  | 56k  | Generic OpenAI provider  |  
| NextChat  | 87k  | BASE_URL env var  |  
| ChatBox  | 39k  | API Host setting  |  
| Jan  | 26k  | Remote model config  |  
| HF Chat-UI  | 8k  | OPENAI_BASE_URL  |  
| big-AGI  | 7k  | Custom endpoint  |  
| OpenAI Python SDK  | —  | `OpenAI(base_url="http://localhost:8642/v1")`  |  
| curl  | —  | Direct HTTP requests  |  
## Multi-User Setup with Profiles[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#multi-user-setup-with-profiles "Direct link to Multi-User Setup with Profiles")
To give multiple users their own isolated Hermes instance (separate config, memory, skills), use [profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles):

```
# Create a profile per userhermes profile create alicehermes profile create bob# Configure each profile's API server on a different port. API_SERVER_* are env# vars (not config.yaml keys), so write them to each profile's .env:cat>> ~/.hermes/profiles/alice/.env <<EOFAPI_SERVER_ENABLED=trueAPI_SERVER_PORT=8643API_SERVER_KEY=alice-secretEOFcat>> ~/.hermes/profiles/bob/.env <<EOFAPI_SERVER_ENABLED=trueAPI_SERVER_PORT=8644API_SERVER_KEY=bob-secretEOF# Start each profile's gatewayhermes -p alice gateway &hermes -p bob gateway &
```

Each profile's API server automatically advertises the profile name as the model ID:
  * `http://localhost:8643/v1/models` → model `alice`
  * `http://localhost:8644/v1/models` → model `bob`


In Open WebUI, add each as a separate connection. The model dropdown shows `alice` and `bob` as distinct models, each backed by a fully isolated Hermes instance. See the [Open WebUI guide](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/open-webui#multi-user-setup-with-profiles) for details.
## Limitations[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#limitations "Direct link to Limitations")
  * **Response storage** — stored responses (for `previous_response_id`) are persisted in SQLite and survive gateway restarts. Max 100 stored responses (LRU eviction).
  * **No file upload** — inline images are supported on both `/v1/chat/completions` and `/v1/responses`, but uploaded files (`file`, `input_file`, `file_id`) and non-image document inputs are not supported through the API.
  * **Model field is cosmetic** — the `model` field in requests is accepted but the actual LLM model used is configured server-side in config.yaml.


## Proxy Mode[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#proxy-mode "Direct link to Proxy Mode")
The API server also serves as the backend for **gateway proxy mode**. When another Hermes gateway instance is configured with `GATEWAY_PROXY_URL` pointing at this API server, it forwards all messages here instead of running its own agent. This enables split deployments — for example, a Docker container handling Matrix E2EE that relays to a host-side agent.
See [Matrix Proxy Mode](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/matrix#proxy-mode-e2ee-on-macos) for the full setup guide.
  * [Quick Start](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#quick-start)
    * [1. Enable the API server](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#1-enable-the-api-server)
    * [2. Start the gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#2-start-the-gateway)
    * [3. Connect a frontend](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#3-connect-a-frontend)
  * [Endpoints](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#endpoints)
    * [POST /v1/chat/completions](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-v1chatcompletions)
    * [POST /v1/responses](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-v1responses)
    * [GET /v1/responses/{id}](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-v1responsesid)
    * [DELETE /v1/responses/{id}](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#delete-v1responsesid)
    * [GET /v1/models](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-v1models)
    * [GET /v1/capabilities](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-v1capabilities)
    * [GET /health](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-health)
    * [GET /health/detailed](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-healthdetailed)
  * [Runs API (streaming-friendly alternative)](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#runs-api-streaming-friendly-alternative)
    * [POST /v1/runs](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-v1runs)
    * [GET /v1/runs/{run_id}](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-v1runsrun_id)
    * [GET /v1/runs/{run_id}/events](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-v1runsrun_idevents)
    * [POST /v1/runs/{run_id}/stop](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-v1runsrun_idstop)
  * [Jobs API (background scheduled work)](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#jobs-api-background-scheduled-work)
    * [GET /api/jobs](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-apijobs)
    * [POST /api/jobs](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-apijobs)
    * [GET /api/jobs/{job_id}](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#get-apijobsjob_id)
    * [PATCH /api/jobs/{job_id}](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#patch-apijobsjob_id)
    * [DELETE /api/jobs/{job_id}](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#delete-apijobsjob_id)
    * [POST /api/jobs/{job_id}/pause](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-apijobsjob_idpause)
    * [POST /api/jobs/{job_id}/resume](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-apijobsjob_idresume)
    * [POST /api/jobs/{job_id}/run](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#post-apijobsjob_idrun)
  * [System Prompt Handling](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#system-prompt-handling)
  * [Authentication](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#authentication)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#configuration)
    * [Environment Variables](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#environment-variables)
    * [config.yaml](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#configyaml)
  * [Security Headers](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#security-headers)
  * [Compatible Frontends](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#compatible-frontends)
  * [Multi-User Setup with Profiles](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#multi-user-setup-with-profiles)
  * [Limitations](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server#limitations)


