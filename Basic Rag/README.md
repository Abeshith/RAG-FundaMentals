# Basic RAG

This folder contains fundamental RAG (Retrieval-Augmented Generation) implementations demonstrating core concepts and techniques. RAG combines the power of information retrieval with generative AI to provide accurate, contextual responses based on external knowledge sources.

## What is RAG?

RAG is a framework that enhances Large Language Models (LLMs) by incorporating external knowledge through a retrieval mechanism. Instead of relying solely on the model's training data, RAG retrieves relevant information from external sources and uses it to generate more accurate and up-to-date responses.

## Basic RAG Pipeline Flow

```
Query → Document Retrieval → Context Augmentation → LLM Generation → Response
  ↓            ↓                    ↓                   ↓            ↓
User Input → Vector Search → Relevant Chunks → Prompt + Context → Final Answer
```

## Key Components

1. **Document Processing**: Text chunking, preprocessing, and cleaning
2. **Embedding Generation**: Converting text into vector representations
3. **Vector Storage**: Storing embeddings in vector databases (ChromaDB, Pinecone, etc.)
4. **Retrieval**: Finding semantically similar documents using cosine similarity
5. **Context Augmentation**: Combining retrieved context with user queries
6. **Generation**: LLM produces final response using augmented context

## Notebooks

### **basic_rag.ipynb**
- **Purpose**: Introduction to basic RAG pipeline implementation with vector embeddings and semantic search
- **Key Concepts**: 
  - Document chunking strategies (fixed-size, semantic)
  - Embedding models (OpenAI, HuggingFace)
  - Vector similarity search
  - Prompt engineering for RAG
- **Use Cases**: General Q&A systems, knowledge base queries
- **Technologies**: LangChain, ChromaDB, OpenAI embeddings

### **document_rag.ipynb**
- **Purpose**: Document-based RAG system for processing and querying local PDF documents
- **Key Concepts**:
  - PDF text extraction and processing
  - Document metadata handling
  - Local knowledge base creation
  - Context-aware question answering
- **Use Cases**: Academic research, legal document analysis, enterprise knowledge management
- **Technologies**: PyPDF2/pdfplumber, vector databases, document loaders

### **url_rag.ipynb**
- **Purpose**: Web-based RAG implementation that retrieves and processes content from URLs
- **Key Concepts**:
  - Web scraping and content extraction
  - Real-time information retrieval
  - Dynamic knowledge base updates
  - URL content processing pipelines
- **Use Cases**: News analysis, real-time fact-checking, web content summarization
- **Technologies**: BeautifulSoup, Selenium, web loaders

### **Rag_With_MongoDB.ipynb**
- **Purpose**: RAG implementation using MongoDB Atlas as a NoSQL document store with vector search capabilities
- **Key Concepts**:
  - NoSQL document storage for metadata and text content
  - MongoDB Atlas vector search functionality
  - Flexible schema for document management
  - Native vector indexing and similarity search
  - Document-based retrieval with metadata filtering
- **Use Cases**: Enterprise knowledge management, content management systems, scalable document repositories
- **Technologies**: MongoDB Atlas, PyMongo, vector search indexes

#### MongoDB Atlas Setup

**Prerequisites:**
1. Create a MongoDB Atlas account at [mongodb.com/atlas](https://www.mongodb.com/atlas)
2. Login to your MongoDB Atlas dashboard

**Step 1: Create a Cluster**
1. Click "Create a New Cluster" or "Build a Database"
2. Choose your cloud provider (AWS, Google Cloud, or Azure)
3. Select a region close to your location
4. Choose cluster tier (M0 Sandbox for free tier)
5. Name your cluster and click "Create Cluster"

**Step 2: Configure Network Access**
1. Go to "Network Access" in the left sidebar
2. Click "Add IP Address"
3. Add your current IP or use "0.0.0.0/0" for development (not recommended for production)
4. Click "Confirm"

**Step 3: Create Database User**
1. Go to "Database Access" in the left sidebar
2. Click "Add New Database User"
3. Choose "Password" authentication
4. Create username and strong password
5. Set user privileges to "Atlas admin" or custom roles as needed
6. Click "Add User"

**Step 4: Get Connection String**
1. Click "Connect" on your cluster
2. Select "Connect your application"
3. Choose Python driver and version 4.0 or later
4. Copy the connection string
5. Replace `<password>` with your user password

**Step 5: Create Vector Search Index**
Use the following JSON configuration to create a vector search index in MongoDB Atlas:

```json
{
  "fields": [{
    "numDimensions": 1024,
    "path": "embedding",
    "similarity": "cosine",
    "type": "vector"
  }]
}
```

### **Rag_With_Mongo_PineCone.ipynb & Rag_With_Mongo_PineCone_Helper.ipynb**

- **Purpose**: Hybrid RAG architecture combining MongoDB Atlas (NoSQL) for metadata storage and Pinecone for vector embeddings
- **Key Concepts**:
  - Dual-storage approach: MongoDB for document metadata, Pinecone for vectors
  - Scalable vector operations with Pinecone's optimized infrastructure
  - Metadata filtering and document management with MongoDB
  - Coordinated data ingestion across both platforms
  - Helper notebook manages background services and utilities
- **Use Cases**: Large-scale enterprise applications, high-performance vector search, complex metadata queries
- **Technologies**: MongoDB Atlas, Pinecone, dual-database coordination

#### MongoDB Atlas + Pinecone Setup

**MongoDB Atlas Setup** (Follow steps above for MongoDB configuration)

**Pinecone Setup:**

**Step 1: Create Pinecone Account**
1. Visit [pinecone.io](https://www.pinecone.io/) and sign up
2. Login to your Pinecone console

**Step 2: Create API Key**
1. Go to "API Keys" in the left sidebar
2. Click "Create API Key"
3. Name your API key and copy the value
4. Store securely for use in notebooks

**Step 3: Create Pinecone Index**
1. Click "Create Index" in the Pinecone console
2. Set index name (e.g., "rag-documents")
3. Set dimensions to 1536 (for OpenAI embeddings)
4. Choose metric: "cosine" for similarity
5. Select environment/region
6. Click "Create Index"

**Implementation Architecture:**
- **Helper Notebook**: Runs background services, manages connections, provides utility functions
- **Main Notebook**: Handles data ingestion pipeline:
  - Document metadata → MongoDB Atlas
  - Document embeddings → Pinecone
  - Coordinated retrieval from both systems
  - Unified query interface

## Getting Started

1. **Prerequisites**: Python 3.8+, API keys for LLM providers, MongoDB Atlas account, Pinecone account (for hybrid approach)
2. **Installation**: Install required packages (langchain, chromadb, openai, pymongo, pinecone-client, etc.)
3. **Configuration**: Set up environment variables for API keys and connection strings
4. **Data Preparation**: Prepare your documents or URLs for processing
5. **Run Notebooks**: Execute notebooks in order: basic → document → url → mongodb → mongo+pinecone


