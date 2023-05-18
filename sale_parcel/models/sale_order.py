# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    delivery_inpost = fields.Boolean('Delivery InPost', default=False)
    parcel_locker_id = fields.Many2one('parcel.locker', string='Parcel Delivery Address',
        help='Parcel locker address for delivery.')

    @api.onchange('partner_id')
    def _onchange_partner_id_inpost(self):
        self.delivery_inpost = False
        self.parcel_locker_id = False

