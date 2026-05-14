<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only -->

本页总览
Sometimes you already know exactly what message you want to send. You don't need an agent to reason about it — you just need a script to run on a timer, and its output (if any) to land in Telegram / Discord / Slack / Signal.
Hermes calls this **no-agent mode**. It's the cron system minus the LLM.

```
   ┌──────────────────┐          ┌──────────────────┐   │ scheduler tick   │  every   │ run script       │   │ (every N minutes)│ ──────▶ │ (bash or python) │   └──────────────────┘          └──────────────────┘                                          │ stdout                                 ┌──────────────────┐                                 │ delivery router  │                                 │ (telegram/disc…) │                                 └──────────────────┘
```

  * **No LLM call.** Zero tokens, zero agent loop, zero model spend.
  * **Script is the job.** The script decides whether to alert. Emit output → message gets sent. Emit nothing → silent tick.
  * **Bash or Python.** `.sh` / `.bash` files run under `/bin/bash`; any other extension runs under the current Python interpreter. Anything in `~/.hermes/scripts/` is accepted.
  * **Same scheduler.** Lives in `cronjob` alongside LLM jobs — pausing, resuming, listing, logs, and delivery targeting all work the same way.


## When to Use It[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#when-to-use-it "When to Use It的直接链接")
Use no-agent mode for:
  * **Memory / disk / GPU watchdogs.** Run every 5 minutes, alert only when a threshold is breached.
  * **CI hooks.** Deploy finished → post the commit SHA. Build failed → send the last 100 lines of the log.
  * **Periodic metrics.** "Daily Stripe revenue at 9am" as a simple API call + pretty-print.
  * **External event pollers.** Check an API, alert on state change.
  * **Heartbeats.** Ping a dashboard every N minutes to prove the host is alive.


Use a normal (LLM-driven) cron job when you need the agent to **decide** what to say — summarize a long document, pick interesting items from a feed, draft a human-friendly message. The no-agent path is for cases where the script's stdout already IS the message.
## Create One from Chat[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#create-one-from-chat "Create One from Chat的直接链接")
The real win of no-agent mode is that the agent itself can set up the watchdog for you — no editor, no shell, no remembering CLI flags. You describe what you want, Hermes writes the script, schedules it, and tells you when it'll fire.
### Example transcript[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#example-transcript "Example transcript的直接链接")
> **You:** ping me on telegram if RAM is over 85% every 5 minutes
> **Hermes:** _(writes`~/.hermes/scripts/memory-watchdog.sh` , then calls `cronjob(...)` with `no_agent=true`)_
> Set up. Runs every 5 min, alerts Telegram only when RAM is over 85%. Script: `memory-watchdog.sh`. Job ID: `abc123`.
Under the hood, the agent makes two tool calls:

```
# 1. Write the check scriptwrite_file(    path="~/.hermes/scripts/memory-watchdog.sh",    content='''#!/usr/bin/env bashram_pct=$(free | awk '/^Mem:/ {printf "%d", $3 * 100 / $2}')if [ "$ram_pct" -ge 85 ]; then  echo "RAM ${ram_pct}% on $(hostname)"# Empty stdout = silent tick; no message sent.''',# 2. Schedule it — no_agent=True skips the LLM on every tickcronjob(    action="create",    schedule="every 5m",    script="memory-watchdog.sh",    no_agent=True,    deliver="telegram",    name="memory-watchdog",
```

From that point on every tick is free: the scheduler runs the script, pipes its stdout to Telegram if non-empty, and never touches a model.
### What the agent decides for you[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#what-the-agent-decides-for-you "What the agent decides for you的直接链接")
When you phrase a request like "alert me when X" or "every N minutes check Y and tell me if Z", Hermes' `cronjob` tool description tells it to reach for `no_agent=True` whenever the message content is fully determined by the script. It falls back to the normal LLM-driven path when the request needs reasoning (_"summarize the new issues"_ , _"pick the most interesting headlines"_ , _"draft a friendly reminder"_).
You don't have to specify `--no-agent` yourself. Just describe the behavior.
### Managing watchdogs from chat[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#managing-watchdogs-from-chat "Managing watchdogs from chat的直接链接")
The agent can pause, resume, edit, and remove jobs the same way it creates them:
> **You:** stop the memory watchdog for tonight
> **Hermes:** _(calls`cronjob(action='pause', job_id='abc123')`)_
> Paused. Resume with "turn it back on" or via `hermes cron resume abc123`.
> **You:** change it to every 15 minutes
> **Hermes:** _(calls`cronjob(action='update', job_id='abc123', schedule='every 15m')`)_
The full lifecycle (create / list / update / pause / resume / run-now / remove) is available to the agent without you learning any CLI commands.
## Create One from the CLI[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#create-one-from-the-cli "Create One from the CLI的直接链接")
Prefer the shell? The CLI path gives you the same result with three commands:

```
# 1. Write your scriptcat> ~/.hermes/scripts/memory-watchdog.sh <<'EOF'#!/usr/bin/env bash# Alert when RAM usage is over 85%. Silent otherwise.RAM_PCT=$(free | awk '/^Mem:/ {printf "%d", $3 * 100 / $2}')if [ "$RAM_PCT" -ge 85 ]; then  echo "⚠ RAM ${RAM_PCT}% on $(hostname)"# Empty stdout = silent run; no message sent.EOFchmod +x ~/.hermes/scripts/memory-watchdog.sh# 2. Schedule ithermes cron create "every 5m"\  --no-agent \--script memory-watchdog.sh \--deliver telegram \--name"memory-watchdog"# 3. Verifyhermes cron listhermes cron run <job_id># fire it once to test
```

That's the whole thing. No prompt, no skill, no model.
## How Script Output Maps to Delivery[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#how-script-output-maps-to-delivery "How Script Output Maps to Delivery的直接链接")  
| Script behavior  | Result  |  
| --- | --- |  
| Exit 0, non-empty stdout  | stdout is delivered verbatim  |  
| Exit 0, empty stdout  | Silent tick — no delivery  |  
| Exit 0, stdout contains `{"wakeAgent": false}` on the last line  | Silent tick (shared gate with LLM jobs)  |  
| Non-zero exit code  | Error alert is delivered (so a broken watchdog doesn't fail silently)  |  
| Script timeout  | Error alert is delivered  |  
The "silent when empty" behavior is the key to the classic watchdog pattern: the script is free to run every minute, but the channel only sees a message when something actually needs attention.
## Script Rules[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#script-rules "Script Rules的直接链接")
Scripts must live in `~/.hermes/scripts/`. This is enforced at both job-creation time and run time — absolute paths, `~/` expansion, and path-traversal patterns (`../`) are rejected. The same directory is shared with the pre-check script gate used by LLM jobs.
Interpreter choice is by file extension:  
| Extension  | Interpreter  |  
| --- | --- |  
|  `.sh`, `.bash`  | `/bin/bash`  |  
| anything else  |  `sys.executable` (current Python)  |  
We intentionally do NOT honour `#!/...` shebangs — keeping the interpreter set explicit and small reduces the surface the scheduler trusts.
## Schedule Syntax[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#schedule-syntax "Schedule Syntax的直接链接")
Same as all other cron jobs:

```
hermes cron create "every 5m"# intervalhermes cron create "every 2h"hermes cron create "0 9 * * *"# standard cron: 9am dailyhermes cron create "30m"# one-shot: run once in 30 minutes
```

See the [cron feature reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/cron) for the full syntax.
## Delivery Targets[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#delivery-targets "Delivery Targets的直接链接")
`--deliver` accepts everything the gateway knows about. Some common shapes:

```
--deliver telegram                       # platform home channel--deliver telegram:-1001234567890        # specific chat--deliver telegram:-1001234567890:17585  # specific Telegram forum topic--deliver discord:#ops--deliver slack:#engineering--deliver signal:+15551234567--deliverlocal# just save to ~/.hermes/cron/output/
```

No running gateway is required at script-run time for bot-token platforms (Telegram, Discord, Slack, Signal, SMS, WhatsApp) — the tool calls each platform's REST endpoint directly using the credentials already in `~/.hermes/.env` / `~/.hermes/config.yaml`.
## Editing and Lifecycle[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#editing-and-lifecycle "Editing and Lifecycle的直接链接")

```
hermes cron list                                    # see all jobshermes cron pause <job_id># stop firing, keep definitionhermes cron resume <job_id>hermes cron edit <job_id>--schedule"every 10m"# adjust cadencehermes cron edit <job_id>--agent# flip to LLM modehermes cron edit <job_id> --no-agent --script# flip backhermes cron remove <job_id># delete it
```

Everything that works on LLM jobs (pause, resume, manual trigger, delivery target changes) works on no-agent jobs too.
## Worked Example: Disk Space Alert[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#worked-example-disk-space-alert "Worked Example: Disk Space Alert的直接链接")

```
cat> ~/.hermes/scripts/disk-alert.sh <<'EOF'#!/usr/bin/env bash# Alert when / or /home is over 90% full.THRESHOLD=90df -h / /home 2>/dev/null | awk -v t="$THRESHOLD" '  NR > 1 && $5+0 >= t {    printf "⚠ Disk %s full on %s\n", $5, $6EOFchmod +x ~/.hermes/scripts/disk-alert.shhermes cron create "*/15 * * * *"\  --no-agent \--script disk-alert.sh \--deliver telegram \--name"disk-alert"
```

Silent when both filesystems are under 90%; fires exactly one line per over-threshold filesystem when one fills up.
## Comparison with Other Patterns[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#comparison-with-other-patterns "Comparison with Other Patterns的直接链接")  
| Approach  | What runs  | When to use  |  
| --- | --- | --- |  
|  `cronjob --no-agent` (this page)  | Your script on Hermes' schedule  | Recurring watchdogs / alerts / metrics that don't need reasoning  |  
|  `cronjob` (default, LLM)  | Agent with optional pre-check script  | When the message content requires reasoning over data  |  
| OS cron + `curl` to a [webhook subscription](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/webhooks)  | Your script on the OS schedule  | When Hermes might be unhealthy (the thing you're monitoring)  |  
For critical system-health watchdogs that must fire _even when the gateway is down_ , use OS-level cron with a plain `curl` to a Hermes webhook subscription (or any external alerting endpoint) — those run as independent OS processes and don't depend on Hermes being up. The in-gateway scheduler is the right choice when the thing being monitored is external.
## Related[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#related "Related的直接链接")
  * [Automate Anything with Cron](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/automate-with-cron) — LLM-driven cron patterns.
  * [Scheduled Tasks (Cron) reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/cron) — full schedule syntax, lifecycle, delivery routing.
  * [Webhook Subscriptions](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/webhooks) — fire-and-forget HTTP entry points for external schedulers.
  * [Gateway Internals](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/developer-guide/gateway-internals) — delivery-router internals.


  * [When to Use It](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#when-to-use-it)
  * [Create One from Chat](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#create-one-from-chat)
    * [Example transcript](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#example-transcript)
    * [What the agent decides for you](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#what-the-agent-decides-for-you)
    * [Managing watchdogs from chat](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#managing-watchdogs-from-chat)
  * [Create One from the CLI](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#create-one-from-the-cli)
  * [How Script Output Maps to Delivery](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#how-script-output-maps-to-delivery)
  * [Script Rules](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#script-rules)
  * [Schedule Syntax](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#schedule-syntax)
  * [Delivery Targets](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#delivery-targets)
  * [Editing and Lifecycle](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#editing-and-lifecycle)
  * [Worked Example: Disk Space Alert](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#worked-example-disk-space-alert)
  * [Comparison with Other Patterns](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only#comparison-with-other-patterns)


