<!-- Source: https://tinyhumans.gitbook.io/openhuman/features/native-tools/system-and-utilities -->

The catch-all family. Small, sharp tools the agent reaches for to round out a task.
## 
Tools in the family
Tool
What it does
`shell`
Run a shell command. Bounded output, captured exit code.
`node_exec`
Run a Node.js snippet - useful for one-off scripting.
`npm_exec`
Run an `npm`/`pnpm`/`yarn` script.
`current_time`
Get the current time in any timezone, with formatting options.
`schedule`
One-shot "do this once at time T" - for recurring jobs see .
`pushover`
Send a push notification to your devices.
`insert_sql_record`
Append a row to the agent's structured workspace SQL store.
`lsp`
Query a language server (definitions, references, diagnostics).
`workspace_state`
Inspect the current workspace - open files, recent edits, environment.
`proxy_config`
Read or change proxy configuration for outbound requests.
`tool_stats`
Self-reflection - what tools have been used in this session and how often.
## 
What it's good for
  * The bits of a workflow that don't fit a richer tool family.
  * "Just run this command and tell me what it printed."
  * Time-aware behaviour ("what time is it for the user right now?") without baking timezone assumptions into prompts.
  * Letting the agent _notify you_ when it's done with a long-running job.


## 
See also
  * - for filesystem-heavy work, prefer the dedicated tools over `shell`.
  * - for anything recurring.


[PreviousAgent Coordinationchevron-left](https://tinyhumans.gitbook.io/openhuman/features/native-tools/agent-coordination)[NextSubconscious Loopchevron-right](https://tinyhumans.gitbook.io/openhuman/features/subconscious)
Last updated 4 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
