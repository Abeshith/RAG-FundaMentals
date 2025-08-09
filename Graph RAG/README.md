# Graph RAG (Knowledge Graph Enhanced Retrieval)

A LangChain implementation of Knowledge Graph-enhanced Retrieval-Augmented Generation that combines traditional vector similarity search with graph-based entity relationships for more contextually rich and accurate responses.

## ✨ Key Highlights

- **Entity Extraction**: Uses spaCy NLP to identify named entities (people, organizations, locations) in documents
- **Knowledge Graph Construction**: Builds relationship networks between entities and documents
- **Community Detection**: Identifies clusters of related entities using Louvain algorithm
- **Hybrid Retrieval**: Combines vector similarity and graph traversal for better context
- **Path Analysis**: Finds relationships between entities through shortest path algorithms
- **Neighbor Enrichment**: Enhances retrieval with entity neighborhood context
- **Visual Graph Analysis**: Visualizes knowledge graphs with matplotlib and networkx

## 🏗️ How It Works

1. **Document Processing**
   - Text documents are loaded and processed
   - Named entities are extracted using spaCy NER
   - Graph nodes are created for documents and entities

2. **Graph Construction**
   - Documents are linked to their contained entities
   - Entities are linked to each other when co-occurring
   - Edge weights reflect relationship strength (frequency of co-occurrence)

3. **Retrieval Enhancement**
   - Traditional vector search finds relevant documents
   - Graph traversal discovers related entities
   - Community detection identifies conceptually related entity clusters
   - Combining both provides richer context to the LLM

4. **Answer Generation**
   - Text context from vector search + graph relationships are combined
   - The LLM generates answers based on both document content and entity relationships
   - Results include explicit relationship information

## 📊 Included Implementations

### Basic Graph RAG (`Graph_RAG.ipynb`)

A foundational implementation that:
- Creates a knowledge graph connecting documents and entities
- Performs vector similarity search to find relevant documents
- Enhances retrieval with entity relationship information
- Visualizes the document-entity graph structure

### Community-Based Hybrid RAG (`Hybrid_Search_RAG.ipynb`)

An advanced implementation that adds:
- Community detection to identify clusters of related entities
- Enhanced graph traversal techniques (shortest paths, neighbor analysis)
- Community-based context augmentation
- Graph analytics for deeper relationship understanding

## 🚀 Getting Started

### Prerequisites
```bash
pip install langchain langchain-groq langchain-community langchain-chroma
pip install spacy networkx matplotlib python-louvain sentence-transformers chromadb
python -m spacy download en_core_web_sm
```

### API Keys Required
- **GROQ_API_KEY**: For the Llama-3.3-70b-versatile model

## 🔄 Core Components

### Entity Extraction
```python
import spacy
nlp = spacy.load("en_core_web_sm")

for text in documents:
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents 
                if ent.label_ in ["PERSON", "ORG", "GPE", "LOC", "EVENT", "WORK_OF_ART"]]
```

### Graph Construction
```python
import networkx as nx
G = nx.Graph()

# Add document and entity nodes
G.add_node(doc_id, text=doc, type="document")
G.add_node(entity, type="entity")

# Connect documents to entities
G.add_edge(doc_id, entity)

# Connect co-occurring entities
for i, ent1 in enumerate(entities):
    for ent2 in entities[i+1:]:
        G.add_edge(ent1, ent2)
```

### Community Detection
```python
from community import community_louvain
partition = community_louvain.best_partition(G)
communities = {}
for entity, community_id in partition.items():
    if community_id not in communities:
        communities[community_id] = []
    communities[community_id].append(entity)
```

### Hybrid Retrieval
```python
# Vector retrieval
relevant_docs = vectorstore.similarity_search(question, k=3)

# Graph-based context enhancement
related_entities = set()
for entity in question_entities:
    # Get entity neighbors
    neighbors = get_entity_neighbors(entity)
    related_entities.update([n[0] for n in neighbors])
    
    # Get community members
    community_members = get_community_entities(entity)
    related_entities.update(community_members[:5])
```

## 🎯 Use Cases

- **Research & Analysis**: Find connections between entities in academic papers
- **Intelligence Analysis**: Discover hidden relationships in complex datasets
- **Content Recommendation**: Suggest related content based on entity relationships
- **Knowledge Discovery**: Uncover non-obvious connections between concepts
- **Narrative Understanding**: Comprehend complex storylines with multiple characters and locations

## 🔍 Advantages Over Traditional RAG

| Feature | Traditional RAG | Graph RAG |
|---------|----------------|-----------|
| Context Understanding | Limited to document chunks | Includes entity relationships |
| Connection Discovery | Implicit through text | Explicit through graph structure |
| Related Concepts | Based on text similarity | Based on relationship structure |
| Information Clustering | Flat document structure | Community-based concept clustering |
| Result Explanation | Limited relationship context | Rich relationship information |

## 📝 File Structure

```
Graph RAG/
├── Graph_RAG.ipynb              # Basic graph-enhanced RAG implementation
├── Hybrid_Search_RAG.ipynb      # Advanced community-based hybrid RAG
└── README.md                    # This file
```
