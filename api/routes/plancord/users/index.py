from fastapi import APIRouter, HTTPException
from dataclasses import dataclass

from api.util.users import User, SigninResponse, get_all_users, verify_user_id_token, sign_in_user, get_user_by_uid

@dataclass
class SigninBody:
    email: str
    password: str

@dataclass
class TokenBody:
    token: str

@dataclass
class CreateUserBody:
    token: str
    user: User

router = APIRouter()

@router.post("/", response_model=list[User], responses={401: {"description": "Invalid token"}})
async def all_users(body: TokenBody):
    uid = verify_user_id_token(body.token)
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token")
    users = get_all_users()
    return users

@router.post("/new", response_model=User, responses={401: {"description": "Invalid token"}})
async def create_user(body: CreateUserBody):
    uid = verify_user_id_token(body.token)
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token")
    return body.user

@router.post("/signin", response_model=SigninResponse, responses={401: {"description": "Invalid credentials"}})
async def sign_in(body: SigninBody):
    res = sign_in_user(body.email, body.password)
    if not res:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return res

@router.post("/me", response_model=User, responses={401: {"description": "Invalid token"}})
async def me(body: TokenBody):
    uid = verify_user_id_token(body.token)
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = get_user_by_uid(uid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{id}", response_model=User, responses={401: {"description": "Invalid token"}})
async def update_user(id: str, body: CreateUserBody):
    uid = verify_user_id_token(body.token)
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = get_user_by_uid(id)
    if not user or not user.admin: # check if requester is admin
        raise HTTPException(status_code=403, detail="Forbidden")
    create_user(body.user) # creating is same as updating in firestore
    return body.user
