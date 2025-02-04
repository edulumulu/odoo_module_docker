# -*- coding: utf-8 -*-
# from odoo import http


# class WorkTraining(http.Controller):
#     @http.route('/work__training/work__training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/work__training/work__training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('work__training.listing', {
#             'root': '/work__training/work__training',
#             'objects': http.request.env['work__training.work__training'].search([]),
#         })

#     @http.route('/work__training/work__training/objects/<model("work__training.work__training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('work__training.object', {
#             'object': obj
#         })

