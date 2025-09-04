import logging
import traceback
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("error_handler")
logging.basicConfig(level=logging.ERROR)

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException as exc:
            logger.error(f"HTTPException: {exc.detail} (Status: {exc.status_code})")
            return JSONResponse(
                status_code=exc.status_code,
                content={"error": exc.detail}
            )
        except Exception as exc:
            error_trace = traceback.format_exc()
            logger.error(f"Unhandled Exception: {exc}\n{error_trace}")
            return JSONResponse(
                status_code=500,
                content={"error": "Internal Server Error"}
            )

def setup_exception_handlers(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def custom_http_exception_handler(request: Request, exc: HTTPException):
        logger.error(f"HTTPException: {exc.detail} (Status: {exc.status_code})")
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.detail}
        )

    @app.exception_handler(Exception)
    async def custom_general_exception_handler(request: Request, exc: Exception):
        error_trace = traceback.format_exc()
        logger.error(f"Unhandled Exception: {exc}\n{error_trace}")
        return JSONResponse(
            status_code=500,
            content={"error": "Internal Server Error"}
        )

    app.add_exception_handler(HTTPException, custom_http_exception_handler)
    app.add_exception_handler(Exception, custom_general_exception_handler)