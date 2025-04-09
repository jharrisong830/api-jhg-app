from fastapi import APIRouter, HTTPException

from api.util.users import User, get_all_users, verify_user_id_token

router = APIRouter()

@router.get("/", response_model=list[User], responses={401: {"description": "Invalid token"}})
async def all_users(token: str):
    uid = verify_user_id_token(token)
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token")
    users = get_all_users()
    return users
