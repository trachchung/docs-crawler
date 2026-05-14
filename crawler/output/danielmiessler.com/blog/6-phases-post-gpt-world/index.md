<!-- Source: https://danielmiessler.com/blog/6-phases-post-gpt-world -->

# 6 Phases of the Post-GPT World
March 27, 2023
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #business](https://danielmiessler.com/archives/?tag=business)[ #creativity](https://danielmiessler.com/archives/?tag=creativity)[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #ethics](https://danielmiessler.com/archives/?tag=ethics)[ #future](https://danielmiessler.com/archives/?tag=future)[ #society](https://danielmiessler.com/archives/?tag=society)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #top](https://danielmiessler.com/archives/?tag=top)
 Asimov-computing…
  1. [Companies Become Models/APIs](https://danielmiessler.com/blog/6-phases-post-gpt-world#companies) >
  2. [People Become Models/APIs](https://danielmiessler.com/blog/6-phases-post-gpt-world#people) >
  3. [AI Assistants](https://danielmiessler.com/blog/6-phases-post-gpt-world#assistants) >


  1. [Content Authentication](https://danielmiessler.com/blog/6-phases-post-gpt-world#authentication) >
  2. [Knowledge Work Replacement](https://danielmiessler.com/blog/6-phases-post-gpt-world#jobs) >
  3. [The Creativity Explosion](https://danielmiessler.com/blog/6-phases-post-gpt-world#creativity) >


## Introduction
We’ve all seen the non-stop stream of news from OpenAI. First we see GPT-4, where you have the announcement on Tuesday morning and you basically have thousands of companies launched by sundown. 
And then we see [chatgpt plugins](https://openai.com/blog/chatgpt-plugins?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world) > drop, which are basically ways of implementing entire businesses as plugins! This is what I said when Brockman dropped the web search plugin. 
Then you’ve got Midjourney, which is putting out some insane stuff, with a special focus on realism. I used it to make this image of Bernie Sanders as a DJ. 
Deep socialist beats, and the hands are improving
Predictions are hard, especially about the future.
Anyway, things are nuts right now. But what I’m going to talk about in this piece isn’t GPT-4, or MidJourney, or [how to make awesome prompts](https://danielmiessler.com/blog/response-shaping-how-to-move-from-ai-prompts-to-ai-whispering/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world&last_resource_guid=Post%3A3e1b76ca-c4c5-4551-aca4-5e005795af1d) >. What I’m going to talk about is **what happens to tech and society** as a result of all these technologies. 
This is the tech I think will logically follow GPT-4 and ChatGPT Plug-ins, and how it will affect jobs, society, and basically the world. As we go through each one, think about which best suits you and which ones you’re going to play in. Let’s look at the first one. 
This is already happening via [ChatGPT Plugins](https://openai.com/blog/chatgpt-plugins?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world) >. 
## 1. Companies become custom models and APIs
Our current companies that display their wares through websites, catalogs, and legacy software with databases and SQL queries will go away. They’ll be replaced by custom GPT models that ingest everything that makes up that business. 
[SPQA](https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world&last_resource_guid=Post%3A3e1b76ca-c4c5-4551-aca4-5e005795af1d) > is one likely architecture for this. 
  * Instead of writing traditional software, companies are going to dump all their data into custom GPT models 
  * That’s all the log data, all their documents, all their voice calls, all their meeting transcripts, all their finances, etc. Basically everything 
  * This data will be combined with another model where the leaders of the company define its mission, its goals, its challenges, and its strategies 
  * Combining these models with a massive LLM like GPT-6 (or whatever is available at the time) will change the interface to companies from statically coded queries to a brittle database schema 
  * Instead you’ll just ask questions and give commands
  * And the way you make your services available will be through such queries, i.e., asking normal human questions that hit your company’s models via API 


## 2. We (humans) become custom models and APIs
First it’ll be companies, then it’ll be us.
Now that we can ingest the content of businesses, what comes next? Ingesting the content of people! 
Both businesses and people have missions, goals, and KPIs.
Just as businesses have logs and Google Docs, we’ll upload all our journals, our blogs, every picture of us from birth, our Twitter feeds, our Instagram, our friend connections, etc. 
But not just our past, also our mission in life, our goals, our preferences, our food likes and dislikes, our favorite celebrities, our favorite art, culture, and music, etc. Don’t worry, there will be interview services that talk to you for hours to extract all of this. It’ll be [the SPQA model](https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world&last_resource_guid=Post%3A3e1b76ca-c4c5-4551-aca4-5e005795af1d) >, just for people. 
MidJourney’s interpretation of this article
  * Imagine being able to instantiate a version of yourself based on everything GPT-7 + this custom model knows about you 
  * It knows your past, your hang-ups, your preferences, your desires, your traumas, your loves and your hates 
  * Now you can spin up a therapist AI and have it interview the AI version of yourself, and create a report to give your actual meatspace therapist 
  * You can talk to younger versions of yourself
  * And without spinning off into orbit for this article (I’ll do this in a separate piece), this will also become the new holy grail for immortality 
  * We’ll upload our full genome, petabytes of knowledge about you and everything that shaped your upbringing. Interviews. Video footage. History. Everything. All that becomes context in the construction of you 
  * That gets stored as a model of you when you die, and the new "cryo" companies will use that as the thing they inject into the new body/brain when that tech becomes available 


Anyway, that last one is a distant use case. But it’s tied to the human desire to survive, so it’s as inevitable as moisturizer. 
The more immediate uses will be instantiations of ourselves for self-exploration and to present as APIs for interaction with the APIs of others, e.g., exchanging preferences, mutual desires, shared goals, social lubrication, meet-ups at scale, synchronized social experiences, etc. 
## 3. AI assistants
It’s hard to predict the actual order here. Maybe they evolve together.
The next thing that happens—and again, this one is already starting as well—is we’ll create models that have one purpose: advocating on our behalf 24/7. 
  * We’ll shape an AI persona to be a friend to us (or a service will pick a persona for us) that knows us inside and out 
  * It’ll know us because it’ll have access to our self-Model created in step 2. Maybe they’ll be the same model. Who knows 
  * And from there it will advocate for us by regularly checking the current state of the world around us (our location, the last time we ate, whether we’re in conversation or not, if we have upcoming meetings, a big date tonight, etc.) 


Another MJ interpretation
  * It’ll do things for us. It’ll make reservations for us, it’ll request that the channel in the sports bar changes to our favorite sport. Yes, the sports bar has a daemon (API) as well. It’ll ask if you want to order your favorite shorts that just went on sale, etc. 
  * In other words, it’ll never sleep. It’ll read all the world’s APIs looking for things that will help you, collecting the latest deals, news, ideas, etc. and getting them ready for you when you next check the news 
  * Of course you can always just ask it what the latest news is, and it’ll give it to you in your format 
  * 24/7 personal assistant, wielding the world’s APIs on your behalf, based on knowing you better than you know yourself 
  * The final piece is that we will start publishing APIs for ourselves
  * Some people will publish more than others of course, but we’ll be able to define our favorite things, our relationship availability, our profession, and tons of other stuff about us in a daemon that’s available for other daemons to read nearby. 


I used to think the assistant would be on the mobile device, but now with ChatGPT Plugins I wonder if this is just another plugin called from the device. 
  * So when you’re in line at Starbucks your personal assistant will be able to say, the person next to you also thinks Name of The Wind is the best fantasy series, and they’re single. 
  * Maybe your assistant will even be sly and submit to the Starbucks API to pay for their drink, while leaving a note saying, "Name of the Wind is in fact the best, coffee is on me ;)" 
  * I wrote [a shitty book about all of this](https://www.amazon.com/Real-Internet-Things-Daniel-Miessler-ebook/dp/B01NCLUA5T/ref=asap_bc?ie=UTF8&utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world) > in 2016 that you should read if you love these ideas. The ideas are strong—and now starting to happen—but the actual writing is hot garbage 


Written in 2016 the ideas are now starting to happen
## 4. Content authentication
With all this creation we’re going to need to authenticate not just what humans make, but what AIs make as well. 
I talked a bit about this [in 2018](https://danielmiessler.com/blog/the-ability-to-fake-voice-and-video-is-about-to-change-everything/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world&last_resource_guid=Post%3A3e1b76ca-c4c5-4551-aca4-5e005795af1d) >. 
  * Something else that’s going to fall out of all this, that was already starting to happen as a result of 4chan, Reddit, and Twitter, is the need to authenticate content 
  * D/Misinformation is already a problem before perfect deepfakes are possible, but we’re right on the cusp of being unable to easily tell if an image, audio clip, or video is authentic 
  * I think the implementation will likely be digital watermarking using public key cryptography, which is not a new idea 
  * The problem with cryptography is seldom the math. It’s usually in the ease-of-use (PGP) and the key management 
  * But even a bad implementation will be better than nothing (I think?) and even if it’s only implemented by a small percentage of key content creators it’ll still have a positive impact 
  * For example, the White House can sign everything they create. Including their text, their audio, and their videos 
  * Journalists will do the same, which will be copied by serious content creators via the platforms they use to publish, e.g., Twitter, Substack, blogging platforms, podcasting platforms, etc. 


MJ can’t seem to make 6 panes like I asked
  * Creation tools will also have watermarking built into them, where they take in keys and use those keys to sign and mark content produced out of them 
  * These tools will not be foolproof, and they’re notoriously easy to hack because of—you guessed it—key management. Losing and having your private key hacked will in some cases cause more trouble than existed before 
  * So the question will be how often that happens, and how easy it is to invalidate content created with a stolen key while getting a new one 
  * If that’s too hard, it’ll just fail and we’ll go back to the current situation which is trusting the distribution source, i.e., the domain or account you’re getting it from 
  * The added wrinkle here is AI content creation. They’ll be making things too, and we’ll want to know whether a given thing (especially in art) was created by a person or an AI 
  * The real difficult part here is in the jump from the digital to the physical world. It’s fairly easy to watermark something digitally, but it’s not easy to do so in a way that can’t be copied or modified to trick people who don’t look for it 
  * In other words the quality of the control depends on everyone collectively being trained to use the watermarking system to validate things, which seems like a major assumption (see cookie popups for an example of how it could go wrong) 


## 5. Knowledge work replacement
One of the oldest predictions about both AI and robots is that it would take jobs. Well, we f*cked around and now we’re about to find out. 
GPT-4 and ChatGPT Plugins by themselves will crush millions of knowledge-worker jobs. And that’s without a global migration to something like an SPQA architecture that turns most work into natural language into questions and commands. 
Don’t worry there’s much better news in the next section.
It’s going to be nasty. Really nasty. How many jobs will go away? Nobody knows, but it’s probably tens or hundreds of millions. McKinsey has [one of the most cited papers](https://www.mckinsey.com/featured-insights/future-of-work/jobs-lost-jobs-gained-what-the-future-of-work-will-mean-for-jobs-skills-and-wages?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world) > on this and they said 15% of workers, or around 400 million people, back in 2017. But that was a very long time ago, and all these studies need to be redone post ChatGPT, let alone ChatGPT-connected-to-the-internet. 
  * What happens when you connect AI to Jira? Email. Slack. Docs. Calendar. ServiceNow 
  * Salesforce (assuming they survive the hoard of startups coming for them) 
  * Take the average admin’s work, or an analyst, or even a data scientist. Their jobs will very soon be implemented as Plugins, Apps, or APIs connected to company models 


There are essentially three ways to be safe in this world.
  1. Be an SME (senior management, technical, strategy, vision, etc.)
  2. Be a creator of the AI tech
  3. Be a polymath generalist who uses the AI tools to solve problems


So lots of people will still be needed, but not the bottom X percentage of creative/intellectual/technical talent. What’s that percentage? I don’t know, and nobody else does either. But it’s not small. 
And here’s the bad news. As AI gets better it’ll come for those three categories as well. Radiologists are SMEs as well. And Oncologists. But pre-GPT AI is already better than them at many of their jobs. 
MJ goes a bit darker
And at some point AI will be able to write its own plugins, and improve its core functionality. That will likely take a while though. And then you have the generalists, who ironically might last the longest. They’re the ones who need to figure out where all the problems are, and figure out the best tools to use. 
This reminds me of the inverse order of AI job replacement we saw with laborers vs. creatives. We thought it would start with the blue collar types and come for artists last. Nope. It was the opposite. I think something similar could happen here with SMEs, AI Tech Creation, and Implementers. 
## 6. The Creativity Explosion
And now for the craziest one. And the one that gives me the most hope.
What’s about to happen to knowledge workers is going to be bleak. And it’s going to happen so quickly. I used to think we were just screwed, but in the last several weeks I’ve had a new thought that is blowing me away. 
Let me ask you this: what percentage of people are producing creative ideas that are being seen by others and that are good enough to earn them a living? Like, on the planet. 
1%? .5%? .01% I don’t know the number, but it’s extraordinarily small. We’ve got 8 billion people now. How many startups are there? How much music is there? How many Hollywoods are there? How many Taylor Swifts? How many Kendrick Lamars? How many Elons? How many Satya Nadellas? 
Too few. And here’s the important question. Why? Why so few?
Part of the answer is that talent matters, and intelligence matters, and creativity matters. Sure. Agreed. But how many people have similar capabilities to these people but don’t have the time or the tools to do anything with them? 
Again, I don’t know the answer to that, but I’m betting it’s **vast**. Not hundreds of people. Not thousands. Millions. 
Positive Disruption in the form of creativity
But they can’t go to a studio. They can’t talk to their producer friends and get a break. They don’t have an art table to work on. They don’t have a beat machine. 
AI is about to change that. We’re about to remove many of the advantages that Steven Spielberg has over Takashi Noshimira, who lives in a small rural town in Japan, who is a creative genius. With these new models coming out, with the ability to create music, create video, create screenplays, create scripts, etc—we’re about to equalize the playing field massively. 
In short, we’re about to multiply the creative output of planet Earth by hundreds of orders of magnitude. 
We’re about to create new pop stars, new singer-songwriter stars, new top artists, new filmmakers, and even new genres of art. Do you realize how isolated and gatekeeping Hollywood is? I mean you basically have to go there to be successful. That rules out like 99.999% of the planet. Just off the top. Then you have to be beautiful and/or lucky and/or rich and/or connected. And wicked lucky on top. 
Not anymore. Not with the AI that’s coming. With the AI that’s coming we’re going to have competitive marketplaces of anime, pop music, short stories, novels, porn, plays, scientific ideas—fucking **everything**. And AI will be used to discover, rate, and surface the content to the masses. 
So yes, we’re about to have a knowledge-work implosion. But it’ll be followed by a creativity explosion. 
## Final thoughts
Thanks to OpenAI’s punctuated equilibrium, we’re about to have:
  1. Businesses and people being articulated by custom AI models that you can interact with using natural language, using APIs 
  2. AI Assistants that deeply know us through our individual models, and spend every moment of every day looking for ways to shape the world to our preferences 
  3. Somewhere between tens and hundreds of millions of people who cannot do any knowledge work better than an AI 
  4. Somewhere between millions and hundreds of millions of people who can now create code, prose, stories, films, and other types of art that competes the highest levels in a global marketplace 


I choose to be an Analytical Optimist. Positive, but cautious while doing so. 
It’s going to be traumatic, and it’s going to be wonderful. Humans weren’t supposed to be punching a clock at a desk job or a factory anyway. 
I hope this has given you something to think about, and if you want to discuss, feel free to reach out. >
### Notes
  1. I stayed away from AGI and superintelligence in this piece because it’s a topic of its own and it kind of breaks all realistic prediction possibilities anyway. Once it happens, all bets are off. 
  2. When we add robotics to this mix, it’ll be like adding another exponent to the unpredictability because it’ll then include laborers. 


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2F6-phases-post-gpt-world&title=6%20Phases%20of%20the%20Post-GPT%20World "Share on Hacker News")
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
aibusinesscreativitycybersecurityethicsfuturesocietytechnologytop
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
