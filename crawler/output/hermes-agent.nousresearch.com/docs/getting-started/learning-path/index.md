<!-- Source: https://hermes-agent.nousresearch.com/docs/getting-started/learning-path -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#__docusaurus_skipToContent_fallback)
On this page
Hermes Agent can do a lot — CLI assistant, Telegram/Discord bot, task automation, RL training, and more. This page helps you figure out where to start and what to read based on your experience level and what you're trying to accomplish.
If you haven't installed Hermes Agent yet, begin with the [Installation guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation) and then run through the [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart). Everything below assumes you have a working installation.
## How to Use This Page[​](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#how-to-use-this-page "Direct link to How to Use This Page")
  * **Know your level?** Jump to the [experience-level table](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#by-experience-level) and follow the reading order for your tier.
  * **Have a specific goal?** Skip to [By Use Case](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#by-use-case) and find the scenario that matches.
  * **Just browsing?** Check the [Key Features](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#key-features-at-a-glance) table for a quick overview of everything Hermes Agent can do.


## By Experience Level[​](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#by-experience-level "Direct link to By Experience Level")  
| Level  | Goal  | Recommended Reading  | Time Estimate  |  
| --- | --- | --- | --- |  
| **Beginner**  | Get up and running, have basic conversations, use built-in tools  |  [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation) → [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart) → [CLI Usage](https://hermes-agent.nousresearch.com/docs/user-guide/cli) → [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)  | ~1 hour  |  
| **Intermediate**  | Set up messaging bots, use advanced features like memory, cron jobs, and skills  |  [Sessions](https://hermes-agent.nousresearch.com/docs/user-guide/sessions) → [Messaging](https://hermes-agent.nousresearch.com/docs/user-guide/messaging) → [Tools](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools) → [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) → [Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) → [Cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)  | ~2–3 hours  |  
| **Advanced**  | Build custom tools, create skills, train models with RL, contribute to the project  |  [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture) → [Adding Tools](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools) → [Creating Skills](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills) → [RL Training](https://hermes-agent.nousresearch.com/docs/user-guide/features/rl-training) → [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)  | ~4–6 hours  |  
## By Use Case[​](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#by-use-case "Direct link to By Use Case")
Pick the scenario that matches what you want to do. Each one links you to the relevant docs in the order you should read them.
### "I want a CLI coding assistant"[​](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#i-want-a-cli-coding-assistant "Direct link to "I want a CLI coding assistant"")
Use Hermes Agent as an interactive terminal assistant for writing, reviewing, and running code.
  1. [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
  2. [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  3. [Code Execution](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
  4. [Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)
  5. [Tips & Tricks](https://hermes-agent.nousresearch.com/docs/guides/tips)


Pass files directly into your conversation with context files. Hermes Agent can read, edit, and run code in your projects.
### "I want a Telegram/Discord bot"[​](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#i-want-a-telegramdiscord-bot "Direct link to "I want a Telegram/Discord bot"")
Deploy Hermes Agent as a bot on your favorite messaging platform.
  1. [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
  2. [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
  3. [Messaging Overview](https://hermes-agent.nousresearch.com/docs/user-guide/messaging)
  4. [Telegram Setup](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram)
  5. [Discord Setup](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord)
  6. [Use Voice Mode with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-voice-mode-with-hermes)


For full project examples, see:
  * [Daily Briefing Bot](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
  * [Team Telegram Assistant](https://hermes-agent.nousresearch.com/docs/guides/team-telegram-assistant)


### "I want to automate tasks"[​](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#i-want-to-automate-tasks "Direct link to "I want to automate tasks"")
Schedule recurring tasks, run batch jobs, or chain agent actions together.
  1. [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  2. [Cron Scheduling](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
  3. [Batch Processing](https://hermes-agent.nousresearch.com/docs/user-guide/features/batch-processing)


Cron jobs let Hermes Agent run tasks on a schedule — daily summaries, periodic checks, automated reports — without you being present.
### "I want to build custom tools/skills"[​](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#i-want-to-build-custom-toolsskills "Direct link to "I want to build custom tools/skills"")
Extend Hermes Agent with your own tools and reusable skill packages.
  1. [Build a Hermes Plugin](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin)
  2. [Tools Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)
  3. [Skills Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
  4. [MCP (Model Context Protocol)](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
  5. [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
  6. [Adding Tools](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
  7. [Creating Skills](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills)


For most custom tool creation, start with plugins. The [Adding Tools](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools) page is for built-in Hermes core development, not the usual user/custom-tool path.
### "I want to train models"[​](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#i-want-to-train-models "Direct link to "I want to train models"")
Use reinforcement learning to fine-tune model behavior with Hermes Agent's built-in RL training pipeline.
  1. [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  2. [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
  3. [RL Training](https://hermes-agent.nousresearch.com/docs/user-guide/features/rl-training)
  4. [Provider Routing](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
  5. [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)


RL training works best when you already understand the basics of how Hermes Agent handles conversations and tool calls. Run through the Beginner path first if you're new.
### "I want to use it as a Python library"[​](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#i-want-to-use-it-as-a-python-library "Direct link to "I want to use it as a Python library"")
Integrate Hermes Agent into your own Python applications programmatically.
  1. [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
  2. [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  3. [Python Library Guide](https://hermes-agent.nousresearch.com/docs/guides/python-library)
  4. [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)


## Key Features at a Glance[​](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#key-features-at-a-glance "Direct link to Key Features at a Glance")
Not sure what's available? Here's a quick directory of major features:  
| Feature  | What It Does  | Link  |  
| --- | --- | --- |  
| **Tools**  | Built-in tools the agent can call (file I/O, search, shell, etc.)  |  
| **Skills**  | Installable plugin packages that add new capabilities  |  
| **Memory**  | Persistent memory across sessions  |  
| **Context Files**  | Feed files and directories into conversations  | [Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)  |  
| **MCP**  | Connect to external tool servers via Model Context Protocol  |  
| **Cron**  | Schedule recurring agent tasks  |  
| **Delegation**  | Spawn sub-agents for parallel work  |  
| **Code Execution**  | Run Python scripts that call Hermes tools programmatically  | [Code Execution](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)  |  
| **Browser**  | Web browsing and scraping  |  
| **Hooks**  | Event-driven callbacks and middleware  |  
| **Batch Processing**  | Process multiple inputs in bulk  | [Batch Processing](https://hermes-agent.nousresearch.com/docs/user-guide/features/batch-processing)  |  
| **RL Training**  | Fine-tune models with reinforcement learning  | [RL Training](https://hermes-agent.nousresearch.com/docs/user-guide/features/rl-training)  |  
| **Provider Routing**  | Route requests across multiple LLM providers  | [Provider Routing](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)  |  
## What to Read Next[​](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#what-to-read-next "Direct link to What to Read Next")
Based on where you are right now:
  * **Just finished installing?** → Head to the [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart) to run your first conversation.
  * **Completed the Quickstart?** → Read [CLI Usage](https://hermes-agent.nousresearch.com/docs/user-guide/cli) and [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) to customize your setup.
  * **Comfortable with the basics?** → Explore [Tools](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools), [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills), and [Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) to unlock the full power of the agent.
  * **Setting up for a team?** → Read [Security](https://hermes-agent.nousresearch.com/docs/user-guide/security) and [Sessions](https://hermes-agent.nousresearch.com/docs/user-guide/sessions) to understand access control and conversation management.
  * **Ready to build?** → Jump into the [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture) to understand the internals and start contributing.
  * **Want practical examples?** → Check out the [Guides](https://hermes-agent.nousresearch.com/docs/guides/tips) section for real-world projects and tips.


You don't need to read everything. Pick the path that matches your goal, follow the links in order, and you'll be productive quickly. You can always come back to this page to find your next step.
  * [How to Use This Page](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#how-to-use-this-page)
  * [By Experience Level](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#by-experience-level)
  * [By Use Case](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#by-use-case)
    * ["I want a CLI coding assistant"](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#i-want-a-cli-coding-assistant)
    * ["I want a Telegram/Discord bot"](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#i-want-a-telegramdiscord-bot)
    * ["I want to automate tasks"](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#i-want-to-automate-tasks)
    * ["I want to build custom tools/skills"](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#i-want-to-build-custom-toolsskills)
    * ["I want to train models"](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#i-want-to-train-models)
    * ["I want to use it as a Python library"](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#i-want-to-use-it-as-a-python-library)
  * [Key Features at a Glance](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#key-features-at-a-glance)
  * [What to Read Next](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path#what-to-read-next)


