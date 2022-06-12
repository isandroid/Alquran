# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api

class Surat(models.Model):
    _name = 'quranum_majid.surat'
    _description = 'Surat Alquran'

    name = fields.Char(string='Nama Bahasa')
    tempat_turun = fields.Selection([("mekah", "Mekah"), ("madinah", "Madinah")])
    jumlah_ayat = fields.Integer()