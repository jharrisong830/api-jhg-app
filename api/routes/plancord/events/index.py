from fastapi import APIRouter, HTTPException
from dataclasses import dataclass

from api.util.users import verify_user_id_token
from api.util.events import Event, get_user_events

@dataclass
class TokenBody:
    token: str

router = APIRouter()

@router.post("/user/{user_id}", response_model=list[Event], responses={401: {"description": "Invalid token"}})
async def all_users(user_id: str, body: TokenBody):
    uid = verify_user_id_token(body.token)
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token")
    events = get_user_events(user_id)
    return events
