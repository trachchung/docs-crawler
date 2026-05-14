<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#__docusaurus_skipToContent_fallback)
On this page
Webhook subscriptions: event-driven agent runs.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#skill-metadata "Direct link to Skill metadata")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/devops/webhook-subscriptions`  |  
| Version  | `1.1.0`  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `webhook`, `events`, `automation`, `integrations`, `notifications`, `push`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Webhook Subscriptions
Create dynamic webhook subscriptions so external services (GitHub, GitLab, Stripe, CI/CD, IoT sensors, monitoring tools) can trigger Hermes agent runs by POSTing events to a URL.
## Setup (Required First)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#setup-required-first "Direct link to Setup \(Required First\)")
The webhook platform must be enabled before subscriptions can be created. Check with:

```
hermes webhook list
```

If it says "Webhook platform is not enabled", set it up:
### Option 1: Setup wizard[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#option-1-setup-wizard "Direct link to Option 1: Setup wizard")

```
hermes gateway setup
```

Follow the prompts to enable webhooks, set the port, and set a global HMAC secret.
### Option 2: Manual config[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#option-2-manual-config "Direct link to Option 2: Manual config")
Add to `~/.hermes/config.yaml`:

```
platforms:webhook:enabled:trueextra:host:"0.0.0.0"port:8644secret:"generate-a-strong-secret-here"
```

### Option 3: Environment variables[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#option-3-environment-variables "Direct link to Option 3: Environment variables")
Add to `~/.hermes/.env`:

```
WEBHOOK_ENABLED=trueWEBHOOK_PORT=8644WEBHOOK_SECRET=generate-a-strong-secret-here
```

After configuration, start (or restart) the gateway:

```
hermes gateway run# Or if using systemd:systemctl --user restart hermes-gateway
```

Verify it's running:

```
curl http://localhost:8644/health
```

## Commands[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#commands "Direct link to Commands")
All management is via the `hermes webhook` CLI command:
### Create a subscription[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#create-a-subscription "Direct link to Create a subscription")

```
hermes webhook subscribe <name>\--prompt"Prompt template with {payload.fields}"\--events"event1,event2"\--description"What this does"\--skills"skill1,skill2"\--deliver telegram \  --deliver-chat-id "12345"\--secret"optional-custom-secret"
```

Returns the webhook URL and HMAC secret. The user configures their service to POST to that URL.
### List subscriptions[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#list-subscriptions "Direct link to List subscriptions")

```
hermes webhook list
```

### Remove a subscription[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#remove-a-subscription "Direct link to Remove a subscription")

```
hermes webhook remove <name>
```

### Test a subscription[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#test-a-subscription "Direct link to Test a subscription")

```
hermes webhook test<name>hermes webhook test<name>--payload'{"key": "value"}'
```

## Prompt Templates[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#prompt-templates "Direct link to Prompt Templates")
Prompts support `{dot.notation}` for accessing nested payload fields:
  * `{issue.title}` — GitHub issue title
  * `{pull_request.user.login}` — PR author
  * `{data.object.amount}` — Stripe payment amount
  * `{sensor.temperature}` — IoT sensor reading


If no prompt is specified, the full JSON payload is dumped into the agent prompt.
## Common Patterns[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#common-patterns "Direct link to Common Patterns")
### GitHub: new issues[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#github-new-issues "Direct link to GitHub: new issues")

```
hermes webhook subscribe github-issues \--events"issues"\--prompt"New GitHub issue #{issue.number}: {issue.title}\n\nAction: {action}\nAuthor: {issue.user.login}\nBody:\n{issue.body}\n\nPlease triage this issue."\--deliver telegram \  --deliver-chat-id "-100123456789"
```

Then in GitHub repo Settings → Webhooks → Add webhook:
  * Payload URL: the returned webhook_url
  * Content type: application/json
  * Secret: the returned secret
  * Events: "Issues"


### GitHub: PR reviews[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#github-pr-reviews "Direct link to GitHub: PR reviews")

```
hermes webhook subscribe github-prs \--events"pull_request"\--prompt"PR #{pull_request.number} {action}: {pull_request.title}\nBy: {pull_request.user.login}\nBranch: {pull_request.head.ref}\n\n{pull_request.body}"\--skills"github-code-review"\--deliver github_comment
```

### Stripe: payment events[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#stripe-payment-events "Direct link to Stripe: payment events")

```
hermes webhook subscribe stripe-payments \--events"payment_intent.succeeded,payment_intent.payment_failed"\--prompt"Payment {data.object.status}: {data.object.amount} cents from {data.object.receipt_email}"\--deliver telegram \  --deliver-chat-id "-100123456789"
```

### CI/CD: build notifications[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#cicd-build-notifications "Direct link to CI/CD: build notifications")

```
hermes webhook subscribe ci-builds \--events"pipeline"\--prompt"Build {object_attributes.status} on {project.name} branch {object_attributes.ref}\nCommit: {commit.message}"\--deliver discord \  --deliver-chat-id "1234567890"
```

### Generic monitoring alert[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#generic-monitoring-alert "Direct link to Generic monitoring alert")

```
hermes webhook subscribe alerts \--prompt"Alert: {alert.name}\nSeverity: {alert.severity}\nMessage: {alert.message}\n\nPlease investigate and suggest remediation."\--deliver origin
```

### Direct delivery (no agent, zero LLM cost)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#direct-delivery-no-agent-zero-llm-cost "Direct link to Direct delivery \(no agent, zero LLM cost\)")
For use cases where you just want to push a notification through to a user's chat — no reasoning, no agent loop — add `--deliver-only`. The rendered `--prompt` template becomes the literal message body and is dispatched directly to the target adapter.
Use this for:
  * External service push notifications (Supabase/Firebase webhooks → Telegram)
  * Monitoring alerts that should forward verbatim
  * Inter-agent pings where one agent is telling another agent's user something
  * Any webhook where an LLM round trip would be wasted effort



```
hermes webhook subscribe antenna-matches \--deliver telegram \  --deliver-chat-id "123456789"\  --deliver-only \--prompt"🎉 New match: {match.user_name} matched with you!"\--description"Antenna match notifications"
```

The POST returns `200 OK` on successful delivery, `502` on target failure — so upstream services can retry intelligently. HMAC auth, rate limits, and idempotency still apply.
Requires `--deliver` to be a real target (telegram, discord, slack, github_comment, etc.) — `--deliver log` is rejected because log-only direct delivery is pointless.
## Security[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#security "Direct link to Security")
  * Each subscription gets an auto-generated HMAC-SHA256 secret (or provide your own with `--secret`)
  * The webhook adapter validates signatures on every incoming POST
  * Static routes from config.yaml cannot be overwritten by dynamic subscriptions
  * Subscriptions persist to `~/.hermes/webhook_subscriptions.json`


## How It Works[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#how-it-works "Direct link to How It Works")
  1. `hermes webhook subscribe` writes to `~/.hermes/webhook_subscriptions.json`
  2. The webhook adapter hot-reloads this file on each incoming request (mtime-gated, negligible overhead)
  3. When a POST arrives matching a route, the adapter formats the prompt and triggers an agent run
  4. The agent's response is delivered to the configured target (Telegram, Discord, GitHub comment, etc.)


## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#troubleshooting "Direct link to Troubleshooting")
If webhooks aren't working:
  1. **Is the gateway running?** Check with `systemctl --user status hermes-gateway` or `ps aux | grep gateway`
  2. **Is the webhook server listening?** `curl http://localhost:8644/health` should return `{"status": "ok"}`
  3. **Check gateway logs:** `grep webhook ~/.hermes/logs/gateway.log | tail -20`
  4. **Signature mismatch?** Verify the secret in your service matches the one from `hermes webhook list`. GitHub sends `X-Hub-Signature-256`, GitLab sends `X-Gitlab-Token`.
  5. **Firewall/NAT?** The webhook URL must be reachable from the service. For local development, use a tunnel (ngrok, cloudflared).
  6. **Wrong event type?** Check `--events` filter matches what the service sends. Use `hermes webhook test <name>` to verify the route works.


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#reference-full-skillmd)
  * [Setup (Required First)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#setup-required-first)
    * [Option 1: Setup wizard](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#option-1-setup-wizard)
    * [Option 2: Manual config](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#option-2-manual-config)
    * [Option 3: Environment variables](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#option-3-environment-variables)
  * [Commands](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#commands)
    * [Create a subscription](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#create-a-subscription)
    * [List subscriptions](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#list-subscriptions)
    * [Remove a subscription](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#remove-a-subscription)
    * [Test a subscription](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#test-a-subscription)
  * [Prompt Templates](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#prompt-templates)
  * [Common Patterns](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#common-patterns)
    * [GitHub: new issues](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#github-new-issues)
    * [GitHub: PR reviews](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#github-pr-reviews)
    * [Stripe: payment events](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#stripe-payment-events)
    * [CI/CD: build notifications](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#cicd-build-notifications)
    * [Generic monitoring alert](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#generic-monitoring-alert)
    * [Direct delivery (no agent, zero LLM cost)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#direct-delivery-no-agent-zero-llm-cost)
  * [How It Works](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#how-it-works)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-webhook-subscriptions#troubleshooting)


