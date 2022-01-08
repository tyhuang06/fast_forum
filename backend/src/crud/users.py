from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.database.models import Users
from src.schemas.users import GetUserSchema
from src.schemas.token import Status

# For file upload
import secrets
from PIL import Image

FILEPATH = "./static/images/"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Helper Functions
async def upload_picture(file, current_user):
    print(FILEPATH)
    filename = file.filename
    _, ext = filename.split(".")

    random_name = secrets.token_hex(8) + "." + ext
    file_path = FILEPATH + random_name

    # Pillow - shink image
    file_content = await file.read()

    with open(file_path, "wb") as file:
        file.write(file_content)

    img = Image.open(file_path)
    img = img.resize(size=(125, 125))
    img.save(file_path)

    file.close()

    # Store in DB
    user = await Users.get(id=current_user.id)
    user.profile_pic = random_name

    await user.save()

    return await GetUserSchema.from_queryset_single(Users.get(id=user.id))


async def create_user(user) -> GetUserSchema:
    user.password = pwd_context.encrypt(user.password)

    try:
        user = await Users.create(**user.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(
            status_code=401, detail=f"Sorry, that username already exists.")

    return await GetUserSchema.from_tortoise_orm(user)


async def update_user(user, current_user) -> GetUserSchema:
    try:
        db_user = await GetUserSchema.from_queryset_single(Users.get(id=current_user.id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"User {user.id} not found.")

    if db_user.id == current_user.id:
        await Users.filter(id=db_user.id).update(**user.dict(exclude_unset=True))

        return await GetUserSchema.from_queryset_single(Users.get(id=db_user.id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update.")


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
