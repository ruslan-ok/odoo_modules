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
        'security/ir.model.access.csv',
        'data/parcel.locker.csv',
        'views/parcel_locker_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
