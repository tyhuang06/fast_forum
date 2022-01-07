from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.posts as crud
from src.auth.jwthandler import get_current_user
from src.schemas.posts import CreatePostSchema, GetPostSchema, UpdatePost
from src.schemas.token import Status
from src.schemas.users import GetUserSchema


router = APIRouter()


@router.get(
    "/post",
    response_model=List[GetPostSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_posts():
    return await crud.get_posts()


@router.post(
    "/post/create", response_model=GetPostSchema, dependencies=[Depends(get_current_user)]
)
async def create_post(
    post: CreatePostSchema, current_user: GetUserSchema = Depends(get_current_user)
) -> GetPostSchema:
    return await crud.create_post(post, current_user)


@router.get(
    "/post/{post_id}",
    response_model=GetPostSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_post(post_id: int) -> GetPostSchema:
    try:
        return await crud.get_note(post_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Post does not exist",
        )


@router.patch(
    "/post/{post_id}/edit",
    dependencies=[Depends(get_current_user)],
    response_model=GetPostSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_post(
    post_id: int,
    post: UpdatePost,
    current_user: GetUserSchema = Depends(get_current_user),
) -> GetPostSchema:
    return await crud.update_post(post_id, post, current_user)


@router.delete(
    "/post/{post_id}/delete",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_post(
    post_id: int, current_user: GetUserSchema = Depends(get_current_user)
):
    return await crud.delete_post(post_id, current_user)
