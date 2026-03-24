# Bitácora de desarrollo - TripAgenda

## Día 1 (16/3/2026)

Se crea el proyecto TripAgenda.

Se define la visión del sistema y el alcance inicial.

Se decide analizar el cuaderno de trabajo del usuario (conductor independiente) para realizar un levantamiento de requerimientos basado en el proceso real.

## Día 2 (17/3/2026)

Qué se hizo:

levantamiento con usuario
análisis del flujo real
definición de reglas de negocio
creación de documentos (alcances, reglas, etc.)
diseño del flujo del sistema

Decisiones importantes:

TripAgenda como agenda + control de pagos
dejar “red de conductores” como fase futura

Estado actual:

fase de análisis completándose

## Día 3 (18/3/2026)

Trabajo realizado

- Revisión y mejora del documento de alcance (alcances.md)
- Definición clara del MVP del sistema
- Creación del documento de requerimientos (requerimientos.md)
- Ajuste y validación de requerimientos funcionales y no funcionales
- Identificación de caso real: viajes "particulares" sin empresa
- Reestructuración completa de reglas de negocio (reglas.md)
- Separación correcta entre requerimientos y reglas de negocio

---

Decisiones importantes

- Se define el MVP enfocado en:
  
  - gestión de viajes
  - agenda
  - empresas
  - detección de conflictos

- Los viajes pueden ser:
  
  - asociados a una empresa
  - o marcados como "particular"

- El sistema sugiere resolución de conflictos, pero el usuario toma la decisión final

- Se incorpora sistema de estados de viaje:
  
  - pendiente
  - confirmado
  - realizado
  - cancelado
  - cedido

---

Estado actual del proyecto

- Fase de análisis y definición: prácticamente completa

- Documentos listos:
  
  - visión.md 
  - alcances.md 
  - requerimientos.md 
  - reglas.md 

- Próximo paso:
  → Definición del modelo de datos (modelo_datos.md)

---

Notas

- Se trabajó con menor energía debido a resfriado
- Aun así se lograron avances importantes en estructura del sistema

## Día 4 (19/3/2026)

Trabajo realizado

- Retoma del proyecto TripAgenda
- Revisión del estado general del sistema
- Definición y validación del modelo de datos (modelo_datos.md)
- Corrección de entidades y relaciones:
  - ajuste de Viaje
  - simplificación de Empresa
  - mejora en Pasajero
  - definición de Tipo de Viaje
- Refinamiento del diagrama de flujo del sistema (diagrama_flujo.md)
- Transformación de flujo conceptual a flujo operativo:
  - creación de viaje
  - edición de viaje
  - detección de conflictos
  - gestión de estados
- Definición de la arquitectura del sistema (arquitectura.md):
  - aplicación web responsive
  - arquitectura cliente-servidor
  - backend con Python + FastAPI
  - base de datos PostgreSQL
- Validación final de toda la documentación del sistema

---

Decisiones importantes

- Se adopta arquitectura simple basada en:
  
  - frontend web
  - backend API REST
  - base de datos relacional

- Se prioriza simplicidad para el MVP sobre soluciones complejas

- Se define el flujo completo del sistema incluyendo:
  
  - validación de conflictos
  - decisiones del usuario
  - estados del viaje

- Se estructura el modelo de datos preparado para futura escalabilidad

---

Estado actual del proyecto

- Fase de análisis y diseño: COMPLETADA 

Documentación completa:

- visión.md 
- alcances.md 
- requerimientos.md 
- reglas.md 
- modelo_datos.md 
- diagrama_flujo.md 
- arquitectura.md 

El proyecto está listo para iniciar desarrollo.

---

Próximo paso

→ Inicio del desarrollo backend:

- configuración del entorno Node.js
- creación de servidor con Express
- primeros endpoints

---

Notas

- Se consolida la base completa del sistema antes de escribir código
- Se logra un nivel de claridad que permite desarrollo sin improvisación

## Día 5 (20/3/2026)

Trabajo realizado:

Creación del repositorio en GitHub
Inicialización del proyecto con Git
Primer commit del sistema (estructura base)
Subida del proyecto a repositorio remoto

Corrección de estructura:
uso de archivos .gitkeep para incluir carpetas vacías (backend y frontend)

Aprendizaje de comandos Git fundamentales:

git init
git add
git commit
git push

Comprensión del flujo de trabajo de Git:

working directory
staging area
repository local
repositorio remoto (GitHub)
Desarrollo backend (inicio)
Instalación de entorno Python
Resolución de problema con pip (uso de ensurepip)

Instalación de dependencias:

fastapi
uvicorn

Creación del archivo main.py en carpeta /backend
Implementación de servidor básico con FastAPI
Creación del primer endpoint (/)
Ejecución del servidor local con uvicorn
Verificación en navegador de funcionamiento correcto
Exploración de documentación automática (/docs)

Flujo completo:

usuario → frontend → API → backend → respuesta
Uso correcto de IA como asistente, no como ejecutor total

Decisiones importantes:

Se adopta Python + FastAPI como backend principal
Se decide mantener frontend simple (sin React en etapa inicial)
Se establece metodología de trabajo basada en:
uso de IA guiado
comprensión del código
revisión y mentoría
Se define GitHub como repositorio oficial del proyecto y portafolio

Estado actual del proyecto:

Fase de documentación: COMPLETADA 
Backend iniciado correctamente 
Servidor funcionando localmente 
Primer endpoint operativo 

Próximo paso:

→ Crear endpoint /viajes
→ Simular almacenamiento de datos en memoria
→ Construir estructura base de API REST

Notas
Se consolida el inicio real del desarrollo del sistema

## Día 6 (21/3/2026)

Qué se hizo:

Implementación de arquitectura backend (models, routes, services)
Creación de base de datos en PostgreSQL
Conexión de FastAPI con base de datos
Implementación de CRUD persistente
Uso de SQLAlchemy como ORM

Logro importante:

Primer sistema funcional con persistencia real de datos

## Día 7 (23/3/2026)

Qué se hizo

Implementación de validaciones avanzadas en modelo Pydantic (Viaje)

Restricción de campos:

  valor > 0
  origen y destino no vacíos
  estado con valores controlados

Implementación de lógica de conflicto horario en creación y actualización de viajes

Corrección de conflicto en UPDATE excluyendo el mismo ID

Implementación de filtro por fecha exacta en endpoint GET /viajes

Implementación de filtro por rango de fechas (fecha_inicio / fecha_fin)

Validación de combinaciones inválidas de parámetros en filtros

Decisiones importantes

Se define estrategia de filtros dinámica en un solo endpoint (no múltiples endpoints)

Se decide postergar filtros por empresa hasta implementar entidad Empresa

Se define que el modelo Viaje queda cerrado para MVP funcional

Estado actual

Backend funcional con:

CRUD completo
Validaciones
Persistencia en base de datos
Filtros de consulta
Entidad Viaje finalizada para MVP
Próximo paso: diseño e implementación de entidad Empresa