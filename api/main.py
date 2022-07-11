from fastapi import FastAPI

from api.routers import interview

app = FastAPI()
app.include_router(interview.router)
