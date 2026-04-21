from odoo.tests.common import TransactionCase


class TestSeguimientoCliente(TransactionCase):
    def test_crear_seguimiento(self):
        partner = self.env.ref('base.res_partner_1')
        seguimiento = self.env['seguimiento.cliente'].create({
            'nombre': 'Test seguimiento',
            'cliente_id': partner.id,
            'fecha': '2026-04-21',
            'notas': 'Notas de prueba',
        })
        self.assertEqual(seguimiento.estado, 'pendiente')
        self.assertEqual(seguimiento.nombre, 'Test seguimiento')

    def test_marcar_realizado(self):
        partner = self.env.ref('base.res_partner_1')
        seguimiento = self.env['seguimiento.cliente'].create({
            'nombre': 'Test seguimiento',
            'cliente_id': partner.id,
            'fecha': '2026-04-21',
        })
        seguimiento.action_marcar_realizado()
        self.assertEqual(seguimiento.estado, 'realizado')