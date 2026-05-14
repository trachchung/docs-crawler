<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear -->

本页总览
Linear: manage issues, projects, teams via GraphQL + curl.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#skill-metadata "Skill metadata的直接链接")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/productivity/linear`  |  
| Version  | `1.0.0`  |  
| Author  | Hermes Agent  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `Linear`, `Project Management`, `Issues`, `GraphQL`, `API`, `Productivity`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Linear — Issue & Project Management
Manage Linear issues, projects, and teams directly via the GraphQL API using `curl`. No MCP server, no OAuth flow, no extra dependencies.
## Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#setup "Setup的直接链接")
  1. Get a personal API key from **Linear Settings > Account > Security & access > Personal API keys** (URL: <https://linear.app/settings/account/security>). Note: the org-level _Settings > API_ page only shows OAuth apps and workspace-member keys, not personal keys.
  2. Set `LINEAR_API_KEY` in your environment (via `hermes setup` or your env config)


## API Basics[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#api-basics "API Basics的直接链接")
  * **Endpoint:** `https://api.linear.app/graphql` (POST)
  * **Auth header:** `Authorization: $LINEAR_API_KEY` (no "Bearer" prefix for API keys)
  * **All requests are POST** with `Content-Type: application/json`
  * **Both UUIDs and short identifiers** (e.g., `ENG-123`) work for `issue(id:)`


Base curl pattern:

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ viewer { id name } }"}'| python3 -m json.tool
```

## Python helper script (ergonomic alternative)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#python-helper-script-ergonomic-alternative "Python helper script \(ergonomic alternative\)的直接链接")
For faster one-liners that don't need hand-written GraphQL, this skill ships a stdlib Python CLI at `scripts/linear_api.py`. Zero dependencies. Same auth (reads `LINEAR_API_KEY`).

```
SCRIPT=$(dirname"$(find ~/.hermes -path'*skills/productivity/linear/scripts/linear_api.py'2>/dev/null |head-1)")/linear_api.pypython3 "$SCRIPT"whoamipython3 "$SCRIPT" list-teamspython3 "$SCRIPT" get-issue ENG-42python3 "$SCRIPT" get-document 38359beef67c      # fetch a doc by slugId from the URLpython3 "$SCRIPT" raw 'query { viewer { name } }'
```

All subcommands: `whoami`, `list-teams`, `list-projects`, `list-states`, `list-issues`, `get-issue`, `search-issues`, `create-issue`, `update-issue`, `update-status`, `add-comment`, `list-documents`, `get-document`, `search-documents`, `raw`. Run with `--help` for flags.
Use the script when: you want a quick answer without crafting GraphQL. Use curl when: you need a query the script doesn't wrap, or you want to compose filters inline.
## Workflow States[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#workflow-states "Workflow States的直接链接")
Linear uses `WorkflowState` objects with a `type` field. **6 state types:**  
| Type  | Description  |  
| --- | --- |  
| `triage`  | Incoming issues needing review  |  
| `backlog`  | Acknowledged but not yet planned  |  
| `unstarted`  | Planned/ready but not started  |  
| `started`  | Actively being worked on  |  
| `completed`  | Done  |  
| `canceled`  | Won't do  |  
Each team has its own named states (e.g., "In Progress" is type `started`). To change an issue's status, you need the `stateId` (UUID) of the target state — query workflow states first.
**Priority values:** 0 = None, 1 = Urgent, 2 = High, 3 = Medium, 4 = Low
## Common Queries[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#common-queries "Common Queries的直接链接")
### Get current user[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#get-current-user "Get current user的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ viewer { id name email } }"}'| python3 -m json.tool
```

### List teams[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-teams "List teams的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ teams { nodes { id name key } } }"}'| python3 -m json.tool
```

### List workflow states for a team[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-workflow-states-for-a-team "List workflow states for a team的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ workflowStates(filter: { team: { key: { eq: \"ENG\" } } }) { nodes { id name type } } }"}'| python3 -m json.tool
```

### List issues (first 20)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-issues-first-20 "List issues \(first 20\)的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ issues(first: 20) { nodes { identifier title priority state { name type } assignee { name } team { key } url } pageInfo { hasNextPage endCursor } } }"}'| python3 -m json.tool
```

### List my assigned issues[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-my-assigned-issues "List my assigned issues的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ viewer { assignedIssues(first: 25) { nodes { identifier title state { name type } priority url } } } }"}'| python3 -m json.tool
```

### Get a single issue (by identifier like ENG-123)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#get-a-single-issue-by-identifier-like-eng-123 "Get a single issue \(by identifier like ENG-123\)的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ issue(id: \"ENG-123\") { id identifier title description priority state { id name type } assignee { id name } team { key } project { name } labels { nodes { name } } comments { nodes { body user { name } createdAt } } url } }"}'| python3 -m json.tool
```

### Search issues by text[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#search-issues-by-text "Search issues by text的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ issueSearch(query: \"bug login\", first: 10) { nodes { identifier title state { name } assignee { name } url } } }"}'| python3 -m json.tool
```

### Filter issues by state type[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#filter-issues-by-state-type "Filter issues by state type的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ issues(filter: { state: { type: { in: [\"started\"] } } }, first: 20) { nodes { identifier title state { name } assignee { name } } } }"}'| python3 -m json.tool
```

### Filter by team and assignee[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#filter-by-team-and-assignee "Filter by team and assignee的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ issues(filter: { team: { key: { eq: \"ENG\" } }, assignee: { email: { eq: \"user@example.com\" } } }, first: 20) { nodes { identifier title state { name } priority } } }"}'| python3 -m json.tool
```

### List projects[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-projects "List projects的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ projects(first: 20) { nodes { id name description progress lead { name } teams { nodes { key } } url } } }"}'| python3 -m json.tool
```

### List team members[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-team-members "List team members的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ users { nodes { id name email active } } }"}'| python3 -m json.tool
```

### List labels[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-labels "List labels的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ issueLabels { nodes { id name color } } }"}'| python3 -m json.tool
```

## Common Mutations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#common-mutations "Common Mutations的直接链接")
### Create an issue[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#create-an-issue "Create an issue的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{    "query": "mutation($input: IssueCreateInput!) { issueCreate(input: $input) { success issue { id identifier title url } } }",    "variables": {      "input": {        "teamId": "TEAM_UUID",        "title": "Fix login bug",        "description": "Users cannot login with SSO",        "priority": 2  }'| python3 -m json.tool
```

### Update issue status[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#update-issue-status "Update issue status的直接链接")
First get the target state UUID from the workflow states query above, then:

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "mutation { issueUpdate(id: \"ENG-123\", input: { stateId: \"STATE_UUID\" }) { success issue { identifier state { name type } } } }"}'| python3 -m json.tool
```

### Assign an issue[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#assign-an-issue "Assign an issue的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "mutation { issueUpdate(id: \"ENG-123\", input: { assigneeId: \"USER_UUID\" }) { success issue { identifier assignee { name } } } }"}'| python3 -m json.tool
```

### Set priority[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#set-priority "Set priority的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "mutation { issueUpdate(id: \"ENG-123\", input: { priority: 1 }) { success issue { identifier priority } } }"}'| python3 -m json.tool
```

### Add a comment[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#add-a-comment "Add a comment的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "mutation { commentCreate(input: { issueId: \"ISSUE_UUID\", body: \"Investigated. Root cause is X.\" }) { success comment { id body } } }"}'| python3 -m json.tool
```

### Set due date[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#set-due-date "Set due date的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "mutation { issueUpdate(id: \"ENG-123\", input: { dueDate: \"2026-04-01\" }) { success issue { identifier dueDate } } }"}'| python3 -m json.tool
```

### Add labels to an issue[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#add-labels-to-an-issue "Add labels to an issue的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "mutation { issueUpdate(id: \"ENG-123\", input: { labelIds: [\"LABEL_UUID_1\", \"LABEL_UUID_2\"] }) { success issue { identifier labels { nodes { name } } } } }"}'| python3 -m json.tool
```

### Add issue to a project[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#add-issue-to-a-project "Add issue to a project的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "mutation { issueUpdate(id: \"ENG-123\", input: { projectId: \"PROJECT_UUID\" }) { success issue { identifier project { name } } } }"}'| python3 -m json.tool
```

### Create a project[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#create-a-project "Create a project的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{    "query": "mutation($input: ProjectCreateInput!) { projectCreate(input: $input) { success project { id name url } } }",    "variables": {      "input": {        "name": "Q2 Auth Overhaul",        "description": "Replace legacy auth with OAuth2 and PKCE",        "teamIds": ["TEAM_UUID"]  }'| python3 -m json.tool
```

## Documents[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#documents "Documents的直接链接")
Linear **Documents** are prose docs (RFCs, specs, notes) stored alongside issues. They have their own `documents` root query and `document(id:)` single-fetch.
### Document URLs and `slugId`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#document-urls-and-slugid "document-urls-and-slugid的直接链接")
Document URLs look like:

```
https://linear.app/<workspace>/document/<slug>-<hexSlugId>
```

The trailing hex segment is the `slugId`. Example: `https://linear.app/nousresearch/document/rfc-hermes-permission-gateway-discord-38359beef67c` → `slugId` is `38359beef67c`.
**Important schema detail:** the Markdown body is in the `content` field. The ProseMirror JSON is in `contentState` (not `contentData` — that field does not exist and the API returns 400).
### Fetch a document by slugId[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#fetch-a-document-by-slugid "Fetch a document by slugId的直接链接")
`document(id:)` only accepts UUIDs. To fetch by the URL's hex slug, filter the collection:

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "query($s: String!) { documents(filter: { slugId: { eq: $s } }, first: 1) { nodes { id title content contentState slugId url creator { name } project { name } updatedAt } } }", "variables": {"s": "38359beef67c"}}'\| python3 -m json.tool
```

Or via the Python helper:

```
python3 scripts/linear_api.py get-document 38359beef67c
```

### Fetch a document by UUID[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#fetch-a-document-by-uuid "Fetch a document by UUID的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ document(id: \"11700cff-b514-4db3-afcc-3ed1afacba1c\") { title content url } }"}'\| python3 -m json.tool
```

### List recent documents[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-recent-documents "List recent documents的直接链接")

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ documents(first: 25, orderBy: updatedAt) { nodes { id title slugId url updatedAt project { name } } } }"}'\| python3 -m json.tool
```

### Search documents by title[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#search-documents-by-title "Search documents by title的直接链接")
Linear's schema has no `searchDocuments` root. Use a title-substring filter instead:

```
curl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ documents(filter: { title: { containsIgnoreCase: \"RFC\" } }, first: 25) { nodes { title slugId url } } }"}'\| python3 -m json.tool
```

## Pagination[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#pagination "Pagination的直接链接")
Linear uses Relay-style cursor pagination:

```
# First pagecurl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ issues(first: 20) { nodes { identifier title } pageInfo { hasNextPage endCursor } } }"}'| python3 -m json.tool# Next page — use endCursor from previous responsecurl-s-X POST https://api.linear.app/graphql \-H"Authorization: $LINEAR_API_KEY"\-H"Content-Type: application/json"\-d'{"query": "{ issues(first: 20, after: \"CURSOR_FROM_PREVIOUS\") { nodes { identifier title } pageInfo { hasNextPage endCursor } } }"}'| python3 -m json.tool
```

Default page size: 50. Max: 250. Always use `first: N` to limit results.
## Filtering Reference[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#filtering-reference "Filtering Reference的直接链接")
Comparators: `eq`, `neq`, `in`, `nin`, `lt`, `lte`, `gt`, `gte`, `contains`, `startsWith`, `containsIgnoreCase`
Combine filters with `or: [...]` for OR logic (default is AND within a filter object).
## Typical Workflow[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#typical-workflow "Typical Workflow的直接链接")
  1. **Query teams** to get team IDs and keys
  2. **Query workflow states** for target team to get state UUIDs
  3. **List or search issues** to find what needs work
  4. **Create issues** with team ID, title, description, priority
  5. **Update status** by setting `stateId` to the target workflow state
  6. **Add comments** to track progress
  7. **Mark complete** by setting `stateId` to the team's "completed" type state


## Rate Limits[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#rate-limits "Rate Limits的直接链接")
  * 5,000 requests/hour per API key
  * 3,000,000 complexity points/hour
  * Use `first: N` to limit results and reduce complexity cost
  * Monitor `X-RateLimit-Requests-Remaining` response header


## Important Notes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#important-notes "Important Notes的直接链接")
  * Always use `terminal` tool with `curl` for API calls — do NOT use `web_extract` or `browser`
  * Always check the `errors` array in GraphQL responses — HTTP 200 can still contain errors
  * If `stateId` is omitted when creating issues, Linear defaults to the first backlog state
  * The `description` field supports Markdown
  * Use `python3 -m json.tool` or `jq` to format JSON responses for readability


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#reference-full-skillmd)
  * [Python helper script (ergonomic alternative)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#python-helper-script-ergonomic-alternative)
  * [Workflow States](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#workflow-states)
  * [Common Queries](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#common-queries)
    * [Get current user](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#get-current-user)
    * [List workflow states for a team](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-workflow-states-for-a-team)
    * [List issues (first 20)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-issues-first-20)
    * [List my assigned issues](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-my-assigned-issues)
    * [Get a single issue (by identifier like ENG-123)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#get-a-single-issue-by-identifier-like-eng-123)
    * [Search issues by text](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#search-issues-by-text)
    * [Filter issues by state type](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#filter-issues-by-state-type)
    * [Filter by team and assignee](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#filter-by-team-and-assignee)
    * [List projects](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-projects)
    * [List team members](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-team-members)
    * [List labels](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-labels)
  * [Common Mutations](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#common-mutations)
    * [Create an issue](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#create-an-issue)
    * [Update issue status](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#update-issue-status)
    * [Assign an issue](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#assign-an-issue)
    * [Set priority](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#set-priority)
    * [Add a comment](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#add-a-comment)
    * [Set due date](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#set-due-date)
    * [Add labels to an issue](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#add-labels-to-an-issue)
    * [Add issue to a project](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#add-issue-to-a-project)
    * [Create a project](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#create-a-project)
  * [Documents](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#documents)
    * [Document URLs and `slugId`](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#document-urls-and-slugid)
    * [Fetch a document by slugId](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#fetch-a-document-by-slugid)
    * [Fetch a document by UUID](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#fetch-a-document-by-uuid)
    * [List recent documents](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#list-recent-documents)
    * [Search documents by title](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#search-documents-by-title)
  * [Filtering Reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#filtering-reference)
  * [Typical Workflow](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#typical-workflow)
  * [Rate Limits](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#rate-limits)
  * [Important Notes](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/productivity/productivity-linear#important-notes)


