# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class StageLevel(models.Model):
    _name = "schapp.level"
    _description = "School levels"

    name = fields.Char('Level Name', size=128, translate=True)
    stage_id = fields.Many2one('schapp.stage', 'Stage', ondelete="cascade", tracking=True)
    