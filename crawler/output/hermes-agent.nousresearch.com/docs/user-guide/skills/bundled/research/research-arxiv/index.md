<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#__docusaurus_skipToContent_fallback)
On this page
Search arXiv papers by keyword, author, category, or ID.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#skill-metadata "Direct link to Skill metadata")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/research/arxiv`  |  
| Version  | `1.0.0`  |  
| Author  | Hermes Agent  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `Research`, `Arxiv`, `Papers`, `Academic`, `Science`, `API`  |  
| Related skills  | [`ocr-and-documents`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-ocr-and-documents)  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# arXiv Research
Search and retrieve academic papers from arXiv via their free REST API. No API key, no dependencies — just curl.
## Quick Reference[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#quick-reference "Direct link to Quick Reference")  
| Action  | Command  |  
| --- | --- |  
| Search papers  | `curl "https://export.arxiv.org/api/query?search_query=all:QUERY&max_results=5"`  |  
| Get specific paper  | `curl "https://export.arxiv.org/api/query?id_list=2402.03300"`  |  
| Read abstract (web)  | `web_extract(urls=["https://arxiv.org/abs/2402.03300"])`  |  
| Read full paper (PDF)  | `web_extract(urls=["https://arxiv.org/pdf/2402.03300"])`  |  
## Searching Papers[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#searching-papers "Direct link to Searching Papers")
The API returns Atom XML. Parse with `grep`/`sed` or pipe through `python3` for clean output.
### Basic search[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#basic-search "Direct link to Basic search")

```
curl-s"https://export.arxiv.org/api/query?search_query=all:GRPO+reinforcement+learning&max_results=5"
```

### Clean output (parse XML to readable format)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#clean-output-parse-xml-to-readable-format "Direct link to Clean output \(parse XML to readable format\)")

```
curl-s"https://export.arxiv.org/api/query?search_query=all:GRPO+reinforcement+learning&max_results=5&sortBy=submittedDate&sortOrder=descending"| python3 -c"import sys, xml.etree.ElementTree as ETns = {'a': 'http://www.w3.org/2005/Atom'}root = ET.parse(sys.stdin).getroot()for i, entry in enumerate(root.findall('a:entry', ns)):    title = entry.find('a:title', ns).text.strip().replace('\n', ' ')    arxiv_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]    published = entry.find('a:published', ns).text[:10]    authors = ', '.join(a.find('a:name', ns).text for a in entry.findall('a:author', ns))    summary = entry.find('a:summary', ns).text.strip()[:200]    cats = ', '.join(c.get('term') for c in entry.findall('a:category', ns))    print(f'{i+1}. [{arxiv_id}] {title}')    print(f'   Authors: {authors}')    print(f'   Published: {published} | Categories: {cats}')    print(f'   Abstract: {summary}...')    print(f'   PDF: https://arxiv.org/pdf/{arxiv_id}')    print()
```

## Search Query Syntax[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#search-query-syntax "Direct link to Search Query Syntax")  
| Prefix  | Searches  | Example  |  
| --- | --- | --- |  
| `all:`  | All fields  | `all:transformer+attention`  |  
| `ti:`  | Title  | `ti:large+language+models`  |  
| `au:`  | Author  | `au:vaswani`  |  
| `abs:`  | Abstract  | `abs:reinforcement+learning`  |  
| `cat:`  | Category  | `cat:cs.AI`  |  
| `co:`  | Comment  | `co:accepted+NeurIPS`  |  
### Boolean operators[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#boolean-operators "Direct link to Boolean operators")

```
# AND (default when using +)search_query=all:transformer+attention# ORsearch_query=all:GPT+OR+all:BERT# AND NOTsearch_query=all:language+model+ANDNOT+all:vision# Exact phrasesearch_query=ti:"chain+of+thought"# Combinedsearch_query=au:hinton+AND+cat:cs.LG
```

## Sort and Pagination[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#sort-and-pagination "Direct link to Sort and Pagination")  
| Parameter  | Options  |  
| --- | --- |  
| `sortBy`  |  `relevance`, `lastUpdatedDate`, `submittedDate`  |  
| `sortOrder`  |  `ascending`, `descending`  |  
| `start`  | Result offset (0-based)  |  
| `max_results`  | Number of results (default 10, max 30000)  |  

```
# Latest 10 papers in cs.AIcurl-s"https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=10"
```

## Fetching Specific Papers[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#fetching-specific-papers "Direct link to Fetching Specific Papers")

```
# By arXiv IDcurl-s"https://export.arxiv.org/api/query?id_list=2402.03300"# Multiple paperscurl-s"https://export.arxiv.org/api/query?id_list=2402.03300,2401.12345,2403.00001"
```

## BibTeX Generation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#bibtex-generation "Direct link to BibTeX Generation")
After fetching metadata for a paper, generate a BibTeX entry:
{% raw %}

```
curl-s"https://export.arxiv.org/api/query?id_list=1706.03762"| python3 -c"import sys, xml.etree.ElementTree as ETns = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}root = ET.parse(sys.stdin).getroot()entry = root.find('a:entry', ns)if entry is None: sys.exit('Paper not found')title = entry.find('a:title', ns).text.strip().replace('\n', ' ')authors = ' and '.join(a.find('a:name', ns).text for a in entry.findall('a:author', ns))year = entry.find('a:published', ns).text[:4]raw_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]cat = entry.find('arxiv:primary_category', ns)primary = cat.get('term') if cat is not None else 'cs.LG'last_name = entry.find('a:author', ns).find('a:name', ns).text.split()[-1]print(f'@article{{{last_name}{year}_{raw_id.replace(\".\", \"\")},')print(f'  title     = {{{title}}},')print(f'  author    = {{{authors}}},')print(f'  year      = {{{year}}},')print(f'  eprint    = {{{raw_id}}},')print(f'  archivePrefix = {{arXiv}},')print(f'  primaryClass  = {{{primary}}},')print(f'  url       = {{https://arxiv.org/abs/{raw_id}}}')print('}')
```

{% endraw %}
## Reading Paper Content[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#reading-paper-content "Direct link to Reading Paper Content")
After finding a paper, read it:

```
# Abstract page (fast, metadata + abstract)web_extract(urls=["https://arxiv.org/abs/2402.03300"])# Full paper (PDF → markdown via Firecrawl)web_extract(urls=["https://arxiv.org/pdf/2402.03300"])
```

For local PDF processing, see the `ocr-and-documents` skill.
## Common Categories[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#common-categories "Direct link to Common Categories")  
| Category  | Field  |  
| --- | --- |  
| `cs.AI`  | Artificial Intelligence  |  
| `cs.CL`  | Computation and Language (NLP)  |  
| `cs.CV`  | Computer Vision  |  
| `cs.LG`  | Machine Learning  |  
| `cs.CR`  | Cryptography and Security  |  
| `stat.ML`  | Machine Learning (Statistics)  |  
| `math.OC`  | Optimization and Control  |  
| `physics.comp-ph`  | Computational Physics  |  
Full list: <https://arxiv.org/category_taxonomy>
## Helper Script[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#helper-script "Direct link to Helper Script")
The `scripts/search_arxiv.py` script handles XML parsing and provides clean output:

```
python scripts/search_arxiv.py "GRPO reinforcement learning"python scripts/search_arxiv.py "transformer attention"--max10--sortdatepython scripts/search_arxiv.py --author"Yann LeCun"--max5python scripts/search_arxiv.py --category cs.AI --sortdatepython scripts/search_arxiv.py --id2402.03300python scripts/search_arxiv.py --id2402.03300,2401.12345
```

No dependencies — uses only Python stdlib.
## Semantic Scholar (Citations, Related Papers, Author Profiles)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#semantic-scholar-citations-related-papers-author-profiles "Direct link to Semantic Scholar \(Citations, Related Papers, Author Profiles\)")
arXiv doesn't provide citation data or recommendations. Use the **Semantic Scholar API** for that — free, no key needed for basic use (1 req/sec), returns JSON.
### Get paper details + citations[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#get-paper-details--citations "Direct link to Get paper details + citations")

```
# By arXiv IDcurl-s"https://api.semanticscholar.org/graph/v1/paper/arXiv:2402.03300?fields=title,authors,citationCount,referenceCount,influentialCitationCount,year,abstract"| python3 -m json.tool# By Semantic Scholar paper ID or DOIcurl-s"https://api.semanticscholar.org/graph/v1/paper/DOI:10.1234/example?fields=title,citationCount"
```

### Get citations OF a paper (who cited it)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#get-citations-of-a-paper-who-cited-it "Direct link to Get citations OF a paper \(who cited it\)")

```
curl-s"https://api.semanticscholar.org/graph/v1/paper/arXiv:2402.03300/citations?fields=title,authors,year,citationCount&limit=10"| python3 -m json.tool
```

### Get references FROM a paper (what it cites)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#get-references-from-a-paper-what-it-cites "Direct link to Get references FROM a paper \(what it cites\)")

```
curl-s"https://api.semanticscholar.org/graph/v1/paper/arXiv:2402.03300/references?fields=title,authors,year,citationCount&limit=10"| python3 -m json.tool
```

### Search papers (alternative to arXiv search, returns JSON)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#search-papers-alternative-to-arxiv-search-returns-json "Direct link to Search papers \(alternative to arXiv search, returns JSON\)")

```
curl-s"https://api.semanticscholar.org/graph/v1/paper/search?query=GRPO+reinforcement+learning&limit=5&fields=title,authors,year,citationCount,externalIds"| python3 -m json.tool
```

### Get paper recommendations[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#get-paper-recommendations "Direct link to Get paper recommendations")

```
curl-s-X POST "https://api.semanticscholar.org/recommendations/v1/papers/"\-H"Content-Type: application/json"\-d'{"positivePaperIds": ["arXiv:2402.03300"], "negativePaperIds": []}'| python3 -m json.tool
```

### Author profile[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#author-profile "Direct link to Author profile")

```
curl-s"https://api.semanticscholar.org/graph/v1/author/search?query=Yann+LeCun&fields=name,hIndex,citationCount,paperCount"| python3 -m json.tool
```

### Useful Semantic Scholar fields[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#useful-semantic-scholar-fields "Direct link to Useful Semantic Scholar fields")
`title`, `authors`, `year`, `abstract`, `citationCount`, `referenceCount`, `influentialCitationCount`, `isOpenAccess`, `openAccessPdf`, `fieldsOfStudy`, `publicationVenue`, `externalIds` (contains arXiv ID, DOI, etc.)
## Complete Research Workflow[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#complete-research-workflow "Direct link to Complete Research Workflow")
  1. **Discover** : `python scripts/search_arxiv.py "your topic" --sort date --max 10`
  2. **Assess impact** : `curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:ID?fields=citationCount,influentialCitationCount"`
  3. **Read abstract** : `web_extract(urls=["https://arxiv.org/abs/ID"])`
  4. **Read full paper** : `web_extract(urls=["https://arxiv.org/pdf/ID"])`
  5. **Find related work** : `curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:ID/references?fields=title,citationCount&limit=20"`
  6. **Get recommendations** : POST to Semantic Scholar recommendations endpoint
  7. **Track authors** : `curl -s "https://api.semanticscholar.org/graph/v1/author/search?query=NAME"`


## Rate Limits[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#rate-limits "Direct link to Rate Limits")  
| API  | Rate  | Auth  |  
| --- | --- | --- |  
| arXiv  | ~1 req / 3 seconds  | None needed  |  
| Semantic Scholar  | 1 req / second  | None (100/sec with API key)  |  
## Notes[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#notes "Direct link to Notes")
  * arXiv returns Atom XML — use the helper script or parsing snippet for clean output
  * Semantic Scholar returns JSON — pipe through `python3 -m json.tool` for readability
  * arXiv IDs: old format (`hep-th/0601001`) vs new (`2402.03300`)
  * PDF: `https://arxiv.org/pdf/{id}` — Abstract: `https://arxiv.org/abs/{id}`
  * HTML (when available): `https://arxiv.org/html/{id}`
  * For local PDF processing, see the `ocr-and-documents` skill


## ID Versioning[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#id-versioning "Direct link to ID Versioning")
  * `arxiv.org/abs/1706.03762` always resolves to the **latest** version
  * `arxiv.org/abs/1706.03762v1` points to a **specific** immutable version
  * When generating citations, preserve the version suffix you actually read to prevent citation drift (a later version may substantially change content)
  * The API `<id>` field returns the versioned URL (e.g., `http://arxiv.org/abs/1706.03762v7`)


## Withdrawn Papers[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#withdrawn-papers "Direct link to Withdrawn Papers")
Papers can be withdrawn after submission. When this happens:
  * The `<summary>` field contains a withdrawal notice (look for "withdrawn" or "retracted")
  * Metadata fields may be incomplete
  * Always check the summary before treating a result as a valid paper


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#reference-full-skillmd)
  * [Quick Reference](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#quick-reference)
  * [Searching Papers](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#searching-papers)
    * [Basic search](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#basic-search)
    * [Clean output (parse XML to readable format)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#clean-output-parse-xml-to-readable-format)
  * [Search Query Syntax](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#search-query-syntax)
    * [Boolean operators](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#boolean-operators)
  * [Sort and Pagination](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#sort-and-pagination)
  * [Fetching Specific Papers](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#fetching-specific-papers)
  * [BibTeX Generation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#bibtex-generation)
  * [Reading Paper Content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#reading-paper-content)
  * [Common Categories](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#common-categories)
  * [Helper Script](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#helper-script)
  * [Semantic Scholar (Citations, Related Papers, Author Profiles)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#semantic-scholar-citations-related-papers-author-profiles)
    * [Get paper details + citations](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#get-paper-details--citations)
    * [Get citations OF a paper (who cited it)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#get-citations-of-a-paper-who-cited-it)
    * [Get references FROM a paper (what it cites)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#get-references-from-a-paper-what-it-cites)
    * [Search papers (alternative to arXiv search, returns JSON)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#search-papers-alternative-to-arxiv-search-returns-json)
    * [Get paper recommendations](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#get-paper-recommendations)
    * [Author profile](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#author-profile)
    * [Useful Semantic Scholar fields](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#useful-semantic-scholar-fields)
  * [Complete Research Workflow](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#complete-research-workflow)
  * [Rate Limits](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#rate-limits)
  * [ID Versioning](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#id-versioning)
  * [Withdrawn Papers](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-arxiv#withdrawn-papers)


