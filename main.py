from logging.config import dictConfig

from api.api import api_router
from core.config import logging_conf, settings
from core.constants import PROD
from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from exceptions import SoundHTTPException

dictConfig(logging_conf)

openapi_url = (
    f"{settings.api_v1_path}/openapi.json"
    if settings.environment != PROD
    else ""
)

app = FastAPI(title=settings.project_name, openapi_url=openapi_url)

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(api_router, prefix=settings.api_v1_path)


@app.exception_handler(SoundHTTPException)
async def fin_exception_handler(_: Request, exc: SoundHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message, "error_code": exc.error_code},
    )


if settings.backend_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.backend_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.project_name,
        version="1.0.0",
        description="FinKG API",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": 'Enter: **"Bearer &lt;JWT&gt;"**, where JWT is the access token',
        }
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
