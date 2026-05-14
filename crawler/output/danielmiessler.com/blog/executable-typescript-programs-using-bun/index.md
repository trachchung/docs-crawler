<!-- Source: https://danielmiessler.com/blog/executable-typescript-programs-using-bun -->

# Self-Contained TypeScript Programs Using Bun
How Bun's auto-install makes TypeScript even better than Python's uv
July 27, 2025
Bun installing dependencies automatically  
Roughly 23-319% of the time, when I run a Python app, it doesn't work because of dependencies, and I end up trying to figure out which of my 17 real and virtual Python environments are actually active.
Using `uv` for everything is way better, but since I'm kind of moving my entire programming world to TypeScript, I'm now using `bun`'s auto-install feature instead. And it's actually a bit better.
## Different Approaches, Same Goal [​](https://danielmiessler.com/blog/executable-typescript-programs-using-bun#different-approaches-same-goal)
Python's `uv` and Bun both solve the "self-contained app" problem by putting the requirements inside the program itself, but they do it in different ways...
### UV's Approach: Inline Comments (smuggling, basically) [​](https://danielmiessler.com/blog/executable-typescript-programs-using-bun#uv-s-approach-inline-comments-smuggling-basically)
Python uses special magical comments to declare dependencies:
python
```
# /// script
# dependencies = ["requests", "rich"]
# ///

import requests
# script continues...
```

123456
It works great, but it feels super hack-y to me.
It feels like we're smuggling in a dependency payload to trick Python into actually working for once.
It feels like we're smuggling in a ~~prompt injection~~ dependency payload to trick Python into actually working for once.
I like `bun`'s approach _much_ better. It just writes the imports out like it's not embarrassed by them!
typescript
```
#!/usr/bin/env bun

// Just import what you need - Bun auto-installs!
import axios from 'axios';
import chalk from 'chalk';

console.log(chalk.cyan.bold('\n🚀 Bun Auto-Install Demo\n'));

// Fetch a random joke
try {
  console.log(chalk.yellow('Getting a random joke...'));
  const jokeResponse = await axios.get('https://official-joke-api.appspot.com/random_joke');
  const joke = jokeResponse.data;
  console.log(chalk.green(`\n${joke.setup}`));
  console.log(chalk.blue(`${joke.punchline} 😄\n`));
} catch (error) {
  console.log(chalk.red('Failed to fetch joke\n'));

v// Fetch a random activity
try {
  console.log(chalk.yellow('Finding something to do...'));
  const activityResponse = await axios.get('https://bored-api.appbrewery.com/random');
  const activity = activityResponse.data;
  console.log(chalk.magenta(`Activity: ${activity.activity}`));
  console.log(chalk.dim(`Type: ${activity.type} | Participants: ${activity.participants}\n`));
} catch (error) {
  console.log(chalk.red('Failed to fetch activity\n'));


// Show a random number to prove it runs fresh
const randomNum = Math.floor(Math.random() * 1000);
console.log(chalk.green(`Random number: ${randomNum}`));

// Show that this runs fresh each time
console.log(chalk.dim('\nRun again for different results!'));
console.log(chalk.dim('No package.json or npm install needed 🎉\n'));
```

123456789101112131415161718192021222324252627282930313233343536
## Running the Script [​](https://danielmiessler.com/blog/executable-typescript-programs-using-bun#running-the-script)
bash
```
# Make it executable
chmod +x test.ts

# Run it directly - dependencies auto-install!
./test.ts

# Or just use bun
bun test.ts
```

12345678
The first time you run the script, `bun` automatically:
  1. Detects the missing packages
  2. Downloads and installs them
  3. Caches them for future runs
  4. Executes your script


No `npm install`, no `package.json`, no setup—just run it.
## Example Output [​](https://danielmiessler.com/blog/executable-typescript-programs-using-bun#example-output)

```
🚀 Bun Auto-Install Demo

Getting a random joke...

Did you watch the new comic book movie?
It was very graphic! 😄

Finding something to do...
Activity: Explore a park you have never been to before
Type: recreational | Participants: 1

Random number: 294

Run again for different results!
No package.json or npm install needed 🎉
```

123456789101112131415
Oh, and it's nuclear fast.

```
bun test.ts  0.08s user 0.06s system 29% cpu 0.469 total
```

## My takeaway [​](https://danielmiessler.com/blog/executable-typescript-programs-using-bun#my-takeaway)
This goes to a larger discussion around Python vs TypeScript, but I feel like this is another example where the latter is just a more natural, modern way of doing things.
_TypeScript all the things._
#### Notes
  1. Shoutout to Greg for getting me into the TypeScript cult.


#### Notes
  1. Shoutout to Greg for getting me into the TypeScript cult.


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fexecutable-typescript-programs-using-bun&title=Self-Contained%20TypeScript%20Programs%20Using%20Bun "Share on Hacker News")
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
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
