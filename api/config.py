from pydantic_settings import BaseSettings, SettingsConfigDict

class FirebaseConfig(BaseSettings):
    firebase_admin_sdk_config: str

    model_config = SettingsConfigDict(env_file=".env")