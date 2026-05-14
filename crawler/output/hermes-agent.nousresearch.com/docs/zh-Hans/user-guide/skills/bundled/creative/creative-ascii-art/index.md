<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art -->

本页总览
ASCII art: pyfiglet, cowsay, boxes, image-to-ascii.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#skill-metadata "Skill metadata的直接链接")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/creative/ascii-art`  |  
| Version  | `4.0.0`  |  
| Author  | 0xbyt4, Hermes Agent  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `ASCII`, `Art`, `Banners`, `Creative`, `Unicode`, `Text-Art`, `pyfiglet`, `figlet`, `cowsay`, `boxes`  |  
| Related skills  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# ASCII Art Skill
Multiple tools for different ASCII art needs. All tools are local CLI programs or free REST APIs — no API keys required.
## Tool 1: Text Banners (pyfiglet — local)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-1-text-banners-pyfiglet--local "Tool 1: Text Banners \(pyfiglet — local\)的直接链接")
Render text as large ASCII art banners. 571 built-in fonts.
### Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#setup "Setup的直接链接")

```
pip install pyfiglet --break-system-packages -q
```

### Usage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#usage "Usage的直接链接")

```
python3 -m pyfiglet "YOUR TEXT"-f slantpython3 -m pyfiglet "TEXT"-f doom -w80# Set widthpython3 -m pyfiglet --list_fonts# List all 571 fonts
```

### Recommended fonts[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#recommended-fonts "Recommended fonts的直接链接")  
| Style  | Font  | Best for  |  
| --- | --- | --- |  
| Clean & modern  | `slant`  | Project names, headers  |  
| Bold & blocky  | `doom`  | Titles, logos  |  
| Big & readable  | `big`  | Banners  |  
| Classic banner  | `banner3`  | Wide displays  |  
| Compact  | `small`  | Subtitles  |  
| Cyberpunk  | `cyberlarge`  | Tech themes  |  
| 3D effect  | `3-d`  | Splash screens  |  
| Gothic  | `gothic`  | Dramatic text  |  
### Tips[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tips "Tips的直接链接")
  * Preview 2-3 fonts and let the user pick their favorite
  * Short text (1-8 chars) works best with detailed fonts like `doom` or `block`
  * Long text works better with compact fonts like `small` or `mini`


## Tool 2: Text Banners (asciified API — remote, no install)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-2-text-banners-asciified-api--remote-no-install "Tool 2: Text Banners \(asciified API — remote, no install\)的直接链接")
Free REST API that converts text to ASCII art. 250+ FIGlet fonts. Returns plain text directly — no parsing needed. Use this when pyfiglet is not installed or as a quick alternative.
### Usage (via terminal curl)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#usage-via-terminal-curl "Usage \(via terminal curl\)的直接链接")

```
# Basic text banner (default font)curl-s"https://asciified.thelicato.io/api/v2/ascii?text=Hello+World"# With a specific fontcurl-s"https://asciified.thelicato.io/api/v2/ascii?text=Hello&font=Slant"curl-s"https://asciified.thelicato.io/api/v2/ascii?text=Hello&font=Doom"curl-s"https://asciified.thelicato.io/api/v2/ascii?text=Hello&font=Star+Wars"curl-s"https://asciified.thelicato.io/api/v2/ascii?text=Hello&font=3-D"curl-s"https://asciified.thelicato.io/api/v2/ascii?text=Hello&font=Banner3"# List all available fonts (returns JSON array)curl-s"https://asciified.thelicato.io/api/v2/fonts"
```

### Tips[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tips-1 "Tips的直接链接")
  * URL-encode spaces as `+` in the text parameter
  * The response is plain text ASCII art — no JSON wrapping, ready to display
  * Font names are case-sensitive; use the fonts endpoint to get exact names
  * Works from any terminal with curl — no Python or pip needed


## Tool 3: Cowsay (Message Art)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-3-cowsay-message-art "Tool 3: Cowsay \(Message Art\)的直接链接")
Classic tool that wraps text in a speech bubble with an ASCII character.
### Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#setup-1 "Setup的直接链接")

```
sudoaptinstall cowsay -y# Debian/Ubuntu# brew install cowsay         # macOS
```

### Usage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#usage-1 "Usage的直接链接")

```
cowsay "Hello World"cowsay -f tux "Linux rules"# Tux the penguincowsay -f dragon "Rawr!"# Dragoncowsay -f stegosaurus "Roar!"# Stegosauruscowthink "Hmm..."# Thought bubblecowsay -l# List all characters
```

### Available characters (50+)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#available-characters-50 "Available characters \(50+\)的直接链接")
`beavis.zen`, `bong`, `bunny`, `cheese`, `daemon`, `default`, `dragon`, `dragon-and-cow`, `elephant`, `eyes`, `flaming-skull`, `ghostbusters`, `hellokitty`, `kiss`, `kitty`, `koala`, `luke-koala`, `mech-and-cow`, `meow`, `moofasa`, `moose`, `ren`, `sheep`, `skeleton`, `small`, `stegosaurus`, `stimpy`, `supermilker`, `surgery`, `three-eyes`, `turkey`, `turtle`, `tux`, `udder`, `vader`, `vader-koala`, `www`
### Eye/tongue modifiers[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#eyetongue-modifiers "Eye/tongue modifiers的直接链接")

```
cowsay -b"Borg"# =_= eyescowsay -d"Dead"# x_x eyescowsay -g"Greedy"# $_$ eyescowsay -p"Paranoid"# @_@ eyescowsay -s"Stoned"# *_* eyescowsay -w"Wired"# O_O eyescowsay -e"OO""Msg"# Custom eyescowsay -T"U ""Msg"# Custom tongue
```

## Tool 4: Boxes (Decorative Borders)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-4-boxes-decorative-borders "Tool 4: Boxes \(Decorative Borders\)的直接链接")
Draw decorative ASCII art borders/frames around any text. 70+ built-in designs.
### Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#setup-2 "Setup的直接链接")

```
sudoaptinstall boxes -y# Debian/Ubuntu# brew install boxes         # macOS
```

### Usage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#usage-2 "Usage的直接链接")

```
echo"Hello World"| boxes                    # Default boxecho"Hello World"| boxes -d stone           # Stone borderecho"Hello World"| boxes -d parchment       # Parchment scrollecho"Hello World"| boxes -dcat# Cat borderecho"Hello World"| boxes -d dog             # Dog borderecho"Hello World"| boxes -d unicornsay      # Unicornecho"Hello World"| boxes -d diamonds        # Diamond patternecho"Hello World"| boxes -d c-cmt           # C-style commentecho"Hello World"| boxes -d html-cmt        # HTML commentecho"Hello World"| boxes -a# Center textboxes -l# List all 70+ designs
```

### Combine with pyfiglet or asciified[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#combine-with-pyfiglet-or-asciified "Combine with pyfiglet or asciified的直接链接")

```
python3 -m pyfiglet "HERMES"-f slant | boxes -d stone# Or without pyfiglet installed:curl-s"https://asciified.thelicato.io/api/v2/ascii?text=HERMES&font=Slant"| boxes -d stone
```

## Tool 5: TOIlet (Colored Text Art)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-5-toilet-colored-text-art "Tool 5: TOIlet \(Colored Text Art\)的直接链接")
Like pyfiglet but with ANSI color effects and visual filters. Great for terminal eye candy.
### Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#setup-3 "Setup的直接链接")

```
sudoaptinstall toilet toilet-fonts -y# Debian/Ubuntu# brew install toilet                      # macOS
```

### Usage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#usage-3 "Usage的直接链接")

```
toilet "Hello World"# Basic text arttoilet -f bigmono12 "Hello"# Specific fonttoilet --gay"Rainbow!"# Rainbow coloringtoilet --metal"Metal!"# Metallic effecttoilet -F border "Bordered"# Add bordertoilet -F border --gay"Fancy!"# Combined effectstoilet -f pagga "Block"# Block-style font (unique to toilet)toilet -F list                          # List available filters
```

### Filters[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#filters "Filters的直接链接")
`crop`, `gay` (rainbow), `metal`, `flip`, `flop`, `180`, `left`, `right`, `border`
**Note** : toilet outputs ANSI escape codes for colors — works in terminals but may not render in all contexts (e.g., plain text files, some chat platforms).
## Tool 6: Image to ASCII Art[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-6-image-to-ascii-art "Tool 6: Image to ASCII Art的直接链接")
Convert images (PNG, JPEG, GIF, WEBP) to ASCII art.
### Option A: ascii-image-converter (recommended, modern)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#option-a-ascii-image-converter-recommended-modern "Option A: ascii-image-converter \(recommended, modern\)的直接链接")

```
# Installsudo snap install ascii-image-converter# OR: go install github.com/TheZoraiz/ascii-image-converter@latest
```


```
ascii-image-converter image.png                  # Basicascii-image-converter image.png -C# Color outputascii-image-converter image.png -d60,30# Set dimensionsascii-image-converter image.png -b# Braille charactersascii-image-converter image.png -n# Negative/invertedascii-image-converter https://url/image.jpg      # Direct URLascii-image-converter image.png --save-txt out   # Save as text
```

### Option B: jp2a (lightweight, JPEG only)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#option-b-jp2a-lightweight-jpeg-only "Option B: jp2a \(lightweight, JPEG only\)的直接链接")

```
sudoaptinstall jp2a -yjp2a --width=80 image.jpgjp2a --colors image.jpg              # Colorized
```

## Tool 7: Search Pre-Made ASCII Art[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-7-search-pre-made-ascii-art "Tool 7: Search Pre-Made ASCII Art的直接链接")
Search curated ASCII art from the web. Use `terminal` with `curl`.
### Source A: ascii.co.uk (recommended for pre-made art)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#source-a-asciicouk-recommended-for-pre-made-art "Source A: ascii.co.uk \(recommended for pre-made art\)的直接链接")
Large collection of classic ASCII art organized by subject. Art is inside HTML `<pre>` tags. Fetch the page with curl, then extract art with a small Python snippet.
**URL pattern:** `https://ascii.co.uk/art/{subject}`
**Step 1 — Fetch the page:**

```
curl-s'https://ascii.co.uk/art/cat'-o /tmp/ascii_art.html
```

**Step 2 — Extract art from pre tags:**

```
import re, htmlwithopen('/tmp/ascii_art.html')as f:    text = f.read()arts = re.findall(r'<pre[^>]*>(.*?)</pre>', text, re.DOTALL)for art in arts:    clean = re.sub(r'<[^>]+>','', art)    clean = html.unescape(clean).strip()iflen(clean)>30:print(clean)print('\n---\n')
```

**Available subjects** (use as URL path):
  * Animals: `cat`, `dog`, `horse`, `bird`, `fish`, `dragon`, `snake`, `rabbit`, `elephant`, `dolphin`, `butterfly`, `owl`, `wolf`, `bear`, `penguin`, `turtle`
  * Objects: `car`, `ship`, `airplane`, `rocket`, `guitar`, `computer`, `coffee`, `beer`, `cake`, `house`, `castle`, `sword`, `crown`, `key`
  * Nature: `tree`, `flower`, `sun`, `moon`, `star`, `mountain`, `ocean`, `rainbow`
  * Characters: `skull`, `robot`, `angel`, `wizard`, `pirate`, `ninja`, `alien`
  * Holidays: `christmas`, `halloween`, `valentine`


**Tips:**
  * Preserve artist signatures/initials — important etiquette
  * Multiple art pieces per page — pick the best one for the user
  * Works reliably via curl, no JavaScript needed


### Source B: GitHub Octocat API (fun easter egg)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#source-b-github-octocat-api-fun-easter-egg "Source B: GitHub Octocat API \(fun easter egg\)的直接链接")
Returns a random GitHub Octocat with a wise quote. No auth needed.

```
curl-s https://api.github.com/octocat
```

## Tool 8: Fun ASCII Utilities (via curl)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-8-fun-ascii-utilities-via-curl "Tool 8: Fun ASCII Utilities \(via curl\)的直接链接")
These free services return ASCII art directly — great for fun extras.
### QR Codes as ASCII Art[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#qr-codes-as-ascii-art "QR Codes as ASCII Art的直接链接")

```
curl-s"qrenco.de/Hello+World"curl-s"qrenco.de/https://example.com"
```

### Weather as ASCII Art[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#weather-as-ascii-art "Weather as ASCII Art的直接链接")

```
curl-s"wttr.in/London"# Full weather report with ASCII graphicscurl-s"wttr.in/Moon"# Moon phase in ASCII artcurl-s"v2.wttr.in/London"# Detailed version
```

## Tool 9: LLM-Generated Custom Art (Fallback)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-9-llm-generated-custom-art-fallback "Tool 9: LLM-Generated Custom Art \(Fallback\)的直接链接")
When tools above don't have what's needed, generate ASCII art directly using these Unicode characters:
### Character Palette[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#character-palette "Character Palette的直接链接")
**Box Drawing:** `╔ ╗ ╚ ╝ ║ ═ ╠ ╣ ╦ ╩ ╬ ┌ ┐ └ ┘ │ ─ ├ ┤ ┬ ┴ ┼ ╭ ╮ ╰ ╯`
**Block Elements:** `░ ▒ ▓ █ ▄ ▀ ▌ ▐ ▖ ▗ ▘ ▝ ▚ ▞`
**Geometric & Symbols:** `◆ ◇ ◈ ● ○ ◉ ■ □ ▲ △ ▼ ▽ ★ ☆ ✦ ✧ ◀ ▶ ◁ ▷ ⬡ ⬢ ⌂`
### Rules[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#rules "Rules的直接链接")
  * Max width: 60 characters per line (terminal-safe)
  * Max height: 15 lines for banners, 25 for scenes
  * Monospace only: output must render correctly in fixed-width fonts


## Decision Flow[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#decision-flow "Decision Flow的直接链接")
  1. **Text as a banner** → pyfiglet if installed, otherwise asciified API via curl
  2. **Wrap a message in fun character art** → cowsay
  3. **Add decorative border/frame** → boxes (can combine with pyfiglet/asciified)
  4. **Art of a specific thing** (cat, rocket, dragon) → ascii.co.uk via curl + parsing
  5. **Convert an image to ASCII** → ascii-image-converter or jp2a
  6. **QR code** → qrenco.de via curl
  7. **Weather/moon art** → wttr.in via curl
  8. **Something custom/creative** → LLM generation with Unicode palette
  9. **Any tool not installed** → install it, or fall back to next option


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#reference-full-skillmd)
  * [Tool 1: Text Banners (pyfiglet — local)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-1-text-banners-pyfiglet--local)
    * [Recommended fonts](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#recommended-fonts)
  * [Tool 2: Text Banners (asciified API — remote, no install)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-2-text-banners-asciified-api--remote-no-install)
    * [Usage (via terminal curl)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#usage-via-terminal-curl)
  * [Tool 3: Cowsay (Message Art)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-3-cowsay-message-art)
    * [Available characters (50+)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#available-characters-50)
    * [Eye/tongue modifiers](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#eyetongue-modifiers)
  * [Tool 4: Boxes (Decorative Borders)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-4-boxes-decorative-borders)
    * [Combine with pyfiglet or asciified](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#combine-with-pyfiglet-or-asciified)
  * [Tool 5: TOIlet (Colored Text Art)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-5-toilet-colored-text-art)
  * [Tool 6: Image to ASCII Art](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-6-image-to-ascii-art)
    * [Option A: ascii-image-converter (recommended, modern)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#option-a-ascii-image-converter-recommended-modern)
    * [Option B: jp2a (lightweight, JPEG only)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#option-b-jp2a-lightweight-jpeg-only)
  * [Tool 7: Search Pre-Made ASCII Art](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-7-search-pre-made-ascii-art)
    * [Source A: ascii.co.uk (recommended for pre-made art)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#source-a-asciicouk-recommended-for-pre-made-art)
    * [Source B: GitHub Octocat API (fun easter egg)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#source-b-github-octocat-api-fun-easter-egg)
  * [Tool 8: Fun ASCII Utilities (via curl)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-8-fun-ascii-utilities-via-curl)
    * [QR Codes as ASCII Art](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#qr-codes-as-ascii-art)
    * [Weather as ASCII Art](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#weather-as-ascii-art)
  * [Tool 9: LLM-Generated Custom Art (Fallback)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#tool-9-llm-generated-custom-art-fallback)
    * [Character Palette](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#character-palette)
  * [Decision Flow](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/creative/creative-ascii-art#decision-flow)


