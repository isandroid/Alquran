# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api

class Tafsir(models.Model):
    _name = 'quranum_majid.tafsir'
    _description = 'Tafsir Alquran'

    name = fields.Char(string='Nomor')
    bahasa_id = fields.Many2one('quranum_majid.bahasa', string='Bahasa')
    teks = fields.Text(string='Teks')