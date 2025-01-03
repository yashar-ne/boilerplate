from fastapi import APIRouter

from app.api.user.schema import AllUserSchema
from app.api.user.schema import UserSchema
from app.api.user.service import UserService

router = APIRouter(prefix="/user")

@router.post("/")
async def create(user: UserSchema):
    new_user = await UserService.create(user)
    return UserSchema.model_validate(new_user)

@router.get("/")
async def read_all():
    all_user = UserService.read_all()
    return AllUserSchema.model_validate(all_user)

@router.get("/{user_id}")
async def read(user_id: int):
    user = await UserService.read(user_id)
    return UserSchema.model_validate(user)

@router.put("/{user_id}")
async def update(user_id: int, user: UserSchema):
    updated_user = await UserService.update(user_id, user)
    return UserSchema.model_validate(updated_user)

@router.delete("/{user_id}")
async def delete(user_id: int):
    await UserService.delete(user_id)

