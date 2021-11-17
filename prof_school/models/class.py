# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class SchoolClass(models.Model):
    _name = "sch.class"
    _description = "School Classes "

    name = fields.Char('Class Name', size=128, translate=True)
    level_id = fields.Many2one('sch.level', 'Level', ondelete="cascade", tracking=True)
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female')])