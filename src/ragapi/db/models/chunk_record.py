"""Chunk record model for text chunk metadata."""

from sqlmodel import Field
from sqlmodel import SQLModel


class ChunkRecord(SQLModel, table=True):
    """Stores metadata for a text chunk in ChromaDB.

    Attributes:
        id: Primary key, auto-increment.
        file_name: Source file name.
        page_number: Page (PDF) or sheet index (Excel).
        chunk_index: Chunk order within the page.
        file_record_id: Foreign key to file_records.id.
    """

    __tablename__ = "chunk_records"

    id: int | None = Field(default=None, primary_key=True)
    file_name: str
    page_number: int
    chunk_index: int
    file_record_id: int | None = Field(
        default=None, foreign_key="file_records.id"
    )
