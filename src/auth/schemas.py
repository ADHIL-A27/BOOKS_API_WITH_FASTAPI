from pydantic import BaseModel,Field
import uuid
from src.books.schemas import Book
from src.reviews.schemas import ReviewModel
from typing import List
from datetime import datetime

class UserCreateModel(BaseModel):
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    username: str = Field(max_length=8)
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)




class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    password_hash: str = Field(exclude=True)
    created_at: datetime
    update_at: datetime
    
class UserBooksModel(UserModel):
    books: List[Book]
    reviews: List[ReviewModel]

class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)
