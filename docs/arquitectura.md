# Arquitectura del sistema — TripAgenda

## 1. Introducción

Este documento define la arquitectura técnica del sistema TripAgenda para su primera versión (MVP).

El objetivo es establecer una base simple, escalable y mantenible para el desarrollo del sistema.

---

## 2. Tipo de aplicación

TripAgenda será una aplicación web responsive, optimizada para dispositivos móviles.

El usuario accederá a través de un navegador web (Chrome, Safari, etc.), sin necesidad de instalar una aplicación.

---

## 3. Arquitectura general

El sistema seguirá una arquitectura cliente-servidor:

- Frontend: interfaz de usuario (lo que ve el conductor)
- Backend: lógica del sistema y procesamiento de datos
- Base de datos: almacenamiento de información

---

## 4. Frontend

El frontend será responsable de:

- Mostrar la agenda diaria y mensual
- Permitir crear, editar y eliminar viajes
- Mostrar alertas de conflicto
- Navegación del sistema

Tecnología sugerida (MVP):

- HTML
- CSS
- JavaScript (vanilla o framework simple más adelante)

---

## 5. Backend

El backend será responsable de:

- Procesar la lógica de negocio
- Validar conflictos de horario
- Gestionar los datos de viajes, empresas y pasajeros
- Exponer endpoints mediante una API REST

Tecnología sugerida (MVP):

- Python
- FastAPI

---

## 6. Base de datos

La base de datos será relacional.

Responsabilidades:

- Almacenar viajes, empresas, pasajeros y tipos de viaje
- Mantener relaciones entre entidades

Tecnología sugerida:

- PostgreSQL

---

## 7. Comunicación entre capas

El frontend se comunicará con el backend mediante HTTP (API REST).

Ejemplo:

- GET /viajes → obtener viajes
- POST /viajes → crear viaje
- PUT /viajes/:id → editar viaje
- DELETE /viajes/:id → eliminar viaje

---

## 8. Estructura del proyecto

El proyecto se organizará en:

- /frontend → interfaz de usuario
- /backend → lógica del sistema
- /docs → documentación

---

## 9. Consideraciones del MVP

- Se prioriza simplicidad sobre complejidad
- No se implementará autenticación en la primera versión
- No habrá despliegue en la nube en esta etapa inicial
- El sistema será utilizado por un solo usuario

---

## 10. Escalabilidad futura

El sistema podrá evolucionar hacia:

- Autenticación de usuarios
- Multiusuario
- Aplicación móvil
- Integraciones externas (WhatsApp, APIs)
- Sistema de pagos