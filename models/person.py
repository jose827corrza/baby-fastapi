from pydantic import BaseModel, Field, EmailStr, SecretStr
from typing import Optional
from enum import Enum

def hi_person():
    print('hola persona')

class HairColor(Enum):
    white = "white"
    black = "black"
    red = "red"
    blonde = "blonde"
    brown = "brown"

class Person(BaseModel):
    first_name: str = Field(description="user's first name")
    last_name: str = Field(description="user's last name")
    age: int = Field(description="user's first name")
    email: EmailStr = Field(description="user's email")
    username: str = Field(description="username showed on the platform")
    password: str = Field(description="Password set by the user")
    hair_color: Optional[HairColor] = Field(description="user's hair color from an enum", default=None)#que puede ser opcional por defecto nulo
    is_married: Optional[bool] = Field(description="user's marital status", default=None)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Jose",
                "last_name": "Corredor",
                "age": 26,
                "username": "josedev",
                "password": "123dev",
                "email": "jose.corrzadeveloper@gmail.com",
                "hair_color": "blonde",
                "is_married": True
            }
        }

class Login(BaseModel):
    username: str = Field(description="username showed on the platform")
    password: SecretStr = Field(description="Password set by the user")