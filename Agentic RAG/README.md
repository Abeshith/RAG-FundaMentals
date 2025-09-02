# 🤖 Agentic RAG Implementations

This folder contains advanced RAG implementations that incorporate agent-based architectures and intelligent routing mechanisms to enhance retrieval and generation capabilities.

## 📚 Contents

### 1. [Agentic_RAG.ipynb](./Agentic_RAG.ipynb)
An implementation of RAG with autonomous agent capabilities for improved retrieval and response generation.
- **Key Features**:
  - Autonomous decision making
  - Self-improving retrieval strategies
  - Context-aware response generation
  - Dynamic query reformulation

### 2. [RAG_Agent_WIth_Memory.ipynb](./RAG_Agent_WIth_Memory.ipynb)
A conversational RAG system that maintains conversation history for contextual responses.
- **Key Features**:
  - Conversation history tracking
  - Context-aware document retrieval
  - Memory-augmented generation
  - Source attribution and tracking
  - PDF document processing capabilities
  - Persistent vector storage

### 3. [Rag_with_langgraph.ipynb](./Rag_with_langgraph.ipynb)
Implementation using LangGraph for structured RAG workflows.
- **Key Features**:
  - Graph-based workflow orchestration
  - Conditional execution paths
  - State management
  - Complex decision trees

### 4. [Routed_RAG_With_LLM_Router.ipynb](./Routed_RAG_With_LLM_Router.ipynb)
A routing-based RAG system that intelligently directs queries to appropriate knowledge sources.
- **Key Features**:
  - LLM-based query routing
  - Multiple knowledge source handling
  - Dynamic retrieval strategy selection
  - Optimized response generation

## 🛠️ Technologies Used
- LangChain
- LangGraph
- ChromaDB
- Groq LLMs
- HuggingFace Embeddings
- PDF Processing Tools

## 🔑 Key Concepts
1. **Agent Architecture**: Autonomous decision-making in RAG systems
2. **Memory Management**: Conversation history and context preservation
3. **Workflow Orchestration**: Structured processing with LangGraph
4. **Intelligent Routing**: Dynamic query direction and processing
5. **State Management**: Maintaining system state across interactions

## 🚀 Getting Started

### Prerequisites
```bash
pip install langchain-groq langgraph chromadb langchain-huggingface langchain-community pypdf langchain_chroma sentence-transformers
```

### Environment Variables
```python
GROQ_API_KEY=your_groq_api_key  # Required for LLM access
```

### Usage Example
```python
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Initialize components
llm = ChatGroq(model_name="llama-3.3-70b-versatile")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create vector store
vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings)

# Set up RAG pipeline
# ... (see individual notebooks for specific implementations)
```
