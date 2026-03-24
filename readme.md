# TripAgenda

TripAgenda es un sistema de agenda de viajes diseñado para conductores independientes que gestionan traslados de pasajeros.

## Descripción

El sistema permite registrar, organizar y visualizar viajes desde una aplicación web, reemplazando el uso de cuadernos o registros manuales.

## Problema que resuelve

Muchos conductores gestionan sus viajes mediante:

* WhatsApp
* llamadas
* cuadernos

Esto genera:

* desorden en la agenda
* dificultad para visualizar horarios
* riesgo de errores en pagos

TripAgenda centraliza toda esta información en una agenda digital.

## Tecnologías utilizadas

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy

## Arquitectura

El backend está estructurado en:

* `routes/` → endpoints
* `services/` → lógica de negocio
* `models/` → modelos de datos
* `database.py` → conexión a base de datos

## Funcionalidades actuales

* Crear viajes
* Obtener lista de viajes
* Obtener viaje por ID
* Actualizar viajes
* Eliminar viajes
* Persistencia en base de datos

## Cómo ejecutar el proyecto

1. Clonar repositorio
2. Ir a carpeta backend:

    ```
    cd backend
    ```
3. Instalar dependencias:

    ```
    python -m pip install -r requirements.txt
    ```
4. Ejecutar servidor:

    ```
    python -m uvicorn main:app --reload
    ```

## Estado del proyecto

En desarrollo — MVP backend en construcción
