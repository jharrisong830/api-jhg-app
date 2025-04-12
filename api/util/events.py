from dataclasses import dataclass
from google.cloud.firestore import FieldFilter, Or

from api.firebase.firestore import store

@dataclass
class Event:
    id: str
    title: str
    description: str
    location: str
    color: str
    start: str # iso formatted datetime string
    end: str
    allDay: bool
    organizer: str
    invitees: list[str]

    @staticmethod
    def from_dict(data: dict):
        return Event(
            id=data.get("id"),
            title=data.get("title"),
            description=data.get("description"),
            location=data.get("location"),
            color=data.get("color"),
            start=data.get("start"),
            end=data.get("end"),
            allDay=data.get("allDay"),
            organizer=data.get("organizer"),
            invitees=data.get("invitees")
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "color": self.color,
            "start": self.start,
            "end": self.end,
            "allDay": self.allDay,
            "organizer": self.organizer,
            "invitees": self.invitees
        }


def get_user_events(user_id: str) -> list[Event]:
    query_snapshot = store.collection("events").where(filter=Or([
        FieldFilter("organizer", "==", user_id),
        FieldFilter("invitees", "array_contains", user_id)
    ])).get()
    return list(map(lambda doc: Event.from_dict(doc.to_dict()), query_snapshot))
    
def create_event(event: Event):
    store.collection("events").document(event.id).set(event.to_dict())