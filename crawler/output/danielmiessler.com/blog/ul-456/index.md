<!-- Source: https://danielmiessler.com/blog/ul-456 -->

# UL NO. 456: A Deep-dive on Prompt Injection
$1 Million to Hack Apple AI Cloud, Feet Pics vs. Spotify, First Impressions of 18.2, System 2 Security Awareness, and more...
October 29, 2024
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #apple](https://danielmiessler.com/archives/?tag=apple)[ #reading](https://danielmiessler.com/archives/?tag=reading)[ #business](https://danielmiessler.com/archives/?tag=business)[ #creativity](https://danielmiessler.com/archives/?tag=creativity)[ #culture](https://danielmiessler.com/archives/?tag=culture)[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #ethics](https://danielmiessler.com/archives/?tag=ethics)[ #future](https://danielmiessler.com/archives/?tag=future)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #meaning](https://danielmiessler.com/archives/?tag=meaning)[ #nationalsecurity](https://danielmiessler.com/archives/?tag=nationalsecurity)[ #philosophy](https://danielmiessler.com/archives/?tag=philosophy)[ #politics](https://danielmiessler.com/archives/?tag=politics)[ #productivity](https://danielmiessler.com/archives/?tag=productivity)[ #science](https://danielmiessler.com/archives/?tag=science)[ #society](https://danielmiessler.com/archives/?tag=society)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #tutorial](https://danielmiessler.com/archives/?tag=tutorial)[ #writing](https://danielmiessler.com/archives/?tag=writing)
 Prime-intellecting…
1 reading now 
SECURITY  AI  PURPOSE**UNSUPERVISED LEARNING****is a newsletter about upgrading to thrive in a world full of AI.** It’s original ideas, analysis, mental models, frameworks, and tooling to prepare you for the world that’s coming.
## TOC
  * [SECURITY](https://danielmiessler.com/blog/ul-456#security) >
  * [AI / TECH](https://danielmiessler.com/blog/ul-456#ai-tech) >
  * [HUMANS](https://danielmiessler.com/blog/ul-456#humans) >
  * [DISCOVERY](https://danielmiessler.com/blog/ul-456#discovery) >
  * [RECOMMENDATION OF THE WEEK](https://danielmiessler.com/blog/ul-456#recommendation-of-the-week) >
  * [APHORISM OF THE WEEK](https://danielmiessler.com/blog/ul-456#aphorism-of-the-week) >


Hey there!
Lily Allen says she earns more from selling feet pics on OnlyFans than from her Spotify streams. She started the account after a pedicurist's suggestion and now makes at least $10,000 monthly from 1,000 subscribers. 
💡Pedicurist as Talent Scout was **not** on my bingo card for 2024. [MORE](https://variety.com/2024/music/news/lily-allen-onlyfans-feet-pictures-spotify-1236191247/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=d6d0317c2d2f66cc116d0ea2d873be198e6794cc) >
—
The new AI features in the 18.2 beta are insanely awesome. Check out this picture I took of a glacier by long-pressing the Siri button on my iPhone 16 Pro. 
It did all that by itself, using the native camera app. I didn’t have to take the picture and send it to OpenAI! 
**In other words, they just fixed Siri.**
Here’s the full thread where I wrote up what I like about the new AI stuff in 18.2. [MORE](https://x.com/DanielMiessler/status/1849257307919515724?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=4b88254609e73f7468ca86e17f8dd81b59f93b55) >
—
Why I think (pure) developers are _seriously_ screwed now. The ease of building an actual app is going way, way down—and faster than even I thought it would. [MORE](https://x.com/DanielMiessler/status/1849979385463402906?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=11b74154d4a36f3eff345f393f9342e6cfd94784) >
—
👇🏼**#1 AI question I get asked** is about how to do AI securely within a company.👇🏼 
Sponsor
**Want to adopt GenAI but need data privacy guardrails first?**
gives security teams [visibility and control around GenAI apps](https://www.harmonic.security/?utm_source=unsupervisedlearning&utm_medium=email&utm_campaign=newsletteroct28&_bhlid=bf9f8616cb27ca4b73aa7a6da1d18e6f223a6ca1) >. 
With Harmonic, you can:
  * Track employee usage and adoption of GenAI
  * Identify Shadow AI and GenAI tools training on your data
  * Detect sensitive data leaving the business via GenAI apps
  * Coach users via inline training and nudging towards safe AI use


[Learn about Harmonic’s unique approach](https://www.harmonic.security/?utm_source=unsupervisedlearning&utm_medium=email&utm_campaign=newsletteroct28&_bhlid=d06b0ed681066e6500d1837730c6923dd44fdd56) > to securing sensitive, unstructured data effectively—without compromising on efficiency.
[ Learn More ](https://www.harmonic.security/?utm_source=unsupervisedlearning&utm_medium=email&utm_campaign=newsletteroct28&_bhlid=fcbc33e08688e07c44b99e52a8817572a061d1e4)
## SECURITY
Apple is offering **$1,000,000** to hack its Private Cloud Compute (PCC) system, which is its new, proprietary cloud system it built to handle Apple Intelligence requests that can’t be done on-device. [MORE](https://www.theverge.com/2024/10/24/24278881/apple-intelligence-bug-bounty-security-researchers-private-cloud-compute?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=ef810bf441b3530d6748e62640c144013e6b29fa) >
🧠**A New Way to Think About Why Security Awareness Doesn’t Work** 💡Had an absolutely brilliant conversation with [Cornelia Puhze](https://www.linkedin.com/in/corneliapuhze?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=7dc065b99f2ef5a677ce3c89f140068f506b62a7) > at the Swiss Cyberstorm speaker dinner. She’s an expert on security awareness and we talked about why most programs don’t work, and her premise was that **the only model that will work is something that interrupts System 1 thinking and gets us a chance with System 2**. 
🤯
In other words, the attacks are getting so good that _you’re not thinking_ —you’re _reacting_. **So all the traditional training in the world won’t help you because you’re not in the mindset where training** _**CAN**_**work**. And this only gets worse with AI-written spearphishing that’s perfectly targeted to your personality flaws.We talked about how the only defense is something like Dialectical Behavior Therapy and similar techniques—that teach you how to **PAUSE** when you become excited or anxious or stressed or whatever. Which is fascinatingly and strangely related to mindfulness. 
Anyway, just love this concept so much because it cleanly explains why security awareness training fails so spectacularly, and hints at a new way of training that could work. [Go follow Cornelia’s work](https://www.linkedin.com/in/corneliapuhze?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=60fa72f1d27cf3b9ea78223f00e52d1279099c78) >. 
—
💉**Clarity on the Definition of Prompt Injection** Got into a debate with someone about whether [Johann Rehberger’s attack against Anthropic’s Computer Use functionality](https://x.com/wunderwuzzi23/status/1849637642339746035?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=4ed66facf64b64c638f73cf0ef938a852c785f2a) > was Prompt Injection or not. Here’s the attack and the thread about it. 
[ ᴅᴀɴɪᴇʟ ᴍɪᴇssʟᴇʀ  @DanielMiessler  This is a SUPER cool demo but I’m not sure I’d classify it as prompt injection.  The issue is that the instruction on the site is to run a program. And Computer Use is designed to follow instructions.  So the demo is showing that computers will follow dangerous instructions.  Johann Rehberger  @wunderwuzzi23  🔥 Welcome the ZombAIs! 🤖🧟 👉 Wondering how difficult it is to craft a prompt injection on a website that takes control of Claude Computer Use, downloads malware & have it join a C2?  Red Teamers might appreciate the blending of TTPs 🙂 Details ⬇️ embracethered.com/blog/posts/202… 10:14 AM • Oct 25, 2024 **12** Likes **3** Retweets  **4 Replies** ](https://twitter.com/DanielMiessler/status/1849756323728007264?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=b04fcd2aa0989704e76c5561110970b595d56518) >
If you go through the whole thread it all comes down to definitions—as usual. My point was that if you tell an AI agent to eat poison—and it eats it and gets hurt—that’s NOT prompt injection. It’s a direct instruction followed by an agent. 
So my take was that if you tell an agent to go to a website and download an executable and execute it—that’s the same. It’s like telling your computer to `rm -rf`. It’ll do it. And that’s not injection, it’s just a dangerous command. 
But what’s super important here is WHO is asking for a given thing to happen, and what they EXPECTED would happen. You have to look at the implied goal of the REQUESTOR, and compare THAT to what ACTUALLY happens. 
So if the requestor said:
Go execute commands on this possibly dangerous website. 
That would _not_ be prompt injection because it was just following commands. 
What I missed in this particular case was that the initial command sent to the tool wasn’t to go and do what was on the website, _but to just load the site_. So the implied expectation of the REQUESTOR was normal browsing—not downloads and executions. So, given my definition above, and this initial setup—**I’d call myself wrong about my original take**. 
Here’s the definition I have in my Real World AI Defintiions now, updated to magnify the importance of this wrinkle. And great research by [Johann Rehberger](https://x.com/wunderwuzzi23?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=cb84f2c24a3f054c74333cd85f5e9647878f8a20) >! 
[THE POST](https://x.com/wunderwuzzi23/status/1849637642339746035?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=4c1e3e41acbc03a7a37cb1ca5561e852c617fa97) > [THE FULL WRITEUP](https://embracethered.com/blog/posts/2024/claude-computer-use-c2-the-zombais-are-coming/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=19c18c1e727c82b0e64b4e1df6bf1c2b8ddf67c4) >
Prompt Injection is an attack technique that uses specially crafted input to trick an AI into doing something that violates intent/expectation and leads to a negative outcome. 
[Real World AI Definitions (RAID)](https://danielmiessler.com/blog/raid-ai-definitions?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=96b0d86a7a93f27f52f3b4c4a00c033645b14e19&last_resource_guid=Post%3Af131a22f-8cae-4304-adec-eb5a130c2b18#prompt-injection) >
Sponsor
**Scale SaaS security and reduce spend with Nudge**
Learn how cloud-first org [Stravito scaled their SaaS security program](https://www.nudgesecurity.com/case-study/stravito?utm_medium=sponsored&utm_source=unsupervisedlearning&utm_content=newsletter&utm_campaign=proof&utm_term=text_casestudy_stravito_secondary&_bhlid=70794095d2a2d4e6ae9f837009c36f40bbd011ae) > while cutting spend and supporting rapid company growth, achieving these results:
  * Immediate visibility of their entire SaaS footprint
  * [Cost savings from unnecessary SaaS licenses](https://www.nudgesecurity.com/case-study/stravito?utm_medium=sponsored&utm_source=unsupervisedlearning&utm_content=newsletter&utm_campaign=proof&utm_term=text_casestudy_stravito_secondary&_bhlid=982dbd0322bd4faad174f217033e128d7f2252eb) >
  * Streamlined user access reviews
  * [Faster vendor security reviews](https://www.nudgesecurity.com/case-study/stravito?utm_medium=sponsored&utm_source=unsupervisedlearning&utm_content=newsletter&utm_campaign=proof&utm_term=text_casestudy_stravito_secondary&_bhlid=512385d6c8564d807cbad43541edd3df2220e518) >
  * Complete (and automated) employee offboarding


Read the case study
[nudgesecurity.com/case-study/stravito](https://www.nudgesecurity.com/case-study/stravito?utm_medium=sponsored&utm_source=unsupervisedlearning&utm_content=newsletter&utm_campaign=proof&utm_term=text_casestudy_stravito_secondary&_bhlid=c0529db995d4c1b26bdd3b414f978dc5f100ac0b) >
[ Read the Case Study ](https://www.nudgesecurity.com/case-study/stravito?utm_medium=sponsored&utm_source=unsupervisedlearning&utm_content=newsletter&utm_campaign=proof&utm_term=text_casestudy_stravito_secondary&_bhlid=013c91cc7c50662007c20064d90e9c718fb2bc01)
VMware has released updates for vCenter Server to fix a critical remote code execution vulnerability, CVE-2024-38812, with a CVSS score of 9.8. [MORE](https://thehackernews.com/2024/10/vmware-releases-vcenter-server-update.html?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=30f45411ee602ee63893080bfe3b9f9423b51395) >
The Biden administration released the first National Security Memorandum on AI. I love its focus on not losing to China, and making sure it’s safe, secure, and trustworthy. It also focused a lot on being aligned with democratic (small d) values.  | 
Fortinet has disclosed a critical vulnerability, CVE-2024-47575, in FortiManager, actively exploited in the wild. Known as FortiJump, this flaw allows remote code execution via the FGFM protocol and affects FortiManager and FortiAnalyzer models. [MORE](https://thehackernews.com/2024/10/fortinet-warns-of-critical.html?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=e1752accad01a210c4dbecd69b0cdc5a64daab36) >
Salt Typhoon (China affiliated) is suspected of breaching major telecom companies, targeting American political figures like Kamala Harris, Charles Schumer, Donald Trump, and J.D. Vance. [MORE](https://www.nytimes.com/2024/10/26/us/politics/salt-typhoon-hack-what-we-know.html?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=914dbae4b886f2e5b8a004b8d3a4920b18157109) >
TSMC has stopped doing business with a client after finding out that chips were being sent to Huawei, which is under US sanctions. The whole game for China now is to find proxies to buy through, or to use services like AWS that can hook up NVIDIA chips. [MORE](https://www.bloomberg.com/news/articles/2024-10-23/tsmc-cuts-off-client-after-discovering-chips-diverted-to-huawei?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=e6fb0626568d9c9252cfa68dc9b8e11e42e5becc) >
Russia amplified false claims about U.S. hurricane responses to manipulate political discourse before the presidential election, according to the Institute for Strategic Dialogue. [MORE](https://abc7chicago.com/post/russia-amplified-hurricane-disinformation-drive-americans-apart-researchers-find/15463309/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=12d0e29ff3fb9c06f74c9ffc47461e8e4f0aa1ac) >
Both US parties are worried about last-minute deepfakes that create chaos and/or move the election. [MORE](https://thehill.com/homenews/campaign/4952349-ai-generated-deepfakes-threaten-election/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=65834d73fbdf4df4c5dab1f382388ed979bc94fb) >
Speaking of that 👆🏼, the FBI says Russian actors created a fake video showing mail-in ballots for Trump being destroyed in Pennsylvania. [MORE](https://ground.news/article/russian-actors-made-fake-video-depicting-mail-in-ballots-for-trump-being-destroyed-fbi-says_a4797a?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=bed3226ffd01bf15c9435a435762f1238adcf914) >
[ Continue reading online to avoid the email cutoff ](https://danielmiessler.com/blog/ul-456?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=b0e7744c1a6458e851fe1882053b4187fd0dd5fc&last_resource_guid=Post%3Af131a22f-8cae-4304-adec-eb5a130c2b18)
## AI / TECH
Google is working on "Project Jarvis," an AI agent for Chrome that automates web tasks like research and booking flights. Powered by Gemini 2.0, Jarvis takes screenshots to interpret and act on tasks. [MORE](https://9to5google.com/2024/10/26/google-jarvis-agent-chrome/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=9ab022792183cf900978ce2490251623029d19c3) >
💡This will be Google’s first move into the all-seeing digital assistant space, and I like to see it only because it will increase pressure on everyone to release theirs.
But I think this implementation is short-sighted due to it being browser-based. They really need "Jarvis" to live deeply in the OS, which is where Apple be heading soon.
World models, or world simulators, are emerging as a significant path for developing AI, and I’m really excited about the direction. 
💡I personally feel (as a non-expert in the weeds) that there will be a certain point of world model development (combined with post-training) that will unlock both AGI and ASI—although it might not be needed for AGI. 
In other words, if an AI understands enough of how the world works, and it understands how to do science (conjecture, experiment design, and testing), that might be all it needs. 
Plus, even if it’s not, it’s also the path to self-improvement. 
TSMC's Phoenix chip plant is outperforming its Taiwan facilities in producing usable chips, according to a company executive on a webinar. Let’s go in-country production! [MORE](https://www.theinformation.com/briefings/tsmc-says-u-s-chip-plant-is-producing-better-results-than-taiwan-facilities?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=1377e1868ef05601e3dffa5223f5fedc7b617145) >
Tesla's Cybertruck is outselling nearly every other electric vehicle in the US. That was quick. Like two months ago they were a laughing stock. [MORE](https://www.businessinsider.com/tesla-cybertruck-outselling-almost-every-other-ev-in-us-2024-10?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=ec115cbc8296be83278c7028662bf2a4601e5da4) >
Waymo just raised $5.6 billion in a Series C to expand to new cities. [MORE](https://techcrunch.com/2024/10/25/waymo-raises-5-6b-from-alphabet-a16z-silver-lake-and-more/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=61482cea04e1d0b524fc6eb5aa4f740f75c7138e) >
Determinate Systems is trying to make Nix is the go-to for software development by enabling flakes, streamlining private repositories, and improving dependency management. [MORE](https://determinate.systems/posts/the-future-is-nix/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=f44a604da02ddb83e0fae1cf6d64ee89d74a862a) >
💡Dammit. These people are going to make me learn Nix aren’t they?
It’s hit my radar enough in the last year that I’m going to take a few days and learn the religion. 
NASDAQ CEO Adena Friedman isn't shocked that startup IPOs haven't bounced back in 2024. She says while the S&P 500 is up 22%, it's mainly due to large-cap companies like Apple and Microsoft, while small-cap companies are struggling. [MORE](https://techcrunch.com/2024/10/27/nasdaq-ceo-adena-friedman-isnt-surprised-we-havent-seen-a-resurgence-in-startup-ipos-yet/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=e587262a5a3603faaa2ce5604aca83bde1ef37ae) >
## HUMANS
Researchers have traced 70% of meteorites to three major collisions in the asteroid belt over the last 40 million years. 
The US economy is leading the G7 with a projected 2.8% GDP growth. US workers are more productive, generating $171,000 in goods and services annually, compared to $120,000 in Europe and $96,000 in Japan. [MORE](https://www.morningbrew.com/daily/stories/2024/10/23/why-the-us-economy-is-leading-its-peers?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=931f44f7059bdf39561870c4b83f85879ec07130) >
Elon Musk has reportedly been in regular contact with Russian President Vladimir Putin since late 2022, which is highly disturbing to me. Probably unrelated, but Elon has seemed a lot less supportive of Ukraine lately. 👎🏼[MORE](https://techcrunch.com/2024/10/25/elon-musk-reportedly-chats-often-with-putin/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=199e9aa7ea19a57eb4626763f83b44f409fab66d) >
Russian lawmakers have ratified a pact with North Korea for mutual military assistance and 3,000 North Korean troops have been deployed to Russia. And South Korea is thinking about sending help to Ukraine as a result. [MORE](https://ground.news/article/russian-lawmakers-ratify-pact-with-north-korea-as-us-confirms-that-pyongyang-sent-troops-to-russia_0e4a8b?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=0b72606e139da5ae7cd6758ea187e3495f61fb64) > | [MORE](https://www.aljazeera.com/news/2024/10/22/south-korea-vows-action-as-north-denies-troops-involvement-in-ukraine-war?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=254ecc39381e872d0d7064aa1891fd04d8d08e56) >
Character amnesia is becoming a widespread issue in China, where even well-educated individuals are forgetting how to write common Chinese characters. [MORE](https://globalchinapulse.net/character-amnesia-in-china/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=5d911df184f39b3b0c4570c6e7c0700b3e021b24) >
A study in Alzheimer's & Dementia suggests semaglutide, found in Ozempic and Wegovy, may lower Alzheimer's risk in Type 2 diabetes patients. The research compared semaglutide to seven other diabetes drugs and found a 70% lower Alzheimer's risk compared to insulin. [MORE](https://www.nbcnews.com/health/health-news/ozempic-linked-lower-alzheimers-risk-people-type-2-diabetes-rcna176821?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=656379707242ab60023c9244c108e263b45b5a81) >
Walking in short bursts can burn 20-60% more energy compared to continuous walking over the same distance. [MORE](https://phys.org/news/2024-10-short-consume-energy-distance.html?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=71a82a0672c2db24c2722ac9dafa83b6c1aae617) >
## DISCOVERY
My friend [Matt Johansen](https://x.com/mattjay?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=aac32d2934d207f20a7a357a1a5442b8aa8ee14a) > highlights the psychological toll of working in security (especially in SOCs), including decision fatigue, anxiety, and sleep disruptions. [MORE](https://www.vulnu.com/p/security-alert-fatigue-mental-health?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=9884e885e19c47e698ed0eed930b40c214a10dc3) >
Google just launched a new 10-hour course called Prompting Essentials to help people write better AI prompts. 
An Ode To Vim [MORE](https://bokwoon.com/posts/1khtfep-an-ode-to-vim/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=7f885358c8c8b215c9fd33e21ea420210d648ff7) >
`PabloNet` — A wall-mounted diffusion mirror turns webcam reflections into AI-generated paintings using `StreamDiffusion`. The setup includes a Raspberry Pi 5, a 10.1" Pi screen, infrared light, and a Pi camera, all housed in a generic frame. [MORE](https://www.matthieulc.com/posts/pablonet/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=60e0a19764b0f33c003d2ecafa07ca88333081f1) >
Japan has introduced a digital nomad visa, and Christian Mack shared his experience of getting one. [MORE](https://www.tokyodev.com/articles/how-i-got-a-digital-nomad-visa-for-japan?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=37c9bd94c59643987b2e6f71c3b7c4fbc14431a0) >
`IRIS` — A new approach called IRIS combines large language models (LLMs) with static analysis to detect security vulnerabilities in software. Using a dataset called CWE-Bench-Java, IRIS detected 69 out of 120 vulnerabilities in Java projects, outperforming traditional static analysis tools that found only 27. [MORE](https://arxiv.org/abs/2405.17238?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=8eb1cffa001759673e6e851156607c529ba6d105) >
School is Not Enough: Learning is a consequence of doing [MORE](https://map.simonsarris.com/p/school-is-not-enough?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=8591f80749830c1faee6cd8301c0e393df7e3e18) >
`llm-whisper-api` — Simon Willison created a quick plugin for LLM to experiment with the OpenAI Whisper API. You can install it using `llm install llm-whisper-api` and run it with `llm whisper-api myfile.mp3`. [MORE](https://simonwillison.net/2024/Oct/27/llm-whisper-api/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=2d391a19ca31916bc213679ae68c5316137fd6e9) >
`simpletext` — A text-only blog engine using Cloudflare Workers and KV store. It's designed to be lightweight and efficient, leveraging Cloudflare's infrastructure for hosting and data storage. [MORE](https://github.com/jonfraser/simpletext?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=6757b25237a45e5df2e99c67e4141d2ca5ece943) >
The Most Important Sentence [MORE](https://danielmiessler.com/blog/the-most-important-sentence?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=b7f11a500e23d8e1c654beb27dfb44630c7c4340&last_resource_guid=Post%3Af131a22f-8cae-4304-adec-eb5a130c2b18) >
One of the weirdest features of the web I know of—text fragments let you link directly to specific text on a webpage without needing an anchor, using a special URL syntax. It even highlights the text when you land on the link. [MORE](https://alfy.blog/2024/10/19/linking-directly-to-web-page-content.html?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-456-a-deep-dive-on-prompt-injection&_bhlid=f4532a5c52d98c1d5c3b7f7967bfd9caa958623b) >
## RECOMMENDATION OF THE WEEK
The counterforce to election stress is reading some older good reading. Here’s a great list to choose from. 
1._Gödel, Escher, Bach: An Eternal Golden Braid_ by Douglas Hofstadter 
2._Zen and the Art of Motorcycle Maintenance_ by Robert M. Pirsig 
3._The Book: On the Taboo Against Knowing Who You Are_ by Alan Watts 
4._The Structure of Scientific Revolutions_ by Thomas S. Kuhn 
5._Finite and Infinite Games_ by James P. Carse 
6._Seeing Like a State_ by James C. Scott 
7._The Spell of the Sensuous_ by David Abram 
8._Ishmael_ by Daniel Quinn 
9._Mind and Nature: A Necessary Unity_ by Gregory Bateson 
10._Small Is Beautiful: Economics as if People Mattered_ by E.F. Schumacher 
## APHORISM OF THE WEEK
❝ 
What you don’t change, you choose. 
 _Laurie Buchanan_
Thank you for reading. Please forward to a friend and/or share on socials to help support the work.🫶🏼 
Daniel
>
Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Ful-456&title=UL%20NO.%20456%3A%20A%20Deep-dive%20on%20Prompt%20Injection "Share on Hacker News")
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
aiapplereadingbusinesscreativityculturecybersecurityethicsfutureinnovationmeaningnationalsecurityphilosophypoliticsproductivitysciencesocietytechnologytutorialwriting
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
