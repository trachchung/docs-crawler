<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#__docusaurus_skipToContent_fallback)
On this page
Open-source embedding database for AI applications. Store embeddings and metadata, perform vector and full-text search, filter by metadata. Simple 4-function API. Scales from notebooks to production clusters. Use for semantic search, RAG applications, or document retrieval. Best for local development and open-source projects.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#skill-metadata "Direct link to Skill metadata")  
| Source  | Optional — install with `hermes skills install official/mlops/chroma`  |  
| --- | --- |  
| Path  | `optional-skills/mlops/chroma`  |  
| Version  | `1.0.0`  |  
| Author  | Orchestra Research  |  
| License  | MIT  |  
| Dependencies  |  `chromadb`, `sentence-transformers`  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `RAG`, `Chroma`, `Vector Database`, `Embeddings`, `Semantic Search`, `Open Source`, `Self-Hosted`, `Document Retrieval`, `Metadata Filtering`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Chroma - Open-Source Embedding Database
The AI-native database for building LLM applications with memory.
## When to use Chroma[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#when-to-use-chroma "Direct link to When to use Chroma")
**Use Chroma when:**
  * Building RAG (retrieval-augmented generation) applications
  * Need local/self-hosted vector database
  * Want open-source solution (Apache 2.0)
  * Prototyping in notebooks
  * Semantic search over documents
  * Storing embeddings with metadata


**Metrics** :
  * **24,300+ GitHub stars**
  * **1,900+ forks**
  * **v1.3.3** (stable, weekly releases)
  * **Apache 2.0 license**


**Use alternatives instead** :
  * **Pinecone** : Managed cloud, auto-scaling
  * **FAISS** : Pure similarity search, no metadata
  * **Weaviate** : Production ML-native database
  * **Qdrant** : High performance, Rust-based


## Quick start[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#quick-start "Direct link to Quick start")
### Installation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#installation "Direct link to Installation")

```
# Pythonpip install chromadb# JavaScript/TypeScriptnpminstall chromadb @chroma-core/default-embed
```

### Basic usage (Python)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#basic-usage-python "Direct link to Basic usage \(Python\)")

```
import chromadb# Create clientclient = chromadb.Client()# Create collectioncollection = client.create_collection(name="my_collection")# Add documentscollection.add(    documents=["This is document 1","This is document 2"],    metadatas=[{"source":"doc1"},{"source":"doc2"}],    ids=["id1","id2"]# Queryresults = collection.query(    query_texts=["document about topic"],    n_results=2print(results)
```

## Core operations[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#core-operations "Direct link to Core operations")
### 1. Create collection[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#1-create-collection "Direct link to 1. Create collection")

```
# Simple collectioncollection = client.create_collection("my_docs")# With custom embedding functionfrom chromadb.utils import embedding_functionsopenai_ef = embedding_functions.OpenAIEmbeddingFunction(    api_key="your-key",    model_name="text-embedding-3-small"collection = client.create_collection(    name="my_docs",    embedding_function=openai_ef# Get existing collectioncollection = client.get_collection("my_docs")# Delete collectionclient.delete_collection("my_docs")
```

### 2. Add documents[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#2-add-documents "Direct link to 2. Add documents")

```
# Add with auto-generated IDscollection.add(    documents=["Doc 1","Doc 2","Doc 3"],    metadatas=[{"source":"web","category":"tutorial"},{"source":"pdf","page":5},{"source":"api","timestamp":"2025-01-01"}    ids=["id1","id2","id3"]# Add with custom embeddingscollection.add(    embeddings=[[0.1,0.2,...],[0.3,0.4,...]],    documents=["Doc 1","Doc 2"],    ids=["id1","id2"]
```

### 3. Query (similarity search)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#3-query-similarity-search "Direct link to 3. Query \(similarity search\)")

```
# Basic queryresults = collection.query(    query_texts=["machine learning tutorial"],    n_results=5# Query with filtersresults = collection.query(    query_texts=["Python programming"],    n_results=3,    where={"source":"web"}# Query with metadata filtersresults = collection.query(    query_texts=["advanced topics"],    where={"$and":[{"category":"tutorial"},{"difficulty":{"$gte":3}}# Access resultsprint(results["documents"])# List of matching documentsprint(results["metadatas"])# Metadata for each docprint(results["distances"])# Similarity scoresprint(results["ids"])# Document IDs
```

### 4. Get documents[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#4-get-documents "Direct link to 4. Get documents")

```
# Get by IDsdocs = collection.get(    ids=["id1","id2"]# Get with filtersdocs = collection.get(    where={"category":"tutorial"},    limit=10# Get all documentsdocs = collection.get()
```

### 5. Update documents[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#5-update-documents "Direct link to 5. Update documents")

```
# Update document contentcollection.update(    ids=["id1"],    documents=["Updated content"],    metadatas=[{"source":"updated"}]
```

### 6. Delete documents[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#6-delete-documents "Direct link to 6. Delete documents")

```
# Delete by IDscollection.delete(ids=["id1","id2"])# Delete with filtercollection.delete(    where={"source":"outdated"}
```

## Persistent storage[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#persistent-storage "Direct link to Persistent storage")

```
# Persist to diskclient = chromadb.PersistentClient(path="./chroma_db")collection = client.create_collection("my_docs")collection.add(documents=["Doc 1"], ids=["id1"])# Data persisted automatically# Reload later with same pathclient = chromadb.PersistentClient(path="./chroma_db")collection = client.get_collection("my_docs")
```

## Embedding functions[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#embedding-functions "Direct link to Embedding functions")
### Default (Sentence Transformers)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#default-sentence-transformers "Direct link to Default \(Sentence Transformers\)")

```
# Uses sentence-transformers by defaultcollection = client.create_collection("my_docs")# Default model: all-MiniLM-L6-v2
```

### OpenAI[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#openai "Direct link to OpenAI")

```
from chromadb.utils import embedding_functionsopenai_ef = embedding_functions.OpenAIEmbeddingFunction(    api_key="your-key",    model_name="text-embedding-3-small"collection = client.create_collection(    name="openai_docs",    embedding_function=openai_ef
```

### HuggingFace[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#huggingface "Direct link to HuggingFace")

```
huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(    api_key="your-key",    model_name="sentence-transformers/all-mpnet-base-v2"collection = client.create_collection(    name="hf_docs",    embedding_function=huggingface_ef
```

### Custom embedding function[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#custom-embedding-function "Direct link to Custom embedding function")

```
from chromadb import Documents, EmbeddingFunction, EmbeddingsclassMyEmbeddingFunction(EmbeddingFunction):def__call__(self,input: Documents)-> Embeddings:# Your embedding logicreturn embeddingsmy_ef = MyEmbeddingFunction()collection = client.create_collection(    name="custom_docs",    embedding_function=my_ef
```

## Metadata filtering[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#metadata-filtering "Direct link to Metadata filtering")

```
# Exact matchresults = collection.query(    query_texts=["query"],    where={"category":"tutorial"}# Comparison operatorsresults = collection.query(    query_texts=["query"],    where={"page":{"$gt":10}}# $gt, $gte, $lt, $lte, $ne# Logical operatorsresults = collection.query(    query_texts=["query"],    where={"$and":[{"category":"tutorial"},{"difficulty":{"$lte":3}}}# Also: $or# Containsresults = collection.query(    query_texts=["query"],    where={"tags":{"$in":["python","ml"]}}
```

## LangChain integration[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#langchain-integration "Direct link to LangChain integration")

```
from langchain_chroma import Chromafrom langchain_openai import OpenAIEmbeddingsfrom langchain.text_splitter import RecursiveCharacterTextSplitter# Split documentstext_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)docs = text_splitter.split_documents(documents)# Create Chroma vector storevectorstore = Chroma.from_documents(    documents=docs,    embedding=OpenAIEmbeddings(),    persist_directory="./chroma_db"# Queryresults = vectorstore.similarity_search("machine learning", k=3)# As retrieverretriever = vectorstore.as_retriever(search_kwargs={"k":5})
```

## LlamaIndex integration[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#llamaindex-integration "Direct link to LlamaIndex integration")

```
from llama_index.vector_stores.chroma import ChromaVectorStorefrom llama_index.core import VectorStoreIndex, StorageContextimport chromadb# Initialize Chromadb = chromadb.PersistentClient(path="./chroma_db")collection = db.get_or_create_collection("my_collection")# Create vector storevector_store = ChromaVectorStore(chroma_collection=collection)storage_context = StorageContext.from_defaults(vector_store=vector_store)# Create indexindex = VectorStoreIndex.from_documents(    documents,    storage_context=storage_context# Queryquery_engine = index.as_query_engine()response = query_engine.query("What is machine learning?")
```

## Server mode[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#server-mode "Direct link to Server mode")

```
# Run Chroma server# Terminal: chroma run --path ./chroma_db --port 8000# Connect to serverimport chromadbfrom chromadb.config import Settingsclient = chromadb.HttpClient(    host="localhost",    port=8000,    settings=Settings(anonymized_telemetry=False)# Use as normalcollection = client.get_or_create_collection("my_docs")
```

## Best practices[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#best-practices "Direct link to Best practices")
  1. **Use persistent client** - Don't lose data on restart
  2. **Add metadata** - Enables filtering and tracking
  3. **Batch operations** - Add multiple docs at once
  4. **Choose right embedding model** - Balance speed/quality
  5. **Use filters** - Narrow search space
  6. **Unique IDs** - Avoid collisions
  7. **Regular backups** - Copy chroma_db directory
  8. **Monitor collection size** - Scale up if needed
  9. **Test embedding functions** - Ensure quality
  10. **Use server mode for production** - Better for multi-user


## Performance[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#performance "Direct link to Performance")  
| Operation  | Latency  | Notes  |  
| --- | --- | --- |  
| Add 100 docs  | ~1-3s  | With embedding  |  
| Query (top 10)  | ~50-200ms  | Depends on collection size  |  
| Metadata filter  | ~10-50ms  | Fast with proper indexing  |  
## Resources[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#resources "Direct link to Resources")
  * **GitHub** : <https://github.com/chroma-core/chroma> ⭐ 24,300+
  * **Docs** : <https://docs.trychroma.com>
  * **Discord** : <https://discord.gg/MMeYNTmh3x>
  * **Version** : 1.3.3+
  * **License** : Apache 2.0


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#reference-full-skillmd)
  * [When to use Chroma](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#when-to-use-chroma)
  * [Quick start](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#quick-start)
    * [Installation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#installation)
    * [Basic usage (Python)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#basic-usage-python)
  * [Core operations](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#core-operations)
    * [1. Create collection](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#1-create-collection)
    * [2. Add documents](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#2-add-documents)
    * [3. Query (similarity search)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#3-query-similarity-search)
    * [4. Get documents](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#4-get-documents)
    * [5. Update documents](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#5-update-documents)
    * [6. Delete documents](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#6-delete-documents)
  * [Persistent storage](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#persistent-storage)
  * [Embedding functions](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#embedding-functions)
    * [Default (Sentence Transformers)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#default-sentence-transformers)
    * [HuggingFace](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#huggingface)
    * [Custom embedding function](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#custom-embedding-function)
  * [Metadata filtering](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#metadata-filtering)
  * [LangChain integration](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#langchain-integration)
  * [LlamaIndex integration](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#llamaindex-integration)
  * [Server mode](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#server-mode)
  * [Best practices](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#best-practices)
  * [Performance](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma#performance)


