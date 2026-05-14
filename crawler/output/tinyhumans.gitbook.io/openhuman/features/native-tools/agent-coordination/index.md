<!-- Source: https://tinyhumans.gitbook.io/openhuman/features/native-tools/agent-coordination -->

Beyond doing the work, the agent has tools for _organising_ the work - planning multi-step jobs, delegating to specialists, spawning subagents, and pausing to ask the user when something is genuinely ambiguous.
## 
Tools in the family
Tool
What it does
`todo_write`
Maintain a structured TODO list across a long task. Marked done as work progresses.
`spawn_subagent`
Spin up a fresh agent with its own context window for a self-contained subtask.
`spawn_worker_thread`
Background work that doesn't need to block the main conversation.
`delegate`
Hand a task to a specialist (e.g. an archetype with different prompts/tools/permissions).
`archetype_delegation`
Route to a named archetype - coder, researcher, planner, etc.
`skill_delegation`
Hand off to a installed in the workspace.
`ask_clarification`
Pause and ask the user a precise question instead of guessing.
`plan_exit`
Exit a planning phase and start executing.
`check_onboarding_status` / `complete_onboarding`
Gate behaviour on whether the user has finished onboarding.
## 
Why these are tools, not implicit behaviour
Long tasks fall apart when the agent tries to keep everything in one head. Splitting work via TODOs and subagents means:
  * Each subagent gets a clean context - fewer tokens, fewer distractions.
  * The main thread keeps a high-level view of progress.
  * Failures in one branch don't poison the rest.


Asking for clarification is a tool too, on purpose: it makes "I should ask the user" a _visible_ decision the agent can be steered toward, not an emergent behaviour.
## 
See also
  * - what a coder-archetype subagent typically uses.
  * - the always-on background agent thread.


[PreviousThird-party Integrationschevron-left](https://tinyhumans.gitbook.io/openhuman/features/native-tools/integrations)[NextSystem & Utilitieschevron-right](https://tinyhumans.gitbook.io/openhuman/features/native-tools/system-and-utilities)
Last updated 4 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
