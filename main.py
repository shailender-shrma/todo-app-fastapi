from fastapi import FastAPI
from route.route import router

app = FastAPI()

app.include_router(router)
