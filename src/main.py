from fastapi import FastAPI

from src.routes import api_router

app = FastAPI()
app.include_router(router=api_router)
