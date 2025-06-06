from typing import List
from pydantic import BaseModel
from pydantic.config import ConfigDict
from datetime import date
from .car import Car_Schema

class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class Rental_Create_Schema(BaseSchema):
    user_id: int
    car_id: int
    start_date: date
    end_date: date

class Rental_Schema(Rental_Create_Schema):
    id: int
    car: Car_Schema

class Rental_List(BaseSchema):
    rentals: List[Rental_Schema]
