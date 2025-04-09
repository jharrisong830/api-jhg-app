from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from api.routes.index import router

app = FastAPI(title="api.jhg.app")
app.include_router(router)

@app.exception_handler(404)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
            "request": f"{request.method} {request.url.path}",
            "status_code": exc.status_code
        }
    )
