<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks -->

本页总览
Receive events from external services (GitHub, GitLab, JIRA, Stripe, etc.) and trigger Hermes agent runs automatically. The webhook adapter runs an HTTP server that accepts POST requests, validates HMAC signatures, transforms payloads into agent prompts, and routes responses back to the source or to another configured platform.
The agent processes the event and can respond by posting comments on PRs, sending messages to Telegram/Discord, or logging the result.
## Video Tutorial[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#video-tutorial "Video Tutorial的直接链接")
## Quick Start[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#quick-start "Quick Start的直接链接")
  1. Enable via `hermes gateway setup` or environment variables
  2. Define routes in `config.yaml` **or** create them dynamically with `hermes webhook subscribe`
  3. Point your service at `http://your-server:8644/webhooks/<route-name>`


## Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#setup "Setup的直接链接")
There are two ways to enable the webhook adapter.
### Via setup wizard[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#via-setup-wizard "Via setup wizard的直接链接")

```
hermes gateway setup
```

Follow the prompts to enable webhooks, set the port, and set a global HMAC secret.
### Via environment variables[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#via-environment-variables "Via environment variables的直接链接")
Add to `~/.hermes/.env`:

```
WEBHOOK_ENABLED=trueWEBHOOK_PORT=8644# defaultWEBHOOK_SECRET=your-global-secret
```

### Verify the server[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#verify-the-server "Verify the server的直接链接")
Once the gateway is running:

```
curl http://localhost:8644/health
```

Expected response:

```
{"status":"ok","platform":"webhook"}
```

## Configuring Routes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#configuring-routes "Configuring Routes的直接链接")
Routes define how different webhook sources are handled. Each route is a named entry under `platforms.webhook.extra.routes` in your `config.yaml`.
### Route properties[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#route-properties "Route properties的直接链接")  
| Property  | Required  | Description  |  
| --- | --- | --- |  
| `events`  | No  | List of event types to accept (e.g. `["pull_request"]`). If empty, all events are accepted. Event type is read from `X-GitHub-Event`, `X-GitLab-Event`, or `event_type` in the payload.  |  
| `secret`  | **Yes**  | HMAC secret for signature validation. Falls back to the global `secret` if not set on the route. Set to `"INSECURE_NO_AUTH"` for testing only (skips validation).  |  
| `prompt`  | No  | Template string with dot-notation payload access (e.g. `{pull_request.title}`). If omitted, the full JSON payload is dumped into the prompt.  |  
| `skills`  | No  | List of skill names to load for the agent run.  |  
| `deliver`  | No  | Where to send the response: `github_comment`, `telegram`, `discord`, `slack`, `signal`, `sms`, `whatsapp`, `matrix`, `mattermost`, `homeassistant`, `email`, `dingtalk`, `feishu`, `wecom`, `weixin`, `bluebubbles`, `qqbot`, or `log` (default).  |  
| `deliver_extra`  | No  | Additional delivery config — keys depend on `deliver` type (e.g. `repo`, `pr_number`, `chat_id`). Values support the same `{dot.notation}` templates as `prompt`.  |  
| `deliver_only`  | No  | If `true`, skip the agent entirely — the rendered `prompt` template becomes the literal message that gets delivered. Zero LLM cost, sub-second delivery. See [Direct Delivery Mode](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#direct-delivery-mode) for use cases. Requires `deliver` to be a real target (not `log`).  |  
### Full example[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#full-example "Full example的直接链接")

```
platforms:webhook:enabled:trueextra:port:8644secret:"global-fallback-secret"routes:github-pr:events:["pull_request"]secret:"github-webhook-secret"prompt:|            Review this pull request:            Repository: {repository.full_name}            PR #{number}: {pull_request.title}            Author: {pull_request.user.login}            URL: {pull_request.html_url}            Diff URL: {pull_request.diff_url}            Action: {action}skills:["github-code-review"]deliver:"github_comment"deliver_extra:repo:"{repository.full_name}"pr_number:"{number}"deploy-notify:events:["push"]secret:"deploy-secret"prompt:"New push to {repository.full_name} branch {ref}: {head_commit.message}"deliver:"telegram"
```

### Prompt Templates[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#prompt-templates "Prompt Templates的直接链接")
Prompts use dot-notation to access nested fields in the webhook payload:
  * `{pull_request.title}` resolves to `payload["pull_request"]["title"]`
  * `{repository.full_name}` resolves to `payload["repository"]["full_name"]`
  * `{__raw__}` — special token that dumps the **entire payload** as indented JSON (truncated at 4000 characters). Useful for monitoring alerts or generic webhooks where the agent needs the full context.
  * Missing keys are left as the literal `{key}` string (no error)
  * Nested dicts and lists are JSON-serialized and truncated at 2000 characters


You can mix `{__raw__}` with regular template variables:

```
prompt:"PR #{pull_request.number} by {pull_request.user.login}: {__raw__}"
```

If no `prompt` template is configured for a route, the entire payload is dumped as indented JSON (truncated at 4000 characters).
The same dot-notation templates work in `deliver_extra` values.
### Forum Topic Delivery[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#forum-topic-delivery "Forum Topic Delivery的直接链接")
When delivering webhook responses to Telegram, you can target a specific forum topic by including `message_thread_id` (or `thread_id`) in `deliver_extra`:

```
webhooks:routes:alerts:events:["alert"]prompt:"Alert: {__raw__}"deliver:"telegram"deliver_extra:chat_id:"-1001234567890"message_thread_id:"42"
```

If `chat_id` is not provided in `deliver_extra`, the delivery falls back to the home channel configured for the target platform.
## GitHub PR Review (Step by Step)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#github-pr-review "GitHub PR Review \(Step by Step\)的直接链接")
This walkthrough sets up automatic code review on every pull request.
### 1. Create the webhook in GitHub[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#1-create-the-webhook-in-github "1. Create the webhook in GitHub的直接链接")
  1. Go to your repository → **Settings** → **Webhooks** → **Add webhook**
  2. Set **Payload URL** to `http://your-server:8644/webhooks/github-pr`
  3. Set **Content type** to `application/json`
  4. Set **Secret** to match your route config (e.g. `github-webhook-secret`)
  5. Under **Which events?** , select **Let me select individual events** and check **Pull requests**
  6. Click **Add webhook**


### 2. Add the route config[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#2-add-the-route-config "2. Add the route config的直接链接")
Add the `github-pr` route to your `~/.hermes/config.yaml` as shown in the example above.
### 3. Ensure `gh` CLI is authenticated[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#3-ensure-gh-cli-is-authenticated "3-ensure-gh-cli-is-authenticated的直接链接")
The `github_comment` delivery type uses the GitHub CLI to post comments:

```
gh auth login
```

### 4. Test it[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#4-test-it "4. Test it的直接链接")
Open a pull request on the repository. The webhook fires, Hermes processes the event, and posts a review comment on the PR.
## GitLab Webhook Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#gitlab-webhook-setup "GitLab Webhook Setup的直接链接")
GitLab webhooks work similarly but use a different authentication mechanism. GitLab sends the secret as a plain `X-Gitlab-Token` header (exact string match, not HMAC).
### 1. Create the webhook in GitLab[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#1-create-the-webhook-in-gitlab "1. Create the webhook in GitLab的直接链接")
  1. Go to your project → **Settings** → **Webhooks**
  2. Set the **URL** to `http://your-server:8644/webhooks/gitlab-mr`
  3. Enter your **Secret token**
  4. Select **Merge request events** (and any other events you want)
  5. Click **Add webhook**


### 2. Add the route config[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#2-add-the-route-config-1 "2. Add the route config的直接链接")

```
platforms:webhook:enabled:trueextra:routes:gitlab-mr:events:["merge_request"]secret:"your-gitlab-secret-token"prompt:|            Review this merge request:            Project: {project.path_with_namespace}            MR !{object_attributes.iid}: {object_attributes.title}            Author: {object_attributes.last_commit.author.name}            URL: {object_attributes.url}            Action: {object_attributes.action}deliver:"log"
```

## Delivery Options[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#delivery-options "Delivery Options的直接链接")
The `deliver` field controls where the agent's response goes after processing the webhook event.  
| Deliver Type  | Description  |  
| --- | --- |  
| `log`  | Logs the response to the gateway log output. This is the default and is useful for testing.  |  
| `github_comment`  | Posts the response as a PR/issue comment via the `gh` CLI. Requires `deliver_extra.repo` and `deliver_extra.pr_number`. The `gh` CLI must be installed and authenticated on the gateway host (`gh auth login`).  |  
| `telegram`  | Routes the response to Telegram. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `discord`  | Routes the response to Discord. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `slack`  | Routes the response to Slack. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `signal`  | Routes the response to Signal. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `sms`  | Routes the response to SMS via Twilio. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `whatsapp`  | Routes the response to WhatsApp. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `matrix`  | Routes the response to Matrix. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `mattermost`  | Routes the response to Mattermost. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `homeassistant`  | Routes the response to Home Assistant. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `email`  | Routes the response to Email. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `dingtalk`  | Routes the response to DingTalk. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `feishu`  | Routes the response to Feishu/Lark. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `wecom`  | Routes the response to WeCom. Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `weixin`  | Routes the response to Weixin (WeChat). Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
| `bluebubbles`  | Routes the response to BlueBubbles (iMessage). Uses the home channel, or specify `chat_id` in `deliver_extra`.  |  
For cross-platform delivery, the target platform must also be enabled and connected in the gateway. If no `chat_id` is provided in `deliver_extra`, the response is sent to that platform's configured home channel.
## Direct Delivery Mode[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#direct-delivery-mode "Direct Delivery Mode的直接链接")
By default, every webhook POST triggers an agent run — the payload becomes a prompt, the agent processes it, and the agent's response is delivered. This costs LLM tokens on every event.
For use cases where you just want to **push a plain notification** — no reasoning, no agent loop, just deliver the message — set `deliver_only: true` on the route. The rendered `prompt` template becomes the literal message body, and the adapter dispatches it directly to the configured delivery target.
### When to use direct delivery[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#when-to-use-direct-delivery "When to use direct delivery的直接链接")
  * **External service push** — Supabase/Firebase webhook fires on a database change → notify a user in Telegram instantly
  * **Monitoring alerts** — Datadog/Grafana alert webhook → push to a Discord channel
  * **Inter-agent pings** — Agent A notifies Agent B's user that a long-running task finished
  * **Background job completion** — Cron job finishes → post result to Slack


Benefits:
  * **Zero LLM tokens** — the agent is never invoked
  * **Sub-second delivery** — a single adapter call, no reasoning loop
  * **Same security as agent mode** — HMAC auth, rate limits, idempotency, and body-size limits all still apply
  * **Synchronous response** — the POST returns `200 OK` once delivery succeeds, or `502` if the target rejects it, so your upstream service can retry intelligently


### Example: Telegram push from Supabase[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#example-telegram-push-from-supabase "Example: Telegram push from Supabase的直接链接")

```
platforms:webhook:enabled:trueextra:port:8644secret:"global-secret"routes:antenna-matches:secret:"antenna-webhook-secret"deliver:"telegram"deliver_only:trueprompt:"🎉 New match: {match.user_name} matched with you!"deliver_extra:chat_id:"{match.telegram_chat_id}"
```

Your Supabase edge function signs the payload with HMAC-SHA256 and POSTs to `https://your-server:8644/webhooks/antenna-matches`. The webhook adapter validates the signature, renders the template from the payload, delivers to Telegram, and returns `200 OK`.
### Example: Dynamic subscription via CLI[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#example-dynamic-subscription-via-cli "Example: Dynamic subscription via CLI的直接链接")

```
hermes webhook subscribe antenna-matches \--deliver telegram \  --deliver-chat-id "123456789"\  --deliver-only \--prompt"🎉 New match: {match.user_name} matched with you!"\--description"Antenna match notifications"
```

### Response codes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#response-codes "Response codes的直接链接")  
| Status  | Meaning  |  
| --- | --- |  
| `200 OK`  | Delivered successfully. Body: `{"status": "delivered", "route": "...", "target": "...", "delivery_id": "..."}`  |  
|  `200 OK` (status=duplicate)  | Duplicate `X-GitHub-Delivery` ID within the idempotency TTL (1 hour). Not re-delivered.  |  
| `401 Unauthorized`  | HMAC signature invalid or missing.  |  
| `400 Bad Request`  | Malformed JSON body.  |  
| `404 Not Found`  | Unknown route name.  |  
| `413 Payload Too Large`  | Body exceeded `max_body_bytes`.  |  
| `429 Too Many Requests`  | Route rate limit exceeded.  |  
| `502 Bad Gateway`  | Target adapter rejected the message or raised. The error is logged server-side; the response body is a generic `Delivery failed` to avoid leaking adapter internals.  |  
### Configuration gotchas[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#configuration-gotchas "Configuration gotchas的直接链接")
  * `deliver_only: true` requires `deliver` to be a real target. `deliver: log` (or omitting `deliver`) is rejected at startup — the adapter refuses to start if it finds a misconfigured route.
  * The `skills` field is ignored in direct delivery mode (no agent runs, so there's nothing to inject skills into).
  * Template rendering uses the same `{dot.notation}` syntax as agent mode, including the `{__raw__}` token.
  * Idempotency uses the same `X-GitHub-Delivery` / `X-Request-ID` header — retries with the same ID return `status=duplicate` and do NOT re-deliver.


## Dynamic Subscriptions (CLI)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#dynamic-subscriptions "Dynamic Subscriptions \(CLI\)的直接链接")
In addition to static routes in `config.yaml`, you can create webhook subscriptions dynamically using the `hermes webhook` CLI command. This is especially useful when the agent itself needs to set up event-driven triggers.
### Create a subscription[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#create-a-subscription "Create a subscription的直接链接")

```
hermes webhook subscribe github-issues \--events"issues"\--prompt"New issue #{issue.number}: {issue.title}\nBy: {issue.user.login}\n\n{issue.body}"\--deliver telegram \  --deliver-chat-id "-100123456789"\--description"Triage new GitHub issues"
```

This returns the webhook URL and an auto-generated HMAC secret. Configure your service to POST to that URL.
### List subscriptions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#list-subscriptions "List subscriptions的直接链接")

```
hermes webhook list
```

### Remove a subscription[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#remove-a-subscription "Remove a subscription的直接链接")

```
hermes webhook remove github-issues
```

### Test a subscription[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#test-a-subscription "Test a subscription的直接链接")

```
hermes webhook test github-issueshermes webhook test github-issues --payload'{"issue": {"number": 42, "title": "Test"}}'
```

### How dynamic subscriptions work[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#how-dynamic-subscriptions-work "How dynamic subscriptions work的直接链接")
  * Subscriptions are stored in `~/.hermes/webhook_subscriptions.json`
  * The webhook adapter hot-reloads this file on each incoming request (mtime-gated, negligible overhead)
  * Static routes from `config.yaml` always take precedence over dynamic ones with the same name
  * Dynamic subscriptions use the same route format and capabilities as static routes (events, prompt templates, skills, delivery)
  * No gateway restart required — subscribe and it's immediately live


### Agent-driven subscriptions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#agent-driven-subscriptions "Agent-driven subscriptions的直接链接")
The agent can create subscriptions via the terminal tool when guided by the `webhook-subscriptions` skill. Ask the agent to "set up a webhook for GitHub issues" and it will run the appropriate `hermes webhook subscribe` command.
## Security[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#security "Security的直接链接")
The webhook adapter includes multiple layers of security:
### HMAC signature validation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#hmac-signature-validation "HMAC signature validation的直接链接")
The adapter validates incoming webhook signatures using the appropriate method for each source:
  * **GitHub** : `X-Hub-Signature-256` header — HMAC-SHA256 hex digest prefixed with `sha256=`
  * **GitLab** : `X-Gitlab-Token` header — plain secret string match
  * **Generic** : `X-Webhook-Signature` header — raw HMAC-SHA256 hex digest


If a secret is configured but no recognized signature header is present, the request is rejected.
### Secret is required[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#secret-is-required "Secret is required的直接链接")
Every route must have a secret — either set directly on the route or inherited from the global `secret`. Routes without a secret cause the adapter to fail at startup with an error. For development/testing only, you can set the secret to `"INSECURE_NO_AUTH"` to skip validation entirely.
`INSECURE_NO_AUTH` is only accepted when the gateway is bound to a loopback host (`127.0.0.1`, `localhost`, `::1`). If it is combined with a non-loopback bind such as `0.0.0.0` or a LAN IP, the adapter refuses to start — this prevents accidentally exposing an unauthenticated endpoint on a public interface.
### Rate limiting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#rate-limiting "Rate limiting的直接链接")
Each route is rate-limited to **30 requests per minute** by default (fixed-window). Configure this globally:

```
platforms:webhook:extra:rate_limit:60# requests per minute
```

Requests exceeding the limit receive a `429 Too Many Requests` response.
### Idempotency[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#idempotency "Idempotency的直接链接")
Delivery IDs (from `X-GitHub-Delivery`, `X-Request-ID`, or a timestamp fallback) are cached for **1 hour**. Duplicate deliveries (e.g. webhook retries) are silently skipped with a `200` response, preventing duplicate agent runs.
### Body size limits[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#body-size-limits "Body size limits的直接链接")
Payloads exceeding **1 MB** are rejected before the body is read. Configure this:

```
platforms:webhook:extra:max_body_bytes:2097152# 2 MB
```

### Prompt injection risk[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#prompt-injection-risk "Prompt injection risk的直接链接")
Webhook payloads contain attacker-controlled data — PR titles, commit messages, issue descriptions, etc. can all contain malicious instructions. Run the gateway in a sandboxed environment (Docker, VM) when exposed to the internet. Consider using the Docker or SSH terminal backend for isolation.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#troubleshooting "Troubleshooting的直接链接")
### Webhook not arriving[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#webhook-not-arriving "Webhook not arriving的直接链接")
  * Verify the port is exposed and accessible from the webhook source
  * Check firewall rules — port `8644` (or your configured port) must be open
  * Verify the URL path matches: `http://your-server:8644/webhooks/<route-name>`
  * Use the `/health` endpoint to confirm the server is running


### Signature validation failing[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#signature-validation-failing "Signature validation failing的直接链接")
  * Ensure the secret in your route config exactly matches the secret configured in the webhook source
  * For GitHub, the secret is HMAC-based — check `X-Hub-Signature-256`
  * For GitLab, the secret is a plain token match — check `X-Gitlab-Token`
  * Check gateway logs for `Invalid signature` warnings


### Event being ignored[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#event-being-ignored "Event being ignored的直接链接")
  * Check that the event type is in your route's `events` list
  * GitHub events use values like `pull_request`, `push`, `issues` (the `X-GitHub-Event` header value)
  * GitLab events use values like `merge_request`, `push` (the `X-GitLab-Event` header value)
  * If `events` is empty or not set, all events are accepted


### Agent not responding[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#agent-not-responding "Agent not responding的直接链接")
  * Run the gateway in foreground to see logs: `hermes gateway run`
  * Check that the prompt template is rendering correctly
  * Verify the delivery target is configured and connected


### Duplicate responses[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#duplicate-responses "Duplicate responses的直接链接")
  * The idempotency cache should prevent this — check that the webhook source is sending a delivery ID header (`X-GitHub-Delivery` or `X-Request-ID`)
  * Delivery IDs are cached for 1 hour


###  `gh` CLI errors (GitHub comment delivery)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#gh-cli-errors-github-comment-delivery "gh-cli-errors-github-comment-delivery的直接链接")
  * Run `gh auth login` on the gateway host
  * Ensure the authenticated GitHub user has write access to the repository
  * Check that `gh` is installed and on the PATH


## Environment Variables[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#environment-variables "Environment Variables的直接链接")  
| Variable  | Description  | Default  |  
| --- | --- | --- |  
| `WEBHOOK_ENABLED`  | Enable the webhook platform adapter  | `false`  |  
| `WEBHOOK_PORT`  | HTTP server port for receiving webhooks  | `8644`  |  
| `WEBHOOK_SECRET`  | Global HMAC secret (used as fallback when routes don't specify their own)  | _(none)_  |  
  * [Video Tutorial](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#video-tutorial)
  * [Quick Start](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#quick-start)
  * [Setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#setup)
    * [Via setup wizard](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#via-setup-wizard)
    * [Via environment variables](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#via-environment-variables)
    * [Verify the server](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#verify-the-server)
  * [Configuring Routes](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#configuring-routes)
    * [Route properties](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#route-properties)
    * [Full example](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#full-example)
    * [Prompt Templates](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#prompt-templates)
    * [Forum Topic Delivery](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#forum-topic-delivery)
  * [GitHub PR Review (Step by Step)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#github-pr-review)
    * [1. Create the webhook in GitHub](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#1-create-the-webhook-in-github)
    * [2. Add the route config](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#2-add-the-route-config)
    * [3. Ensure `gh` CLI is authenticated](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#3-ensure-gh-cli-is-authenticated)
  * [GitLab Webhook Setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#gitlab-webhook-setup)
    * [1. Create the webhook in GitLab](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#1-create-the-webhook-in-gitlab)
    * [2. Add the route config](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#2-add-the-route-config-1)
  * [Delivery Options](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#delivery-options)
  * [Direct Delivery Mode](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#direct-delivery-mode)
    * [When to use direct delivery](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#when-to-use-direct-delivery)
    * [Example: Telegram push from Supabase](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#example-telegram-push-from-supabase)
    * [Example: Dynamic subscription via CLI](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#example-dynamic-subscription-via-cli)
    * [Response codes](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#response-codes)
    * [Configuration gotchas](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#configuration-gotchas)
  * [Dynamic Subscriptions (CLI)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#dynamic-subscriptions)
    * [Create a subscription](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#create-a-subscription)
    * [List subscriptions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#list-subscriptions)
    * [Remove a subscription](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#remove-a-subscription)
    * [Test a subscription](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#test-a-subscription)
    * [How dynamic subscriptions work](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#how-dynamic-subscriptions-work)
    * [Agent-driven subscriptions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#agent-driven-subscriptions)
  * [Security](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#security)
    * [HMAC signature validation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#hmac-signature-validation)
    * [Secret is required](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#secret-is-required)
    * [Rate limiting](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#rate-limiting)
    * [Idempotency](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#idempotency)
    * [Body size limits](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#body-size-limits)
    * [Prompt injection risk](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#prompt-injection-risk)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#troubleshooting)
    * [Webhook not arriving](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#webhook-not-arriving)
    * [Signature validation failing](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#signature-validation-failing)
    * [Event being ignored](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#event-being-ignored)
    * [Agent not responding](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#agent-not-responding)
    * [Duplicate responses](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#duplicate-responses)
    * [`gh` CLI errors (GitHub comment delivery)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#gh-cli-errors-github-comment-delivery)
  * [Environment Variables](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/webhooks#environment-variables)


