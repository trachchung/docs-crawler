<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting -->

本页总览
When a cron job isn't behaving as expected, work through these checks in order. Most issues fall into one of four categories: timing, delivery, permissions, or skill loading.
## Jobs Not Firing[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#jobs-not-firing "Jobs Not Firing的直接链接")
### Check 1: Verify the job exists and is active[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-1-verify-the-job-exists-and-is-active "Check 1: Verify the job exists and is active的直接链接")

```
hermes cron list
```

Look for the job and confirm its state is `[active]` (not `[paused]` or `[completed]`). If it shows `[completed]`, the repeat count may be exhausted — edit the job to reset it.
### Check 2: Confirm the schedule is correct[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-2-confirm-the-schedule-is-correct "Check 2: Confirm the schedule is correct的直接链接")
A misformatted schedule silently defaults to one-shot or is rejected entirely. Test your expression:  
| Your expression  | Should evaluate to  |  
| --- | --- |  
| `0 9 * * *`  | 9:00 AM every day  |  
| `0 9 * * 1`  | 9:00 AM every Monday  |  
| `every 2h`  | Every 2 hours from now  |  
| `30m`  | 30 minutes from now  |  
| `2025-06-01T09:00:00`  | June 1, 2025 at 9:00 AM UTC  |  
If the job fires once and then disappears from the list, it's a one-shot schedule (`30m`, `1d`, or an ISO timestamp) — expected behavior.
### Check 3: Is the gateway running?[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-3-is-the-gateway-running "Check 3: Is the gateway running?的直接链接")
Cron jobs are fired by the gateway's background ticker thread, which ticks every 60 seconds. A regular CLI chat session does **not** automatically fire cron jobs.
If you're expecting jobs to fire automatically, you need a running gateway (`hermes gateway` for foreground, or `hermes gateway start` for the installed service). For one-off debugging, you can manually trigger a tick with `hermes cron tick`.
### Check 4: Check the system clock and timezone[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-4-check-the-system-clock-and-timezone "Check 4: Check the system clock and timezone的直接链接")
Jobs use the local timezone. If your machine's clock is wrong or in a different timezone than expected, jobs will fire at the wrong times. Verify:

```
datehermes cron list   # Compare next_run times with local time
```

## Delivery Failures[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#delivery-failures "Delivery Failures的直接链接")
### Check 1: Verify the deliver target is correct[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-1-verify-the-deliver-target-is-correct "Check 1: Verify the deliver target is correct的直接链接")
Delivery targets are case-sensitive and require the correct platform to be configured. A misconfigured target silently drops the response.  
| Target  | Requires  |  
| --- | --- |  
| `telegram`  |  `TELEGRAM_BOT_TOKEN` in `~/.hermes/.env`  |  
| `discord`  |  `DISCORD_BOT_TOKEN` in `~/.hermes/.env`  |  
| `slack`  |  `SLACK_BOT_TOKEN` in `~/.hermes/.env`  |  
| `whatsapp`  | WhatsApp gateway configured  |  
| `signal`  | Signal gateway configured  |  
| `matrix`  | Matrix homeserver configured  |  
| `email`  | SMTP configured in `config.yaml`  |  
| `sms`  | SMS provider configured  |  
| `local`  | Write access to `~/.hermes/cron/output/`  |  
| `origin`  | Delivers to the chat where the job was created  |  
Other supported platforms include `mattermost`, `homeassistant`, `dingtalk`, `feishu`, `wecom`, `weixin`, `bluebubbles`, `qqbot`, and `webhook`. You can also target a specific chat with `platform:chat_id` syntax (e.g., `telegram:-1001234567890`).
If delivery fails, the job still runs — it just won't send anywhere. Check `hermes cron list` for updated `last_error` field (if available).
### Check 2: Check `[SILENT]` usage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-2-check-silent-usage "check-2-check-silent-usage的直接链接")
If your cron job produces no output or the agent responds with `[SILENT]`, delivery is suppressed. This is intentional for monitoring jobs — but make sure your prompt isn't accidentally suppressing everything.
A prompt that says "respond with [SILENT] if nothing changed" will silently swallow non-empty responses too. Check your conditional logic.
### Check 3: Platform token permissions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-3-platform-token-permissions "Check 3: Platform token permissions的直接链接")
Each messaging platform bot needs specific permissions to receive messages. If delivery silently fails:
  * **Telegram** : Bot must be an admin in the target group/channel
  * **Discord** : Bot must have permission to send in the target channel
  * **Slack** : Bot must be added to the workspace and have `chat:write` scope


### Check 4: Response wrapping[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-4-response-wrapping "Check 4: Response wrapping的直接链接")
By default, cron responses are wrapped with a header and footer (`cron.wrap_response: true` in `config.yaml`). Some platforms or integrations may not handle this well. To disable:

```
cron:wrap_response:false
```

## Skill Loading Failures[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#skill-loading-failures "Skill Loading Failures的直接链接")
### Check 1: Verify skills are installed[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-1-verify-skills-are-installed "Check 1: Verify skills are installed的直接链接")

```
hermes skills list
```

Skills must be installed before they can be attached to cron jobs. If a skill is missing, install it first with `hermes skills install <skill-name>` or via `/skills` in the CLI.
### Check 2: Check skill name vs. skill folder name[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-2-check-skill-name-vs-skill-folder-name "Check 2: Check skill name vs. skill folder name的直接链接")
Skill names are case-sensitive and must match the installed skill's folder name. If your job specifies `ai-funding-daily-report` but the skill folder is `ai-funding-daily-report`, confirm the exact name from `hermes skills list`.
### Check 3: Skills that require interactive tools[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-3-skills-that-require-interactive-tools "Check 3: Skills that require interactive tools的直接链接")
Cron jobs run with the `cronjob`, `messaging`, and `clarify` toolsets disabled. This prevents recursive cron creation, direct message sending (delivery is handled by the scheduler), and interactive prompts. If a skill relies on these toolsets, it won't work in a cron context.
Check the skill's documentation to confirm it works in non-interactive (headless) mode.
### Check 4: Multi-skill ordering[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-4-multi-skill-ordering "Check 4: Multi-skill ordering的直接链接")
When using multiple skills, they load in order. If Skill A depends on context from Skill B, make sure B loads first:

```
/cron add"0 9 * * *""..."--skill context-skill --skill target-skill
```

In this example, `context-skill` loads before `target-skill`.
## Job Errors and Failures[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#job-errors-and-failures "Job Errors and Failures的直接链接")
### Check 1: Review recent job output[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-1-review-recent-job-output "Check 1: Review recent job output的直接链接")
If a job ran and failed, you may see error context in:
  1. The chat where the job delivers (if delivery succeeded)
  2. `~/.hermes/logs/agent.log` for scheduler messages (or `errors.log` for warnings)
  3. The job's `last_run` metadata via `hermes cron list`


### Check 2: Common error patterns[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-2-common-error-patterns "Check 2: Common error patterns的直接链接")
**"No such file or directory" for scripts** The `script` path must be an absolute path (or relative to the Hermes config directory). Verify:

```
ls ~/.hermes/scripts/your-script.py   # Must existhermes cron edit <job_id>--script ~/.hermes/scripts/your-script.py
```

**"Skill not found" at job execution** The skill must be installed on the machine running the scheduler. If you move between machines, skills don't automatically sync — reinstall them with `hermes skills install <skill-name>`.
**Job runs but delivers nothing** Likely a delivery target issue (see Delivery Failures above) or a silently suppressed response (`[SILENT]`).
**Job hangs or times out** The scheduler uses an inactivity-based timeout (default 600s, configurable via `HERMES_CRON_TIMEOUT` env var, `0` for unlimited). The agent can run as long as it's actively calling tools — the timer only fires after sustained inactivity. Long-running jobs should use scripts to handle data collection and deliver only the result.
### Check 3: Lock contention[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-3-lock-contention "Check 3: Lock contention的直接链接")
The scheduler uses file-based locking to prevent overlapping ticks. If two gateway instances are running (or a CLI session conflicts with a gateway), jobs may be delayed or skipped.
Kill duplicate gateway processes:

```
ps aux |grep hermes# Kill duplicate processes, keep only one
```

### Check 4: Permissions on jobs.json[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-4-permissions-on-jobsjson "Check 4: Permissions on jobs.json的直接链接")
Jobs are stored in `~/.hermes/cron/jobs.json`. If this file is not readable/writable by your user, the scheduler will fail silently:

```
ls-la ~/.hermes/cron/jobs.jsonchmod600 ~/.hermes/cron/jobs.json   # Your user should own it
```

## Performance Issues[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#performance-issues "Performance Issues的直接链接")
### Slow job startup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#slow-job-startup "Slow job startup的直接链接")
Each cron job creates a fresh AIAgent session, which may involve provider authentication and model loading. For time-sensitive schedules, add buffer time (e.g., `0 8 * * *` instead of `0 9 * * *`).
### Too many overlapping jobs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#too-many-overlapping-jobs "Too many overlapping jobs的直接链接")
The scheduler executes jobs sequentially within each tick. If multiple jobs are due at the same time, they run one after another. Consider staggering schedules (e.g., `0 9 * * *` and `5 9 * * *` instead of both at `0 9 * * *`) to avoid delays.
### Large script output[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#large-script-output "Large script output的直接链接")
Scripts that dump megabytes of output will slow down the agent and may hit token limits. Filter/summarize at the script level — emit only what the agent needs to reason about.
## Diagnostic Commands[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#diagnostic-commands "Diagnostic Commands的直接链接")

```
hermes cron list                    # Show all jobs, states, next_run timeshermes cron run <job_id># Schedule for next tick (for testing)hermes cron edit <job_id># Fix configuration issueshermes logs                         # View recent Hermes logshermes skills list                  # Verify installed skills
```

## Getting More Help[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#getting-more-help "Getting More Help的直接链接")
If you've worked through this guide and the issue persists:
  1. Run the job with `hermes cron run <job_id>` (fires on next gateway tick) and watch for errors in the chat output
  2. Check `~/.hermes/logs/agent.log` for scheduler messages and `~/.hermes/logs/errors.log` for warnings
  3. Open an issue at [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) with: 
     * The job ID and schedule
     * The delivery target
     * What you expected vs. what happened
     * Relevant error messages from the logs


_For the complete cron reference, see[Automate Anything with Cron](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/automate-with-cron) and [Scheduled Tasks (Cron)](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/cron)._
  * [Jobs Not Firing](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#jobs-not-firing)
    * [Check 1: Verify the job exists and is active](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-1-verify-the-job-exists-and-is-active)
    * [Check 2: Confirm the schedule is correct](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-2-confirm-the-schedule-is-correct)
    * [Check 3: Is the gateway running?](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-3-is-the-gateway-running)
    * [Check 4: Check the system clock and timezone](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-4-check-the-system-clock-and-timezone)
  * [Delivery Failures](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#delivery-failures)
    * [Check 1: Verify the deliver target is correct](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-1-verify-the-deliver-target-is-correct)
    * [Check 2: Check `[SILENT]` usage](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-2-check-silent-usage)
    * [Check 3: Platform token permissions](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-3-platform-token-permissions)
    * [Check 4: Response wrapping](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-4-response-wrapping)
  * [Skill Loading Failures](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#skill-loading-failures)
    * [Check 1: Verify skills are installed](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-1-verify-skills-are-installed)
    * [Check 2: Check skill name vs. skill folder name](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-2-check-skill-name-vs-skill-folder-name)
    * [Check 3: Skills that require interactive tools](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-3-skills-that-require-interactive-tools)
    * [Check 4: Multi-skill ordering](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-4-multi-skill-ordering)
  * [Job Errors and Failures](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#job-errors-and-failures)
    * [Check 1: Review recent job output](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-1-review-recent-job-output)
    * [Check 2: Common error patterns](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-2-common-error-patterns)
    * [Check 3: Lock contention](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-3-lock-contention)
    * [Check 4: Permissions on jobs.json](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#check-4-permissions-on-jobsjson)
  * [Performance Issues](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#performance-issues)
    * [Slow job startup](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#slow-job-startup)
    * [Too many overlapping jobs](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#too-many-overlapping-jobs)
    * [Large script output](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#large-script-output)
  * [Diagnostic Commands](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#diagnostic-commands)
  * [Getting More Help](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-troubleshooting#getting-more-help)


