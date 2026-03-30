from typing import Optional
from pydantic import BaseModel
from enum import Enum

class Propriedade(str, Enum):
    alugado = "alugado"
    proprio = "proprio"

class ModeloSchema(BaseModel):
    id_modelo: int
    id_combustivel: int

    nome_modelo: str
    cor: str
    fabricante: str
    ano: int
    capacidade: int
    propriedade: Propriedade

    class Config:
        from_attributes = True

class ModeloUpdateSchema(BaseModel):
    id_modelo: Optional[int]
    id_combustivel: Optional[int]

    nome_modelo: Optional[str]
    cor: Optional[str]
    fabricante: Optional[str]
    ano: Optional[int]
    capacidade: Optional[int]
    propriedade: Optional[Propriedade]

    class Config:
        from_attributes = True