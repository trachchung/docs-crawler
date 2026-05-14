<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage -->

本页总览
Hermes Agent uses a SQLite database (`~/.hermes/state.db`) to persist session metadata, full message history, and model configuration across CLI and gateway sessions. This replaces the earlier per-session JSONL file approach.
Source file: `hermes_state.py`
## Architecture Overview[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#architecture-overview "Architecture Overview的直接链接")

```
~/.hermes/state.db (SQLite, WAL mode)├── sessions              — Session metadata, token counts, billing├── messages              — Full message history per session├── messages_fts          — FTS5 virtual table (content + tool_name + tool_calls)├── messages_fts_trigram  — FTS5 virtual table with trigram tokenizer (CJK / substring search)├── state_meta            — Key/value metadata table└── schema_version        — Single-row table tracking migration state
```

Key design decisions:
  * **WAL mode** for concurrent readers + one writer (gateway multi-platform)
  * **FTS5 virtual table** for fast text search across all session messages
  * **Session lineage** via `parent_session_id` chains (compression-triggered splits)
  * **Source tagging** (`cli`, `telegram`, `discord`, etc.) for platform filtering
  * Batch runner and RL trajectories are NOT stored here (separate systems)


## SQLite Schema[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#sqlite-schema "SQLite Schema的直接链接")
### Sessions Table[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#sessions-table "Sessions Table的直接链接")

```
CREATETABLEIFNOTEXISTS sessions (    id TEXTPRIMARYKEY,    source TEXTNOTNULL,    user_id TEXT,    model TEXT,    model_config TEXT,    system_prompt TEXT,    parent_session_id TEXT,    started_at REALNOTNULL,    ended_at REAL,    end_reason TEXT,    message_count INTEGERDEFAULT0,    tool_call_count INTEGERDEFAULT0,    input_tokens INTEGERDEFAULT0,    output_tokens INTEGERDEFAULT0,    cache_read_tokens INTEGERDEFAULT0,    cache_write_tokens INTEGERDEFAULT0,    reasoning_tokens INTEGERDEFAULT0,    billing_provider TEXT,    billing_base_url TEXT,    billing_mode TEXT,    estimated_cost_usd REAL,    actual_cost_usd REAL,    cost_status TEXT,    cost_source TEXT,    pricing_version TEXT,    title TEXT,    api_call_count INTEGERDEFAULT0,FOREIGNKEY(parent_session_id)REFERENCES sessions(id)CREATEINDEXIFNOTEXISTS idx_sessions_source ON sessions(source);CREATEINDEXIFNOTEXISTS idx_sessions_parent ON sessions(parent_session_id);CREATEINDEXIFNOTEXISTS idx_sessions_started ON sessions(started_at DESC);CREATEUNIQUEINDEXIFNOTEXISTS idx_sessions_title_uniqueON sessions(title)WHERE title ISNOTNULL;
```

### Messages Table[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#messages-table "Messages Table的直接链接")

```
CREATETABLEIFNOTEXISTS messages (    id INTEGERPRIMARYKEY AUTOINCREMENT,    session_id TEXTNOTNULLREFERENCES sessions(id),    role TEXTNOTNULL,    content TEXT,    tool_call_id TEXT,    tool_calls TEXT,    tool_name TEXT,timestampREALNOTNULL,    token_count INTEGER,    finish_reason TEXT,    reasoning TEXT,    reasoning_content TEXT,    reasoning_details TEXT,    codex_reasoning_items TEXT,    codex_message_items TEXTCREATEINDEXIFNOTEXISTS idx_messages_session ON messages(session_id,timestamp);
```

Notes:
  * `tool_calls` is stored as a JSON string (serialized list of tool call objects)
  * `reasoning_details`, `codex_reasoning_items`, and `codex_message_items` are stored as JSON strings
  * `reasoning` stores the raw reasoning text for providers that expose it
  * Timestamps are Unix epoch floats (`time.time()`)


### FTS5 Full-Text Search[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#fts5-full-text-search "FTS5 Full-Text Search的直接链接")

```
CREATE VIRTUAL TABLEIFNOTEXISTS messages_fts USING fts5(    content,    content=messages,    content_rowid=id
```

The FTS5 table is kept in sync via three triggers that fire on INSERT, UPDATE, and DELETE of the `messages` table:

```
CREATETRIGGERIFNOTEXISTS messages_fts_insert AFTERINSERTON messages BEGININSERTINTO messages_fts(rowid, content)VALUES(new.id, new.content);END;CREATETRIGGERIFNOTEXISTS messages_fts_delete AFTERDELETEON messages BEGININSERTINTO messages_fts(messages_fts, rowid, content)VALUES('delete', old.id, old.content);END;CREATETRIGGERIFNOTEXISTS messages_fts_update AFTERUPDATEON messages BEGININSERTINTO messages_fts(messages_fts, rowid, content)VALUES('delete', old.id, old.content);INSERTINTO messages_fts(rowid, content)VALUES(new.id, new.content);END;
```

## Schema Version and Migrations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#schema-version-and-migrations "Schema Version and Migrations的直接链接")
Current schema version: **11**
The `schema_version` table stores a single integer. Simple column additions are handled declaratively by `_reconcile_columns()` (which diffs live columns against `SCHEMA_SQL` and ADDs any missing ones). The version-gated chain is reserved for data migrations and index/FTS changes that can't be expressed declaratively:  
| Version  | Change  |  
| --- | --- |  
| 1  | Initial schema (sessions, messages, FTS5)  |  
| 2  | Add `finish_reason` column to messages  |  
| 3  | Add `title` column to sessions  |  
| 4  | Add unique index on `title` (NULLs allowed, non-NULL must be unique)  |  
| 5  | Add billing columns: `cache_read_tokens`, `cache_write_tokens`, `reasoning_tokens`, `billing_provider`, `billing_base_url`, `billing_mode`, `estimated_cost_usd`, `actual_cost_usd`, `cost_status`, `cost_source`, `pricing_version`  |  
| 6  | Add reasoning columns to messages: `reasoning`, `reasoning_details`, `codex_reasoning_items`  |  
| 7  | Add `reasoning_content` column to messages  |  
| 8  | Add `api_call_count` column to sessions  |  
| 9  | Add `codex_message_items` column to messages for Codex Responses message id/phase replay  |  
| 10  | Add `messages_fts_trigram` virtual table (trigram tokenizer for CJK / substring search) and backfill existing rows  |  
| 11  | Re-index `messages_fts` and `messages_fts_trigram` to cover `tool_name` + `tool_calls` and switch from external-content to inline mode; drop old triggers and backfill every message row  |  
Declarative column adds use `ALTER TABLE ADD COLUMN` wrapped in try/except to handle the column-already-exists case (idempotent). The version number is bumped after each successful migration block.
## Write Contention Handling[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#write-contention-handling "Write Contention Handling的直接链接")
Multiple hermes processes (gateway + CLI sessions + worktree agents) share one `state.db`. The `SessionDB` class handles write contention with:
  * **Short SQLite timeout** (1 second) instead of the default 30s
  * **Application-level retry** with random jitter (20-150ms, up to 15 retries)
  * **BEGIN IMMEDIATE** transactions to surface lock contention at transaction start
  * **Periodic WAL checkpoints** every 50 successful writes (PASSIVE mode)


This avoids the "convoy effect" where SQLite's deterministic internal backoff causes all competing writers to retry at the same intervals.

```
_WRITE_MAX_RETRIES = 15_WRITE_RETRY_MIN_S = 0.020   # 20ms_WRITE_RETRY_MAX_S = 0.150   # 150ms_CHECKPOINT_EVERY_N_WRITES = 50
```

## Common Operations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#common-operations "Common Operations的直接链接")
### Initialize[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#initialize "Initialize的直接链接")

```
from hermes_state import SessionDBdb = SessionDB()# Default: ~/.hermes/state.dbdb = SessionDB(db_path=Path("/tmp/test.db"))# Custom path
```

### Create and Manage Sessions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#create-and-manage-sessions "Create and Manage Sessions的直接链接")

```
# Create a new sessiondb.create_session(    session_id="sess_abc123",    source="cli",    model="anthropic/claude-sonnet-4.6",    user_id="user_1",    parent_session_id=None,# or previous session ID for lineage# End a sessiondb.end_session("sess_abc123", end_reason="user_exit")# Reopen a session (clear ended_at/end_reason)db.reopen_session("sess_abc123")
```

### Store Messages[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#store-messages "Store Messages的直接链接")

```
msg_id = db.append_message(    session_id="sess_abc123",    role="assistant",    content="Here's the answer...",    tool_calls=[{"id":"call_1","function":{"name":"terminal","arguments":"{}"}}],    token_count=150,    finish_reason="stop",    reasoning="Let me think about this...",
```

### Retrieve Messages[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#retrieve-messages "Retrieve Messages的直接链接")

```
# Raw messages with all metadatamessages = db.get_messages("sess_abc123")# OpenAI conversation format (for API replay)conversation = db.get_messages_as_conversation("sess_abc123")# Returns: [{"role": "user", "content": "..."}, {"role": "assistant", ...}]
```

### Session Titles[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#session-titles "Session Titles的直接链接")

```
# Set a title (must be unique among non-NULL titles)db.set_session_title("sess_abc123","Fix Docker Build")# Resolve by title (returns most recent in lineage)session_id = db.resolve_session_by_title("Fix Docker Build")# Auto-generate next title in lineagenext_title = db.get_next_title_in_lineage("Fix Docker Build")# Returns: "Fix Docker Build #2"
```

## Full-Text Search[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#full-text-search "Full-Text Search的直接链接")
The `search_messages()` method supports FTS5 query syntax with automatic sanitization of user input.
### Basic Search[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#basic-search "Basic Search的直接链接")

```
results = db.search_messages("docker deployment")
```

### FTS5 Query Syntax[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#fts5-query-syntax "FTS5 Query Syntax的直接链接")  
| Syntax  | Example  | Meaning  |  
| --- | --- | --- |  
| Keywords  | `docker deployment`  | Both terms (implicit AND)  |  
| Quoted phrase  | `"exact phrase"`  | Exact phrase match  |  
| Boolean OR  | `docker OR kubernetes`  | Either term  |  
| Boolean NOT  | `python NOT java`  | Exclude term  |  
| Prefix  | `deploy*`  | Prefix match  |  
### Filtered Search[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#filtered-search "Filtered Search的直接链接")

```
# Search only CLI sessionsresults = db.search_messages("error", source_filter=["cli"])# Exclude gateway sessionsresults = db.search_messages("bug", exclude_sources=["telegram","discord"])# Search only user messagesresults = db.search_messages("help", role_filter=["user"])
```

### Search Results Format[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#search-results-format "Search Results Format的直接链接")
Each result includes:
  * `id`, `session_id`, `role`, `timestamp`
  * `snippet` — FTS5-generated snippet with `>>>match<<<` markers
  * `context` — 1 message before and after the match (content truncated to 200 chars)
  * `source`, `model`, `session_started` — from the parent session


The `_sanitize_fts5_query()` method handles edge cases:
  * Strips unmatched quotes and special characters
  * Wraps hyphenated terms in quotes (`chat-send` → `"chat-send"`)
  * Removes dangling boolean operators (`hello AND` → `hello`)


## Session Lineage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#session-lineage "Session Lineage的直接链接")
Sessions can form chains via `parent_session_id`. This happens when context compression triggers a session split in the gateway.
### Query: Find Session Lineage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#query-find-session-lineage "Query: Find Session Lineage的直接链接")

```
-- Find all ancestors of a sessionWITH RECURSIVE lineage AS(SELECT*FROM sessions WHERE id = ?UNIONALLSELECT s.*FROM sessions sJOIN lineage l ON s.id = l.parent_session_idSELECT id, title, started_at, parent_session_id FROM lineage;-- Find all descendants of a sessionWITH RECURSIVE descendants AS(SELECT*FROM sessions WHERE id = ?UNIONALLSELECT s.*FROM sessions sJOIN descendants d ON s.parent_session_id = d.idSELECT id, title, started_at FROM descendants;
```

### Query: Recent Sessions with Preview[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#query-recent-sessions-with-preview "Query: Recent Sessions with Preview的直接链接")

```
SELECT s.*,COALESCE((SELECT SUBSTR(m.content,1,63)FROM messages mWHERE m.session_id = s.id AND m.role ='user'AND m.content ISNOTNULLORDERBY m.timestamp, m.id LIMIT1),)AS preview,COALESCE((SELECTMAX(m2.timestamp)FROM messages m2 WHERE m2.session_id = s.id),.started_at)AS last_activeFROM sessions sORDERBY s.started_at DESCLIMIT20;
```

### Query: Token Usage Statistics[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#query-token-usage-statistics "Query: Token Usage Statistics的直接链接")

```
-- Total tokens by modelSELECT model,COUNT(*)as session_count,SUM(input_tokens)as total_input,SUM(output_tokens)as total_output,SUM(estimated_cost_usd)as total_costFROM sessionsWHERE model ISNOTNULLGROUPBY modelORDERBY total_cost DESC;-- Sessions with highest token usageSELECT id, title, model, input_tokens + output_tokens AS total_tokens,       estimated_cost_usdFROM sessionsORDERBY total_tokens DESCLIMIT10;
```

## Export and Cleanup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#export-and-cleanup "Export and Cleanup的直接链接")

```
# Export a single session with messagesdata = db.export_session("sess_abc123")# Export all sessions (with messages) as list of dictsall_data = db.export_all(source="cli")# Delete old sessions (only ended sessions)deleted_count = db.prune_sessions(older_than_days=90)deleted_count = db.prune_sessions(older_than_days=30, source="telegram")# Clear messages but keep the session recorddb.clear_messages("sess_abc123")# Delete session and all messagesdb.delete_session("sess_abc123")
```

## Database Location[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#database-location "Database Location的直接链接")
Default path: `~/.hermes/state.db`
This is derived from `hermes_constants.get_hermes_home()` which resolves to `~/.hermes/` by default, or the value of `HERMES_HOME` environment variable.
The database file, WAL file (`state.db-wal`), and shared-memory file (`state.db-shm`) are all created in the same directory.
  * [Architecture Overview](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#architecture-overview)
  * [SQLite Schema](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#sqlite-schema)
    * [Sessions Table](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#sessions-table)
    * [Messages Table](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#messages-table)
    * [FTS5 Full-Text Search](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#fts5-full-text-search)
  * [Schema Version and Migrations](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#schema-version-and-migrations)
  * [Write Contention Handling](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#write-contention-handling)
  * [Common Operations](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#common-operations)
    * [Create and Manage Sessions](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#create-and-manage-sessions)
    * [Store Messages](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#store-messages)
    * [Retrieve Messages](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#retrieve-messages)
    * [Session Titles](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#session-titles)
  * [Full-Text Search](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#full-text-search)
    * [Basic Search](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#basic-search)
    * [FTS5 Query Syntax](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#fts5-query-syntax)
    * [Filtered Search](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#filtered-search)
    * [Search Results Format](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#search-results-format)
  * [Session Lineage](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#session-lineage)
    * [Query: Find Session Lineage](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#query-find-session-lineage)
    * [Query: Recent Sessions with Preview](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#query-recent-sessions-with-preview)
    * [Query: Token Usage Statistics](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#query-token-usage-statistics)
  * [Export and Cleanup](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#export-and-cleanup)
  * [Database Location](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/session-storage#database-location)


