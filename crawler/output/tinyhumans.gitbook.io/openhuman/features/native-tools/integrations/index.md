<!-- Source: https://tinyhumans.gitbook.io/openhuman/features/native-tools/integrations -->

OpenHuman's agent can call into [118+ third-party services](https://tinyhumans.gitbook.io/openhuman/features/integrations) - Gmail, Notion, GitHub, Slack, Stripe, Calendar, and the long tail - through a single proxied tool surface.
## 
How it shows up to the agent
Once you've connected a service via OAuth, its actions become callable tools. The agent doesn't need to know whether a tool talks to Gmail or to a local file - it just calls the tool, the proxy routes the request through the OpenHuman backend with your token, and the result comes back like any other tool output.
A few examples of what becomes available:
  * "Send a message to #engineering on Slack."
  * "Create an issue in the openhuman repo."
  * "What's on my calendar tomorrow?"
  * "Pull the last 20 Stripe charges over $1000."


## 
Native vs proxied
Some services have **native providers** - Rust modules that know how to ingest the service into the directly (e.g. Gmail's native ingest path). Others are exposed as **proxied tools** only: the agent can call them, but there's no automatic ingest yet. New native providers are added as features land.
## 
Privacy boundary
OpenHuman's core never calls any third-party API directly. All requests go through the OpenHuman backend, which handles OAuth tokens and rate limiting. Your tokens never sit on disk in plaintext on your machine, and the agent only sees the _results_ of tool calls, not the credentials.
## 
See also
  * [Third-party Integrations (catalog)](https://tinyhumans.gitbook.io/openhuman/features/integrations) - the user-facing pitch, OAuth flow, and connection management.
  * - how connected services flow into the Memory Tree.
  * - the full boundary.


[PreviousTool-Scoped Memorychevron-left](https://tinyhumans.gitbook.io/openhuman/features/native-tools/tool-memory)[NextAgent Coordinationchevron-right](https://tinyhumans.gitbook.io/openhuman/features/native-tools/agent-coordination)
Last updated 4 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
