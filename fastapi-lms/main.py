from typing import Optional

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


users: list[User] = []


@app.get("/users", response_model=list[User])
async def get_users() -> list[User]:
    return users


@app.post("/users")
async def create_user(user: User) -> str:
    users.append(user)
    return f"{user} added"


@app.get("/users/{id}")
async def get_user(id: int = Path(..., description="The ID of the user I want to retrieve", gt=2)) -> User:
    return users[id]
