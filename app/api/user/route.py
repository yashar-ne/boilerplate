from fastapi import APIRouter

from schema import UserSchema
from service import UserService

router = APIRouter(prefix="/user")


@router.get("/")
async def read_all():
    all_user = await UserService.read_all()
    return UserSchema.model_validate(all_user)

