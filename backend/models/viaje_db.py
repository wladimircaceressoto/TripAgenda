from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from models.db_base import Base

class ViajeDB(Base):
    __tablename__ = "viajes"

    id = Column(Integer, primary_key=True, index=True)
    origen = Column(String, nullable=False)
    destino = Column(String, nullable=False)
    valor = Column(Integer, nullable=False)
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    empresa_id = Column(Integer, ForeignKey('empresas.id'), nullable=True)
    empresa = relationship('EmpresaDB', back_populates='viajes')
    estado = Column(String, default="pendiente")