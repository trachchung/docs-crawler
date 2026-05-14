<!-- Source: https://danielmiessler.com/blog/ai-changes-2026 -->

# AI Changes I Expect in 2026
My thoughts on what's coming for AI in 2026
January 5, 2026
 Boss-fighting…
Here are the biggest changes I see coming to AI in 2026.
# AI becomes _**Verifiable**_ [​](https://danielmiessler.com/blog/ai-changes-2026#ai-becomes-verifiable)
And when I say "verifiable," I don't mean "trustworthy," which a lot of people confuse and has always been a criticism of AI since 2023.
This is verifiability in the test-driven-development sense. Or the prompting evals sense. It's testing and judging whether the output is what we asked for.
I tremendously appreciate [Andrej Karpathy's](https://karpathy.ai/) concept of [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35), where he talks about 1.0 being about _writing_ software, and 2.0 being about _verifying_ software.
This rhymes closely with several converging thoughts I've had over the last 10 years around [goal pursual](https://danielmiessler.com/blog/the-real-internet-of-things#desired-outcome-management-dom) ([TRIOT](https://danielmiessler.com/blog/the-real-internet-of-things), 2016), hill-climbing, [moving from current state to ideal state](https://danielmiessler.com/blog/ai-state-management), and [automation of the scientific method](https://github.com/danielmiessler/PAI#the-inner-loop-the-scientific-method).
Central to all of these is _Verifiability_.
You can't hill-climb if you don't know if you're getting higher. So the primary questions become:
  * What does success look like, and
  * What are the verifiable markers indicating that you're making progress towards it?


_I'm obsessed with finding ways to do this across domains._ And the cross-domain bit is actually what's important. One of the main reasons AI impacted coding first is that it's one of the more _verifiable_ domains that exist.
  * You know if something compiles
  * You know if something runs
  * You know if something produces the output that you wanted


So, what are the equivalents of these for other tasks? Like business tasks and personal tasks. That is what will start to congeal over the next year and after.
Right now it's not much of a consideration because most people aren't thinking deeply about AI or how it will be used or how it will apply to their business. They are too busy responding to the board and management telling them to implement it yesterday already.
# Agents Move from Call and Response to Continuous [​](https://danielmiessler.com/blog/ai-changes-2026#agents-move-from-call-and-response-to-continuous)
As great as 2025 was for agents, they were still largely manual and interactive. You ask them to do something, they go off and do it, and they come back with the result.
But if you shut down your interface, like closing down [Claude Code](https://www.anthropic.com/claude-code) for example, it all stops until you start it back up again.
This year, we are going to see a lot more continuous agents via:
  1. Cloud environments that run in conjunction with your interactive sessions
  2. Scheduled Agentic tasks
  3. Triggers for monitoring systems to look for that activate agents to perform tasks based on a particular state change


I'm working on all of these as part of the [PAI](https://github.com/danielmiessler/PAI) project. But others will be working on the same things as well.
Speculating...
# The Value of Things Becomes Vertical [​](https://danielmiessler.com/blog/ai-changes-2026#the-value-of-things-becomes-vertical)
It will become a lot less valuable to do only parts of a task that you're asked to do. We'll all be asked to go vertical, which is a fancy word for solving all the different problems involved in creating the solution.
The new expectation will be that you can go from problem to solution, up to and including the promotion of the solution so it actually gets adopted.
Keep in mind, this is how principals and fellows have always worked. The more senior someone becomes in an org, the more we require them to be vertical, albeit by using their team.
# We All Get Massive AI Content Fatigue [​](https://danielmiessler.com/blog/ai-changes-2026#we-all-get-massive-ai-content-fatigue)
The problem with AI content isn't only with addictive short-form videos on sites like TikTok, X, and Instagram.
Post and reply-based sites like LinkedIn could become unusable because not only are a lot of the articles going to be AI, but the replies will be as well.
So like, what's the point? Are we just watching AI talk to AI?
Already, at the end of 2025, when I posted something, I would immediately see 3-4 comments come in within a couple of minutes with these highly articulate, well-formed, and obviously AI sentences and paragraphs. From someone I've never interacted with or heard of.
I think this will force us to lower our apertures on who we follow and allow to lock it down only to people that we trust to produce authentic content and actually produce opinions of value.
# The Gap between the AI-Native and the AI-Abstinent/Averse Explodes [​](https://danielmiessler.com/blog/ai-changes-2026#the-gap-between-the-ai-native-and-the-ai-abstinent-averse-explodes)
In 2024 and 2025 it was kind of okay for you to think AI was stupid or hype, and to use it as little as possible at work and in your personal life. The difference between someone using AI and you still wasn't _that_ large.
That changes this year.
The amount of work that an AI-native person can do will increase so much that hiring managers will be looking at this as one of their primary hiring filters. And even in people's personal lives, it's just going to become obvious who is AI magnified and who isn't.
# Creation Becomes More Interesting Than Consumption for Many [​](https://danielmiessler.com/blog/ai-changes-2026#creation-becomes-more-interesting-than-consumption-for-many)
One of the more positive things I see happening is people getting excited about building and creating things.
In the last month of 2025, much of my friend group has stopped playing games and has started building using [Claude Code](https://www.anthropic.com/claude-code). And they are _addicted_.
Addiction isn't usually a good thing, but when compared to watching TikTok or NETFLIX I have to say this is an improvement. It does present a question, though, of if we're making things for people to use, who is going to use them?
# We'll See Our First Bestselling Books Written by AI [​](https://danielmiessler.com/blog/ai-changes-2026#we-ll-see-our-first-bestselling-books-written-by-ai)
I think writing a book is largely an orchestration problem.
Plenty of people have amazing ideas for characters or points they want to make across fiction and nonfiction. The issue is being able to hold it all in your mind at once and logically break it into chapters and then churning through the content.
I'm sure there are thousands, and maybe even millions, of people who have lots of notes for a book. Maybe even chapter outlines, or maybe even just a list of ideas for a book they wish they could write.
Platforms like [Claude Code](https://www.anthropic.com/claude-code) and the open-source [PAI](https://github.com/danielmiessler/PAI) platform I'm building make something like this a lot more approachable.
My project, and I'm sure many others, will be able to take a whole bunch of notes from you, interview you extensively for one or more hours as you fill in the scaffolding of what you want to happen in the book. If it's fiction, or what you want to convey, if it's nonfiction. And then the system will proceed to build out a structure, fill in the main points, and weave the whole thing together in a matter of minutes.
Books are not that long. The issue is just the organization of all those thoughts into something cohesive.
Of course you'll still need good ideas and creativity, and some measure of discipline. But if the discipline required drops to 2% of what it used to be, and the orchestration component which stopped the vast majority of would-be authors from becoming actual authors goes away, we're about to have a whole bunch of books hit the market. And some of them will be extraordinary.
# AI-Powered Content Discovery Finally Arrives (Prediction Validated) [​](https://danielmiessler.com/blog/ai-changes-2026#ai-powered-content-discovery-finally-arrives-prediction-validated)
In January 2026, Elon Musk announced how Grok would power X's new algorithm:
  * Grok reads every post on X (100M+ daily)
  * Matches content to 300-400M users based on what they'll enjoy
  * Filters spam and scam automatically
  * Fixes the small/new account visibility problem
  * Users can ask Grok to adjust their feed


This is exactly what I predicted in November 2020 with my fake product announcement [Introducing Amazon Curate (I Wish)](https://danielmiessler.com/blog/introducing-amazon-curate-i-wish):
> "**Survey** : A high-speed crawling platform optimized for discovering niche content across the internet. **Surface** : A customization engine using machine learning to analyze content features and match them with user interests."
I also wrote in [Machine Learning Will Revolutionize Content Discovery](https://danielmiessler.com/blog/machine-learning-will-revolutionize-content-discovery) that "99% of the best content is never discovered" and that ML would finally fix the small creator visibility problem.
The core insight was that "great contentness" could be assessed algorithmically—quality over popularity. The best content would finally rise to the top based on merit, not just follower count or engagement gaming.
Six years later, that's exactly what X is building with Grok. Sometimes predictions take a while to materialize, but the underlying human need (finding quality content) was always there. The technology just had to catch up.
# X Returns as a Primary Media Platform After Years of Being Shunned Due to Hateful and Clickbait Content [​](https://danielmiessler.com/blog/ai-changes-2026#x-returns-as-a-primary-media-platform-after-years-of-being-shunned-due-to-hateful-and-clickbait-content)
If you use X for a particular topic, and especially for AI, it is, without question, the best place to have conversations about the latest things that are happening.
A lot of people who abandoned X to go to [Bluesky](https://bsky.app/) or [Mastodon](https://joinmastodon.org/) found out that they were lacking key ingredients and possessing others that were their own type of toxic. Most of the people actually building things and being excited and positive about the world are on X, not there. So the conversations did not have nearly as much energy and positivity to them.
# AI Zombie Apps Start to Become Significant Technical Debt [​](https://danielmiessler.com/blog/ai-changes-2026#ai-zombie-apps-start-to-become-significant-technical-debt)
This will largely be an enterprise problem, but it will apply to the internet in general.
So many people are making so many things, and priorities are changing so fast, that they will just kind of stand them up and leave them out there. That's a whole lot of attack surface that will slowly decay over time.
This will cause problems in two major ways:
  1. Security is important because there will often be misconfigurations, keys, API tokens, and all sorts of things out there that allow for compromise of accounts and sensitive information.
  2. People will lose money because they don't realize how much they're paying for services that they thought they turned off


Eventually, AI will catch up and agents will be able to track all this stuff down for people. But there's going to be a window of a few years when this is going to get really nasty. I think that starts spinning up in 2026.
#### Notes
  1. On the X thing, even worse, the "better" platforms ended up largely being people attacking each other about who was more liberal and inclusive, etc., in a way that destroyed all hope of an open, useful discussion. It made it impossible to have normal conversations without being attacked by fellow liberals. Like, people who agreed with you 99% on the issues that matter. So basically the alternatives dried up, with the exception of LinkedIn which is thriving now. And with AI going nuclear in 2025, X became the place to talk about it. X still has significant problems with what it allows as it relates to companies wanting to buy advertisements there. That will remain a problem because Elon's definition of what should not be on a platform is literally "things that are illegal". So if it's legal to say, then he will allow it on the platform. I think that's admirable and the right position, but I still hate it because it attracts and encourages the worst of humanity to go there and spew garbage. It also makes it nearly untouchable for companies wanting to conduct business there. There needs to be a much better filtering system that allows awful people to do whatever they want to do without bothering regular people trying to have normal conversations and do business. We'll see how that plays out. But for AI conversation—and I think an increasing amount of other types of focused conversation—the toxicity doesn't really enter into it, and it's just the best place for talking about what people are building in a positive way. The positivity is absolutely critical. Sometimes it borders on mania, but I'll take that any day over constant whining about how much the world sucks while essentially doing nothing about it.


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-changes-2026&title=AI%20Changes%20I%20Expect%20in%202026 "Share on Hacker News")
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
aifuture
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
