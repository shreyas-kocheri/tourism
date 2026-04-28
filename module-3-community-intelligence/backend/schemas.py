from pydantic import BaseModel
from typing import List

class PostCreate(BaseModel):
    email: str
    state: str
    district: str
    message: str


class CommentCreate(BaseModel):
    email: str
    text: str


class CommentOut(BaseModel):
    email: str
    text: str

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    id: int
    email: str
    state: str
    district: str
    message: str
    likes: int
    dislikes: int
    trust_status: str
    comments: List[CommentOut]

    class Config:
        orm_mode = True
