from dataclasses import dataclass

from api.firebase.firestore import store
from api.firebase.auth import auth

@dataclass
class User:
    uid: str | None
    regId: str
    userName: str
    email: str
    displayName: str
    admin: bool
    registered: bool

    @staticmethod
    def from_dict(data: dict):
        return User(
            uid=data.get("uid"),
            regId=data.get("regId"),
            userName=data.get("userName"),
            email=data.get("email"),
            displayName=data.get("displayName"),
            admin=data.get("admin"),
            registered=data.get("registered")
        )
    
    def to_dict(self):
        return {
            "uid": self.uid,
            "regId": self.regId,
            "userName": self.userName,
            "email": self.email,
            "displayName": self.displayName,
            "admin": self.admin,
            "registered": self.registered
        }


def get_all_users() -> list[User]:
    query_snapshot = store.collection("users").get()
    return list(map(lambda doc: User.from_dict(doc.to_dict()), query_snapshot))

def get_user_by_uid(uid: str) -> User | None:
    query_snapshot = store.collection("users").where("uid", "==", uid).get()
    if len(query_snapshot) == 0:
        return None
    return User.from_dict(query_snapshot[0].to_dict())

def verify_user_id_token(id_token: str) -> str | None:
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token.get("uid")
        if uid is None:
            return None
        return uid
    except:
        return None
    