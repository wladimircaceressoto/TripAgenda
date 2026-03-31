from typing import List

from fastapi import APIRouter
from models.empresa import EmpresaCreate, EmpresaResponse
from services import empresa_service

router = APIRouter()

# GET todas las empresas
@router.get("/empresas", response_model=List[EmpresaResponse])
def get_empresas():
    return empresa_service.get_empresas()

# GET empresa por id
@router.get("/empresas/{id}", response_model=EmpresaResponse)
def get_empresa_por_id(id: int):
    return empresa_service.get_empresa_por_id(id)

# POST crear empresa
@router.post("/empresas", response_model=EmpresaResponse)
def create_empresa(empresa: EmpresaCreate):
    return empresa_service.create_empresa(empresa)
