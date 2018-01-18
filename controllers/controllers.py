# -*- coding: utf-8 -*-
from odoo import http

class Adacemy(http.Controller):
	#return server response 
	@http.route('/academy/academy/', auth='public')
	def index(self, **kw):
		return "Hey"

	#return hard-coded array and render template with id: list_teachers
	@http.route('/academy/teachers/', auth='public')
	def list_teachers(self, **kw):
		context_val = {
			'teachers': ['Diana Dille', 'Jahir Jahon', "Lester Lestery"],
		}
		return http.request.render('academy.list_teachers', context_val)

	#return all records from model and render template with specific id
	@http.route('/academy/allteachers/', auth='public', website=True)
	def get_all_teachers(self, **kw):
		Teachers = http.request.env['academy.teachers']
		teachers = Teachers.search([])
		context = {
			'teachers': teachers
		}
		return http.request.render('academy.get_all_teachers', context)

	#pass variables through routes
	@http.route('/academy/new/<name>/', auth='public', website=True)
	def display_name(self, name):
		return '<h1> {} </h1>'.format(name)

	#pass variables of specific type through routes
	@http.route('/academy/new/<int:id>/', auth='public', website=True)
	def display_value_with_type(self, id):
		return '<h1> {} ({})</h1>'.format(id, type(id).__name__)

	#set route that searches the model and returns an object/record
	@http.route('/academy/<model("academy.teachers"):dbobject>/', auth='public', website=True)
	def show_person(self, dbobject):
		context = {'person': dbobject}
		return http.request.render('academy.biography', context)


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