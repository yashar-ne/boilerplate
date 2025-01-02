from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    email: str
    is_superuser: bool
    is_active: bool

class UserPrivate(User):
    hashed_password: str