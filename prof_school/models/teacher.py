# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, fields


class Tacher(models.Model):
    _inherit = "hr.employee"
    _columns = {
        'name': fields.char('Name',  size=64),
        'order_line': fields.one2many('sch.student', 'student_id', 'Dependant Students'),
    }
