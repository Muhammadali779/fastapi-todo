from fastapi import FastAPI

from app.api.router import router

app = FastAPI(title="Todo List", version="1.0.0", description="FastAPI Todo List API")

app.include_router(router, prefix="/api")
