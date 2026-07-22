from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

from .exceptions import LLMServiceError
from .config import APP_NAME, APP_DESC, APP_VERSION
from .routes import router
from .logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title=APP_NAME,
    description=APP_DESC,
    version=APP_VERSION
)

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logger.info("Text summariser API started")

@app.get("/")
def home():
    return {
        "message": "Text Summariser API is running"
    }

@app.exception_handler(LLMServiceError)
async def llm_exception_handler(
    request: Request,
    exc: LLMServiceError
):
    return JSONResponse(
        status_code=503,
        content={
            "detail": str(exc)
        }
    )