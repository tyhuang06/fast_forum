from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from tortoise.contrib.fastapi import HTTPNotFoundError

import src.crud.users as crud
from src.auth.users import validate_user
from src.schemas.token import Status
from src.schemas.users import CreateUserSchema, GetUserSchema, UpdateUser

from fastapi import File, UploadFile

from src.auth.jwthandler import (
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


router = APIRouter()


@router.post('/register', response_model=GetUserSchema)
async def create_user(user: CreateUserSchema) -> GetUserSchema:
    return await crud.create_user(user)


@router.post("/login")
async def login(user: OAuth2PasswordRequestForm = Depends()):
    user = await validate_user(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    content = {"message": "You've successfully logged in. Welcome back!"}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False,
    )

    return response


@router.get(
    "/user/account", response_model=GetUserSchema, dependencies=[Depends(get_current_user)]
)
async def get_user(current_user: GetUserSchema = Depends(get_current_user)):
    return current_user


@router.patch(
    "/user/account/edit",
    dependencies=[Depends(get_current_user)],
    response_model=GetUserSchema,
    responses={404: {"model": HTTPNotFoundError}})
async def update_user(
        user: UpdateUser,
        current_user: GetUserSchema = Depends(get_current_user)) -> GetUserSchema:
    return await crud.update_user(user, current_user)


@router.post(
    "/user/account/upload",
    dependencies=[Depends(get_current_user)],
    response_model=GetUserSchema,)
async def create_upload_file(
        file: UploadFile = File(...),
        current_user: GetUserSchema = Depends(get_current_user)):
    return await crud.upload_picture(file, current_user)


@router.delete(
    "/user/{user_id}/delete",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_user(
    user_id: int, current_user: GetUserSchema = Depends(get_current_user)
) -> Status:
    return await crud.delete_user(user_id, current_user)
