from operator import index
from fastapi import HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.viaje_db import ViajeDB
from fastapi import HTTPException

def get_viajes():
    db: Session = SessionLocal()
    viajes = db.query(ViajeDB).all()
    db.close()
    return viajes


def get_viaje_por_id(id: int):
    db: Session = SessionLocal()
    viaje = db.query(ViajeDB).filter(ViajeDB.id == id).first()
    db.close()

    if not viaje:
        raise HTTPException(status_code=404, detail="Viaje no encontrado")

    return viaje

def create_viaje(viaje):
    db: Session = SessionLocal()

    nuevo_viaje = ViajeDB(
        origen=viaje.origen,
        destino=viaje.destino,
        valor=viaje.valor,
        fecha=viaje.fecha,
        hora=viaje.hora,
        empresa=viaje.empresa,
        estado=viaje.estado
    )

    db.add(nuevo_viaje)
    db.commit()
    db.refresh(nuevo_viaje)
    db.close()


def update_viaje(id: int, viaje_actualizado):
    db: Session = SessionLocal()
    viaje = db.query(ViajeDB).filter(ViajeDB.id == id).first()

    if not viaje:
        db.close()
        raise HTTPException(status_code=404, detail="Viaje no encontrado")

    viaje.origen = viaje_actualizado.origen
    viaje.destino = viaje_actualizado.destino
    viaje.valor = viaje_actualizado.valor
    viaje.fecha = viaje_actualizado.fecha
    viaje.hora = viaje_actualizado.hora
    viaje.empresa = viaje_actualizado.empresa
    viaje.estado = viaje_actualizado.estado

    db.commit()
    db.refresh(viaje)
    db.close()

    return viaje

def delete_viaje(id: int):
    db: Session = SessionLocal()
    viaje = db.query(ViajeDB).filter(ViajeDB.id == id).first()

    if not viaje:
        db.close()
        raise HTTPException(status_code=404, detail="Viaje no encontrado")

    db.delete(viaje)
    db.commit()
    db.close()

    return {"message": f"Viaje con id {id} eliminado"}