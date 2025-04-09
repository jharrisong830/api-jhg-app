from api.firebase.configuration import app
from firebase_admin import auth as authentication

auth = authentication.Client(app)
