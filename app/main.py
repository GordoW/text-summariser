from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .exceptions import LLMServiceError
from .config import APP_NAME, APP_DESC, APP_VERSION
from .routes import router


app = FastAPI(
    title=APP_NAME,
    description=APP_DESC,
    version=APP_VERSION
)


app.include_router(router)


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