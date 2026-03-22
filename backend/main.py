from fastapi import FastAPI
from routes import viajes

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "TripAgenda API funcionando"}

# Conectar rutas
app.include_router(viajes.router)

from database import engine

print("Conectando a la base de datos...")