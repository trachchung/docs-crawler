<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues -->

本页总览
Create, triage, label, assign GitHub issues via gh or REST.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#skill-metadata "Skill metadata的直接链接")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/github/github-issues`  |  
| Version  | `1.1.0`  |  
| Author  | Hermes Agent  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `GitHub`, `Issues`, `Project-Management`, `Bug-Tracking`, `Triage`  |  
| Related skills  |  [`github-auth`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/github/github-github-auth), [`github-pr-workflow`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/github/github-github-pr-workflow)  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# GitHub Issues Management
Create, search, triage, and manage GitHub issues. Each section shows `gh` first, then the `curl` fallback.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#prerequisites "Prerequisites的直接链接")
  * Authenticated with GitHub (see `github-auth` skill)
  * Inside a git repo with a GitHub remote, or specify the repo explicitly


### Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#setup "Setup的直接链接")

```
ifcommand-v gh &>/dev/null && gh auth status &>/dev/null;thenAUTH="gh"elseAUTH="git"if[-z"$GITHUB_TOKEN"];thenif[-f ~/.hermes/.env ]&&grep-q"^GITHUB_TOKEN=" ~/.hermes/.env;thenGITHUB_TOKEN=$(grep"^GITHUB_TOKEN=" ~/.hermes/.env |head-1|cut-d=-f2|tr-d'\n\r')elifgrep-q"github.com" ~/.git-credentials 2>/dev/null;thenGITHUB_TOKEN=$(grep"github.com" ~/.git-credentials 2>/dev/null |head-1|sed's|https://[^:]*:\([^@]*\)@.*|\1|')REMOTE_URL=$(git remote get-url origin)OWNER_REPO=$(echo"$REMOTE_URL"|sed-E's|.*github\.com[:/]||; s|\.git$||')OWNER=$(echo"$OWNER_REPO"|cut -d/ -f1)REPO=$(echo"$OWNER_REPO"|cut -d/ -f2)
```

## 1. Viewing Issues[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#1-viewing-issues "1. Viewing Issues的直接链接")
**With gh:**

```
gh issue listgh issue list --stateopen--label"bug"gh issue list --assignee @megh issue list --search"authentication error"--state allgh issue view 42
```

**With curl:**

```
# List open issuescurl-s\-H"Authorization: token $GITHUB_TOKEN"\"https://api.github.com/repos/$OWNER/$REPO/issues?state=open&per_page=20"\| python3 -c"import sys, jsonfor i in json.load(sys.stdin):    if 'pull_request' not in i:  # GitHub API returns PRs in /issues too        labels = ', '.join(l['name'] for l in i['labels'])        print(f\"#{i['number']:5}  {i['state']:6}  {labels:30}  {i['title']}\")"# Filter by labelcurl-s\-H"Authorization: token $GITHUB_TOKEN"\"https://api.github.com/repos/$OWNER/$REPO/issues?state=open&labels=bug&per_page=20"\| python3 -c"import sys, jsonfor i in json.load(sys.stdin):    if 'pull_request' not in i:        print(f\"#{i['number']}  {i['title']}\")"# View a specific issuecurl-s\-H"Authorization: token $GITHUB_TOKEN"\  https://api.github.com/repos/$OWNER/$REPO/issues/42 \| python3 -c"import sys, jsoni = json.load(sys.stdin)labels = ', '.join(l['name'] for l in i['labels'])assignees = ', '.join(a['login'] for a in i['assignees'])print(f\"#{i['number']}: {i['title']}\")print(f\"State: {i['state']}  Labels: {labels}  Assignees: {assignees}\")print(f\"Author: {i['user']['login']}  Created: {i['created_at']}\")print(f\"\n{i['body']}\")"# Search issuescurl-s\-H"Authorization: token $GITHUB_TOKEN"\"https://api.github.com/search/issues?q=authentication+error+repo:$OWNER/$REPO"\| python3 -c"import sys, jsonfor i in json.load(sys.stdin)['items']:    print(f\"#{i['number']}  {i['state']:6}  {i['title']}\")"
```

## 2. Creating Issues[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#2-creating-issues "2. Creating Issues的直接链接")
**With gh:**

```
gh issue create \--title"Login redirect ignores ?next= parameter"\--body"## DescriptionAfter logging in, users always land on /dashboard.## Steps to Reproduce1. Navigate to /settings while logged out2. Get redirected to /login?next=/settings3. Log in4. Actual: redirected to /dashboard (should go to /settings)## Expected BehaviorRespect the ?next= query parameter."\--label"bug,backend"\--assignee"username"
```

**With curl:**

```
curl-s-X POST \-H"Authorization: token $GITHUB_TOKEN"\  https://api.github.com/repos/$OWNER/$REPO/issues \-d'{    "title": "Login redirect ignores ?next= parameter",    "body": "## Description\nAfter logging in, users always land on /dashboard.\n\n## Steps to Reproduce\n1. Navigate to /settings while logged out\n2. Get redirected to /login?next=/settings\n3. Log in\n4. Actual: redirected to /dashboard\n\n## Expected Behavior\nRespect the ?next= query parameter.",    "labels": ["bug", "backend"],    "assignees": ["username"]
```

### Bug Report Template[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#bug-report-template "Bug Report Template的直接链接")

```
## Bug Description<What's happening>## Steps to Reproduce1. <step>2. <step>## Expected Behavior<What should happen>## Actual Behavior<What actually happens>## Environment- OS: <os>- Version: <version>
```

### Feature Request Template[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#feature-request-template "Feature Request Template的直接链接")

```
## Feature Description<What you want>## Motivation<Why this would be useful>## Proposed Solution<How it could work>## Alternatives Considered<Other approaches>
```

## 3. Managing Issues[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#3-managing-issues "3. Managing Issues的直接链接")
### Add/Remove Labels[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#addremove-labels "Add/Remove Labels的直接链接")
**With gh:**

```
gh issue edit 42 --add-label "priority:high,bug"gh issue edit 42 --remove-label "needs-triage"
```

**With curl:**

```
# Add labelscurl-s-X POST \-H"Authorization: token $GITHUB_TOKEN"\  https://api.github.com/repos/$OWNER/$REPO/issues/42/labels \-d'{"labels": ["priority:high", "bug"]}'# Remove a labelcurl-s-X DELETE \-H"Authorization: token $GITHUB_TOKEN"\  https://api.github.com/repos/$OWNER/$REPO/issues/42/labels/needs-triage# List available labels in the repocurl-s\-H"Authorization: token $GITHUB_TOKEN"\  https://api.github.com/repos/$OWNER/$REPO/labels \| python3 -c"import sys, jsonfor l in json.load(sys.stdin):    print(f\"  {l['name']:30}  {l.get('description', '')}\")"
```

### Assignment[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#assignment "Assignment的直接链接")
**With gh:**

```
gh issue edit 42 --add-assignee usernamegh issue edit 42 --add-assignee @me
```

**With curl:**

```
curl-s-X POST \-H"Authorization: token $GITHUB_TOKEN"\  https://api.github.com/repos/$OWNER/$REPO/issues/42/assignees \-d'{"assignees": ["username"]}'
```

### Commenting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#commenting "Commenting的直接链接")
**With gh:**

```
gh issue comment 42--body"Investigated — root cause is in auth middleware. Working on a fix."
```

**With curl:**

```
curl-s-X POST \-H"Authorization: token $GITHUB_TOKEN"\  https://api.github.com/repos/$OWNER/$REPO/issues/42/comments \-d'{"body": "Investigated — root cause is in auth middleware. Working on a fix."}'
```

### Closing and Reopening[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#closing-and-reopening "Closing and Reopening的直接链接")
**With gh:**

```
gh issue close 42gh issue close 42--reason"not planned"gh issue reopen 42
```

**With curl:**

```
# Closecurl-s-X PATCH \-H"Authorization: token $GITHUB_TOKEN"\  https://api.github.com/repos/$OWNER/$REPO/issues/42 \-d'{"state": "closed", "state_reason": "completed"}'# Reopencurl-s-X PATCH \-H"Authorization: token $GITHUB_TOKEN"\  https://api.github.com/repos/$OWNER/$REPO/issues/42 \-d'{"state": "open"}'
```

### Linking Issues to PRs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#linking-issues-to-prs "Linking Issues to PRs的直接链接")
Issues are automatically closed when a PR merges with the right keywords in the body:

```
Closes #42Fixes #42Resolves #42
```

To create a branch from an issue:
**With gh:**

```
gh issue develop 42--checkout
```

**With git (manual equivalent):**

```
git checkout main &&git pull origin maingit checkout -b fix/issue-42-login-redirect
```

## 4. Issue Triage Workflow[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#4-issue-triage-workflow "4. Issue Triage Workflow的直接链接")
When asked to triage issues:
  1. **List untriaged issues:**



```
# With ghgh issue list --label"needs-triage"--stateopen# With curlcurl-s\-H"Authorization: token $GITHUB_TOKEN"\"https://api.github.com/repos/$OWNER/$REPO/issues?labels=needs-triage&state=open"\| python3 -c"import sys, jsonfor i in json.load(sys.stdin):    if 'pull_request' not in i:        print(f\"#{i['number']}  {i['title']}\")"
```

  1. **Read and categorize** each issue (view details, understand the bug/feature)
  2. **Apply labels and priority** (see Managing Issues above)
  3. **Assign** if the owner is clear
  4. **Comment with triage notes** if needed


## 5. Bulk Operations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#5-bulk-operations "5. Bulk Operations的直接链接")
For batch operations, combine API calls with shell scripting:
**With gh:**

```
# Close all issues with a specific labelgh issue list --label"wontfix"--json number --jq'.[].number'|\xargs-I{} gh issue close {}--reason"not planned"
```

**With curl:**

```
# List issue numbers with a label, then close eachcurl-s\-H"Authorization: token $GITHUB_TOKEN"\"https://api.github.com/repos/$OWNER/$REPO/issues?labels=wontfix&state=open"\| python3 -c"import sys,json; [print(i['number']) for i in json.load(sys.stdin)]"\|whileread num;docurl-s-X PATCH \-H"Authorization: token $GITHUB_TOKEN"\      https://api.github.com/repos/$OWNER/$REPO/issues/$num\-d'{"state": "closed", "state_reason": "not_planned"}'echo"Closed #$num"done
```

## Quick Reference Table[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#quick-reference-table "Quick Reference Table的直接链接")  
| Action  | gh  | curl endpoint  |  
| --- | --- | --- |  
| List issues  | `gh issue list`  | `GET /repos/{o}/{r}/issues`  |  
| View issue  | `gh issue view N`  | `GET /repos/{o}/{r}/issues/N`  |  
| Create issue  | `gh issue create ...`  | `POST /repos/{o}/{r}/issues`  |  
| Add labels  | `gh issue edit N --add-label ...`  | `POST /repos/{o}/{r}/issues/N/labels`  |  
| Assign  | `gh issue edit N --add-assignee ...`  | `POST /repos/{o}/{r}/issues/N/assignees`  |  
| Comment  | `gh issue comment N --body ...`  | `POST /repos/{o}/{r}/issues/N/comments`  |  
| Close  | `gh issue close N`  | `PATCH /repos/{o}/{r}/issues/N`  |  
| Search  | `gh issue list --search "..."`  | `GET /search/issues?q=...`  |  
  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#reference-full-skillmd)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#prerequisites)
  * [1. Viewing Issues](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#1-viewing-issues)
  * [2. Creating Issues](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#2-creating-issues)
    * [Bug Report Template](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#bug-report-template)
    * [Feature Request Template](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#feature-request-template)
  * [3. Managing Issues](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#3-managing-issues)
    * [Add/Remove Labels](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#addremove-labels)
    * [Closing and Reopening](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#closing-and-reopening)
    * [Linking Issues to PRs](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#linking-issues-to-prs)
  * [4. Issue Triage Workflow](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#4-issue-triage-workflow)
  * [5. Bulk Operations](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#5-bulk-operations)
  * [Quick Reference Table](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/github/github-github-issues#quick-reference-table)


