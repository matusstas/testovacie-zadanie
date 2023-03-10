from pydantic import BaseModel
from typing import List

class Content(BaseModel):
    status: str
    message: str

class Post(BaseModel):
    id: int
    userId: int
    title: str
    body: str

class Post2(BaseModel):
    userId: int
    title: str
    body: str

class Posts(BaseModel):
    posts: List[Post]
