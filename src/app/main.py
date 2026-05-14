from fastapi import FastAPI
from app.routers.users import users_public_router

app = FastAPI()

# Mount the aggregated routers
app.include_router(users_public_router, prefix="/api/v1")

