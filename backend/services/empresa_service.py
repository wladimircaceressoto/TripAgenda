from fastapi import HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.empresa_db import EmpresaDB
from models.empresa import EmpresaCreate

def get_empresas():
    db: Session = SessionLocal()
    empresas = db.query(EmpresaDB).all()
    db.close()
    return empresas

def get_empresa_por_id(id: int):
    db: Session = SessionLocal()
    empresa = db.query(EmpresaDB).filter(EmpresaDB.id == id).first()
    db.close()

    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

    return empresa

def create_empresa(empresa: EmpresaCreate):
    db: Session = SessionLocal()

    # Verificar si ya existe una empresa con el mismo nombre
    existente = db.query(EmpresaDB).filter(EmpresaDB.nombre == empresa.nombre).first()
    if existente:
        db.close()
        raise HTTPException(status_code=400, detail="Ya existe una empresa con ese nombre")

    nueva_empresa = EmpresaDB(
        nombre=empresa.nombre
    )

    db.add(nueva_empresa)
    db.commit()
    db.refresh(nueva_empresa)
    db.close()

    return nueva_empresa
