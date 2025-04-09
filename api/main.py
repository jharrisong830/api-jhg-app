from fastapi import FastAPI

from api.routes.index import router

app = FastAPI()
app.include_router(router)
