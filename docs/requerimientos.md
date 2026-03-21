# Requerimientos del sistema — TripAgenda

## 1. Introducción

Este documento define los requerimientos funcionales y no funcionales del sistema TripAgenda, basado en el alcance definido para la primera versión (MVP).

---

## 2. Requerimientos funcionales

Los requerimientos funcionales describen las acciones que el sistema debe permitir al usuario.

# 2.1 Gestión de viajes

- El sistema debe permitir crear un viaje ingresando:
  
  - fecha
  - hora
  - origen
  - destino
  - empresa
  - valor
  - notas

- El sistema debe permitir editar un viaje existente

- El sistema debe permitir eliminar un viaje

- El sistema debe permitir crear un viaje incluso si algunos datos no están completos (ej: origen o destino pendiente)

---

# 2.2 Agenda

- El sistema debe mostrar una agenda diaria con los viajes del día

- El sistema debe mostrar una vista mensual de los viajes

- El sistema debe permitir visualizar múltiples viajes en un mismo día

---

# 2.3 Empresas

- El sistema debe permitir asociar un viaje a una empresa

- El sistema debe permitir marcar un viaje como "particular" cuando no pertenezca a ninguna empresa

- El sistema debe permitir filtrar los viajes por empresa

---

# 2.4 Conflictos de horario

- El sistema debe detectar conflictos basándose en la superposición de horarios entre viajes registrados en un mismo día

- El sistema debe mostrar una advertencia visual en caso de conflicto

---

# 2.5 Historial

- El sistema debe permitir visualizar viajes pasados

- El sistema debe mostrar los viajes en orden cronológico

---

## 3. Requerimientos no funcionales

Los requerimientos no funcionales describen cómo debe comportarse el sistema.

# 3.1 Usabilidad

- El sistema debe ser fácil de usar desde un teléfono móvil

- El sistema debe tener una interfaz clara y simple

- El usuario debe poder registrar un viaje en pocos pasos

---

# 3.2 Rendimiento

- El sistema debe cargar la agenda en menos de 2 segundos

- Las acciones (crear, editar, eliminar) deben ejecutarse de forma inmediata

---

# 3.3 Accesibilidad

- El sistema debe ser usable sin conocimientos técnicos

---

# 3.4 Disponibilidad

- El sistema debe estar disponible en cualquier momento desde el navegador

---

# 3.5 Seguridad (nivel básico MVP)

- Los datos del usuario deben estar protegidos

- El sistema debe evitar pérdida de información

---

## 4. Notas adicionales

(Espacio para futuras mejoras o ideas que no estén en el MVP)

Ejemplo:

- Integración con WhatsApp
- Automatización de pagos
- Notificaciones