from fastapi import FastAPI

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