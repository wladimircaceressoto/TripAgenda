# Alcance del sistema - TripAgenda

## 1. Contexto del sistema

El sistema TripAgenda está diseñado para conductores independientes que gestionan servicios de transporte.

Actualmente el flujo de trabajo es manual:

- Las solicitudes llegan por WhatsApp o correo
- Se registran en un cuaderno (respaldo)
- Luego se ordenan por fecha en otra hoja
- Se separan por empresa (turismo, radio taxi, etc.)
- Se revisa diariamente la agenda
- Se utiliza el registro para validar pagos mensuales

Problemas detectados:

- Doble trabajo (anotar + transcribir)
- Difícil visualización de agenda ordenada
- Gestión manual de conflictos de horario
- Riesgo de errores en pagos
- No hay automatización

---

## 2. Objetivo del alcance

Definir las funcionalidades inclidas en la primera versión (MVP) del sistema TripAgenda, enfocado en digitalizar y simplificar la gestión diaria de viajes para conductores independientes.

---

## 3. Funcionalidades incluidas (MVP)

# 3.1 Gestión de viajes

- Crear viaje
- Editar viaje
- Eliminar viaje
- Registrar información básica:
  - fecha
  - hora
  - origen
  - destino
  - empresa
  - valor
  - notas

---

# 3.2 Agenda

- Visualización de agenda diaria
- Visualización de agenda mensual
- Listado de múltiples viajes por día

---

# 3.3 Empresas

- Asociar viajes a una empresa
- Filtrar viajes por empresa

---

# 3.4 Conflictos de horario

- Detección de cruces de horarios entre viajes
- Advertencia visual en caso de conflicto

---

# 3.5 Historial básico

- Consulta de viajes registrados anteriormente
- Visualización cronológica de viajes

---

## 4. Funcionalidades excluidas (fuera del MVP)

La primera versión del sistema NO incluirá:

- Pagos automáticos o integración financiera
- Aplicación móvil nativa
- Integración con GPS o mapas en tiempo real
- Automatización con WhatsApp o correo
- Gestión de múltiples conductores
- Sistema multiusuario
- Notificaciones inteligentes
- Inteligencia artificial

---

## 5. Supuestos del sistema

- El sistema será utilizado por un solo conductor
- Los datos serán ingresados manualmente
- No existe integración con sistemas externos
- El usuario tiene conocimientos básicos de uso de smartphone

---

## 6. Limitaciones del MVP

- No existe sincronización automática con otras plataformas
- No hay reportes avanzados de ingresos
- No hay control automático de pagos
- No hay sistema de respaldo automatizado

---

## 7. Usuario principal

Conductor independiente que realiza traslados de pasajeros.

Ejemplo de usuario real: conductor que recibe solicitudes por WhatsApp o correo y actualmente gestiona sus viajes en un cuaderno.

---

## 8. Plataforma

Aplicación web optimizada para dispositivos móviles.

---

## 9. Problema que resuelve

Actualmente muchos conductores organizan sus viajes mediante cuadernos o notas manuales, lo que genera:

- Dificultad para visualizar horarios
- Desorden en la planificación
- Riesgo de errores en la gestión
- Dificultad para revisar historial

TripAgenda busca centralizar toda esta información en una agenda digital accesible desde el teléfono, reduciendo errores y mejorando la organización diaria.