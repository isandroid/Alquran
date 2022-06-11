# -*- coding: utf-8 -*-
# from odoo import http


# class QuranumMajid(http.Controller):
#     @http.route('/quranum_majid/quranum_majid', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quranum_majid/quranum_majid/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('quranum_majid.listing', {
#             'root': '/quranum_majid/quranum_majid',
#             'objects': http.request.env['quranum_majid.quranum_majid'].search([]),
#         })

#     @http.route('/quranum_majid/quranum_majid/objects/<model("quranum_majid.quranum_majid"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quranum_majid.object', {
#             'object': obj
#         })
