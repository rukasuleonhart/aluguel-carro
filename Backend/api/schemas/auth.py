from pydantic import BaseModel
from pydantic.config import ConfigDict

# Classe base com from_attributes ativado para permitir a conversão de modelos ORM para Pydantic
class BaseSchema(BaseModel):
   model_config = ConfigDict(from_attributes=True)

class Token_Schema(BaseSchema):
   access_token: str # o token JWT que vamos gerar
   token_type:str # o modelo que o cliente deve usar para Autorização