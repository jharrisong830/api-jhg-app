from dataclasses import dataclass
import requests
from json import dumps
from google.cloud.firestore import FieldFilter

from api.firebase.firestore import store
from api.firebase.auth import auth
from api.config import get_firebase_config

@dataclass
class User:
    regId: str
    userName: str
    email: str
    displayName: str
    admin: bool
    registered: bool
    uid: str | None = None

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
    

@dataclass
class SigninResponse:
    token: str
    uid: str

    @staticmethod
    def from_response_dict(data: dict):
        return SigninResponse(
            token=data.get("idToken"),
            uid=data.get("localId")
        )
    
    def to_dict(self):
        return {
            "token": self.id_token,
            "uid": self.uid
        }


def get_all_users() -> list[User]:
    query_snapshot = store.collection("users").get()
    return list(map(lambda doc: User.from_dict(doc.to_dict()), query_snapshot))

def get_user_by_uid(uid: str) -> User | None:
    query_snapshot = store.collection("users").where(filter=FieldFilter("uid", "==", uid)).get()
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
    
def sign_in_user(email: str, password: str) -> SigninResponse | None:
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={get_firebase_config().firebase_api_key}"
    request_body = dumps({ "email": email, "password": password, "returnSecureToken": True })
    res = requests.post(url, data=request_body)
    if res.status_code != 200:
        return None
    return SigninResponse.from_response_dict(res.json())
    
def create_user(user: User):
    store.collection("users").document(user.regId).set(user.to_dict())