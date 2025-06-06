from typing import List, Optional
from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

# Classe base com from_attributes ativado para permitir a conversão de modelos ORM para Pydantic
class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class Car_Create_Schema(BaseSchema):
    brand: str
    model: str
    price: float
    images: List[str]
    speed: str
    acceleration: str
    fuel: str
    transmission: str
    horsepower: str
    seats: int

class Car_Schema(Car_Create_Schema):
    id: int

class Car_List(BaseSchema):
    cars: List[Car_Schema]