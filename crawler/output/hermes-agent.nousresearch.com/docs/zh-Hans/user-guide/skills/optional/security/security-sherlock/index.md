<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock -->

本页总览
OSINT username search across 400+ social networks. Hunt down social media accounts by username.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#skill-metadata "Skill metadata的直接链接")  
| Source  | Optional — install with `hermes skills install official/security/sherlock`  |  
| --- | --- |  
| Path  | `optional-skills/security/sherlock`  |  
| Version  | `1.0.0`  |  
| Author  | unmodeled-tyler  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `osint`, `security`, `username`, `social-media`, `reconnaissance`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Sherlock OSINT Username Search
Hunt down social media accounts by username across 400+ social networks using the [Sherlock Project](https://github.com/sherlock-project/sherlock).
## When to Use[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#when-to-use "When to Use的直接链接")
  * User asks to find accounts associated with a username
  * User wants to check username availability across platforms
  * User is conducting OSINT or reconnaissance research
  * User asks "where is this username registered?" or similar


## Requirements[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#requirements "Requirements的直接链接")
  * Sherlock CLI installed: `pipx install sherlock-project` or `pip install sherlock-project`
  * Alternatively: Docker available (`docker run -it --rm sherlock/sherlock`)
  * Network access to query social platforms


## Procedure[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#procedure "Procedure的直接链接")
### 1. Check if Sherlock is Installed[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#1-check-if-sherlock-is-installed "1. Check if Sherlock is Installed的直接链接")
**Before doing anything else** , verify sherlock is available:

```
sherlock --version
```

If the command fails:
  * Offer to install: `pipx install sherlock-project` (recommended) or `pip install sherlock-project`
  * **Do NOT** try multiple installation methods — pick one and proceed
  * If installation fails, inform the user and stop


### 2. Extract Username[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#2-extract-username "2. Extract Username的直接链接")
**Extract the username directly from the user's message if clearly stated.**
Examples where you should **NOT** use clarify:
  * "Find accounts for nasa" → username is `nasa`
  * "Search for johndoe123" → username is `johndoe123`
  * "Check if alice exists on social media" → username is `alice`
  * "Look up user bob on social networks" → username is `bob`


**Only use clarify if:**
  * Multiple potential usernames mentioned ("search for alice or bob")
  * Ambiguous phrasing ("search for my username" without specifying)
  * No username mentioned at all ("do an OSINT search")


When extracting, take the **exact** username as stated — preserve case, numbers, underscores, etc.
### 3. Build Command[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#3-build-command "3. Build Command的直接链接")
**Default command** (use this unless user specifically requests otherwise):

```
sherlock --print-found --no-color "<username>"--timeout90
```

**Optional flags** (only add if user explicitly requests):
  * `--nsfw` — Include NSFW sites (only if user asks)
  * `--tor` — Route through Tor (only if user asks for anonymity)


**Do NOT ask about options via clarify** — just run the default search. Users can request specific options if needed.
### 4. Execute Search[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#4-execute-search "4. Execute Search的直接链接")
Run via the `terminal` tool. The command typically takes 30-120 seconds depending on network conditions and site count.
**Example terminal call:**

```
"command":"sherlock --print-found --no-color \"target_username\"","timeout":180
```

### 5. Parse and Present Results[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#5-parse-and-present-results "5. Parse and Present Results的直接链接")
Sherlock outputs found accounts in a simple format. Parse the output and present:
  1. **Summary line:** "Found X accounts for username 'Y'"
  2. **Categorized links:** Group by platform type if helpful (social, professional, forums, etc.)
  3. **Output file location:** Sherlock saves results to `<username>.txt` by default


**Example output parsing:**

```
[+] Instagram: https://instagram.com/username[+] Twitter: https://twitter.com/username[+] GitHub: https://github.com/username
```

Present findings as clickable links when possible.
## Pitfalls[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#pitfalls "Pitfalls的直接链接")
### No Results Found[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#no-results-found "No Results Found的直接链接")
If Sherlock finds no accounts, this is often correct — the username may not be registered on checked platforms. Suggest:
  * Checking spelling/variation
  * Trying similar usernames with `?` wildcard: `sherlock "user?name"`
  * The user may have privacy settings or deleted accounts


### Timeout Issues[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#timeout-issues "Timeout Issues的直接链接")
Some sites are slow or block automated requests. Use `--timeout 120` to increase wait time, or `--site` to limit scope.
### Tor Configuration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#tor-configuration "Tor Configuration的直接链接")
`--tor` requires Tor daemon running. If user wants anonymity but Tor isn't available, suggest:
  * Installing Tor service
  * Using `--proxy` with an alternative proxy


### False Positives[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#false-positives "False Positives的直接链接")
Some sites always return "found" due to their response structure. Cross-reference unexpected results with manual checks.
### Rate Limiting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#rate-limiting "Rate Limiting的直接链接")
Aggressive searches may trigger rate limits. For bulk username searches, add delays between calls or use `--local` with cached data.
## Installation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#installation "Installation的直接链接")
### pipx (recommended)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#pipx-recommended "pipx \(recommended\)的直接链接")

```
pipx install sherlock-project
```

### pip[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#pip "pip的直接链接")

```
pip install sherlock-project
```

### Docker[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#docker "Docker的直接链接")

```
docker pull sherlock/sherlockdocker run -it--rm sherlock/sherlock <username>
```

### Linux packages[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#linux-packages "Linux packages的直接链接")
Available on Debian 13+, Ubuntu 22.10+, Homebrew, Kali, BlackArch.
## Ethical Use[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#ethical-use "Ethical Use的直接链接")
This tool is for legitimate OSINT and research purposes only. Remind users:
  * Only search usernames they own or have permission to investigate
  * Respect platform terms of service
  * Do not use for harassment, stalking, or illegal activities
  * Consider privacy implications before sharing results


## Verification[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#verification "Verification的直接链接")
After running sherlock, verify:
  1. Output lists found sites with URLs
  2. `<username>.txt` file created (default output) if using file output
  3. If `--print-found` used, output should only contain `[+]` lines for matches


## Example Interaction[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#example-interaction "Example Interaction的直接链接")
**User:** "Can you check if the username 'johndoe123' exists on social media?"
**Agent procedure:**
  1. Check `sherlock --version` (verify installed)
  2. Username provided — proceed directly
  3. Run: `sherlock --print-found --no-color "johndoe123" --timeout 90`
  4. Parse output and present links


**Response format:**
> Found 12 accounts for username 'johndoe123':
> • <https://twitter.com/johndoe123> • <https://github.com/johndoe123> • <https://instagram.com/johndoe123> • [... additional links]
> Results saved to: johndoe123.txt
**User:** "Search for username 'alice' including NSFW sites"
**Agent procedure:**
  1. Check sherlock installed
  2. Username + NSFW flag both provided
  3. Run: `sherlock --print-found --no-color --nsfw "alice" --timeout 90`
  4. Present results


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#reference-full-skillmd)
  * [When to Use](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#when-to-use)
  * [Requirements](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#requirements)
  * [Procedure](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#procedure)
    * [1. Check if Sherlock is Installed](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#1-check-if-sherlock-is-installed)
    * [2. Extract Username](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#2-extract-username)
    * [3. Build Command](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#3-build-command)
    * [4. Execute Search](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#4-execute-search)
    * [5. Parse and Present Results](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#5-parse-and-present-results)
  * [Pitfalls](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#pitfalls)
    * [No Results Found](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#no-results-found)
    * [Timeout Issues](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#timeout-issues)
    * [Tor Configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#tor-configuration)
    * [False Positives](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#false-positives)
    * [Rate Limiting](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#rate-limiting)
  * [Installation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#installation)
    * [pipx (recommended)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#pipx-recommended)
    * [Linux packages](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#linux-packages)
  * [Ethical Use](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#ethical-use)
  * [Verification](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#verification)
  * [Example Interaction](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/security/security-sherlock#example-interaction)


