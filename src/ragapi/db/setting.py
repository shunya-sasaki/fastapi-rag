"""Database settings for the application."""

from pydantic import BaseSettings


class DataBaseSettings(BaseSettings):
    """Configuration settings for PostgreSQL database connection."""

    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_port: str
