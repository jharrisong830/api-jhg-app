from fastapi import APIRouter

from .users.index import router as users_router
from .events.index import router as events_router

router = APIRouter()
router.include_router(users_router, prefix="/users")
router.include_router(events_router, prefix="/events")
