<!-- Source: https://danielmiessler.com/blog/why-i-think-karpathy-is-wrong-on-the-agi-timeline -->

# Why I Think Karpathy is Wrong on the AGI Timeline
It's not about LLMs, it's about AI systems
October 20, 2025
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #agi](https://danielmiessler.com/archives/?tag=agi)[ #future](https://danielmiessler.com/archives/?tag=future)[ #technology](https://danielmiessler.com/archives/?tag=technology)
 Morpheus-believing…
2 reading now 
[Andrej Karpathy came on Dwarkesh's podcast](https://youtu.be/lXUZvyajciY) recently, and I have a number of thoughts.
# The wrong definition of AGI (in my opinion) [​](https://danielmiessler.com/blog/why-i-think-karpathy-is-wrong-on-the-agi-timeline#the-wrong-definition-of-agi-in-my-opinion)
Many are saying that Karpathy thinks AGI is 10 years away, and therefore Gary Marcus is right, and people like myself, Sholto, and all the other people saying AGI is within a few years have just lost the war.
Compelling, but it's not that simple.
Debates like these usually hinge on definitions, and the definition that Karpathy is using came from when he was back at OpenAI:
An AI that can do any economically valuable work as good or better than a human.The OpenAI / Karpathy Definition of AGI
 _I don't think this is the best definition to use at this moment._
I think it's a good _pure_ definition, or _Computer Science_ definition, but I think we should focus our definition more around the thing that matters most to humans (as opposed to AI people).
I'm worried—as Karpathy and Dwarkesh are as well—about human work replacement. Specifically human knowledge work. And that's why I've been using this definition since 2023:
An AI system that can replace an average knowledge worker.
For me, this is better for two reasons:
  1. It focuses on the fact that it's an AI _system_ , and not one particular component of a system (like a model)
  2. It provides a more direct benchmark for the thing we care about, i.e., Are companies actually replacing workers with this system? Yes or no?


The system part is key.
# Why does "system" vs. LLM matter? [​](https://danielmiessler.com/blog/why-i-think-karpathy-is-wrong-on-the-agi-timeline#why-does-system-vs-llm-matter)
I have no reason—or ability—to disagree with Karpathy on the limitations of pure LLMs. He recently wrote _yet another one_ in 1,000 lines of code. He's the actual sensei here, and I know .00017% of what he knows about LLMs. The problem is AI systems aren't just the LLMs themselves. They're not naked neural nets.
When you go to chatgpt.com and talk with `gpt-5` you're not talking to a base neural net; you're talking to _an AI system_.
You're talking to the result of that initial LLM being shaped and molded with colossal amounts of extra scaffolding and engineering work to be the best possible **system** it can be for doing its particular task. Being a chatbot/assistant, in its case.
This distinction is everything because replacing human jobs will also be done through composite, stitched-together systems that are many times more powerful than their parts.
To replace a project manager or an executive assistant, the companies building human worker replacement aren't going to sit back and wait for GPT-9 or Gemini 7.5.
Human worker replacement will happen through AI products/systems that _work around_ the pure limitations of LLMs and of individual model intelligence.
[Claude Code](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) is a brilliant example of this.
Just soccer pitching numbers, Claude Code—when it launched—was like 5x better than Opus or Sonnet at helping developers write code.
Well it's less than 10 months later and it's gotten _many times better than that_ already.
Like night and day.
Yes, the models got better, but that's not what made the difference. It was [constant iterative improvements](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) grinding towards improving how the AI talks to itself. Coordination. Context Management / Engineering. And just now they added skills, which takes the whole thing to 11-million.
This is exactly the type of efficiency ratchet that will apply to human work replacement. Where we don't have enough context window to read all the company's docs, companies will/have invented systems to do that.
Where they're not general enough to match human flexibility, they'll add so many great use cases and capabilities—based roughly around the Agent Skills paradigm—that we eventually won't notice because it'll cover most.
# Good enough to replace a bad worker is a low standard, and it's not improving [​](https://danielmiessler.com/blog/why-i-think-karpathy-is-wrong-on-the-agi-timeline#good-enough-to-replace-a-bad-worker-is-a-low-standard-and-it-s-not-improving)
The part that concerns me the most about the speed of progress towards AI replacing human knowledge workers is not the speed of AI system improvement. It's the fact that the bar is so low.
A good portion of our culture's comedy is based on the utter incompetence of like half of our workforce.
  * The worst possible customer service
  * People bragging about how little work they do
  * Making a sport out of doing the bare minimum
  * People absolutely detesting their jobs
  * Even decent workers just mindlessly punching in and out


Mediocrity is the baseline. Almost by definition.
**That** is what a multi-billion dollar human worker replacement startups are competing with—not the top 10% performers you know.
Think of it this way: In the time that we went from Claude Code not existing, to it getting really good, to it now having shareable work task replacement skills, the bottom 50% of knowledge workers improved how much?
Zero.
In the time since ChatGPT came out, the bottom 50% of knowledge workers improved their capabilities by how much?
Again, 0%.
The bar for human work replacement is not moving, while the capabilities of AI Systems are going absolutely apeshit.
# But wait, that's just for the bottom 50%, right? [​](https://danielmiessler.com/blog/why-i-think-karpathy-is-wrong-on-the-agi-timeline#but-wait-that-s-just-for-the-bottom-50-right)
You might push back by saying this is only for the people not trying very hard, or who aren't that smart or whatever.
I largely agree with you, but it doesn't matter.
You and me and Dwarkesh and Karpathy are going to be fine. So what?
If AI _only_ eats the absolute worst, bottom 50% of knowledge workers in the next 5-10 years, [we're still talking about hundreds of millions of jobs](https://www.google.com/search?q=how+many+knowlege+workers+in+the+world%3F&oq=how+many+knowlege+workers+in+the+world%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyBwgEEAAY7wUyBwgFEAAY7wUyCggGEAAYogQYiQXSAQg5NTAzajBqNKgCALACAA&sourceid=chrome&ie=UTF-8).
This is why I disagree with Karpathy on this.
It's not because he's wrong. He's not. But he's focused on the wrong thing.
If the thing we care about is AI's near-term and practical impact on humanity, the thing to watch is not how smart individual models are, or the specific technical limitations of RL to achieving continuous learning.
_It's the**trillions** of dollars being invested in replacing the static worst 50% of human workers._
Those trillions are being spent on having the Worker Replacement System be _just general enough_ to hit that mark.
So my question to you is, given what we see in model improvement and systems like Claude Code that exponentially magnify model capability, do you really want to bet against that happening?
I don't.
And this is why I think "AGI" will be here before 2028. Not because all the stuff Karpathy is talking about will be solved, but because it won't matter if they are.
#### Notes
  1. Another example is when [Sholto](https://youtu.be/FQy4YMYFLsI) was like, our AI pipelines for improving AI and doing AI work, doing AI research are all extremely crappy. They're all basically duct tape and string and silly putty. And almost every part of the process can be improved (paraphrased).
  2. This is part of my greater point I've been talking about since early 2023, which I call "slack in the rope." There are a thousand different ways that could be improved that all make up the composite result of an improvement to the overall system. The issue is, we don't know how much improvement exists in each of those thousand, but oftentimes they're multiplicative!
  3. So it could be that (indulge me) in pipeline number 37/1000, we're going to go from 13% efficiency to 14% efficiency over the next two years. It's not going to do much of anything. And you multiply that by all the other systems, no big deal. But it could be that in pipeline number 349/1000, we're actually going to go from 12% efficiency to 87% efficiency from some random trick that some researcher found and posted on the internet and now all the big labs are doing it. And suddenly our overall AI capabilities explode.
  4. Oh and by the way, I thought Karpathy was just brilliant on the podcast. My favorite idea from this was how we need to inject entropy into our lives, especially as we age. Because the same way that models collapse, old people do as well. Just really love that. My second favorite idea was the fact that evolution codes not only neural net weights into DNA but it uses compression to code the machine that builds the neural net weights in a larger brain. 🧠💥


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fwhy-i-think-karpathy-is-wrong-on-the-agi-timeline&title=Why%20I%20Think%20Karpathy%20is%20Wrong%20on%20the%20AGI%20Timeline "Share on Hacker News")
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
aiagifuturetechnology
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
