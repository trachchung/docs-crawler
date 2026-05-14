<!-- Source: https://danielmiessler.com/blog/ai-agents-api-calling-prompt-injection -->

# OpenAI's November 23' Releases Are a Watershed Moment for Human Creativity—and Prompt Injection
Making it trivial to create and share AI Agents that connect to real-word APIs will have a drastic impact on Information Security
November 12, 2023
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #business](https://danielmiessler.com/archives/?tag=business)[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #future](https://danielmiessler.com/archives/?tag=future)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #technology](https://danielmiessler.com/archives/?tag=technology)
 Glanding-fierce…
AI Agents + API Access + Prompt Injection
So I want to talk real quick about [the recent announcements](https://openai.com/blog/new-models-and-developer-products-announced-at-devday?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=openai-s-november-23-releases-are-a-watershed-moment-for-human-creativity-and-prompt-injection) > from OpenAI.Without hyperbole, I think what they announced represents both the greatest boon for business and the biggest problem for security that we’ve seen injected in a single day in many decades.There were many announcements, and many of them—such as model updates—are wonderful but relatively inert. **But what is not without implication is the unbelievably massive expansion of API calling capabilities**. On this front, they announced two main things: 
  1. Custom GPTs
  2. Assistants


Custom GPT’s are basically a front-end version of assistants. And importantly, they both have the same functionality of being able to call Code Interpreter, browse the web, and call arbitrary APIs. Let me say that again– _they can call any API_. **I’ve been saying for a long time that the #1 threat AI security, from a cyber security standpoint, is AI agents having the ability to call APIs.** What they did yesterday was open that up to the entire world. I just saw an interview with the head of API’s at Zapier, and they are now fully integrated with the new Assistant API, so everything that you can do in Zapier you can now do inside of an assistant.And just to refresh everyone, you can basically do ANYTHING in Zapier. Again, just to be clear, this is extraordinarily awesome for humanity, and for business, and for the economy, and for developers, and for so many people going forward. It was an amazing conference and a fantastic set of announcements.But for us in security, we better get ready.**The amount of prompt injection we’re about to see propagate across the Internet is going to be staggering.**
We are talking about injections on websites being crawled automatically by agents, consumed by the agents, executed by the agents, sent onto other APIs, which then connect to other APIs, which ultimately land on sensitive data back ends. The possibilities for attack just became endless. And again, I’m not saying they shouldn’t have done it. I’m not saying this is bad. I’m just saying as security people, get ready. We're entering a world where everything is about to be parsed by AI Agents that have code execution and action-taking capabilities, and the implications are going to be massive. 
Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-agents-api-calling-prompt-injection&title=OpenAI's%20November%2023'%20Releases%20Are%20a%20Watershed%20Moment%20for%20Human%20Creativity%E2%80%94and%20Prompt%20Injection "Share on Hacker News")
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
aibusinesscybersecurityfutureinnovationtechnology
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
