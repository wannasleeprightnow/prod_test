from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import pydantic


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserScheme(pydantic.BaseModel):
    id: int
    username: str
    password: str


users: list[UserScheme] = []


@app.get("/user", status_code=200)
async def test_get() -> list[UserScheme]:
    global users
    print(users)
    return users


@app.post("/user", status_code=201)
async def test_post(user: UserScheme = Body()) -> UserScheme:
    global users
    users += [user]
    return user
