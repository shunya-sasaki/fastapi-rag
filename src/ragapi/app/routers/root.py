"""API router for root endpoints."""

from fastapi import APIRouter

from ragapi.utils import GitVersion

router = APIRouter()


@router.get("/version/")
def get_version() -> dict[str, str]:
    """Return the current application version."""
    return {"version": GitVersion.version()}
