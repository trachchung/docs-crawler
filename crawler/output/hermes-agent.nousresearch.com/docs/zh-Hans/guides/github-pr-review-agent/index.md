<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent -->

本页总览
**The problem:** Your team opens PRs faster than you can review them. PRs sit for days waiting for eyeballs. Junior devs merge bugs because nobody had time to check. You spend your mornings catching up on diffs instead of building.
**The solution:** An AI agent that watches your repos around the clock, reviews every new PR for bugs, security issues, and code quality, and sends you a summary — so you only spend time on PRs that actually need human judgment.
**What you'll build:**

```
┌───────────────────────────────────────────────────────────────────┐│                                                                   ││   Cron Timer  ──▶  Hermes Agent  ──▶  GitHub API  ──▶  Review     ││   (every 2h)       + gh CLI           (PR diffs)       delivery   ││                    + skill                             (Telegram, ││                    + memory                            Discord,   ││                                                        local)     ││                                                                   │└───────────────────────────────────────────────────────────────────┘
```

This guide uses **cron jobs** to poll for PRs on a schedule — no server or public endpoint needed. Works behind NAT and firewalls.
If you have a public endpoint available, check out [Automated GitHub PR Comments with Webhooks](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/webhook-github-pr-review) — GitHub pushes events to Hermes instantly when PRs are opened or updated.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#prerequisites "Prerequisites的直接链接")
  * **Hermes Agent installed** — see the [Installation guide](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/getting-started/installation)
  * **Gateway running** for cron jobs: 

```
hermes gateway install# Install as a service# orhermes gateway           # Run in foreground
```

  * **GitHub CLI (`gh`) installed and authenticated**: 

```
# Installbrew install gh        # macOSsudoaptinstall gh    # Ubuntu/Debian# Authenticategh auth login
```

  * **Messaging configured** (optional) — [Telegram](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/telegram) or [Discord](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/discord)


Use `deliver: "local"` to save reviews to `~/.hermes/cron/output/`. Great for testing before wiring up notifications.
## Step 1: Verify the Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#step-1-verify-the-setup "Step 1: Verify the Setup的直接链接")
Make sure Hermes can access GitHub. Start a chat:

```
hermes
```

Test with a simple command:

```
Run: gh pr list --repo NousResearch/hermes-agent --state open --limit 3
```

You should see a list of open PRs. If this works, you're ready.
## Step 2: Try a Manual Review[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#step-2-try-a-manual-review "Step 2: Try a Manual Review的直接链接")
Still in the chat, ask Hermes to review a real PR:

```
Review this pull request. Read the diff, check for bugs, security issues,and code quality. Be specific about line numbers and quote problematic code.Run: gh pr diff 3888 --repo NousResearch/hermes-agent
```

Hermes will:
  1. Execute `gh pr diff` to fetch the code changes
  2. Read through the entire diff
  3. Produce a structured review with specific findings


If you're happy with the quality, time to automate it.
## Step 3: Create a Review Skill[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#step-3-create-a-review-skill "Step 3: Create a Review Skill的直接链接")
A skill gives Hermes consistent review guidelines that persist across sessions and cron runs. Without one, review quality varies.

```
mkdir-p ~/.hermes/skills/code-review
```

Create `~/.hermes/skills/code-review/SKILL.md`:

```
---name: code-reviewdescription: Review pull requests for bugs, security issues, and code quality---# Code Review GuidelinesWhen reviewing a pull request:## What to Check1.**Bugs** — Logic errors, off-by-one, null/undefined handling2.**Security** — Injection, auth bypass, secrets in code, SSRF3.**Performance** — N+1 queries, unbounded loops, memory leaks4.**Style** — Naming conventions, dead code, missing error handling5.**Tests** — Are changes tested? Do tests cover edge cases?## Output FormatFor each finding:-**File:Line** — exact location-**Severity** — Critical / Warning / Suggestion-**What's wrong** — one sentence-**Fix** — how to fix it## Rules- Be specific. Quote the problematic code.- Don't flag style nitpicks unless they affect readability.- If the PR looks good, say so. Don't invent problems.- End with: APPROVE / REQUEST_CHANGES / COMMENT
```

Verify it loaded — start `hermes` and you should see `code-review` in the skills list at startup.
## Step 4: Teach It Your Conventions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#step-4-teach-it-your-conventions "Step 4: Teach It Your Conventions的直接链接")
This is what makes the reviewer actually useful. Start a session and teach Hermes your team's standards:

```
Remember: In our backend repo, we use Python with FastAPI.All endpoints must have type annotations and Pydantic models.We don't allow raw SQL — only SQLAlchemy ORM.Test files go in tests/ and must use pytest fixtures.
```


```
Remember: In our frontend repo, we use TypeScript with React.No `any` types allowed. All components must have props interfaces.We use React Query for data fetching, never useEffect for API calls.
```

These memories persist forever — the reviewer will enforce your conventions without being told each time.
## Step 5: Create the Automated Cron Job[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#step-5-create-the-automated-cron-job "Step 5: Create the Automated Cron Job的直接链接")
Now wire it all together. Create a cron job that runs every 2 hours:

```
hermes cron create "0 */2 * * *"\"Check for new open PRs and review them.Repos to monitor:- myorg/backend-api- myorg/frontend-appSteps:1. Run: gh pr list --repo REPO --state open --limit 5 --json number,title,author,createdAt2. For each PR created or updated in the last 4 hours:   - Run: gh pr diff NUMBER --repo REPO   - Review the diff using the code-review guidelines3. Format output as:## PR Reviews — today### [repo] #[number]: [title]**Author:** [name] | **Verdict:** APPROVE/REQUEST_CHANGES/COMMENT[findings]If no new PRs found, say: No new PRs to review."\--name"pr-review"\--deliver telegram \--skill code-review
```

Verify it's scheduled:

```
hermes cron list
```

### Other useful schedules[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#other-useful-schedules "Other useful schedules的直接链接")  
| Schedule  | When  |  
| --- | --- |  
| `0 */2 * * *`  | Every 2 hours  |  
| `0 9,13,17 * * 1-5`  | Three times a day, weekdays only  |  
| `0 9 * * 1`  | Weekly Monday morning roundup  |  
| `30m`  | Every 30 minutes (high-traffic repos)  |  
## Step 6: Run It On Demand[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#step-6-run-it-on-demand "Step 6: Run It On Demand的直接链接")
Don't want to wait for the schedule? Trigger it manually:

```
hermes cron run pr-review
```

Or from within a chat session:

```
/cron run pr-review
```

## Going Further[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#going-further "Going Further的直接链接")
### Post Reviews Directly to GitHub[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#post-reviews-directly-to-github "Post Reviews Directly to GitHub的直接链接")
Instead of delivering to Telegram, have the agent comment on the PR itself:
Add this to your cron prompt:

```
After reviewing, post your review:- For issues: gh pr review NUMBER --repo REPO --comment --body "YOUR_REVIEW"- For critical issues: gh pr review NUMBER --repo REPO --request-changes --body "YOUR_REVIEW"- For clean PRs: gh pr review NUMBER --repo REPO --approve --body "Looks good"
```

Make sure `gh` has a token with `repo` scope. Reviews are posted as whoever `gh` is authenticated as.
### Weekly PR Dashboard[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#weekly-pr-dashboard "Weekly PR Dashboard的直接链接")
Create a Monday morning overview of all your repos:

```
hermes cron create "0 9 * * 1"\"Generate a weekly PR dashboard:- myorg/backend-api- myorg/frontend-app- myorg/infraFor each repo show:1. Open PR count and oldest PR age2. PRs merged this week3. Stale PRs (older than 5 days)4. PRs with no reviewer assignedFormat as a clean summary."\--name"weekly-dashboard"\--deliver telegram
```

### Multi-Repo Monitoring[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#multi-repo-monitoring "Multi-Repo Monitoring的直接链接")
Scale up by adding more repos to the prompt. The agent processes them sequentially — no extra setup needed.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#troubleshooting "Troubleshooting的直接链接")
### "gh: command not found"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#gh-command-not-found ""gh: command not found"的直接链接")
The gateway runs in a minimal environment. Ensure `gh` is in the system PATH and restart the gateway.
### Reviews are too generic[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#reviews-are-too-generic "Reviews are too generic的直接链接")
  1. Add the `code-review` skill (Step 3)
  2. Teach Hermes your conventions via memory (Step 4)
  3. The more context it has about your stack, the better the reviews


### Cron job doesn't run[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#cron-job-doesnt-run "Cron job doesn't run的直接链接")

```
hermes gateway status    # Is the gateway running?hermes cron list         # Is the job enabled?
```

### Rate limits[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#rate-limits "Rate limits的直接链接")
GitHub allows 5,000 API requests/hour for authenticated users. Each PR review uses ~3-5 requests (list + diff + optional comments). Even reviewing 100 PRs/day stays well within limits.
## What's Next?[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#whats-next "What's Next?的直接链接")
  * **[Webhook-Based PR Reviews](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/webhook-github-pr-review)** — get instant reviews when PRs are opened (requires a public endpoint)
  * **[Daily Briefing Bot](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/daily-briefing-bot)** — combine PR reviews with your morning news digest
  * **[Build a Plugin](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/build-a-hermes-plugin)** — wrap the review logic into a shareable plugin
  * — run a dedicated reviewer profile with its own memory and config
  * **[Fallback Providers](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/fallback-providers)** — ensure reviews run even when one provider is down


  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#prerequisites)
  * [Step 1: Verify the Setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#step-1-verify-the-setup)
  * [Step 2: Try a Manual Review](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#step-2-try-a-manual-review)
  * [Step 3: Create a Review Skill](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#step-3-create-a-review-skill)
  * [Step 4: Teach It Your Conventions](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#step-4-teach-it-your-conventions)
  * [Step 5: Create the Automated Cron Job](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#step-5-create-the-automated-cron-job)
    * [Other useful schedules](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#other-useful-schedules)
  * [Step 6: Run It On Demand](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#step-6-run-it-on-demand)
  * [Going Further](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#going-further)
    * [Post Reviews Directly to GitHub](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#post-reviews-directly-to-github)
    * [Weekly PR Dashboard](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#weekly-pr-dashboard)
    * [Multi-Repo Monitoring](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#multi-repo-monitoring)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#troubleshooting)
    * ["gh: command not found"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#gh-command-not-found)
    * [Reviews are too generic](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#reviews-are-too-generic)
    * [Cron job doesn't run](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#cron-job-doesnt-run)
    * [Rate limits](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#rate-limits)
  * [What's Next?](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/github-pr-review-agent#whats-next)


