<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug -->

本页总览
Debug REST/GraphQL APIs: status codes, auth, schemas, repro.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#skill-metadata "Skill metadata的直接链接")  
| Source  | Optional — install with `hermes skills install official/software-development/rest-graphql-debug`  |  
| --- | --- |  
| Path  | `optional-skills/software-development/rest-graphql-debug`  |  
| Version  | `1.2.0`  |  
| Author  | eren-karakus0  |  
| License  | MIT  |  
| Tags  |  `api`, `rest`, `graphql`, `http`, `debugging`, `testing`, `curl`, `integration`  |  
| Related skills  |  [`systematic-debugging`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/software-development/software-development-systematic-debugging), [`test-driven-development`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/software-development/software-development-test-driven-development)  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# API Testing & Debugging
Drive REST and GraphQL diagnosis through Hermes tools — `terminal` for `curl`, `execute_code` for Python `requests`, `web_extract` for vendor docs. Isolate the failing layer before guessing at the fix.
## When to Use[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#when-to-use "When to Use的直接链接")
  * API returns unexpected status or body
  * Auth fails (401/403 after token refresh, OAuth, API key)
  * Works in Postman but fails in code
  * Webhook / callback integration debugging
  * Building or reviewing API integration tests
  * Rate limiting or pagination issues


Skip for UI rendering, DB query tuning, or DNS/firewall infra (escalate).
## Core Principle[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#core-principle "Core Principle的直接链接")
**Isolate the layer, then fix.** A 200 OK can hide broken data. A 500 can mask a one-character auth typo. Walk the chain in order; never skip a step.

```
1. Connectivity   → can we reach the host at all?1.5 Timeouts      → connect-slow vs read-slow?2. TLS/SSL        → cert valid and trusted?3. Auth           → credentials correct and unexpired?4. Request format → payload shape match server expectations?5. Response parse → does our code accept what came back?6. Semantics      → does the data mean what we assume?
```

## 5-Minute Quickstart[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#5-minute-quickstart "5-Minute Quickstart的直接链接")
### REST via terminal[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#rest-via-terminal "REST via terminal的直接链接")

```
# Verbose request/response exchangeterminal('curl -v https://api.example.com/users/1')# POST with JSONterminal("""curl -X POST https://api.example.com/users \\  -H 'Content-Type: application/json' \\  -H "Authorization: Bearer $TOKEN" \\  -d '{"name":"test","email":"test@example.com"}'""")# Headers onlyterminal('curl -sI https://api.example.com/health')# Pretty-print JSONterminal('curl -s https://api.example.com/users | python3 -m json.tool')
```

### GraphQL via terminal[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#graphql-via-terminal "GraphQL via terminal的直接链接")

```
terminal("""curl -X POST https://api.example.com/graphql \\  -H 'Content-Type: application/json' \\  -H "Authorization: Bearer $TOKEN" \\  -d '{"query":"{ user(id: 1) { name email } }"}'""")
```

**GraphQL gotcha:** servers often return HTTP 200 even when the query failed. Always inspect the `errors` field regardless of status code:

```
execute_code('''import os, requestsresp = requests.post(    "https://api.example.com/graphql",    json={"query": "{ user(id: 1) { name email } }"},    headers={"Authorization": f"Bearer {os.environ['TOKEN']}"},    timeout=10,data = resp.json()if data.get("errors"):    for err in data["errors"]:        print(f"GraphQL error: {err['message']} (path: {err.get('path')})")print(data.get("data"))''')
```

### Python (requests) via execute_code[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#python-requests-via-execute_code "Python \(requests\) via execute_code的直接链接")

```
execute_code('''import requestsresp = requests.get(    "https://api.example.com/users/1",    headers={"Authorization": "Bearer <TOKEN>"},    timeout=(3.05, 30),  # (connect, read)print(resp.status_code, dict(resp.headers))print(resp.text[:500])''')
```

## Layered Debug Flow[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#layered-debug-flow "Layered Debug Flow的直接链接")
### Step 1 — Connectivity[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-1--connectivity "Step 1 — Connectivity的直接链接")

```
terminal('nslookup api.example.com')terminal('curl -v --connect-timeout 5 https://api.example.com/health')
```

Failures: DNS not resolving, firewall, VPN required, proxy missing.
### Step 1.5 — Timeouts[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-15--timeouts "Step 1.5 — Timeouts的直接链接")
Distinguish _can't reach_ from _reaches but slow_ :

```
terminal('''curl -w "dns:%{time_namelookup}s connect:%{time_connect}s tls:%{time_appconnect}s ttfb:%{time_starttransfer}s total:%{time_total}s\\n" \\  -o /dev/null -s https://api.example.com/endpoint''')
```

In Python, always pass a tuple timeout — `requests` has no default and will hang forever:

```
execute_code('''import requestsfrom requests.exceptions import ConnectTimeout, ReadTimeouttry:    requests.get(url, timeout=(3.05, 30))except ConnectTimeout:    print("Cannot reach host — DNS, firewall, VPN")except ReadTimeout:    print("Connected but server is slow")''')
```

Diagnosis: high `time_connect` is network/firewall; high `time_starttransfer` with low `time_connect` is a slow server.
### Step 2 — TLS/SSL[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-2--tlsssl "Step 2 — TLS/SSL的直接链接")

```
terminal('curl -vI https://api.example.com 2>&1 | grep -E "SSL|subject|expire|issuer"')
```

Failures: expired cert, self-signed, hostname mismatch, missing CA bundle. Use `-k` only for ad-hoc debug, never in code.
### Step 3 — Authentication[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-3--authentication "Step 3 — Authentication的直接链接")

```
# Token validity checkterminal('curl -s -o /dev/null -w "%{http_code}\\n" -H "Authorization: Bearer $TOKEN" https://api.example.com/me')# Decode JWT exp claim — handles base64url padding correctlyexecute_code('''import json, base64, ostok = os.environ["TOKEN"]payload = tok.split(".")[1]payload += "=" * (-len(payload) % 4)print(json.dumps(json.loads(base64.urlsafe_b64decode(payload)), indent=2))''')
```

Checklist:
  * Token expired? (`exp` claim in JWT)
  * Right scheme? Bearer vs Basic vs Token vs `X-Api-Key`
  * Right environment? Staging key on prod is a classic
  * API key in header vs query param (`?api_key=…`)?


### Step 4 — Request Format[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-4--request-format "Step 4 — Request Format的直接链接")

```
terminal("""curl -v -X POST https://api.example.com/endpoint \\  -H 'Content-Type: application/json' \\  -d '{"key":"value"}' 2>&1""")
```

**Content-Type / body mismatch — the silent 415/400:**

```
# WRONG — data= sends form-encoded, header liesrequests.post(url, data='{"k":"v"}', headers={"Content-Type":"application/json"})# RIGHT — json= auto-sets header AND serializesrequests.post(url, json={"k":"v"})# WRONG — Accept says XML, code calls .json()requests.get(url, headers={"Accept":"text/xml"})# RIGHT — let requests build multipart with boundaryrequests.post(url, files={"file":open("doc.pdf","rb")})
```

Common: form-encoded vs JSON, missing required fields, wrong HTTP method, unencoded query params.
### Step 5 — Response Parsing[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-5--response-parsing "Step 5 — Response Parsing的直接链接")
Always inspect content-type before calling `.json()`:

```
execute_code('''import requestsresp = requests.post(url, json=payload, timeout=10)print(f"status={resp.status_code}")print(f"headers={dict(resp.headers)}")ct = resp.headers.get("Content-Type", "")if "application/json" in ct:    print(resp.json())else:    print(f"unexpected content-type {ct!r}, body={resp.text[:500]!r}")''')
```

Failures: HTML error page where JSON expected, empty body, wrong charset.
### Step 6 — Semantic Validation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-6--semantic-validation "Step 6 — Semantic Validation的直接链接")
Parsed cleanly — but is the data _correct_?
  * Does `"status": "active"` mean what your code thinks?
  * ID in response matches the one requested?
  * Timestamps in expected timezone?
  * Pagination returning all results, or just page 1?


## HTTP Status Playbook[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#http-status-playbook "HTTP Status Playbook的直接链接")
### 401 Unauthorized — credentials missing or invalid[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#401-unauthorized--credentials-missing-or-invalid "401 Unauthorized — credentials missing or invalid的直接链接")
  1. `Authorization` header actually present? (`curl -v` to confirm)
  2. Token correct and unexpired?
  3. Right auth scheme? (`Bearer` vs `Basic` vs `Token`)
  4. Some APIs use query param (`?api_key=…`) instead of header.


### 403 Forbidden — authenticated but not authorized[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#403-forbidden--authenticated-but-not-authorized "403 Forbidden — authenticated but not authorized的直接链接")
  1. Token has the required scopes/permissions?
  2. Resource owned by a different account?
  3. IP allowlist blocking you?
  4. CORS in browser? (check `Access-Control-Allow-Origin`)


### 404 Not Found — resource doesn't exist or URL is wrong[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#404-not-found--resource-doesnt-exist-or-url-is-wrong "404 Not Found — resource doesn't exist or URL is wrong的直接链接")
  1. Path correct? (trailing slash, typo, version prefix)
  2. Resource ID exists?
  3. Right API version (`/v1/` vs `/v2/`)?
  4. Right base URL (staging vs prod)?


### 409 Conflict — state collision[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#409-conflict--state-collision "409 Conflict — state collision的直接链接")
  1. Resource already exists (duplicate create)?
  2. Stale `ETag` / `If-Match`?
  3. Concurrent modification by another process?


### 422 Unprocessable Entity — valid JSON, invalid data[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#422-unprocessable-entity--valid-json-invalid-data "422 Unprocessable Entity — valid JSON, invalid data的直接链接")
The error body usually names the bad fields. Check:
  * Field types (string vs int, date format)
  * Required vs optional
  * Enum values inside the allowed set


### 429 Too Many Requests — rate limited[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#429-too-many-requests--rate-limited "429 Too Many Requests — rate limited的直接链接")
Check `Retry-After` and `X-RateLimit-*` headers. Exponential backoff:

```
execute_code('''import time, requestsdef with_backoff(method, url, **kwargs):    for attempt in range(5):        resp = requests.request(method, url, **kwargs)        if resp.status_code != 429:            return resp        wait = int(resp.headers.get("Retry-After", 2 ** attempt))        time.sleep(wait)    return resp''')
```

### 5xx — server-side, usually not your fault[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#5xx--server-side-usually-not-your-fault "5xx — server-side, usually not your fault的直接链接")
  * **500** — server bug. Capture correlation ID, file with provider.
  * **502** — upstream down. Backoff + retry.
  * **503** — overloaded / maintenance. Check status page.
  * **504** — upstream timeout. Reduce payload or raise timeout.


For all 5xx: backoff with jitter, alert on persistence.
## Pagination & Idempotency[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#pagination--idempotency "Pagination & Idempotency的直接链接")
**Pagination.** Verify you're getting _all_ results. Look for `next_cursor`, `next_page`, `total_count`. Two patterns:
  * Offset (`?limit=100&offset=200`) — simple, can skip items if data shifts.
  * Cursor (`?cursor=abc123`) — preferred for live or large datasets.


**Idempotency.** For non-idempotent operations (POST), send `Idempotency-Key: <uuid>` so retries don't double-charge / double-create. Mandatory for payments and orders.
## Contract Validation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#contract-validation "Contract Validation的直接链接")
Catch schema drift before it hits production:

```
execute_code('''import requestsdef validate_user(data: dict) -> list[str]:    errors = []    required = {"id": int, "email": str, "created_at": str}    for field, expected in required.items():        if field not in data:            errors.append(f"missing field: {field}")        elif not isinstance(data[field], expected):            errors.append(f"{field}: want {expected.__name__}, got {type(data[field]).__name__}")    return errorsresp = requests.get(f"{BASE}/users/1", headers=HEADERS, timeout=10)issues = validate_user(resp.json())if issues:    print(f"contract violations: {issues}")''')
```

Run after API upgrades, when integrating new third parties, or in CI smoke tests.
## Correlation IDs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#correlation-ids "Correlation IDs的直接链接")
Always capture the provider's request ID — fastest path to vendor support:

```
execute_code('''import requestsresp = requests.post(url, json=payload, headers=headers, timeout=10)request_id = (    resp.headers.get("X-Request-Id")    or resp.headers.get("X-Trace-Id")    or resp.headers.get("CF-Ray")  # Cloudflareif resp.status_code >= 400:    print(f"failed status={resp.status_code} req_id={request_id} ts={resp.headers.get('Date')}")''')
```

**Vendor bug-report template:**

```
Endpoint:    POST /api/v1/ordersRequest ID:  req_abc123xyzTimestamp:   2026-03-17T14:30:00ZStatus:      500Expected:    201 with order objectActual:      500 {"error":"internal server error"}Repro:       curl -X POST … (auth: <REDACTED>)
```

## Regression Test Template[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#regression-test-template "Regression Test Template的直接链接")
Drop this into `tests/` and run via `terminal('pytest tests/test_api_smoke.py -v')`:

```
import os, requests, pytestBASE_URL = os.environ.get("API_BASE_URL","https://api.example.com")TOKEN    = os.environ.get("API_TOKEN","")HEADERS  ={"Authorization":f"Bearer {TOKEN}"}classTestAPISmoke:deftest_health(self):        resp = requests.get(f"{BASE_URL}/health", timeout=5)assert resp.status_code ==200deftest_list_users_returns_array(self):        resp = requests.get(f"{BASE_URL}/users", headers=HEADERS, timeout=10)assert resp.status_code ==200        data = resp.json()assertisinstance(data.get("data", data),list)deftest_get_user_required_fields(self):        resp = requests.get(f"{BASE_URL}/users/1", headers=HEADERS, timeout=10)assert resp.status_code in(200,404)if resp.status_code ==200:            user = resp.json()assert"id"in user and"email"in userdeftest_invalid_auth_returns_401(self):        resp = requests.get(f"{BASE_URL}/users",            headers={"Authorization":"Bearer invalid-token"},            timeout=10,assert resp.status_code ==401
```

## Security[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#security "Security的直接链接")
### Token handling[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#token-handling "Token handling的直接链接")
  * Never log full tokens. Redact: `Bearer <REDACTED>`.
  * Never hardcode tokens in scripts. Read from env (`os.environ["API_TOKEN"]`) or `~/.hermes/.env`.
  * Rotate immediately if a token surfaces in logs, error messages, or git history.


### Safe logging[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#safe-logging "Safe logging的直接链接")

```
defredact_auth(headers:dict)->dict:    sensitive ={"authorization","x-api-key","cookie","set-cookie"}return{k:("<REDACTED>"if k.lower()in sensitive else v)for k, v in headers.items()}
```

### Leak checklist[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#leak-checklist "Leak checklist的直接链接")
  * **Credentials in URLs.** API keys in query strings end up in server logs, browser history, referrer headers — use headers.
  * **PII in error responses.** `404 on /users/123` shouldn't reveal whether the user exists (enumeration).
  * **Stack traces in prod.** 500s shouldn't leak file paths, framework versions.
  * **Internal hostnames/IPs.** `10.x.x.x`, `internal-api.corp.local` in error bodies.
  * **Tokens echoed back.** Some APIs include the auth token in error details. Verify they don't.
  * **Verbose`Server` / `X-Powered-By`.** Stack-info leaks. Note for security review.


## Hermes Tool Patterns[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#hermes-tool-patterns "Hermes Tool Patterns的直接链接")
### terminal — for curl, dig, openssl[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#terminal--for-curl-dig-openssl "terminal — for curl, dig, openssl的直接链接")

```
terminal('curl -sI https://api.example.com')terminal('openssl s_client -connect api.example.com:443 -servername api.example.com </dev/null 2>/dev/null | openssl x509 -noout -dates')
```

### execute_code — for multi-step Python flows[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#execute_code--for-multi-step-python-flows "execute_code — for multi-step Python flows的直接链接")
When debugging spans auth → fetch → paginate → validate, use `execute_code`. Variables persist for the script, results print to stdout, no risk of token spam in your context:

```
execute_code('''import os, requeststoken = os.environ["API_TOKEN"]base  = "https://api.example.com"H     = {"Authorization": f"Bearer {token}"}# 1. authme = requests.get(f"{base}/me", headers=H, timeout=10)print(f"auth {me.status_code}")# 2. paginateall_users, cursor = [], Nonewhile True:    params = {"cursor": cursor} if cursor else {}    r = requests.get(f"{base}/users", headers=H, params=params, timeout=10)    body = r.json()    all_users.extend(body["data"])    cursor = body.get("next_cursor")    if not cursor:        breakprint(f"users={len(all_users)}")''')
```

### web_extract — for vendor API docs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#web_extract--for-vendor-api-docs "web_extract — for vendor API docs的直接链接")
Pull the spec for the endpoint you're debugging instead of guessing:

```
web_extract(urls=["https://docs.example.com/api/v1/users"])
```

### delegate_task — for full CRUD test sweeps[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#delegate_task--for-full-crud-test-sweeps "delegate_task — for full CRUD test sweeps的直接链接")

```
delegate_task(    goal="Test all CRUD endpoints for /api/v1/users",    context="""Follow the rest-graphql-debug skill (optional-skills/software-development/rest-graphql-debug).Base URL: https://api.example.comAuth: Bearer token from API_TOKEN env var.For each verb (POST, GET, PATCH, DELETE):  - happy path: assert status + response schema  - error cases: 400, 404, 422  - log a repro curl for any failure (redact tokens)Output: pass/fail per endpoint + correlation IDs for failures.""",    toolsets=["terminal","file"],
```

## Output Format[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#output-format "Output Format的直接链接")
When reporting findings:

```
## FindingEndpoint: POST /api/v1/usersStatus:   422 Unprocessable EntityReq ID:   req_abc123xyz## Reprocurl -X POST https://api.example.com/api/v1/users \  -H 'Content-Type: application/json' \  -H 'Authorization: Bearer <REDACTED>' \  -d '{"name":"test"}'## Root CauseMissing required field `email`. Server validation rejects before processing.## Fix-d '{"name":"test","email":"test@example.com"}'
```

## Related[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#related "Related的直接链接")
  * `systematic-debugging` — once the failing API layer is isolated, root-cause your code
  * `test-driven-development` — write the regression test before shipping the fix


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#reference-full-skillmd)
  * [When to Use](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#when-to-use)
  * [Core Principle](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#core-principle)
  * [5-Minute Quickstart](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#5-minute-quickstart)
    * [REST via terminal](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#rest-via-terminal)
    * [GraphQL via terminal](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#graphql-via-terminal)
    * [Python (requests) via execute_code](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#python-requests-via-execute_code)
  * [Layered Debug Flow](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#layered-debug-flow)
    * [Step 1 — Connectivity](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-1--connectivity)
    * [Step 1.5 — Timeouts](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-15--timeouts)
    * [Step 2 — TLS/SSL](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-2--tlsssl)
    * [Step 3 — Authentication](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-3--authentication)
    * [Step 4 — Request Format](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-4--request-format)
    * [Step 5 — Response Parsing](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-5--response-parsing)
    * [Step 6 — Semantic Validation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#step-6--semantic-validation)
  * [HTTP Status Playbook](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#http-status-playbook)
    * [401 Unauthorized — credentials missing or invalid](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#401-unauthorized--credentials-missing-or-invalid)
    * [403 Forbidden — authenticated but not authorized](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#403-forbidden--authenticated-but-not-authorized)
    * [404 Not Found — resource doesn't exist or URL is wrong](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#404-not-found--resource-doesnt-exist-or-url-is-wrong)
    * [409 Conflict — state collision](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#409-conflict--state-collision)
    * [422 Unprocessable Entity — valid JSON, invalid data](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#422-unprocessable-entity--valid-json-invalid-data)
    * [429 Too Many Requests — rate limited](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#429-too-many-requests--rate-limited)
    * [5xx — server-side, usually not your fault](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#5xx--server-side-usually-not-your-fault)
  * [Pagination & Idempotency](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#pagination--idempotency)
  * [Contract Validation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#contract-validation)
  * [Correlation IDs](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#correlation-ids)
  * [Regression Test Template](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#regression-test-template)
  * [Security](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#security)
    * [Token handling](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#token-handling)
    * [Safe logging](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#safe-logging)
    * [Leak checklist](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#leak-checklist)
  * [Hermes Tool Patterns](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#hermes-tool-patterns)
    * [terminal — for curl, dig, openssl](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#terminal--for-curl-dig-openssl)
    * [execute_code — for multi-step Python flows](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#execute_code--for-multi-step-python-flows)
    * [web_extract — for vendor API docs](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#web_extract--for-vendor-api-docs)
    * [delegate_task — for full CRUD test sweeps](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#delegate_task--for-full-crud-test-sweeps)
  * [Output Format](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/software-development/software-development-rest-graphql-debug#output-format)


