# Plan Técnico: Módulo seguimiento_clientes para Odoo 19

## 1. Lista de archivos necesarios

seguimiento_clientes/
├── __init__.py                      # Inicialización del paquete
├── __manifest__.py                  # Manifiesto del módulo (Odoo 19)
├── models/
│   ├── __init__.py                   # Inicialización de models
│   └── seguimiento_cliente.py       # Modelo principal
├── views/
│   ├── seguimiento_cliente_views.xml # Vistas tree y form
│   └── seguimiento_cliente_menu.xml  # Menúes
├── security/
│   └── ir.model.access.csv           # Control de acceso
├── data/
│   └── secuencia.xml                  # Secuencia para IDs (opcional)
├── demo/
│   └── demo.xml                       # Datos de demostración
└── tests/
    ├── __init__.py
    └── test_seguimiento_cliente.py   # Pruebas unitarias


## 2. Orden correcto de implementación

| Paso | Archivo | Descripción |
|------|---------|-------------|
| 1 | __manifest__.py | Definir metadatos del módulo (nombre, versión, dependencias, categoría) |
| 2 | __init__.py (raíz) | Importar models |
| 3 | models/seguimiento_cliente.py | Crear clase Python con campos: nombre, cliente (Many2one), fecha, estado (selection), notas (text) |
| 4 | models/__init__.py | Importar la clase |
| 5 | views/seguimiento_cliente_views.xml | Definir vista tree, vista form, y botón de acción |
| 6 | views/seguimiento_cliente_menu.xml | Crear menú y acción para acceder a las vistas |
| 7 | security/ir.model.access.csv | Definir permisos (lectura, escritura, creación, eliminación) |
| 8 | tests/test_seguimiento_cliente.py | Crear pruebas unitarias |
| 9 | demo/demo.xml | Datos de ejemplo (opcional) |
| 10 | Actualizar módulo en Odoo | Instalación y pruebas


## 3. Errores habituales en Odoo 19

### Errores de sintaxis del modelo
- Nombre de campo duplicado: Usar el mismo nombre dos veces
- Olvidar required=True en campos obligatorios
- Tipo de campo incorrecto: Confundir many2one con many2many

### Errores en vistas XML
- ID de vista duplicado
- Etiqueta <field> mal anidada
- Nombre de campo inexistente
- View arch malformed: Etiquetas no cerradas

### Errores en el manifest
- Dependencias faltantes
- Formato JSON inválido
- Orden de claves incorrecto

### Errores de instalación
- No actualizar lista de módulos
- Cache de Odoo
- Permisos insuficientes

### Errores en botones
- Método no existe
- Tipo de botón incorrecto


## 4. Checklist final de validación

### Verificación del código
[ ] El modelo tiene todos los campos requeridos: nombre, cliente, fecha, estado, notas
[ ] Campo cliente es Many2one hacia res.partner
[ ] Campo estado es selection con opciones: pendiente, realizado
[ ] Vista tree muestra los campos relevantes
[ ] Vista form permite edición completa
[ ] Botón cambia estado a "realizado" correctamente
[ ] El filtro muestra solo registros pendientes

### Verificación de seguridad
[ ] Archivo ir.model.access.csv creado con permisos correctos
[ ] Grupo de usuarios asignado

### Verificación funcional
[ ] El módulo se instala sin errores
[ ] Se pueden crear nuevos registros
[ ] El botón de cambiar estado funciona
[ ] El filtro por "pendiente" muestra los registros correctos

### Verificación de pruebas
[ ] Las pruebas unitarias pasan
[ ] Las pruebas cubren creación y cambio de estado

### Documentación de evidencias
[ ] Captura de pantalla del modelo en modo desarrollador
[ ] Captura de vista tree con registros
[ ] Captura de vista form
[ ] Captura de filtro funcionando
[ ] Resultado de pruebas unitarias


## Notas adicionales

- En Odoo 19, el archivo de manifiesto se llama __manifest__.py
- La definición de campos usa la nueva API (campos como atributos de clase)
- El modelo res.partner está en el módulo base
