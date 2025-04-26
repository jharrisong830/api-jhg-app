from fastapi import APIRouter
from fastapi.responses import RedirectResponse

# from .plancord.index import router as plancord_router
from api.util.projects import Project, projects

router = APIRouter()
# router.include_router(plancord_router, prefix="/plancord")

@router.get("/", status_code=307)
async def root_redirect():
    return RedirectResponse(url="/docs")

@router.get("/projects", response_model=list[Project])
async def get_projects():
    return projects
