# AGENTS.md - Odoo 19 Module: seguimiento_clientes

## Project Type
Odoo 19 add-on module for customer follow-up management.

## Module Structure
```
seguimiento_clientes/
├── __init__.py                     # Imports models
├── __manifest__.py                # Module metadata (depends: base, contacts)
├── models/
│   ├── __init__.py
│   └── seguimiento_cliente.py    # Model: seguimiento.cliente
├── views/
│   ├── seguimiento_cliente_views.xml  # Tree, Form, Search, action, menu
│   └── seguimiento_menu.xml         # Empty (menu in views.xml)
├── security/
│   └── ir.model.access.csv          # Access control
├── demo/
│   └── demo.xml
└── test/
    └── test_seguimiento_cliente.py
```

## Commands
- **Odoo shell**: `odoo shell -d <database>`
- **Install/Upgrade**: Apps > Update Apps List > Install/Upgrade seguimiento_clientes
- **Tests**: Odoo auto-discovers tests in `test/` - run via Odoo shell or UI

## Model: seguimiento.cliente
- `_name`: `seguimiento.cliente`
- Fields: `nombre`, `cliente_id` (Many2one to res.partner), `fecha`, `estado` (pendiente/realizado), `notas`
- Method: `action_marcar_realizado()` sets estado = 'realizado'

## Common Odoo Gotchas
- View arch: close all XML tags properly
- Field names: Python field names must match XML `<field name="...">`
- After code changes: run "Update Apps List" in Odoo
- Menu defined in `seguimiento_cliente_views.xml`, not in empty `seguimiento_menu.xml`
