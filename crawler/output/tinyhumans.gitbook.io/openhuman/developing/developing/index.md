<!-- Source: https://tinyhumans.gitbook.io/openhuman/developing/developing -->

OpenHuman is open source under GPLv3 at [github.com/tinyhumansai/openhumanarrow-up-right](https://github.com/tinyhumansai/openhuman). This section is for contributors and anyone running OpenHuman from source.
If you just want to use the app, head to . If you're here to read the architecture, hack on a feature, or land a PR, you're in the right place.
## 
Where things live
Path
What's there
`app/`
pnpm workspace `openhuman-app`. Vite + React frontend (`app/src/`) and the Tauri desktop host (`app/src-tauri/`).
`src/`
Rust crate `openhuman_core` and the `openhuman-core` CLI binary. Domains, JSON-RPC, MCP routing.
`gitbooks/`
This site (the public-facing docs).
`docs/`
Older deep references not yet migrated to GitBook (memory pipeline diagrams, agent flows, etc.).
`CLAUDE.md` at the repo root is the source of truth for AI agents working on the codebase. Same rules apply to humans.
## 
Start here
If it's your first time pulling the repo:
  1. . Toolchain, dependencies, the vendored Tauri CLI, sidecar staging - everything `pnpm dev` needs to actually start.
  2. . Fresh-machine setup for the repo-root Rust crate only: pinned toolchain, OS packages, and exact `cargo` commands.
  3. [**Architecture** arrow-up-right](https://github.com/tinyhumansai/openhuman/blob/main/gitbooks/developing/architecture.md). How the desktop app, the Rust core sidecar, the JSON-RPC bridge, and the dual sockets fit together. Read this before you make non-trivial changes.
  4. and . The React app and the desktop host that wraps it.


## 
Testing
OpenHuman ships with three test layers. Know which one your change belongs in:
  * . When to write Vitest vs cargo tests vs WDIO.
  * . WDIO/Appium specs, dual-platform setup (Linux tauri-driver, macOS Appium Mac2), and how to run a single spec locally.
  * . The artifact-capture layer that makes E2E and agent runs debuggable after the fact.


PRs must clear the **≥ 80% coverage on changed lines** gate. Add tests for new behavior, not just the happy path.
## 
Shipping
  * . Version policy, release cadence, OAuth + installer rules.
  * . Backend/cloud-side deployment when a change crosses the desktop boundary.


## 
Going deeper
  * . The agent's code-focused tool surface and how to extend it.
  * [**Chromium Embedded Framework**](https://tinyhumans.gitbook.io/openhuman/developing/cef). How embedded provider webviews work, why they don't run injected JS, and what the per-provider scanners do instead.


For features still being built, the page covers the background task evaluation system end-to-end.
## 
Contributing
  * Open issues and PRs at [tinyhumansai/openhumanarrow-up-right](https://github.com/tinyhumansai/openhuman).
  * PRs target `main`. Push to your fork, not upstream.
  * Follow [`CONTRIBUTING.md`arrow-up-right](https://github.com/tinyhumansai/openhuman/blob/main/CONTRIBUTING.md) and the issue/PR templates.
  * Keep changes focused. A bug fix doesn't need surrounding cleanup; a one-shot operation doesn't need a helper.


Help building toward AGI doesn't have to mean shipping a kernel - bugfixes, docs, integrations, and tests all move the bar.
[PreviousCloud Deploychevron-left](https://tinyhumans.gitbook.io/openhuman/features/cloud-deploy)[NextGetting Set Upchevron-right](https://tinyhumans.gitbook.io/openhuman/developing/getting-set-up)
Last updated 14 hours ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
