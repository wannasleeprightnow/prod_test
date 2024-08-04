from fastapi import FastAPI, Body
import pydantic


app = FastAPI()


class UserScheme(pydantic.BaseModel):
    id: int
    username: str
    password: str


users: list[UserScheme] = []


@app.get("/users", status_code=200)
async def test_get() -> list[UserScheme]:
    return users


@app.post("/add_user", status_code=201)
async def test_post(data: UserScheme = Body()):
    global users
    users.append(data)
