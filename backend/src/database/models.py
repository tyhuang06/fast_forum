from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True, null=False)
    email = fields.CharField(max_length=50, unique=True, null=False)
    password = fields.CharField(max_length=60, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    profile_pic = fields.CharField(
        max_length=200, null=False, default="default.jpg")

    def __str__(self) -> str:
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Posts(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225, null=False)
    content = fields.TextField()
    author = fields.ForeignKeyField("models.Users", related_name="post")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.author_id} on {self.created_at}"
