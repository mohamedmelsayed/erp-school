# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class Enrollment(models.Model):
    _name = "sch.enrollment"

    student_id=fields.Many2one('sch.student','Student')
    year_id=fields.Many2one('sch.study_year','Study Year')
    class_name_id=fields.Many2one('sch.class','Student Class')