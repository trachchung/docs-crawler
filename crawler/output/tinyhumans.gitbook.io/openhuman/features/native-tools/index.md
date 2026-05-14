<!-- Source: https://tinyhumans.gitbook.io/openhuman/features/native-tools -->

OpenHuman's agent doesn't ship empty. Every model behind the agent has a curated set of tools available the moment you install - no plugin marketplace, no API keys to wire up, no MCP servers to register. The whole toolbelt is in the box.
This page is the index. Each subpage covers one family of tools.
## 
Why ship them natively
A plugin-only model means tools live in different processes, behind RPC, with their own auth and packaging stories. That's fine for open-ended extensibility, but for the **core** tools every agent needs (read a file, search the web, edit code, set a reminder, join a meeting), shipping them in-process means:
  * Consistent error handling.
  * Zero install friction.
  * All output passes through for free.
  * Predictable security boundary - filesystem tools respect workspace scoping, network tools go through the OpenHuman proxy.


## 
The toolbelt
Family
What it covers
Search the live web without bringing your own API key.
Pull clean text out of any URL - articles, docs, READMEs.
Read/write/edit/patch files, glob, grep, git, lint, test.
[Browser & Computer Control](https://tinyhumans.gitbook.io/openhuman/features/native-tools/browser-and-computer)
Open URLs, screenshot, click, type, move the mouse.
Recurring jobs, one-off reminders, scheduled agent runs.
Speech-to-text in, text-to-speech out, live Google Meet agent.
Recall, store, forget, and search the .
[Third-party Integrations](https://tinyhumans.gitbook.io/openhuman/features/integrations)
The agent's view of the .
Spawn subagents, delegate to skills, plan, ask the user.
Shell, node, SQL, current time, push notifications, LSP.
## 
See also
  * - what keeps tool output costs bounded.
  * [Third-party Integrations](https://tinyhumans.gitbook.io/openhuman/features/integrations) - the user-facing pitch and OAuth flow for the 118+ catalog.
  * - the boundary every tool runs inside.


[PreviousLocal AI (optional)chevron-left](https://tinyhumans.gitbook.io/openhuman/features/model-routing/local-ai)[NextWeb Searchchevron-right](https://tinyhumans.gitbook.io/openhuman/features/native-tools/web-search)
Last updated 4 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
