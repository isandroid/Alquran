# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api

class Teks(models.Model):
    _name = 'quranum_majid.teks'
    _description = 'Teks Quran'

    bahasa_id = fields.Many2one('quranum_majid.bahasa', string='Bahasa')
    surat_id = fields.Many2one('quranum_majid.surat', string='Surat')
    ayat_nomor = fields.Integer(string='Nomor Ayat')
    teks = fields.Text(string='Teks')