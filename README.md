# RAG-Fundamentals 🚀

> **Comprehensive Collection of Retrieval-Augmented Generation Techniques**

A complete hands-on guide to RAG implementations, from basic concepts to advanced techniques. This repository contains practical notebooks demonstrating various RAG approaches, retrieval strategies, and optimization methods.

## 📊 RAG Architecture Flowchart

Based on the provided flowchart, here's the complete RAG system architecture:

```mermaid
graph TD
    A[📄 DATA] --> B[🔪 CHUNK 1]
    A --> C[🔪 CHUNK 2] 
    A --> D[🔪 CHUNK 3]
    
    B --> E[🧠 EMBEDDING 1]
    C --> F[🧠 EMBEDDING 2]
    D --> G[🧠 EMBEDDING 3]
    
    E --> H[💾 DATABASE<br/>Vector Store]
    F --> H
    G --> H
    
    I[👤 USER] --> J[🔎 QUERY]
    J --> K[🧠 EMBEDDING<br/>Query]
    
    I -.->|Generation| L[🔍 SEMANTIC SEARCH]
    K --> L
    H --> L
    
    L --> M[🎯 RETRIEVAL]
    M --> N[📊 RANKED RESULTS]
    N --> O[🔄 RERANKED RESULTS]
    
    O --> P[🤖 LLM<br/>Query+Prompt+Context]
    P --> Q[💬 RESPONSE]
    
    style A fill:#e1f5fe
    style H fill:#f3e5f5
    style I fill:#fff3e0
    style P fill:#e8f5e8
    style Q fill:#fce4ec
```

### Core RAG Components:
1. **📄 Data Processing**: Documents are split into manageable chunks
2. **🧠 Embedding**: Text chunks converted to vector representations  
3. **💾 Vector Database**: Stores embeddings for efficient retrieval
4. **🔍 Semantic Search**: Finds relevant chunks using similarity
5. **🎯 Retrieval**: Returns top-k most relevant documents
6. **🔄 Reranking**: Optimizes order for better context
7. **🤖 LLM Generation**: Produces final answer with retrieved context

## 🎯 What is RAG?

**Retrieval-Augmented Generation** combines the power of:
- **🔍 Information Retrieval**: Finding relevant external knowledge
- **🤖 Language Generation**: Creating contextual responses
- **📚 External Knowledge**: Up-to-date, domain-specific information

## 📁 Repository Structure

### 🔰 [Basic RAG](./Basic%20Rag/)
**Foundation techniques for RAG implementation**

| Notebook | Purpose | Key Techniques |
|----------|---------|----------------|
| `basic_rag.ipynb` | Core RAG pipeline | Vector embeddings, semantic search, prompt engineering |
| `document_rag.ipynb` | PDF document processing | Local knowledge base, metadata handling |
| `url_rag.ipynb` | Web content RAG | Real-time retrieval, dynamic knowledge updates |

### 🔍 [Retriever Techniques](./Retriever%20Techniques/)
**Advanced retrieval strategies beyond basic semantic search**

| Technique | Notebook | Innovation |
|-----------|----------|------------|
| **Contextual Compression** | `Contextual_Compression_Retriever.ipynb` | Compresses retrieved docs to extract only relevant portions |
| **HyDE** | `Hypothetical_Document_Embedding_(HyDE).ipynb` | Generates hypothetical answers to improve retrieval accuracy |
| **Multi-Hop Retrieval** | `MultiHop_Query_Step_by_Step_Retrieval.ipynb` | Step-by-step retrieval for complex queries |
| **Parent Document** | `Parent_Document_Retriever.ipynb` | Retrieves small chunks but returns larger parent documents |
| **Self-Query** | `Self_Query_Retrieval.ipynb` | Natural language query parsing with metadata filtering |
| **Sentence Window** | `Sentence_Window_Retrieval.ipynb` | Expanded context windows around relevant sentences |

### 🏆 [ReRanking Techniques](./ReRanking%20Techniques/)
**Optimize retrieved document ordering for better LLM performance**

| Method | Notebook | Advantage |
|--------|----------|-----------|
| **BM25 Rerank** | `bm25_rerank_rag.ipynb` | Statistical keyword-based relevance scoring |
| **Cohere Rerank** | `cohere_rerank.ipynb` | State-of-the-art neural reranking API |
| **Cross-Encoder** | `cross_encoder_rerank.ipynb` | Joint query-document encoding for precise relevance |
| **Flash ReRank** | `Flash_ReRanking.ipynb` | Ultra-fast reranking for real-time applications |

### 🔗 [Hybrid Search RAG](./HybridSearch%20Rag/)
**Combine multiple search methodologies for superior performance**

| Technique | Notebook | Combines |
|-----------|----------|----------|
| **Cosine Similarity** | `cosine.ipynb` | Vector similarity mathematics and optimization |
| **Hybrid Search** | `hybridsearch-rag.ipynb` | Semantic + keyword search with score fusion algorithms |

### ⚡ [RAG Fusion](./Rag%20Fusion/)
**Fuse multiple retrieval methods for comprehensive results**

| Method | Notebook | Fusion Strategy |
|--------|----------|-----------------|
| **Reciprocal Rank Fusion** | `ReciProcal_Rank_Fusion.ipynb` | Combines rankings from multiple retrievers using RRF algorithm |

### 🎯 [Lost In Middle Problem](./Lost%20In%20Middle%20Rag%20Problem/)
**Solve positional bias where important info gets overlooked in middle context**

| Solution | Notebook | Approach |
|----------|----------|----------|
| **Merger & Reranking** | `MergerRetriever_And_Reranking.ipynb` | Strategic document ordering and context reorganization |

### 🖼️ [MultiModal RAG](./MultiModal%20RAG/)
**Process and understand multiple data types including text, images, charts, and diagrams**

| Technique | Notebook | Innovation |
|-----------|----------|------------|
| **MultiModal Processing** | `MultiModal_RAG(IMG+TexT).ipynb` | CLIP-based unified embeddings for text and images, cross-modal retrieval |

### 🤖 [Agentic RAG](./Agentic%20RAG/)
**Intelligent agent-based RAG systems with autonomous decision making**

| Method | Notebook | Capability |
|--------|----------|------------|
| **Agentic RAG** | `Agentic_RAG.ipynb` | Autonomous agent-based retrieval and generation |
| **LangGraph RAG** | `Rag_with_langgraph.ipynb` | Graph-based workflow orchestration for complex RAG |
| **Routed RAG** | `Routed_RAG_With_LLM_Router.ipynb` | LLM-powered routing for dynamic retrieval strategies |

### 🔬 [Advanced RAG](./Advanced%20RAG/)
**Cutting-edge RAG techniques for specialized applications**

| Technique | Notebook | Advanced Feature |
|-----------|----------|------------------|
| **Agentic RAG** | `Agentic_RAG.ipynb` | Agent-based autonomous reasoning and retrieval |
| **Corrective RAG (CRAG)** | `Corrective_RAG_(CRAG).ipynb` | Self-correcting retrieval with confidence scoring |

### �‍💼 [Supervisor Agent RAG](./Supervior%20Agent%20RAG/)
**Intelligent routing across multiple knowledge domains with domain-specific vector stores**

| Technique | Notebook | Capability |
|-----------|----------|------------|
| **Supervisor Agent** | `SuperVisor_RAG_Agent.ipynb` | Multi-domain routing with automatic classification and caching |

### 💾 [Structured Query RAG](./Structured%20Query%20RAG/)
**Text-to-SQL RAG systems for natural language querying of structured databases**

| Technique | Notebook | Capability |
|-----------|----------|------------|
| **Structured Retrieval** | `Structured_Retrieval_RAG.ipynb` | Schema-aware natural language to SQL with result interpretation |

### ⏱️ [Dynamic RAG](./Dynamic%20RAG/)
**Self-updating knowledge bases with version control and real-time updates**

| Technique | Notebook | Capability |
|-----------|----------|------------|
| **Dynamic Knowledge Update** | `Dynamic_Knowledge_Update_RAG.ipynb` | Version-tracked document updates with timestamp awareness |

### �📊 [RAG Evaluation](./RAG%20Evaluation/)
**Comprehensive evaluation frameworks for RAG system performance**

| Framework | Notebook | Evaluation Focus |
|-----------|----------|------------------|
| **RAG Evaluation** | `RAG_Evaluation.ipynb` | Custom evaluation metrics and benchmarking |
| **RAGAs Evaluation** | `RAGAs_Evaluation.ipynb` | Automated evaluation using RAGAs framework |

## 🔧 Key Technologies Used

- **🦜 LangChain**: RAG framework and components
- **🤗 HuggingFace**: Embeddings and transformers
- **📊 ChromaDB**: Vector database storage
- **🔍 FAISS**: Efficient similarity search
- **🌐 OpenAI**: Embeddings and language models
- **⚡ Cohere**: Professional reranking services
- **🖼️ CLIP**: Multimodal embeddings for text and images
- **🔄 LangGraph**: Graph-based workflow orchestration
- **⚖️ RAGAs**: Automated RAG evaluation framework
- **🧠 Groq**: High-performance LLM inference
- **📝 Sentence Transformers**: Lightweight embedding models
- **🗃️ SQLite**: Structured database for Text-to-SQL RAG
- **📊 Tavily**: Web search API for real-time information

## 🚀 Getting Started

1. **Clone the repository**
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Start with Basic RAG** to understand fundamentals
4. **Explore Retriever Techniques** for advanced retrieval strategies
5. **Implement ReRanking** for better accuracy
6. **Try Hybrid Approaches** for production systems
7. **Explore MultiModal RAG** for documents with images and text
8. **Advance to Agentic RAG** for autonomous intelligent systems
9. **Use RAG Evaluation** to benchmark and optimize performance


## 🎯 Use Cases Covered

- **📖 Document Q&A**: Academic papers, legal documents
- **🌐 Web Search**: Real-time information retrieval
- **🏢 Enterprise**: Knowledge management systems
- **🔬 Research**: Multi-document analysis and synthesis
- **💬 Chatbots**: Context-aware conversational AI
- **🖼️ Multimodal Analysis**: Documents with text, images, and charts
- **🤖 Autonomous Systems**: Agent-based intelligent retrieval
- **📊 Performance Evaluation**: RAG system benchmarking and optimization
- **🔄 Self-Correcting Systems**: Adaptive and corrective RAG implementations
- **💾 Structured Data**: Natural language querying of databases with Text-to-SQL
- **🔄 Dynamic Knowledge**: Self-updating, version-controlled knowledge bases
- **🧠 Multi-Domain Routing**: Intelligent classification and retrieval across different knowledge domains

---

> **🎯 Master RAG**: From basic retrieval to advanced fusion techniques, this repository provides everything needed to build Development-ready RAG systems.
