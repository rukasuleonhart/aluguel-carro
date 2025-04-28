from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr

from .car import Car_Schema
from .rental import Rental_Schema

# Classe base com from_attributes ativado para permitir a conversão de modelos ORM para Pydantic
class BaseSchema(BaseModel):
    class Config:
        from_attributes = True

class User_Public_Schema(BaseSchema):
    nome: str
    email: EmailStr
    telefone: Optional[str] = None

class User_Create_Schema(User_Public_Schema):
    senha: str

class User_Read_Schema(User_Public_Schema):
    id:int

# Listar Usuários
class Users_List(BaseSchema):
    users: List[User_Read_Schema]

# leitura de usuários com carros para ser alugados
class User_Read_With_Cars_Schema(User_Read_Schema):
    carros: List[Car_Schema] = Field(default_factory=list)

# leitura de usuários que alugou carros
class User_Read_With_Rentals_Schema(User_Read_Schema):
    alugueis: List[Rental_Schema] = Field(default_factory=list)

# leitura de todos usuários
class User_Read_Full_Schema(User_Read_Schema):
    carros: List[Car_Schema] = Field(default_factory=list)
    alugueis: List[Rental_Schema] = Field(default_factory=list)