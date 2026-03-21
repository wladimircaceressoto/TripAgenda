# Reglas de negocio — TripAgenda

## 1. Registro de viajes

- Un viaje puede ser registrado aunque no tenga todos sus datos completos

- Los viajes pueden ser ingresados en cualquier orden

- El sistema debe ordenar automáticamente los viajes por fecha y hora

---

## 2. Relación con empresas

- Un viaje puede estar asociado a una empresa o ser marcado como "particular"

---

## 3. Organización de agenda

- Un conductor puede tener múltiples viajes en un mismo día

---

## 4. Conflictos de horario

- Dos viajes se consideran en conflicto cuando sus horarios se superponen en el mismo día

- El sistema debe detectar automáticamente los conflictos al crear o editar un viaje

---

## 5. Gestión de conflictos

- Cuando existe un conflicto, el usuario puede decidir cuál viaje mantener

- El sistema puede sugerir mantener el viaje de mayor valor, pero la decisión final es del usuario

- Un viaje puede ser cedido (no realizado por el conductor) en caso de conflicto

---

## 6. Estados del viaje

- Un viaje puede tener distintos estados:
  - pendiente
  - confirmado
  - realizado
  - cancelado
  - cedido

---

## 7. Persistencia de información

- Todos los viajes registrados deben mantenerse como historial, incluso si son cancelados o cedidos