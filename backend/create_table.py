from database import engine
from models.db_base import Base

# Importar modelos para que SQLAlchemy los registre
from models.viaje_db import ViajeDB
from models.empresa_db import EmpresaDB

print("Tablas registradas en metadata:", Base.metadata.tables.keys())
print("Engine conectado a:", engine.url)

Base.metadata.create_all(bind=engine)

print("✅ Tablas creadas correctamente")