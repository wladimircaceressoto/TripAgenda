from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class Viaje(BaseModel):
    origen: str
    destino: str
    valor: int
    fecha: date
    hora: time
    empresa: Optional[str] = None  
    estado: str = "pendiente" 