<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw -->

本页总览
`hermes claw migrate` imports your OpenClaw (or legacy Clawdbot/Moldbot) setup into Hermes. This guide covers exactly what gets migrated, the config key mappings, and what to verify after migration.
## Quick start[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#quick-start "Quick start的直接链接")

```
# Preview then migrate (always shows a preview first, then asks to confirm)hermes claw migrate# Preview only, no changeshermes claw migrate --dry-run# Full migration including API keys, skip confirmationhermes claw migrate --preset full --migrate-secrets --yes
```

The migration always shows a full preview of what will be imported before making any changes. Review the list, then confirm to proceed.
Reads from `~/.openclaw/` by default. Legacy `~/.clawdbot/` or `~/.moltbot/` directories are detected automatically. Same for legacy config filenames (`clawdbot.json`, `moltbot.json`).
## Options[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#options "Options的直接链接")  
| Option  | Description  |  
| --- | --- |  
| `--dry-run`  | Preview only — stop after showing what would be migrated.  |  
| `--preset <name>`  |  `full` (all compatible settings) or `user-data` (excludes infrastructure config). Neither preset imports secrets by default — pass `--migrate-secrets` explicitly.  |  
| `--overwrite`  | Overwrite existing Hermes files on conflicts (default: refuse to apply when the plan has conflicts).  |  
| `--migrate-secrets`  | Include API keys. Required even under `--preset full` — no preset imports secrets silently.  |  
| `--no-backup`  | Skip the pre-migration zip snapshot of `~/.hermes/` (by default a single restore-point archive is written before apply, under `~/.hermes/backups/pre-migration-*.zip`; restorable with `hermes import`).  |  
| `--source <path>`  | Custom OpenClaw directory.  |  
| `--workspace-target <path>`  | Where to place `AGENTS.md`.  |  
| `--skill-conflict <mode>`  |  `skip` (default), `overwrite`, or `rename`.  |  
| `--yes`  | Skip the confirmation prompt after preview.  |  
## What gets migrated[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#what-gets-migrated "What gets migrated的直接链接")
### Persona, memory, and instructions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#persona-memory-and-instructions "Persona, memory, and instructions的直接链接")  
| What  | OpenClaw source  | Hermes destination  | Notes  |  
| --- | --- | --- | --- |  
| Persona  | `workspace/SOUL.md`  | `~/.hermes/SOUL.md`  | Direct copy  |  
| Workspace instructions  | `workspace/AGENTS.md`  |  `AGENTS.md` in `--workspace-target`  | Requires `--workspace-target` flag  |  
| Long-term memory  | `workspace/MEMORY.md`  | `~/.hermes/memories/MEMORY.md`  | Parsed into entries, merged with existing, deduped. Uses `§` delimiter.  |  
| User profile  | `workspace/USER.md`  | `~/.hermes/memories/USER.md`  | Same entry-merge logic as memory.  |  
| Daily memory files  | `workspace/memory/*.md`  | `~/.hermes/memories/MEMORY.md`  | All daily files merged into main memory.  |  
Workspace files are also checked at `workspace.default/` and `workspace-main/` as fallback paths (OpenClaw renamed `workspace/` to `workspace-main/` in recent versions, and uses `workspace-{agentId}` for multi-agent setups).
### Skills (4 sources)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#skills-4-sources "Skills \(4 sources\)的直接链接")  
| Source  | OpenClaw location  | Hermes destination  |  
| --- | --- | --- |  
| Workspace skills  | `workspace/skills/`  | `~/.hermes/skills/openclaw-imports/`  |  
| Managed/shared skills  | `~/.openclaw/skills/`  | `~/.hermes/skills/openclaw-imports/`  |  
| Personal cross-project  | `~/.agents/skills/`  | `~/.hermes/skills/openclaw-imports/`  |  
| Project-level shared  | `workspace/.agents/skills/`  | `~/.hermes/skills/openclaw-imports/`  |  
Skill conflicts are handled by `--skill-conflict`: `skip` leaves the existing Hermes skill, `overwrite` replaces it, `rename` creates a `-imported` copy.
### Model and provider configuration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#model-and-provider-configuration "Model and provider configuration的直接链接")  
| What  | OpenClaw config path  | Hermes destination  | Notes  |  
| --- | --- | --- | --- |  
| Default model  | `agents.defaults.model`  |  `config.yaml` → `model`  | Can be a string or `{primary, fallbacks}` object  |  
| Custom providers  | `models.providers.*`  |  `config.yaml` → `custom_providers`  | Maps `baseUrl`, `apiType`/`api` — handles both short ("openai", "anthropic") and hyphenated ("openai-completions", "anthropic-messages", "google-generative-ai") values  |  
| Provider API keys  | `models.providers.*.apiKey`  | `~/.hermes/.env`  | Requires `--migrate-secrets`. See [API key resolution](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#api-key-resolution) below.  |  
### Agent behavior[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#agent-behavior "Agent behavior的直接链接")  
| What  | OpenClaw config path  | Hermes config path  | Mapping  |  
| --- | --- | --- | --- |  
| Max turns  | `agents.defaults.timeoutSeconds`  | `agent.max_turns`  |  `timeoutSeconds / 10`, capped at 200  |  
| Verbose mode  | `agents.defaults.verboseDefault`  | `agent.verbose`  | "off" / "on" / "full"  |  
| Reasoning effort  | `agents.defaults.thinkingDefault`  | `agent.reasoning_effort`  | "always"/"high"/"xhigh" → "high", "auto"/"medium"/"adaptive" → "medium", "off"/"low"/"none"/"minimal" → "low"  |  
| Compression  | `agents.defaults.compaction.mode`  | `compression.enabled`  | "off" → false, anything else → true  |  
| Compression model  | `agents.defaults.compaction.model`  | `compression.summary_model`  | Direct string copy  |  
| Human delay  | `agents.defaults.humanDelay.mode`  | `human_delay.mode`  | "natural" / "custom" / "off"  |  
| Human delay timing  |  `agents.defaults.humanDelay.minMs` / `.maxMs`  |  `human_delay.min_ms` / `.max_ms`  | Direct copy  |  
| Timezone  | `agents.defaults.userTimezone`  | `timezone`  | Direct string copy  |  
| Exec timeout  | `tools.exec.timeoutSec`  | `terminal.timeout`  | Direct copy (field is `timeoutSec`, not `timeout`)  |  
| Docker sandbox  | `agents.defaults.sandbox.backend`  | `terminal.backend`  | "docker" → "docker"  |  
| Docker image  | `agents.defaults.sandbox.docker.image`  | `terminal.docker_image`  | Direct copy  |  
### Session reset policies[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#session-reset-policies "Session reset policies的直接链接")  
| OpenClaw config path  | Hermes config path  | Notes  |  
| --- | --- | --- |  
| `session.reset.mode`  | `session_reset.mode`  | "daily", "idle", or both  |  
| `session.reset.atHour`  | `session_reset.at_hour`  | Hour (0–23) for daily reset  |  
| `session.reset.idleMinutes`  | `session_reset.idle_minutes`  | Minutes of inactivity  |  
Note: OpenClaw also has `session.resetTriggers` (a simple string array like `["daily", "idle"]`). If the structured `session.reset` isn't present, the migration falls back to inferring from `resetTriggers`.
### MCP servers[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#mcp-servers "MCP servers的直接链接")  
| OpenClaw field  | Hermes field  | Notes  |  
| --- | --- | --- |  
| `mcp.servers.*.command`  | `mcp_servers.*.command`  | Stdio transport  |  
| `mcp.servers.*.args`  | `mcp_servers.*.args`  |  
| `mcp.servers.*.env`  | `mcp_servers.*.env`  |  
| `mcp.servers.*.cwd`  | `mcp_servers.*.cwd`  |  
| `mcp.servers.*.url`  | `mcp_servers.*.url`  | HTTP/SSE transport  |  
| `mcp.servers.*.tools.include`  | `mcp_servers.*.tools.include`  | Tool filtering  |  
| `mcp.servers.*.tools.exclude`  | `mcp_servers.*.tools.exclude`  |  
### TTS (text-to-speech)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#tts-text-to-speech "TTS \(text-to-speech\)的直接链接")
TTS settings are read from **two** OpenClaw config locations with this priority:
  1. `messages.tts.providers.{provider}.*` (canonical location)
  2. Top-level `talk.providers.{provider}.*` (fallback)
  3. Legacy flat keys `messages.tts.{provider}.*` (oldest format)

  
| What  | Hermes destination  |  
| --- | --- |  
| Provider name  |  `config.yaml` → `tts.provider`  |  
| ElevenLabs voice ID  |  `config.yaml` → `tts.elevenlabs.voice_id`  |  
| ElevenLabs model ID  |  `config.yaml` → `tts.elevenlabs.model_id`  |  
| OpenAI model  |  `config.yaml` → `tts.openai.model`  |  
| OpenAI voice  |  `config.yaml` → `tts.openai.voice`  |  
| Edge TTS voice  |  `config.yaml` → `tts.edge.voice` (OpenClaw renamed "edge" to "microsoft" — both are recognized)  |  
| TTS assets  |  `~/.hermes/tts/` (file copy)  |  
### Messaging platforms[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#messaging-platforms "Messaging platforms的直接链接")  
| Platform  | OpenClaw config path  | Hermes `.env` variable  | Notes  |  
| --- | --- | --- | --- |  
| Telegram  |  `channels.telegram.botToken` or `.accounts.default.botToken`  | `TELEGRAM_BOT_TOKEN`  | Token can be string or [SecretRef](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#secretref-handling). Both flat and accounts layout supported.  |  
| Telegram  | `credentials/telegram-default-allowFrom.json`  | `TELEGRAM_ALLOWED_USERS`  | Comma-joined from `allowFrom[]` array  |  
| Discord  |  `channels.discord.token` or `.accounts.default.token`  | `DISCORD_BOT_TOKEN`  |  
| Discord  |  `channels.discord.allowFrom` or `.accounts.default.allowFrom`  | `DISCORD_ALLOWED_USERS`  |  
| Slack  |  `channels.slack.botToken` or `.accounts.default.botToken`  | `SLACK_BOT_TOKEN`  |  
| Slack  |  `channels.slack.appToken` or `.accounts.default.appToken`  | `SLACK_APP_TOKEN`  |  
| Slack  |  `channels.slack.allowFrom` or `.accounts.default.allowFrom`  | `SLACK_ALLOWED_USERS`  |  
| WhatsApp  |  `channels.whatsapp.allowFrom` or `.accounts.default.allowFrom`  | `WHATSAPP_ALLOWED_USERS`  | Auth via Baileys QR pairing — requires re-pairing after migration  |  
| Signal  |  `channels.signal.account` or `.accounts.default.account`  | `SIGNAL_ACCOUNT`  |  
| Signal  |  `channels.signal.httpUrl` or `.accounts.default.httpUrl`  | `SIGNAL_HTTP_URL`  |  
| Signal  |  `channels.signal.allowFrom` or `.accounts.default.allowFrom`  | `SIGNAL_ALLOWED_USERS`  |  
| Matrix  |  `channels.matrix.accessToken` or `.accounts.default.accessToken`  | `MATRIX_ACCESS_TOKEN`  | Uses `accessToken` (not `botToken`)  |  
| Mattermost  |  `channels.mattermost.botToken` or `.accounts.default.botToken`  | `MATTERMOST_BOT_TOKEN`  |  
### Other config[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#other-config "Other config的直接链接")  
| What  | OpenClaw path  | Hermes path  | Notes  |  
| --- | --- | --- | --- |  
| Approval mode  | `approvals.exec.mode`  |  `config.yaml` → `approvals.mode`  | "auto"→"off", "always"→"manual", "smart"→"smart"  |  
| Command allowlist  | `exec-approvals.json`  |  `config.yaml` → `command_allowlist`  | Patterns merged and deduped  |  
| Browser CDP URL  | `browser.cdpUrl`  |  `config.yaml` → `browser.cdp_url`  |  
| Browser headless  | `browser.headless`  |  `config.yaml` → `browser.headless`  |  
| Brave search key  | `tools.web.search.brave.apiKey`  |  `.env` → `BRAVE_API_KEY`  | Requires `--migrate-secrets`  |  
| Gateway auth token  | `gateway.auth.token`  |  `.env` → `HERMES_GATEWAY_TOKEN`  | Requires `--migrate-secrets`  |  
| Working directory  | `agents.defaults.workspace`  |  `.env` → `MESSAGING_CWD`  |  
### Archived (no direct Hermes equivalent)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#archived-no-direct-hermes-equivalent "Archived \(no direct Hermes equivalent\)的直接链接")
These are saved to `~/.hermes/migration/openclaw/<timestamp>/archive/` for manual review:  
| What  | Archive file  | How to recreate in Hermes  |  
| --- | --- | --- |  
| `IDENTITY.md`  | `archive/workspace/IDENTITY.md`  | Merge into `SOUL.md`  |  
| `TOOLS.md`  | `archive/workspace/TOOLS.md`  | Hermes has built-in tool instructions  |  
| `HEARTBEAT.md`  | `archive/workspace/HEARTBEAT.md`  | Use cron jobs for periodic tasks  |  
| `BOOTSTRAP.md`  | `archive/workspace/BOOTSTRAP.md`  | Use context files or skills  |  
| Cron jobs  | `archive/cron-config.json`  | Recreate with `hermes cron create`  |  
| Plugins  | `archive/plugins-config.json`  | See [plugins guide](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/hooks)  |  
| Hooks/webhooks  | `archive/hooks-config.json`  | Use `hermes webhook` or gateway hooks  |  
| Memory backend  | `archive/memory-backend-config.json`  | Configure via `hermes honcho`  |  
| Skills registry  | `archive/skills-registry-config.json`  | Use `hermes skills config`  |  
| UI/identity  | `archive/ui-identity-config.json`  | Use `/skin` command  |  
| Logging  | `archive/logging-diagnostics-config.json`  | Set in `config.yaml` logging section  |  
| Multi-agent list  | `archive/agents-list.json`  | Use Hermes profiles  |  
| Channel bindings  | `archive/bindings.json`  | Manual setup per platform  |  
| Complex channels  | `archive/channels-deep-config.json`  | Manual platform config  |  
## API key resolution[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#api-key-resolution "API key resolution的直接链接")
When `--migrate-secrets` is enabled, API keys are collected from **four sources** in priority order:
  1. **Config values** — `models.providers.*.apiKey` and TTS provider keys in `openclaw.json`
  2. **Environment file** — `~/.openclaw/.env` (keys like `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`, etc.)
  3. **Config env sub-object** — `openclaw.json` → `"env"` or `"env"."vars"` (some setups store keys here instead of a separate `.env` file)
  4. **Auth profiles** — `~/.openclaw/agents/main/agent/auth-profiles.json` (per-agent credentials)


Config values take priority. Each subsequent source fills any remaining gaps.
### Supported key targets[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#supported-key-targets "Supported key targets的直接链接")
`OPENROUTER_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `DEEPSEEK_API_KEY`, `GEMINI_API_KEY`, `ZAI_API_KEY`, `MINIMAX_API_KEY`, `ELEVENLABS_API_KEY`, `TELEGRAM_BOT_TOKEN`, `VOICE_TOOLS_OPENAI_KEY`
Keys not in this allowlist are never copied.
## SecretRef handling[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#secretref-handling "SecretRef handling的直接链接")
OpenClaw config values for tokens and API keys can be in three formats:

```
// Plain string"channels":{"telegram":{"botToken":"123456:ABC-DEF..."}}// Environment template"channels":{"telegram":{"botToken":"${TELEGRAM_BOT_TOKEN}"}}// SecretRef object"channels":{"telegram":{"botToken":{"source":"env","id":"TELEGRAM_BOT_TOKEN"}}}
```

The migration resolves all three formats. For env templates and SecretRef objects with `source: "env"`, it looks up the value in `~/.openclaw/.env` and the `openclaw.json` env sub-object. SecretRef objects with `source: "file"` or `source: "exec"` can't be resolved automatically — the migration warns about these, and those values must be added to Hermes manually via `hermes config set`.
## After migration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#after-migration "After migration的直接链接")
  1. **Check the migration report** — printed on completion with counts of migrated, skipped, and conflicting items.
  2. **Review archived files** — anything in `~/.hermes/migration/openclaw/<timestamp>/archive/` needs manual attention.
  3. **Start a new session** — imported skills and memory entries take effect in new sessions, not the current one.
  4. **Verify API keys** — run `hermes status` to check provider authentication.
  5. **Test messaging** — if you migrated platform tokens, restart the gateway: `systemctl --user restart hermes-gateway`
  6. **Check session policies** — verify `hermes config get session_reset` matches your expectations.
  7. **Re-pair WhatsApp** — WhatsApp uses QR code pairing (Baileys), not token migration. Run `hermes whatsapp` to pair.
  8. **Archive cleanup** — after confirming everything works, run `hermes claw cleanup` to rename leftover OpenClaw directories to `.pre-migration/` (prevents state confusion).


## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#troubleshooting "Troubleshooting的直接链接")
### "OpenClaw directory not found"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#openclaw-directory-not-found ""OpenClaw directory not found"的直接链接")
The migration checks `~/.openclaw/`, then `~/.clawdbot/`, then `~/.moltbot/`. If your installation is elsewhere, use `--source /path/to/your/openclaw`.
### "No provider API keys found"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#no-provider-api-keys-found ""No provider API keys found"的直接链接")
Keys might be stored in several places depending on your OpenClaw version: inline in `openclaw.json` under `models.providers.*.apiKey`, in `~/.openclaw/.env`, in the `openclaw.json` `"env"` sub-object, or in `agents/main/agent/auth-profiles.json`. The migration checks all four. If keys use `source: "file"` or `source: "exec"` SecretRefs, they can't be resolved automatically — add them via `hermes config set`.
### Skills not appearing after migration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#skills-not-appearing-after-migration "Skills not appearing after migration的直接链接")
Imported skills land in `~/.hermes/skills/openclaw-imports/`. Start a new session for them to take effect, or run `/skills` to verify they're loaded.
### TTS voice not migrated[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#tts-voice-not-migrated "TTS voice not migrated的直接链接")
OpenClaw stores TTS settings in two places: `messages.tts.providers.*` and the top-level `talk` config. The migration checks both. If your voice ID was set via the OpenClaw UI (stored in a different path), you may need to set it manually: `hermes config set tts.elevenlabs.voice_id YOUR_VOICE_ID`.
  * [Quick start](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#quick-start)
  * [What gets migrated](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#what-gets-migrated)
    * [Persona, memory, and instructions](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#persona-memory-and-instructions)
    * [Skills (4 sources)](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#skills-4-sources)
    * [Model and provider configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#model-and-provider-configuration)
    * [Agent behavior](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#agent-behavior)
    * [Session reset policies](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#session-reset-policies)
    * [MCP servers](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#mcp-servers)
    * [TTS (text-to-speech)](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#tts-text-to-speech)
    * [Messaging platforms](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#messaging-platforms)
    * [Other config](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#other-config)
    * [Archived (no direct Hermes equivalent)](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#archived-no-direct-hermes-equivalent)
  * [API key resolution](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#api-key-resolution)
    * [Supported key targets](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#supported-key-targets)
  * [SecretRef handling](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#secretref-handling)
  * [After migration](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#after-migration)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#troubleshooting)
    * ["OpenClaw directory not found"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#openclaw-directory-not-found)
    * ["No provider API keys found"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#no-provider-api-keys-found)
    * [Skills not appearing after migration](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#skills-not-appearing-after-migration)
    * [TTS voice not migrated](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw#tts-voice-not-migrated)


