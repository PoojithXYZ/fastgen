from fastapi import APIRouter, Depends
from app.modules.users.routers import router as users_module_router
from app.modules.auth.dependencies import verify_token

users_public_router = APIRouter()

users_public_router.include_router(
    users_module_router,
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(verify_token)]
)

# api_router.include_router(user_v1_router, prefix="/v1/users", tags=["Users"])

