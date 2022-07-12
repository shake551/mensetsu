from fastapi import FastAPI

from api.routers import interview, user

app = FastAPI()
app.include_router(interview.router)
app.include_router(user.router)
