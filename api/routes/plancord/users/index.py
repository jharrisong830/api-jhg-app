from fastapi import APIRouter

from api.util.users import User, get_all_users

router = APIRouter()

@router.get("/", response_model=list[User])
async def all_users():
    users = get_all_users()
    return users
