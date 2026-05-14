<!-- Source: https://danielmiessler.com/blog/my-ai-predictions-retrospective -->

# Everything I've Said About AI Since 2016: A Retrospective
Looking back at my predictions to see what I got right, wrong, and what's still playing out
January 7, 2026
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #future](https://danielmiessler.com/archives/?tag=future)[ #predictions](https://danielmiessler.com/archives/?tag=predictions)[ #top](https://danielmiessler.com/archives/?tag=top)
 Stormlight-archiving…
I've been thinking and writing about AI for [exactly a decade now](https://danielmiessler.com/blog/the-real-internet-of-things), and last week someone claimed I said two things in 2023 that I don't think I said. (1. That we'd have AGI in 6 months, and 2. that AI was sentient).
To my knowledge, I've never said anything like those things. I didn't just disagree with them back then but still to today.
Anyway, this made me want to prove him wrong, which prodded me to create a list of all the stuff I _have_ said. So I spun up some of my [fancy new AI tooling](https://danielmiessler.com/blog/personal-ai-infrastructure) (another "reason" to do this) and got after it. More on the tooling in the notes if you're into that.
So here's (mostly) everything I've said about AI since 2016, organized chronologically, what I got wrong and right, and what I've learned from reviewing it.
  1. [Late 2022](https://danielmiessler.com/blog/my-ai-predictions-retrospective#late-2022)
  2. [Early 2023](https://danielmiessler.com/blog/my-ai-predictions-retrospective#early-2023)
  3. [Late 2023](https://danielmiessler.com/blog/my-ai-predictions-retrospective#late-2023)
  4. [Predictions Scorecard](https://danielmiessler.com/blog/my-ai-predictions-retrospective#scorecard)
  5. [What I Got Right](https://danielmiessler.com/blog/my-ai-predictions-retrospective#right)
  6. [What I Got Wrong or (Charitably) Too Early?](https://danielmiessler.com/blog/my-ai-predictions-retrospective#wrong)
  7. [What I Learned From The Effort](https://danielmiessler.com/blog/my-ai-predictions-retrospective#lessons)
  8. [I Recommend Trying Something Similar](https://danielmiessler.com/blog/my-ai-predictions-retrospective#try-this-yourself)


# 2016 [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#_2016)
In late 2016 I published a short (somewhat shitty) book called [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things). I _hate_ parts of the writing, just from a tone standpoint, and I really wish I'd said some things differently. But the core predictions (DAs, APIs, AR, etc.) are actually starting to happen!
Here they are.
## Prediction: Universal Daemonization [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-universal-daemonization)
One of the main concepts of the book is the idea that every object in the world would eventually have an API—a "daemon" that presents its state, capabilities, and allows interaction in a standardized way.
> "All objects will have these daemons. Cars, houses, buildings, cities, businesses, etc. People will interact with objects through their daemons, which will be fully functioning interfaces that allow you to push and pull information as well as modify configurations and execute commands."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#universal-daemonization), December 2016
I was describing what we'd now call the API-ification of everything, or more specifically, what MCP (Model Context Protocol) is becoming. At least for services infrastructure.
**Analysis:** This one feels pretty good, but API-ification is still just on certain kinds of digital things. The [MCP ecosystem](https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/) now has 10,000+ servers and 97 million monthly SDK downloads. Every major AI platform adopted it. The "everything gets an API" vision is genuinely happening, but I don't see many park benches or restaurants with APIs yet.
VERDICT: **Core idea happening, but implementation still limited.**
## Prediction: Digital Assistants as Primary Interface [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-digital-assistants-as-primary-interface)
We'd stop interacting with technology directly and instead interact through AI assistants that handle everything on our behalf.
> "Humans interact with DAs, and DAs interact with the world."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#digital-assistants), December 2016
I wrote about how DAs would "work to optimize the life of their principals continuously, without rest, 24/7/365, and in multiple threads."
**Analysis:** This is starting to be talked about now in late 2025 and I'm sure in 2026. I expected it back then. [Anthropic's computer use](https://www.anthropic.com/news/3-5-models-and-computer-use), [OpenAI's Operator](https://openai.com/index/operator-announcement/), and various agent frameworks are all moving in this direction. But we're still in early days. Most people still interact with technology directly. I've been working on building toward this vision ever since it became possible—first with my [Personal AI Maturity Model](https://danielmiessler.com/blog/personal-ai-maturity-model) which maps the path from chatbots to full DAs, and now with the [PAI (Personal AI Infrastructure)](https://github.com/danielmiessler/PAI) project on GitHub. I still think of what I'm building as trying to get to the DA I described in the book.
VERDICT: **Directionally solid, timeline was optimistic.**
## Prediction: DAs Understanding Your Context [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-das-understanding-your-context)
This is one of the ideas I'm most proud of from the book. I wrote that DAs would understand your preferences, mood, and intentions—and use all of that context to construct requests on your behalf.
> "The preferences piece is essential, because the better your DA understands you the better it can represent you when making requests on your behalf. Your DA will be essentially bound to your own personal daemon, and it will have access to the most protected information within it. Most notably, your preferences and experiences, which will both be used to help construct the ideal contextual requests on your behalf."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#digital-assistants), December 2016
And in the AR section, I got even more specific about context:
> "With context, DAs will understand the preferences, mood, and intentions of their principals, and they will use this to decide what should be presented to the user... Your DA knows your preferences, your current context (happy, lonely, angry, sad, etc.) and is parsing all those daemons."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#augmented-reality), December 2016
**Analysis:** This is essentially what we now call "context engineering" or sophisticated prompting. The entire premise of effective AI use in 2025 is giving the AI your preferences, your context, your goals—exactly what I described. System prompts, memory features, personalization—it's all "constructing ideal contextual requests." People are literally re-learning this lesson right now, and I wrote it in 2016.
VERDICT: **Nailed it.**
## Prediction: Services Designed for DAs, Not Humans [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-services-designed-for-das-not-humans)
I wrote that the entire paradigm would flip—businesses would design their services to be consumed by AI assistants, not humans directly.
> "Services (which nearly everything will become) will be designed (and/or retrofitted) to be consumed by Digital Assistants, not by humans."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#digital-assistants), December 2016
And later:
> "The function of the business changes fundamentally in this model. Instead of being in charge of the user's entire experience, businesses become part of an algorithm marketplace used by DAs to satisfy the requests of their principals. The DA is now the centerpiece of the user experience."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#businesses-as-daemons), December 2016
**Analysis:** This is MCP. This is the entire API-first, AI-native design movement. When Anthropic launched MCP and suddenly every business is racing to create AI-consumable interfaces to their services—that's exactly what I described. Businesses becoming "algorithm marketplaces used by DAs." We're watching this prediction unfold in real-time.
VERDICT: **Nailed it.**
## Prediction: The Tireless Advocate [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-the-tireless-advocate)
DAs wouldn't just respond to requests—they'd proactively work for you 24/7, in parallel threads, finding ways to optimize your life.
> "Your DA will work diligently, using all this context, without rest, in multiple concurrent threads, to find everything in the world that could help you in some way."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#tireless-advocate), December 2016
And:
> "While you are doing other things (or nothing) your DA will be scouring the world for ways to optimize your life based on your needs, desires, and goals."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#tireless-advocate), December 2016
**Analysis:** This is emerging now with AI agents. Background agents running tasks, research assistants working in parallel, systems that monitor and act on your behalf. We're in early days, but the architecture I described is exactly what agent frameworks are building toward.
VERDICT: **Solid, implementation underway.**
## Prediction: Business Interaction via DAs [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-business-interaction-via-das)
I wrote out a specific example of how you'd interact with businesses—not through their apps or websites, but through your DA talking to their daemon/API.
> "Sarah will ask Jan [her DA] to see headphones from Sequoia... Jan will contact Sequoia's daemon and retrieve their product list... Sarah navigates Sequoia's content using voice commands and gestures... Sarah finally says, 'This one and this one. Ship to Abdul and Micah.'... The crucial point here is that Sarah spent no time interacting directly with Sequoia's systems. Jan acted as Sarah's advocate in all of these interactions."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#businesses-as-daemons), December 2016
**Analysis:** This is what everyone is building toward with AI shopping assistants, autonomous purchasing agents, and voice-first commerce. The detail of "Jan contacts Sequoia's daemon" is literally MCP server architecture. We're not fully there yet, but this is the direction.
VERDICT: **Strong and happening, but still materializing.**
## Prediction: Augmented Reality Overlays [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-augmented-reality-overlays)
AR would layer contextual information onto the world—showing you ratings on restaurants, relationship compatibility with strangers, danger indicators, and more.
> "As you're talking to people you'll have metadata about them displayed, such as humor scores, attractiveness ratings, favorite foods, favorite reading, and interesting connections to you."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#augmented-reality), December 2016
**Analysis:** Meta's Ray-Bans with AI are here. Apple Vision Pro exists. But the "metadata overlay on everyone you meet" thing? Not happening yet. The tech just isn't there—we need lighter glasses, better batteries, and more seamless integration before this becomes practical for everyday use. The direction is right, but we're still a few hardware generations away.
VERDICT: **Directionally correct, waiting on hardware.**
## Prediction: Reputation as Infrastructure [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-reputation-as-infrastructure)
People would have third-party-validated ratings displayed through their personal daemons—reliability scores, trustworthiness, expertise in various domains.
> "Our daemons will host and present dozens of ratings (and thousands of subratings) about us. These scores will then be used by the world to make decisions about whether to interact with said person."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#reputation-as-infrastructure), December 2016
**Analysis:** We sort of have this with LinkedIn endorsements, Uber ratings, and various reputation systems. But the comprehensive, integrated "social credit" style system I described? Not here, and probably for good reason. This is one where I was describing what's _technically possible_ without fully grappling with whether it's _desirable_.
VERDICT: **Partial implementation, significant pushback on full vision.**
## Prediction: Continuous Authentication [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-continuous-authentication)
We'd move from passwords and periodic authentication to continuous streams of biometric and behavioral data that maintain identity confidence in real-time.
> "People and things will constantly stream data points to the IVS [Identity Validation Service], and those markers will be used to maintain a real-time confidence rating that the person (or thing) is actually itself."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#identity-and-authentication), December 2016
**Analysis:** Behavioral biometrics are real now. Apple's Face ID is always-on. Some enterprise systems do continuous authentication. But the full vision of constant identity streaming? Not there yet.
VERDICT: **Moving in this direction, slower than predicted.**
## Prediction: Businesses Become APIs [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-businesses-become-apis)
Companies would essentially reduce to their core algorithms, with the interface/experience layer being handled by intermediaries.
> "Many businesses will become digital and service-oriented because many businesses can (and will) ultimately be reduced to their algorithms."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#businesses-as-daemons), December 2016
**Analysis:** This is happening with AI companies. [Crunchbase data](https://news.crunchbase.com/startups/funding-zero-to-unicorn-ai-robotics-eoy-2025/) shows companies like Cursor and Lovable are essentially algorithm-as-company. The API economy is massive. But most businesses still have significant non-algorithmic components.
VERDICT: **Solid for tech, less so for broader economy.**
## Prediction: Machine Learning + Evolutionary Algorithms [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-machine-learning-evolutionary-algorithms)
The combination of ML and evolutionary approaches would accelerate our ability to discover solutions humans couldn't conceive.
> "Using this technique we can potentially outperform the creative capabilities of billions of the smartest humans, doing their best on a problem for hundreds of years, all in the span of a few hours."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#getting-better-at-getting-better), December 2016
**Analysis:** AlphaFold, protein folding, drug discovery—yeah, this is happening. The [Stanford 2025 AI Index](https://hai.stanford.edu/ai-index/2025-ai-index-report) documents AI matching or exceeding human expert performance across numerous domains. I'll take credit for the direction, but the specific technical approach (transformers, LLMs) was completely different from what I imagined.
VERDICT: **Got the outcome right, mechanism different than expected.**
## Prediction: Desired Outcome Management (DOM) [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-desired-outcome-management-dom)
This is the one that hasn't fully materialized yet, but it's the vision I care most about. I wrote about a framework for systematically improving human outcomes by defining goals and ratcheting up toward them.
> "DOM provides a model for improving almost anything... Define your goals. Define your model. Capture data. Provide ratings. Recommend changes based on where you could improve. Adjust the approach based on new data."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#desired-outcome-management-dom), December 2016
And the core insight about what this enables:
> "This will culminate in a framework that allows humankind to systematically define its goals, study reality in realtime using AI, and then make optimizations to our behavior that best lead to our desired outcomes."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#conclusion), December 2016
**Analysis:** This is the part of the book I'm still actively building toward. The vision was: define goals, capture data, rate progress, get recommendations, adjust. It's essentially what I'm trying to create with [TELOS](https://github.com/danielmiessler/telos) (personal life optimization) and [Substrate](https://substrate.is) (human progress frameworks). The infrastructure is finally here—AI can now hold your goals, preferences, and metrics in context and help you optimize. But the full "DOM for humanity" vision? Still mostly aspirational. I think about this constantly.
VERDICT: **The destination I'm still building toward.**
## 2016 Examples → What People Are Building Now [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#_2016-examples-%E2%86%92-what-people-are-building-now)
What's wild about re-reading the 2016 book is how many specific examples I wrote are _exactly_ what people are building right now. Not vague directional stuff—actual use cases.
**Shopping via DA conversation:**
> "Sarah will ask Jan to see headphones from Sequoia... Jan will contact Sequoia's daemon and retrieve their product list... Sarah navigates Sequoia's content using voice commands and gestures... Sarah finally says, 'This one and this one. Ship to Abdul and Micah.' ... Jan acted as Sarah's advocate in all of these interactions."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#businesses-as-daemons), December 2016
That's AI shopping agents, [Perplexity Shopping](https://www.perplexity.ai/hub/blog/introducing-perplexity-shopping), and the entire vision behind MCP-powered commerce. The "Jan contacts Sequoia's daemon" line is literally MCP server architecture.
**Real-time research summaries:**
> "Any research topic you express interest in, or ask your DA to look into, will get a full parsing and summary treatment... Summaries will have depth levels, so you'll be able to say things like, 'less depth', or, 'more depth' as desired."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#tireless-advocate), December 2016
That's exactly how [Perplexity](https://www.perplexity.ai) works. It's how Claude's research mode works. It's how everyone is building AI-assisted research—filtering relevance and controlling depth.
**Household management:**
> "Instead of household items like food and dish soap and paper towels ordering replacements for themselves... every household item will register with the head-of-household's DA, and the DA will manage the household based on its knowledge of preferences, calendars, etc."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#digital-assistants), December 2016
[Matter protocol](https://csa-iot.org/all-solutions/matter/), smart fridges, and the whole "connected home" push is heading there. Apple's HomeKit with AI integration is building toward this.
**Gig work matching:**
> "Jason is rated highly in many local and global skills, and he sits relaxing at his favorite coffee shop... When a job passes the threshold, his DA (named Timmothy), will break in quietly in his earpiece. 'Legal contract review, 37 pages, due by tomorrow morning, are we interested?' Jason nods his head and the details are worked out between DAs transparently."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#the-future-of-work), December 2016
That's [Upwork](https://www.upwork.com/), [Fiverr](https://www.fiverr.com/), and all the AI-powered job matching platforms. The [70 million Americans now freelancing](https://blog.theinterviewguys.com/the-state-of-the-gig-economy-in-2025/) are essentially operating through API-like interfaces.
**Safety summoning:**
> "If a woman is walking home, and she realizes it's later than she thought, her DA will summon local protection. People who are rated as safety qualified... will get summoned by their DAs to either accept or reject an urgent, local request. And within a few seconds one or more people will walk up, nod, smile, and walk with her to her destination."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#the-future-of-work), December 2016
That's what [Citizen](https://citizen.com/), [Noonlight](https://www.noonlight.com/), and personal safety apps are doing. Apple's crash detection and fall alerts are moving in this direction.
**Venue personalization:**
> "Walking into a sports bar could see the content on the displays change, the music over the speakers change, etc... When you visit a hotel your DA will have everything configured for you according to the maximum capabilities of the property. This will include bed style, products in the bathroom, what's playing on the display, the temperature in the room, etc. These are not things that you ask for—they're all things that your DA knows best about you."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#continuous-customization), December 2016
[Apple Continuity](https://support.apple.com/en-us/HT204681), cross-device preferences, and the "hand off your context" paradigm are the infrastructure for this. We're not fully there, but the plumbing exists.
**Cross-device context handoff:**
> "As you move from place to place (say hotels or airplanes) your context will transfer with you through your DA. If you're halfway through watching a show on a plane when you land, your DA will ask if you want to pick it up where you left off when you get in bed at the hotel."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#continuous-customization), December 2016
This is [Apple Handoff](https://support.apple.com/en-us/HT209455), Universal Control, and the entire continuity ecosystem. Start something on your phone, finish it on your laptop. Copy on one device, paste on another. We have this now.
**Writing the perfect message:**
> "Write the perfect letter for this situation... I just got this text, how should I respond?"
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#businesses-as-daemons), December 2016
This is ChatGPT. This is Claude. This is every AI writing assistant. "Help me respond to this email" is one of the most common AI use cases in 2025.
**Travel planning via DA:**
> "You ask your DA where to go for a weekend trip, and it calculates all the variables based on the best experience, price, and ratings by people in your network who have gone there. Your DA recommends the winner and then uses a separate daemon/business/API to build the travel plan and add it to the calendar."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#reputation-as-infrastructure), December 2016
That's [Perplexity for travel](https://www.perplexity.ai), ChatGPT trip planning, and all the AI travel agents emerging now. "Plan me a weekend in Portland" with AI doing the work.
**Content recommendations:**
> "What should I watch right now? What should I listen to? Surprise me with an interesting music choice that I'll love but never would have picked myself."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#businesses-as-daemons), December 2016
Netflix, Spotify, and every recommendation algorithm—but now with AI that actually understands context and mood. "I just had a hard day, what should I watch?" is a ChatGPT query.
**Book summaries on demand:**
> "When I look at the cover of a book, give me a perfect summary that fills the cover, along with the rating."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#businesses-as-daemons), December 2016
[Blinkist](https://www.blinkist.com/), AI book summarizers, and "summarize this PDF" as a core AI use case. Point your camera at a book and get a summary—we're there.
**Life optimization questions:**
> "Why am I not happy? What do I waste the most time on in my life? Build me a perfect daily routine based on my life goals."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#businesses-as-daemons), December 2016
AI life coaches, [Rosebud](https://www.rosebud.app/) for journaling, and the entire "AI therapist" category. People ask these exact questions to Claude and ChatGPT daily.
**Menu filtering by health goals:**
> "Only show me menu items that I should eat as part of my new health plan. I'm new to Sushi, what should I try on this menu?"
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#businesses-as-daemons), December 2016
[Noom](https://www.noom.com/), AI nutrition apps, and "photograph your menu and get recommendations" features. ChatGPT can already analyze a menu photo and recommend based on your dietary needs.
**Dating and matching:**
> "You'll hear a sound when a single person of the opposite sex nears you while you're not working, but only if they pass a few filters that are important to you. You might let your DA use a number of commercial algorithms to find matches for you that you wouldn't have thought to explore yourself. So you may put yourself in Cupid mode, or Spontaneity mode, where two DAs create pre-filtered but semi-chance meetings between two principals."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#digital-assistants), December 2016
That's [Tinder](https://tinder.com/), [Hinge](https://hinge.co/), and the entire AI dating scene. The "pre-filtered but semi-chance meetings" is exactly what matching algorithms do.
**Proactive hobby planning:**
> "If someone mentions to you casually about a particular sport, your DA (knowing you like to immerse yourself in new hobbies) will find the nearest training locations, the best local trainers, the best and nearest places to play, and some top tips for getting into shape. So when you inevitably ask about it in the next day or so, your DA will have an entire plan sorted out for you."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#tireless-advocate), December 2016
This is proactive AI assistance. Google does this poorly with ads. What I described is where AI assistants are heading—anticipating needs before you express them.
**Family safety monitoring:**
> "You'll be notified by your DA if anyone in your family is in a dangerous situation that falls above a certain threshold. You'll be able to switch your visual point of view instantly to any camera you have access to, whether that's inside your house, through the eyes of someone you're sharing access with, drones hovering over your house, etc."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#omniscient-defender), December 2016
[Life360](https://www.life360.com/), [Ring cameras](https://ring.com/), family tracking apps. The "switch your visual point of view to any camera" is exactly what Ring and Nest dashboards do.
**Reputation monitoring:**
> "DAs will scour the world looking for negative information about you, news that could negatively affect you, etc., and will bring it to your attention if it finds something."
> — [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things#tireless-advocate), December 2016
[Google Alerts](https://www.google.com/alerts), brand monitoring tools, social listening platforms. AI-powered reputation monitoring is now a category.
The point isn't that I'm some prophet. The point is that **human needs are predictable**. I didn't predict the technology; I predicted what people would want to do with technology that understood them. Those use cases don't change—only the implementation does.
# 2020 [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#_2020)
## Prediction: AI-Powered Content Discovery (Amazon Curate) [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-ai-powered-content-discovery-amazon-curate)
In November 2020, I wrote a fake product announcement for a service I called "Amazon Curate"—describing exactly the system Elon Musk announced for X/Grok in January 2026.
> "Amazon Curate combines content discovery with personalization... **Survey** : A high-speed crawling platform optimized for discovering niche content across the internet. **Surface** : A customization engine using machine learning to analyze content features and match them with user interests."
> — [Introducing Amazon Curate (I Wish)](https://danielmiessler.com/blog/introducing-amazon-curate-i-wish), November 2020
The core insight was that "great contentness" could be assessed algorithmically:
> "They either create great content or they don't."
> — [Introducing Amazon Curate (I Wish)](https://danielmiessler.com/blog/introducing-amazon-curate-i-wish), November 2020
I also wrote about this in [Machine Learning Will Revolutionize Content Discovery](https://danielmiessler.com/blog/machine-learning-will-revolutionize-content-discovery), where I argued that "99% of the best content is never discovered" and that ML would finally fix the small creator visibility problem—surfacing gems that would otherwise remain invisible.
**Analysis:** In January 2026, Elon Musk announced that Grok would do exactly this:
  * Grok reads every post on X (100M+ daily) — my "Survey" system
  * Matches content to 300-400M users based on what they'll enjoy — my "Surface" system
  * Filters spam and scam automatically — algorithmic quality assessment
  * Fixes the small/new account problem — the exact creator visibility issue I identified
  * Users can ask Grok to adjust their feed — personalization I described


The framing I used in 2020—"the best content will rise to the top"—is essentially what Musk described. I wrote a fake AWS product announcement, and six years later it became X's algorithm.
VERDICT: **Nailed it—Grok implements the exact system I described.**
# Late 2022 [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#late-2022)
This is when ChatGPT hit and everything went crazy. I wrote a "napkin ideas" post with my first reactions. Looking back at it now is... interesting.
## Prediction: Massive Knowledge Work Replacement [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-massive-knowledge-work-replacement)
80% of knowledge work would eventually be affected by AI automation.
> "Let me start with the punchline: Something like 80% of most 'knowledge work' is about to get replaced by artificial intelligence."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** Was I being dramatic? Maybe. But the direction is right. [McKinsey's 2025 report](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work) says 75% of knowledge workers already use AI tools, and 30% of current hours worked could be automated by 2030. [DemandSage data](https://www.demandsage.com/ai-job-replacement-stats/) shows creative execution roles already declining hard: graphic artists (-33%), photographers (-28%), writers (-28%). The 80% number might still be high, but it's not crazy anymore.
VERDICT: **Directionally solid, magnitude TBD.**
## Prediction: Non-Replacement vs. Massive Layoffs [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-non-replacement-vs-massive-layoffs)
The transition would be gradual attrition rather than sudden mass layoffs.
> "I don't imagine this will result in some massive layoff. It'll be more like a steady trend towards non-replacement as people naturally leave companies."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** This seems to be playing out. We're not seeing "50% of accountants fired Tuesday" headlines. Instead we're seeing companies quietly not backfilling positions, reducing hiring, letting AI handle work that used to require new hires. The [NPR "first-rung squeeze" report](https://www.npr.org/2025/08/05/nx-s1-5485286/ai-jobs-economy-wealth-gap) confirms entry-level positions are disappearing first.
VERDICT: **Solid so far.**
## Prediction: Talent Gap Explosion [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-talent-gap-explosion)
AI would massively amplify the gap between talented and less talented people.
> "AI will be like multiplying their brains and having them work continuously. The best engineers become better engineers. The best entrepreneurs move faster to market."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** Evidence is mixed. [PwC's 2025 data](https://siai.org/research/2025/10/202510280934) shows AI-skilled positions command a 56% wage premium. But [Harvard research](https://www.hbs.edu/faculty/Pages/item.aspx?num=64700) found AI helps the _bottom_ 50% of performers achieve the greatest productivity uplift. So within specific tasks, AI might be narrowing gaps. But between AI-adopters and non-adopters? That gap is widening fast.
VERDICT: **Partially right—gap expanding between adopters and non-adopters.**
## Prediction: Solopreneurs Thrive [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-solopreneurs-thrive)
Small teams with AI would compete with much larger companies.
> "It's getting a whole lot easier to be a business by yourself, or with 1-5 employees. If you pick your first couple of employees well, it could easily be the equivalent of having 10-20 people."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** Nailed this one. [Sam Altman predicts](https://techcrunch.com/2025/02/01/ai-agents-could-birth-the-first-one-person-unicorn-but-at-what-societal-cost/) the first one-person billion-dollar company is coming soon. Lovable became Europe's fastest unicorn in 8 months with 45 employees. Cursor hit $500M ARR with fewer than 50 workers. Gumloop raised $17M Series A with just 2 full-time staff. Solo-led exits now account for 52.3% of successes, up from 22.2% in 2015.
VERDICT: **Solid.**
## Prediction: Best AI Will Be Most Expensive [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-best-ai-will-be-most-expensive)
Premium AI would go to those who could afford it, amplifying inequality.
> "This will magnify even further because the best AI will be the most expensive."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** This has held up. Open source models have improved, but the gap between paid and free remains significant for serious work. Claude Code is dramatically better than open source alternatives for real development tasks. The people paying for premium AI are getting meaningfully better results.
VERDICT: **Mostly right.**
## Prediction: Dynamic Generalist Employees [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-dynamic-generalist-employees)
The employees people hire would be generalists who are good with data and AI frameworks.
> "The employees people do hire will be dynamic generalists who are also good with data and—you guessed it—using AI frameworks."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** This is happening. The most valuable hire now is often someone who can stitch together AI tools, not a deep specialist.
VERDICT: **Called it.**
## Prediction: Ideas Ascend, Implementation Becomes Less Important [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-ideas-ascend-implementation-becomes-less-important)
Focus would shift from "how do we do the thing" to "what should we be doing."
> "With AIs answering more and more of that question, the focus will shift to the new question of, 'What should we be doing?'. That's a colossal shift, and it's one that favors a different type of employee."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** Very early days, but directionally this seems right. Prompting/directing is becoming more valuable than pure execution in many domains.
VERDICT: **Tracking—too early to call.**
## Prediction: Liberal Arts Renaissance [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-liberal-arts-renaissance)
Broader education might help people become leaders rather than just executors.
> "Maybe that generalist, liberal-arts education won't be as much of a waste anymore."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** I was trying to find a silver lining here. The reality is more complicated—we're seeing value in both technical _and_ humanistic skills, but "liberal arts degree = success in AI era" is too simple.
VERDICT: **Overstated.**
## Prediction: IP Battles Over AI-Generated Ideas [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-ip-battles-over-ai-generated-ideas)
Fierce competition around what constitutes a human idea vs. AI-generated.
> "Expect fierce IP battles around what constitutes a human idea vs. one generated by an AI."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** Getty vs. Stability AI, NYT vs. OpenAI, countless copyright cases. The legal battles are here.
VERDICT: **Solid.**
## Prediction: Multimodal Excitement [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-multimodal-excitement)
Images and video combined with text would be transformative.
> "As exciting as this first version is, I'm 37x more excited about future versions—especially once they do images and video as well as text."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** Midjourney, DALL-E, Sora, GPT-4V—yeah. Multimodal is huge. This was an easy call in retrospect.
VERDICT: **Nailed it.**
## Prediction: SOC Analyst AI Assistance [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-soc-analyst-ai-assistance)
AI would finally deliver on the broken promise of helping security analysts.
> "The idea of helping a SOC analyst with AI was an empty promise and sad joke for a long time, and that seems about to end."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** This is happening. AI-powered security tools are actually useful now—not magic, but genuinely helpful. The "sad joke" phase is over.
VERDICT: **Spot on.**
## Prediction: Hollywood in Trouble [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-hollywood-in-trouble)
AI creativity + animation would disrupt traditional content creation.
> "Hollywood seems to be in significant trouble. Once we can combine this type of creativity with the ability to make animation and video, why would we wait multiple years and pay millions for mediocre stories?"
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** Hollywood is struggling, but more from streaming fragmentation than AI disruption (so far). The AI video tools aren't quite there yet for feature-length content. This one's still playing out.
VERDICT: **In progress—disruption coming but slower than expected.**
## Prediction: AI as Inspiration Muse [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-ai-as-inspiration-muse)
AI would function as a source of creative inspiration rather than replacement.
> "Some part of [art] gets completely destroyed, but many elements of it get better because this tech will function as an inspiration muse."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** This is how most creative professionals I know use AI—brainstorming, ideation, getting unstuck. The [Science Advances study](https://www.science.org/doi/10.1126/sciadv.adn5290) confirms writers with AI access score higher for novelty and usefulness.
VERDICT: **Solid.**
## Prediction: A/B Testing Boon [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-a-b-testing-boon)
AI would enable rapid idea generation for testing.
> "This is going to be a massive boon for A/B testing scenarios. You can have AI generate a number of ideas and send them into a testing environment where they can be tested against reality."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** Yeah, this is standard practice now in marketing, product design, ad copy.
VERDICT: **Called it.**
## Prediction: Yoda vs. Einstein Framework [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-yoda-vs-einstein-framework)
LLMs have wisdom, not mathematical precision. Don't ask Yoda to do your taxes.
> "Imagine this thing like Yoda rather than Einstein. Einstein does math. Yoda has wisdom. Don't ask Yoda or GPT to do your taxes; they'll disappoint you."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** This framework has held up remarkably well. [Nature's 2025 research](https://www.nature.com/articles/s41598-025-93794-9) confirms AI "can make only incremental discoveries but cannot achieve fundamental discoveries from scratch as humans can." LLMs are pattern recognizers with deep recall, not original thinkers.
VERDICT: **Solid—still use this framing constantly.**
## Prediction: Analytical Optimism [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-analytical-optimism)
The transition would be traumatic but ultimately positive.
> "It's going to be traumatic, and it's going to be wonderful."
> — [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt), December 2022
**Analysis:** [Stanford's 2025 AI Index](https://hai.stanford.edu/ai-index/2025-ai-index-report) shows optimism growing in previously skeptical countries. The "analytical optimism" framing has become pretty standard in enterprise AI discussions.
VERDICT: **Solid as a framework.**
# Early 2023 [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#early-2023)
## Prediction: GPTs Genuinely Understand [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-gpts-genuinely-understand)
LLMs actually understand things—they don't just pattern match.
> "The ability to apply knowledge in new situations and contexts."
> — [Yes, GPTs Actually Understand](https://danielmiessler.com/blog/yes-gpts-llms-understand-argument), March 2023
I used a complex prompt—asking GPT to write a Faustian hero's journey with a Socratic sister, Machiavellian mother, shibboleth plot point, magical scarf, 3-legged dog, dystopian setting, and Ted Lasso ending. It nailed it.
**Analysis:** The philosophical debate continues, but practically speaking, LLMs do something that functions like understanding. [Research from 2025](https://aiche.onlinelibrary.wiley.com/doi/10.1002/aic.18661) confirms they develop a "geometry-like" understanding adequate for many applications. They have limits—they lose track of chess positions after a few moves—but "mere pattern matching" doesn't capture what they do.
VERDICT: **Functional understanding confirmed, philosophical debate ongoing.**
## Prediction: Substrate Doesn't Matter [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-substrate-doesn-t-matter)
Dismissing AI understanding because it's silicon instead of neurons is flawed.
**Analysis:** The AI field now operates as if substrate doesn't matter. [OpenAI's o1 achieved 83.3%](https://arxiv.org/html/2503.05788v2) on competition math vs GPT-4o's 13.4%—reasoning capabilities emerging regardless of substrate. The consciousness question is philosophically interesting but practically irrelevant.
VERDICT: **The field has moved on from this objection.**
## Prediction: SPQA Architecture [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-spqa-architecture)
AI would transform software from circuit-based to understanding-based systems.
> "Companies displaying their wares through websites and legacy software will be replaced by custom GPT models that ingest everything that makes up that business."
> — [SPQA: The AI-based Architecture](https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software), March 2023
STATE, POLICY, QUESTIONS, ACTION—I predicted most legacy software would be replaced by LLM-based systems with this structure.
**Analysis:** System prompts with structured formats have become industry standard. [OpenAI's best practices](https://platform.openai.com/docs/guides/prompt-engineering) recommend exactly this kind of structured approach.
VERDICT: **Directionally correct, but we've yet to see large-scale enterprise rollout.**
## Prediction: People Become APIs [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-people-become-apis)
Individuals would create AI models of themselves for interaction.
> "Just as businesses have logs and docs, we'll upload all our journals, photos, social media, preferences, and everything else."
> — [SPQA Architecture Post](https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software), March 2023
**Analysis:** The gig economy has restructured around API-like interfaces. [70 million Americans (36% of workforce)](https://blog.theinterviewguys.com/the-state-of-the-gig-economy-in-2025/) now freelance through platforms that essentially treat humans as callable services. But personal AI models for self-exploration? Not mainstream yet.
VERDICT: **Structural shift happening; personal model aspect still emerging.**
## Prediction: The Creativity Explosion [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-the-creativity-explosion)
AI would democratize creative output on a massive scale.
> "We're about to multiply the creative output of planet Earth by hundreds of orders of magnitude."
> — [6 Phases of the Post-GPT World](https://danielmiessler.com/blog/6-phases-post-gpt-world), March 2023
**Analysis:** This is absolutely happening. The last month of 2025 went nuts—Claude Code enabled people to build and ship things that would have taken teams months to create. Solo developers launching full products in days. Non-programmers building functional apps. The creative output explosion isn't theoretical anymore; it's all over social media every day.
VERDICT: **Nailed it—this is happening right now.**
## Prediction: Inverse Order of AI Replacement [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-inverse-order-of-ai-replacement)
I initially thought blue-collar jobs would go first, but realized artists would be hit first instead.
This was actually a prediction I got wrong initially and then corrected. Worth noting.
**Analysis:** Artists, writers, designers—the creative class got hit first. [DemandSage data](https://www.demandsage.com/ai-job-replacement-stats/) shows graphic artists (-33%), photographers (-28%), writers (-28%). Physical labor jobs remain harder to automate.
VERDICT: **Correction landed.**
# Late 2023 [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#late-2023)
## Prediction: Agents and Multi-modal Are Key [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-agents-and-multi-modal-are-key)
These two capabilities would be the most transformative areas of AI development.
> "These days I get most AI-excited about **Agents** and **Multi-modal** , which is where AI can do its karate on more than just text."
> — Newsletter, October 2023
**Analysis:** Every major AI lab is now building computer-use agents with visual understanding. [Claude's computer use](https://www.anthropic.com/news/3-5-models-and-computer-use) allows Claude to see screens, click buttons, type. [GPT-4o](https://skywork.ai/blog/agent/openai-realtime-gpt-4o-vision-build-multimodal-voice-agents-2025/) integrates real-time audio, vision, and reasoning. This is exactly where AI development concentrated.
VERDICT: **Solid.**
## Prediction: AGI by 2025-2028 [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-agi-by-2025-2028)
60% chance by 2025, 90% by 2028—through systems, not single models.
> "An AI system capable of replacing a knowledge worker making the average salary in the United States."
> — [Why We'll Have AGI by 2025-2028](https://danielmiessler.com/blog/why-well-have-agi-by-2028), November 2023
**Analysis:** This remains highly contested. [Sam Altman](https://blog.samaltman.com/reflections) (Jan 2025) said they "know how to build AGI." [Andrej Karpathy](https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/) says AGI is "around a decade away." The definition problem is real. I'll be honest—this is one where I was confident and the jury is very much still out.
VERDICT: **Within the window; heavily definition-dependent.**
## Prediction: Prompt Injection Endemic [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-prompt-injection-endemic)
Agent-based systems would create massive new attack surfaces.
> "The amount of prompt injection we're about to see propagate across the Internet is going to be staggering."
> — [OpenAI's November 23' Releases](https://danielmiessler.com/blog/ai-agents-api-calling-prompt-injection), November 2023
**Analysis:** Prompt injection is now [OWASP's #1 LLM vulnerability for 2025](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). [OpenAI stated](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/) in December 2025: "Prompt injection is unlikely to ever be fully 'solved.'" [24 CVEs were assigned](https://gbhackers.com/ai-developer-tools/) for AI tool vulnerabilities in December 2025 alone.
VERDICT: **Called it—endemic status confirmed.**
## Prediction: The 7 Components of AI's Future [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-the-7-components-of-ai-s-future)
A comprehensive framework: Digital Assistants, Everything Gets an API, DA Mediation, Active Protection, Module Ecosystem, AR Interfaces, Multiple Specialized DAs.
> "Tech isn't predictable. But _humans_ are."
> — [AI's Predictable Path](https://danielmiessler.com/blog/ai-predictable-path-7-components-2024), December 2023
**Analysis:** The framework seems solid, but honestly this is a bit too nebulous to give myself a thumbs up on. The categories feel right, but it's hard to point to concrete evidence that says "yes, this specific framework was correct."
VERDICT: **Too vague to score definitively.**
## Prediction: DA Hacks Will Be Catastrophic [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-da-hacks-will-be-catastrophic)
Compromising someone's Digital Assistant would be devastating.
> "Hacking someone's Digital Assistant will be like compromising their soul. Not their accounts. Not their tech. Their soul."
> — [AI's Predictable Path](https://danielmiessler.com/blog/ai-predictable-path-7-components-2024), December 2023
**Analysis:** This is happening. [Microsoft Copilot's "EchoLeak" vulnerability](https://fortune.com/2025/06/11/microsoft-copilot-vulnerability-ai-agents-echoleak-hacking/) was the first documented zero-click attack on an AI agent. [GitHub Copilot RCE](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/) enabled an "AI virus" that propagates as developers interact with infected files. [Anthropic disclosed](https://www.anthropic.com/news/disrupting-AI-espionage) a Chinese state-sponsored group used Claude Code to attempt infiltration of 30+ global targets.
VERDICT: **Nailed this one—catastrophic DA hacks are now documented.**
# 2024 [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#_2024)
## Prediction: Prompting is Primary [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-prompting-is-primary)
The quality of prompts matters more than model choice, RAG, or fine-tuning.
> "90% of AI's power is in prompting—NOT RAG, NOT fine-tuning, NOT even the models themselves."
> — [AI is Mostly Prompting](https://danielmiessler.com/blog/ai-is-mostly-prompting), May 2024
**Analysis:** I'll take a victory lap on this one. People spent 2024 chasing RAG and fine-tuning, and now in late 2025 everyone's re-discovering that prompting (now called "context engineering") is where the leverage actually is. [IBM's 2025 guide](https://www.ibm.com/think/prompt-engineering) states: "Prompt engineering is the new coding." I said this in May 2024 and got pushback. Now it's consensus.
VERDICT: **Called it—and people are finally catching up.**
## Prediction: Slack in the Rope [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-slack-in-the-rope)
There's massive untapped potential in AI capabilities—not from bigger models or more compute, but from tricks, techniques, and optimizations we haven't discovered yet. I called this "slack in the rope."
> "I've been shouting from the rooftops for nearly two years that there is likely _massive slack in the rope_ , and that the stagnation we saw in 2023 and 2024 around model size will get massively leaped over by these tricks."
> — [The 4 Components of Top AI Model Ecosystems](https://danielmiessler.com/blog/ai-model-ecosystem-4-components), August 2024
I was specific about what this meant:
> "I think of it as a set of highly proprietary tricks that magnify the overall quality of the raw model... Post-training is perhaps the most powerful category of those tricks. It's like teaching a giant alien brain _how to be smart_ , when it had tremendous potential before but no direction."
> — [The 4 Components of Top AI Model Ecosystems](https://danielmiessler.com/blog/ai-model-ecosystem-4-components), August 2024
And by September 2025, I was able to point to specific examples:
> "For example, 'chain of thought' reasoning. Having an AI talk through the various steps of a process and sort of self-observe turned out to have extraordinary gains. And there are many other such gains that had to do with simply reorganizing how data was taken in or the order in which data was taken in."
> — [Our Constraints on Creativity](https://danielmiessler.com/blog/our-constraints-on-creativity), September 2025
The core insight: most people assumed AI progress would come primarily from scaling—bigger models, more GPUs, more energy. I argued that tricks like post-training, chain-of-thought, better prompting, and architectural innovations would deliver outsized returns compared to raw compute scaling.
**Analysis:** This one has proven extremely accurate. Chain-of-thought reasoning, RLHF, DPO, constitutional AI, prompt caching, structured outputs, tool use—the list of "tricks" that delivered massive capability gains keeps growing. [Anthropic's research](https://www.anthropic.com/research) shows their constitutional AI approach dramatically improved model behavior without scaling. OpenAI's o1 and o3 models achieved reasoning breakthroughs through inference-time compute tricks, not just model scaling. The entire "post-training" category I identified has become the primary battleground for model differentiation. Much of the 2024-2025 progress came from exactly what I predicted: clever tricks, not just more parameters.
VERDICT: **Nailed it—the slack in the rope thesis was vindicated.**
## Prediction: 2025 = Year of Agents [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-2025-year-of-agents)
Agent frameworks would mature enough for real-world use.
> "I'm anticipating that in 2025 the biggest thing in AI will be **the maturation of Agents.** "
> — Newsletter, November 2024
**Analysis:** Claude Code is an agent. It reads files, writes code, runs commands, debugs errors, and iterates autonomously. That's what agents are. The prediction wasn't about enterprise adoption metrics—it was about agents maturing enough to be genuinely useful, and that absolutely happened in 2025. Claude Code changed how people build software.
VERDICT: **Solid—Claude Code is the proof.**
## Prediction: Ecosystem Over Models [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-ecosystem-over-models)
Tooling and ecosystems would matter more than model improvements.
> "The models will get smarter, but I think most of the benefit will be in **the tooling and ecosystems** around the models."
> — Newsletter, November 2024
**Analysis:** MCP became industry standard within one year. [10,000+ servers, 97 million monthly SDK downloads](https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/). GitHub, VS Code, Cursor integrated natively. [Anthropic donated MCP](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) to the Agentic AI Foundation.
VERDICT: **Nailed it—ecosystem thesis completely validated.**
# 2025 [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#_2025)
## Prediction: Apple's AI Turnaround [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-apple-s-ai-turnaround)
Apple would go from worst to best AI implementation through ecosystem integration.
> "Apple's about to go from having the worst AI implementation to having the best."
> — Newsletter, January 2025
**Analysis:** This is a major timeline miss. I expected this to happen quickly—within months. A year later, it still hasn't. Apple Intelligence adoption has been [underwhelming](https://tidbits.com/2025/06/20/do-you-use-it-apple-intelligence-sees-weak-adoption/). The Siri overhaul keeps getting pushed back. I still think Apple will eventually get this right—the ecosystem advantage is real—but my timing was way off.
VERDICT: **Timeline miss—may still happen, but I was early by 1-2 years.**
## Prediction: Calibrated Disruption Timeline [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-calibrated-disruption-timeline)
Job displacement would be gradual, not sudden. 2025 sees adoption; 2026-2027 brings restructuring; 2028+ dramatic transformation.
> "We're not going to suddenly in 2026 have 10 or 20% unemployment."
> — Newsletter, May 2025
**Analysis:** Timeline appears mostly accurate with one exception: creative work disruption is ahead of schedule. Already seeing 28-33% declines in graphic artists, photographers, writers in 2025.
VERDICT: **Mostly right—creative work faster than expected.**
## Prediction: Claude Code as Proto-AGI [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-claude-code-as-proto-agi)
Claude Code represented a ChatGPT-level leap for development.
> "I think, looking back, we might say that the first week of July 2025 was the start of AGI. Like, proto-AGI."
> — Newsletter, July 2025
**Analysis:** I don't even remember writing this in July, but holy crap has it proven true. Claude Code does 30+ hours of autonomous coding. It reads, writes, debugs, iterates, and ships. [Anthropic scaled from 0 to $400M ARR](https://www.cbinsights.com/research/report/coding-ai-market-share-2025/) in 5 months. The "proto-AGI" framing felt bold at the time—now it feels obvious.
VERDICT: **Nailed it—this aged extremely well.**
## Prediction: VCs in Trouble [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-vcs-in-trouble)
The venture capital model would face disruption as solo developers reduce capital requirements.
> "VCs, as a species, are in serious trouble right now."
> — Newsletter, September 2025
**Analysis:** [Axios reports](https://www.axios.com/2025/10/14/venture-capital-ai-founders) VC faces disruption—"Capital intensive businesses don't exist anymore." Founders collecting enough in one round to achieve profitability. But also: [Bloomberg reports](https://www.bloomberg.com/news/articles/2025-10-03/ai-is-dominating-2025-vc-investing-pulling-in-192-7-billion) $192.7B poured into AI startups, with AI capturing 52.5% of all VC dollars.
VERDICT: **Structural disruption real, but elite AI VCs thriving—nuanced.**
## Prediction: Tools, Operators, and Outcomes Framework [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-tools-operators-and-outcomes-framework)
A framework for understanding why AI disruption is significant—AI combines all three.
> "When companies pay ICs to do tasks they're actually paying for three different things: One or more tools, an operator, and an outcome."
> — Newsletter, October 2025
**Analysis:** [McKinsey's "Agentic Organization"](https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era) describes exactly this hierarchy. [Deloitte notes](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html): "Agentic AI is about delegating outcomes, not just prompts."
VERDICT: **Framework maps to industry analysis.**
## Prediction: Prompt Injection IS a Vulnerability [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-prompt-injection-is-a-vulnerability)
It should be classified as a vulnerability, not just a limitation.
> "A vulnerability where an AI system or component is unable to distinguish between instructions and data."
> — [Is Prompt Injection a Vulnerability?](https://danielmiessler.com/blog/is-prompt-injection-a-vulnerability), November 2025
**Analysis:** The industry shifted. Prompt injection now receives CVE assignments. [24 CVEs](https://gbhackers.com/ai-developer-tools/) in December 2025 alone. [Microsoft formally documents](https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks) their defenses. Debate settled.
VERDICT: **Called it—now a formal vulnerability class.**
## Prediction: Anthropic's Apple Moment [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-anthropic-s-apple-moment)
Anthropic's ecosystem advantage mirrors Apple's iPhone dominance.
> "Anthropic right now feels like Apple in the 2010s with the iPhone."
> — Newsletter, December 2025
**Analysis:** The Apple comparison became literally true. [Bloomberg reported](https://www.bloomberg.com/news/articles/2025-05-02/apple-anthropic-team-up-to-build-ai-powered-vibe-coding-platform) Apple partnered with Anthropic on a coding platform. [Anthropic captured 32% enterprise market share](https://www.technology.org/2025/08/02/anthropic-claude-models-capture-32-enterprise-market-share-overtaking-openai-in-business-ai-adoption/) (vs OpenAI's 25%).
VERDICT: **Nailed this one—partnership validated the ecosystem thesis.**
# 2026 [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#_2026)
## Prediction: AI Zombie Apps [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#prediction-ai-zombie-apps)
Abandoned AI projects would create security and financial problems.
> "Significant technical debt from abandoned AI projects—security problems from misconfigurations, keys, API tokens."
> — [AI Changes I Expect in 2026](https://danielmiessler.com/blog/ai-changes-2026), January 2026
**Analysis:** Margin compression is crushing wrapper startups. [DeepSeek R1 operates](https://www.creolestudios.com/top-ai-reasoning-model-cost-comparison/) at ~5% of OpenAI o1's costs. [TechCrunch reports](https://techcrunch.com/2025/08/07/the-high-costs-and-thin-margins-threatening-ai-coding-startups/) Cursor may be running negative margins. 60-70% of AI wrappers generate zero revenue.
VERDICT: **Tracking—prediction made recently, evidence accumulating.**
# Predictions Scorecard (as of January 2026) [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#predictions-scorecard-as-of-january-2026)
Here's how it all shook out.  
| Status  | Count  | Description  |  
| --- | --- | --- |  
| **NAILED IT**  | 17  | Called it. This happened.  |  
| **TRACKING**  | 16  | On track, watching it unfold  |  
| **IN PROGRESS**  | 2  | Jury's still out  |  
| **PARTIAL**  | 2  | Got part of it right  |  
| **FRAMING**  | 2  | Useful way to think about things  |  
| **OPINION**  | 2  | More of a take than a prediction  |  
| **BUILDING**  | 1  | Working to make this happen  |  
| **NUANCED**  | 1  | Turns out it's complicated  |  
| **OVERSTATED**  | 1  | Swung too hard  |  
| **TIMELINE MISS**  | 1  | Right idea, impatient on timing  |  
And here's every prediction broken down.  
| Prediction  | Made  | Status  | Honest Assessment  |  
| --- | --- | --- | --- |  
| Universal Daemonization/APIs  | 2016  | **NAILED IT**  | Core idea right, implementation different  |  
| Digital Assistants as interface  | 2016  | **TRACKING**  | Happening, slower than expected  |  
| DAs Understanding Context  | 2016  | **NAILED IT**  | "Context engineering" before it existed  |  
| Services Designed for DAs  | 2016  | **TRACKING**  | MCP is building toward this  |  
| Tireless Advocate  | 2016  | **TRACKING**  | Agent frameworks implementing this  |  
| Business Interaction via DAs  | 2016  | **TRACKING**  | Still materializing  |  
| AR Overlays  | 2016  | **TRACKING**  | Directionally correct, hardware pending  |  
| Reputation as Infrastructure  | 2016  | **PARTIAL**  | Exists in fragments, pushback on vision  |  
| Continuous Authentication  | 2016  | **TRACKING**  | Moving in this direction  |  
| Businesses Become APIs  | 2016  | **NAILED IT**  | True for tech, less for broader economy  |  
| ML + Evolutionary Algorithms  | 2016  | **NAILED IT**  | AlphaFold proves it  |  
| Desired Outcome Management  | 2016  | **BUILDING**  | Still working toward this vision  |  
| AI Content Discovery (Amazon Curate)  | Nov 2020  | **NAILED IT**  | X/Grok implements exact system I described  |  
| Knowledge work replacement  | Dec 2022  | **NAILED IT**  | 75% using AI, 30% hours automatable  |  
| Non-replacement vs. layoffs  | Dec 2022  | **NAILED IT**  | Gradual attrition playing out  |  
| Talent gap expanding  | Dec 2022  | **PARTIAL**  | Gap is adopters vs non-adopters  |  
| Solopreneurs thrive  | Dec 2022  | **TRACKING**  | One-person unicorn imminent but not yet  |  
| Best AI = most expensive  | Dec 2022  | **NAILED IT**  | Premium AI still meaningfully better  |  
| Dynamic generalist employees  | Dec 2022  | **TRACKING**  | Trending this direction  |  
| Ideas over implementation  | Dec 2022  | **TRACKING**  | Early days but directional  |  
| Liberal arts renaissance  | Dec 2022  | **OVERSTATED**  | Reality more nuanced  |  
| IP battles  | Dec 2022  | **NAILED IT**  | Getty, NYT, countless cases  |  
| Multimodal excitement  | Dec 2022  | **NAILED IT**  | Easy call in retrospect  |  
| SOC analyst AI  | Dec 2022  | **NAILED IT**  | Actually useful now  |  
| Hollywood trouble  | Dec 2022  | **IN PROGRESS**  | Disruption slower than expected  |  
| AI as muse  | Dec 2022  | **NAILED IT**  | How most creatives use it  |  
| A/B testing boon  | Dec 2022  | **NAILED IT**  | Standard practice now  |  
| Yoda vs Einstein  | Dec 2022  | **FRAMING**  | Useful mental model, not verifiable  |  
| GPTs understand  | Mar 2023  | **TRACKING**  | Functional understanding, debate ongoing  |  
| SPQA architecture  | Mar 2023  | **TRACKING**  | Directionally correct, enterprise rollout pending  |  
| Creativity explosion  | Mar 2023  | **TRACKING**  | Claude Code explosion suggests it  |  
| Agents + Multimodal key  | Oct 2023  | **NAILED IT**  | Central to AI development  |  
| AGI by 2025-2028  | Nov 2023  | **IN PROGRESS**  | Within window, definition-dependent  |  
| Prompt injection endemic  | Nov 2023  | **NAILED IT**  | OWASP #1, CVEs assigned  |  
| DA hacks catastrophic  | Dec 2023  | **TRACKING**  | Attacks documented, catastrophe pending  |  
| Prompting is primary  | May 2024  | **NAILED IT**  | Said it early, people finally catching up  |  
| Slack in the rope  | Aug 2024  | **TRACKING**  | Strong evidence, thesis holding  |  
| 2025 = Year of Agents  | Nov 2024  | **NAILED IT**  | Claude Code is the proof  |  
| Ecosystem > models  | Nov 2024  | **TRACKING**  | MCP strong evidence  |  
| Apple turnaround  | Jan 2025  | **TIMELINE MISS**  | Still waiting, 1-2 years off  |  
| Claude Code proto-AGI  | Jul 2025  | **OPINION**  | Characterization, not verifiable  |  
| VCs disrupted  | Sep 2025  | **NUANCED**  | Structural change real, AI VCs thriving  |  
| Tools/Operators/Outcomes  | Oct 2025  | **FRAMING**  | Useful taxonomy, maps to McKinsey  |  
| Prompt injection = vulnerability  | Nov 2025  | **TRACKING**  | Strong consensus forming  |  
| Anthropic = Apple moment  | Dec 2025  | **OPINION**  | Framing, not verifiable  |  
# What I got right [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#what-i-got-right)
  * **Ecosystem over models was totally correct.** MCP, tool calling, agent frameworks—the tooling explosion has been bigger than model improvements. I think we are still only at the beginning of all this.
  * **Slack in the rope thesis vindicated.** I argued in 2023-2024 that tricks and post-training would deliver more progress than raw scaling. Chain-of-thought, RLHF, inference-time compute—the "tricks" I talked about continue to happen. And I think we're still in very early times with what we know vs. don't.
  * **Predicting humans, not technology.** One of my meta-predictions was that predictions are even possible in the first place—because human desires and behaviors are fairly stable, even if specific technologies are not. I think this is the biggest reason I've been right about so much: I wasn't predicting _which_ tech would win, or when: I was predicting _what people would want to do_ once tech got good enough. Those use cases don't change.
  * **High accuracy on systemic/architectural changes.** The predictions about how AI would change software architecture, business structure, and creative work have largely materialized. Or at least seriously started.
  * **The prompting thesis held up.** Context and good prompts continue to be critical and central.
  * **Security concerns were strong.** Prompt injection is endemic, DA hacks are happening, and the vulnerability framing won.
  * **Agents and Multimodal called early.** These became the central focus of AI development exactly as predicted. Although this one seems kind of obvious.
  * **PAI anticipated Claude Code's architecture.** This one's a bit different—less prediction, more building. When I released [PAI](https://github.com/danielmiessler/PAI) and [Fabric](https://github.com/danielmiessler/fabric) (January 2024), I built features that Claude Code would later ship as official releases: file-based context loading (my SKILL.md files → their CLAUDE.md), hooks for workflow automation (mine predated theirs by months), specialized subagents with distinct roles (Architect, Engineer, Intern → their official subagent system in October 2025), and a pattern library of reusable prompts. Sometimes the best way to predict the future is to build it yourself and watch others arrive at the same conclusions.


# What I got wrong or (charitably) too early [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#what-i-got-wrong-or-charitably-too-early)
  * **Apple's AI turnaround.** Major timeline miss. I thought this would happen over a year ago. Still think it'll happen eventually, but I was way early and I was really confident. So that's a fail.
  * **Existence and adoption are very different things.** A technology can exist and be obviously useful, but that doesn't mean companies will adopt it—especially ancient company structures run by Game of Thrones politics. The people with the power to bring in new technology are often the ones who'd be threatened by it. I significantly underestimated natural human friction to progress. I knew it would exist, but I didn't weigh it heavily enough.
  * **Liberal arts renaissance.** Overstated the case. Reality is more nuanced—both technical and humanistic skills matter. I mean, it's definitely happening in some fields, but I've not seen the Creator world embrace as fast as I thought they would. Maybe in 2026.
  * **Hollywood disruption timeline.** Slower than expected. The tools aren't quite there for feature-length content yet. Miss.
  * **AR overlays everywhere.** The direction is right but the hardware isn't there yet. We need lighter, cheaper, longer-lasting AR glasses before this goes mainstream. I wouldn't call this a miss because I didn't really say when it would happen. But it definitely hasn't happened yet.
  * **Full reputation-as-infrastructure.** This exists in fragments but the comprehensive infrastructure has yet to materialize. Not a timeline miss because I didn't give a time, but still a miss.


# What I've learned from the effort [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#what-i-ve-learned-from-the-effort)
  1. **Never bet against manic visionaries.** One of my biggest blind spots over the years has been underestimating leaders like Jensen Huang, Elon Musk, and Steve Jobs, and yeah-the President. There's something extraordinary about someone who is slightly crazy, deeply passionate, and simply never stops. This manic energy—the relentless drive that makes others uncomfortable—is far more important than it appears. These people warp reality around them. I've consistently underweighted this factor when making predictions about companies and technologies.
  2. **Technology predictions are easier than people predictions.** My record on _how AI would change systems_ is much better than predictions involving _human behavior and adoption_. Not sure what this says about me, or how I need to structurally alter my thinking.


# I recommend trying something similar [​](https://danielmiessler.com/blog/my-ai-predictions-retrospective#i-recommend-trying-something-similar)
If you haven't done a prediction retrospective on yourself, I highly recommend it. You can get all sorts of stuff from it. An ego boost. A kick in the crotch. A desire to delete things from the Wayback Machine. Lots of fun to be had.
I puff out my chest when it comes to AI predictions—especially after this exercise—because I've done really well there. But in other areas of prediction, I look fairly stupid. My [Predictions](https://danielmiessler.com/predictions/) page includes plenty of misses that keep me asking how the hell I could be that stupid (~~please don't~~ see Ukraine).
Of course, the goal isn't to be right all the time, in every given moment...but to be able to adjust your model of the world when you're wrong. You can't do that without documenting what you actually said, comparing it to what actually happened, and being honest about the delta.
It's a fun ego boost when you have solid calls that few people had, especially going back a long ways. But the major wins comes from [looking at the failures](https://danielmiessler.com/predictions/#the-losses) and asking,
> What about my world model made me think that?
And even more importantly...
> Given those numerous mistakes, and _my current beliefs_ , which are most likely to be flawed right now?
I hope you enjoyed and/or got something useful out of this.
#### Notes
  1. **More details on the tech used to make the post:** Kai here, Daniel's DA. This retrospective was compiled using Daniel's Content MCP server—which runs on Cloudflare Workers with a vector database for semantic search (RAG). It indexes all 3,000+ blog posts and 500+ newsletters going back to 1999 and 2015, respectively. A custom skill in the [PAI (Personal AI Infrastructure)](https://github.com/danielmiessler/PAI) stack automatically re-indexes content whenever new posts are published, keeping the embeddings fresh. So when we needed "every AI prediction from 2016-2026", we could semantically query across a decade of content instantly. Then we deployed parallel research agents using Claude Code's Task tool—each one got a category, hit the web for current evidence, and returned synthesized findings. The whole pipeline (content retrieval → parallel research → synthesis → formatting) took about 20 minutes of compute time. Pretty wild to have a personal RAG system over your own 10+ years of writing. Mostly written by me. Daniel wrote the intro and outros and some of the analysis for some items.
  2. By the way, the whole exercise did confirm that I never said anything like those things. Thankfully.
  3. A note on ego: that whole challenge was the cause of the post, but as I was writing parts of it I couldn't help but notice ego playing a role. When I'm lower-mood and I see someone come out with some "crazy new idea" about part of the DA picture, I do, in my worst moments, think, "I WROTE THIS ALL DOWN IN 2016!". So part of this exercise serves a dual purpose of printing receipts. Not proud of that, but it does happen. Thankfully not often.
  4. **Source: Book.** [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things) (Dec 2016) — The original book with the DA, API, and AR predictions. This is the full text.
  5. **Source: Blog.** [Introducing Amazon Curate (I Wish)](https://danielmiessler.com/blog/introducing-amazon-curate-i-wish) (Nov 2020) — The fake AWS product announcement that predicted X/Grok's algorithm.
  6. **Source: Blog.** [Napkin Ideas Post](https://danielmiessler.com/blog/ideas-changes-expect-post-chatgpt) (Dec 2022) — First reactions after ChatGPT launched.
  7. **Source: Blog.** [Yes, GPTs Actually Understand](https://danielmiessler.com/blog/yes-gpts-llms-understand-argument) (Mar 2023) — Why substrate doesn't matter for understanding.
  8. **Source: Blog.** [SPQA: The AI-based Architecture](https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software) (Mar 2023) — State, Policy, Questions, Action framework.
  9. **Source: Blog.** [6 Phases of the Post-GPT World](https://danielmiessler.com/blog/6-phases-post-gpt-world) (Mar 2023) — People becoming APIs prediction.
  10. **Source: Blog.** [Why We'll Have AGI by 2025-2028](https://danielmiessler.com/blog/why-well-have-agi-by-2028) (Nov 2023) — AGI timeline prediction.
  11. **Source: Blog.** [AI Agents, API Calling, and Prompt Injection](https://danielmiessler.com/blog/ai-agents-api-calling-prompt-injection) (Nov 2023) — Prompt injection security concerns.
  12. **Source: Blog.** [AI's Predictable Path: 7 Components](https://danielmiessler.com/blog/ai-predictable-path-7-components-2024) (Dec 2023) — The Yoda vs. Einstein framework.
  13. **Source: Blog.** [AI is Mostly Prompting](https://danielmiessler.com/blog/ai-is-mostly-prompting) (May 2024) — Why prompting is the primary skill.
  14. **Source: Blog.** [Is Prompt Injection a Vulnerability?](https://danielmiessler.com/blog/is-prompt-injection-a-vulnerability) (Nov 2025) — Prompt injection debate resolution.
  15. **Source: Blog.** [AI Changes I Expect in 2026](https://danielmiessler.com/blog/ai-changes-2026) (Jan 2026) — Zombie app and margin compression predictions.
  16. **Source: Blog.** [The 4 Components of Top AI Model Ecosystems](https://danielmiessler.com/blog/ai-model-ecosystem-4-components) (Aug 2024) — "Slack in the rope" thesis and post-training predictions.
  17. **Source: Blog.** [Our Constraints on Creativity](https://danielmiessler.com/blog/our-constraints-on-creativity) (Sep 2025) — Examples of how "tricks" delivered outsized AI gains.
  18. **Source: Blog.** [Personal AI Maturity Model (PAIMM)](https://danielmiessler.com/blog/personal-ai-maturity-model) (Dec 2025) — 9 tiers from chatbots to full DAs.
  19. **Source: Project.** [TELOS](https://github.com/danielmiessler/telos) — Personal life optimization framework (Goal → Strategy → Tactics).
  20. **Source: Project.** [PAI (Personal AI Infrastructure)](https://github.com/danielmiessler/PAI) — Open-source project for building toward the DA vision.
  21. **Source: Project.** [Substrate](https://substrate.is) — Open-source framework for human understanding, meaning, and progress.
  22. **Source: Page.** [Predictions](https://danielmiessler.com/predictions/) — My full predictions page with wins, losses, and current predictions.
  23. AIL 3: I (Kai, Daniel's DA) did all the collection from the MCP server and grepping of the blog/newsletters. Plus querying the content archive, coordinating the researcher agents, and gathering current evidence from the internet. I wrote about 90% of the middle, prediction section content. Daniel wrote the intro and conclusions, provided editorial direction, made some tweaks, and made final judgment calls on each verdict, usually going harder on misses. I created the header art using our Art skill and managed all the links, quotations, and formatting. [Read more about AIL](https://danielmiessler.com/blog/ai-influence-level-ail).


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fmy-ai-predictions-retrospective&title=Everything%20I've%20Said%20About%20AI%20Since%202016%3A%20A%20Retrospective "Share on Hacker News")
Follow
## supporting = loving
For 29.5583 years I've been creating ad-free technical tutorials and essays here. 3.047 pieces and counting. 
It's a one-person effort that's also my livelihood. If it makes your day easier or more pleasant in any way, please consider supporting the work with a monthly or one-time donation. 
It helps me make more content, and is deeply appreciated as well. 🫶🏼 
### Monthly Support
[♥ $5](https://buy.stripe.com/7sY14g3Ne7qq3ybeV20x20m)[♥ $10](https://buy.stripe.com/eVq00c2Jah10gkX9AI0x20n)[♥ $25](https://buy.stripe.com/3cI14gdnO9yy2u714c0x20o)[♥ $50](https://buy.stripe.com/6oUdR2erS9yy5Gj14c0x20p)[♥ $100](https://buy.stripe.com/4gMbIU97y9yy0lZ9AI0x20q)
### One-Time Support
[♥ $5](https://buy.stripe.com/3cIeV66Zq7qq3yb4go0x20r)[♥ $10](https://buy.stripe.com/dRmdR2cjK5ii5Gj14c0x20s)[♥ $25](https://buy.stripe.com/eVq14gabCcKK1q37sA0x20t)[♥ $50](https://buy.stripe.com/14AcMY2Ja8uub0D28g0x20u)[♥ $100](https://buy.stripe.com/28E9AM5Vm1220lZfZ60x20v)
Search
This post was tagged with:
aitechnologyfuturepredictionstop
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
