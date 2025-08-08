# Dynamic Knowledge Update RAG

A LangChain implementation demonstrating how to build a dynamic, self-updating Retrieval-Augmented Generation (RAG) system that can refresh its knowledge base on-the-fly without requiring retraining.

## ✨ Key Highlights

- **Dynamic Document Management**: Add, update, and delete documents in real-time
- **Version Control**: Automatically tracks document versions and timestamps
- **Content Change Detection**: Only updates when document content actually changes
- **Time-Aware Retrieval**: Includes document timestamps in context for freshness awareness
- **Batch Updates**: Efficiently update multiple documents at once
- **Zero Downtime**: Knowledge base remains available during updates
- **Metadata Enrichment**: Each chunk includes update time and version information

## 🏗️ How It Works

1. **Document Management**
   - Each document has a unique ID for tracking and updating
   - System detects if content has changed before updating
   - Old vector embeddings are automatically deleted when updated

2. **Vector Store Integration**
   - Chroma vector database with SentenceTransformer embeddings
   - Documents stored with rich metadata including timestamps
   - Efficient vector ID tracking for managing updates

3. **Version History**
   - Each document update is tracked with timestamp and version number
   - Previous versions are removed from the vector store to avoid duplicates
   - In-memory tracking for quick version reference

4. **Query Process**
   - Semantic search finds the most relevant documents
   - Date stamps are included in context to show information freshness
   - LLM generates answers with awareness of update timelines

## 📊 Example Use Cases

### Policy Updates
```python
# Initial policy document
add_or_update_document("policy", """
Work Policy:
- Remote work: 2 days per week
- Vacation: 20 days per year
""")

# Later, policy is updated with new information
add_or_update_document("policy", """
Work Policy (Updated):
- Remote work: 4 days per week
- Vacation: 25 days per year
- Health days: 3 days per month
""")
```

### Product Catalog Changes
```python
# Initial product listing
add_or_update_document("products", """
Product Catalog 2025:
- AI Assistant: $99/month
- Data Analytics Tool: $199/month
- Security Suite: $299/month
""")

# Updated with new pricing and products
add_or_update_document("products", """
Product Catalog 2025 (New Pricing):
- AI Assistant: $79/month (20% off!)
- Data Analytics Tool: $149/month (price drop!)
- Security Suite: $299/month
- New: Mobile App: $49/month
""")
```

### Evolving Company News
```python
# January update
add_or_update_document("company_news", """
Company News - January 2025:
- Hired 50 new employees
- Opened office in Tokyo
- Revenue increased 30%
""")

# February update with additional developments
add_or_update_document("company_news", """
Company News - February 2025:
- Hired 100 more employees (total 150 new hires)
- Tokyo office fully operational
- Revenue increased 45% (updated numbers)
- Acquired startup TechFlow
""")
```

## 🚀 Getting Started

### Prerequisites
```bash
pip install langchain langchain-groq sentence-transformers chromadb langchain_community
```

### API Keys Required
- **GROQ_API_KEY**: For the Llama-3.3-70b-versatile model

### Basic Usage

```python
# Add a new document
add_or_update_document("doc_id", "Document content goes here")

# Query the knowledge base
answer = query_knowledge_base("What information are you looking for?")
print(answer)

# Update an existing document
add_or_update_document("doc_id", "Updated content with new information")

# Add multiple documents at once
documents = {
    "doc1": "First document content",
    "doc2": "Second document content",
    "doc3": "Third document content"
}
update_multiple_documents(documents)

# Check knowledge base status
show_knowledge_base_status()
```

## 🔄 Dynamic RAG vs. Static RAG

| Feature | Static RAG | Dynamic RAG |
|---------|------------|-------------|
| Document Updates | Requires full reindexing | Real-time updates |
| Information Freshness | Can become outdated | Always current |
| Version Tracking | Typically not available | Built-in timestamps |
| Update Frequency | Periodic batch updates | Continuous updates |
| Storage Efficiency | May store duplicates | Removes outdated versions |
| Development Workflow | Rebuild required | Zero-downtime updates |
| Content Change Detection | Manual tracking | Automatic detection |

## 🛠️ Core Components

### Document Store
```python
document_store = {
    "doc_id": {
        "content": "The actual document content",
        "vector_ids": ["id1", "id2"],  # IDs in the vector store
        "last_updated": "2025-01-15T10:30:45"  # ISO timestamp
    }
}
```

### Vector Store
```python
from langchain.vectorstores import Chroma
vectorstore = Chroma(
    collection_name="dynamic_kb", 
    embedding_function=embeddings
)
```

### Document Update Function
```python
def add_or_update_document(doc_id, content):
    # Check if document changed
    # Remove old version if it exists
    # Add new version with metadata
    # Store tracking info
```

### Query Function
```python
def query_knowledge_base(question):
    # Retrieve relevant documents
    # Format context with timestamps
    # Generate answer with LLM
```

## 🔍 Advanced Features

### Batch Operations
The system supports batch updates for efficiency when multiple documents need to be updated at once.

### Content Change Detection
Avoids unnecessary updates by comparing new content with existing versions.

### Status Reporting
Built-in function to view the current state of all documents in the knowledge base.

### Time-Aware Context
Document timestamps are included in the context, helping the LLM understand information freshness.

## 📝 File Structure

```
Dynamic RAG/
├── Dynamic_Knowledge_Update_RAG.ipynb    # Main implementation
└── README.md                            # This file
```

## 🎯 Use Cases

- **Company Knowledge Base**: Keep internal documentation and policies current
- **Product Catalogs**: Update pricing and features in real-time
- **News Systems**: Continuously update with latest developments
- **Technical Documentation**: Keep instructions and specifications up-to-date
- **Customer Support**: Maintain current answers for support questions
