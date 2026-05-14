<!-- Source: https://tinyhumans.gitbook.io/openhuman/features/native-tools/browser-and-computer -->

When the agent needs to _use_ your machine the way a person would - open a page, screenshot it, click a button, type a phrase - these tools are how it does it.
## 
Browser
  * **Open** a URL in an embedded webview the agent can read back from.
  * **Screenshot** the current page.
  * **Inspect** image output and metadata, so the agent can describe what it sees.


The browser surface runs through CEF (Chromium Embedded Framework) and includes a security layer that scopes what pages can do. See [Chromium Embedded Framework](https://tinyhumans.gitbook.io/openhuman/developing/cef) for the platform details.
## 
Computer (mouse + keyboard)
  * **Mouse** - move, click, drag.
  * **Keyboard** - type text, send key chords.
  * **Human path** - moves and clicks follow human-like trajectories rather than teleporting, so they don't trip naive bot detection.


## 
What it's good for
  * Driving sites that don't have an API or a .
  * Multi-step UI flows where a single screenshot isn't enough.
  * Automating local apps from inside a chat.


## 
See also
  * - when you only need the article, not the whole page.
  * [Chromium Embedded Framework](https://tinyhumans.gitbook.io/openhuman/developing/cef) - the runtime browser layer.


[PreviousCoderchevron-left](https://tinyhumans.gitbook.io/openhuman/features/native-tools/coder)[NextCron & Schedulingchevron-right](https://tinyhumans.gitbook.io/openhuman/features/native-tools/cron)
Last updated 4 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
