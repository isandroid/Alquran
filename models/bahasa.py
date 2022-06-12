# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api

class Bahasa(models.Model):
    _name = 'quranum_majid.bahasa'
    _description = 'Bahasa Alquran'

    name = fields.Char(string='Nama Bahasa')