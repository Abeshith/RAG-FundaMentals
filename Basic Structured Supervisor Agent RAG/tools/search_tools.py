from langchain_tavily import TavilySearch
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

class SearchTools:
    def __init__(self):
        self.web_search = TavilySearch(max_results=3)
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_store = Chroma(
            persist_directory="./chroma_db",
            embedding_function=self.embeddings
        )
    
    def search_web(self, query: str) -> str:
        """Search web using Tavily"""
        try:
            results = self.web_search.invoke(query)
            if isinstance(results, list) and results:
                return results[0].page_content
            return "No web results found"
        except Exception as e:
            return f"Web search error: {str(e)}"
    
    def search_documents(self, query: str) -> str:
        """Search local documents"""
        try:
            docs = self.vector_store.similarity_search(query, k=3)
            if docs:
                return "\n\n".join([doc.page_content for doc in docs])
            return "No documents found"
        except Exception as e:
            return f"Document search error: {str(e)}"
