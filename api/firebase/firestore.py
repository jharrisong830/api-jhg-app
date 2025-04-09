from api.firebase.configuration import app
from firebase_admin import firestore

store = firestore.client(app)
