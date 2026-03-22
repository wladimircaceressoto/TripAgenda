from fastapi import APIRouter
from models.viaje import Viaje
from services import viaje_service

router = APIRouter()

# GET todos
@router.get("/viajes")
def get_viajes():
    return viaje_service.get_viajes()

# GET por id
@router.get("/viajes/{id}")
def get_viaje_por_id(id: int):
    return viaje_service.get_viaje_por_id(id)

# POST
@router.post("/viajes")
def create_viaje(viaje: Viaje):
    return viaje_service.create_viaje(viaje)

# PUT
@router.put("/viajes/{id}")
def update_viaje(id: int, viaje: Viaje):
    return viaje_service.update_viaje(id, viaje)

# DELETE
@router.delete("/viajes/{id}")
def delete_viaje(id: int):
    return viaje_service.delete_viaje(id)