from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.db_base import Base

class EmpresaDB(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    viajes = relationship('ViajeDB', back_populates='empresa')