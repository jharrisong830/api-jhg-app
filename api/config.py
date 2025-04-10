from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class FirebaseConfig(BaseSettings):
    firebase_admin_sdk_config: str
    firebase_api_key: str

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_firebase_config():
    return FirebaseConfig()
