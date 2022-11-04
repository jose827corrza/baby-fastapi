from pydantic import BaseModel, Field
from typing import Optional

def hi_localization():
    print('hola loc')

class Localization(BaseModel):
    city: str = Field(description="City where you live")
    state: str = Field(description="State where you live")
    country: str = Field(description="Country where you live")

    class Config:
        schema_extra = {
            "example": {
                "city": "Soacha",
                "state": "Cundinamarca",
                "country": "Colombia"
            }
        }