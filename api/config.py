from functools import lru_cache
from os import environ
from pydantic_settings import BaseSettings, SettingsConfigDict

class FirebaseConfig(BaseSettings):
    firebase_admin_sdk_config: str = environ.get("FIREBASE_ADMIN_SDK_CONFIG")
    firebase_api_key: str = environ.get("FIREBASE_API_KEY")

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_firebase_config():
    return FirebaseConfig()
