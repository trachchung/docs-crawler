<!-- Source: https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#__docusaurus_skipToContent_fallback)
On this page
The cron subsystem provides scheduled task execution — from simple one-shot delays to recurring cron-expression jobs with skill injection and cross-platform delivery.
## Key Files[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#key-files "Direct link to Key Files")  
| File  | Purpose  |  
| --- | --- |  
| `cron/jobs.py`  | Job model, storage, atomic read/write to `jobs.json`  |  
| `cron/scheduler.py`  | Scheduler loop — due-job detection, execution, repeat tracking  |  
| `tools/cronjob_tools.py`  | Model-facing `cronjob` tool registration and handler  |  
| `gateway/run.py`  | Gateway integration — cron ticking in the long-running loop  |  
| `hermes_cli/cron.py`  | CLI `hermes cron` subcommands  |  
## Scheduling Model[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#scheduling-model "Direct link to Scheduling Model")
Four schedule formats are supported:  
| Format  | Example  | Behavior  |  
| --- | --- | --- |  
| **Relative delay**  |  `30m`, `2h`, `1d`  | One-shot, fires after the specified duration  |  
| **Interval**  |  `every 2h`, `every 30m`  | Recurring, fires at regular intervals  |  
| **Cron expression**  | `0 9 * * *`  | Standard 5-field cron syntax (minute, hour, day, month, weekday)  |  
| **ISO timestamp**  | `2025-01-15T09:00:00`  | One-shot, fires at the exact time  |  
The model-facing surface is a single `cronjob` tool with action-style operations: `create`, `list`, `update`, `pause`, `resume`, `run`, `remove`.
## Job Storage[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#job-storage "Direct link to Job Storage")
Jobs are stored in `~/.hermes/cron/jobs.json` with atomic write semantics (write to temp file, then rename). Each job record contains:

```
"id":"a1b2c3d4e5f6","name":"Daily briefing","prompt":"Summarize today's AI news and funding rounds","schedule":{"kind":"cron","expr":"0 9 * * *","display":"0 9 * * *""skills":["ai-funding-daily-report"],"deliver":"telegram:-1001234567890","repeat":{"times":null,"completed":42"state":"scheduled","enabled":true,"next_run_at":"2025-01-16T09:00:00Z","last_run_at":"2025-01-15T09:00:00Z","last_status":"ok","created_at":"2025-01-01T00:00:00Z","model":null,"provider":null,"script":null
```

### Job Lifecycle States[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#job-lifecycle-states "Direct link to Job Lifecycle States")  
| State  | Meaning  |  
| --- | --- |  
| `scheduled`  | Active, will fire at next scheduled time  |  
| `paused`  | Suspended — won't fire until resumed  |  
| `completed`  | Repeat count exhausted or one-shot that has fired  |  
| `running`  | Currently executing (transient state)  |  
### Backward Compatibility[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#backward-compatibility "Direct link to Backward Compatibility")
Older jobs may have a single `skill` field instead of the `skills` array. The scheduler normalizes this at load time — single `skill` is promoted to `skills: [skill]`.
## Scheduler Runtime[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#scheduler-runtime "Direct link to Scheduler Runtime")
### Tick Cycle[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#tick-cycle "Direct link to Tick Cycle")
The scheduler runs on a periodic tick (default: every 60 seconds):

```
tick()  1. Acquire scheduler lock (prevents overlapping ticks)  2. Load all jobs from jobs.json  3. Filter to due jobs (next_run <= now AND state == "scheduled")  4. For each due job:     a. Set state to "running"     b. Create fresh AIAgent session (no conversation history)     c. Load attached skills in order (injected as user messages)     d. Run the job prompt through the agent     e. Deliver the response to the configured target     f. Update run_count, compute next_run     g. If repeat count exhausted → state = "completed"     h. Otherwise → state = "scheduled"  5. Write updated jobs back to jobs.json  6. Release scheduler lock
```

### Gateway Integration[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#gateway-integration "Direct link to Gateway Integration")
In gateway mode, the scheduler runs in a dedicated background thread (`_start_cron_ticker` in `gateway/run.py`) that calls `scheduler.tick()` every 60 seconds alongside message handling.
In CLI mode, cron jobs only fire when `hermes cron` commands are run or during active CLI sessions.
### Fresh Session Isolation[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#fresh-session-isolation "Direct link to Fresh Session Isolation")
Each cron job runs in a completely fresh agent session:
  * No conversation history from previous runs
  * No memory of previous cron executions (unless persisted to memory/files)
  * The prompt must be self-contained — cron jobs cannot ask clarifying questions
  * The `cronjob` toolset is disabled (recursion guard)


## Skill-Backed Jobs[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#skill-backed-jobs "Direct link to Skill-Backed Jobs")
A cron job can attach one or more skills via the `skills` field. At execution time:
  1. Skills are loaded in the specified order
  2. Each skill's SKILL.md content is injected as context
  3. The job's prompt is appended as the task instruction
  4. The agent processes the combined skill context + prompt


This enables reusable, tested workflows without pasting full instructions into cron prompts. For example:

```
Create a daily funding report → attach "ai-funding-daily-report" skill
```

### Script-Backed Jobs[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#script-backed-jobs "Direct link to Script-Backed Jobs")
Jobs can also attach a Python script via the `script` field. The script runs _before_ each agent turn, and its stdout is injected into the prompt as context. This enables data collection and change detection patterns:

```
# ~/.hermes/scripts/check_competitors.pyimport requests, json# Fetch competitor release notes, diff against last run# Print summary to stdout — agent analyzes and reports
```

The script timeout defaults to 120 seconds. `_get_script_timeout()` resolves the limit through a three-layer chain:
  1. **Module-level override** — `_SCRIPT_TIMEOUT` (for tests/monkeypatching). Only used when it differs from the default.
  2. **Environment variable** — `HERMES_CRON_SCRIPT_TIMEOUT`
  3. **Config** — `cron.script_timeout_seconds` in `config.yaml` (read via `load_config()`)
  4. **Default** — 120 seconds


### Provider Recovery[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#provider-recovery "Direct link to Provider Recovery")
`run_job()` passes the user's configured fallback providers and credential pool into the `AIAgent` instance:
  * **Fallback providers** — reads `fallback_providers` (list) or `fallback_model` (legacy dict) from `config.yaml`, matching the gateway's `_load_fallback_model()` pattern. Passed as `fallback_model=` to `AIAgent.__init__`, which normalizes both formats into a fallback chain.
  * **Credential pool** — loads via `load_pool(provider)` from `agent.credential_pool` using the resolved runtime provider name. Only passed when the pool has credentials (`pool.has_credentials()`). Enables same-provider key rotation on 429/rate-limit errors.


This mirrors the gateway's behavior — without it, cron agents would fail on rate limits without attempting recovery.
## Delivery Model[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#delivery-model "Direct link to Delivery Model")
Cron job results can be delivered to any supported platform:  
| Target  | Syntax  | Example  |  
| --- | --- | --- |  
| Origin chat  | `origin`  | Deliver to the chat where the job was created  |  
| Local file  | `local`  | Save to `~/.hermes/cron/output/`  |  
| Telegram  |  `telegram` or `telegram:<chat_id>`  | `telegram:-1001234567890`  |  
| Discord  |  `discord` or `discord:#channel`  | `discord:#engineering`  |  
| Slack  | `slack`  | Deliver to Slack home channel  |  
| WhatsApp  | `whatsapp`  | Deliver to WhatsApp home  |  
| Signal  | `signal`  | Deliver to Signal  |  
| Matrix  | `matrix`  | Deliver to Matrix home room  |  
| Mattermost  | `mattermost`  | Deliver to Mattermost home  |  
| Email  | `email`  | Deliver via email  |  
| SMS  | `sms`  | Deliver via SMS  |  
| Home Assistant  | `homeassistant`  | Deliver to HA conversation  |  
| DingTalk  | `dingtalk`  | Deliver to DingTalk  |  
| Feishu  | `feishu`  | Deliver to Feishu  |  
| WeCom  | `wecom`  | Deliver to WeCom  |  
| Weixin  | `weixin`  | Deliver to Weixin (WeChat)  |  
| BlueBubbles  | `bluebubbles`  | Deliver to iMessage via BlueBubbles  |  
| QQ Bot  | `qqbot`  | Deliver to QQ (Tencent) via Official API v2  |  
For Telegram topics, use the format `telegram:<chat_id>:<thread_id>` (e.g., `telegram:-1001234567890:17585`).
### Response Wrapping[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#response-wrapping "Direct link to Response Wrapping")
By default (`cron.wrap_response: true`), cron deliveries are wrapped with:
  * A header identifying the cron job name and task
  * A footer noting the agent cannot see the delivered message in conversation


The `[SILENT]` prefix in a cron response suppresses delivery entirely — useful for jobs that only need to write to files or perform side effects.
### Session Isolation[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#session-isolation "Direct link to Session Isolation")
Cron deliveries are NOT mirrored into gateway session conversation history. They exist only in the cron job's own session. This prevents message alternation violations in the target chat's conversation.
## Recursion Guard[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#recursion-guard "Direct link to Recursion Guard")
Cron-run sessions have the `cronjob` toolset disabled. This prevents:
  * A scheduled job from creating new cron jobs
  * Recursive scheduling that could explode token usage
  * Accidental mutation of the job schedule from within a job


## Locking[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#locking "Direct link to Locking")
The scheduler uses cross-process file-based locking (`fcntl.flock` on Unix, `msvcrt.locking` on Windows) to prevent overlapping ticks from executing the same due-job batch twice — even between the gateway's in-process ticker and a standalone `hermes cron` / manual `tick()` call. If the lock cannot be acquired, `tick()` returns 0 immediately.
## CLI Interface[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#cli-interface "Direct link to CLI Interface")
The `hermes cron` CLI provides direct job management:

```
hermes cron list                    # Show all jobshermes cron create                  # Interactive job creation (alias: add)hermes cron edit <job_id># Edit job configurationhermes cron pause <job_id># Pause a running jobhermes cron resume <job_id># Resume a paused jobhermes cron run <job_id># Trigger immediate executionhermes cron remove <job_id># Delete a job
```

## Related Docs[​](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#related-docs "Direct link to Related Docs")
  * [Cron Feature Guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
  * [Gateway Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-internals)
  * [Agent Loop Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop)


  * [Scheduling Model](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#scheduling-model)
  * [Job Storage](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#job-storage)
    * [Job Lifecycle States](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#job-lifecycle-states)
    * [Backward Compatibility](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#backward-compatibility)
  * [Scheduler Runtime](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#scheduler-runtime)
    * [Gateway Integration](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#gateway-integration)
    * [Fresh Session Isolation](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#fresh-session-isolation)
  * [Skill-Backed Jobs](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#skill-backed-jobs)
    * [Script-Backed Jobs](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#script-backed-jobs)
    * [Provider Recovery](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#provider-recovery)
  * [Delivery Model](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#delivery-model)
    * [Response Wrapping](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#response-wrapping)
    * [Session Isolation](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#session-isolation)
  * [Recursion Guard](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#recursion-guard)
  * [CLI Interface](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#cli-interface)
  * [Related Docs](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals#related-docs)


