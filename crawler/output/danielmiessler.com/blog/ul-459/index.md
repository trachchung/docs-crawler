<!-- Source: https://danielmiessler.com/blog/ul-459 -->

# UL NO. 459: New Active 0-day Exploitation, AI That Sees Your Open Apps, The RebootAI Project
A conversation with Rob Allen from ThreatLocker, UL's Black Friday sale, Finland's internet disrupted, and more...
November 19, 2024
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #apple](https://danielmiessler.com/archives/?tag=apple)[ #reading](https://danielmiessler.com/archives/?tag=reading)[ #business](https://danielmiessler.com/archives/?tag=business)[ #creativity](https://danielmiessler.com/archives/?tag=creativity)[ #culture](https://danielmiessler.com/archives/?tag=culture)[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #ethics](https://danielmiessler.com/archives/?tag=ethics)[ #future](https://danielmiessler.com/archives/?tag=future)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #meaning](https://danielmiessler.com/archives/?tag=meaning)[ #productivity](https://danielmiessler.com/archives/?tag=productivity)[ #science](https://danielmiessler.com/archives/?tag=science)[ #society](https://danielmiessler.com/archives/?tag=society)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #tutorial](https://danielmiessler.com/archives/?tag=tutorial)[ #writing](https://danielmiessler.com/archives/?tag=writing)
 Glanding-flux…
1 reading now 
SECURITY  AI  PURPOSE**UNSUPERVISED LEARNING****is a newsletter about upgrading to thrive in a world full of AI.** It’s original ideas, analysis, mental models, frameworks, and tooling to prepare you for the world that’s coming.
## TOC
  * [SECURITY](https://danielmiessler.com/blog/ul-459#security) >
  * [AI / TECH](https://danielmiessler.com/blog/ul-459#ai-tech) >
  * [HUMANS](https://danielmiessler.com/blog/ul-459#humans) >
  * [IDEAS](https://danielmiessler.com/blog/ul-459#ideas) >
  * [DISCOVERY](https://danielmiessler.com/blog/ul-459#discovery) >
  * [RECOMMENDATION OF THE WEEK](https://danielmiessler.com/blog/ul-459#recommendation-of-the-week) >
  * [APHORISM OF THE WEEK](https://danielmiessler.com/blog/ul-459#aphorism-of-the-week) >


Hey there!
  * Had a great conversation with Rob Allen from [ThreatLocker](https://www.threatlocker.com/ul?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=17aad21cc90819fbcca4158cab0eda1fd9ac57ee) > about their Zero Trust approach: deny-by-default, dynamic ACLs, and blocking ransomware at every stage. 

> > > > > > >
A Conversation with Rob Allen from ThreatLocker 
The UL Black Friday Membership window is now open. [GET IT](https://buy.stripe.com/eVa7w50oY21823K14m?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=ebdb3a1b1b6e77cc6db58c796af422939b82a9a4) > 👇🏼 
#  🦃UL Membership Black Friday Sale
It’s time for turkey and cranberry sauce again, which means it’s also time for **a Black Friday Sale of 20% off the first year of UL Membership**.
Here’s what members get:
  * Access to the smartest, most curious, and **KINDEST** community out there
  * Direct access to Daniel and hundreds of security and AI professionals
  * Exclusive Member-Only content
  * Access to the UL Book Club, which has run monthly since 2017!
  * Access to our Mid-month Meetups, where we discuss career / life
  * DEEP discounts on paid courses and products


**Best of all is the people**. It’s seriously the best community I’ve ever been a part of.
🫶🏼
_"Daniel has created a place for civil discussion in a world that frequently prefers argument over discussion."__- Ben Collins_
Use coupon code BLACKFRIDAY20
[ Join Our Community of the Kind and Curious ](https://buy.stripe.com/eVa7w50oY21823K14m?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=9446a17fd838d7d78608e1e91cb5229310e1e2d5)
  * Upgraded all my Ubiquiti gear and am making progress towards a 10Gbit world. 
  * Heading to Saudi soon to speak at Blackhat MEA!


## SECURITY
This one didn’t get nearly enough coverage last week. **ChatGPT has a new feature that can read code from MacOS apps like VS Code, Xcode, and Terminal** , making it easier for people to use AI in a live way without copy-pasting. The new feature called, "Work with Apps," uses MacOS's Accessibility API to read text right from your screen. [MORE](https://techcrunch.com/2024/11/14/chatgpt-can-now-read-some-of-your-macs-desktop-apps/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=fa43a8183e5ca6c19bb8a6c17912b8155d230e5b) >
💡This is getting closer to what some other startups are working on, where they’re watching your screen and AI is operating on it. That functionality scares the crap out of me, though, so I’m only likely to use it with Apple and maybe Google if they haven an option to turn off the data harvesting / ads stuff.
For startups, I’m really worried about them getting all this data and then getting compromised. I see it as a virtual inevitability. I really only trust a handful of companies (mostly just Apple, actually) with this much—and this level—of data.
Something—or some one—has cut the data cable between Finland and Germany. Finland's internet access is currently routed through Sweden. Many are assuming shenanigans. [MORE](https://www.bloomberg.com/news/articles/2024-11-18/finland-says-subsea-germany-link-serving-data-centers-is-severed?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=1e1e5389316b2394adc2479d8598f916fbd75fe8) >
Sponsor
**Are genAI tools integrated with your other apps?**
Nudge Security [discovers all genAI accounts ever created by anyone in your org](https://www.nudgesecurity.com/use-cases/ai-security?utm_medium=sponsored&utm_source=unsupervisedlearning&utm_content=newsletter&utm_campaign=ai_security&utm_term=secondary_ai-integrations&_bhlid=def631610c41238b2de2d239f8d6d7c8d659368e) >, as well as the OAuth grants that enable data-sharing across apps.
Start a free trial to:
• Discover all genAI tools ever used in your org
• See all users, authentication methods, and OAuth grants
• [Get alerted of new genAI tools](https://www.nudgesecurity.com/use-cases/ai-security?utm_medium=sponsored&utm_source=unsupervisedlearning&utm_content=newsletter&utm_campaign=ai_security&utm_term=secondary_ai-integrations&_bhlid=993af2bc78a3a96404a041f7a88d8cc8bd2c0833) > or integrations
• Vet unfamiliar tools with security profiles for each provider 
[nudgesecurity.com/use-cases/ai-security](https://www.nudgesecurity.com/use-cases/ai-security?utm_medium=sponsored&utm_source=unsupervisedlearning&utm_content=newsletter&utm_campaign=ai_security&utm_term=secondary_ai-integrations&_bhlid=ae71fe5c4a8c84c780e847e0af734b99ec818e98) >
[ Try it Now ](https://www.nudgesecurity.com/use-cases/ai-security?utm_medium=sponsored&utm_source=unsupervisedlearning&utm_content=newsletter&utm_campaign=ai_security&utm_term=secondary_ai-integrations&_bhlid=71e7586505f6200960b4dc593725ea8137ac5f26)
Palo Alto Networks has released Indicators of Compromise (IoCs) for a new zero-day vulnerability affecting their firewalls. 
VMware confirmed that threat actors are exploiting two vCenter Server vulnerabilities, CVE-2024-38812 and CVE-2024-38813, which were first disclosed at the 2024 Matrix Cup hacking competition. 
Sponsor
**Build a Cybersecurity Awareness Program That Works**
Learn how Goodwin Motor Group crafted a [successful cybersecurity culture](https://my.demio.com/ref/vmFQd0VLINWcsozs?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=8b3ea75599d8f7e0db5042ee925d86c7430ef838) > that engages everyone—from execs to frontline staff. [Discover actionable tips](https://my.demio.com/ref/vmFQd0VLINWcsozs?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=dcfe9e715dada52fae08a4c4ca78c4f539bb15bd) > for creating compelling training, sustaining participation, and , shared by the champions behind this thriving program. 
[ Reserve My Spot ](https://my.demio.com/ref/vmFQd0VLINWcsozs?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=f4052c8f75c40c9718858eb17c0ad3814c1529ff) [ Continue reading online to avoid the email cutoff ](https://danielmiessler.com/blog/ul-459?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=1c2fb7e2b2e46bdfbb58d41e23c14086dbf6273b&last_resource_guid=Post%3A63c45ae2-17db-4c06-b3db-5442c1097133)
## AI / TECH
Anthropic has a new Prompt Improver, that takes a given prompt and writes a better one. This is an example of ecosystem improvement I’ve been talking about. [MORE](https://x.com/dr_cintas/status/1858187352918618495?s=12&utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=ed63f54a7c71653cb2fc55dac2dbf05e280f7366) >
OpenAI might launch an "AI agent" tool called "Operator" in January. Operator will compete with Anthropic's "Computer Use" and Google's rumored agent. [MORE](https://techcrunch.com/2024/11/13/openais-take-on-ai-agents-could-come-in-january/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=aae0ed2892bfc105d4069b25864ce871c234387e) >
💡I’m anticipating that in 2025 the biggest thing in AI will be **the maturation of Agents.** They started getting decent in 2024, next year they’ll get mature enough—and integrated enough—for real-world use cases. 
The models will get smarter, but I think most of the benefit will be in [the tooling and ecosystems](https://danielmiessler.com/blog/ai-model-ecosystem-4-components?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=aaab27bc0e0fe5d0d4da62da74d2e57161f1ef48&last_resource_guid=Post%3A63c45ae2-17db-4c06-b3db-5442c1097133) > around the models—not the models themselves.
For agents, it’s helpful to remember what the actual milestone is, which is pretty simple to track.
  * Constant monitoring of audio, video, text of everything you’re doing
  * That means cameras and microphones on your body
  * And full monitoring of the screens and I/O of your devices/computers


This is what’s going to feed your personal and work DAs with the full context it needs to serve you best. And that’s [what all these efforts will eventually push towards](https://danielmiessler.com/blog/ai-predictable-path-7-components-2024?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=c64ada421c880b4309c64bbff01344100b3f09c9&last_resource_guid=Post%3A63c45ae2-17db-4c06-b3db-5442c1097133) >, even if they’re not doing so yet.
Sam Altman and Arianna Huffington's Thrive AI Health is an AI assistant that aims to offer personalized advice on sleep, food, fitness, and more. [MORE](https://techcrunch.com/2024/11/14/sam-altman-and-arianna-huffingtons-thrive-ai-health-assistant-has-a-bare-bones-demo/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=960a542cc35a18102ca5486bec333cc69d9a5b6f) >
is putting $20 million in cash and $2 million in cloud credits into a new initiative to help researchers use AI for scientific breakthroughs. 
Apple's M4 Max CPU transcribes audio twice as fast as Nvidia's RTX A5000 GPU while using significantly less power. In a user test, the M4 Max completed an audio transcode in 2:29 minutes using Whisper V3 Turbo, consuming just 25 watts, compared to the RTX A5000's 4:33 minutes and 190 watts. [MORE](https://www.tomshardware.com/pc-components/cpus/apple-m4-max-cpu-transcribes-audio-twice-as-fast-as-the-rtx-a5000-gpu-in-user-test-m4-max-pulls-just-25w-compared-to-the-rtx-a5000s-190w?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=325beaa6540eab7278efe703804b8c41dd44d742) >
💡Really want one of these, but can’t justify it yet. The real question is whether our next AI rigs should be a cluster of Mac Mini’s, or a standard big beefy NVIDIA-based box.
I’m thinking it might be big box for the next one, and then the one after that is probably some other architecture we can’t see yet? Or perhaps an Exolab cluster of Apple-based systems?
iOS 18.2's Music Recognition feature now logs where you were when you heard a song. This new "Musical Memories" feature geotags songs, so you can remember the exact location you discovered them. [MORE](https://9to5mac.com/2024/11/13/ios-18-2-music-recognition-will-tell-you-where-you-heard-a-song/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=6dc639fb02f0505dae0b34f34c522e3b6f8eb1c6) >
## HUMANS
Pharma stocks have crashed due to RFK Jr. taking over Health and Human Services. Moderna is down close to 40%, and other stocks are suffering in a similar way. Not sure how this isn’t a buy opportunity, though. I don’t see how most people (and RFK) don’t figure out how to tell the difference between good and bad stuff these companies are doing. [MORE](https://www.morningbrew.com/daily/stories/2024/11/16/rfk-jr-cabinet-nomination-tanks-pharma-stocks?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=2e2c3f8d39eef7ce3c2baf469b4738af6e1ce299) >
Netflix hit a record 65 million concurrent streams during the Mike Tyson vs. Jake Paul fight, reaching 60 million households worldwide. But there were over 100,000 complaints about buffering and connection problems. [MORE](https://www.theverge.com/2024/11/16/24298338/netflix-mike-ttyson-vs-jake-paul-fight-netflix-60-million-households-streaming-quality-buffering?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=e75c912014367d73cb84fd9619658327a62f8c7f) >
A new study shows that treating bullying as a collective issue rather than an individual one can significantly reduce its occurrence in primary schools. The approach involves engaging the entire school community, including teachers, students, and parents, to address and prevent bullying. [MORE](https://phys.org/news/2024-11-bullying-problem-incidence-primary-schools.html?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=25a3938ce90d52a97ca80cc53ff99727b7b10cf9) >
💡I love this concept, which reminds me of how some countries handle prostitution by going after the buyers rather than the sellers. It’s an economics way of looking at a whole system, and not just the obvious place. 
With bullying, I think what needs to happen is some level of shaming of the kids who see it happen and do nothing about it, e.g., intervening, telling adults, etc.
## IDEAS
**RebootAI — An Offline AI Oracle for Emergencies** I want to build a local AI that can run offline in bad situations like earthquakes, meteor strikes, and any other scenario where we might have power (like from solar), but no internet. So the idea is that I want something I can ask how to do anything! **Tourniquets, sterilizing water, building shelters, identifying edible plants, etc**. So ideally this would be both text and image capable, and just as resilient an implementation as possible. 
Who wants to help me build it? Or does anyone know of one already out there? Even better if it’s its own standalone box, and you can just update the model used every once in a while. 
## DISCOVERY
Cloudflare's `robots.txt` file is a mix of ASCII art and directives for web crawlers. It allows Twitterbot and DemandbaseWebsitePreview to access specific language pages, but blocks many others from accessing various parts of the site, like search results and feedback pages. [MORE](https://www.cloudflare.com/robots.txt?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=ff72c2b2266dbddaaea7051e60311cae708c6e47) >
`Managing High Performers` — A guide on how to effectively manage high-performing employees. It covers strategies for keeping them motivated, providing the right challenges, and ensuring they feel valued within the organization. [MORE](https://substack.com/@staysaasy/p-144436923?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=308065a784fe20c3048db5898162611c3644c7bf) >
Ian's Secure Shoelace Knot is the best shoelace knot I know of. I actually tie this for my sneakers and mostly leave them that way and slip them on and off. [MORE](https://www.fieggen.com/shoelace/secureknot.htm?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ul-no-459-new-active-0-day-exploitation-ai-that-sees-your-open-apps-the-rebootai-project&_bhlid=c6dbcb260715b3f3200d5ffe5103e6ce6aa14911) >
## RECOMMENDATION OF THE WEEK
  1. Check out the Aphorism of the Week below.
  2. Focus your efforts on being flexible after wrong notes, as opposed to being able to play perfect notes all the time. 


2025 and the next few years are likely to be so crazy that we won’t be able to plan or play the right notes. 
But what we can get good at doing is **adapting once the wrong note is played**. 
## APHORISM OF THE WEEK
❝ 
If you hit a wrong note, it's the next note you play that determines if it's good or bad. 
Miles Davis 
Thank you for reading. Please forward to a friend and/or share on socials to help support the work.🫶🏼 
Daniel
>
Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Ful-459&title=UL%20NO.%20459%3A%20New%20Active%200-day%20Exploitation%2C%20AI%20That%20Sees%20Your%20Open%20Apps%2C%20The%20RebootAI%20Project "Share on Hacker News")
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
aiapplereadingbusinesscreativityculturecybersecurityethicsfutureinnovationmeaningproductivitysciencesocietytechnologytutorialwriting
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
