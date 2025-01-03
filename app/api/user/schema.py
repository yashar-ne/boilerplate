from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    email: str
    is_superuser: bool
    is_active: bool

class UserSchemaPrivate(UserSchema):
    hashed_password: str