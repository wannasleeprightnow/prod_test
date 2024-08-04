from fastapi import FastAPI, Body
import pydantic


app = FastAPI()


class UserScheme(pydantic.BaseModel):
    id: int
    username: str
    password: str


users: list[UserScheme] = []


@app.get("/user", status_code=200)
async def test_get() -> list[UserScheme]:
    return users


@app.post("/user", status_code=201)
async def test_post(user: UserScheme = Body()) -> UserScheme:
    global users
    users.append(user)
    return user
