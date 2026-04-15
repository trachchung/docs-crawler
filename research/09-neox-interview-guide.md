# NeoX Interview Guide — Vetting a Mid/Senior Backend Engineer

**Candidate profile (from CV):**
- NestJS / Node.js; MongoDB + MySQL + Redis; BullMQ; Docker; ElasticSearch
- Kafka + Debezium CDC streaming from MongoDB/MySQL
- Integrated CyberSource, MPGS (Mastercard Payment Gateway Services), direct bank APIs
- Claims: $10M USD/mo volume, 30% response-time improvement via refactor + caching
- DGW Asia (NeoX), May 2023 – Sep 2024 — ~16 months
- Prior: 1Fox (2 yrs backend)

**Goal:** prove he actually *built* the NeoX backend vs. wrote CRUD around it. The CV name-drops specific tech — **anchor every tier on those claims**. If he can't defend what he wrote, that's the signal.

**How to use:**
- Tier 0 (5 min) — scope. Force him to point at concrete modules.
- Tier 1 (20 min) — must-know mechanics on the tech he claims.
- Tier 2 (25 min) — design trade-offs where he had ownership.
- Tier 3 (20 min) — stress tests on real fintech incidents.
- Tier 4 (10 min) — seniority signals.

---

## Tier 0 — Scope & Ownership (5 min)

**Q0.1** "Your CV says 'APIs and background workers for transactions, disbursements, and reconciliation.' Pick the one NestJS service you owned most deeply. Name the module, the main entities, and the last non-trivial change you made."

- *Good*: specific service ("the disbursement-worker"), BullMQ queue names, a real bug/feature.
- *Red flag*: paraphrases his own CV without naming anything concrete.

**Q0.2** "Who else worked on that service? If I pulled your commits out, what would break?"

- Tests honest scoping. Anyone can claim ownership; few can describe their actual delta.

**Q0.3** "You list CyberSource and MPGS. Which did you integrate from scratch, which did you inherit, and which produced the weirdest prod bug?"

- Filter for hands-on vs. passenger.

---

## Tier 1 — Must-Know Mechanics (20 min)

### Q1.1 — NestJS module boundaries
"In the disbursement service, how do you structure NestJS modules when the same entity is touched by an HTTP controller, a BullMQ processor, and a Kafka consumer? Specifically: where does the `DisbursementService` live, and what do you inject into the processor?"

- *Expected*: shared feature module exporting `DisbursementService`; processors and consumers in separate modules importing it; avoid circular deps via `forwardRef` only as last resort; repository pattern or `TypeOrmModule.forFeature`/`MongooseModule.forFeature`.
- *Red flag*: "everything in one module" or can't explain provider scope (`DEFAULT` vs `REQUEST` vs `TRANSIENT`) — critical because per-request scope breaks inside BullMQ processors.

**Follow-up**: "A BullMQ processor needs a service that was registered as `Scope.REQUEST`. What happens?" → it resolves once per job technically, but you lose request-context (e.g., tracing, user). He should know this bit you.

### Q1.2 — BullMQ for disbursement
"Walk me through processing a disbursement batch with BullMQ. The batch has 200 items (NeoX's cap). One item fails at the bank. What do you do?"

- *Expected*: per-item job, not per-batch; parent/child jobs or `flows`; `attempts` + `backoff: exponential`; idempotency key = `requestTransId` so retries don't double-pay; DLQ for manual ops; explicit distinction between retriable (network/timeout) vs non-retriable (invalid account) bank errors.
- *Red flag*: retries the whole batch or has no DLQ.

**Follow-up**: "Why not Kafka for this?" → queue semantics (per-job retry, delayed, rate-limit) vs. log semantics. Kafka for fan-out/replay, BullMQ for work.

### Q1.3 — Debezium CDC gotchas
"You streamed MongoDB and MySQL changes via Debezium to downstream services. Name two traps you hit."

- *Expected* (any two):
  - **MongoDB pre-image**: without `changeStreamPreAndPostImages`, the `before` field is null — diff-based consumers break.
  - **Schema evolution**: Debezium emits Avro/JSON with schema; adding a nullable column is safe, renaming is not; downstream deserializers crash.
  - **Snapshot mode**: initial snapshot can take hours on a production DB; offset stored in Kafka — if topic deleted, you re-snapshot.
  - **Transactional boundary**: MySQL binlog row events don't carry txn boundaries by default; two logically-atomic writes arrive as separate events — consumers see inconsistent state.
  - **Tombstones** on DELETE — consumers must handle null values, not treat as upsert.
- *Red flag*: just says "we used Debezium, it worked."

**Follow-up**: "If an analytics consumer falls behind by 4 hours, how do you catch it up without replaying from the start?" → offset management, compacted topics, or snapshot-then-stream.

### Q1.4 — MongoDB vs MySQL split
"NeoX uses both. Based on your work: what lived where, and why? Give one entity that would have been a mistake to put in the other."

- *Expected*: MySQL for transactional / financial ledger (ACID, joins on reconciliation); MongoDB for merchant profiles, webhook configs, audit/event logs, flexible card policy docs. Poor fit for MySQL: schema-variable policy JSON. Poor fit for MongoDB: the reconciliation ledger (needs multi-doc atomic + joins).
- *Red flag*: "MongoDB is faster" with no nuance.

### Q1.5 — Redis usage
"Where did Redis fit? Name three distinct uses in NeoX's backend and one place you considered it but didn't use it."

- *Expected*: (1) OAuth access-token cache per merchant, (2) idempotency lookup for `neo_MerchantTxnID` dedup before hitting DB, (3) rate-limit on merchant API keys, (4) BullMQ backing store. Avoided in: the ledger itself (not durable enough), long-lived settlement state.
- Probe: "Redis as idempotency store — how do you handle the race where two duplicate requests arrive within the same millisecond?" → `SET NX EX` with the request body hash, not just the key.

### Q1.6 — CyberSource + MPGS specifics
"Between CyberSource and MPGS, pick one. Describe the request signing / auth model, and what field trips people up most."

- *Expected (CyberSource)*: HTTP Signature (RFC) with `host`, `digest`, `(request-target)`, signed with merchant's secret; **`digest` must be SHA-256 of raw body, Base64, with `SHA-256=` prefix** — people miss the prefix. Or: REST auth with `v-c-merchant-id`. Shared-secret vs JWT flows.
- *Expected (MPGS)*: HTTPS with merchant-ID basic auth + API password; session-based checkout for hosted; `apiOperation` parameter names (`PAY`, `AUTHORIZE`, `CAPTURE`, `VOID`, `REFUND`). 3DS2 integration via `initiate3DS` → `authenticatePayer`. `transaction.id` uniqueness per order.
- *Red flag*: can't name a single field. This is table-stakes for someone who claims to have integrated either.

**Follow-up**: "A 3DS2 challenge returns but the customer closes the browser before completing. What's the transaction state on MPGS, and how do you reconcile?" → tests actual integration depth.

### Q1.7 — The $10M/mo claim
"$10M USD monthly, Vietnam, mostly VND — that's roughly 250B VND. Break that down: how many transactions/month, median size, peak TPS? If you don't know exactly, estimate and tell me how you'd look it up."

- Tests whether he operated the system or just saw the dashboard once. A builder has rough numbers loaded (e.g., "~100k txns/mo, median 2.5M VND, peak ~30 TPS at 20:00"). Someone who didn't will give vague answers.

### Q1.8 — The 30% improvement claim
"You said you cut response times by 30% via refactoring and caching. Walk me through exactly what you measured, what you changed, and how you proved it."

- *Good*: specific endpoint (e.g., `GET /merchants/:id/transactions`); specific bottleneck (N+1 query, or cold MongoDB query without compound index, or serial bank-account-inquiry inside reconciliation); specific fix (Redis cache with invalidation on write, or compound index, or batched bank inquiry); before/after percentile — **p95 or p99**, not average; load-test tool named (k6, Artillery).
- *Red flag*: "we added Redis caching and it got faster" with no before/after.

---

## Tier 2 — Design & Trade-offs (25 min)

### Q2.1 — Reconciliation service design
"Design NeoX's reconciliation job from scratch in NestJS. Inputs: successful transactions in MySQL, daily settlement file from a bank. Output: reconciled rows + discrepancy alerts. It must run nightly for each merchant's configurable T-day window. Walk me through the code organization, queue topology, and what makes it correct."

- *Expected*: `@Cron` trigger that fans jobs into BullMQ per-merchant (avoid one giant cron); idempotent by `(merchantId, periodStart, periodEnd)` — re-running must not double-settle; authoritative timestamp = bank's (not local `created_at`); two-sided diff: NeoX→Bank and Bank→NeoX; alert on drift (`serviceInformation` grouped); failed reconciliations don't block successful ones (per-merchant isolation). Transactional boundary: `reconcileStatus` flip in MySQL + Kafka event emit — use outbox pattern or Debezium CDC, not dual write.
- *Red flag*: one big transaction; dual-writes Kafka+DB without outbox.

### Q2.2 — Debezium-driven IPN delivery
"Could you use Debezium to drive IPN delivery to merchants instead of a service that writes to both DB and a queue? Design it. What goes wrong?"

- *Expected*: yes — outbox table, Debezium picks it up → Kafka → IPN worker. Wins: no dual-write inconsistency. Losses: need to model non-IPN events; Debezium lag = IPN lag; ordering within a merchant — Kafka partition by `merchantId`; replay semantics if worker consumes but fails (use consumer group commit after successful IPN ACK, not on poll). Redis dedup layer for consumer crashes.
- *Red flag*: doesn't recognize the dual-write problem.

### Q2.3 — IPN HOL blocking
"Merchants' endpoints have wildly different latencies. One merchant's endpoint is slow (30s timeouts) and you see healthy merchants waiting behind them. How do you fix it in BullMQ?"

- *Expected*: per-merchant queue OR per-merchant rate limiter (BullMQ supports `limiter` per queue); concurrency per merchant-group; circuit breaker that fails fast when a merchant has N consecutive failures in a window; separate "quarantine" worker pool for degraded merchants so they don't evict healthy jobs from the main pool.

### Q2.4 — MongoDB for merchant webhook config
"Merchant webhook config is in Mongo — URL, secret, filter on `serviceInformation.code/groupId`. A single merchant has 50 configs. Reads vastly outnumber writes. How do you model + cache?"

- *Expected*: single doc per merchant with `webhooks: []` subarray (bounded ~50 is fine in a Mongo doc; 10k wouldn't be); indexed on `merchantId`; cache the whole merchant's config in Redis with pub/sub invalidation on write; filter evaluation in-process, not in Mongo. Probe: "What if two service instances have stale cache after a config update?" → Redis pub/sub + TTL floor.

### Q2.5 — The dual auth problem
"Payment Gateway uses SHA256(params+secret); Disbursement/Collections use OAuth Bearer. If you had to add a new API today, which would you pick and why?"

- *Expected*: OAuth — rotatable, scoped, token expiry aligns with incident response. Gateway's scheme is SHA256, not HMAC → vulnerable to length-extension in principle; uses shared secret that can't be rotated per-operation. A senior flags: backward compat on PG means you can't just switch.

### Q2.6 — When Kafka, when BullMQ
"NeoX has both. Draw the line. Give me three flows and tell me which belongs where."

- *Expected*: Kafka — CDC from DB, fan-out events to analytics/ES, cross-service notifications, anything with multiple consumers and replay needs. BullMQ — per-job work with retry/backoff/DLQ: IPN delivery, disbursement execution, virtual-card issuance, reconciliation batch items. Some flows start in Kafka (event emitted) and land in BullMQ (work scheduled). A classic: Kafka → worker → BullMQ job.

---

## Tier 3 — Real-World Stress Tests (20 min)

### Q3.1 — 02:00 page
"The reconciliation job's `processed_count` metric is flat for 15 minutes. What do you check, in order, inside a NestJS + BullMQ + MySQL + Mongo stack?"

- *Expected order*: BullMQ admin (Bull Board) → queued/active/failed counts; Redis connectivity (BullMQ backing); DB connection pool saturation (TypeORM/Mongoose pool); one stuck job holding a worker (job timeout config); upstream bank API latency; recent deploy. Bonus: `prom-client` metrics named specifically.

### Q3.2 — Debezium drift
"Analytics says last hour's transaction count is 15% lower than what's in MySQL. Where do you look?"

- *Expected*: Debezium connector status (`/connectors/{name}/status`); consumer group lag (`kafka-consumer-groups.sh --describe`); snapshot vs streaming phase; schema registry compat break; MySQL binlog retention — if Debezium fell behind past binlog retention, events are lost; transactional isolation — did MySQL commit, but binlog not flushed (`sync_binlog=0`)?

### Q3.3 — Deploy gone wrong
"You shipped a NestJS refactor that moved `@Injectable()` services around. The next morning, 0.1% of disbursement jobs silently no-op — they log 'started' but not 'completed.' Debug it."

- *Expected*: check if scope changed (`REQUEST`-scoped service injected into a singleton processor = stale state); check if an async `onModuleInit` is awaited (if not, workers start before dependencies are ready); check if DI lost a decorator; check if a global filter swallows exceptions silently.

### Q3.4 — CyberSource outage
"CyberSource returns 5xx for 10 minutes during peak. What happens in NeoX, and what should happen?"

- *Expected*: happens — retries pile up in queue, merchant IPNs stall, eventual timeout failures returned to merchants. Should — circuit breaker on CyberSource adapter with a short half-open probe; failover to alternate acquirer (MPGS) if payment method allows; graceful degradation at checkout (hide card option, keep wallet/QR); dashboards that SHOW provider-level SLA. Bonus: bulkhead pattern so CyberSource failures don't exhaust the shared HTTP pool that MPGS also uses.

### Q3.5 — Tell me about the incident that taught you the most
Open-ended. Listen for: ownership, blast-radius measurement, symptom vs cause, durable fix. *Red flag*: "we never had real incidents" or blames ops.

### Q3.6 — PCI exposure
"You mention 'PCI compliance' on your CV. What PCI-DSS scope was NeoX in, and where did your code touch the CDE (Cardholder Data Environment)?"

- *Expected*: specifics — did he touch PAN at all, or always tokenized by CyberSource/MPGS? If tokenized, NeoX's scope is likely SAQ A-EP or D depending on direct-API flow. Virtual Card service handles encrypted PAN → that's in scope. Knows that logging/memory dumps are the common leak paths.
- *Red flag*: can't distinguish tokenized flows from raw PAN flows.

---

## Tier 4 — Seniority Signals (10 min)

### Q4.1 — On-call
"NeoX is real money. How did on-call rotation work, what was your most common alert, and what did you change to reduce alert volume?"

### Q4.2 — Trade-off you'd revisit
"Name one technical choice on NeoX that you'd undo with hindsight."

### Q4.3 — Bank partner surprise
"Tell me about a time a bank or NAPAS quietly changed something that broke you. How did you find out?"

### Q4.4 — Saying no
"A product manager asks for a feature that would weaken your idempotency guarantees. How do you push back?"

### Q4.5 — Ramp down from DGW
"You left September 2024. What state did you leave the disbursement/reconciliation stack in? What's the first thing the person who inherited it had to learn?"

- Probe for handover quality.

---

## Gotchas to Have Loaded (lie-detector)

A real builder recognizes most of these instantly.

| Gotcha | What it proves |
|--------|---------------|
| `neo_TransAmount` and `neo_ExtData` arrive in IPN but are NOT hashed | Read the IPN spec end-to-end |
| `neo_Receiver` for QR refund is **Base64(JSON)** | Actually implemented a refund |
| Cancel window = 5 min; after that → refund flow | Void vs refund |
| Disbursement `transactions[]` capped at 200 (code `2051`) | Read error taxonomy |
| Virtual Card error `2226` = merchant's RSA pubkey missing | Debugged card issuance |
| Webhook filter is `code AND groupId`, never OR | Used multi-tenant routing |
| `reconcileStatus=SETTLED` is not payout success | Knows the two state machines |
| CyberSource `digest` header needs `SHA-256=` prefix | Actually integrated it |
| MPGS `apiOperation` values (`PAY`, `AUTHORIZE`, `CAPTURE`…) | Ran the state machine |
| BullMQ `Scope.REQUEST` breaks inside processors | Hit it in prod |
| MongoDB change streams need `changeStreamPreAndPostImages` for `before` | Used Debezium on Mongo |
| Redis `SET NX EX` for idempotency, not `EXISTS` + `SET` | Knows the race |
| SHA256(msg+key) is not HMAC (length-extension) | Real crypto awareness |

---

## Coding Task (30 min, pick one)

**Task A — IPN verifier in NestJS**
"Write a NestJS `Guard` or middleware that validates `neo_SecureHash` on inbound IPN. Bonus: explain where in the request pipeline it must run and why the built-in body parser is a problem."

- Watch for: raw-body access (`express.json({ verify: (req, _, buf) => req.rawBody = buf })`); alphabetical sort over the right keys (exclude `neo_TransAmount`, `neo_ExtData`, `neo_SecureHash` itself); hex UPPER compare; constant-time comparison (`crypto.timingSafeEqual`).

**Task B — BullMQ disbursement worker**
"Pseudocode the processor for a single disbursement item. Handle: bank timeout (retry), invalid account (do not retry), duplicate `requestTransId` (check-then-no-op). Emit a Kafka event on terminal state."

- Watch for: idempotency key on the outbox row, not on the Kafka emit; explicit retriable vs fatal error classification; DLQ; no direct dual write.

**Task C — Debezium outbox for IPN**
"Design an `outbox_ipn` table schema + the NestJS code that writes to it atomically with the transaction state change. Explain how Debezium picks it up and how the IPN consumer achieves at-least-once delivery with merchant-side dedup via `neo_TransactionID`."

- Watch for: single-transaction insert to outbox + state flip; Debezium connector tombstone on delete vs. `soft-delete` flag; Kafka partition key = `merchantId` (ordering) not `transactionId`.

---

## Scoring Rubric

| Dimension | Strong | Medium | Weak |
|-----------|--------|--------|------|
| CV claims stand up | Numbers, code paths, tools named unprompted | Matches CV when prompted | Vague, repeats CV verbatim |
| Failure modes | Volunteers edge cases | Needs prompting | "It just worked" |
| Trade-offs | Frames choices with alternatives | One-sided | "It's how we did it" |
| Judgement | Says "I don't know" + how to find out | Occasionally bluffs | Makes things up |
| Seniority | On-call, handover, people | Technical only | Happy path only |

**Decision heuristic**:
- **Hire** if Tier 1 ≥ 6/8, Tier 2 ≥ 4/6, a convincing Tier 3.5 incident, AND Q1.7 + Q1.8 land.
- **Maybe** if Tier 1 passes but can't defend the 30% / $10M claims with specifics — trial task before offer.
- **Pass** if he can't explain a single Debezium gotcha, or either CyberSource/MPGS signing, or how BullMQ retries work. Those are the load-bearing CV claims.

---

## Pre-Interview Prep for You

1. Read his `package.json` claims back to him — NestJS version, BullMQ version, `@kafkajs/*`. Concrete versions reveal real usage.
2. Ask for a code sample (sanitized). Look at: module organization, error handling, test coverage on money-handling paths.
3. If he references a specific CyberSource/MPGS SDK (`cybersource-rest-client-node`), verify he can explain its auth-helper's behavior.
4. $10M/mo + 30% perf + 16 months tenure — ask when each landed, in order. Real builders have timeline clarity.
