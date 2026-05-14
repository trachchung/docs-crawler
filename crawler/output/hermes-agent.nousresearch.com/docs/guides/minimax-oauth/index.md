<!-- Source: https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#__docusaurus_skipToContent_fallback)
On this page
Hermes Agent supports **MiniMax** through a browser-based OAuth login flow, using the same credentials as the [MiniMax portal](https://www.minimax.io). No API key or credit card is required — log in once and Hermes automatically refreshes your session.
The transport reuses the `anthropic_messages` adapter (MiniMax exposes an Anthropic Messages-compatible endpoint at `/anthropic`), so all existing tool-calling, streaming, and context features work without any adapter changes.
## Overview[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#overview "Direct link to Overview")  
| Item  | Value  |  
| --- | --- |  
| Provider ID  | `minimax-oauth`  |  
| Display name  | MiniMax (OAuth)  |  
| Auth type  | Browser OAuth (PKCE device-code flow)  |  
| Transport  | Anthropic Messages-compatible (`anthropic_messages`)  |  
| Models  |  `MiniMax-M2.7`, `MiniMax-M2.7-highspeed`  |  
| Global endpoint  | `https://api.minimax.io/anthropic`  |  
| China endpoint  | `https://api.minimaxi.com/anthropic`  |  
| Requires env var  | No (`MINIMAX_API_KEY` is **not** used for this provider)  |  
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#prerequisites "Direct link to Prerequisites")
  * Python 3.9+
  * Hermes Agent installed
  * A MiniMax account at [minimax.io](https://www.minimax.io) (global) or [minimaxi.com](https://www.minimaxi.com) (China)
  * A browser available on the local machine (or use `--no-browser` for remote sessions)


## Quick Start[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#quick-start "Direct link to Quick Start")

```
# Launch the provider and model pickerhermes model# → Select "MiniMax (OAuth)" from the provider list# → Hermes opens your browser to the MiniMax authorization page# → Approve access in the browser# → Select a model (MiniMax-M2.7 or MiniMax-M2.7-highspeed)# → Start chattinghermes
```

After the first login, credentials are stored under `~/.hermes/auth.json` and are refreshed automatically before each session.
## Logging In Manually[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#logging-in-manually "Direct link to Logging In Manually")
You can trigger a login without going through the model picker:

```
hermes auth add minimax-oauth
```

### China region[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#china-region "Direct link to China region")
If your account is on the China platform (`minimaxi.com`), use the China-region OAuth provider id `minimax-cn` instead, or skip OAuth and configure `MINIMAX_CN_API_KEY` / `MINIMAX_CN_BASE_URL` directly. The `--region cn` flag described in older docs is **not** wired through the CLI's argument parser; use the `minimax-cn` provider instead:

```
hermes auth add minimax-cn --type oauth   # if OAuth is supported on your CN account# or simpler:echo'MINIMAX_CN_API_KEY=your-key'>> ~/.hermes/.env
```

### Remote / headless sessions[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#remote--headless-sessions "Direct link to Remote / headless sessions")
On servers or containers where no browser is available:

```
hermes auth add minimax-oauth --no-browser
```

Hermes will print the verification URL and user code — open the URL on any device and enter the code when prompted.
## The OAuth Flow[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#the-oauth-flow "Direct link to The OAuth Flow")
Hermes implements a PKCE device-code flow against the MiniMax OAuth endpoints:
  1. Hermes generates a PKCE verifier / challenge pair and a random state value.
  2. It POSTs to `{base_url}/oauth/code` with the challenge and receives a `user_code` and `verification_uri`.
  3. Your browser opens `verification_uri`. If prompted, enter the `user_code`.
  4. Hermes polls `{base_url}/oauth/token` until the token arrives (or the deadline passes).
  5. Tokens (`access_token`, `refresh_token`, expiry) are saved to `~/.hermes/auth.json` under the `minimax-oauth` key.


Token refresh (standard OAuth `refresh_token` grant) runs automatically at each session start when the access token is within 60 seconds of expiry.
## Checking Login Status[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#checking-login-status "Direct link to Checking Login Status")

```
hermes doctor
```

The `◆ Auth Providers` section will show:

```
✓ MiniMax OAuth  (logged in, region=global)
```

or, if not logged in:

```
⚠ MiniMax OAuth  (not logged in)
```

## Switching Models[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#switching-models "Direct link to Switching Models")

```
hermes model# → Select "MiniMax (OAuth)"# → Pick from the model list
```

Or set the model directly:

```
hermes config set model MiniMax-M2.7hermes config set provider minimax-oauth
```

## Configuration Reference[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#configuration-reference "Direct link to Configuration Reference")
After login, `~/.hermes/config.yaml` will contain entries similar to:

```
model:default: MiniMax-M2.7provider: minimax-oauthbase_url: https://api.minimax.io/anthropic
```

### Region endpoints[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#region-endpoints "Direct link to Region endpoints")  
| Provider id  | Portal  | Inference endpoint  |  
| --- | --- | --- |  
|  `minimax-oauth` (global)  | `https://api.minimax.io`  | `https://api.minimax.io/anthropic`  |  
|  `minimax-cn` (China)  | `https://api.minimaxi.com`  | `https://api.minimaxi.com/anthropic`  |  
### Provider aliases[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#provider-aliases "Direct link to Provider aliases")
All of the following resolve to `minimax-oauth`:

```
hermes --provider minimax-oauth    # canonicalhermes --provider minimax-portal   # aliashermes --provider minimax-global   # aliashermes --provider minimax_oauth    # alias (underscore form)
```

## Environment Variables[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#environment-variables "Direct link to Environment Variables")
The `minimax-oauth` provider does **not** use `MINIMAX_API_KEY` or `MINIMAX_BASE_URL`. Those variables are for the API-key-based `minimax` and `minimax-cn` providers only.  
| Variable  | Effect  |  
| --- | --- |  
| `MINIMAX_API_KEY`  | Used by `minimax` provider only — ignored for `minimax-oauth`  |  
| `MINIMAX_CN_API_KEY`  | Used by `minimax-cn` provider only — ignored for `minimax-oauth`  |  
To force the `minimax-oauth` provider at runtime:

```
HERMES_INFERENCE_PROVIDER=minimax-oauth hermes
```

## Models[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#models "Direct link to Models")  
| Model  | Best for  |  
| --- | --- |  
| `MiniMax-M2.7`  | Long-context reasoning, complex tool-calling  |  
| `MiniMax-M2.7-highspeed`  | Lower latency, lighter tasks, auxiliary calls  |  
Both models support up to 200,000 tokens of context.
`MiniMax-M2.7-highspeed` is also used automatically as the auxiliary model for vision and delegation tasks when `minimax-oauth` is the primary provider.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#troubleshooting "Direct link to Troubleshooting")
### Token expired — not re-logging in automatically[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#token-expired--not-re-logging-in-automatically "Direct link to Token expired — not re-logging in automatically")
Hermes refreshes the token on every session start if it is within 60 seconds of expiry. If the access token is already expired (for example, after a long offline period), the refresh happens automatically on the next request. If refresh fails with `refresh_token_reused` or `invalid_grant`, Hermes marks the session as requiring re-login.
**Fix:** run `hermes auth add minimax-oauth` again to start a fresh login.
### Authorization timed out[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#authorization-timed-out "Direct link to Authorization timed out")
The device-code flow has a finite expiry window. If you don't approve the login in time, Hermes raises a timeout error.
**Fix:** re-run `hermes auth add minimax-oauth` (or `hermes model`). The flow starts fresh.
### State mismatch (possible CSRF)[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#state-mismatch-possible-csrf "Direct link to State mismatch \(possible CSRF\)")
Hermes detected that the `state` value returned by the authorization server does not match what it sent.
**Fix:** re-run the login. If it persists, check for a proxy or redirect that is modifying the OAuth response.
### Logging in from a remote server[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#logging-in-from-a-remote-server "Direct link to Logging in from a remote server")
If `hermes` cannot open a browser window, use `--no-browser`:

```
hermes auth add minimax-oauth --no-browser
```

Hermes prints the URL and code. Open the URL on any device and complete the flow there.
### "Not logged into MiniMax OAuth" error at runtime[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#not-logged-into-minimax-oauth-error-at-runtime "Direct link to "Not logged into MiniMax OAuth" error at runtime")
The auth store has no credentials for `minimax-oauth`. You have not logged in yet, or the credential file was deleted.
**Fix:** run `hermes model` and select MiniMax (OAuth), or run `hermes auth add minimax-oauth`.
## Logging Out[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#logging-out "Direct link to Logging Out")
To remove stored MiniMax OAuth credentials:

```
hermes auth remove minimax-oauth
```

## See Also[​](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#see-also "Direct link to See Also")
  * [AI Providers reference](https://hermes-agent.nousresearch.com/docs/integrations/providers)
  * [Environment Variables](https://hermes-agent.nousresearch.com/docs/reference/environment-variables)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
  * [hermes doctor](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#prerequisites)
  * [Quick Start](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#quick-start)
  * [Logging In Manually](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#logging-in-manually)
    * [China region](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#china-region)
    * [Remote / headless sessions](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#remote--headless-sessions)
  * [The OAuth Flow](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#the-oauth-flow)
  * [Checking Login Status](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#checking-login-status)
  * [Switching Models](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#switching-models)
  * [Configuration Reference](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#configuration-reference)
    * [Region endpoints](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#region-endpoints)
    * [Provider aliases](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#provider-aliases)
  * [Environment Variables](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#environment-variables)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#troubleshooting)
    * [Token expired — not re-logging in automatically](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#token-expired--not-re-logging-in-automatically)
    * [Authorization timed out](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#authorization-timed-out)
    * [State mismatch (possible CSRF)](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#state-mismatch-possible-csrf)
    * [Logging in from a remote server](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#logging-in-from-a-remote-server)
    * ["Not logged into MiniMax OAuth" error at runtime](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#not-logged-into-minimax-oauth-error-at-runtime)
  * [Logging Out](https://hermes-agent.nousresearch.com/docs/guides/minimax-oauth#logging-out)


