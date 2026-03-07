"""API routers."""

from ragapi.app.routers.chat import router as chat_router
from ragapi.app.routers.root import router as root_router

routers = [root_router, chat_router]
