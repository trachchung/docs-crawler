<!-- Source: https://tinyhumans.gitbook.io/openhuman/features/native-tools/web-search -->

The agent can search the live web on its own. Backed by a server-side proxy (Parallel) so you don't carry a search API key, the tool returns titles, snippets, and URLs ready to follow up on.
## 
What it's good for
  * Research - "what's the latest on X".
  * Citation hunting - "find me three sources for Y".
  * Fact-checking before answering - the agent runs a quick search if it isn't confident.


## 
How it differs from generic HTTP
A pure `http_request` tool can fetch a URL but can't _find_ one. Web Search is the discovery layer: it picks the right URLs for the agent, which then hands them off to the for the actual reading.
## 
See also
  * - fetch and clean a specific URL.
  * - search snippets are compressed before they hit the model.


[PreviousAvailable Toolschevron-left](https://tinyhumans.gitbook.io/openhuman/features/native-tools)[NextWeb Scraperchevron-right](https://tinyhumans.gitbook.io/openhuman/features/native-tools/web-scraper)
Last updated 4 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
