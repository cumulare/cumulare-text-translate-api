from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> None:
    """Returns healthceck."""
