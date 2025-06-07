from langchain.tools.retriever import create_retriever_tool 
from philoagents.application.rag.retreievers import get_retriever 
from philoagents.config import settings

retreiver = get_retriever(
    embedding_model_id=settings.EMBEDDING_MODEL_ID,
    k=settings.RAG_TOP_K,
    device=settings.RAG_DEVICE
)

retreiver_tool = create_retriever_tool(
    retreiver,
     "retrieve_philosopher_context",
    "Search and return information about a specific philosopher. Always use this tool when the user asks you about a philosopher, their works, ideas or historical context.",
)

tools = [retreiver_tool]
