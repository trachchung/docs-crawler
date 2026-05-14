<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings -->

本页总览
Use the Teams meeting pipeline when you want Hermes to ingest Microsoft Graph meeting events, fetch transcripts first, fall back to recordings plus STT when needed, and deliver a structured summary to downstream sinks.
This page focuses on setup and enablement:
  * Graph credentials
  * webhook listener configuration
  * Teams delivery modes
  * pipeline config shape


For day-2 operations, go-live checks, and the operator worksheet, use the dedicated guide: [Operate the Teams Meeting Pipeline](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/operate-teams-meeting-pipeline).
## What This Feature Does[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#what-this-feature-does "What This Feature Does的直接链接")
The pipeline:
  1. receives Microsoft Graph webhook events
  2. resolves the meeting and prefers transcript artifacts first
  3. falls back to recording download plus STT when no usable transcript is available
  4. stores durable job state and sink records locally
  5. can write summaries to Notion, Linear, and Microsoft Teams


Operator actions stay in the CLI (the `teams-pipeline` subcommand is registered by the `teams_pipeline` plugin — enable it via `hermes plugins enable teams_pipeline` or set `plugins.enabled: [teams_pipeline]` in `config.yaml`):

```
hermes teams-pipeline validatehermes teams-pipeline listhermes teams-pipeline maintain-subscriptions
```

## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#prerequisites "Prerequisites的直接链接")
Before enabling the meetings pipeline, make sure you have:
  * a working Hermes install
  * the existing [Microsoft Teams bot setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/teams) if you want Teams outbound delivery
  * Microsoft Graph application credentials with the permissions required for the meeting resources you plan to subscribe to
  * a public HTTPS URL that Microsoft Graph can call for webhook delivery
  * `ffmpeg` installed if you want recording-plus-STT fallback


## Step 1: Add Microsoft Graph Credentials[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#step-1-add-microsoft-graph-credentials "Step 1: Add Microsoft Graph Credentials的直接链接")
Add Graph app-only credentials to `~/.hermes/.env`:

```
MSGRAPH_TENANT_ID=<tenant-id>MSGRAPH_CLIENT_ID=<client-id>MSGRAPH_CLIENT_SECRET=<client-secret>
```

These credentials are used by:
  * the Graph client foundation
  * subscription maintenance commands
  * meeting resolution and artifact fetches
  * Graph-based Teams outbound delivery when you do not provide a dedicated Teams access token


## Step 2: Enable the Graph Webhook Listener[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#step-2-enable-the-graph-webhook-listener "Step 2: Enable the Graph Webhook Listener的直接链接")
The webhook listener is a gateway platform named `msgraph_webhook`. At minimum, enable it and set a client state value:

```
MSGRAPH_WEBHOOK_ENABLED=trueMSGRAPH_WEBHOOK_PORT=8646MSGRAPH_WEBHOOK_CLIENT_STATE=<random-shared-secret>MSGRAPH_WEBHOOK_ACCEPTED_RESOURCES=communications/onlineMeetings
```

The listener exposes:
  * `/msgraph/webhook` for Graph notifications
  * `/health` for a simple health check


You need to route your public HTTPS endpoint to that listener. For example, if your public domain is `https://ops.example.com`, your Graph notification URL would typically be:

```
https://ops.example.com/msgraph/webhook
```

## Step 3: Configure Teams Delivery and Pipeline Behavior[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#step-3-configure-teams-delivery-and-pipeline-behavior "Step 3: Configure Teams Delivery and Pipeline Behavior的直接链接")
The meeting pipeline reads its runtime config from the existing `teams` platform entry. Pipeline-specific knobs live under `teams.extra.meeting_pipeline`. Teams outbound delivery stays on the normal Teams platform config surface.
Example `~/.hermes/config.yaml`:

```
platforms:msgraph_webhook:enabled:trueextra:port:8646client_state:"replace-me"accepted_resources:-"communications/onlineMeetings"teams:enabled:trueextra:client_id:"your-teams-client-id"client_secret:"your-teams-client-secret"tenant_id:"your-teams-tenant-id"# outbound summary deliverydelivery_mode:"graph"# or incoming_webhookteam_id:"team-id"channel_id:"channel-id"# incoming_webhook_url: "https://..."meeting_pipeline:transcript_min_chars:80transcript_required:falsetranscription_fallback:trueffmpeg_extract_audio:truenotion:enabled:falselinear:enabled:false
```

## Teams Delivery Modes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#teams-delivery-modes "Teams Delivery Modes的直接链接")
The pipeline supports two Teams summary-delivery modes inside the existing Teams plugin.
###  `incoming_webhook`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#incoming_webhook "incoming_webhook的直接链接")
Use this when you want a simple webhook post into Teams without channel-message creation through Graph.
Required config:

```
platforms:teams:enabled:trueextra:delivery_mode:"incoming_webhook"incoming_webhook_url:"https://..."
```

###  `graph`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#graph "graph的直接链接")
Use this when you want Hermes to post the summary through Microsoft Graph into a Teams chat or channel.
Supported targets:
  * `chat_id`
  * `team_id` + `channel_id`
  * `team_id` + `home_channel` fallback for the existing Teams platform


Example:

```
platforms:teams:enabled:trueextra:delivery_mode:"graph"team_id:"team-id"channel_id:"channel-id"
```

## Step 4: Start the Gateway[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#step-4-start-the-gateway "Step 4: Start the Gateway的直接链接")
Start Hermes normally after updating config:

```
hermes gateway run
```

Or, if you run Hermes in Docker, start the gateway the same way you already do for your deployment.
Check the listener:

```
curl http://localhost:8646/health
```

## Step 5: Create Graph Subscriptions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#step-5-create-graph-subscriptions "Step 5: Create Graph Subscriptions的直接链接")
Use the plugin CLI to create and inspect subscriptions.
Examples:

```
hermes teams-pipeline subscribe \--resource communications/onlineMeetings/getAllTranscripts \  --notification-url https://ops.example.com/msgraph/webhook \  --client-state "$MSGRAPH_WEBHOOK_CLIENT_STATE"hermes teams-pipeline subscribe \--resource communications/onlineMeetings/getAllRecordings \  --notification-url https://ops.example.com/msgraph/webhook \  --client-state "$MSGRAPH_WEBHOOK_CLIENT_STATE"
```

Microsoft Graph caps webhook subscriptions at 72 hours and will not auto-renew them. You MUST schedule `hermes teams-pipeline maintain-subscriptions` before going live, or notifications will silently stop three days after any manual subscription creation. See [Automating subscription renewal](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/operate-teams-meeting-pipeline#automating-subscription-renewal-required-for-production) in the operator runbook — three options (Hermes cron, systemd timer, plain crontab).
For subscription maintenance and day-2 operator flows, continue with the guide: [Operate the Teams Meeting Pipeline](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/operate-teams-meeting-pipeline).
## Validation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#validation "Validation的直接链接")
Run the built-in validation snapshot:

```
hermes teams-pipeline validate
```

Useful companion checks:

```
hermes teams-pipeline token-healthhermes teams-pipeline subscriptions
```

## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#troubleshooting "Troubleshooting的直接链接")  
| Problem  | What to check  |  
| --- | --- |  
| Graph webhook validation fails  | Confirm the public URL is correct and reachable, and that Graph is calling the exact `/msgraph/webhook` path  |  
| Jobs do not appear in `hermes teams-pipeline list`  | Confirm `msgraph_webhook` is enabled and that subscriptions point at the right notification URL  |  
| Transcript-first never succeeds  | Check Graph permissions for transcript resources and whether the transcript artifact exists for that meeting  |  
| Recording fallback fails  | Confirm `ffmpeg` is installed and the Graph app can access recording artifacts  |  
| Teams summary delivery fails  | Re-check `delivery_mode`, target IDs, and Teams auth config  |  
## Related Docs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#related-docs "Related Docs的直接链接")
  * [Microsoft Teams bot setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/teams)
  * [Operate the Teams Meeting Pipeline](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/operate-teams-meeting-pipeline)


  * [What This Feature Does](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#what-this-feature-does)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#prerequisites)
  * [Step 1: Add Microsoft Graph Credentials](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#step-1-add-microsoft-graph-credentials)
  * [Step 2: Enable the Graph Webhook Listener](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#step-2-enable-the-graph-webhook-listener)
  * [Step 3: Configure Teams Delivery and Pipeline Behavior](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#step-3-configure-teams-delivery-and-pipeline-behavior)
  * [Teams Delivery Modes](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#teams-delivery-modes)
    * [`incoming_webhook`](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#incoming_webhook)
  * [Step 4: Start the Gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#step-4-start-the-gateway)
  * [Step 5: Create Graph Subscriptions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#step-5-create-graph-subscriptions)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#troubleshooting)
  * [Related Docs](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings#related-docs)


