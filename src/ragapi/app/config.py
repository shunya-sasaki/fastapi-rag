"""App configuration management."""

from ragapi.models import AppConfig

config = AppConfig.from_jsonfile("config.json")
