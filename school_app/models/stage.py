# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class SchoolStage(models.Model):
    _name = "schapp.stage"
    _description = "School Stage"
    _rec_name = "name"

    name = fields.Char('Stage Name', size=128, translate=True)
