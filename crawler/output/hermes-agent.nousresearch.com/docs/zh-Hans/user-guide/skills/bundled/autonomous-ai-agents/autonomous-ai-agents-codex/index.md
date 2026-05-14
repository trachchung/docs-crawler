<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex -->

本页总览
Delegate coding to OpenAI Codex CLI (features, PRs).
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#skill-metadata "Skill metadata的直接链接")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/autonomous-ai-agents/codex`  |  
| Version  | `1.0.0`  |  
| Author  | Hermes Agent  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `Coding-Agent`, `Codex`, `OpenAI`, `Code-Review`, `Refactoring`  |  
| Related skills  |  [`claude-code`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-claude-code), [`hermes-agent`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-hermes-agent)  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Codex CLI
Delegate coding tasks to [Codex](https://github.com/openai/codex) via the Hermes terminal. Codex is OpenAI's autonomous coding agent CLI.
## When to use[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#when-to-use "When to use的直接链接")
  * Building features
  * Refactoring
  * PR reviews
  * Batch issue fixing


Requires the codex CLI and a git repository.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#prerequisites "Prerequisites的直接链接")
  * Codex installed: `npm install -g @openai/codex`
  * OpenAI auth configured: either `OPENAI_API_KEY` or Codex OAuth credentials from the Codex CLI login flow
  * **Must run inside a git repository** — Codex refuses to run outside one
  * Use `pty=true` in terminal calls — Codex is an interactive terminal app


For Hermes itself, `model.provider: openai-codex` uses Hermes-managed Codex OAuth from `~/.hermes/auth.json` after `hermes auth add openai-codex`. For the standalone Codex CLI, a valid CLI OAuth session may live under `~/.codex/auth.json`; do not treat a missing `OPENAI_API_KEY` alone as proof that Codex auth is missing.
## One-Shot Tasks[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#one-shot-tasks "One-Shot Tasks的直接链接")

```
terminal(command="codex exec 'Add dark mode toggle to settings'", workdir="~/project", pty=true)
```

For scratch work (Codex needs a git repo):

```
terminal(command="cd $(mktemp -d) && git init && codex exec 'Build a snake game in Python'", pty=true)
```

## Background Mode (Long Tasks)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#background-mode-long-tasks "Background Mode \(Long Tasks\)的直接链接")

```
# Start in background with PTYterminal(command="codex exec --full-auto 'Refactor the auth module'", workdir="~/project", background=true, pty=true)# Returns session_id# Monitor progressprocess(action="poll", session_id="<id>")process(action="log", session_id="<id>")# Send input if Codex asks a questionprocess(action="submit", session_id="<id>", data="yes")# Kill if neededprocess(action="kill", session_id="<id>")
```

## Key Flags[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#key-flags "Key Flags的直接链接")  
| Flag  | Effect  |  
| --- | --- |  
| `exec "prompt"`  | One-shot execution, exits when done  |  
| `--full-auto`  | Sandboxed but auto-approves file changes in workspace  |  
| `--yolo`  | No sandbox, no approvals (fastest, most dangerous)  |  
## PR Reviews[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#pr-reviews "PR Reviews的直接链接")
Clone to a temp directory for safe review:

```
terminal(command="REVIEW=$(mktemp -d) && git clone https://github.com/user/repo.git $REVIEW && cd $REVIEW && gh pr checkout 42 && codex review --base origin/main", pty=true)
```

## Parallel Issue Fixing with Worktrees[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#parallel-issue-fixing-with-worktrees "Parallel Issue Fixing with Worktrees的直接链接")

```
# Create worktreesterminal(command="git worktree add -b fix/issue-78 /tmp/issue-78 main", workdir="~/project")terminal(command="git worktree add -b fix/issue-99 /tmp/issue-99 main", workdir="~/project")# Launch Codex in eachterminal(command="codex --yolo exec 'Fix issue #78: <description>. Commit when done.'", workdir="/tmp/issue-78", background=true, pty=true)terminal(command="codex --yolo exec 'Fix issue #99: <description>. Commit when done.'", workdir="/tmp/issue-99", background=true, pty=true)# Monitorprocess(action="list")# After completion, push and create PRsterminal(command="cd /tmp/issue-78 && git push -u origin fix/issue-78")terminal(command="gh pr create --repo user/repo --head fix/issue-78 --title 'fix: ...' --body '...'")# Cleanupterminal(command="git worktree remove /tmp/issue-78", workdir="~/project")
```

## Batch PR Reviews[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#batch-pr-reviews "Batch PR Reviews的直接链接")

```
# Fetch all PR refsterminal(command="git fetch origin '+refs/pull/*/head:refs/remotes/origin/pr/*'", workdir="~/project")# Review multiple PRs in parallelterminal(command="codex exec 'Review PR #86. git diff origin/main...origin/pr/86'", workdir="~/project", background=true, pty=true)terminal(command="codex exec 'Review PR #87. git diff origin/main...origin/pr/87'", workdir="~/project", background=true, pty=true)# Post resultsterminal(command="gh pr comment 86 --body '<review>'", workdir="~/project")
```

## Rules[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#rules "Rules的直接链接")
  1. **Always use`pty=true`** — Codex is an interactive terminal app and hangs without a PTY
  2. **Git repo required** — Codex won't run outside a git directory. Use `mktemp -d && git init` for scratch
  3. **Use`exec` for one-shots** — `codex exec "prompt"` runs and exits cleanly
  4. **`--full-auto`for building** — auto-approves changes within the sandbox
  5. **Background for long tasks** — use `background=true` and monitor with `process` tool
  6. **Don't interfere** — monitor with `poll`/`log`, be patient with long-running tasks
  7. **Parallel is fine** — run multiple Codex processes at once for batch work


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#reference-full-skillmd)
  * [When to use](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#when-to-use)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#prerequisites)
  * [One-Shot Tasks](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#one-shot-tasks)
  * [Background Mode (Long Tasks)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#background-mode-long-tasks)
  * [Parallel Issue Fixing with Worktrees](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#parallel-issue-fixing-with-worktrees)
  * [Batch PR Reviews](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex#batch-pr-reviews)


