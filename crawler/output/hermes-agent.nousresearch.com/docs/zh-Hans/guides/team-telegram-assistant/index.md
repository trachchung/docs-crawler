<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant -->

本页总览
This tutorial walks you through setting up a Telegram bot powered by Hermes Agent that multiple team members can use. By the end, your team will have a shared AI assistant they can message for help with code, research, system administration, and anything else — secured with per-user authorization.
## What We're Building[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#what-were-building "What We're Building的直接链接")
A Telegram bot that:
  * **Any authorized team member** can DM for help — code reviews, research, shell commands, debugging
  * **Runs on your server** with full tool access — terminal, file editing, web search, code execution
  * **Per-user sessions** — each person gets their own conversation context
  * **Secure by default** — only approved users can interact, with two authorization methods
  * **Scheduled tasks** — daily standups, health checks, and reminders delivered to a team channel


## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#prerequisites "Prerequisites的直接链接")
Before starting, make sure you have:
  * **Hermes Agent installed** on a server or VPS (not your laptop — the bot needs to stay running). Follow the [installation guide](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/getting-started/installation) if you haven't yet.
  * **A Telegram account** for yourself (the bot owner)
  * **An LLM provider configured** — at minimum, an API key for OpenAI, Anthropic, or another supported provider in `~/.hermes/.env`


A $5/month VPS is plenty for running the gateway. Hermes itself is lightweight — the LLM API calls are what cost money, and those happen remotely.
## Step 1: Create a Telegram Bot[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#step-1-create-a-telegram-bot "Step 1: Create a Telegram Bot的直接链接")
Every Telegram bot starts with **@BotFather** — Telegram's official bot for creating bots.
  1. **Open Telegram** and search for `@BotFather`, or go to [t.me/BotFather](https://t.me/BotFather)
  2. **Send`/newbot`** — BotFather will ask you two things:
     * **Display name** — what users see (e.g., `Team Hermes Assistant`)
     * **Username** — must end in `bot` (e.g., `myteam_hermes_bot`)
  3. **Copy the bot token** — BotFather replies with something like:

```
Use this token to access the HTTP API:7123456789:AAH1bGciOiJSUzI1NiIsInR5cCI6Ikp...
```

Save this token — you'll need it in the next step.
  4. **Set a description** (optional but recommended):

```
/setdescription
```

Choose your bot, then enter something like:

```
Team AI assistant powered by Hermes Agent. DM me for help with code, research, debugging, and more.
```

  5. **Set bot commands** (optional — gives users a command menu):

```
/setcommands
```

Choose your bot, then paste:

```
new - Start a fresh conversationmodel - Show or change the AI modelstatus - Show session infohelp - Show available commandsstop - Stop the current task
```



Keep your bot token secret. Anyone with the token can control the bot. If it leaks, use `/revoke` in BotFather to generate a new one.
## Step 2: Configure the Gateway[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#step-2-configure-the-gateway "Step 2: Configure the Gateway的直接链接")
You have two options: the interactive setup wizard (recommended) or manual configuration.
### Option A: Interactive Setup (Recommended)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#option-a-interactive-setup-recommended "Option A: Interactive Setup \(Recommended\)的直接链接")

```
hermes gateway setup
```

This walks you through everything with arrow-key selection. Pick **Telegram** , paste your bot token, and enter your user ID when prompted.
### Option B: Manual Configuration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#option-b-manual-configuration "Option B: Manual Configuration的直接链接")
Add these lines to `~/.hermes/.env`:

```
# Telegram bot token from BotFatherTELEGRAM_BOT_TOKEN=7123456789:AAH1bGciOiJSUzI1NiIsInR5cCI6Ikp...# Your Telegram user ID (numeric)TELEGRAM_ALLOWED_USERS=123456789
```

### Finding Your User ID[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#finding-your-user-id "Finding Your User ID的直接链接")
Your Telegram user ID is a numeric value (not your username). To find it:
  1. Message [@userinfobot](https://t.me/userinfobot) on Telegram
  2. It instantly replies with your numeric user ID
  3. Copy that number into `TELEGRAM_ALLOWED_USERS`


Telegram user IDs are permanent numbers like `123456789`. They're different from your `@username`, which can change. Always use the numeric ID for allowlists.
## Step 3: Start the Gateway[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#step-3-start-the-gateway "Step 3: Start the Gateway的直接链接")
### Quick Test[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#quick-test "Quick Test的直接链接")
Run the gateway in the foreground first to make sure everything works:

```
hermes gateway
```

You should see output like:

```
[Gateway] Starting Hermes Gateway...[Gateway] Telegram adapter connected[Gateway] Cron scheduler started (tick every 60s)
```

Open Telegram, find your bot, and send it a message. If it replies, you're in business. Press `Ctrl+C` to stop.
### Production: Install as a Service[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#production-install-as-a-service "Production: Install as a Service的直接链接")
For a persistent deployment that survives reboots:

```
hermes gateway installsudo hermes gateway install--system# Linux only: boot-time system service
```

This creates a background service: a user-level **systemd** service on Linux by default, a **launchd** service on macOS, or a boot-time Linux system service if you pass `--system`.

```
# Linux — manage the default user servicehermes gateway starthermes gateway stophermes gateway status# View live logsjournalctl --user-u hermes-gateway -f# Keep running after SSH logoutsudo loginctl enable-linger $USER# Linux servers — explicit system-service commandssudo hermes gateway start --systemsudo hermes gateway status --systemjournalctl -u hermes-gateway -f
```


```
# macOS — manage the servicehermes gateway starthermes gateway stoptail-f ~/.hermes/logs/gateway.log
```

The launchd plist captures your shell PATH at install time so gateway subprocesses can find tools like Node.js and ffmpeg. If you install new tools later, re-run `hermes gateway install` to update the plist.
### Verify It's Running[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#verify-its-running "Verify It's Running的直接链接")

```
hermes gateway status
```

Then send a test message to your bot on Telegram. You should get a response within a few seconds.
## Step 4: Set Up Team Access[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#step-4-set-up-team-access "Step 4: Set Up Team Access的直接链接")
Now let's give your teammates access. There are two approaches.
### Approach A: Static Allowlist[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#approach-a-static-allowlist "Approach A: Static Allowlist的直接链接")
Collect each team member's Telegram user ID (have them message [@userinfobot](https://t.me/userinfobot)) and add them as a comma-separated list:

```
# In ~/.hermes/.envTELEGRAM_ALLOWED_USERS=123456789,987654321,555555555
```

Restart the gateway after changes:

```
hermes gateway stop && hermes gateway start
```

### Approach B: DM Pairing (Recommended for Teams)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#approach-b-dm-pairing-recommended-for-teams "Approach B: DM Pairing \(Recommended for Teams\)的直接链接")
DM pairing is more flexible — you don't need to collect user IDs upfront. Here's how it works:
  1. **Teammate DMs the bot** — since they're not on the allowlist, the bot replies with a one-time pairing code:

```
🔐 Pairing code: XKGH5N7PSend this code to the bot owner for approval.
```

  2. **Teammate sends you the code** (via any channel — Slack, email, in person)
  3. **You approve it** on the server:

```
hermes pairing approve telegram XKGH5N7P
```

  4. **They're in** — the bot immediately starts responding to their messages


**Managing paired users:**

```
# See all pending and approved usershermes pairing list# Revoke someone's accesshermes pairing revoke telegram 987654321# Clear expired pending codeshermes pairing clear-pending
```

DM pairing is ideal for teams because you don't need to restart the gateway when adding new users. Approvals take effect immediately.
### Security Considerations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#security-considerations "Security Considerations的直接链接")
  * **Never set`GATEWAY_ALLOW_ALL_USERS=true`** on a bot with terminal access — anyone who finds your bot could run commands on your server
  * Pairing codes expire after **1 hour** and use cryptographic randomness
  * Rate limiting prevents brute-force attacks: 1 request per user per 10 minutes, max 3 pending codes per platform
  * After 5 failed approval attempts, the platform enters a 1-hour lockout
  * All pairing data is stored with `chmod 0600` permissions


## Step 5: Configure the Bot[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#step-5-configure-the-bot "Step 5: Configure the Bot的直接链接")
### Set a Home Channel[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#set-a-home-channel "Set a Home Channel的直接链接")
A **home channel** is where the bot delivers cron job results and proactive messages. Without one, scheduled tasks have nowhere to send output.
**Option 1:** Use the `/sethome` command in any Telegram group or chat where the bot is a member.
**Option 2:** Set it manually in `~/.hermes/.env`:

```
TELEGRAM_HOME_CHANNEL=-1001234567890TELEGRAM_HOME_CHANNEL_NAME="Team Updates"
```

To find a channel ID, add [@userinfobot](https://t.me/userinfobot) to the group — it will report the group's chat ID.
### Configure Tool Progress Display[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#configure-tool-progress-display "Configure Tool Progress Display的直接链接")
Control how much detail the bot shows when using tools. In `~/.hermes/config.yaml`:

```
display:tool_progress: new    # off | new | all | verbose
```
  
| Mode  | What You See  |  
| --- | --- |  
| `off`  | Clean responses only — no tool activity  |  
| `new`  | Brief status for each new tool call (recommended for messaging)  |  
| `all`  | Every tool call with details  |  
| `verbose`  | Full tool output including command results  |  
Users can also change this per-session with the `/verbose` command in chat.
### Set Up a Personality with SOUL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#set-up-a-personality-with-soulmd "Set Up a Personality with SOUL.md的直接链接")
Customize how the bot communicates by editing `~/.hermes/SOUL.md`:
For a full guide, see [Use SOUL.md with Hermes](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/use-soul-with-hermes).

```
# SoulYou are a helpful team assistant. Be concise and technical.Use code blocks for any code. Skip pleasantries — the teamvalues directness. When debugging, always ask for error logsbefore guessing at solutions.
```

### Add Project Context[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#add-project-context "Add Project Context的直接链接")
If your team works on specific projects, create context files so the bot knows your stack:

```
<!-- ~/.hermes/AGENTS.md --># Team Context- We use Python 3.12 with FastAPI and SQLAlchemy- Frontend is React with TypeScript- CI/CD runs on GitHub Actions- Production deploys to AWS ECS- Always suggest writing tests for new code
```

Context files are injected into every session's system prompt. Keep them concise — every character counts against your token budget.
## Step 6: Set Up Scheduled Tasks[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#step-6-set-up-scheduled-tasks "Step 6: Set Up Scheduled Tasks的直接链接")
With the gateway running, you can schedule recurring tasks that deliver results to your team channel.
### Daily Standup Summary[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#daily-standup-summary "Daily Standup Summary的直接链接")
Message the bot on Telegram:

```
Every weekday at 9am, check the GitHub repository atgithub.com/myorg/myproject for:1. Pull requests opened/merged in the last 24 hours2. Issues created or closed3. Any CI/CD failures on the main branchFormat as a brief standup-style summary.
```

The agent creates a cron job automatically and delivers results to the chat where you asked (or the home channel).
### Server Health Check[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#server-health-check "Server Health Check的直接链接")

```
Every 6 hours, check disk usage with 'df -h', memory with 'free -h',and Docker container status with 'docker ps'. Report anything unusual —partitions above 80%, containers that have restarted, or high memory usage.
```

### Managing Scheduled Tasks[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#managing-scheduled-tasks "Managing Scheduled Tasks的直接链接")

```
# From the CLIhermes cron list          # View all scheduled jobshermes cron status        # Check if scheduler is running# From Telegram chat/cron list                # View jobs/cron remove <job_id># Remove a job
```

Cron job prompts run in completely fresh sessions with no memory of prior conversations. Make sure each prompt contains **all** the context the agent needs — file paths, URLs, server addresses, and clear instructions.
## Production Tips[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#production-tips "Production Tips的直接链接")
### Use Docker for Safety[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#use-docker-for-safety "Use Docker for Safety的直接链接")
On a shared team bot, use Docker as the terminal backend so agent commands run in a container instead of on your host:

```
# In ~/.hermes/.envTERMINAL_BACKEND=dockerTERMINAL_DOCKER_IMAGE=nikolaik/python-nodejs:python3.11-nodejs20
```

Or in `~/.hermes/config.yaml`:

```
terminal:backend: dockercontainer_cpu:1container_memory:5120container_persistent:true
```

This way, even if someone asks the bot to run something destructive, your host system is protected.
### Monitor the Gateway[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#monitor-the-gateway "Monitor the Gateway的直接链接")

```
# Check if the gateway is runninghermes gateway status# Watch live logs (Linux)journalctl --user-u hermes-gateway -f# Watch live logs (macOS)tail-f ~/.hermes/logs/gateway.log
```

### Keep Hermes Updated[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#keep-hermes-updated "Keep Hermes Updated的直接链接")
From Telegram, send `/update` to the bot — it will pull the latest version and restart. Or from the server:

```
hermes updatehermes gateway stop && hermes gateway start
```

### Log Locations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#log-locations "Log Locations的直接链接")  
| What  | Location  |  
| --- | --- |  
| Gateway logs  |  `journalctl --user -u hermes-gateway` (Linux) or `~/.hermes/logs/gateway.log` (macOS)  |  
| Cron job output  | `~/.hermes/cron/output/{job_id}/{timestamp}.md`  |  
| Cron job definitions  | `~/.hermes/cron/jobs.json`  |  
| Pairing data  | `~/.hermes/pairing/`  |  
| Session history  | `~/.hermes/sessions/`  |  
## Going Further[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#going-further "Going Further的直接链接")
You've got a working team Telegram assistant. Here are some next steps:
  * **[Security Guide](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/security)** — deep dive into authorization, container isolation, and command approval
  * **[Messaging Gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging)** — full reference for gateway architecture, session management, and chat commands
  * **[Telegram Setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/telegram)** — platform-specific details including voice messages and TTS
  * **[Scheduled Tasks](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/cron)** — advanced cron scheduling with delivery options and cron expressions
  * **[Context Files](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/context-files)** — AGENTS.md, SOUL.md, and .cursorrules for project knowledge
  * **[Personality](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/personality)** — built-in personality presets and custom persona definitions
  * **Add more platforms** — the same gateway can simultaneously run [Discord](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/discord), [Slack](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/slack), and [WhatsApp](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/messaging/whatsapp)


_Questions or issues? Open an issue on GitHub — contributions are welcome._
  * [What We're Building](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#what-were-building)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#prerequisites)
  * [Step 1: Create a Telegram Bot](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#step-1-create-a-telegram-bot)
  * [Step 2: Configure the Gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#step-2-configure-the-gateway)
    * [Option A: Interactive Setup (Recommended)](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#option-a-interactive-setup-recommended)
    * [Option B: Manual Configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#option-b-manual-configuration)
    * [Finding Your User ID](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#finding-your-user-id)
  * [Step 3: Start the Gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#step-3-start-the-gateway)
    * [Production: Install as a Service](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#production-install-as-a-service)
    * [Verify It's Running](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#verify-its-running)
  * [Step 4: Set Up Team Access](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#step-4-set-up-team-access)
    * [Approach A: Static Allowlist](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#approach-a-static-allowlist)
    * [Approach B: DM Pairing (Recommended for Teams)](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#approach-b-dm-pairing-recommended-for-teams)
    * [Security Considerations](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#security-considerations)
  * [Step 5: Configure the Bot](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#step-5-configure-the-bot)
    * [Set a Home Channel](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#set-a-home-channel)
    * [Configure Tool Progress Display](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#configure-tool-progress-display)
    * [Set Up a Personality with SOUL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#set-up-a-personality-with-soulmd)
    * [Add Project Context](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#add-project-context)
  * [Step 6: Set Up Scheduled Tasks](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#step-6-set-up-scheduled-tasks)
    * [Daily Standup Summary](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#daily-standup-summary)
    * [Server Health Check](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#server-health-check)
    * [Managing Scheduled Tasks](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#managing-scheduled-tasks)
  * [Production Tips](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#production-tips)
    * [Use Docker for Safety](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#use-docker-for-safety)
    * [Monitor the Gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#monitor-the-gateway)
    * [Keep Hermes Updated](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#keep-hermes-updated)
    * [Log Locations](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#log-locations)
  * [Going Further](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/team-telegram-assistant#going-further)


