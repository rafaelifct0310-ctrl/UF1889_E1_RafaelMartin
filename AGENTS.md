# AGENTS.md - Odoo 19 Module: seguimiento_clientes

## Project Type
Odoo 19 add-on module for customer follow-up management.

## Module Structure
```
seguimiento_clientes/
├── __init__.py           # Empty, imports models
├── __manifest__.py       # Module metadata (depends: base, contacts)
├── models/
│   ├── __init__.py       # Empty
│   └── seguimiento.py    # Model: seguimiento.cliente
├── views/
│   ├── seguimiento_views.xml    # Tree, Form, Search views + action + menu
│   └── seguimiento_menu.xml     # Empty (menu defined in views.xml)
├── security/
│   └── ir.model.access.csv      # Missing - needs creation
├── data/
├── demo/
└── test/
    └── __init__.py               # Empty
```

## Key Commands
- **Odoo shell**: `odoo shell -d <database>`
- **Upgrade module**: Apps > Update module list > Upgrade seguimiento_clientes
- **Run tests**: Odoo automatically discovers tests in `test/` directory

## Critical Notes
- This is an Odoo module, not a standalone Python project
- No standard `npm`, `pip`, or build commands apply
- Module must be installed within an Odoo 19 instance
- The `security/ir.model.access.csv` file is referenced in `__manifest__.py` but missing - must be created
- `views/seguimiento_menu.xml` is empty but menu is already defined in `seguimiento_views.xml`

## Model: seguimiento.cliente
- `_name`: `seguimiento.cliente`
- Fields: `nombre`, `cliente_id` (Many2one to res.partner), `fecha`, `estado` (selection: pendiente/realizado), `notas`
- Method: `action_marcar_realizado()` marks record as "realizado"

## Common Odoo Errors to Avoid
- View arch malformed: always close XML tags properly
- Field name mismatch: Python field names must match XML `<field name="">`
- Missing dependencies in `__manifest__.py` causes installation failure
- Must run "Update Apps List" in Odoo after adding new module
