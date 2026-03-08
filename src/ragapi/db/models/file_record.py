"""File record model for uploaded file metadata."""

from datetime import datetime

from sqlmodel import Field
from sqlmodel import SQLModel


class FileRecord(SQLModel, table=True):
    """Stores metadata for an uploaded file.

    Attributes:
        id: Primary key, auto-increment.
        file_name: Original uploaded file name.
        page_count: Number of pages (PDF) or sheets (Excel).
        chunk_count: Number of text chunks created.
        uploaded_at: Upload timestamp.
    """

    __tablename__ = "file_records"

    id: int | None = Field(default=None, primary_key=True)
    file_name: str
    page_count: int
    chunk_count: int
    uploaded_at: datetime = Field(default_factory=datetime.now)
