from pydantic import BaseModel


class EmpresaCreate(BaseModel):
    nombre: str


class EmpresaResponse(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

