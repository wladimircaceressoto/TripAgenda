from fastapi import FastAPI
from routes import viajes, empresas

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "TripAgenda API funcionando"}

# Conectar rutas
app.include_router(viajes.router)
app.include_router(empresas.router)

from database import engine

print("Conectando a la base de datos...")