<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions -->

本页总览
Hermes Agent automatically saves every conversation as a session. Sessions enable conversation resume, cross-session search, and full conversation history management.
## How Sessions Work[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#how-sessions-work "How Sessions Work的直接链接")
Every conversation — whether from the CLI, Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Teams, or any other messaging platform — is stored as a session with full message history. Sessions are tracked in two complementary systems:
  1. **SQLite database** (`~/.hermes/state.db`) — structured session metadata with FTS5 full-text search
  2. **JSONL transcripts** (`~/.hermes/sessions/`) — raw conversation transcripts including tool calls (gateway)


The SQLite database stores:
  * Session ID, source platform, user ID
  * **Session title** (unique, human-readable name)
  * Model name and configuration
  * System prompt snapshot
  * Full message history (role, content, tool calls, tool results)
  * Token counts (input/output)
  * Timestamps (started_at, ended_at)
  * Parent session ID (for compression-triggered session splitting)


### Session Sources[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-sources "Session Sources的直接链接")
Each session is tagged with its source platform:  
| Source  | Description  |  
| --- | --- |  
| `cli`  | Interactive CLI (`hermes` or `hermes chat`)  |  
| `telegram`  | Telegram messenger  |  
| `discord`  | Discord server/DM  |  
| `slack`  | Slack workspace  |  
| `whatsapp`  | WhatsApp messenger  |  
| `signal`  | Signal messenger  |  
| `matrix`  | Matrix rooms and DMs  |  
| `mattermost`  | Mattermost channels  |  
| `email`  | Email (IMAP/SMTP)  |  
| `sms`  | SMS via Twilio  |  
| `dingtalk`  | DingTalk messenger  |  
| `feishu`  | Feishu/Lark messenger  |  
| `wecom`  | WeCom (WeChat Work)  |  
| `weixin`  | Weixin (personal WeChat)  |  
| `bluebubbles`  | Apple iMessage via BlueBubbles macOS server  |  
| `qqbot`  | QQ Bot (Tencent QQ) via Official API v2  |  
| `homeassistant`  | Home Assistant conversation  |  
| `webhook`  | Incoming webhooks  |  
| `api-server`  | API server requests  |  
| `acp`  | ACP editor integration  |  
| `cron`  | Scheduled cron jobs  |  
| `batch`  | Batch processing runs  |  
## CLI Session Resume[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#cli-session-resume "CLI Session Resume的直接链接")
Resume previous conversations from the CLI using `--continue` or `--resume`:
### Continue Last Session[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#continue-last-session "Continue Last Session的直接链接")

```
# Resume the most recent CLI sessionhermes --continuehermes -c# Or with the chat subcommandhermes chat --continuehermes chat -c
```

This looks up the most recent `cli` session from the SQLite database and loads its full conversation history.
### Resume by Name[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#resume-by-name "Resume by Name的直接链接")
If you've given a session a title (see [Session Naming](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-naming) below), you can resume it by name:

```
# Resume a named sessionhermes -c"my project"# If there are lineage variants (my project, my project #2, my project #3),# this automatically resumes the most recent onehermes -c"my project"# → resumes "my project #3"
```

### Resume Specific Session[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#resume-specific-session "Resume Specific Session的直接链接")

```
# Resume a specific session by IDhermes --resume 20250305_091523_a1b2c3d4hermes -r 20250305_091523_a1b2c3d4# Resume by titlehermes --resume"refactoring auth"# Or with the chat subcommandhermes chat --resume 20250305_091523_a1b2c3d4
```

Session IDs are shown when you exit a CLI session, and can be found with `hermes sessions list`.
### Conversation Recap on Resume[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#conversation-recap-on-resume "Conversation Recap on Resume的直接链接")
When you resume a session, Hermes displays a compact recap of the previous conversation in a styled panel before the input prompt:
Resume mode shows a compact recap panel with recent user and assistant turns before returning you to the live prompt.
The recap:
  * Shows **user messages** (gold `●`) and **assistant responses** (green `◆`)
  * **Truncates** long messages (300 chars for user, 200 chars / 3 lines for assistant)
  * **Collapses tool calls** to a count with tool names (e.g., `[3 tool calls: terminal, web_search]`)
  * **Hides** system messages, tool results, and internal reasoning
  * **Caps** at the last 10 exchanges with a "... N earlier messages ..." indicator
  * Uses **dim styling** to distinguish from the active conversation


To disable the recap and keep the minimal one-liner behavior, set in `~/.hermes/config.yaml`:

```
display:resume_display: minimal   # default: full
```

Session IDs follow the format `YYYYMMDD_HHMMSS_<hex>` — CLI/TUI sessions use a 6-char hex suffix (e.g. `20250305_091523_a1b2c3`), gateway sessions use an 8-char suffix (e.g. `20250305_091523_a1b2c3d4`). You can resume by ID (full or unique prefix) or by title — both work with `-c` and `-r`.
## Cross-Platform Handoff[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#cross-platform-handoff "Cross-Platform Handoff的直接链接")
Use `/handoff <platform>` from a CLI session to transfer the live conversation to a messaging platform's home channel. The agent picks up exactly where the CLI left off — same session id, full role-aware transcript, tool calls and all.

```
# Inside a CLI session/handoff telegram
```

What happens:
  1. The CLI validates that `<platform>` is enabled and has a home channel set (run `/sethome` from the destination chat once to configure it).
  2. The CLI marks the session pending and **block-polls the gateway**. It refuses if the agent is mid-turn — wait for the current response to finish first.
  3. The gateway watcher claims the handoff and asks the destination adapter for a fresh thread:
     * **Telegram** — opens a new forum topic (DM topics if Bot API 9.4+ Topics mode is enabled in the chat, or a forum supergroup topic).
     * **Discord** — creates a 1440-min auto-archive thread under the home text channel.
     * **Slack** — posts a seed message and uses its `ts` as the thread anchor.
     * **WhatsApp / Signal / Matrix / SMS** — no native threads, falls back to the home channel directly.
  4. The gateway re-binds the destination key to your existing CLI session id, then forges a synthetic user turn asking the agent to confirm and summarize. The reply lands in the new thread.
  5. When the gateway acknowledges success, the CLI prints a `/resume` hint and exits cleanly:

```
↻ Handoff complete. The session is now active on telegram.  Resume it on this CLI later with: /resume my-session-title
```

  6. From that point, the conversation lives on the platform. Reply in the new thread — anyone authorized in that channel shares the same session, and any later real user message in the thread joins seamlessly because thread sessions key without `user_id`.


**Resume back to CLI:** when you want to come back to a desktop, just run `/resume <title>` (or `hermes -r "<title>"` from the shell) and pick up where the platform left off.
**Failure modes:**
  * No home channel configured → CLI refuses with a `/sethome` hint.
  * Platform not enabled / gateway not running → CLI times out at 60s with a clear message and your CLI session stays intact.
  * Thread creation fails (permissions, topics-mode off) → falls back to the home channel directly and still completes; no thread isolation but the handoff itself works.
  * `adapter.send` fails (rate limit, transient API error) → handoff marked failed with the reason; the row clears so you can retry.


**Limitation worth knowing:** for non-thread-capable platforms with multi-user group home channels, the synthetic turn keys as a DM-style session. This works for self-DM home channels (the typical setup) but isn't ideal for genuinely shared group chats. Threading covers Telegram / Discord / Slack — by far the common case — so most setups never hit this.
## Session Naming[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-naming "Session Naming的直接链接")
Give sessions human-readable titles so you can find and resume them easily.
### Auto-Generated Titles[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#auto-generated-titles "Auto-Generated Titles的直接链接")
Hermes automatically generates a short descriptive title (3–7 words) for each session after the first exchange. This runs in a background thread using a fast auxiliary model, so it adds no latency. You'll see auto-generated titles when browsing sessions with `hermes sessions list` or `hermes sessions browse`.
Auto-titling only fires once per session and is skipped if you've already set a title manually.
### Setting a Title Manually[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#setting-a-title-manually "Setting a Title Manually的直接链接")
Use the `/title` slash command inside any chat session (CLI or gateway):

```
/title my research project
```

The title is applied immediately. If the session hasn't been created in the database yet (e.g., you run `/title` before sending your first message), it's queued and applied once the session starts.
You can also rename existing sessions from the command line:

```
hermes sessions rename 20250305_091523_a1b2c3d4 "refactoring auth module"
```

### Title Rules[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#title-rules "Title Rules的直接链接")
  * **Unique** — no two sessions can share the same title
  * **Max 100 characters** — keeps listing output clean
  * **Sanitized** — control characters, zero-width chars, and RTL overrides are stripped automatically
  * **Normal Unicode is fine** — emoji, CJK, accented characters all work


### Auto-Lineage on Compression[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#auto-lineage-on-compression "Auto-Lineage on Compression的直接链接")
When a session's context is compressed (manually via `/compress` or automatically), Hermes creates a new continuation session. If the original had a title, the new session automatically gets a numbered title:

```
"my project" → "my project #2" → "my project #3"
```

When you resume by name (`hermes -c "my project"`), it automatically picks the most recent session in the lineage.
### /title in Messaging Platforms[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#title-in-messaging-platforms "/title in Messaging Platforms的直接链接")
The `/title` command works in all gateway platforms (Telegram, Discord, Slack, WhatsApp):
  * `/title My Research` — set the session title
  * `/title` — show the current title


## Session Management Commands[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-management-commands "Session Management Commands的直接链接")
Hermes provides a full set of session management commands via `hermes sessions`:
### List Sessions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#list-sessions "List Sessions的直接链接")

```
# List recent sessions (default: last 20)hermes sessions list# Filter by platformhermes sessions list --source telegram# Show more sessionshermes sessions list --limit50
```

When sessions have titles, the output shows titles, previews, and relative timestamps:

```
Title                  Preview                                  Last Active   ID────────────────────────────────────────────────────────────────────────────────────────────────refactoring auth       Help me refactor the auth module please   2h ago        20250305_091523_amy project #3          Can you check the test failures?          yesterday     20250304_143022_e—                      What's the weather in Las Vegas?          3d ago        20250303_101500_f
```

When no sessions have titles, a simpler format is used:

```
Preview                                            Last Active   Src    ID──────────────────────────────────────────────────────────────────────────────────────Help me refactor the auth module please             2h ago        cli    20250305_091523_aWhat's the weather in Las Vegas?                    3d ago        tele   20250303_101500_f
```

### Export Sessions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#export-sessions "Export Sessions的直接链接")

```
# Export all sessions to a JSONL filehermes sessions export backup.jsonl# Export sessions from a specific platformhermes sessions export telegram-history.jsonl --source telegram# Export a single sessionhermes sessions export session.jsonl --session-id 20250305_091523_a1b2c3d4
```

Exported files contain one JSON object per line with full session metadata and all messages.
### Delete a Session[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#delete-a-session "Delete a Session的直接链接")

```
# Delete a specific session (with confirmation)hermes sessions delete 20250305_091523_a1b2c3d4# Delete without confirmationhermes sessions delete 20250305_091523_a1b2c3d4 --yes
```

### Rename a Session[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#rename-a-session "Rename a Session的直接链接")

```
# Set or change a session's titlehermes sessions rename 20250305_091523_a1b2c3d4 "debugging auth flow"# Multi-word titles don't need quotes in the CLIhermes sessions rename 20250305_091523_a1b2c3d4 debugging auth flow
```

If the title is already in use by another session, an error is shown.
### Prune Old Sessions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#prune-old-sessions "Prune Old Sessions的直接链接")

```
# Delete ended sessions older than 90 days (default)hermes sessions prune# Custom age thresholdhermes sessions prune --older-than 30# Only prune sessions from a specific platformhermes sessions prune --source telegram --older-than 60# Skip confirmationhermes sessions prune --older-than 30--yes
```

Pruning only deletes **ended** sessions (sessions that have been explicitly ended or auto-reset). Active sessions are never pruned.
### Session Statistics[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-statistics "Session Statistics的直接链接")

```
hermes sessions stats
```

Output:

```
Total sessions: 142Total messages: 3847  cli: 89 sessions  telegram: 38 sessions  discord: 15 sessionsDatabase size: 12.4 MB
```

For deeper analytics — token usage, cost estimates, tool breakdown, and activity patterns — use [`hermes insights`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/reference/cli-commands#hermes-insights).
## Session Search Tool[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-search-tool "Session Search Tool的直接链接")
The agent has a built-in `session_search` tool that performs full-text search across all past conversations using SQLite's FTS5 engine.
### How It Works[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#how-it-works "How It Works的直接链接")
  1. FTS5 searches matching messages ranked by relevance
  2. Groups results by session, takes the top N unique sessions (default 3)
  3. Loads each session's conversation, truncates to ~100K chars centered on matches
  4. Sends to a fast summarization model for focused summaries
  5. Returns per-session summaries with metadata and surrounding context


### FTS5 Query Syntax[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#fts5-query-syntax "FTS5 Query Syntax的直接链接")
The search supports standard FTS5 query syntax:
  * Simple keywords: `docker deployment`
  * Phrases: `"exact phrase"`
  * Boolean: `docker OR kubernetes`, `python NOT java`
  * Prefix: `deploy*`


### When It's Used[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#when-its-used "When It's Used的直接链接")
The agent is prompted to use session search automatically:
> _"When the user references something from a past conversation or you suspect relevant prior context exists, use session_search to recall it before asking them to repeat themselves."_
## Per-Platform Session Tracking[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#per-platform-session-tracking "Per-Platform Session Tracking的直接链接")
### Gateway Sessions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#gateway-sessions "Gateway Sessions的直接链接")
On messaging platforms, sessions are keyed by a deterministic session key built from the message source:  
| Chat Type  | Default Key Format  | Behavior  |  
| --- | --- | --- |  
| Telegram DM  | `agent:main:telegram:dm:<chat_id>`  | One session per DM chat  |  
| Discord DM  | `agent:main:discord:dm:<chat_id>`  | One session per DM chat  |  
| WhatsApp DM  | `agent:main:whatsapp:dm:<canonical_identifier>`  | One session per DM user (LID/phone aliases collapse to one identity when mapping exists)  |  
| Group chat  | `agent:main:<platform>:group:<chat_id>:<user_id>`  | Per-user inside the group when the platform exposes a user ID  |  
| Group thread/topic  | `agent:main:<platform>:group:<chat_id>:<thread_id>`  | Shared session for all thread participants (default). Per-user with `thread_sessions_per_user: true`.  |  
| Channel  | `agent:main:<platform>:channel:<chat_id>:<user_id>`  | Per-user inside the channel when the platform exposes a user ID  |  
When Hermes cannot get a participant identifier for a shared chat, it falls back to one shared session for that room.
### Shared vs Isolated Group Sessions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#shared-vs-isolated-group-sessions "Shared vs Isolated Group Sessions的直接链接")
By default, Hermes uses `group_sessions_per_user: true` in `config.yaml`. That means:
  * Alice and Bob can both talk to Hermes in the same Discord channel without sharing transcript history
  * one user's long tool-heavy task does not pollute another user's context window
  * interrupt handling also stays per-user because the running-agent key matches the isolated session key


If you want one shared "room brain" instead, set:

```
group_sessions_per_user:false
```

That reverts groups/channels to a single shared session per room, which preserves shared conversational context but also shares token costs, interrupt state, and context growth.
### Session Reset Policies[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-reset-policies "Session Reset Policies的直接链接")
Gateway sessions are automatically reset based on configurable policies:
  * **idle** — reset after N minutes of inactivity
  * **daily** — reset at a specific hour each day
  * **both** — reset on whichever comes first (idle or daily)
  * **none** — never auto-reset


Before a session is auto-reset, the agent is given a turn to save any important memories or skills from the conversation.
Sessions with **active background processes** are never auto-reset, regardless of policy.
## Storage Locations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#storage-locations "Storage Locations的直接链接")  
| What  | Path  | Description  |  
| --- | --- | --- |  
| SQLite database  | `~/.hermes/state.db`  | All session metadata + messages with FTS5  |  
| Gateway transcripts  | `~/.hermes/sessions/`  | JSONL transcripts per session + sessions.json index  |  
| Gateway index  | `~/.hermes/sessions/sessions.json`  | Maps session keys to active session IDs  |  
The SQLite database uses WAL mode for concurrent readers and a single writer, which suits the gateway's multi-platform architecture well.
### Database Schema[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#database-schema "Database Schema的直接链接")
Key tables in `state.db`:
  * **sessions** — session metadata (id, source, user_id, model, title, timestamps, token counts). Titles have a unique index (NULL titles allowed, only non-NULL must be unique).
  * **messages** — full message history (role, content, tool_calls, tool_name, token_count)
  * **messages_fts** — FTS5 virtual table for full-text search across message content


## Session Expiry and Cleanup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-expiry-and-cleanup "Session Expiry and Cleanup的直接链接")
### Automatic Cleanup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#automatic-cleanup "Automatic Cleanup的直接链接")
  * Gateway sessions auto-reset based on the configured reset policy
  * Before reset, the agent saves memories and skills from the expiring session
  * Opt-in auto-pruning: when `sessions.auto_prune` is `true`, ended sessions older than `sessions.retention_days` (default 90) are pruned at CLI/gateway startup
  * After a prune that actually removed rows, `state.db` is `VACUUM`ed to reclaim disk space (SQLite does not shrink the file on plain DELETE)
  * Pruning runs at most once per `sessions.min_interval_hours` (default 24); the last-run timestamp is tracked inside `state.db` itself so it's shared across every Hermes process in the same `HERMES_HOME`


Default is **off** — session history is valuable for `session_search` recall, and silently deleting it could surprise users. Enable in `~/.hermes/config.yaml`:

```
sessions:auto_prune:true# opt in — default is falseretention_days:90# keep ended sessions this many daysvacuum_after_prune:true# reclaim disk space after a pruning sweepmin_interval_hours:24# don't re-run the sweep more often than this
```

Active sessions are never auto-pruned, regardless of age.
### Manual Cleanup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#manual-cleanup "Manual Cleanup的直接链接")

```
# Prune sessions older than 90 dayshermes sessions prune# Delete a specific sessionhermes sessions delete <session_id># Export before pruning (backup)hermes sessions export backup.jsonlhermes sessions prune --older-than 30--yes
```

The database grows slowly (typical: 10-15 MB for hundreds of sessions) and session history powers `session_search` recall across past conversations, so auto-prune ships disabled. Enable it if you're running a heavy gateway/cron workload where `state.db` is meaningfully affecting performance (observed failure mode: 384 MB state.db with ~1000 sessions slowing down FTS5 inserts and `/resume` listing). Use `hermes sessions prune` for one-off cleanup without turning on the automatic sweep.
  * [How Sessions Work](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#how-sessions-work)
    * [Session Sources](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-sources)
  * [CLI Session Resume](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#cli-session-resume)
    * [Continue Last Session](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#continue-last-session)
    * [Resume by Name](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#resume-by-name)
    * [Resume Specific Session](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#resume-specific-session)
    * [Conversation Recap on Resume](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#conversation-recap-on-resume)
  * [Cross-Platform Handoff](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#cross-platform-handoff)
  * [Session Naming](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-naming)
    * [Auto-Generated Titles](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#auto-generated-titles)
    * [Setting a Title Manually](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#setting-a-title-manually)
    * [Title Rules](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#title-rules)
    * [Auto-Lineage on Compression](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#auto-lineage-on-compression)
    * [/title in Messaging Platforms](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#title-in-messaging-platforms)
  * [Session Management Commands](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-management-commands)
    * [List Sessions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#list-sessions)
    * [Export Sessions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#export-sessions)
    * [Delete a Session](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#delete-a-session)
    * [Rename a Session](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#rename-a-session)
    * [Prune Old Sessions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#prune-old-sessions)
    * [Session Statistics](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-statistics)
  * [Session Search Tool](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-search-tool)
    * [How It Works](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#how-it-works)
    * [FTS5 Query Syntax](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#fts5-query-syntax)
    * [When It's Used](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#when-its-used)
  * [Per-Platform Session Tracking](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#per-platform-session-tracking)
    * [Gateway Sessions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#gateway-sessions)
    * [Shared vs Isolated Group Sessions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#shared-vs-isolated-group-sessions)
    * [Session Reset Policies](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-reset-policies)
  * [Storage Locations](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#storage-locations)
    * [Database Schema](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#database-schema)
  * [Session Expiry and Cleanup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#session-expiry-and-cleanup)
    * [Automatic Cleanup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#automatic-cleanup)
    * [Manual Cleanup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/sessions#manual-cleanup)


