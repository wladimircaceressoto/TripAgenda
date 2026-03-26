from pydantic import BaseModel, Field, conint, constr
from typing import Optional, Literal
from datetime import date, time

class Viaje(BaseModel):
    origen: constr(strip_whitespace=True, min_length=1) = Field(..., description="Ciudad de origen no puede estar vacía")
    destino: constr(strip_whitespace=True, min_length=1) = Field(..., description="Ciudad de destino no puede estar vacía")
    valor: conint(gt=0) = Field(..., description="Valor debe ser mayor a 0")
    fecha: date
    hora: time
    empresa_id: Optional[int] = None
    estado: Literal["pendiente", "realizado", "cancelado"] = "pendiente" 