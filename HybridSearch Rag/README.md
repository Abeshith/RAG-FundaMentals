# HybridSearch RAG

Hybrid search approaches that combine multiple search methodologies (semantic, keyword, etc.) to achieve superior retrieval performance in RAG systems. This approach leverages the complementary strengths of different search paradigms to overcome individual limitations.

## What is Hybrid Search?

Hybrid Search combines dense vector search (semantic) with sparse retrieval methods (keyword-based) to create a more robust and comprehensive search system. This approach addresses the limitations of using either method in isolation and provides better coverage across different query types and information needs.

## Search Paradigms Comparison

### Dense Search (Semantic)
- **Strengths**: Understands context, handles synonyms, conceptual similarity
- **Weaknesses**: May miss exact keywords, less interpretable, computationally heavy
- **Best For**: Conceptual queries, natural language questions, semantic similarity

### Sparse Search (Keyword)
- **Strengths**: Exact keyword matching, fast, interpretable, handles rare terms
- **Weaknesses**: No semantic understanding, struggles with synonyms, brittle
- **Best For**: Specific term searches, exact phrase matching, technical queries

### Hybrid Approach Benefits
- **Complementary Coverage**: Combines strengths of both approaches
- **Improved Recall**: Captures more relevant documents
- **Better Precision**: Enhanced relevance through multiple signals
- **Query Adaptability**: Performs well across diverse query types

## Hybrid Search Architecture

```
User Query
    ↓
┌─────────────────────────────────────────┐
│         Query Processing                 │
├─────────────────────────────────────────┤
│ • Query analysis and understanding      │
│ • Keyword extraction                    │
│ • Semantic interpretation               │
└─────────────────────────────────────────┘
    ↓
┌──────────────────┐    ┌──────────────────┐
│   Dense Search   │    │   Sparse Search  │
│                  │    │                  │
│ • Vector DB      │    │ • Inverted Index │
│ • Embeddings     │    │ • BM25 Scoring   │
│ • Cosine Sim     │    │ • TF-IDF         │
└──────────────────┘    └──────────────────┘
    ↓                           ↓
┌─────────────────────────────────────────┐
│         Result Fusion                   │
├─────────────────────────────────────────┤
│ • Score normalization                   │
│ • Weighted combination                  │
│ • Rank fusion algorithms                │
└─────────────────────────────────────────┘
    ↓
Final Ranked Results
```

## Notebooks

### **cosine.ipynb**
- **Purpose**: Cosine similarity-based search implementation for semantic document retrieval
- **Key Concepts**:
  - **Vector Similarity Mathematics**: Understanding cosine distance calculations
  - **Embedding Space Analysis**: How semantic relationships are captured in vector space
  - **Similarity Threshold Optimization**: Finding optimal cutoff points for relevance
  - **Performance Benchmarking**: Evaluating cosine similarity effectiveness

#### Cosine Similarity Deep Dive

**Mathematical Foundation**:
```
cosine_similarity(A, B) = (A · B) / (||A|| × ||B||)

Where:
- A · B = dot product of vectors A and B
- ||A|| = magnitude (norm) of vector A
- ||B|| = magnitude (norm) of vector B
```

**Properties**:
- Range: [-1, 1] (typically [0, 1] for document embeddings)
- 1 = Perfect similarity
- 0 = No similarity
- -1 = Perfect dissimilarity (rare in document contexts)

#### Implementation Details:

**Vector Normalization**:
```python
def normalize_vector(vector):
    norm = np.linalg.norm(vector)
    return vector / norm if norm != 0 else vector

def cosine_similarity_batch(query_vector, document_vectors):
    # Efficient batch computation
    query_norm = normalize_vector(query_vector)
    doc_norms = normalize_vector(document_vectors)
    return np.dot(query_norm, doc_norms.T)
```

**Optimization Techniques**:
- **Approximate Nearest Neighbors**: FAISS, Annoy for fast similarity search
- **Quantization**: Reduce vector precision for memory efficiency
- **Indexing Strategies**: Hierarchical clustering, LSH for scalability

#### **Use Cases**:
- **Semantic Document Retrieval**: Finding conceptually similar documents
- **Content Recommendation**: Suggesting related articles or products
- **Duplicate Detection**: Identifying similar or duplicate content
- **Clustering**: Grouping similar documents together

### **hybridsearch-rag.ipynb**
- **Purpose**: Comprehensive hybrid search system combining semantic search with keyword-based methods
- **Key Concepts**:
  - **Multi-Modal Retrieval**: Integrating dense and sparse search methods
  - **Score Fusion Algorithms**: Advanced techniques for combining different search scores
  - **Query Classification**: Determining optimal search strategy based on query characteristics
  - **Performance Optimization**: Balancing accuracy with computational efficiency

#### Hybrid Search Implementation Strategies

**1. Parallel Hybrid Search**
```
Query → [Dense Search] + [Sparse Search] → Score Fusion → Results
  ↓         ↓                ↓              ↓           ↓
Input → Semantic Results + Keyword Results → Combined → Output
```

#### Advanced Fusion Algorithms

**1. Reciprocal Rank Fusion (RRF)**
```python
def reciprocal_rank_fusion(dense_results, sparse_results, k=60):
    fusion_scores = {}
    
    for rank, doc in enumerate(dense_results):
        fusion_scores[doc] = fusion_scores.get(doc, 0) + 1/(k + rank + 1)
    
    for rank, doc in enumerate(sparse_results):
        fusion_scores[doc] = fusion_scores.get(doc, 0) + 1/(k + rank + 1)
    
    return sorted(fusion_scores.items(), key=lambda x: x[1], reverse=True)
```

#### **Implementation Components**:

**1. Dense Search Module**:
- Vector embedding generation
- Similarity computation
- Result ranking and scoring
- Performance optimization

**2. Sparse Search Module**:
- Inverted index construction
- BM25/TF-IDF scoring
- Boolean query processing
- Phrase matching capabilities

**3. Fusion Engine**:
- Score normalization
- Weight optimization
- Result merging
- Quality assessment


## Performance Optimization Strategies

### Computational Efficiency
```
Optimization Level 1: Basic Hybrid
├── Parallel processing of dense and sparse search
├── Efficient vector operations
└── Optimized index structures

Optimization Level 2: Advanced Hybrid
├── Query-adaptive method selection
├── Early termination strategies
└── Result caching mechanisms

Optimization Level 3: Production Hybrid
├── GPU acceleration for vector operations
├── Distributed search architecture
└── Real-time adaptation algorithms
```
