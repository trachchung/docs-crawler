<!-- Source: https://tinyhumans.gitbook.io/openhuman/features/native-tools/cron -->

Scheduling is a first-class capability, not a workaround. The agent can set up recurring jobs ("every weekday at 9am, summarise my inbox"), one-off reminders ("nudge me about this in three hours"), and arbitrary agent runs on a cron schedule.
## 
Tools in the family
Tool
What it does
`cron_add`
Create a new scheduled job - cron expression + agent prompt.
`cron_list`
List existing jobs and their next-run times.
`cron_update`
Edit an existing job - change schedule, prompt, or enabled state.
`cron_remove`
Delete a job.
`cron_run`
Run a job once, immediately, regardless of its schedule.
`cron_runs`
Inspect the recent run history - when, how long, what it produced.
There's also a one-shot `schedule` tool in for "do this once at time T" cases that don't need a recurring entry.
## 
What it's good for
  * Daily / weekly digests delivered to your messaging channel of choice.
  * Polling a slow integration that doesn't push events.
  * Reminders the agent itself owns ("remind me Thursday to follow up with Alice").
  * Recurring research - "every Monday, check what's new on this topic and write me a brief".


## 
How it ties back to the rest
Every cron run is just a normal agent invocation, so it can use any other tool - search the web, query the , call a , send a message. Run history is recorded so you can see what each tick produced.
## 
See also
  * - the one-shot `schedule` tool.
  * - for jobs that fan out into subagents.


[PreviousBrowser & Computer Controlchevron-left](https://tinyhumans.gitbook.io/openhuman/features/native-tools/browser-and-computer)[NextVoicechevron-right](https://tinyhumans.gitbook.io/openhuman/features/native-tools/voice)
Last updated 4 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
