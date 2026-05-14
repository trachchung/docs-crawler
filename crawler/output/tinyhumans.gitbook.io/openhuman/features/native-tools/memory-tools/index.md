<!-- Source: https://tinyhumans.gitbook.io/openhuman/features/native-tools/memory-tools -->

The is OpenHuman's knowledge base. The memory tools are how the agent talks to it during a conversation.
## 
Tools in the family
Tool
What it does
`recall`
Search the Memory Tree by query - source-scoped, topic-scoped, or global. Returns chunks with provenance.
`store`
Write a new memory the agent decided is worth keeping (a fact, a preference, a piece of context).
`forget`
Remove a memory by ID - used when something is wrong, stale, or the user explicitly asks to forget it.
There is also a tree-aware retrieval surface (drill down a topic, fetch the global digest for a day) - the agent picks the right one based on the question.
## 
Why these are tools, not implicit context
The Memory Tree is too big to dump into every conversation. The tools let the model _ask_ - "what do I know about Alice?", "what happened yesterday?", "remind me of last week's Stripe webhook" - and the retrieval layer returns just the relevant chunks, with provenance back to the source file in your Obsidian vault.
## 
See also
  * - what these tools read from and write to.
  * - how the tree gets populated in the first place.


[PreviousVoicechevron-left](https://tinyhumans.gitbook.io/openhuman/features/native-tools/voice)[NextTool-Scoped Memorychevron-right](https://tinyhumans.gitbook.io/openhuman/features/native-tools/tool-memory)
Last updated 4 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://tinyhumans.ai/privacy).
close
AcceptReject
