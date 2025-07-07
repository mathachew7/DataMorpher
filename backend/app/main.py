from api import router  # not from app.api

from fastapi import FastAPI

app = FastAPI(title="DataMorpher API")

app.include_router(router)
