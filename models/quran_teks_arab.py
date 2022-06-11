# -*- coding: utf-8 -*-

from odoo import models, fields, api

class QuranTeksArab(models.Model):
    _name = 'quranum_majid.quran_teks_arab'
    _description = 'Teks Arab Quran'

# id,surat,ayat,teks

    quran_teks_arab_id = fields.Integer(string='ID')
    surat = fields.Integer(string='Nomor Surat')
    ayat = fields.Integer(string='Nomor Ayat')
    teks = fields.Text(string='Teks Arab')

    # value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
