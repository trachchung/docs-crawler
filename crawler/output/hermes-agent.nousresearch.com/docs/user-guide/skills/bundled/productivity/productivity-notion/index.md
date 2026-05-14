<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#__docusaurus_skipToContent_fallback)
On this page
Notion API via curl: pages, databases, blocks, search.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#skill-metadata "Direct link to Skill metadata")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/productivity/notion`  |  
| Version  | `1.0.0`  |  
| Author  | community  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `Notion`, `Productivity`, `Notes`, `Database`, `API`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Notion API
Use the Notion API via curl to create, read, update pages, databases (data sources), and blocks. No extra tools needed — just curl and a Notion API key.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#prerequisites "Direct link to Prerequisites")
  1. Create an integration at <https://notion.so/my-integrations>
  2. Copy the API key (starts with `ntn_` or `secret_`)
  3. Store it in `~/.hermes/.env`: 

```
NOTION_API_KEY=ntn_your_key_here
```

  4. **Important:** Share target pages/databases with your integration in Notion (click "..." → "Connect to" → your integration name)


## API Basics[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#api-basics "Direct link to API Basics")
All requests use this pattern:

```
curl-s-X GET "https://api.notion.com/v1/..."\-H"Authorization: Bearer $NOTION_API_KEY"\-H"Notion-Version: 2025-09-03"\-H"Content-Type: application/json"
```

The `Notion-Version` header is required. This skill uses `2025-09-03` (latest). In this version, databases are called "data sources" in the API.
## Common Operations[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#common-operations "Direct link to Common Operations")
### Search[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#search "Direct link to Search")

```
curl-s-X POST "https://api.notion.com/v1/search"\-H"Authorization: Bearer $NOTION_API_KEY"\-H"Notion-Version: 2025-09-03"\-H"Content-Type: application/json"\-d'{"query": "page title"}'
```

### Get Page[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#get-page "Direct link to Get Page")

```
curl-s"https://api.notion.com/v1/pages/{page_id}"\-H"Authorization: Bearer $NOTION_API_KEY"\-H"Notion-Version: 2025-09-03"
```

### Get Page Content (blocks)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#get-page-content-blocks "Direct link to Get Page Content \(blocks\)")

```
curl-s"https://api.notion.com/v1/blocks/{page_id}/children"\-H"Authorization: Bearer $NOTION_API_KEY"\-H"Notion-Version: 2025-09-03"
```

### Create Page in a Database[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#create-page-in-a-database "Direct link to Create Page in a Database")

```
curl-s-X POST "https://api.notion.com/v1/pages"\-H"Authorization: Bearer $NOTION_API_KEY"\-H"Notion-Version: 2025-09-03"\-H"Content-Type: application/json"\-d'{    "parent": {"database_id": "xxx"},    "properties": {      "Name": {"title": [{"text": {"content": "New Item"}}]},      "Status": {"select": {"name": "Todo"}}
```

### Query a Database[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#query-a-database "Direct link to Query a Database")

```
curl-s-X POST "https://api.notion.com/v1/data_sources/{data_source_id}/query"\-H"Authorization: Bearer $NOTION_API_KEY"\-H"Notion-Version: 2025-09-03"\-H"Content-Type: application/json"\-d'{    "filter": {"property": "Status", "select": {"equals": "Active"}},    "sorts": [{"property": "Date", "direction": "descending"}]
```

### Create a Database[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#create-a-database "Direct link to Create a Database")

```
curl-s-X POST "https://api.notion.com/v1/data_sources"\-H"Authorization: Bearer $NOTION_API_KEY"\-H"Notion-Version: 2025-09-03"\-H"Content-Type: application/json"\-d'{    "parent": {"page_id": "xxx"},    "title": [{"text": {"content": "My Database"}}],    "properties": {      "Name": {"title": {}},      "Status": {"select": {"options": [{"name": "Todo"}, {"name": "Done"}]}},      "Date": {"date": {}}
```

### Update Page Properties[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#update-page-properties "Direct link to Update Page Properties")

```
curl-s-X PATCH "https://api.notion.com/v1/pages/{page_id}"\-H"Authorization: Bearer $NOTION_API_KEY"\-H"Notion-Version: 2025-09-03"\-H"Content-Type: application/json"\-d'{"properties": {"Status": {"select": {"name": "Done"}}}}'
```

### Add Content to a Page[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#add-content-to-a-page "Direct link to Add Content to a Page")

```
curl-s-X PATCH "https://api.notion.com/v1/blocks/{page_id}/children"\-H"Authorization: Bearer $NOTION_API_KEY"\-H"Notion-Version: 2025-09-03"\-H"Content-Type: application/json"\-d'{    "children": [      {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": "Hello from Hermes!"}}]}}
```

## Property Types[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#property-types "Direct link to Property Types")
Common property formats for database items:
  * **Title:** `{"title": [{"text": {"content": "..."}}]}`
  * **Rich text:** `{"rich_text": [{"text": {"content": "..."}}]}`
  * **Select:** `{"select": {"name": "Option"}}`
  * **Multi-select:** `{"multi_select": [{"name": "A"}, {"name": "B"}]}`
  * **Date:** `{"date": {"start": "2026-01-15", "end": "2026-01-16"}}`
  * **Checkbox:** `{"checkbox": true}`
  * **Number:** `{"number": 42}`
  * **URL:** `{"url": "https://..."}`
  * **Email:** `{"email": "user@example.com"}`
  * **Relation:** `{"relation": [{"id": "page_id"}]}`


## Key Differences in API Version 2025-09-03[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#key-differences-in-api-version-2025-09-03 "Direct link to Key Differences in API Version 2025-09-03")
  * **Databases → Data Sources:** Use `/data_sources/` endpoints for queries and retrieval
  * **Two IDs:** Each database has both a `database_id` and a `data_source_id`
    * Use `database_id` when creating pages (`parent: {"database_id": "..."}`)
    * Use `data_source_id` when querying (`POST /v1/data_sources/{id}/query`)
  * **Search results:** Databases return as `"object": "data_source"` with their `data_source_id`


## Notes[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#notes "Direct link to Notes")
  * Page/database IDs are UUIDs (with or without dashes)
  * Rate limit: ~3 requests/second average
  * The API cannot set database view filters — that's UI-only
  * Use `is_inline: true` when creating data sources to embed them in pages
  * Add `-s` flag to curl to suppress progress bars (cleaner output for Hermes)
  * Pipe output through `jq` for readable JSON: `... | jq '.results[0].properties'`


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#reference-full-skillmd)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#prerequisites)
  * [Common Operations](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#common-operations)
    * [Get Page Content (blocks)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#get-page-content-blocks)
    * [Create Page in a Database](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#create-page-in-a-database)
    * [Query a Database](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#query-a-database)
    * [Create a Database](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#create-a-database)
    * [Update Page Properties](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#update-page-properties)
    * [Add Content to a Page](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#add-content-to-a-page)
  * [Property Types](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#property-types)
  * [Key Differences in API Version 2025-09-03](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-notion#key-differences-in-api-version-2025-09-03)


