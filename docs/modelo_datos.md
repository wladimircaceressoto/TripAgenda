# Modelo de Datos — TripAgenda

## 1. Introducción

Este documento define la estructura de datos del sistema TripAgenda para su primera versión (MVP).

El objetivo es representar las entidades principales del sistema, sus atributos y relaciones, sirviendo como base para el desarrollo del backend y la base de datos.

---

## 2. Entidades del sistema

### 2.1 Viaje

Representa un traslado o servicio realizado por el conductor.

Atributos:

- id (PK)
- fecha
- hora
- origen
- destino
- valor_estimado
- valor_final (opcional)
- notas (opcional)
- empresa_id (FK, opcional para viajes particulares)
- estado
- pasajero_id (FK)
- pasajeros_cantidad
- tipo_viaje_id (FK)

---

### 2.2 Empresa

Representa una empresa que proporciona servicios al conductor (ej: turismo, radio taxi).

Atributos:

- id (PK)
- nombre

---

### 2.3 Pasajero

Representa a la persona principal asociada a un viaje.

Atributos:

- id (PK)
- telefono (único)
- nombre
- apellido (opcional)
- nacionalidad (opcional)
- notas (opcional)

---

### 2.4 Tipo de Viaje

Clasifica el tipo de servicio realizado.

Atributos:

- id (PK)
- nombre

---

## 3. Relaciones entre entidades

- Un viaje puede estar asociado a una empresa o ser particular
- Un viaje pertenece a un pasajero
- Un viaje tiene un tipo de viaje
- Un viaje puede incluir múltiples pasajeros (representado por el campo pasajeros_cantidad)
- Una empresa puede tener múltiples viajes

---

## 4. Consideraciones del modelo

- El campo "empresa_id" puede ser nulo para representar viajes particulares
- Se utiliza "pasajeros_cantidad" para simplificar el modelo en el MVP
- El campo "valor_final" se incluye para futuras funcionalidades relacionadas con pagos
- El estado del viaje será gestionado como un valor controlado (pendiente, confirmado, realizado, cancelado, cedido)

---

## 5. Posibles mejoras futuras

- Tabla intermedia para relación muchos a muchos entre viajes y pasajeros
- Relación entre empresas y tipos de viaje
- Sistema de pagos asociado a viajes
- Historial detallado de cambios en los viajes