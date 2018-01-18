# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teachers(models.Model):
	_name='academy.teachers'
	name = fields.Char("Teacher Name")
	biography = fields.Html("Teacher Bio")
	course_ids = fields.One2many('product.template', 'teacher_id', string='Courses')
	
class Course(models.Model):
	# _name='product.template'
	# _inherit='mail.thread'
	_inherit='product.template'
	name = fields.Char("Course Name")
	teacher_id = fields.Many2one('academy.teachers', 'Teacher', index=True, required=True)

# class academy(models.Model):
#     _name = 'academy.academy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100