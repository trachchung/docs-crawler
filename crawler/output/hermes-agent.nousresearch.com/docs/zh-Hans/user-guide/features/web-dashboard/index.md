<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard -->

本页总览
The web dashboard is a browser-based UI for managing your Hermes Agent installation. Instead of editing YAML files or running CLI commands, you can configure settings, manage API keys, and monitor sessions from a clean web interface.
## Quick Start[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#quick-start "Quick Start的直接链接")

```
hermes dashboard
```

This starts a local web server and opens `http://127.0.0.1:9119` in your browser. The dashboard runs entirely on your machine — no data leaves localhost.
### Options[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#options "Options的直接链接")  
| Flag  | Default  | Description  |  
| --- | --- | --- |  
| `--port`  | `9119`  | Port to run the web server on  |  
| `--host`  | `127.0.0.1`  | Bind address  |  
| `--no-open`  | —  | Don't auto-open the browser  |  
| `--insecure`  | off  | Allow binding to non-localhost hosts (**DANGEROUS** — exposes API keys on the network; pair with a firewall and strong auth)  |  
| `--tui`  | off  | Expose the in-browser Chat tab (embedded `hermes --tui` via PTY/WebSocket). Alternatively set `HERMES_DASHBOARD_TUI=1`.  |  

```
# Custom porthermes dashboard --port8080# Bind to all interfaces (use with caution on shared networks)hermes dashboard --host0.0.0.0# Start without opening browserhermes dashboard --no-open
```

## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#prerequisites "Prerequisites的直接链接")
The default `hermes-agent` install does not ship the HTTP stack or PTY helper — those are optional extras. The **web dashboard** needs FastAPI and Uvicorn (`web` extra). The **Chat** tab also needs `ptyprocess` to spawn the embedded TUI behind a pseudo-terminal (`pty` extra on POSIX). Install both with:

```
pip install'hermes-agent[web,pty]'
```

The `web` extra pulls in FastAPI/Uvicorn; `pty` pulls in `ptyprocess` (POSIX) or `pywinpty` (native Windows — note that the embedded TUI itself still requires WSL). `pip install hermes-agent[all]` includes both extras and is the easiest path if you also want messaging/voice/etc.
When you run `hermes dashboard` without the dependencies, it will tell you what to install. If the frontend hasn't been built yet and `npm` is available, it builds automatically on first launch.
## Pages[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#pages "Pages的直接链接")
### Status[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#status "Status的直接链接")
The landing page shows a live overview of your installation:
  * **Agent version** and release date
  * **Gateway status** — running/stopped, PID, connected platforms and their state
  * **Active sessions** — count of sessions active in the last 5 minutes
  * **Recent sessions** — list of the 20 most recent sessions with model, message count, token usage, and a preview of the conversation


The status page auto-refreshes every 5 seconds.
### Chat[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#chat "Chat的直接链接")
The **Chat** tab embeds the full Hermes TUI (the same interface you get from `hermes --tui`) directly in the browser. Everything you can do in the terminal TUI — slash commands, model picker, tool-call cards, markdown streaming, clarify/sudo/approval prompts, skin theming — works identically here, because the dashboard is running the real TUI binary and rendering its ANSI output through [xterm.js](https://xtermjs.org/) with its WebGL renderer for pixel-perfect cell layout.
**How it works:**
  * `/api/pty` opens a WebSocket authenticated with the dashboard's session token
  * The server spawns `hermes --tui` behind a POSIX pseudo-terminal
  * Keystrokes travel to the PTY; ANSI output streams back to the browser
  * xterm.js's WebGL renderer paints each cell to an integer-pixel grid; mouse tracking (SGR 1006), wide characters (Unicode 11), and box-drawing glyphs all render natively
  * Resizing the browser window resizes the TUI via the `@xterm/addon-fit` addon


**Resume an existing session:** from the **Sessions** tab, click the play icon (▶) next to any session. That jumps to `/chat?resume=<id>` and launches the TUI with `--resume`, loading the full history.
**Prerequisites:**
  * Node.js (same requirement as `hermes --tui`; the TUI bundle is built on first launch)
  * `ptyprocess` — installed by the `pty` extra (`pip install 'hermes-agent[web,pty]'`, or `[all]` covers both)
  * POSIX kernel (Linux, macOS, or WSL2). The `/chat` terminal pane specifically needs a POSIX PTY — native Windows Python has no equivalent, so on a native Windows install the rest of the dashboard (sessions, jobs, metrics, config editor) works but the `/chat` tab will show a banner telling you to use WSL2 for that feature.


Close the browser tab and the PTY is reaped cleanly on the server. Re-opening spawns a fresh session.
### Config[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#config "Config的直接链接")
A form-based editor for `config.yaml`. All 150+ configuration fields are auto-discovered from `DEFAULT_CONFIG` and organized into tabbed categories:
  * **model** — default model, provider, base URL, reasoning settings
  * **terminal** — backend (local/docker/ssh/modal), timeout, shell preferences
  * **display** — skin, tool progress, resume display, spinner settings
  * **agent** — max iterations, gateway timeout, service tier
  * **delegation** — subagent limits, reasoning effort
  * **memory** — provider selection, context injection settings
  * **approvals** — dangerous command approval mode (ask/yolo/deny)
  * And more — every section of config.yaml has corresponding form fields


Fields with known valid values (terminal backend, skin, approval mode, etc.) render as dropdowns. Booleans render as toggles. Everything else is a text input.
**Actions:**
  * **Save** — writes changes to `config.yaml` immediately
  * **Reset to defaults** — reverts all fields to their default values (doesn't save until you click Save)
  * **Export** — downloads the current config as JSON
  * **Import** — uploads a JSON config file to replace the current values


Config changes take effect on the next agent session or gateway restart. The web dashboard edits the same `config.yaml` file that `hermes config set` and the gateway read from.
### API Keys[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#api-keys "API Keys的直接链接")
Manage the `.env` file where API keys and credentials are stored. Keys are grouped by category:
  * **LLM Providers** — OpenRouter, Anthropic, OpenAI, DeepSeek, etc.
  * **Tool API Keys** — Browserbase, Firecrawl, Tavily, ElevenLabs, etc.
  * **Messaging Platforms** — Telegram, Discord, Slack bot tokens, etc.
  * **Agent Settings** — non-secret env vars like `API_SERVER_ENABLED`


Each key shows:
  * Whether it's currently set (with a redacted preview of the value)
  * A description of what it's for
  * A link to the provider's signup/key page
  * An input field to set or update the value
  * A delete button to remove it


Advanced/rarely-used keys are hidden by default behind a toggle.
### Sessions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#sessions "Sessions的直接链接")
Browse and inspect all agent sessions. Each row shows the session title, source platform icon (CLI, Telegram, Discord, Slack, cron), model name, message count, tool call count, and how long ago it was active. Live sessions are marked with a pulsing badge.
  * **Search** — full-text search across all message content using FTS5. Results show highlighted snippets and auto-scroll to the first matching message when expanded.
  * **Expand** — click a session to load its full message history. Messages are color-coded by role (user, assistant, system, tool) and rendered as Markdown with syntax highlighting.
  * **Tool calls** — assistant messages with tool calls show collapsible blocks with the function name and JSON arguments.
  * **Delete** — remove a session and its message history with the trash icon.


### Logs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#logs "Logs的直接链接")
View agent, gateway, and error log files with filtering and live tailing.
  * **File** — switch between `agent`, `errors`, and `gateway` log files
  * **Level** — filter by log level: ALL, DEBUG, INFO, WARNING, or ERROR
  * **Component** — filter by source component: all, gateway, agent, tools, cli, or cron
  * **Lines** — choose how many lines to display (50, 100, 200, or 500)
  * **Auto-refresh** — toggle live tailing that polls for new log lines every 5 seconds
  * **Color-coded** — log lines are colored by severity (red for errors, yellow for warnings, dim for debug)


### Analytics[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#analytics "Analytics的直接链接")
Usage and cost analytics computed from session history. Select a time period (7, 30, or 90 days) to see:
  * **Summary cards** — total tokens (input/output), cache hit percentage, total estimated or actual cost, and total session count with daily average
  * **Daily token chart** — stacked bar chart showing input and output token usage per day, with hover tooltips showing breakdowns and cost
  * **Daily breakdown table** — date, session count, input tokens, output tokens, cache hit rate, and cost for each day
  * **Per-model breakdown** — table showing each model used, its session count, token usage, and estimated cost


### Cron[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#cron "Cron的直接链接")
Create and manage scheduled cron jobs that run agent prompts on a recurring schedule.
  * **Create** — fill in a name (optional), prompt, cron expression (e.g. `0 9 * * *`), and delivery target (local, Telegram, Discord, Slack, or email)
  * **Job list** — each job shows its name, prompt preview, schedule expression, state badge (enabled/paused/error), delivery target, last run time, and next run time
  * **Pause / Resume** — toggle a job between active and paused states
  * **Trigger now** — immediately execute a job outside its normal schedule
  * **Delete** — permanently remove a cron job


### Skills[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#skills "Skills的直接链接")
Browse, search, and toggle skills and toolsets. Skills are loaded from `~/.hermes/skills/` and grouped by category.
  * **Search** — filter skills and toolsets by name, description, or category
  * **Category filter** — click category pills to narrow the list (e.g. MLOps, MCP, Red Teaming, AI)
  * **Toggle** — enable or disable individual skills with a switch. Changes take effect on the next session.
  * **Toolsets** — a separate section shows built-in toolsets (file operations, web browsing, etc.) with their active/inactive status, setup requirements, and list of included tools


The web dashboard reads and writes your `.env` file, which contains API keys and secrets. It binds to `127.0.0.1` by default — only accessible from your local machine. If you bind to `0.0.0.0`, anyone on your network can view and modify your credentials. The dashboard has no authentication of its own.
##  `/reload` Slash Command[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#reload-slash-command "reload-slash-command的直接链接")
The dashboard PR also adds a `/reload` slash command to the interactive CLI. After changing API keys via the web dashboard (or by editing `.env` directly), use `/reload` in an active CLI session to pick up the changes without restarting:

```
You → /reload  Reloaded .env (3 var(s) updated)
```

This re-reads `~/.hermes/.env` into the running process's environment. Useful when you've added a new provider key via the dashboard and want to use it immediately.
## REST API[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#rest-api "REST API的直接链接")
The web dashboard exposes a REST API that the frontend consumes. You can also call these endpoints directly for automation:
### GET /api/status[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apistatus "GET /api/status的直接链接")
Returns agent version, gateway status, platform states, and active session count.
### GET /api/sessions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apisessions "GET /api/sessions的直接链接")
Returns the 20 most recent sessions with metadata (model, token counts, timestamps, preview).
### GET /api/config[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apiconfig "GET /api/config的直接链接")
Returns the current `config.yaml` contents as JSON.
### GET /api/config/defaults[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apiconfigdefaults "GET /api/config/defaults的直接链接")
Returns the default configuration values.
### GET /api/config/schema[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apiconfigschema "GET /api/config/schema的直接链接")
Returns a schema describing every config field — type, description, category, and select options where applicable. The frontend uses this to render the correct input widget for each field.
### PUT /api/config[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#put-apiconfig "PUT /api/config的直接链接")
Saves a new configuration. Body: `{"config": {...}}`.
### GET /api/env[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apienv "GET /api/env的直接链接")
Returns all known environment variables with their set/unset status, redacted values, descriptions, and categories.
### PUT /api/env[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#put-apienv "PUT /api/env的直接链接")
Sets an environment variable. Body: `{"key": "VAR_NAME", "value": "secret"}`.
### DELETE /api/env[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#delete-apienv "DELETE /api/env的直接链接")
Removes an environment variable. Body: `{"key": "VAR_NAME"}`.
### GET /api/sessions/{session_id}[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apisessionssession_id "GET /api/sessions/{session_id}的直接链接")
Returns metadata for a single session.
### GET /api/sessions/{session_id}/messages[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apisessionssession_idmessages "GET /api/sessions/{session_id}/messages的直接链接")
Returns the full message history for a session, including tool calls and timestamps.
### GET /api/sessions/search[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apisessionssearch "GET /api/sessions/search的直接链接")
Full-text search across message content. Query parameter: `q`. Returns matching session IDs with highlighted snippets.
### DELETE /api/sessions/{session_id}[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#delete-apisessionssession_id "DELETE /api/sessions/{session_id}的直接链接")
Deletes a session and its message history.
### GET /api/logs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apilogs "GET /api/logs的直接链接")
Returns log lines. Query parameters: `file` (agent/errors/gateway), `lines` (count), `level`, `component`.
### GET /api/analytics/usage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apianalyticsusage "GET /api/analytics/usage的直接链接")
Returns token usage, cost, and session analytics. Query parameter: `days` (default 30). Response includes daily breakdowns and per-model aggregates.
### GET /api/cron/jobs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apicronjobs "GET /api/cron/jobs的直接链接")
Returns all configured cron jobs with their state, schedule, and run history.
### POST /api/cron/jobs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#post-apicronjobs "POST /api/cron/jobs的直接链接")
Creates a new cron job. Body: `{"prompt": "...", "schedule": "0 9 * * *", "name": "...", "deliver": "local"}`.
### POST /api/cron/jobs/{job_id}/pause[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#post-apicronjobsjob_idpause "POST /api/cron/jobs/{job_id}/pause的直接链接")
Pauses a cron job.
### POST /api/cron/jobs/{job_id}/resume[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#post-apicronjobsjob_idresume "POST /api/cron/jobs/{job_id}/resume的直接链接")
Resumes a paused cron job.
### POST /api/cron/jobs/{job_id}/trigger[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#post-apicronjobsjob_idtrigger "POST /api/cron/jobs/{job_id}/trigger的直接链接")
Immediately triggers a cron job outside its schedule.
### DELETE /api/cron/jobs/{job_id}[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#delete-apicronjobsjob_id "DELETE /api/cron/jobs/{job_id}的直接链接")
Deletes a cron job.
### GET /api/skills[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apiskills "GET /api/skills的直接链接")
Returns all skills with their name, description, category, and enabled status.
### PUT /api/skills/toggle[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#put-apiskillstoggle "PUT /api/skills/toggle的直接链接")
Enables or disables a skill. Body: `{"name": "skill-name", "enabled": true}`.
### GET /api/tools/toolsets[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apitoolstoolsets "GET /api/tools/toolsets的直接链接")
Returns all toolsets with their label, description, tools list, and active/configured status.
## CORS[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#cors "CORS的直接链接")
The web server restricts CORS to localhost origins only:
  * `http://localhost:9119` / `http://127.0.0.1:9119` (production)
  * `http://localhost:3000` / `http://127.0.0.1:3000`
  * `http://localhost:5173` / `http://127.0.0.1:5173` (Vite dev server)


If you run the server on a custom port, that origin is added automatically.
## Development[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#development "Development的直接链接")
If you're contributing to the web dashboard frontend:

```
# Terminal 1: start the backend APIhermes dashboard --no-open# Terminal 2: start the Vite dev server with HMRcd web/npminstallnpm run dev
```

The Vite dev server at `http://localhost:5173` proxies `/api` requests to the FastAPI backend at `http://127.0.0.1:9119`.
The frontend is built with React 19, TypeScript, Tailwind CSS v4, and shadcn/ui-style components. Production builds output to `hermes_cli/web_dist/` which the FastAPI server serves as a static SPA.
## Automatic Build on Update[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#automatic-build-on-update "Automatic Build on Update的直接链接")
When you run `hermes update`, the web frontend is automatically rebuilt if `npm` is available. This keeps the dashboard in sync with code updates. If `npm` isn't installed, the update skips the frontend build and `hermes dashboard` will build it on first launch.
## Themes & plugins[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#themes--plugins "Themes & plugins的直接链接")
The dashboard ships with six built-in themes and can be extended with user-defined themes, plugin tabs, and backend API routes — all drop-in, no repo clone needed.
**Switch themes live** from the header bar — click the palette icon next to the language switcher. Selection persists to `config.yaml` under `dashboard.theme` and is restored on page load.
Built-in themes:  
| Theme  | Character  |  
| --- | --- |  
|  **Hermes Teal** (`default`)  | Dark teal + cream, system fonts, comfortable spacing  |  
|  **Hermes Teal (Large)** (`default-large`)  | Same as default with 18px text and roomier spacing  |  
|  **Midnight** (`midnight`)  | Deep blue-violet, Inter + JetBrains Mono  |  
|  **Ember** (`ember`)  | Warm crimson + bronze, Spectral serif + IBM Plex Mono  |  
|  **Mono** (`mono`)  | Grayscale, IBM Plex, compact  |  
|  **Cyberpunk** (`cyberpunk`)  | Neon green on black, Share Tech Mono  |  
|  **Rosé** (`rose`)  | Pink + ivory, Fraunces serif, spacious  |  
To build your own theme, add a plugin tab, inject into shell slots, or expose plugin-specific REST endpoints, see **[Extending the Dashboard](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/extending-the-dashboard)** — the complete guide covers:
  * Theme YAML schema — palette, typography, layout, assets, componentStyles, colorOverrides, customCSS
  * Layout variants — `standard`, `cockpit`, `tiled`
  * Plugin manifest, SDK, shell slots, page-scoped slots (inject widgets into built-in pages without overriding them), backend FastAPI routes
  * A full combined theme-plus-plugin walkthrough (Strike Freedom cockpit demo)
  * Discovery, reload, and troubleshooting


  * [Quick Start](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#quick-start)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#prerequisites)
  * [Pages](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#pages)
  * [`/reload` Slash Command](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#reload-slash-command)
  * [REST API](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#rest-api)
    * [GET /api/status](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apistatus)
    * [GET /api/sessions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apisessions)
    * [GET /api/config](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apiconfig)
    * [GET /api/config/defaults](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apiconfigdefaults)
    * [GET /api/config/schema](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apiconfigschema)
    * [PUT /api/config](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#put-apiconfig)
    * [GET /api/env](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apienv)
    * [PUT /api/env](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#put-apienv)
    * [DELETE /api/env](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#delete-apienv)
    * [GET /api/sessions/{session_id}](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apisessionssession_id)
    * [GET /api/sessions/{session_id}/messages](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apisessionssession_idmessages)
    * [GET /api/sessions/search](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apisessionssearch)
    * [DELETE /api/sessions/{session_id}](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#delete-apisessionssession_id)
    * [GET /api/logs](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apilogs)
    * [GET /api/analytics/usage](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apianalyticsusage)
    * [GET /api/cron/jobs](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apicronjobs)
    * [POST /api/cron/jobs](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#post-apicronjobs)
    * [POST /api/cron/jobs/{job_id}/pause](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#post-apicronjobsjob_idpause)
    * [POST /api/cron/jobs/{job_id}/resume](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#post-apicronjobsjob_idresume)
    * [POST /api/cron/jobs/{job_id}/trigger](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#post-apicronjobsjob_idtrigger)
    * [DELETE /api/cron/jobs/{job_id}](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#delete-apicronjobsjob_id)
    * [GET /api/skills](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apiskills)
    * [PUT /api/skills/toggle](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#put-apiskillstoggle)
    * [GET /api/tools/toolsets](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#get-apitoolstoolsets)
  * [Development](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#development)
  * [Automatic Build on Update](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#automatic-build-on-update)
  * [Themes & plugins](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/web-dashboard#themes--plugins)


