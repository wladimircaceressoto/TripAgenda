from fastapi import HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.empresa_db import EmpresaDB
from models.viaje_db import ViajeDB
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

def update_empresa(id: int, empresa_actualizada: EmpresaCreate):
    db: Session = SessionLocal()
    empresa = db.query(EmpresaDB).filter(EmpresaDB.id == id).first()

    if not empresa:
        db.close()
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

    # Verificar que no exista otra empresa con el mismo nombre (excepto esta misma)
    existente = db.query(EmpresaDB).filter(
        EmpresaDB.nombre == empresa_actualizada.nombre,
        EmpresaDB.id != id
    ).first()
    if existente:
        db.close()
        raise HTTPException(status_code=400, detail="Ya existe otra empresa con ese nombre")

    empresa.nombre = empresa_actualizada.nombre

    db.commit()
    db.refresh(empresa)
    db.close()

    return empresa

def delete_empresa(id: int):
    db: Session = SessionLocal()
    empresa = db.query(EmpresaDB).filter(EmpresaDB.id == id).first()

    if not empresa:
        db.close()
        raise HTTPException(status_code=404, detail="Empresa no encontrada")

    # Verificar si hay viajes asociados a la empresa antes de eliminar
    viaje_asociado = db.query(ViajeDB).filter(ViajeDB.empresa_id == id).first()
    if viaje_asociado:
        db.close()
        raise HTTPException(status_code=400, detail="No se puede eliminar la empresa porque tiene viajes asociados")

    db.delete(empresa)
    db.commit()
    db.close()

    return {"message": f"Empresa con id {id} eliminada"}
