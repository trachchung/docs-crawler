<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#__docusaurus_skipToContent_fallback)
On this page
Managed vector database for production AI applications. Fully managed, auto-scaling, with hybrid search (dense + sparse), metadata filtering, and namespaces. Low latency (<100ms p95). Use for production RAG, recommendation systems, or semantic search at scale. Best for serverless, managed infrastructure.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#skill-metadata "Direct link to Skill metadata")  
| Source  | Optional — install with `hermes skills install official/mlops/pinecone`  |  
| --- | --- |  
| Path  | `optional-skills/mlops/pinecone`  |  
| Version  | `1.0.0`  |  
| Author  | Orchestra Research  |  
| License  | MIT  |  
| Dependencies  | `pinecone-client`  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `RAG`, `Pinecone`, `Vector Database`, `Managed Service`, `Serverless`, `Hybrid Search`, `Production`, `Auto-Scaling`, `Low Latency`, `Recommendations`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Pinecone - Managed Vector Database
The vector database for production AI applications.
## When to use Pinecone[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#when-to-use-pinecone "Direct link to When to use Pinecone")
**Use when:**
  * Need managed, serverless vector database
  * Production RAG applications
  * Auto-scaling required
  * Low latency critical (<100ms)
  * Don't want to manage infrastructure
  * Need hybrid search (dense + sparse vectors)


**Metrics** :
  * Fully managed SaaS
  * Auto-scales to billions of vectors
  * **p95 latency <100ms**
  * 99.9% uptime SLA


**Use alternatives instead** :
  * **Chroma** : Self-hosted, open-source
  * **FAISS** : Offline, pure similarity search
  * **Weaviate** : Self-hosted with more features


## Quick start[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#quick-start "Direct link to Quick start")
### Installation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#installation "Direct link to Installation")

```
pip install pinecone-client
```

### Basic usage[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#basic-usage "Direct link to Basic usage")

```
from pinecone import Pinecone, ServerlessSpec# Initializepc = Pinecone(api_key="your-api-key")# Create indexpc.create_index(    name="my-index",    dimension=1536,# Must match embedding dimension    metric="cosine",# or "euclidean", "dotproduct"    spec=ServerlessSpec(cloud="aws", region="us-east-1")# Connect to indexindex = pc.Index("my-index")# Upsert vectorsindex.upsert(vectors=[{"id":"vec1","values":[0.1,0.2,...],"metadata":{"category":"A"}},{"id":"vec2","values":[0.3,0.4,...],"metadata":{"category":"B"}}# Queryresults = index.query(    vector=[0.1,0.2,...],    top_k=5,    include_metadata=Trueprint(results["matches"])
```

## Core operations[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#core-operations "Direct link to Core operations")
### Create index[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#create-index "Direct link to Create index")

```
# Serverless (recommended)pc.create_index(    name="my-index",    dimension=1536,    metric="cosine",    spec=ServerlessSpec(        cloud="aws",# or "gcp", "azure"        region="us-east-1"# Pod-based (for consistent performance)from pinecone import PodSpecpc.create_index(    name="my-index",    dimension=1536,    metric="cosine",    spec=PodSpec(        environment="us-east1-gcp",        pod_type="p1.x1"
```

### Upsert vectors[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#upsert-vectors "Direct link to Upsert vectors")

```
# Single upsertindex.upsert(vectors=["id":"doc1","values":[0.1,0.2,...],# 1536 dimensions"metadata":{"text":"Document content","category":"tutorial","timestamp":"2025-01-01"# Batch upsert (recommended)vectors =[{"id":f"vec{i}","values": embedding,"metadata": metadata}for i,(embedding, metadata)inenumerate(zip(embeddings, metadatas))index.upsert(vectors=vectors, batch_size=100)
```

### Query vectors[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#query-vectors "Direct link to Query vectors")

```
# Basic queryresults = index.query(    vector=[0.1,0.2,...],    top_k=10,    include_metadata=True,    include_values=False# With metadata filteringresults = index.query(    vector=[0.1,0.2,...],    top_k=5,filter={"category":{"$eq":"tutorial"}}# Namespace queryresults = index.query(    vector=[0.1,0.2,...],    top_k=5,    namespace="production"# Access resultsformatchin results["matches"]:print(f"ID: {match['id']}")print(f"Score: {match['score']}")print(f"Metadata: {match['metadata']}")
```

### Metadata filtering[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#metadata-filtering "Direct link to Metadata filtering")

```
# Exact matchfilter={"category":"tutorial"}# Comparisonfilter={"price":{"$gte":100}}# $gt, $gte, $lt, $lte, $ne# Logical operatorsfilter={"$and":[{"category":"tutorial"},{"difficulty":{"$lte":3}}}# Also: $or# In operatorfilter={"tags":{"$in":["python","ml"]}}
```

## Namespaces[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#namespaces "Direct link to Namespaces")

```
# Partition data by namespaceindex.upsert(    vectors=[{"id":"vec1","values":[...]}],    namespace="user-123"# Query specific namespaceresults = index.query(    vector=[...],    namespace="user-123",    top_k=5# List namespacesstats = index.describe_index_stats()print(stats['namespaces'])
```

## Hybrid search (dense + sparse)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#hybrid-search-dense--sparse "Direct link to Hybrid search \(dense + sparse\)")

```
# Upsert with sparse vectorsindex.upsert(vectors=["id":"doc1","values":[0.1,0.2,...],# Dense vector"sparse_values":{"indices":[10,45,123],# Token IDs"values":[0.5,0.3,0.8]# TF-IDF scores"metadata":{"text":"..."}# Hybrid queryresults = index.query(    vector=[0.1,0.2,...],    sparse_vector={"indices":[10,45],"values":[0.5,0.3]    top_k=5,    alpha=0.5# 0=sparse, 1=dense, 0.5=hybrid
```

## LangChain integration[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#langchain-integration "Direct link to LangChain integration")

```
from langchain_pinecone import PineconeVectorStorefrom langchain_openai import OpenAIEmbeddings# Create vector storevectorstore = PineconeVectorStore.from_documents(    documents=docs,    embedding=OpenAIEmbeddings(),    index_name="my-index"# Queryresults = vectorstore.similarity_search("query", k=5)# With metadata filterresults = vectorstore.similarity_search("query",    k=5,filter={"category":"tutorial"}# As retrieverretriever = vectorstore.as_retriever(search_kwargs={"k":10})
```

## LlamaIndex integration[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#llamaindex-integration "Direct link to LlamaIndex integration")

```
from llama_index.vector_stores.pinecone import PineconeVectorStore# Connect to Pineconepc = Pinecone(api_key="your-key")pinecone_index = pc.Index("my-index")# Create vector storevector_store = PineconeVectorStore(pinecone_index=pinecone_index)# Use in LlamaIndexfrom llama_index.core import StorageContext, VectorStoreIndexstorage_context = StorageContext.from_defaults(vector_store=vector_store)index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
```

## Index management[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#index-management "Direct link to Index management")

```
# List indicesindexes = pc.list_indexes()# Describe indexindex_info = pc.describe_index("my-index")print(index_info)# Get index statsstats = index.describe_index_stats()print(f"Total vectors: {stats['total_vector_count']}")print(f"Namespaces: {stats['namespaces']}")# Delete indexpc.delete_index("my-index")
```

## Delete vectors[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#delete-vectors "Direct link to Delete vectors")

```
# Delete by IDindex.delete(ids=["vec1","vec2"])# Delete by filterindex.delete(filter={"category":"old"})# Delete all in namespaceindex.delete(delete_all=True, namespace="test")# Delete entire indexindex.delete(delete_all=True)
```

## Best practices[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#best-practices "Direct link to Best practices")
  1. **Use serverless** - Auto-scaling, cost-effective
  2. **Batch upserts** - More efficient (100-200 per batch)
  3. **Add metadata** - Enable filtering
  4. **Use namespaces** - Isolate data by user/tenant
  5. **Monitor usage** - Check Pinecone dashboard
  6. **Optimize filters** - Index frequently filtered fields
  7. **Test with free tier** - 1 index, 100K vectors free
  8. **Use hybrid search** - Better quality
  9. **Set appropriate dimensions** - Match embedding model
  10. **Regular backups** - Export important data


## Performance[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#performance "Direct link to Performance")  
| Operation  | Latency  | Notes  |  
| --- | --- | --- |  
| Upsert  | ~50-100ms  | Per batch  |  
| Query (p50)  | ~50ms  | Depends on index size  |  
| Query (p95)  | ~100ms  | SLA target  |  
| Metadata filter  | ~+10-20ms  | Additional overhead  |  
## Pricing (as of 2025)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#pricing-as-of-2025 "Direct link to Pricing \(as of 2025\)")
**Serverless** :
  * $0.096 per million read units
  * $0.06 per million write units
  * $0.06 per GB storage/month


**Free tier** :
  * 1 serverless index
  * 100K vectors (1536 dimensions)
  * Great for prototyping


## Resources[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#resources "Direct link to Resources")
  * **Website** : <https://www.pinecone.io>
  * **Docs** : <https://docs.pinecone.io>
  * **Console** : <https://app.pinecone.io>
  * **Pricing** : <https://www.pinecone.io/pricing>


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#reference-full-skillmd)
  * [When to use Pinecone](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#when-to-use-pinecone)
  * [Quick start](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#quick-start)
    * [Installation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#installation)
    * [Basic usage](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#basic-usage)
  * [Core operations](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#core-operations)
    * [Create index](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#create-index)
    * [Upsert vectors](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#upsert-vectors)
    * [Query vectors](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#query-vectors)
    * [Metadata filtering](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#metadata-filtering)
  * [Hybrid search (dense + sparse)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#hybrid-search-dense--sparse)
  * [LangChain integration](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#langchain-integration)
  * [LlamaIndex integration](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#llamaindex-integration)
  * [Index management](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#index-management)
  * [Delete vectors](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#delete-vectors)
  * [Best practices](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#best-practices)
  * [Performance](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#performance)
  * [Pricing (as of 2025)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pinecone#pricing-as-of-2025)


