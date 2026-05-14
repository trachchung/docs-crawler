<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#__docusaurus_skipToContent_fallback)
On this page
Pitfalls, examples, and edge cases for Hermes Kanban workers. The lifecycle itself is auto-injected into every worker's system prompt as KANBAN_GUIDANCE (from agent/prompt_builder.py); this skill is what you load when you want deeper detail on specific scenarios.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#skill-metadata "Direct link to Skill metadata")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/devops/kanban-worker`  |  
| Version  | `2.0.0`  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `kanban`, `multi-agent`, `collaboration`, `workflow`, `pitfalls`  |  
| Related skills  | [`kanban-orchestrator`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-orchestrator)  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Kanban Worker — Pitfalls and Examples
> You're seeing this skill because the Hermes Kanban dispatcher spawned you as a worker with `--skills kanban-worker` — it's loaded automatically for every dispatched worker. The **lifecycle** (6 steps: orient → work → heartbeat → block/complete) also lives in the `KANBAN_GUIDANCE` block that's auto-injected into your system prompt. This skill is the deeper detail: good handoff shapes, retry diagnostics, edge cases.
## Workspace handling[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#workspace-handling "Direct link to Workspace handling")
Your workspace kind determines how you should behave inside `$HERMES_KANBAN_WORKSPACE`:  
| Kind  | What it is  | How to work  |  
| --- | --- | --- |  
| `scratch`  | Fresh tmp dir, yours alone  | Read/write freely; it gets GC'd when the task is archived.  |  
| `dir:<path>`  | Shared persistent directory  | Other runs will read what you write. Treat it like long-lived state. Path is guaranteed absolute (the kernel rejects relative paths).  |  
| `worktree`  | Git worktree at the resolved path  | If `.git` doesn't exist, run `git worktree add <path> <branch>` from the main repo first, then cd and work normally. Commit work here.  |  
## Tenant isolation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#tenant-isolation "Direct link to Tenant isolation")
If `$HERMES_TENANT` is set, the task belongs to a tenant namespace. When reading or writing persistent memory, prefix memory entries with the tenant so context doesn't leak across tenants:
  * Good: `business-a: Acme is our biggest customer`
  * Bad (leaks): `Acme is our biggest customer`


## Good summary + metadata shapes[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#good-summary--metadata-shapes "Direct link to Good summary + metadata shapes")
The `kanban_complete(summary=..., metadata=...)` handoff is how downstream workers read what you did. Patterns that work:
**Coding task:**

```
kanban_complete(    summary="shipped rate limiter — token bucket, keys on user_id with IP fallback, 14 tests pass",    metadata={"changed_files":["rate_limiter.py","tests/test_rate_limiter.py"],"tests_run":14,"tests_passed":14,"decisions":["user_id primary, IP fallback for unauthenticated requests"],
```

**Coding task that needs human review (review-required):**
For most code-changing tasks, the work isn't truly _done_ until a human reviewer has eyes on it. Block instead of complete, with `reason` prefixed `review-required: ` so the dashboard surfaces the row as needing review. Drop the structured metadata (changed files, test counts, diff/PR url) into a comment first, since `kanban_block` only carries the human-readable reason — comments are the durable annotation channel. Reviewer either approves and runs `hermes kanban unblock <id>` (which re-spawns you with the comment thread for any follow-ups) or asks for changes via another comment.

```
import jsonkanban_comment(    body="review-required handoff:\n"+ json.dumps({"changed_files":["rate_limiter.py","tests/test_rate_limiter.py"],"tests_run":14,"tests_passed":14,"diff_path":"/path/to/worktree",# or PR url if pushed"decisions":["user_id primary, IP fallback for unauthenticated requests"],}, indent=2),kanban_block(    reason="review-required: rate limiter shipped, 14/14 tests pass — needs eyes on the user_id/IP fallback choice before merging",
```

Use `kanban_complete` only when the task is genuinely terminal — e.g. a one-line typo fix, a docs change with no functional consequences, or a research task where the artifact IS the writeup itself.
**Research task:**

```
kanban_complete(    summary="3 competing libraries reviewed; vLLM wins on throughput, SGLang on latency, Tensorrt-LLM on memory efficiency",    metadata={"sources_read":12,"recommendation":"vLLM","benchmarks":{"vllm":1.0,"sglang":0.87,"trtllm":0.72},
```

**Review task:**

```
kanban_complete(    summary="reviewed PR #123; 2 blocking issues found (SQL injection in /search, missing CSRF on /settings)",    metadata={"pr_number":123,"findings":[{"severity":"critical","file":"api/search.py","line":42,"issue":"raw SQL concat"},{"severity":"high","file":"api/settings.py","issue":"missing CSRF middleware"},"approved":False,
```

Shape `metadata` so downstream parsers (reviewers, aggregators, schedulers) can use it without re-reading your prose.
## Claiming cards you actually created[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#claiming-cards-you-actually-created "Direct link to Claiming cards you actually created")
If your run produced new kanban tasks (via `kanban_create`), pass the ids in `created_cards` on `kanban_complete`. The kernel verifies each id exists and was created by your profile; any phantom id blocks the completion with an error listing what went wrong, and the rejected attempt is permanently recorded on the task's event log. **Only list ids you captured from a successful`kanban_create` return value — never invent ids from prose, never paste ids from earlier runs, never claim cards another worker created.**

```
# GOOD — capture return values, then claim them.c1 = kanban_create(title="remediate SQL injection", assignee="security-worker")c2 = kanban_create(title="fix CSRF middleware", assignee="web-worker")kanban_complete(    summary="Review done; spawned remediations for both findings.",    metadata={"pr_number":123,"approved":False},    created_cards=[c1["task_id"], c2["task_id"]],
```


```
# BAD — claiming ids you don't have captured return values for.kanban_complete(    summary="Created remediation cards t_a1b2c3d4, t_deadbeef",# hallucinated    created_cards=["t_a1b2c3d4","t_deadbeef"],# → gate rejects
```

If a `kanban_create` call fails (exception, tool_error), the card was NOT created — do not include a phantom id for it. Retry the create, or omit the id and mention the failure in your summary. The prose-scan pass also catches `t_<hex>` references in your free-form summary that don't resolve; these don't block the completion but show up as advisory warnings on the task in the dashboard.
## Block reasons that get answered fast[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#block-reasons-that-get-answered-fast "Direct link to Block reasons that get answered fast")
Bad: `"stuck"` — the human has no context.
Good: one sentence naming the specific decision you need. Leave longer context as a comment instead.

```
kanban_comment(    task_id=os.environ["HERMES_KANBAN_TASK"],    body="Full context: I have user IPs from Cloudflare headers but some users are behind NATs with thousands of peers. Keying on IP alone causes false positives.",kanban_block(reason="Rate limit key choice: IP (simple, NAT-unsafe) or user_id (requires auth, skips anonymous endpoints)?")
```

The block message is what appears in the dashboard / gateway notifier. The comment is the deeper context a human reads when they open the task.
## Heartbeats worth sending[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#heartbeats-worth-sending "Direct link to Heartbeats worth sending")
Good heartbeats name progress: `"epoch 12/50, loss 0.31"`, `"scanned 1.2M/2.4M rows"`, `"uploaded 47/120 videos"`.
Bad heartbeats: `"still working"`, empty notes, sub-second intervals. Every few minutes max; skip entirely for tasks under ~2 minutes.
## Retry scenarios[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#retry-scenarios "Direct link to Retry scenarios")
If you open the task and `kanban_show` returns `runs: [...]` with one or more closed runs, you're a retry. The prior runs' `outcome` / `summary` / `error` tell you what didn't work. Don't repeat that path. Typical retry diagnostics:
  * `outcome: "timed_out"` — the previous attempt hit `max_runtime_seconds`. You may need to chunk the work or shorten it.
  * `outcome: "crashed"` — OOM or segfault. Reduce memory footprint.
  * `outcome: "spawn_failed"` + `error: "..."` — usually a profile config issue (missing credential, bad PATH). Ask the human via `kanban_block` instead of retrying blindly.
  * `outcome: "reclaimed"` + `summary: "task archived..."` — operator archived the task out from under the previous run; you probably shouldn't be running at all, check status carefully.
  * `outcome: "blocked"` — a previous attempt blocked; the unblock comment should be in the thread by now.


## Do NOT[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#do-not "Direct link to Do NOT")
  * Call `delegate_task` as a substitute for `kanban_create`. `delegate_task` is for short reasoning subtasks inside YOUR run; `kanban_create` is for cross-agent handoffs that outlive one API loop.
  * Modify files outside `$HERMES_KANBAN_WORKSPACE` unless the task body says to.
  * Create follow-up tasks assigned to yourself — assign to the right specialist.
  * Complete a task you didn't actually finish. Block it instead.


## Pitfalls[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#pitfalls "Direct link to Pitfalls")
**Task state can change between dispatch and your startup.** Between when the dispatcher claimed and when your process actually booted, the task may have been blocked, reassigned, or archived. Always `kanban_show` first. If it reports `blocked` or `archived`, stop — you shouldn't be running.
**Workspace may have stale artifacts.** Especially `dir:` and `worktree` workspaces can have files from previous runs. Read the comment thread — it usually explains why you're running again and what state the workspace is in.
**Don't rely on the CLI when the guidance is available.** The `kanban_*` tools work across all terminal backends (Docker, Modal, SSH). `hermes kanban <verb>` from your terminal tool will fail in containerized backends because the CLI isn't installed there. When in doubt, use the tool.
## CLI fallback (for scripting)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#cli-fallback-for-scripting "Direct link to CLI fallback \(for scripting\)")
Every tool has a CLI equivalent for human operators and scripts:
  * `kanban_show` ↔ `hermes kanban show <id> --json`
  * `kanban_complete` ↔ `hermes kanban complete <id> --summary "..." --metadata '{...}'`
  * `kanban_block` ↔ `hermes kanban block <id> "reason"`
  * `kanban_create` ↔ `hermes kanban create "title" --assignee <profile> [--parent <id>]`
  * etc.


Use the tools from inside an agent; the CLI exists for the human at the terminal.
  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#reference-full-skillmd)
  * [Workspace handling](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#workspace-handling)
  * [Tenant isolation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#tenant-isolation)
  * [Good summary + metadata shapes](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#good-summary--metadata-shapes)
  * [Claiming cards you actually created](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#claiming-cards-you-actually-created)
  * [Block reasons that get answered fast](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#block-reasons-that-get-answered-fast)
  * [Heartbeats worth sending](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#heartbeats-worth-sending)
  * [Retry scenarios](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#retry-scenarios)
  * [CLI fallback (for scripting)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/devops/devops-kanban-worker#cli-fallback-for-scripting)


