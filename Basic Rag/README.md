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

## Getting Started

1. **Prerequisites**: Python 3.8+, API keys for LLM providers
2. **Installation**: Install required packages (langchain, chromadb, openai, etc.)
3. **Configuration**: Set up environment variables for API keys
4. **Data Preparation**: Prepare your documents or URLs for processing
5. **Run Notebooks**: Execute notebooks in order: basic → document → url


