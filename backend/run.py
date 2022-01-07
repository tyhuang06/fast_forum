import uvicorn
from tortoise import Tortoise
from dotenv import load_dotenv

load_dotenv()
Tortoise.init_models(["src.database.models"], "models")

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
