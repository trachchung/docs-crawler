<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer -->

本页总览
Index a codebase with GitNexus and serve an interactive knowledge graph via web UI + Cloudflare tunnel.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#skill-metadata "Skill metadata的直接链接")  
| Source  | Optional — install with `hermes skills install official/research/gitnexus-explorer`  |  
| --- | --- |  
| Path  | `optional-skills/research/gitnexus-explorer`  |  
| Version  | `1.0.0`  |  
| Author  | Hermes Agent + Teknium  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `gitnexus`, `code-intelligence`, `knowledge-graph`, `visualization`  |  
| Related skills  |  [`native-mcp`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/mcp/mcp-native-mcp), [`codebase-inspection`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/github/github-codebase-inspection)  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# GitNexus Explorer
Index any codebase into a knowledge graph and serve an interactive web UI for exploring symbols, call chains, clusters, and execution flows. Tunneled via Cloudflare for remote access.
## When to Use[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#when-to-use "When to Use的直接链接")
  * User wants to visually explore a codebase's architecture
  * User asks for a knowledge graph / dependency graph of a repo
  * User wants to share an interactive codebase explorer with someone


## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#prerequisites "Prerequisites的直接链接")
  * **Node.js** (v18+) — required for GitNexus and the proxy
  * **git** — repo must have a `.git` directory
  * **cloudflared** — for tunneling (auto-installed to ~/.local/bin if missing)


## Size Warning[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#size-warning "Size Warning的直接链接")
The web UI renders all nodes in the browser. Repos under ~5,000 files work well. Large repos (30k+ nodes) will be sluggish or crash the browser tab. The CLI/MCP tools work at any scale — only the web visualization has this limit.
## Steps[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#steps "Steps的直接链接")
### 1. Clone and Build GitNexus (one-time setup)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#1-clone-and-build-gitnexus-one-time-setup "1. Clone and Build GitNexus \(one-time setup\)的直接链接")

```
GITNEXUS_DIR="${GITNEXUS_DIR:-$HOME/.local/share/gitnexus}"if[!-d"$GITNEXUS_DIR/gitnexus-web/dist"];thengit clone https://github.com/abhigyanpatwari/GitNexus.git "$GITNEXUS_DIR"cd"$GITNEXUS_DIR/gitnexus-shared"&&npminstall&&npm run buildcd"$GITNEXUS_DIR/gitnexus-web"&&npminstall
```

### 2. Patch the Web UI for Remote Access[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#2-patch-the-web-ui-for-remote-access "2. Patch the Web UI for Remote Access的直接链接")
The web UI defaults to `localhost:4747` for API calls. Patch it to use same-origin so it works through a tunnel/proxy:
**File:`$GITNEXUS_DIR/gitnexus-web/src/config/ui-constants.ts`** Change:

```
exportconstDEFAULT_BACKEND_URL='http://localhost:4747';
```

To:

```
exportconstDEFAULT_BACKEND_URL=typeof window !=='undefined'&& window.location.hostname !=='localhost'? window.location.origin :'http://localhost:4747';
```

**File:`$GITNEXUS_DIR/gitnexus-web/vite.config.ts`** Add `allowedHosts: true` inside the `server: { }` block (only needed if running dev mode instead of production build):

```
server:{    allowedHosts:true,// ... existing config
```

Then build the production bundle:

```
cd"$GITNEXUS_DIR/gitnexus-web"&& npx vite build
```

### 3. Index the Target Repo[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#3-index-the-target-repo "3. Index the Target Repo的直接链接")

```
cd /path/to/target-reponpx gitnexus analyze --skip-agents-mdrm-rf .claude/    # remove Claude Code-specific artifacts
```

Add `--embeddings` for semantic search (slower — minutes instead of seconds).
The index lives in `.gitnexus/` inside the repo (auto-gitignored).
### 4. Create the Proxy Script[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#4-create-the-proxy-script "4. Create the Proxy Script的直接链接")
Write this to a file (e.g., `$GITNEXUS_DIR/proxy.mjs`). It serves the production web UI and proxies `/api/*` to the GitNexus backend — same origin, no CORS issues, no sudo, no nginx.

```
importhttpfrom'node:http';importfsfrom'node:fs';importpathfrom'node:path';constAPI_PORT=parseInt(process.env.API_PORT||'4747');constDIST_DIR= process.argv[2]||'./dist';constPORT=parseInt(process.argv[3]||'8888');constMIME={'.html':'text/html','.js':'application/javascript','.css':'text/css','.json':'application/json','.png':'image/png','.svg':'image/svg+xml','.ico':'image/x-icon','.woff2':'font/woff2','.woff':'font/woff','.wasm':'application/wasm',functionproxyToApi(req, res){const opts ={hostname:'127.0.0.1',port:API_PORT,path: req.url,method: req.method,headers: req.headers,const proxy = http.request(opts,(upstream)=>{    res.writeHead(upstream.statusCode, upstream.headers);    upstream.pipe(res,{end:true});});  proxy.on('error',()=>{ res.writeHead(502); res.end('Backend unavailable');});  req.pipe(proxy,{end:true});functionserveStatic(req, res){let filePath = path.join(DIST_DIR, req.url==='/'?'index.html': req.url.split('?')[0]);if(!fs.existsSync(filePath)) filePath = path.join(DIST_DIR,'index.html');const ext = path.extname(filePath);const mime =MIME[ext]||'application/octet-stream';try{const data = fs.readFileSync(filePath);    res.writeHead(200,{'Content-Type': mime,'Cache-Control':'public, max-age=3600'});    res.end(data);}catch{ res.writeHead(404); res.end('Not found');}http.createServer((req, res)=>{if(req.url.startsWith('/api'))proxyToApi(req, res);elseserveStatic(req, res);}).listen(PORT,()=>console.log(`GitNexus proxy on http://localhost:${PORT}`));
```

### 5. Start the Services[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#5-start-the-services "5. Start the Services的直接链接")

```
# Terminal 1: GitNexus backend APInpx gitnexus serve &# Terminal 2: Proxy (web UI + API on one port)node"$GITNEXUS_DIR/proxy.mjs""$GITNEXUS_DIR/gitnexus-web/dist"8888&
```

Verify: `curl -s http://localhost:8888/api/repos` should return the indexed repo(s).
### 6. Tunnel with Cloudflare (optional — for remote access)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#6-tunnel-with-cloudflare-optional--for-remote-access "6. Tunnel with Cloudflare \(optional — for remote access\)的直接链接")

```
# Install cloudflared if needed (no sudo)if!command-v cloudflared &>/dev/null;thenmkdir-p ~/.local/bincurl-sL https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 \-o ~/.local/bin/cloudflaredchmod +x ~/.local/bin/cloudflaredexportPATH="$HOME/.local/bin:$PATH"# Start tunnel (--config /dev/null avoids conflicts with existing named tunnels)cloudflared tunnel --config /dev/null --url http://localhost:8888 --no-autoupdate --protocol http2
```

The tunnel URL (e.g., `https://random-words.trycloudflare.com`) is printed to stderr. Share it — anyone with the link can explore the graph.
### 7. Cleanup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#7-cleanup "7. Cleanup的直接链接")

```
# Stop servicespkill-f"gitnexus serve"pkill-f"proxy.mjs"pkill-f cloudflared# Remove index from the target repocd /path/to/target-reponpx gitnexus cleanrm-rf .claude/
```

## Pitfalls[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#pitfalls "Pitfalls的直接链接")
  * **`--config /dev/null`is required for cloudflared** if the user has an existing named tunnel config at `~/.cloudflared/config.yml`. Without it, the catch-all ingress rule in the config returns 404 for all quick tunnel requests.
  * **Production build is mandatory for tunneling.** The Vite dev server blocks non-localhost hosts by default (`allowedHosts`). The production build + Node proxy avoids this entirely.
  * **The web UI does NOT create`.claude/` or `CLAUDE.md`.** Those are created by `npx gitnexus analyze`. Use `--skip-agents-md` to suppress the markdown files, then `rm -rf .claude/` for the rest. These are Claude Code integrations that hermes-agent users don't need.
  * **Browser memory limit.** The web UI loads the entire graph into browser memory. Repos with 5k+ files may be sluggish. 30k+ files will likely crash the tab.
  * **Embeddings are optional.** `--embeddings` enables semantic search but takes minutes on large repos. Skip it for quick exploration; add it if you want natural language queries via the AI chat panel.
  * **Multiple repos.** `gitnexus serve` serves ALL indexed repos. Index several repos, start serve once, and the web UI lets you switch between them.


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#reference-full-skillmd)
  * [When to Use](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#when-to-use)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#prerequisites)
  * [Size Warning](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#size-warning)
  * [Steps](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#steps)
    * [1. Clone and Build GitNexus (one-time setup)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#1-clone-and-build-gitnexus-one-time-setup)
    * [2. Patch the Web UI for Remote Access](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#2-patch-the-web-ui-for-remote-access)
    * [3. Index the Target Repo](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#3-index-the-target-repo)
    * [4. Create the Proxy Script](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#4-create-the-proxy-script)
    * [5. Start the Services](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#5-start-the-services)
    * [6. Tunnel with Cloudflare (optional — for remote access)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-gitnexus-explorer#6-tunnel-with-cloudflare-optional--for-remote-access)


