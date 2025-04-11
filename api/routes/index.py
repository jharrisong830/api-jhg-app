from fastapi import APIRouter

from .plancord.index import router as plancord_router
from api.util.projects import Project, projects

router = APIRouter()
router.include_router(plancord_router, prefix="/plancord")

@router.get("/hello")
async def root_hello():
    return "Hello!"

@router.get("/projects", response_model=list[Project])
async def get_projects():
    return projects
