from dataclasses import dataclass

from api.firebase.firestore import store

@dataclass
class User:
    uid: str | None
    regId: str
    userName: str
    email: str
    displayName: str
    admin: bool
    registered: bool

def get_all_users():
    query_snapshot = store.collection("users").get()
    return list(map(lambda doc: doc.to_dict(), query_snapshot))
