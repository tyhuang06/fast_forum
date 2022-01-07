from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.database.models import Users
from src.schemas.users import GetUserSchema
from src.schemas.token import Status


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(user) -> GetUserSchema:
    user.password = pwd_context.encrypt(user.password)

    try:
        user = await Users.create(**user.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(
            status_code=401, detail=f"Sorry, that username already exists.")

    return await GetUserSchema.from_tortoise_orm(user)


async def delete_user(user_id, current_user) -> Status:
    try:
        user = await GetUserSchema.from_queryset_single(Users.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"User {user_id} not found.")

    if user.id == current_user.id:
        deleted_count = await Users.filter(id=user_id).delete()

        if not deleted_count:
            raise HTTPException(
                status_code=404, detail=f"User {user_id} not found.")

        return Status(message=f"Deleted user {user_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete.")