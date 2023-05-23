# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import pandas as pd
import json


class ParcelLocker(models.Model):
    """ Model for a parcel locker.
        Parcel locker is an automated postal box that allows users
        for a self-service collection of parcels and oversize letters
        as well as the dispatch of parcels.
    """
    _name = 'parcel.locker'
    _description = 'Parcel Lockers'
    _rec_name = 'code'
    _order = 'code'
    _rec_names_search = ['code', 'city', 'street', 'building', 'zip', 'description']

    code = fields.Char('Code', required=True)
    description = fields.Char('Description')
    city = fields.Char('City', required=True)
    city_eng = fields.Char('City in English', required=True)
    street = fields.Char('Street', required=True)
    area = fields.Char('Area', required=True)
    zip = fields.Char('Post code (zip)', required=True)
    building = fields.Char('Building number')
    latitude = fields.Char('Latitude', required=True)
    longitude = fields.Char('Longitude', required=True)
    sale_order_ids = fields.One2many(comodel_name='sale.order', inverse_name='parcel_locker_id', string='Orders for this Parcel Machine')
    count = fields.Integer(string="Order Count", compute='_compute_count', store=True)

    #=== COMPUTE METHODS ===#

    @api.depends('sale_order_ids')
    def _compute_count(self):
        for wizard in self:
            wizard.count = len(wizard.sale_order_ids)

    def _cron_update_from_csv(self, fname='points.json'):
        with open(fname) as data_file:
            data = json.load(data_file)
        df = pd.json_normalize(data, 'items')
        df_torun = df[df['g'] == 'torun'][['n', 'd', 'c', 'g', 'e', 'r', 'o', 'b', 'l.a', 'l.o']]
        last_id = 0
        self._cr.execute('SELECT max(parcel_locker.id) FROM parcel_locker')
        res = self._cr.fetchone()
        if res:
            last_id = res[0]
        for index, row in df_torun.iterrows():
            pm = self.env['parcel.locker'].search(domain=[('code', '=', row['n'])], limit=1)
            if pm:
                if (pm['description'] != row['d']) or (pm['city'] != row['c']) or (pm['city_eng'] != row['g']) or (pm['street'] != row['e']) or (pm['area'] != row['r']) or \
                    (pm['zip'] != row['o']) or (pm['building'] != row['b']) or (pm['latitude'] != row['l.a']) or (pm['longitude'] != row['l.o']):
                    pm.write({
                        'description': row['d'], 
                        'city': row['c'], 
                        'city_eng': row['g'], 
                        'street': row['e'], 
                        'area': row['r'], 
                        'zip': row['o'], 
                        'building': row['b'], 
                        'latitude': row['l.a'], 
                        'longitude': row['l.o']
                        })
            else:
                if index > last_id:
                    last_id = index
                else:
                    last_id += 1
                self.env['parcel.locker'].create({
                    'id': last_id, 
                    'code': row['n'], 
                    'description': row['d'], 
                    'city': row['c'], 
                    'city_eng': row['g'], 
                    'street': row['e'], 
                    'area': row['r'], 
                    'zip': row['o'], 
                    'building': row['b'], 
                    'latitude': row['l.a'], 
                    'longitude': row['l.o']
                    })
                self.env['parcel.locker'].flush_model()
