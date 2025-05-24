from fastapi import APIRouter, HTTPException
from dataclasses import dataclass

from api.util.users import verify_user_id_token
from api.util.events import Event, get_user_events, create_event, get_event_by_id

@dataclass
class TokenBody:
    token: str

@dataclass
class CreateEventBody:
    token: str
    event: Event

router = APIRouter()

@router.post("/new", response_model=Event, responses={401: {"description": "Invalid token"}})
async def create_event_request(body: CreateEventBody):
    uid = verify_user_id_token(body.token)
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token")
    create_event(body.event)
    return body.event

@router.post("/user/{user_id}", response_model=list[Event], responses={401: {"description": "Invalid token"}})
async def all_users(user_id: str, body: TokenBody):
    uid = verify_user_id_token(body.token)
    if not uid:
        raise HTTPException(status_code=401, detail="Invalid token")
    events = get_user_events(user_id)
    return events

@router.post("/{id}", response_model=Event, responses={401: {"description": "Invalid token"}, 404: {"description": "Event not found"}})
async def event_by_id(id: str, body: TokenBody):
    authUid = verify_user_id_token(body.token)
    if not authUid:
        raise HTTPException(status_code=401, detail="Invalid token")
    event = get_event_by_id(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event
