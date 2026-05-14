from dash.html import Base
from pydantic import BaseModel

# email hashed_pswd is_active


class User(BaseModel): # or import this ???
    pass

class UserCreate(User):
    pass

class UserPublic(User):
    pass

