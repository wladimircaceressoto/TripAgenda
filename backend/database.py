from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL de conexión
DATABASE_URL = "postgresql://postgres:Maximo7275@localhost:5432/tripagenda_db"

# Crear engine
engine = create_engine(DATABASE_URL)

#Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🔥 PRUEBA DE CONEXIÓN REAL
try:
    with engine.connect() as connection:
        print("✅ Conexión a la base de datos exitosa")
except Exception as e:
    print("❌ Error de conexión:", e)