# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class SchoolStage(models.Model):
    _name = "sch.parent"
    _description = "School Parent"

    name = fields.Char('Parent Name', translate=True)
    phone = fields.Char("Phone")
    address = fields.Char("Parent Address" , translate=True)
   # is_employee = fields.Boolean("Is Employee" , default=True, translate=True)
    student_id = fields.One2many("sch.student" , 'parent_student')
    image = fields.Binary()

