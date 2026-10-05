from fastapi import FastAPI

from api.routes import router


app = FastAPI(
    title="AI Business Process Automation Agent",
    version="1.0.0",
)

app.include_router(router)
