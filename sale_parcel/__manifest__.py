# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Delivery InPost',
    'version': '1.0',
    'author': 'Ruslan Akunevich',
    'category': 'Customizations',
    'summary': 'Sales Orders, Delivery & Invoicing Control',
    'description': """
Delivery InPost
==================================

This module allows delivery to a parcel machine.
""",
    'depends': ['base', 'sale'],
    'data': [
        'security/sale_parcel_security.xml',
        'security/ir.model.access.csv',
        'data/parcel.locker.csv',
        'data/ir_cron_data.xml',
        'views/parcel_locker_views.xml',
        'views/sale_order_views.xml',
        'views/sale_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
