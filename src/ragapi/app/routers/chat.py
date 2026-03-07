"""API router for chat endpoints."""

from fastapi import APIRouter
from langchain_core.messages import HumanMessage
from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama

from ragapi.models import ChatRequest
from ragapi.models import ChatResponse

router = APIRouter(prefix="/chat", tags=["chat"])

llm = ChatOllama(model="gemma3", base_url="http://ollama:11434")


@router.post("/", response_model=ChatResponse)
async def chat(request_body: ChatRequest) -> ChatResponse:
    """Generate a chat response using Ollama."""
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=request_body.query),
    ]
    response = await llm.ainvoke(messages)
    return ChatResponse(answer=str(response.content))
