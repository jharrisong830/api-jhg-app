from fastapi import APIRouter, HTTPException
from dataclasses import dataclass

from api.util.users import User, get_all_users, verify_user_id_token, sign_in_user

@dataclass
class SigninBody:
    email: str
    password: str

router = APIRouter()

@router.get("/", response_model=list[User], responses={401: {"description": "Invalid token"}})
async def all_users(token: str):
    uid = verify_user_id_token(token)
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token")
    users = get_all_users()
    return users

@router.post("/signin", response_model=str, responses={401: {"description": "Invalid credentials"}})
async def sign_in(body: SigninBody):
    id_token = sign_in_user(body.email, body.password)
    if not id_token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return id_token
