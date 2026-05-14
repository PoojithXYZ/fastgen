from fastapi import APIRouter


router = APIRouter(prefix="?")

@router.get('/me')
def abcd():
    pass

@router.get('/users/{id}')
def abcd2(id: str):
    pass

@router.post('/users/registration_or_what')
def register(name:str):
    pass

def create_user(): # same stuff in auth ???
    pass

def update_user_profile(): # same stuff in auth ???
    pass

