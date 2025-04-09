import firebase_admin
from firebase_admin import credentials
from functools import lru_cache
from json import loads

from api.config import FirebaseConfig

@lru_cache
def get_firebase_config():
    return FirebaseConfig()

cred = credentials.Certificate(loads(get_firebase_config().firebase_admin_sdk_config))
app = firebase_admin.initialize_app(cred)
