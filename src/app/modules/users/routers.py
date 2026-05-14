from fastapi import APIRouter, Depends, HTTPException, status
from . import services, models, dependencies

router = APIRouter()

# which stuff should be in services.py ???

@router.post("/", response_model=models.UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user_in: models.UserCreate, db=Depends(dependencies.get_db)):
    return services.user.create(db, obj_in=user_in)

@router.get("/me", response_model=models.UserRead)
def get_my_profile(current_user=Depends(dependencies.get_current_user)):
    return current_user


def get_user():
    pass

def update_user():
    pass


def delete_user():
    pass

