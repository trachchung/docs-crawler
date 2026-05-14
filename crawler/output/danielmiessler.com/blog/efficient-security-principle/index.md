<!-- Source: https://danielmiessler.com/blog/efficient-security-principle -->

# Efficient Security Principle (ESP)
A way of explaining why security's baseline is so low in places, and why it's so hard to raise
March 26, 2024
[ #business](https://danielmiessler.com/archives/?tag=business)[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #ethics](https://danielmiessler.com/archives/?tag=ethics)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #society](https://danielmiessler.com/archives/?tag=society)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #recommended](https://danielmiessler.com/archives/?tag=recommended)[ #top](https://danielmiessler.com/archives/?tag=top)
 Deep-working…
One of the hardest things about being in information security is the frustration.
The longer you’re in the field the more you’re exposed to ridiculously insecure systems that nobody seems to want to fix. We know how to fix them. We often have the money. And security people are explaining—at maximum volume—exactly how to do it. But it doesn’t happen.
I’d like to propose an explanation and name for this phenomenon—the **Efficient Security Principle (ESP)**.
**The Efficient Security Principle**
  1. The security baseline of an offering or system faces continuous downward pressure from customer excitement about, or reliance on, the offering in question.
  2. The baseline for an offering’s security will be set at the point at which people will not stop using the offering because it’s insecure.
  3. The better the offering is, the lower the security baseline can be without losing customers.


In other words, the way we know something has the "right" amount of security —acceptable, not ethically or morally—is when people **just keep using it**. There are countless examples.
  * Online companies, when they get hacked constantly
  * Email use at companies, when it’s the #1 way to get compromised
  * Online banking, when fraud is constant
  * Front door locks, when they’re trivial to pick
  * The internet in general, when we know it’s an open wound


**We use these things anyway because the value they provide massively outweighs the security risks in our minds.**
The moment enough people stop using something due to security being too bad, the baseline goes up. And not before.
This dynamic explains a phenomenon I wrote about in 2018: [why software remains insecure](https://danielmiessler.com/blog/the-reason-software-remains-insecure) despite decades of security improvements. The fundamental reason isn't lack of knowledge, tools, or expertise—it's that insecure software continues to provide so much value to society that we collectively tolerate the risks. Security only improves when the pain of insecurity finally exceeds the benefits of the vulnerable systems.
## How to use this principle [​](https://danielmiessler.com/blog/efficient-security-principle#how-to-use-this-principle)
**If You’re a Technical Security Expert**
Security experts often believe the level of security for a given system is much lower than it should be. Which makes sense. We’re close to it. We see the depth of the problems. And we know how to make it better.
_Recommendation_**:** Realize that it’s not about us as technical security experts. Realize that it’s about the bigger system, which is primarily concerned with the functionality they’re getting from an offering, not with its security risks. If people in general know the risk and they’re still taking it, that’s just because they value the offering that much. Don’t take it personally.
**If You’re a Security Leader**
Even security leaders within large organizations can become disillusioned because they don’t see their programs being taken seriously. Just like the technical implementers, they know how to improve security and they can get quite upset when nobody is listening.
_Recommendation_**:** First, make sure the baseline is actually where people think it is. If there are security gaps that the company—or its users—don’t know about, make those visible to close the gap of knowledge and get additional support. Second, find innovative ways to raise the baseline in a way that doesn’t inconvenience the company or its users. They may not want to spend much extra effort to raise the baseline, but they won’t object if it goes up without effort on their part.
# Summary [​](https://danielmiessler.com/blog/efficient-security-principle#summary)
  1. The Efficient Security Principle says that security is only as good as it needs to be to keep people from abandoning the service, and that the more popular or essential the offering, the lower the security can be.
  2. Progress is still possible—especially through policy change and regulation—but it mostly comes gradually, at glacial speeds, or in fast jumps from major incidents. But security experts loudly calling out how low the baseline is, and gesturing wildly towards the solution, seldom results in change.
  3. Passionate security experts struggling with low security baselines should absorb this truth so their mental health and job satisfaction don’t suffer unnecessarily.


#### Notes
  1. Thanks to Saša Zdjelar and Clint Gibler for their insights while talking through some of these ideas with me, and Saša for the email example.
  2. The principle applies most to very large systems, like the internet, or the overall security of a massive publicly-traded company, not granular or small-scale mechanisms.
  3. There is a natural, glacial upgrade of all security just generally as a result of technical improvement, and within companies that are working on it diligently. If it’s invisible enough, the change can come naturally in a way that doesn’t bother users, which is technically a lifting of the baseline. But it’s so gradual that it doesn’t really apply to a given point of time when someone is wondering why security isn’t better.
  4. Saša Zdjelar points out that SMS is a good example of where the danger became too great and a global push happened to phase it out in a relatively short amount of time.
  5. There are also Security Blindspots where security experts know something that the public doesn’t. So they’re using the offering now, but if they knew how bad it really was, they might not. That’s a special case that doesn’t apply here. This principle deals with the situation where the functionality is deemed more important with full knowledge, not with situations where knowledge is unavailable or withheld.
  6. This principle evolved from a similar essay I wrote in 2018 called [_Why Software Remains Insecure_](https://danielmiessler.com/blog/the-reason-software-remains-insecure), where I argued that software remains vulnerable because "the benefits created by insecure products far outweigh the downsides." The ESP formalizes this observation into a broader principle that applies beyond just software.
  7. Pardon the formal, "I’m so smart" tone of the piece. I’m trying to make it evergreen, and thus remove having too much hesitation and throat clearing and personality from it. It’s really still just a capture of a Frame of thinking that I find useful, and I’ll continue to upgrade it as I see opportunities for improvement.


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fefficient-security-principle&title=Efficient%20Security%20Principle%20\(ESP\) "Share on Hacker News")
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
businesscybersecurityethicsinnovationsocietytechnologyrecommendedtop
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
