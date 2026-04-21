{
    'name': 'Seguimiento de Clientes',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Módulo para gestionar el seguimiento de clientes',
    'description': """
        Módulo para realizar seguimiento de interacciones con clientes.
        Permite registrar visitas, llamadas y otras comunicaciones.
    """,
    'author': 'Rafael Martin',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/seguimiento_cliente_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
