from typing import List, Optional
from pydantic import BaseModel, Field

# Classe base com orm_mode ativado para permitir a conversão de modelos ORM para Pydantic
class BaseSchema(BaseModel):
    class Config:
        orm_mode = True

class Car_Schema(BaseSchema):
    id: int
    marca: str
    modelo: str
    ano: int
    placa: str
    cor: str
    quilometragem: float
    tipo_combustível: str
    cambio: str
    numero_portas: str
    categoria: str
    disponivel: bool
    preco_por_dia: float
    localizacao: str
    descricao: Optional[str] = None
    fotos: Optional[List[str]] = Field(default_factory=list)
    proprietario_id: int

    
