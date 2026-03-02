"""Data models for file upload endpoint."""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from ragapi.utils import FormatConverter


class FileMetadata(BaseModel):
    """Metadata extracted from an uploaded file.

    Args:
        file_name (str): Original name of the uploaded file.
        page_count (int): Number of pages in the file.
    """

    model_config = ConfigDict(
        alias_generator=FormatConverter.snake_to_camel,
        populate_by_name=True,
    )

    file_name: str
    page_count: int = Field(ge=0)


class UploadResponse(BaseModel):
    """Response model for file upload.

    Args:
        file_name (str): Original name of the uploaded file.
        page_count (int): Number of pages in the file.
        message (str): Status message.
    """

    model_config = ConfigDict(
        alias_generator=FormatConverter.snake_to_camel,
        populate_by_name=True,
    )

    file_name: str
    page_count: int = Field(ge=0)
    message: str = "File uploaded successfully."
