from pydantic import BaseModel

class Concessionaria(BaseModel):
    nome: str
    marca: str
    modelo: str
    ano: int