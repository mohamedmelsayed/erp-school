# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class SchoolParent(models.Model):
    _name = "schapp.parent"
    _description = "Parent"
	
    _rec_name = "name"
    employee_id = fields.Many2one('hr.employee','Employee Id')

    name = fields.Char(string="Name")
    email = fields.Char(string="Email" )
    phone = fields.Char(string="phone" )
    address = fields.Char(string="Address" )
    is_employee = fields.Boolean("Is Employee" , default=False)
    student_id = fields.One2many("schapp.student","parent_id" )

