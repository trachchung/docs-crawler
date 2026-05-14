<!-- Source: https://danielmiessler.com/blog/using-the-smartest-ai-to-rate-other-ai -->

# Using the Smartest AI to Rate Other AI
A Fabric Pattern that assesses how well a given model does on a task relative to humans
November 12, 2024
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #productivity](https://danielmiessler.com/archives/?tag=productivity)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #writing](https://danielmiessler.com/archives/?tag=writing)
 Of-course-still-loving-you…
1 reading now 
The structure of the rate_ai_result Stitch
Since early 2023 I’ve wanted a system that can assess how well AI does at a given task. 
And when I say "system", what I really mean is an AI system. Which means I want an AI system that rates AI systems. There are a bunch of these out there now, as well as a number of AI output eval frameworks that are somewhat useful. 
But I wanted a simpler architecture that uses high-quality prompting to do the work. In other words, what could I give **a smart, Judging AI** as instructions such that it can evaluate the sophistication of**less smart, to-be-tested** AI? So here’s the structure I used. 
A typical result of the assessment
  1. I created a [Fabric](https://github.com/danielmiessler/fabric?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=using-the-smartest-ai-to-rate-other-ai&_bhlid=58cafacd5dc5d657e9fe51fb70d100e4c426a2f9) > Pattern called `rate_ai_result` which is used by the smartest AI available (the Judging AI). In this case, I’m using `o1-preview`. [THE PATTERN](https://github.com/danielmiessler/fabric/blob/main/patterns/rate_ai_result/system.md?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=using-the-smartest-ai-to-rate-other-ai&_bhlid=823aaadfc88fb548fbeaa367649887d514adb947) >
  2. Craft a Stitch (piped Patterns working together) that collects all the components together to send to the Judging AI. 
  3. The components are:
a. The input that the first AI will do its work onb. The instructions for the first AI on how to perform the taskc. The output of the AI’s work 
  4. Those are then sent to the Judging AI using a single command.
`(echo "beginning of content input" ; f -u https://danielmiessler.com/blog/framing-is-everything ; echo "end ofcontent input"; echo "beginning of AI instructions (prompt)"; cat ~/.config/fabric/patterns/extract_insights/system.md; echo "end of AI instructions (prompt)" ; echo "beginning of AI output" ; f -u https://danielmiessler.com/blog/framing-is-everything | f -p extract_insights -m gpt-3.5-turbo ; echo "end of AI output. Now you should have all three." ) | f -rp rate_ai_result -m o1-preview-2024-09-12`
  5. In this command, we’re pulling the content of a webpage, pulling the content of the AI instructions (the prompt/Pattern), and then pulling the results of the AI doing the task using `gpt-3.5-turbo`. 
  6. That is all then sent to the `rate_ai_result` Pattern using `o1-preview`. 


The command from Step 4.
## The `rate_ai_result` Pattern
The setup is simple enough, but most of the magic is in the rating pattern itself. 
What I’m having it do is think deeply about how to assess the quality of how the task was done—given the fact that it has the input, the prompt, and the output—relative to various human levels. Here are the steps within the Pattern/prompt. 
A snippet of the rate_ai_result Pattern (click through for full pattern) 
We also told it to rate the quality of the AI’s work across over 16,000 dimensions. We also gave it multiple considerations to use as seed examples of analysis types (which reminds me a lot of Attention, actually). 
Hints to o1 on how to build its own multi-dimensional rating system
This is one of my experimental techniques that I’ve been playing with in my prompts, and we need to understand that tricks like this could range from highly effective, to completely useless, to even counter-productive. I intend to test that more soon using eval frameworks, or wait until the platforms do it themselves. But if any model so far might be able to use such trickery, it’s `o1`. 
Anyway, here’s the result that came back: **Bachelor’s Level**.
GPT 3.5 Turbo got a rating of Bachelor’s Level
After hacking on this for a few hours this weekend I am happy to report something. 
**I’ve got this thing predictably scoring the sophistication of various models on the human scale—across multiple types of task.**
In other words, GPT-3.5 is scoring as High School or Bachelor’s level—predictably—doing [lots of different AI tasks](https://github.com/danielmiessler/fabric?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=using-the-smartest-ai-to-rate-other-ai&_bhlid=e2a86b382da3307a297463b39e5bf127a025d8d9) >. So, 
  * Threat Modeling
  * Finding Vulnerabilities
  * Writing
  * Summarization
  * Contract Reviews
  * Etc.


…while GPT-4o and Opus score way higher—and o1 scores the highest! Again, across various tasks and multiple runs. 
_That’s insane._
It means—as kludgy as this first version is—we have a basic system for judging the "intelligence" of an AI system relative to humans. And I’m pretty sure I can make this thing way better with just a bit of work. 
What’s coolest to me about it is that it’s a framework. When the new best model comes out, that becomes the judge. And when new models come out we want to test for particular tasks (like tiny models optimized for a particular thing), we can just plug them in. Plus we can keep optimizing the `rate_ai_result` pattern itself. 
Anyway, just wanted to share this so people can attack it, improve it, and build with it. 
Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fusing-the-smartest-ai-to-rate-other-ai&title=Using%20the%20Smartest%20AI%20to%20Rate%20Other%20AI "Share on Hacker News")
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
aicybersecurityinnovationproductivitytechnologywriting
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
