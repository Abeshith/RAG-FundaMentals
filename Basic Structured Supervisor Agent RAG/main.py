import os
from utils.config import load_config, get_api_keys
from agents.supervisor import SupervisorAgent
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Setup LangSmith
os.environ["LANGSMITH_TRACING_V2"] = "true"
os.environ["LANGSMITH_PROJECT"] = "Modularized-Structured-RAG"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"

def setup_documents():
    """Load some sample documents"""
    urls = [
        "https://python.langchain.com/docs/get_started/introduction",
        "https://docs.python.org/3/tutorial/introduction.html"
    ]
    
    loader = WebBaseLoader(urls)
    docs = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)
    
    # Add to vector store
    from tools.search_tools import SearchTools
    tools = SearchTools()
    tools.vector_store.add_documents(chunks)
    print(f"Added {len(chunks)} documents to vector store")

def main():
    print("🤖 Starting Supervisor RAG System...")
    
    # Load config and API keys
    config = load_config()
    api_keys = get_api_keys()
    
    # Check API keys
    if not api_keys['groq']:
        print("❌ Missing GROQ_API_KEY")
        return
    
    # Setup documents (run once)
    print("📚 Setting up documents...")
    setup_documents()
    
    # Initialize supervisor
    supervisor = SupervisorAgent(config, api_keys)
    print("✅ Supervisor Agent Ready!")
    
    # Chat loop
    while True:
        try:
            query = input("\n🔍 Ask anything (or 'quit'): ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                break
            
            if not query:
                continue
            
            print("Processing...")
            result = supervisor.process(query)
            
            print(f"\n🎯 Routed to: {result['routed_to']} agent")
            print(f"💬 Answer: {result['answer']}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("👋 Goodbye!")

if __name__ == "__main__":
    main()
