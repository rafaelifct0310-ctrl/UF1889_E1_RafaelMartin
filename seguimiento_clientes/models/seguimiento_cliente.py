from odoo import models, fields, api
from datetime import date


class SeguimientoCliente(models.Model):
    _name = 'seguimiento.cliente'
    _description = 'Seguimiento de Clientes'
    _order = 'fecha desc'

    nombre = fields.Char(string='Nombre', required=True)
    cliente_id = fields.Many2one(
        'res.partner',
        string='Cliente',
        required=True,
        domain=[('is_company', '=', True)]
    )
    fecha = fields.Date(
        string='Fecha',
        required=True,
        default=lambda self: fields.Date.today()
    )
    estado = fields.Selection(
        string='Estado',
        selection=[
            ('pendiente', 'Pendiente'),
            ('realizado', 'Realizado'),
        ],
        default='pendiente',
        required=True
    )
    notas = fields.Text(string='Notas')

    def action_marcar_realizado(self):
        for record in self:
            record.estado = 'realizado'
