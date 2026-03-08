"""Database manager for PostgreSQL connections."""

import os
from collections.abc import Generator

from sqlmodel import Session
from sqlmodel import SQLModel
from sqlmodel import create_engine

from ragapi.db.models import ChunkRecord  # noqa: F401
from ragapi.db.models import FileRecord  # noqa: F401
from ragapi.db.setting import DatabaseSettings


class DatabaseManager:
    """Manages PostgreSQL database connections and sessions."""

    def __init__(self) -> None:
        """Initialize database manager with PostgreSQL connection."""
        settings = DatabaseSettings()
        user = os.getenv("POSTGRES_USER", "rag")
        password = os.getenv("POSTGRES_PASSWORD", "rag")
        host = os.getenv("POSTGRES_HOST", "db")
        port = os.getenv("POSTGRES_PORT", "5432")
        db = os.getenv("POSTGRES_DB", "rag_metadata")
        url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
        self.engine = create_engine(url)

    def create_tables(self) -> None:
        """Create all registered SQLModel tables."""
        SQLModel.metadata.create_all(self.engine)

    def get_session(self) -> Generator[Session, None, None]:
        """Yield a database session for FastAPI dependency injection."""
        with Session(self.engine) as session:
            yield session
