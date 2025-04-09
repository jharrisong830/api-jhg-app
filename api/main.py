from fastapi import FastAPI

from routes.index import router

app = FastAPI()
app.include_router(router)
