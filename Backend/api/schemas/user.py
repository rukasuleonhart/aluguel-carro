from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr
from pydantic.config import ConfigDict

# Classe base com from_attributes ativado para permitir a conversão de modelos ORM para Pydantic
class BaseSchema(BaseModel):
   model_config = ConfigDict(from_attributes=True)

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