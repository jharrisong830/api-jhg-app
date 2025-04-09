from fastapi import APIRouter

from .users.index import router as users_router

router = APIRouter()
router.include_router(users_router, prefix="/users")
