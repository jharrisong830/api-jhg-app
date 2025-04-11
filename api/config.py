# from dataclasses import dataclass
# from functools import lru_cache
# from os import environ
# from dotenv import load_dotenv

# load_dotenv()

# @dataclass
# class FirebaseConfig():
#     firebase_admin_sdk_config: str = environ.get("FIREBASE_ADMIN_SDK_CONFIG")
#     firebase_api_key: str = environ.get("FIREBASE_API_KEY")

# @lru_cache
# def get_firebase_config():
#     return FirebaseConfig()
