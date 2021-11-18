# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, fields


class Parent(models.Model):
    _name="sch.parent"
    _inherit = "res.partner"
    
    name = fields.Char(string="Parert name")
    # relation with name-partener id 
    phone = fields.Char(string="Phone")
    address =
    studen = 
    # relation with student-id 
    is_employee

