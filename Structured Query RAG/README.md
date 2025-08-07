# Structured Query RAG (Text-to-SQL)

A LangChain implementation that combines Retrieval-Augmented Generation (RAG) with Text-to-SQL capabilities, allowing users to query databases using natural language.

## ✨ Key Highlights

- **Natural Language to SQL**: Converts plain English questions into precise SQL queries
- **Schema-Aware Retrieval**: Uses vector embeddings to find the most relevant database tables and columns
- **RAG for SQL Generation**: Retrieves relevant schema before generating SQL, improving accuracy
- **Result Interpretation**: Translates raw SQL results back into natural language answers
- **SQLite Integration**: Demonstrates with a sample company database (employees and departments)
- **Groq + Llama Integration**: Leverages Llama-3.3-70b for high-quality SQL generation and answer synthesis

## 🏗️ How It Works

1. **Database Schema Embedding**
   - Extracts table and column information from the database
   - Stores schema details in a vector database (Chroma)
   - Includes sample data to help the model understand data patterns

2. **Natural Language Query Processing**
   - User submits a plain English question
   - System retrieves the most relevant schema information using semantic search
   - LLM generates a SQL query based on the question and schema context

3. **Query Execution**
   - The generated SQL is executed against the database
   - Results are captured along with column metadata

4. **Answer Generation**
   - Raw SQL results, original question, and SQL query are sent to the LLM
   - Model generates a natural language answer based on the results
   - Response includes the answer, SQL query, and formatted results

## 🛠️ Components

### Database Setup
- **SQLite Database**: Simple in-memory relational database
- **Sample Tables**: 
  - `employees`: Records with name, department, salary, hire date, and age
  - `departments`: Department records with name, budget, and manager

### Vector Store
- **Chroma Vector Database**: Stores table schemas and metadata
- **Embedding Model**: HuggingFace sentence-transformers/all-MiniLM-L6-v2
- **Schema Documents**: Each table's structure stored as a separate document

### LLM Integration
- **ChatGroq with Llama-3.3-70b**: Handles both SQL generation and answer synthesis
- **Temperature Setting**: 0.1 for precise and deterministic SQL generation
- **Structured Prompting**: Specialized prompts for SQL generation vs. answer creation

## 📊 Example Queries

The notebook demonstrates the system with various types of queries:

### Basic Aggregation
- "How many employees are there in total?"
- "What's the total payroll for all employees?"

### Filtering Operations
- "Who are the employees in the Engineering department?"
- "Show me employees older than 30 years"
- "Which departments have budgets over 250000?"

### Group By & Analytics
- "What is the average salary by department?"
- "Show me the oldest employee in each department"

### Comparisons
- "Which department has the highest budget?"


## 🔄 Comparison with Other RAG Approaches

### Traditional Document RAG vs. Structured Query RAG

| Feature | Traditional RAG | Structured Query RAG |
|---------|----------------|----------------------|
| Data Source | Unstructured documents | Structured databases |
| Query Language | Natural language | Natural language → SQL → Results → Natural language |
| Retrieval Focus | Document chunks | Database schema |
| Answer Generation | Direct from retrieved chunks | SQL execution + result interpretation |
| Hallucination Risk | Higher (may confabulate) | Lower (grounded in actual query results) |
