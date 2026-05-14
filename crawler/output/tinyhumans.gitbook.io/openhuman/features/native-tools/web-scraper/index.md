<!-- Source: https://tinyhumans.gitbook.io/openhuman/features/native-tools/web-scraper -->

A purpose-built fetch tool, separate from generic `http_request` / `curl`. It exists because the agent doesn't want raw HTML - it wants the _article_.
## 
What it does
  * Fetches a URL.
  * Strips boilerplate (nav, ads, footer, scripts).
  * Returns clean text the agent can reason over.


## 
Guardrails
  * Caps response at 1 MB - large pages get truncated, not silently dropped.
  * 20-second timeout - slow servers don't stall the conversation.
  * Subject to the same proxy and URL-guard rules as other network tools.


## 
What it's good for
  * Reading articles, blog posts, docs pages, GitHub READMEs without the noise.
  * Following up on a result.
  * Summarising a single page on demand.


## 
See also
  * - find URLs to feed into the scraper.
  * - what trims long pages before they hit the model.


[PreviousWeb Searchchevron-left](https://tinyhumans.gitbook.io/openhuman/features/native-tools/web-search)[NextCoderchevron-right](https://tinyhumans.gitbook.io/openhuman/features/native-tools/coder)
Last updated 4 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
