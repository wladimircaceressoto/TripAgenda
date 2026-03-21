## Flujo del Sistema (fase 1)

# Flujo principal — Gestión de viajes

[ Inicio ]
↓
[ Ver agenda diaria ]
↓
¿Acción del usuario?
 ├── Ver viaje
 ├── Crear viaje
 └── Editar viaje

# Flujo: Crear viaje

[ Crear viaje ]
↓
[ Ingresar datos ]
↓
[ Guardar viaje ]
↓
[ Validar conflicto de horario ]
↓
¿Existe conflicto?
 ├── Sí → [ Mostrar advertencia ]
 │        ↓
 │   [ Usuario decide continuar o modificar ]
 └── No → continuar
↓
[ Guardado exitoso ]
↓
[ Volver a agenda diaria ]

# Flujo: Editar viaje

[ Seleccionar viaje ]
↓
[ Editar datos ]
↓
[ Guardar cambios ]
↓
[ Validar conflicto ]
↓
(igual que crear)
↓
[ Volver a agenda ]

# Flujo: Ejecución del servicio

[ Viaje en agenda ]
↓
[ Marcar estado ]
 ├── realizado
 ├── cancelado
 └── cedido
↓
[ Guardar estado ]

# Flujo: Historial

[ Ver agenda ]
↓
[ Navegar a fechas pasadas ]
↓
[ Visualizar viajes ]