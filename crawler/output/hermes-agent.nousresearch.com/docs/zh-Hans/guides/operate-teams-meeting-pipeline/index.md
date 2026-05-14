<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline -->

本页总览
Use this guide after you have already enabled the feature from [Teams Meetings](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/teams-meetings).
This page covers:
  * operator CLI flows
  * routine subscription maintenance
  * failure triage
  * go-live checks
  * rollout worksheet


## Core Operator Commands[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#core-operator-commands "Core Operator Commands的直接链接")
### Validate the config snapshot[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#validate-the-config-snapshot "Validate the config snapshot的直接链接")

```
hermes teams-pipeline validate
```

Use this first after any config change.
### Inspect token health[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#inspect-token-health "Inspect token health的直接链接")

```
hermes teams-pipeline token-healthhermes teams-pipeline token-health --force-refresh
```

Use `--force-refresh` when you suspect stale auth state.
### Inspect subscriptions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#inspect-subscriptions "Inspect subscriptions的直接链接")

```
hermes teams-pipeline subscriptions
```

### Renew near-expiry subscriptions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#renew-near-expiry-subscriptions "Renew near-expiry subscriptions的直接链接")

```
hermes teams-pipeline maintain-subscriptionshermes teams-pipeline maintain-subscriptions --dry-run
```

### Automating subscription renewal (REQUIRED for production)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#automating-subscription-renewal-required-for-production "Automating subscription renewal \(REQUIRED for production\)的直接链接")
**Microsoft Graph subscriptions expire in at most 72 hours.** If nothing renews them, meeting notifications silently stop after 3 days and the pipeline looks "broken." This is the #1 operational failure mode for any Graph-backed integration.
You MUST run `maintain-subscriptions` on a schedule. Pick one of these three options:
#### Option 1: Hermes cron (recommended if you already run the Hermes gateway)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#option-1-hermes-cron-recommended-if-you-already-run-the-hermes-gateway "Option 1: Hermes cron \(recommended if you already run the Hermes gateway\)的直接链接")
Hermes ships a built-in cron scheduler. The `--no-agent` mode runs a script as the job (rather than using an LLM), and `--script` must point at a file under `~/.hermes/scripts/`. First create the script:

```
mkdir-p ~/.hermes/scriptscat> ~/.hermes/scripts/maintain-teams-subscriptions.sh <<'EOF'#!/usr/bin/env bashexec hermes teams-pipeline maintain-subscriptionsEOFchmod +x ~/.hermes/scripts/maintain-teams-subscriptions.sh
```

Then register a script-only cron job that runs every 12 hours (gives 6x headroom against the 72h expiry window):

```
hermes cron create "0 */12 * * *"\--name"teams-pipeline-maintain-subscriptions"\  --no-agent \--script maintain-teams-subscriptions.sh \--deliverlocal
```

Verify it was registered and inspect the next run time:

```
hermes cron listhermes cron status        # scheduler status
```

#### Option 2: systemd timer (recommended for Linux production deployments)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#option-2-systemd-timer-recommended-for-linux-production-deployments "Option 2: systemd timer \(recommended for Linux production deployments\)的直接链接")
Create `/etc/systemd/system/hermes-teams-pipeline-maintain.service`:

```
[Unit]Description=Hermes Teams pipeline subscription maintenanceAfter=network-online.target[Service]Type=oneshotUser=hermesEnvironmentFile=/etc/hermes/envExecStart=/usr/local/bin/hermes teams-pipeline maintain-subscriptions
```

And `/etc/systemd/system/hermes-teams-pipeline-maintain.timer`:

```
[Unit]Description=Run Hermes Teams pipeline subscription maintenance every 12 hours[Timer]OnBootSec=5minOnUnitActiveSec=12hPersistent=true[Install]WantedBy=timers.target
```

Enable:

```
sudo systemctl daemon-reloadsudo systemctl enable--now hermes-teams-pipeline-maintain.timersystemctl list-timers hermes-teams-pipeline-maintain.timer
```

#### Option 3: Plain crontab[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#option-3-plain-crontab "Option 3: Plain crontab的直接链接")

```
0 */12 * * * /usr/local/bin/hermes teams-pipeline maintain-subscriptions >> /var/log/hermes/teams-pipeline-maintain.log 2>&1
```

Make sure the cron environment has the `MSGRAPH_*` credentials. Simplest fix: source `~/.hermes/.env` at the top of a wrapper script that crontab calls.
#### Verifying renewal is working[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#verifying-renewal-is-working "Verifying renewal is working的直接链接")
After you've set up the schedule, check renewal activity after the first scheduled run:

```
hermes teams-pipeline subscriptions   # should show expirationDateTime advancedhermes teams-pipeline maintain-subscriptions --dry-run   # should show "0 expiring soon" most of the time
```

If you ever see your Graph webhook mysteriously "stop working" after exactly ~72 hours, this is the first thing to check: did the renewal job actually run?
### Inspect recent jobs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#inspect-recent-jobs "Inspect recent jobs的直接链接")

```
hermes teams-pipeline listhermes teams-pipeline list --status failedhermes teams-pipeline show <job-id>
```

### Replay a stored job[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#replay-a-stored-job "Replay a stored job的直接链接")

```
hermes teams-pipeline run <job-id>
```

### Dry-run meeting artifact fetches[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#dry-run-meeting-artifact-fetches "Dry-run meeting artifact fetches的直接链接")

```
hermes teams-pipeline fetch --meeting-id <meeting-id>hermes teams-pipeline fetch --join-web-url "<join-url>"
```

## Routine Runbook[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#routine-runbook "Routine Runbook的直接链接")
### After first setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#after-first-setup "After first setup的直接链接")
Run these in order:

```
hermes teams-pipeline validatehermes teams-pipeline token-health --force-refreshhermes teams-pipeline subscriptions
```

Then trigger or wait for a real meeting event and confirm:

```
hermes teams-pipeline listhermes teams-pipeline show <job-id>
```

### Daily or periodic checks[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#daily-or-periodic-checks "Daily or periodic checks的直接链接")
  * run `hermes teams-pipeline maintain-subscriptions --dry-run`
  * inspect `hermes teams-pipeline list --status failed`
  * verify the Teams delivery target is still the correct chat or channel


### Before changing webhook URLs or delivery targets[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#before-changing-webhook-urls-or-delivery-targets "Before changing webhook URLs or delivery targets的直接链接")
  * update the public notification URL or Teams target config
  * run `hermes teams-pipeline validate`
  * renew or recreate affected subscriptions
  * confirm new events land in the expected sink


## Failure Triage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#failure-triage "Failure Triage的直接链接")
### No jobs are being created[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#no-jobs-are-being-created "No jobs are being created的直接链接")
Check:
  * `msgraph_webhook` is enabled
  * the public notification URL points to `/msgraph/webhook`
  * the client state in the subscription matches `MSGRAPH_WEBHOOK_CLIENT_STATE`
  * subscriptions still exist remotely and are not expired


### Jobs stay in retry or fail before summarization[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#jobs-stay-in-retry-or-fail-before-summarization "Jobs stay in retry or fail before summarization的直接链接")
Check:
  * transcript permissions and availability
  * recording permissions and artifact availability
  * `ffmpeg` availability if recording fallback is enabled
  * Graph token health


### Summaries are produced but not delivered to Teams[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#summaries-are-produced-but-not-delivered-to-teams "Summaries are produced but not delivered to Teams的直接链接")
Check:
  * `platforms.teams.enabled: true`
  * `delivery_mode`
  * `incoming_webhook_url` for webhook mode
  * `chat_id` or `team_id` plus `channel_id` for Graph mode
  * Teams auth config if Graph posting is used


### Duplicate or unexpected replays[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#duplicate-or-unexpected-replays "Duplicate or unexpected replays的直接链接")
Check:
  * whether you manually replayed a job with `hermes teams-pipeline run`
  * whether the sink record already exists for that meeting
  * whether you intentionally enabled a resend path in your local config


## Go-Live Checklist[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#go-live-checklist "Go-Live Checklist的直接链接")
  * Graph credentials are present and correct
  * `msgraph_webhook` is enabled and reachable from the public internet
  * `MSGRAPH_WEBHOOK_CLIENT_STATE` is set and matches subscriptions
  * transcript subscription is created
  * recording subscription is created if STT fallback is required
  * `ffmpeg` is installed if recording fallback is enabled
  * Teams outbound delivery target is configured and verified
  * Notion and Linear sinks are configured only if actually needed
  * `hermes teams-pipeline validate` returns an OK snapshot
  * `hermes teams-pipeline token-health --force-refresh` succeeds
  * **`maintain-subscriptions`is scheduled** (Hermes cron, systemd timer, or crontab — see [Automating subscription renewal](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#automating-subscription-renewal-required-for-production)). Without this, Graph subscriptions silently expire within 72 hours.
  * a real end-to-end meeting event has produced a stored job
  * at least one summary has reached the intended delivery sink


## Delivery-Mode Decision Guide[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#delivery-mode-decision-guide "Delivery-Mode Decision Guide的直接链接")  
| Mode  | Use when  | Tradeoff  |  
| --- | --- | --- |  
| `incoming_webhook`  | you only need simple posting into Teams  | simplest setup, less control  |  
| `graph`  | you need channel or chat posting through Graph  | more control, more auth and target config  |  
## Operator Worksheet[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#operator-worksheet "Operator Worksheet的直接链接")
Fill this out before rollout:  
| Item  | Value  |  
| --- | --- |  
| Public notification URL  |  
| Graph tenant ID  |  
| Graph client ID  |  
| Webhook client state  |  
| Transcript resource subscription  |  
| Recording resource subscription  |  
| Teams delivery mode  |  
| Teams chat ID or team/channel  |  
| Notion database ID  |  
| Linear team ID  |  
| Store path override, if any  |  
| Owner for daily checks  |  
## Change Review Worksheet[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#change-review-worksheet "Change Review Worksheet的直接链接")
Use this before changing the deployment:  
| Question  | Answer  |  
| --- | --- |  
| Are we changing the public webhook URL?  |  
| Are we rotating Graph credentials?  |  
| Are we changing Teams delivery mode?  |  
| Are we moving to a new Teams chat or channel?  |  
| Do subscriptions need to be recreated or renewed?  |  
| Do we need a fresh end-to-end verification run?  |  
## Related Docs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#related-docs "Related Docs的直接链接")
  * [Teams Meetings setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/teams-meetings)
  * [Microsoft Teams bot setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/teams)


  * [Core Operator Commands](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#core-operator-commands)
    * [Validate the config snapshot](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#validate-the-config-snapshot)
    * [Inspect token health](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#inspect-token-health)
    * [Inspect subscriptions](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#inspect-subscriptions)
    * [Renew near-expiry subscriptions](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#renew-near-expiry-subscriptions)
    * [Automating subscription renewal (REQUIRED for production)](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#automating-subscription-renewal-required-for-production)
    * [Inspect recent jobs](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#inspect-recent-jobs)
    * [Replay a stored job](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#replay-a-stored-job)
    * [Dry-run meeting artifact fetches](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#dry-run-meeting-artifact-fetches)
  * [Routine Runbook](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#routine-runbook)
    * [After first setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#after-first-setup)
    * [Daily or periodic checks](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#daily-or-periodic-checks)
    * [Before changing webhook URLs or delivery targets](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#before-changing-webhook-urls-or-delivery-targets)
  * [Failure Triage](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#failure-triage)
    * [No jobs are being created](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#no-jobs-are-being-created)
    * [Jobs stay in retry or fail before summarization](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#jobs-stay-in-retry-or-fail-before-summarization)
    * [Summaries are produced but not delivered to Teams](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#summaries-are-produced-but-not-delivered-to-teams)
    * [Duplicate or unexpected replays](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#duplicate-or-unexpected-replays)
  * [Go-Live Checklist](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#go-live-checklist)
  * [Delivery-Mode Decision Guide](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#delivery-mode-decision-guide)
  * [Operator Worksheet](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#operator-worksheet)
  * [Change Review Worksheet](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#change-review-worksheet)
  * [Related Docs](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline#related-docs)


