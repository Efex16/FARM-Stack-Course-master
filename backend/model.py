<<<<<<< HEAD
#  @Efex @Aminat
=======
#  @Efex
>>>>>>> b389d1d360b8c08c7dc0428784684b874d149948
#  ALX GRAD PROJECT - September 2023

# Pydantic allows auto creation of JSON Schemas from models
from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str
