"""Data models for chat endpoint."""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from ragapi.utils import FormatConverter


class RagChatRequest(BaseModel):
    """Request model for chat endpoint.

    Args:
        query (str): User input query.
        file_indices (list[int]): Reference file index numbers
            for context retrieval.
        preset_prompts (list[str]): Preset prompt templates
            to augment the query.
    """

    model_config = ConfigDict(
        alias_generator=FormatConverter.snake_to_camel,
        populate_by_name=True,
    )

    query: str = Field(min_length=1)
    file_indices: list[int] = Field(default_factory=list)
    preset_prompts: list[str] = Field(default_factory=list)


class RagChatResponse(BaseModel):
    """Response model for chat endpoint.

    Args:
        answer (str): Generated response text.
        sources (list[str]): Source references used
            in generating the response.
    """

    model_config = ConfigDict(
        alias_generator=FormatConverter.snake_to_camel,
        populate_by_name=True,
    )

    answer: str
    sources: list[str] = Field(default_factory=list)
