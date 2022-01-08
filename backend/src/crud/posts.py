from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Posts
from src.schemas.posts import GetPostSchema
from src.schemas.token import Status


async def get_posts():
    return await GetPostSchema.from_queryset(Posts.all())


async def get_note(post_id) -> GetPostSchema:
    return await GetPostSchema.from_queryset_single(Posts.get(id=post_id))


async def create_post(post, current_user) -> GetPostSchema:
    post_dict = post.dict(exclude_unset=True)
    post_dict["author_id"] = current_user.id
    post = await Posts.create(**post_dict)

    return await GetPostSchema.from_tortoise_orm(post)


async def update_post(post_id, post, current_user) -> GetPostSchema:
    try:
        db_post = await GetPostSchema.from_queryset_single(Posts.get(id=post_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Post {post_id} not found")

    if db_post.author.id == current_user.id:
        await Posts.filter(id=post_id).update(**post.dict(exclude_unset=True))

        return await GetPostSchema.from_queryset_single(Posts.get(id=post_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update.")


async def delete_post(post_id, current_user):
    try:
        db_post = await GetPostSchema.from_queryset_single(Posts.get(id=post_id))
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Post {post_id} not found.")

    if db_post.author.id == current_user.id:
        deleted_count = await Posts.filter(id=post_id).delete()

        if not deleted_count:
            raise HTTPException(
                status_code=404, detail=f"Post {post_id} not found.")

        return Status(message=f"Deleted note {post_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete.")
