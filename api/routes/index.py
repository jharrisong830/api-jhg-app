from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def root_hello():
    return "Hello!"
