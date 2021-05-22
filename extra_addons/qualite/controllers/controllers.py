# -*- coding: utf-8 -*-
# from odoo import http


# class Qualite(http.Controller):
#     @http.route('/qualite/qualite/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qualite/qualite/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qualite.listing', {
#             'root': '/qualite/qualite',
#             'objects': http.request.env['qualite.qualite'].search([]),
#         })

#     @http.route('/qualite/qualite/objects/<model("qualite.qualite"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qualite.object', {
#             'object': obj
#         })
