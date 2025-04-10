import firebase_admin
from firebase_admin import credentials
from json import loads

from api.config import get_firebase_config

cred = credentials.Certificate(loads(get_firebase_config().firebase_admin_sdk_config))
app = firebase_admin.initialize_app(cred)
