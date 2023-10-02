#  @Efex @Aminat
#  ALX GRAD PROJECT - September 2023

# Pydantic allows auto creation of JSON Schemas from models
from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str
