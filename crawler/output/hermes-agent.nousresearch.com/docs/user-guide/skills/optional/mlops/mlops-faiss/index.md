<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#__docusaurus_skipToContent_fallback)
On this page
Facebook's library for efficient similarity search and clustering of dense vectors. Supports billions of vectors, GPU acceleration, and various index types (Flat, IVF, HNSW). Use for fast k-NN search, large-scale vector retrieval, or when you need pure similarity search without metadata. Best for high-performance applications.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#skill-metadata "Direct link to Skill metadata")  
| Source  | Optional — install with `hermes skills install official/mlops/faiss`  |  
| --- | --- |  
| Path  | `optional-skills/mlops/faiss`  |  
| Version  | `1.0.0`  |  
| Author  | Orchestra Research  |  
| License  | MIT  |  
| Dependencies  |  `faiss-cpu`, `faiss-gpu`, `numpy`  |  
| Platforms  | linux, macos  |  
| Tags  |  `RAG`, `FAISS`, `Similarity Search`, `Vector Search`, `Facebook AI`, `GPU Acceleration`, `Billion-Scale`, `K-NN`, `HNSW`, `High Performance`, `Large Scale`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# FAISS - Efficient Similarity Search
Facebook AI's library for billion-scale vector similarity search.
## When to use FAISS[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#when-to-use-faiss "Direct link to When to use FAISS")
**Use FAISS when:**
  * Need fast similarity search on large vector datasets (millions/billions)
  * GPU acceleration required
  * Pure vector similarity (no metadata filtering needed)
  * High throughput, low latency critical
  * Offline/batch processing of embeddings


**Metrics** :
  * **31,700+ GitHub stars**
  * Meta/Facebook AI Research
  * **Handles billions of vectors**
  * **C++** with Python bindings


**Use alternatives instead** :
  * **Chroma/Pinecone** : Need metadata filtering
  * **Weaviate** : Need full database features
  * **Annoy** : Simpler, fewer features


## Quick start[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#quick-start "Direct link to Quick start")
### Installation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#installation "Direct link to Installation")

```
# CPU onlypip install faiss-cpu# GPU supportpip install faiss-gpu
```

### Basic usage[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#basic-usage "Direct link to Basic usage")

```
import faissimport numpy as np# Create sample data (1000 vectors, 128 dimensions)d =128nb =1000vectors = np.random.random((nb, d)).astype('float32')# Create indexindex = faiss.IndexFlatL2(d)# L2 distanceindex.add(vectors)# Add vectors# Searchk =5# Find 5 nearest neighborsquery = np.random.random((1, d)).astype('float32')distances, indices = index.search(query, k)print(f"Nearest neighbors: {indices}")print(f"Distances: {distances}")
```

## Index types[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#index-types "Direct link to Index types")
### 1. Flat (exact search)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#1-flat-exact-search "Direct link to 1. Flat \(exact search\)")

```
# L2 (Euclidean) distanceindex = faiss.IndexFlatL2(d)# Inner product (cosine similarity if normalized)index = faiss.IndexFlatIP(d)# Slowest, most accurate
```

### 2. IVF (inverted file) - Fast approximate[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#2-ivf-inverted-file---fast-approximate "Direct link to 2. IVF \(inverted file\) - Fast approximate")

```
# Create quantizerquantizer = faiss.IndexFlatL2(d)# IVF index with 100 clustersnlist =100index = faiss.IndexIVFFlat(quantizer, d, nlist)# Train on dataindex.train(vectors)# Add vectorsindex.add(vectors)# Search (nprobe = clusters to search)index.nprobe =10distances, indices = index.search(query, k)
```

### 3. HNSW (Hierarchical NSW) - Best quality/speed[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#3-hnsw-hierarchical-nsw---best-qualityspeed "Direct link to 3. HNSW \(Hierarchical NSW\) - Best quality/speed")

```
# HNSW indexM =32# Number of connections per layerindex = faiss.IndexHNSWFlat(d, M)# No training neededindex.add(vectors)# Searchdistances, indices = index.search(query, k)
```

### 4. Product Quantization - Memory efficient[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#4-product-quantization---memory-efficient "Direct link to 4. Product Quantization - Memory efficient")

```
# PQ reduces memory by 16-32×m =8# Number of subquantizersnbits =8index = faiss.IndexPQ(d, m, nbits)# Train and addindex.train(vectors)index.add(vectors)
```

## Save and load[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#save-and-load "Direct link to Save and load")

```
# Save indexfaiss.write_index(index,"large.index")# Load indexindex = faiss.read_index("large.index")# Continue usingdistances, indices = index.search(query, k)
```

## GPU acceleration[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#gpu-acceleration "Direct link to GPU acceleration")

```
# Single GPUres = faiss.StandardGpuResources()index_cpu = faiss.IndexFlatL2(d)index_gpu = faiss.index_cpu_to_gpu(res,0, index_cpu)# GPU 0# Multi-GPUindex_gpu = faiss.index_cpu_to_all_gpus(index_cpu)# 10-100× faster than CPU
```

## LangChain integration[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#langchain-integration "Direct link to LangChain integration")

```
from langchain_community.vectorstores import FAISSfrom langchain_openai import OpenAIEmbeddings# Create FAISS vector storevectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())# Savevectorstore.save_local("faiss_index")# Loadvectorstore = FAISS.load_local("faiss_index",    OpenAIEmbeddings(),    allow_dangerous_deserialization=True# Searchresults = vectorstore.similarity_search("query", k=5)
```

## LlamaIndex integration[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#llamaindex-integration "Direct link to LlamaIndex integration")

```
from llama_index.vector_stores.faiss import FaissVectorStoreimport faiss# Create FAISS indexd =1536faiss_index = faiss.IndexFlatL2(d)vector_store = FaissVectorStore(faiss_index=faiss_index)
```

## Best practices[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#best-practices "Direct link to Best practices")
  1. **Choose right index type** - Flat for <10K, IVF for 10K-1M, HNSW for quality
  2. **Normalize for cosine** - Use IndexFlatIP with normalized vectors
  3. **Use GPU for large datasets** - 10-100× faster
  4. **Save trained indices** - Training is expensive
  5. **Tune nprobe/ef_search** - Balance speed/accuracy
  6. **Monitor memory** - PQ for large datasets
  7. **Batch queries** - Better GPU utilization


## Performance[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#performance "Direct link to Performance")  
| Index Type  | Build Time  | Search Time  | Memory  | Accuracy  |  
| --- | --- | --- | --- | --- |  
| Flat  | Fast  | Slow  | High  | 100%  |  
| IVF  | Medium  | Fast  | Medium  | 95-99%  |  
| HNSW  | Slow  | Fastest  | High  | 99%  |  
| PQ  | Medium  | Fast  | Low  | 90-95%  |  
## Resources[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#resources "Direct link to Resources")
  * **GitHub** : <https://github.com/facebookresearch/faiss> ⭐ 31,700+
  * **Wiki** : <https://github.com/facebookresearch/faiss/wiki>
  * **License** : MIT


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#reference-full-skillmd)
  * [When to use FAISS](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#when-to-use-faiss)
  * [Quick start](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#quick-start)
    * [Installation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#installation)
    * [Basic usage](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#basic-usage)
  * [Index types](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#index-types)
    * [1. Flat (exact search)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#1-flat-exact-search)
    * [2. IVF (inverted file) - Fast approximate](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#2-ivf-inverted-file---fast-approximate)
    * [3. HNSW (Hierarchical NSW) - Best quality/speed](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#3-hnsw-hierarchical-nsw---best-qualityspeed)
    * [4. Product Quantization - Memory efficient](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#4-product-quantization---memory-efficient)
  * [Save and load](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#save-and-load)
  * [GPU acceleration](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#gpu-acceleration)
  * [LangChain integration](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#langchain-integration)
  * [LlamaIndex integration](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#llamaindex-integration)
  * [Best practices](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#best-practices)
  * [Performance](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss#performance)


