<!-- Source: https://tinyhumans.gitbook.io/openhuman/features/integrations -->

OpenHuman ships with backend-proxied access to **118+ third-party services**. Connecting any of them is a one-click OAuth flow inside the app, there are no API keys to wire by hand, and no plugin marketplace to navigate.
(Under the hood, the connector layer is powered by [Composioarrow-up-right](https://composio.dev). You will not need to think about it.)
Once a service is connected, it shows up in four places at once:
  1. As an **agent tool** , the model can call it directly.
  2. As a **memory source** , syncs it into the every twenty minutes.
  3. As a **profile signal** , your activity across services feeds your personalization.
  4. As a **trigger source** , live events (a new email, a new charge, an inbound DM) flow into the pipeline and can fire off agent actions automatically.


## 
Some of what's in the catalog
The catalog spans productivity, business, social, messaging and Google. A non-exhaustive sample:
Category
Examples
**Email & calendar**
Gmail, Outlook, Google Calendar, Apple Calendar
**Docs & storage**
Google Docs, Google Drive, Notion, Dropbox, Airtable
**Code & dev**
GitHub, Linear, Jira, Figma
**Comms**
Slack, Discord, Microsoft Teams, Telegram, WhatsApp
**CRM & sales**
Salesforce, HubSpot
**Commerce & payments**
Stripe, Shopify
**Project management**
Asana, Trello
**Social**
Twitter / X, Spotify, YouTube
## 
Native vs proxied
Some services have **native providers**. Rust modules that know how to ingest the service into the Memory Tree directly (e.g. Gmail's native ingest path). Others are exposed as **proxied tools** only: the agent can call them, but there's no automatic ingest yet. New native providers are added as features land.
## 
How connections work
Click **Connect** on any integration. A browser window opens for OAuth. Once you sign in, the connection becomes active and OpenHuman starts syncing it through on the next 20-minute tick.
Each integration shows its current status:
  * **Not connected**. integration has not been set up.
  * **Connected**. integration is active and being synced.
  * **Manage**. active integration with options to reconfigure or disconnect.


You can revoke any connection at any time from the Skills tab.
## 
Messaging channels
Three integrations are special. OpenHuman uses them to _talk back_ to you, not just read from them:
  * **Telegram**. the primary messaging channel. Two-way: send and receive messages, manage chats, search history, create groups, 80+ actions on your behalf. All actions run through your own encrypted credentials.
  * **Discord**. send and receive messages via Discord. Connect your account to receive OpenHuman messages there.
  * **Web**. a browser-based chat interface within the desktop app. Messages stay entirely local.


Set your default under **Settings → Automation & Channels → Messaging Channels**. The active route status shows which channel is currently in use. Telegram offers two credential modes: connect via OpenHuman (one-click, encrypted) or provide your own credentials for maximum control.
## 
Skills
Beyond third-party services, OpenHuman has **skills** , small sandboxed modules that run inside the app, fetch external data, run on a schedule, transform information, and respond to events. Each runs with enforced resource limits. Skills install from the Skills tab and integrate with the same Memory Tree as everything else.
## 
Native voice and tools
Two capabilities ship native rather than as integrations because they're load-bearing for the desktop experience:
  * . STT in, TTS out, plus a live Google Meet agent that joins meetings, transcribes them into your Memory Tree, and can speak back into the call.
  * . built-in web search, web-fetch scraper, and a full filesystem/git/lint/test/grep coder toolset that the agent uses out of the box.


## 
Privacy boundary
OpenHuman's core never calls any third-party API directly. All requests go through the OpenHuman backend, which handles OAuth tokens and rate limiting. Your tokens never sit on disk in plaintext on your machine, and the agent only sees the _results_ of tool calls, not the credentials.
See for the full boundary.
## 
See also
  * , live events from connected integrations and how they fire agent actions.
  * [Auto-fetch from Integrations](https://tinyhumans.gitbook.io/openhuman/features/obsidian-wiki/auto-fetch)
  * 

[PreviousAuto-fetch from Integrationschevron-left](https://tinyhumans.gitbook.io/openhuman/features/obsidian-wiki/auto-fetch)[NextTriggerschevron-right](https://tinyhumans.gitbook.io/openhuman/features/integrations/triggers)
Last updated 4 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
