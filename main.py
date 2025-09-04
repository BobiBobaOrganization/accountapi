 # ANTONINI IDI NAHUY
import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.api import account_api
from src.config import get_settings
from src.dependencies import get_account_storage
from src.middlewares import error_handler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
)

get_account_storage()

app = FastAPI(
    title="Authentication Api",
    description="Api for user registration and registration authentication",
    version="0.0.0",
    contact={
        "name": "Anton",
        "email": "Prohvatilov.Anton@gmail.com",
    },
    openapi_tags=[{
        "name": "users",
        "description": "Operations with users.",
    }]
)

app.include_router(account_api.router)
error_handler.setup_exception_handlers(app)
app.add_middleware(error_handler.ErrorHandlerMiddleware)

@app.get("/info")
async def info():
    return JSONResponse(
        content={
            "application_version": get_settings().APPLICATION_VERSION,
            "test_mode": get_settings().TEST_MODE
        }
    )