<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player -->

本页总览
Play Pokemon via headless emulator + RAM reads.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#skill-metadata "Skill metadata的直接链接")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/gaming/pokemon-player`  |  
| Platforms  | linux, macos, windows  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Pokemon Player
Play Pokemon games via headless emulation using the `pokemon-agent` package.
## When to Use[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#when-to-use "When to Use的直接链接")
  * User says "play pokemon", "start pokemon", "pokemon game"
  * User asks about Pokemon Red, Blue, Yellow, FireRed, etc.
  * User wants to watch an AI play Pokemon
  * User references a ROM file (.gb, .gbc, .gba)


## Startup Procedure[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#startup-procedure "Startup Procedure的直接链接")
### 1. First-time setup (clone, venv, install)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#1-first-time-setup-clone-venv-install "1. First-time setup \(clone, venv, install\)的直接链接")
The repo is NousResearch/pokemon-agent on GitHub. Clone it, then set up a Python 3.10+ virtual environment. Use uv (preferred for speed) to create the venv and install the package in editable mode with the pyboy extra. If uv is not available, fall back to python3 -m venv + pip.
On this machine it is already set up at /home/teknium/pokemon-agent with a venv ready — just cd there and source .venv/bin/activate.
You also need a ROM file. Ask the user for theirs. On this machine one exists at roms/pokemon_red.gb inside that directory. NEVER download or provide ROM files — always ask the user.
### 2. Start the game server[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#2-start-the-game-server "2. Start the game server的直接链接")
From inside the pokemon-agent directory with the venv activated, run pokemon-agent serve with --rom pointing to the ROM and --port 9876. Run it in the background with &. To resume from a saved game, add --load-state with the save name. Wait 4 seconds for startup, then verify with GET /health.
### 3. Set up live dashboard for user to watch[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#3-set-up-live-dashboard-for-user-to-watch "3. Set up live dashboard for user to watch的直接链接")
Use an SSH reverse tunnel via localhost.run so the user can view the dashboard in their browser. Connect with ssh, forwarding local port 9876 to remote port 80 on nokey@localhost.run. Redirect output to a log file, wait 10 seconds, then grep the log for the .lhr.life URL. Give the user the URL with /dashboard/ appended. The tunnel URL changes each time — give the user the new one if restarted.
## Save and Load[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#save-and-load "Save and Load的直接链接")
### When to save[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#when-to-save "When to save的直接链接")
  * Every 15-20 turns of gameplay
  * ALWAYS before gym battles, rival encounters, or risky fights
  * Before entering a new town or dungeon
  * Before any action you are unsure about


### How to save[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#how-to-save "How to save的直接链接")
POST /save with a descriptive name. Good examples: before_brock, route1_start, mt_moon_entrance, got_cut
### How to load[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#how-to-load "How to load的直接链接")
POST /load with the save name.
### List available saves[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#list-available-saves "List available saves的直接链接")
GET /saves returns all saved states.
### Loading on server startup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#loading-on-server-startup "Loading on server startup的直接链接")
Use --load-state flag when starting the server to auto-load a save. This is faster than loading via the API after startup.
## The Gameplay Loop[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#the-gameplay-loop "The Gameplay Loop的直接链接")
### Step 1: OBSERVE — check state AND take a screenshot[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-1-observe--check-state-and-take-a-screenshot "Step 1: OBSERVE — check state AND take a screenshot的直接链接")
GET /state for position, HP, battle, dialog. GET /screenshot and save to /tmp/pokemon.png, then use vision_analyze. Always do BOTH — RAM state gives numbers, vision gives spatial awareness.
### Step 2: ORIENT[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-2-orient "Step 2: ORIENT的直接链接")
  * Dialog/text on screen → advance it
  * In battle → fight or run
  * Party hurt → head to Pokemon Center
  * Near objective → navigate carefully


### Step 3: DECIDE[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-3-decide "Step 3: DECIDE的直接链接")
Priority: dialog > battle > heal > story objective > training > explore
### Step 4: ACT — move 2-4 steps max, then re-check[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-4-act--move-2-4-steps-max-then-re-check "Step 4: ACT — move 2-4 steps max, then re-check的直接链接")
POST /action with a SHORT action list (2-4 actions, not 10-15).
### Step 5: VERIFY — screenshot after every move sequence[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-5-verify--screenshot-after-every-move-sequence "Step 5: VERIFY — screenshot after every move sequence的直接链接")
Take a screenshot and use vision_analyze to confirm you moved where intended. This is the MOST IMPORTANT step. Without vision you WILL get lost.
### Step 6: RECORD progress to memory with PKM: prefix[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-6-record-progress-to-memory-with-pkm-prefix "Step 6: RECORD progress to memory with PKM: prefix的直接链接")
### Step 7: SAVE periodically[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-7-save-periodically "Step 7: SAVE periodically的直接链接")
## Action Reference[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#action-reference "Action Reference的直接链接")
  * press_a — confirm, talk, select
  * press_b — cancel, close menu
  * press_start — open game menu
  * walk_up/down/left/right — move one tile
  * hold_b_N — hold B for N frames (use for speeding through text)
  * wait_60 — wait about 1 second (60 frames)
  * a_until_dialog_end — press A repeatedly until dialog clears


## Critical Tips from Experience[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#critical-tips-from-experience "Critical Tips from Experience的直接链接")
### USE VISION CONSTANTLY[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#use-vision-constantly "USE VISION CONSTANTLY的直接链接")
  * Take a screenshot every 2-4 movement steps
  * The RAM state tells you position and HP but NOT what is around you
  * Ledges, fences, signs, building doors, NPCs — only visible via screenshot
  * Ask the vision model specific questions: "what is one tile north of me?"
  * When stuck, always screenshot before trying random directions


### Warp Transitions Need Extra Wait Time[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#warp-transitions-need-extra-wait-time "Warp Transitions Need Extra Wait Time的直接链接")
When walking through a door or stairs, the screen fades to black during the map transition. You MUST wait for it to complete. Add 2-3 wait_60 actions after any door/stair warp. Without waiting, the position reads as stale and you will think you are still in the old map.
### Building Exit Trap[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#building-exit-trap "Building Exit Trap的直接链接")
When you exit a building, you appear directly IN FRONT of the door. If you walk north, you go right back inside. ALWAYS sidestep first by walking left or right 2 tiles, then proceed in your intended direction.
### Dialog Handling[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#dialog-handling "Dialog Handling的直接链接")
Gen 1 text scrolls slowly letter-by-letter. To speed through dialog, hold B for 120 frames then press A. Repeat as needed. Holding B makes text display at max speed. Then press A to advance to the next line. The a_until_dialog_end action checks the RAM dialog flag, but this flag does not catch ALL text states. If dialog seems stuck, use the manual hold_b + press_a pattern instead and verify via screenshot.
### Ledges Are One-Way[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#ledges-are-one-way "Ledges Are One-Way的直接链接")
Ledges (small cliff edges) can only be jumped DOWN (south), never climbed UP (north). If blocked by a ledge going north, you must go left or right to find the gap around it. Use vision to identify which direction the gap is. Ask the vision model explicitly.
### Navigation Strategy[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#navigation-strategy "Navigation Strategy的直接链接")
  * Move 2-4 steps at a time, then screenshot to check position
  * When entering a new area, screenshot immediately to orient
  * Ask the vision model "which direction to [destination]?"
  * If stuck for 3+ attempts, screenshot and re-evaluate completely
  * Do not spam 10-15 movements — you will overshoot or get stuck


### Running from Wild Battles[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#running-from-wild-battles "Running from Wild Battles的直接链接")
On the battle menu, RUN is bottom-right. To reach it from the default cursor position (FIGHT, top-left): press down then right to move cursor to RUN, then press A. Wrap with hold_b to speed through text/animations.
### Battling (FIGHT)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#battling-fight "Battling \(FIGHT\)的直接链接")
On the battle menu FIGHT is top-left (default cursor position). Press A to enter move selection, A again to use the first move. Then hold B to speed through attack animations and text.
## Battle Strategy[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#battle-strategy "Battle Strategy的直接链接")
### Decision Tree[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#decision-tree "Decision Tree的直接链接")
  1. Want to catch? → Weaken then throw Poke Ball
  2. Wild you don't need? → RUN
  3. Type advantage? → Use super-effective move
  4. No advantage? → Use strongest STAB move
  5. Low HP? → Switch or use Potion


### Gen 1 Type Chart (key matchups)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#gen-1-type-chart-key-matchups "Gen 1 Type Chart \(key matchups\)的直接链接")
  * Water beats Fire, Ground, Rock
  * Fire beats Grass, Bug, Ice
  * Grass beats Water, Ground, Rock
  * Electric beats Water, Flying
  * Ground beats Fire, Electric, Rock, Poison
  * Psychic beats Fighting, Poison (dominant in Gen 1!)


### Gen 1 Quirks[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#gen-1-quirks "Gen 1 Quirks的直接链接")
  * Special stat = both offense AND defense for special moves
  * Psychic type is overpowered (Ghost moves bugged)
  * Critical hits based on Speed stat
  * Wrap/Bind prevent opponent from acting
  * Focus Energy bug: REDUCES crit rate instead of raising it


## Memory Conventions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#memory-conventions "Memory Conventions的直接链接")  
| Prefix  | Purpose  | Example  |  
| --- | --- | --- |  
| PKM:OBJECTIVE  | Current goal  | Get Parcel from Viridian Mart  |  
| PKM:MAP  | Navigation knowledge  | Viridian: mart is northeast  |  
| PKM:STRATEGY  | Battle/team plans  | Need Grass type before Misty  |  
| PKM:PROGRESS  | Milestone tracker  | Beat rival, heading to Viridian  |  
| PKM:STUCK  | Stuck situations  | Ledge at y=28 go right to bypass  |  
| PKM:TEAM  | Team notes  | Squirtle Lv6, Tackle + Tail Whip  |  
## Progression Milestones[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#progression-milestones "Progression Milestones的直接链接")
  * Choose starter
  * Deliver Parcel from Viridian Mart, receive Pokedex
  * Boulder Badge — Brock (Rock) → use Water/Grass
  * Cascade Badge — Misty (Water) → use Grass/Electric
  * Thunder Badge — Lt. Surge (Electric) → use Ground
  * Rainbow Badge — Erika (Grass) → use Fire/Ice/Flying
  * Soul Badge — Koga (Poison) → use Ground/Psychic
  * Marsh Badge — Sabrina (Psychic) → hardest gym
  * Volcano Badge — Blaine (Fire) → use Water/Ground
  * Earth Badge — Giovanni (Ground) → use Water/Grass/Ice
  * Elite Four → Champion!


## Stopping Play[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#stopping-play "Stopping Play的直接链接")
  1. Save the game with a descriptive name via POST /save
  2. Update memory with PKM:PROGRESS
  3. Tell user: "Game saved as [name]! Say 'play pokemon' to resume."
  4. Kill the server and tunnel background processes


## Pitfalls[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#pitfalls "Pitfalls的直接链接")
  * NEVER download or provide ROM files
  * Do NOT send more than 4-5 actions without checking vision
  * Always sidestep after exiting buildings before going north
  * Always add wait_60 x2-3 after door/stair warps
  * Dialog detection via RAM is unreliable — verify with screenshots
  * Save BEFORE risky encounters
  * The tunnel URL changes each time you restart it


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#reference-full-skillmd)
  * [When to Use](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#when-to-use)
  * [Startup Procedure](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#startup-procedure)
    * [1. First-time setup (clone, venv, install)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#1-first-time-setup-clone-venv-install)
    * [2. Start the game server](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#2-start-the-game-server)
    * [3. Set up live dashboard for user to watch](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#3-set-up-live-dashboard-for-user-to-watch)
  * [Save and Load](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#save-and-load)
    * [When to save](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#when-to-save)
    * [How to save](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#how-to-save)
    * [How to load](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#how-to-load)
    * [List available saves](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#list-available-saves)
    * [Loading on server startup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#loading-on-server-startup)
  * [The Gameplay Loop](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#the-gameplay-loop)
    * [Step 1: OBSERVE — check state AND take a screenshot](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-1-observe--check-state-and-take-a-screenshot)
    * [Step 2: ORIENT](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-2-orient)
    * [Step 3: DECIDE](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-3-decide)
    * [Step 4: ACT — move 2-4 steps max, then re-check](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-4-act--move-2-4-steps-max-then-re-check)
    * [Step 5: VERIFY — screenshot after every move sequence](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-5-verify--screenshot-after-every-move-sequence)
    * [Step 6: RECORD progress to memory with PKM: prefix](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-6-record-progress-to-memory-with-pkm-prefix)
    * [Step 7: SAVE periodically](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#step-7-save-periodically)
  * [Action Reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#action-reference)
  * [Critical Tips from Experience](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#critical-tips-from-experience)
    * [USE VISION CONSTANTLY](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#use-vision-constantly)
    * [Warp Transitions Need Extra Wait Time](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#warp-transitions-need-extra-wait-time)
    * [Building Exit Trap](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#building-exit-trap)
    * [Dialog Handling](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#dialog-handling)
    * [Ledges Are One-Way](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#ledges-are-one-way)
    * [Navigation Strategy](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#navigation-strategy)
    * [Running from Wild Battles](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#running-from-wild-battles)
    * [Battling (FIGHT)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#battling-fight)
  * [Battle Strategy](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#battle-strategy)
    * [Decision Tree](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#decision-tree)
    * [Gen 1 Type Chart (key matchups)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#gen-1-type-chart-key-matchups)
    * [Gen 1 Quirks](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#gen-1-quirks)
  * [Memory Conventions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#memory-conventions)
  * [Progression Milestones](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#progression-milestones)
  * [Stopping Play](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/gaming/gaming-pokemon-player#stopping-play)


