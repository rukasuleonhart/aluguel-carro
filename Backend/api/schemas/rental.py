from pydantic import BaseModel
from datetime import datetime

# Classe base com orm_mode ativado para permitir a conversão de modelos ORM para Pydantic
class BaseSchema(BaseModel):
    class Config:
        orm_mode = True

class Rental_Schema(BaseSchema):
    id: int
    car_id: int
    locatario_id: int
    data_inicio: datetime
    data_fim: datetime
    preco: float