<!-- Source: https://danielmiessler.com/blog/our-constraints-on-creativity -->

# Our Constraints on Creativity
A list of different ways we limit ourselves creatively
September 11, 2025
[ #philosophy](https://danielmiessler.com/archives/?tag=philosophy)[ #productivity](https://danielmiessler.com/archives/?tag=productivity)[ #society](https://danielmiessler.com/archives/?tag=society)
 Confusion-matrix-reading…
Breaking free from constraints on creativity  
There are multiple constraints that limit how creative we can be as humans.
Let's talk about each of them and how we can counter them.
# Type 1: Not hearing your inner creativity [​](https://danielmiessler.com/blog/our-constraints-on-creativity#type-1-not-hearing-your-inner-creativity)
What I'll call Type 1 is the inability to access your true, internal self. I discovered this concept while reading ["Letters to a Young Poet"](https://www.amazon.com/Letters-Young-Poet-Rainer-Rilke/dp/0393310396)—a correspondence between a young poet and [Rilke](https://en.wikipedia.org/wiki/Rainer_Maria_Rilke) in the early 1900s. The young poet sought advice about his poetry. Rilke responded by urging him to reconnect with his inner curious child.
> To be solitary as you were when you were a child, when the grownups walked around involved with matters that seemed large and important because they looked so busy and because you didn't understand a thing about what they were doing. Rainer Maria Rilke
Rilke argued that we're most creative as young children—exploring without access to the adult world. Everything is possible. Everything becomes a game, exciting, imaginative. Rilke believed this represents our purest form of creativity.
Mathematica by David Bessis  
I encountered a similar idea again in ["Mathematica"](https://www.amazon.com/Mathematica-Secret-World-Intuition-Curiosity/dp/0300270887), which explains how our understanding of advanced mathematics is completely wrong.
It argues you can't learn higher-level math through memorization or mastering equations. It says Math is imagination-based! And that it requires visualizing how things work and how they connect. This visual understanding isn't secondary— _it's the entire foundation_.
The author says this concept of the inner child, inner curiosity, or pure curiosity is absolutely essential. It's the voice we must rediscover within ourselves if we want to produce meaningful ideas. In Math, but I'd argue in other areas as well (see Rilke)
I can't express to you how much you have to read this book. It is just extraordinary.
# Type 2: External restrictions on your creativity [​](https://danielmiessler.com/blog/our-constraints-on-creativity#type-2-external-restrictions-on-your-creativity)
Type 2 self-restriction is external, and looks a lot like peer pressure or audience capture. And whether you're a creator with an audience or not doesn't matter. What matters are the expectations placed on you.
And the real danger isn't the expectations you recognize— _it's the invisible ones._ Expectations from peers, family, friends, and work.
Nothing is worse than talking to yourself in someone else's voice.
They don't just restrict what you're allowed to write or say. They restrict what you feel comfortable thinking. They limit how you approach problems or conceive solutions. You end up thinking only within the bounds of what's acceptable to those around you. You stop feeling creative. You stop having ideas. All because you've self-limited.
To do your best work, you need both types of freedom. You must separate yourself—go into isolation. A quiet office or library will suffice.
> What is necessary, after all, is only this: solitude, vast inner solitude. To walk inside yourself and meet no one for hours—that is what you must be able to attain. Rainer Maria Rilke
You should try to enter a state of pure, young-minded, unbridled curiosity. True authentic exploration and imagination. That's Type 1 freedom. Imagine it flowing from you, spilling out, uncontrolled. Type 2 freedom means escaping external factors that shape and limit what emerges from you.
Here's the complication, which utterly fascinates me: Excessive Type 2 limitations can actually destroy your Type 1 creativity.
It's as if Type 2 limitations recognize the dangerous ideas lurking within pure, childlike curiosity. They know that unrestricted creativity might produce thoughts that "those people" wouldn't approve of.
# Type 3: The anchoring restriction [​](https://danielmiessler.com/blog/our-constraints-on-creativity#type-3-the-anchoring-restriction)
I just wrote [a new piece about the two primary limitations to creativity](https://danielmiessler.com/blog/two-creativity-barriers). You should check it out. But after finishing it I realized there was a third limitation, which is not even thinking about some options for creating a new solution, or solving a problem, because it was previously impossible.
# The analytics awakening [​](https://danielmiessler.com/blog/our-constraints-on-creativity#the-analytics-awakening)
Let me give you my example from yesterday, while I was working on this newsletter. I was wishing I could get more from Fathom Analytics, which was my web analytics replacement for Google Analytics since it became total shit, and for Chartbeat since they became hundreds of dollars per month.
Chartbeat has always been my favorite web analytics platform. It's gorgeous. It's dynamic. And most importantly—it counts pages that people are reading, not just the initial page load. In other words, it works how it's supposed to.
So yesterday I was looking at my Fathom interface and I'm like wait…could I just replace Chartbeat myself?
It took me about 18 minutes to go from having the thought to having a full Google Analytics / Chartbeat replacement.
# The build [​](https://danielmiessler.com/blog/our-constraints-on-creativity#the-build)
So I made this.
My custom analytics platform showing real-time visitor data  
Oh, and I made a menu bar visual using Swift, which is way better than what I had with Fathom. That took less than minutes.
The 🔥 142 bit  
# The results [​](https://danielmiessler.com/blog/our-constraints-on-creativity#the-results)
So let me be clear. I replaced Google Analytics and Chartbeat in a couple of hours (just visual tweaking after I had the main functionality in less than 20 minutes), and I have **WAY MORE** of my desired features than both of them combined. It's literally better for me in every way.
I now have:
  * **Historical metrics** (which Chartbeat didn't have)
  * **Realtime true metrics** (which Google Analytics didn't have)
  * **A MacOS menubar item** (which neither of them had)
  * **Infinite customization ability**


I just replaced two SaaS apps that I've used for years. And I just kind of casually made it happen while I was reading stories and writing the newsletter.
It took a good amount of skill to Spec Code the thing via prompting (because I understand how the JS had to work, etc.), but Kai then took that and wrote the whole thing for me once he had that.
# Two realizations [​](https://danielmiessler.com/blog/our-constraints-on-creativity#two-realizations)
So, two things:
  1. **Holy crap this is nuts**
  2. **We need to completely reframe what's possible now**


I have literally thought about wanting to replace Chartbeat _hundreds_ of times prior to November of 2022. I just didn't have the time to do all those separate pieces, plus have the UI skills to make it look good. We're talking about:
  * The analytics JavaScript itself
  * The listener services
  * The database
  * The storage of the metrics
  * The queries against the endpoints
  * And then the GUI


18 minutes.
That's how long it took to go from:
> Hey, I wonder if I could make this?
...to it actually working. 18 minutes. And if I weren't working on the newsletter that probably would have been half that.
This is the anchoring restriction has to do with naturally only assuming things can be done the way that we learned them.
It's an inertia problem.
# Type 4: The slack in the rope restriction [​](https://danielmiessler.com/blog/our-constraints-on-creativity#type-4-the-slack-in-the-rope-restriction)
This seems related to the third, but it's sneaky and colossal.
I call it Slack in the Rope.
This is another inertia problem, but much larger in scale.
It's like Type 3, but for society as a whole.
Example: Education.
A lot of people would say that it's obvious that a 4-year education in something like computer science in a 4-year university should not take that long.
They would say that the limitations are societal and institutional, and this is the reason that things are still done the way they are.
We've got ancient textbooks that cost an extraordinary amount of money.
We have most university professors really just guiding people through the textbook, which, as we said already, isn't very good and is quite outdated.
Meanwhile, we have potentially far better content and training available using YouTube videos and AI to create custom curriculums with more examples, tutors available 24/7, etc.
But we still send people to college to learn how to program and build software.
I've heard of a childhood education company that's treating teachers more like mentors and guides and is using highly customized AI-selected course curriculums to teach kids reading and math. Within two years, every single person in the class is in the top 1% of the country.
I believe these types of opportunities are everywhere.
I'm talking about completely re-thinking what is possible from first principles. In finding little tricks that make a huge difference.
A good example of this we've seen in the last few years for advancements in AI.
Many people thought the biggest gains were going to come from hardware, and that all the gains were going to come from the hardware.
I was saying back in 2023 that at first it would come from the hardware, but I thought that it would soon start to be slack in the rope improvements from very small and strange observations.
For example, "chain of thought" reasoning. Having an AI talk through the various steps of a process and sort of self-observe turned out to have extraordinary gains. And there are many other such gains that had to do with simply reorganizing how data was taken in or the order in which data was taken in.
It turns out that many of these advancements combined together make up a significant portion of the progress we've made in AI over the last three years. Not nearly as much of the progress has come from straight hardware improvements as most people thought would be the case in 2023.
# What to do [​](https://danielmiessler.com/blog/our-constraints-on-creativity#what-to-do)
I find this framework liberating, exciting, and challenging. It's—at least to me—a simple framework for improving your creative output.
  1. Improve your access to your inner curiosity
  2. Identify and reduce constrains on expressing it


Some might call this writer's block. Perhaps writer's block is simply a Type 1 limitation. Maybe. Not sure. But what I know for certain is that both limitations obstruct maximum creativity. So I urge you to address both.
I don't have a clear methodology here yet, as I'm just now figuring out this framing. But here's what I'm going to do.
  1. Find ways to isolate yourself from external influences and improve your hearing of your inner voice. Or what [Steven Pressfield](https://stevenpressfield.com/) calls, The Muse.
  2. Once you figure out how to get there, incorporate going to that place into your regular routine.
  3. Then try to pay attention to and enumerate the various limitations from outside and also self-imposed because of the outside that you have against expressing your actual self.
  4. Develop the skill of better identifying these hidden limitations that you give yourself based on the voice of others.


That's all I have for now. I'm sure I will update this later. In the meantime, I wish you luck in your journey to address these obstacles.
#### Notes
  1. There is another type of creativity limitation which is more about execution, related to AI. Basically, I find myself regularly not thinking of a solution that I can now do with AI just because for my entire career I never would've been able to do it myself. I'm trying to get out of the habit of being limited in this way, but it takes real effort.


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Four-constraints-on-creativity&title=Our%20Constraints%20on%20Creativity "Share on Hacker News")
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
philosophyproductivitysociety
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
