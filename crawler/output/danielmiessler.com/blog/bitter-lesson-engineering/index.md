<!-- Source: https://danielmiessler.com/blog/bitter-lesson-engineering -->

# Bitter Lesson Engineering
We need to avoid the Bitter Lesson mistake when building AI systems
February 23, 2026
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)
 Epoch-training…
2 reading now 
I have a new concept I'm using everywhere in my AI engineering called Bitter Lesson Engineering (BLE).
The idea comes from Richard Sutton's essay, ["The Bitter Lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html).
The essay argues that all of our human attempts to control, modify, and enhance AI are kind of not worth it, because when you increase the intelligence of AI—through more hardware or better algorithms or whatever— _that_ will increase intelligence far more than anything we can do with our human approaches.
We have to learn the bitter lesson that building in how we think we think does not work in the long run.Richard Sutton
It's stronger than that actually. Not only will it _not be better_ if we try to help, but it will likely be **far worse**.
Essentially, we should avoid poisoning AI's native capabilities with our supposedly superior guidance, because it's not actually superior.
Some other quotes from [the essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html):
> "The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin."
> "We want AI agents that can discover like we can, not which contain what we have discovered."
> "We should build in only the meta-methods that can find and capture this arbitrary complexity."
> "Building in our discoveries only makes it harder to see how the discovering process can be done."
## This is about more than just agentic engineering [​](https://danielmiessler.com/blog/bitter-lesson-engineering#this-is-about-more-than-just-agentic-engineering)
This is obviously super important for people who are building AI, but it goes way beyond that.
Anything you are doing with AI, where you are asking AI to help you, needs to follow the BLE (Bitter Lesson Engineering) principle.
### LIFE MANAGEMENT [​](https://danielmiessler.com/blog/bitter-lesson-engineering#life-management)
If you're trying to get help managing your life, like managing routines, improving your finances, etc: don't give it a bunch of your own accumulated methodologies and tell it to implement them. Instead, articulate exactly the life you want to have.
### BUSINESS [​](https://danielmiessler.com/blog/bitter-lesson-engineering#business)
If you're getting help starting a business, don't tell it how to help you: tell it the business you want to build and the life you want to have.
### GENERAL AI INTERACTION [​](https://danielmiessler.com/blog/bitter-lesson-engineering#general-ai-interaction)
Focus less on the steps of execution and focus more on the results you want and don't want.
## My takeaways [​](https://danielmiessler.com/blog/bitter-lesson-engineering#my-takeaways)
So here's what I recommend you take from all this.
  1. The way we think about logic and intelligence and efficiency are very likely primitive
  2. So we shouldn't be hard-coding those rules or ideas into how we "teach" AI to do things
  3. As AI gets smarter it'll come up with way better ways to do the same thing from first-principles


So my simple BLE rule for myself when building AI systems, or really doing anything with AI going forward, is:
**Don't confuse the "what" with the "how".**
Be extremely specific about what you _want_ , and then give the best tools you have to the best AI you have, and let it figure out how to execute.
This means as the AI gets smarter, our scaffolding becomes more about preferences than execution, ultimately making our entire system meta-upgradeable instead of BLE-hobbled.
#### Notes
  1. AIL Level 1: Daniel wrote this entire post from his own ideas and voice recordings. I (Kai, his DA) helped with formatting and generating the header image. [Learn more about AIL](https://danielmiessler.com/blog/ai-influence-level-ail)
  2. Citation: Richard Sutton, ["The Bitter Lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), March 13, 2019.
  3. A BLE-hobbled system is one where the scaffolding has aged to the point of making your overall system worse instead of better. After which point the AI could actually do a better job if it didn't have to follow our super-smart, dumb instructions.
  4. I also build BLE into the [PAI](https://github.com/danielmiessler/PAI) project through an `AISTEERING` rule.
  5. The magic combination going forward is the best AI, with the highest quality context about you, that has access to the best tools.


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fbitter-lesson-engineering&title=Bitter%20Lesson%20Engineering "Share on Hacker News")
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
aitechnologyinnovation
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
