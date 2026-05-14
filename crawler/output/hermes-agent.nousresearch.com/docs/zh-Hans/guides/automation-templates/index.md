<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates -->

本页总览
Copy-paste recipes for common automation patterns. Each template uses Hermes's built-in [cron scheduler](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/cron) for time-based triggers and [webhook platform](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/webhooks) for event-driven triggers.
Every template works with **any model** — not locked to a single provider.  
| Trigger  | How  | Tool  |  
| --- | --- | --- |  
| **Schedule**  | Runs on a cadence (hourly, nightly, weekly)  |  `cronjob` tool or `/cron` slash command  |  
| **GitHub Event**  | Fires on PR opens, pushes, issues, CI results  | Webhook platform (`hermes webhook subscribe`)  |  
| **API Call**  | External service POSTs JSON to your endpoint  | Webhook platform (config.yaml routes or `hermes webhook subscribe`)  |  
All three support delivery to Telegram, Discord, Slack, SMS, email, GitHub comments, or local files.
## Development Workflow[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#development-workflow "Development Workflow的直接链接")
### Nightly Backlog Triage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#nightly-backlog-triage "Nightly Backlog Triage的直接链接")
Label, prioritize, and summarize new issues every night. Delivers a digest to your team channel.
**Trigger:** Schedule (nightly)

```
hermes cron create "0 2 * * *"\"You are a project manager triaging the NousResearch/hermes-agent GitHub repo.1. Run: gh issue list --repo NousResearch/hermes-agent --state open --json number,title,labels,author,createdAt --limit 302. Identify issues opened in the last 24 hours3. For each new issue:   - Suggest a priority label (P0-critical, P1-high, P2-medium, P3-low)   - Suggest a category label (bug, feature, docs, security)   - Write a one-line triage note4. Summarize: total open issues, new today, breakdown by priorityFormat as a clean digest. If no new issues, respond with [SILENT]."\--name"Nightly backlog triage"\--deliver telegram
```

### Automatic PR Code Review[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#automatic-pr-code-review "Automatic PR Code Review的直接链接")
Review every pull request automatically when it's opened. Posts a review comment directly on the PR.
**Trigger:** GitHub webhook
**Option A — Dynamic subscription (CLI):**

```
hermes webhook subscribe github-pr-review \--events"pull_request"\--prompt"Review this pull request:Repository: {repository.full_name}PR #{pull_request.number}: {pull_request.title}Author: {pull_request.user.login}Action: {action}Diff URL: {pull_request.diff_url}Fetch the diff with: curl -sL {pull_request.diff_url}Review for:- Security issues (injection, auth bypass, secrets in code)- Performance concerns (N+1 queries, unbounded loops, memory leaks)- Code quality (naming, duplication, error handling)- Missing tests for new behaviorPost a concise review. If the PR is a trivial docs/typo change, say so briefly."\--skill github-code-review \--deliver github_comment
```

**Option B — Static route (config.yaml):**

```
platforms:webhook:enabled:trueextra:port:8644secret:"your-global-secret"routes:github-pr-review:events:["pull_request"]secret:"github-webhook-secret"prompt:|            Review PR #{pull_request.number}: {pull_request.title}            Repository: {repository.full_name}            Author: {pull_request.user.login}            Diff URL: {pull_request.diff_url}            Review for security, performance, and code quality.skills:["github-code-review"]deliver:"github_comment"deliver_extra:repo:"{repository.full_name}"pr_number:"{pull_request.number}"
```

Then in GitHub: **Settings → Webhooks → Add webhook** → Payload URL: `http://your-server:8644/webhooks/github-pr-review`, Content type: `application/json`, Secret: `github-webhook-secret`, Events: **Pull requests**.
### Docs Drift Detection[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#docs-drift-detection "Docs Drift Detection的直接链接")
Weekly scan of merged PRs to find API changes that need documentation updates.
**Trigger:** Schedule (weekly)

```
hermes cron create "0 9 * * 1"\"Scan the NousResearch/hermes-agent repo for documentation drift.1. Run: gh pr list --repo NousResearch/hermes-agent --state merged --json number,title,files,mergedAt --limit 302. Filter to PRs merged in the last 7 days3. For each merged PR, check if it modified:   - Tool schemas (tools/*.py) — may need docs/reference/tools-reference.md update   - CLI commands (hermes_cli/commands.py, hermes_cli/main.py) — may need docs/reference/cli-commands.md update   - Config options (hermes_cli/config.py) — may need docs/user-guide/configuration.md update   - Environment variables — may need docs/reference/environment-variables.md update4. Cross-reference: for each code change, check if the corresponding docs page was also updated in the same PRReport any gaps where code changed but docs didn't. If everything is in sync, respond with [SILENT]."\--name"Docs drift detection"\--deliver telegram
```

### Dependency Security Audit[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#dependency-security-audit "Dependency Security Audit的直接链接")
Daily scan for known vulnerabilities in project dependencies.
**Trigger:** Schedule (daily)

```
hermes cron create "0 6 * * *"\"Run a dependency security audit on the hermes-agent project.1. cd ~/.hermes/hermes-agent && source .venv/bin/activate2. Run: pip audit --format json 2>/dev/null || pip audit 2>&13. Run: npm audit --json 2>/dev/null (in website/ directory if it exists)4. Check for any CVEs with CVSS score >= 7.0If vulnerabilities found:- List each one with package name, version, CVE ID, severity- Check if an upgrade is available- Note if it's a direct dependency or transitiveIf no vulnerabilities, respond with [SILENT]."\--name"Dependency audit"\--deliver telegram
```

## DevOps & Monitoring[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#devops--monitoring "DevOps & Monitoring的直接链接")
### Deploy Verification[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#deploy-verification "Deploy Verification的直接链接")
Trigger smoke tests after every deployment. Your CI/CD pipeline POSTs to the webhook when a deploy completes.
**Trigger:** API call (webhook)

```
hermes webhook subscribe deploy-verify \--events"deployment"\--prompt"A deployment just completed:Service: {service}Environment: {environment}Version: {version}Deployed by: {deployer}Run these verification steps:1. Check if the service is responding: curl -s -o /dev/null -w '%{http_code}' {health_url}2. Search recent logs for errors: check the deployment payload for any error indicators3. Verify the version matches: curl -s {health_url}/versionReport: deployment status (healthy/degraded/failed), response time, any errors found.If healthy, keep it brief. If degraded or failed, provide detailed diagnostics."\--deliver telegram
```

Your CI/CD pipeline triggers it:

```
curl-X POST http://your-server:8644/webhooks/deploy-verify \-H"Content-Type: application/json"\-H"X-Hub-Signature-256: sha256=$(echo-n'{"service":"api","environment":"prod","version":"2.1.0","deployer":"ci","health_url":"https://api.example.com/health"}'| openssl dgst -sha256-hmac'your-secret'|cut -d' '-f2)"\-d'{"service":"api","environment":"prod","version":"2.1.0","deployer":"ci","health_url":"https://api.example.com/health"}'
```

### Alert Triage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#alert-triage "Alert Triage的直接链接")
Correlate monitoring alerts with recent changes to draft a response. Works with Datadog, PagerDuty, Grafana, or any alerting system that can POST JSON.
**Trigger:** API call (webhook)

```
hermes webhook subscribe alert-triage \--prompt"Monitoring alert received:Alert: {alert.name}Severity: {alert.severity}Service: {alert.service}Message: {alert.message}Timestamp: {alert.timestamp}Investigate:1. Search the web for known issues with this error pattern2. Check if this correlates with any recent deployments or config changes3. Draft a triage summary with:   - Likely root cause   - Suggested first response steps   - Escalation recommendation (P1-P4)Be concise. This goes to the on-call channel."\--deliver slack
```

### Uptime Monitor[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#uptime-monitor "Uptime Monitor的直接链接")
Check endpoints every 30 minutes. Only notify when something is down.
**Trigger:** Schedule (every 30 min)
~/.hermes/scripts/check-uptime.py

```
import urllib.request, json, timeENDPOINTS =[{"name":"API","url":"https://api.example.com/health"},{"name":"Web","url":"https://www.example.com"},{"name":"Docs","url":"https://docs.example.com"},results =[]for ep in ENDPOINTS:try:        start = time.time()        req = urllib.request.Request(ep["url"], headers={"User-Agent":"Hermes-Monitor/1.0"})        resp = urllib.request.urlopen(req, timeout=10)        elapsed =round((time.time()- start)*1000)        results.append({"name": ep["name"],"status": resp.getcode(),"ms": elapsed})except Exception as e:        results.append({"name": ep["name"],"status":"DOWN","error":str(e)})down =[r for r in results if r.get("status")=="DOWN"or(isinstance(r.get("status"),int)and r["status"]>=500)]if down:print("OUTAGE DETECTED")for r in down:print(f"  {r['name']}: {r.get('error',f'HTTP {r[\"status\"]}')} ")print(f"\nAll results: {json.dumps(results, indent=2)}")else:print("NO_ISSUES")
```


```
hermes cron create "every 30m"\"If the script reports OUTAGE DETECTED, summarize which services are down and suggest likely causes. If NO_ISSUES, respond with [SILENT]."\--script ~/.hermes/scripts/check-uptime.py \--name"Uptime monitor"\--deliver telegram
```

## Research & Intelligence[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#research--intelligence "Research & Intelligence的直接链接")
### Competitive Repository Scout[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#competitive-repository-scout "Competitive Repository Scout的直接链接")
Monitor competitor repos for interesting PRs, features, and architectural decisions.
**Trigger:** Schedule (daily)

```
hermes cron create "0 8 * * *"\"Scout these AI agent repositories for notable activity in the last 24 hours:Repos to check:- anthropics/claude-code- openai/codex- All-Hands-AI/OpenHands- Aider-AI/aiderFor each repo:1. gh pr list --repo <repo> --state all --json number,title,author,createdAt,mergedAt --limit 152. gh issue list --repo <repo> --state open --json number,title,labels,createdAt --limit 10Focus on:- New features being developed- Architectural changes- Integration patterns we could learn from- Security fixes that might affect us tooSkip routine dependency bumps and CI fixes. If nothing notable, respond with [SILENT].If there are findings, organize by repo with brief analysis of each item."\--skill competitive-pr-scout \--name"Competitor scout"\--deliver telegram
```

### AI News Digest[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#ai-news-digest "AI News Digest的直接链接")
Weekly roundup of AI/ML developments.
**Trigger:** Schedule (weekly)

```
hermes cron create "0 9 * * 1"\"Generate a weekly AI news digest covering the past 7 days:1. Search the web for major AI announcements, model releases, and research breakthroughs2. Search for trending ML repositories on GitHub3. Check arXiv for highly-cited papers on language models and agentsStructure:## Headlines (3-5 major stories)## Notable Papers (2-3 papers with one-sentence summaries)## Open Source (interesting new repos or major releases)## Industry Moves (funding, acquisitions, launches)Keep each item to 1-2 sentences. Include links. Total under 600 words."\--name"Weekly AI digest"\--deliver telegram
```

### Paper Digest with Notes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#paper-digest-with-notes "Paper Digest with Notes的直接链接")
Daily arXiv scan that saves summaries to your note-taking system.
**Trigger:** Schedule (daily)

```
hermes cron create "0 8 * * *"\"Search arXiv for the 3 most interesting papers on 'language model reasoning' OR 'tool-use agents' from the past day. For each paper, create an Obsidian note with the title, authors, abstract summary, key contribution, and potential relevance to Hermes Agent development."\--skill arxiv --skill obsidian \--name"Paper digest"\--deliverlocal
```

## GitHub Event Automations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#github-event-automations "GitHub Event Automations的直接链接")
### Issue Auto-Labeling[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#issue-auto-labeling "Issue Auto-Labeling的直接链接")
Automatically label and respond to new issues.
**Trigger:** GitHub webhook

```
hermes webhook subscribe github-issues \--events"issues"\--prompt"New GitHub issue received:Repository: {repository.full_name}Issue #{issue.number}: {issue.title}Author: {issue.user.login}Action: {action}Body: {issue.body}Labels: {issue.labels}If this is a new issue (action=opened):1. Read the issue title and body carefully2. Suggest appropriate labels (bug, feature, docs, security, question)3. If it's a bug report, check if you can identify the affected component from the description4. Post a helpful initial response acknowledging the issueIf this is a label or assignment change, respond with [SILENT]."\--deliver github_comment
```

### CI Failure Analysis[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#ci-failure-analysis "CI Failure Analysis的直接链接")
Analyze CI failures and post diagnostics on the PR.
**Trigger:** GitHub webhook

```
# config.yaml routeplatforms:webhook:enabled:trueextra:routes:ci-failure:events:["check_run"]secret:"ci-secret"prompt:|            CI check failed:            Repository: {repository.full_name}            Check: {check_run.name}            Status: {check_run.conclusion}            PR: #{check_run.pull_requests.0.number}            Details URL: {check_run.details_url}If conclusion is "failure":            1. Fetch the log from the details URL if accessible            2. Identify the likely cause of failure            3. Suggest a fix            If conclusion is "success", respond with [SILENT].deliver:"github_comment"deliver_extra:repo:"{repository.full_name}"pr_number:"{check_run.pull_requests.0.number}"
```

### Auto-Port Changes Across Repos[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#auto-port-changes-across-repos "Auto-Port Changes Across Repos的直接链接")
When a PR merges in one repo, automatically port the equivalent change to another.
**Trigger:** GitHub webhook

```
hermes webhook subscribe auto-port \--events"pull_request"\--prompt"PR merged in the source repository:Repository: {repository.full_name}PR #{pull_request.number}: {pull_request.title}Author: {pull_request.user.login}Action: {action}Merge commit: {pull_request.merge_commit_sha}If action is 'closed' and pull_request.merged is true:1. Fetch the diff: curl -sL {pull_request.diff_url}2. Analyze what changed3. Determine if this change needs to be ported to the Go SDK equivalent4. If yes, create a branch, apply the equivalent changes, and open a PR on the target repo5. Reference the original PR in the new PR descriptionIf action is not 'closed' or not merged, respond with [SILENT]."\--skill github-pr-workflow \--deliver log
```

## Business Operations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#business-operations "Business Operations的直接链接")
### Stripe Payment Monitoring[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#stripe-payment-monitoring "Stripe Payment Monitoring的直接链接")
Track payment events and get summaries of failures.
**Trigger:** API call (webhook)

```
hermes webhook subscribe stripe-payments \--events"payment_intent.succeeded,payment_intent.payment_failed,charge.dispute.created"\--prompt"Stripe event received:Event type: {type}Amount: {data.object.amount} cents ({data.object.currency})Customer: {data.object.customer}Status: {data.object.status}For payment_intent.payment_failed:- Identify the failure reason from {data.object.last_payment_error}- Suggest whether this is a transient issue (retry) or permanent (contact customer)For charge.dispute.created:- Flag as urgent- Summarize the dispute detailsFor payment_intent.succeeded:- Brief confirmation onlyKeep responses concise for the ops channel."\--deliver slack
```

### Daily Revenue Summary[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#daily-revenue-summary "Daily Revenue Summary的直接链接")
Compile key business metrics every morning.
**Trigger:** Schedule (daily)

```
hermes cron create "0 8 * * *"\"Generate a morning business metrics summary.Search the web for:1. Current Bitcoin and Ethereum prices2. S&P 500 status (pre-market or previous close)3. Any major tech/AI industry news from the last 12 hoursFormat as a brief morning briefing, 3-4 bullet points max.Deliver as a clean, scannable message."\--name"Morning briefing"\--deliver telegram
```

## Multi-Skill Workflows[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#multi-skill-workflows "Multi-Skill Workflows的直接链接")
### Security Audit Pipeline[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#security-audit-pipeline "Security Audit Pipeline的直接链接")
Combine multiple skills for a comprehensive weekly security review.
**Trigger:** Schedule (weekly)

```
hermes cron create "0 3 * * 0"\"Run a comprehensive security audit of the hermes-agent codebase.1. Check for dependency vulnerabilities (pip audit, npm audit)2. Search the codebase for common security anti-patterns:   - Hardcoded secrets or API keys   - SQL injection vectors (string formatting in queries)   - Path traversal risks (user input in file paths without validation)   - Unsafe deserialization (pickle.loads, yaml.load without SafeLoader)3. Review recent commits (last 7 days) for security-relevant changes4. Check if any new environment variables were added without being documentedWrite a security report with findings categorized by severity (Critical, High, Medium, Low).If nothing found, report a clean bill of health."\--skill codebase-security-audit \--name"Weekly security audit"\--deliver telegram
```

### Content Pipeline[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#content-pipeline "Content Pipeline的直接链接")
Research, draft, and prepare content on a schedule.
**Trigger:** Schedule (weekly)

```
hermes cron create "0 10 * * 3"\"Research and draft a technical blog post outline about a trending topic in AI agents.1. Search the web for the most discussed AI agent topics this week2. Pick the most interesting one that's relevant to open-source AI agents3. Create an outline with:   - Hook/intro angle   - 3-4 key sections   - Technical depth appropriate for developers   - Conclusion with actionable takeaway4. Save the outline to ~/drafts/blog-$(date +%Y%m%d).mdKeep the outline to ~300 words. This is a starting point, not a finished post."\--name"Blog outline"\--deliverlocal
```

## Quick Reference[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#quick-reference "Quick Reference的直接链接")
### Cron Schedule Syntax[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#cron-schedule-syntax "Cron Schedule Syntax的直接链接")  
| Expression  | Meaning  |  
| --- | --- |  
| `every 30m`  | Every 30 minutes  |  
| `every 2h`  | Every 2 hours  |  
| `0 2 * * *`  | Daily at 2:00 AM  |  
| `0 9 * * 1`  | Every Monday at 9:00 AM  |  
| `0 9 * * 1-5`  | Weekdays at 9:00 AM  |  
| `0 3 * * 0`  | Every Sunday at 3:00 AM  |  
| `0 */6 * * *`  | Every 6 hours  |  
### Delivery Targets[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#delivery-targets "Delivery Targets的直接链接")  
| Target  | Flag  | Notes  |  
| --- | --- | --- |  
| Same chat  | `--deliver origin`  | Default — delivers to where the job was created  |  
| Local file  | `--deliver local`  | Saves output, no notification  |  
| Telegram  | `--deliver telegram`  | Home channel, or `telegram:CHAT_ID` for specific  |  
| Discord  | `--deliver discord`  | Home channel, or `discord:CHANNEL_ID`  |  
| Slack  | `--deliver slack`  | Home channel  |  
| SMS  | `--deliver sms:+15551234567`  | Direct to phone number  |  
| Specific thread  | `--deliver telegram:-100123:456`  | Telegram forum topic  |  
### Webhook Template Variables[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#webhook-template-variables "Webhook Template Variables的直接链接")  
| Variable  | Description  |  
| --- | --- |  
| `{pull_request.title}`  | PR title  |  
| `{issue.number}`  | Issue number  |  
| `{repository.full_name}`  | `owner/repo`  |  
| `{action}`  | Event action (opened, closed, etc.)  |  
| `{__raw__}`  | Full JSON payload (truncated at 4000 chars)  |  
| `{sender.login}`  | GitHub user who triggered the event  |  
### The [SILENT] Pattern[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#the-silent-pattern "The \[SILENT\] Pattern的直接链接")
When a cron job's response contains `[SILENT]`, delivery is suppressed. Use this to avoid notification spam on quiet runs:

```
If nothing noteworthy happened, respond with [SILENT].
```

This means you only get notified when the agent has something to report.
  * [Development Workflow](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#development-workflow)
    * [Nightly Backlog Triage](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#nightly-backlog-triage)
    * [Automatic PR Code Review](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#automatic-pr-code-review)
    * [Docs Drift Detection](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#docs-drift-detection)
    * [Dependency Security Audit](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#dependency-security-audit)
  * [DevOps & Monitoring](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#devops--monitoring)
    * [Deploy Verification](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#deploy-verification)
    * [Alert Triage](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#alert-triage)
    * [Uptime Monitor](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#uptime-monitor)
  * [Research & Intelligence](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#research--intelligence)
    * [Competitive Repository Scout](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#competitive-repository-scout)
    * [AI News Digest](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#ai-news-digest)
    * [Paper Digest with Notes](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#paper-digest-with-notes)
  * [GitHub Event Automations](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#github-event-automations)
    * [Issue Auto-Labeling](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#issue-auto-labeling)
    * [CI Failure Analysis](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#ci-failure-analysis)
    * [Auto-Port Changes Across Repos](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#auto-port-changes-across-repos)
  * [Business Operations](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#business-operations)
    * [Stripe Payment Monitoring](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#stripe-payment-monitoring)
    * [Daily Revenue Summary](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#daily-revenue-summary)
  * [Multi-Skill Workflows](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#multi-skill-workflows)
    * [Security Audit Pipeline](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#security-audit-pipeline)
    * [Content Pipeline](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#content-pipeline)
  * [Quick Reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#quick-reference)
    * [Cron Schedule Syntax](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#cron-schedule-syntax)
    * [Delivery Targets](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#delivery-targets)
    * [Webhook Template Variables](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#webhook-template-variables)
    * [The [SILENT] Pattern](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automation-templates#the-silent-pattern)


