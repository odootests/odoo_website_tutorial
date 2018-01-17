# -*- coding: utf-8 -*-
from odoo import http

class Adacemy(http.Controller):
	@http.route('/academy/academy/', auth='public')
	def index(self, **kw):
		return "Hey"

	@http.route('/academy/teachers/', auth='public')
	def list_teachers(self, **kw):
		context_val = {
			'teachers': ['Diana Dille', 'Jahir Jahon', "Lester Lestery"]
		}
		return http.request.render('academy.list_teachers', context_val)



# class Academy(http.Controller):
#     @http.route('/academy/academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })