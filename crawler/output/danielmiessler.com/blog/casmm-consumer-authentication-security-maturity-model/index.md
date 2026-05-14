<!-- Source: https://danielmiessler.com/blog/casmm-consumer-authentication-security-maturity-model -->

# The Consumer Authentication Strength Maturity Model (CASMM) V6
March 25, 2021
[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #tutorial](https://danielmiessler.com/archives/?tag=tutorial)[ #top](https://danielmiessler.com/archives/?tag=top)
 Critical-hitting…
1 reading now 
If you know anything about internet security then you likely spend _a lot_ of your time helping people improve their password hygiene. 
People like moving up rankings, so let’s use that!
**This page is an attempt to create an easy-to-use,****_visual_****model to help you have that conversation.**
## How to use this model
All models are broken, but some are useful!
The idea is for security-savvy people to help less-knowledgeable users in the following two ways: 
Any improvement is good. Even one step matters.
  1. **Show Them Where They Are** — The first way to use this model is to simply ask the user about their current behavior and show them where that ranks within these 8 Levels. If you show them they’re down at Level 1 or 2, the combination of seeing how low they are in the chart and the color might convey some measure of concern. 
  2. **Show Them How to Move** — Next, show them how to move upwards in the model! 


Most non-savvy internet users live at Levels, 1, 2, and 3. This group gets the most benefit by moving from there to Level 4, which is to get all their major accounts enrolled into a Password Manager like 1Password or LastPass. This means using the password manager to create new, secure passwords, and then changing the passwords for those services. 
Resist the urge to let the Best be the enemy of Better.
The next biggest jump is to go from Level 4 to level 5 or above, which is the transition from Password Only to Multifactor Authentication (MFA). That transition is the most important thing at that stage, so even moving from Level 4 to Level 5 is a major improvement! 
Once at Level 5, the goal should be to get out of Level 5 and into 6, 7, or 8. This is because Level 5 (text/SMS-based MFA) is by far the weakest form of MFA in the model. 
Where one "should" be in this hierarchy depends on your threat model.
Once you get to Level 6 (App-based MFA codes) the main weakness you have is the creation and handling of the MFA codes themselves. This means a code is sent to you somehow, which you must then pass on to the service in order to authenticate. This is **bad** because it still leaves the door open for attackers to steal that token through phishing and vishing (voice-based phishing). 
You can’t phish MFA codes that don’t exist!
In fact, many malware and phishing packages are now including not only fields to capture someone’s username and password, but also their MFA code as well. And if you’re an unsophisticated user, you’re just as likely to give away your MFA code as you are your password. 
This is why the final stage of improvement lies at Levels 7 and 8. At that stage, there are no MFA Codes to steal! At these two levels, MFA authentication takes place transparently in the background, in a cryptographically secure way that never involves the user. And since the user never sees a code, that code cannot be stolen. 
At the final levels, and specifically at Level 8, there is an additional protection in that the authentication requests can only be sent to a specific URL that was registered when the authentication method was established. In other words, if I set up Level 8 authentication (like WebAuthn) with Gmail, then when I authenticate with my FIDO2 token, or my operating system, the authentication in the background can only be sent to Gmail. 
## Summary
  1. CASMM is a visual reference designed to help security-minded people help their less savvy friends, family, and colleagues secure themselves. 
  2. The most security improvement one can get is by moving from any Level 3 and below to using strong, unique passwords managed by a Password Manager (Level 4). 
  3. You get increasingly strong authentication as you move from 4 –> 5 and above, from 5 –> 6 or 7, and then finally from 7 –> 8. 
  4. Don’t skip Step 4. It’s best to make the move to unique, quality passwords stored in a manager before you add 2FA, and then try to move as high as possible within Levels 5-8. 


I hope this helps you or someone you care about!
### Old Versions (Version 5)
In this section we’ll maintain previous versions of the CASMM model to capture how it changes over time. 
### Notes
  1. Mar 13, 2022 — The V6 update draws a stronger line between systems that give a user a code (which is phishable) vs. those that do all the work transparently in the background. This changes Level 7 into an app-based level where no code is given to users, which means no code can be phished. 
  2. Mar 30, 2021 — After more thinking and conversation with many in the security community, I reverted the numbering back to low-to-high instead of high-to-low. This is mostly because pretty much every other similar maturity model does the same. In other words, if there are 5 levels, level 5 is usually the best. Plus, having something be #1 implies that it can’t be improved, so if something better emerges it requires that the entire numbering system be reset rather than simply adding a new tier. Examples: CMMI, ISO, etc. Thanks to Ian L. for best making this point. 
  3. Mar 30, 2021 — Another point to mention about "passwordless" is that if it were truly passwordless throughout the process it would likely be weaker than 2FA in most cases, but what we really mean by passwordless here is "from the perspective of the user at the moment of authenticating to something during the course of a day". In other words, they’ve already fully authenticated to their OS, etc. to be able to use WebAuthN (for example) in the first place, so it’s not truly passwordless in most cases. But it is for the user experience at the time of a standard, daily authentication activity. 
  4. Mar 29, 2021 — After much gnashing of teeth on Twitter, and many nice requests as well, I’ve added a higher tier for passwordless auth using technologies like WebAuthN and FIDO2. I also slightly tweaked the names of some of the boxes to make them shorter and clearer, and fixed an issue with Yubikey incorrectly being in Rank 2. 
  5. Mar 26, 2021 — The response to this has been extraordinary, and a few people have already showed me translations into other languages! Evidently I was right in assuming that most security people have this conversation constantly, and appreciated having some sort of reference. 
  6. Mar 25, 2021 — There are absolutely tangible differences between different "token" types. OTP is not the same as U2F is not the same as something that’s FIDO2 compliant. But for regular users I think it’s ok to combine them all into one that lives at the top of the model. 
  7. Mar 24, 2021 — Thanks to Andrew R. Jamieson for making the suggestion to show what each rank is vulnerable to. 
  8. Mar 24, 2021 — Someone mentioned that there are higher ranks of authentication out there, which I agree with, but this is specifically for everyday users. 
  9. Mar 24, 2021 — We can pronounce the acronym as "Chasm", as in, "Lets see how deep into the chasm you are…" 🙂 
  10. Mar 25, 2021 — At the suggestion of someone on Twitter, I decided to invert the numeric scores for the levels, so 7 is worst and 1 is the best. People were saying progress makes more sense if it’s moving toward #1, and I think I agree. 
  11. I know there’s debate about this, but even with all the recent (Spring 2021) attacks on SMS, I _still_ consider SMS-based 2FA superior to password alone. My reasoning is simply that it requires more work for the attacker in most situations and prevents the most primitive form of credential stuffing—which is the most common type of authentication attack against accounts. 
  12. Thanks to Troy Hunt, Anton Chuvakin, and Tim Dierks for spawning the idea for this. 


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fcasmm-consumer-authentication-security-maturity-model&title=The%20Consumer%20Authentication%20Strength%20Maturity%20Model%20\(CASMM\)%20V6 "Share on Hacker News")
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
cybersecurityinnovationtechnologytutorialtop
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
