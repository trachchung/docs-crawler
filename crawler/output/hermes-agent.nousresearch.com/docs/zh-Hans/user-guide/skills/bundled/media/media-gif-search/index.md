<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search -->

本页总览
Search/download GIFs from Tenor via curl + jq.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#skill-metadata "Skill metadata的直接链接")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/media/gif-search`  |  
| Version  | `1.1.0`  |  
| Author  | Hermes Agent  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `GIF`, `Media`, `Search`, `Tenor`, `API`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# GIF Search (Tenor API)
Search and download GIFs directly via the Tenor API using curl. No extra tools needed.
## When to use[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#when-to-use "When to use的直接链接")
Useful for finding reaction GIFs, creating visual content, and sending GIFs in chat.
## Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#setup "Setup的直接链接")
Set your Tenor API key in your environment (add to `~/.hermes/.env`):

```
TENOR_API_KEY=your_key_here
```

Get a free API key at <https://developers.google.com/tenor/guides/quickstart> — the Google Cloud Console Tenor API key is free and has generous rate limits.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#prerequisites "Prerequisites的直接链接")
  * `curl` and `jq` (both standard on macOS/Linux)
  * `TENOR_API_KEY` environment variable


## Search for GIFs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#search-for-gifs "Search for GIFs的直接链接")

```
# Search and get GIF URLscurl-s"https://tenor.googleapis.com/v2/search?q=thumbs+up&limit=5&key=${TENOR_API_KEY}"| jq -r'.results[].media_formats.gif.url'# Get smaller/preview versionscurl-s"https://tenor.googleapis.com/v2/search?q=nice+work&limit=3&key=${TENOR_API_KEY}"| jq -r'.results[].media_formats.tinygif.url'
```

## Download a GIF[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#download-a-gif "Download a GIF的直接链接")

```
# Search and download the top resultURL=$(curl-s"https://tenor.googleapis.com/v2/search?q=celebration&limit=1&key=${TENOR_API_KEY}"| jq -r'.results[0].media_formats.gif.url')curl-sL"$URL"-o celebration.gif
```

## Get Full Metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#get-full-metadata "Get Full Metadata的直接链接")

```
curl-s"https://tenor.googleapis.com/v2/search?q=cat&limit=3&key=${TENOR_API_KEY}"| jq '.results[] | {title: .title, url: .media_formats.gif.url, preview: .media_formats.tinygif.url, dimensions: .media_formats.gif.dims}'
```

## API Parameters[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#api-parameters "API Parameters的直接链接")  
| Parameter  | Description  |  
| --- | --- |  
| Search query (URL-encode spaces as `+`)  |  
| `limit`  | Max results (1-50, default 20)  |  
| `key`  | API key (from `$TENOR_API_KEY` env var)  |  
| `media_filter`  | Filter formats: `gif`, `tinygif`, `mp4`, `tinymp4`, `webm`  |  
| `contentfilter`  | Safety: `off`, `low`, `medium`, `high`  |  
| `locale`  | Language: `en_US`, `es`, `fr`, etc.  |  
## Available Media Formats[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#available-media-formats "Available Media Formats的直接链接")
Each result has multiple formats under `.media_formats`:  
| Format  | Use case  |  
| --- | --- |  
| `gif`  | Full quality GIF  |  
| `tinygif`  | Small preview GIF  |  
| `mp4`  | Video version (smaller file size)  |  
| `tinymp4`  | Small preview video  |  
| `webm`  | WebM video  |  
| `nanogif`  | Tiny thumbnail  |  
## Notes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#notes "Notes的直接链接")
  * URL-encode the query: spaces as `+`, special chars as `%XX`
  * For sending in chat, `tinygif` URLs are lighter weight
  * GIF URLs can be used directly in markdown: `![alt](https://github.com/NousResearch/hermes-agent/blob/main/skills/media/gif-search/url)`


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#reference-full-skillmd)
  * [When to use](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#when-to-use)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#prerequisites)
  * [Search for GIFs](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#search-for-gifs)
  * [Download a GIF](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#download-a-gif)
  * [Get Full Metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#get-full-metadata)
  * [API Parameters](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#api-parameters)
  * [Available Media Formats](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/media/media-gif-search#available-media-formats)


