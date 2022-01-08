from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM
from src.routes import users, posts

from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


origins = ["http://localhost:8080"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(users.router)
app.include_router(posts.router)


register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
def home():
    return "Hello, World!"
