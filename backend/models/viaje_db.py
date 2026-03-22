from sqlalchemy import Column, Integer, String, Date, Time
from models.db_base import Base

class ViajeDB(Base):
    __tablename__ = "viajes"

    id = Column(Integer, primary_key=True, index=True)
    origen = Column(String, nullable=False)
    destino = Column(String, nullable=False)
    valor = Column(Integer, nullable=False)
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    empresa = Column(String, nullable=True)
    estado = Column(String, default="pendiente")