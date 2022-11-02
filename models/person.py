from pydantic import BaseModel
from typing import Optional

def hi_person():
    print('hola persona')

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None #que puede ser opcional por defecto nulo
    is_married: Optional[bool] = None