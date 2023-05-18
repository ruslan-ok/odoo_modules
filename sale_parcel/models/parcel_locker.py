# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _

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
    
