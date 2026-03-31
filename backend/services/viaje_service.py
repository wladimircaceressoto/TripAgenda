from fastapi import HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.viaje_db import ViajeDB

def get_viajes(fecha=None, fecha_inicio=None, fecha_fin=None, empresa_id=None):
    db: Session = SessionLocal()

    # Validaciones de parámetros
    if fecha and (fecha_inicio or fecha_fin):
        db.close()
        raise HTTPException(status_code=400, detail="No se puede usar 'fecha' con 'fecha_inicio' o 'fecha_fin'")

    if (fecha_inicio and not fecha_fin) or (fecha_fin and not fecha_inicio):
        db.close()
        raise HTTPException(status_code=400, detail="Debe proporcionar ambos 'fecha_inicio' y 'fecha_fin' para búsqueda por rango")

    # Construcción dinámica de la consulta
    query = db.query(ViajeDB)

    # Aplicar filtro de fecha si viene
    if fecha:
        query = query.filter(ViajeDB.fecha == fecha)
    elif fecha_inicio and fecha_fin:
        query = query.filter(ViajeDB.fecha >= fecha_inicio, ViajeDB.fecha <= fecha_fin)

    # Aplicar filtro de empresa_id si viene
    if empresa_id:
        query = query.filter(ViajeDB.empresa_id == empresa_id)

    # Ejecutar consulta
    viajes = query.all()

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

    # Verificar conflicto horario: si ya existe un viaje con la misma fecha y hora
    conflicto = db.query(ViajeDB).filter(
        ViajeDB.fecha == viaje.fecha,
        ViajeDB.hora == viaje.hora
    ).first()

    if conflicto:
        db.close()
        raise HTTPException(status_code=400, detail="Conflicto horario: ya existe un viaje programado para esa fecha y hora")

    nuevo_viaje = ViajeDB(
        origen=viaje.origen,
        destino=viaje.destino,
        valor=viaje.valor,
        fecha=viaje.fecha,
        hora=viaje.hora,
        empresa_id=viaje.empresa_id,
        estado=viaje.estado
    )

    db.add(nuevo_viaje)
    db.commit()
    db.refresh(nuevo_viaje)
    db.close()

    return nuevo_viaje


def update_viaje(id: int, viaje_actualizado):
    db: Session = SessionLocal()
    viaje = db.query(ViajeDB).filter(ViajeDB.id == id).first()

    if not viaje:
        db.close()
        raise HTTPException(status_code=404, detail="Viaje no encontrado")

    # Verificar conflicto horario: si ya existe otro viaje (no este mismo) con la misma fecha y hora
    conflicto = db.query(ViajeDB).filter(
        ViajeDB.fecha == viaje_actualizado.fecha,
        ViajeDB.hora == viaje_actualizado.hora,
        ViajeDB.id != id
    ).first()

    if conflicto:
        db.close()
        raise HTTPException(status_code=400, detail="Conflicto horario: ya existe otro viaje programado para esa fecha y hora")

    viaje.origen = viaje_actualizado.origen
    viaje.destino = viaje_actualizado.destino
    viaje.valor = viaje_actualizado.valor
    viaje.fecha = viaje_actualizado.fecha
    viaje.hora = viaje_actualizado.hora
    viaje.empresa_id = viaje_actualizado.empresa_id
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