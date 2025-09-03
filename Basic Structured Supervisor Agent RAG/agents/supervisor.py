from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from tools.search_tools import SearchTools

# Define the state that flows through the graph
class SupervisorState(TypedDict):
    query: str
    agent_choice: str
    search_results: str
    final_answer: str

class SupervisorAgent:
    def __init__(self, config: dict, api_keys: dict):
        self.llm = ChatGroq(
            model=config['groq']['model'],
            temperature=config['groq']['temperature'],
            api_key=api_keys['groq']
        )
        self.tools = SearchTools()
        
        # Create the graph
        self.graph = self._build_graph()
    
    def _build_graph(self) -> StateGraph:
        """Build the LangGraph workflow"""
        graph = StateGraph(SupervisorState)
        
        # Add nodes
        graph.add_node("route_query", self._route_query)
        graph.add_node("web_search", self._web_search)
        graph.add_node("doc_search", self._doc_search)
        graph.add_node("generate_answer", self._generate_answer)
        
        # Define the flow
        graph.set_entry_point("route_query")
        
        # Conditional routing based on agent choice
        graph.add_conditional_edges(
            "route_query",
            self._decide_agent,
            {
                "web": "web_search",
                "doc": "doc_search"
            }
        )
        
        # Both search nodes go to answer generation
        graph.add_edge("web_search", "generate_answer")
        graph.add_edge("doc_search", "generate_answer")
        graph.add_edge("generate_answer", END)

        app = graph.compile()

        app.get_graph().draw_mermaid_png(output_file_path="graph.png")
        
        return app
    
    def _route_query(self, state: SupervisorState) -> SupervisorState:
        """Decide which agent should handle the query"""
        routing_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a query router. Decide if this query needs current web information or can be answered from existing documents. Respond with only 'web' or 'doc'."),
            ("human", "{query}")
        ])
        
        messages = routing_prompt.format_messages(query=state["query"])
        response = self.llm.invoke(messages)
        
        # Simple decision logic
        choice = "web" if "web" in response.content.lower() else "doc"
        state["agent_choice"] = choice
        return state
    
    def _decide_agent(self, state: SupervisorState) -> Literal["web", "doc"]:
        """Return the routing decision"""
        return state["agent_choice"]
    
    def _web_search(self, state: SupervisorState) -> SupervisorState:
        """Perform web search"""
        results = self.tools.search_web(state["query"])
        state["search_results"] = f"Web Search Results:\n{results}"
        return state
    
    def _doc_search(self, state: SupervisorState) -> SupervisorState:
        """Perform document search"""
        results = self.tools.search_documents(state["query"])
        state["search_results"] = f"Document Search Results:\n{results}"
        return state
    
    def _generate_answer(self, state: SupervisorState) -> SupervisorState:
        """Generate final answer using LLM"""
        answer_prompt = ChatPromptTemplate.from_messages([
            ("system", "Answer the user's question using the provided search results. Be concise and helpful."),
            ("human", "Question: {query}\n\nSearch Results: {results}")
        ])
        
        messages = answer_prompt.format_messages(
            query=state["query"],
            results=state["search_results"]
        )
        
        response = self.llm.invoke(messages)
        state["final_answer"] = response.content
        return state
    
    def process(self, query: str) -> dict:
        """Process a query through the supervisor workflow"""
        initial_state = SupervisorState(
            query=query,
            agent_choice="",
            search_results="",
            final_answer=""
        )
        
        # Run the graph
        result = self.graph.invoke(initial_state)
        
        return {
            "query": result["query"],
            "routed_to": result["agent_choice"],
            "answer": result["final_answer"]
        }
