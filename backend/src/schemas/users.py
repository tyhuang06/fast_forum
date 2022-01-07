from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Users

# For creating new users
CreateUserSchema = pydantic_model_creator(
    Users, name="CreateUser", exclude_readonly=True)
# For retrieving user info returning to end users
GetUserSchema = pydantic_model_creator(
    Users, name="GetUser", exclude=["password"])
# For validating users
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at"])
