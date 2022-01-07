from typing import Optional
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Posts

# For creating new posts
CreatePostSchema = pydantic_model_creator(Posts, name="CreatePost", exclude=[
                                          "author_id"], exclude_readonly=True)
# For retrieving posts
GetPostSchema = pydantic_model_creator(Posts, name="GetPost", exclude=[
                                       "author.password", "author.created_at"])


class UpdatePost(BaseModel):
    title: Optional[str]
    content: Optional[str]
