from fastapi import APIRouter

from .plancord.index import router as plancord_router

router = APIRouter()
router.include_router(plancord_router, prefix="/plancord")

@router.get("/hello")
async def root_hello():
    return "Hello!"

