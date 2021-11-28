# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class StudyYear(models.Model):
    _name = "schapp.study_year"
    _rec_name = "year_name"

    year_name = fields.Char(compute="_compute_year_name", store=True)
    start_date = fields.Date('Begining Date')
    end_date = fields.Date('End Date')


    @api.depends('start_date', 'end_date')
    def _compute_year_name(self):
        self.year_name = str(self.start_date)+" - "+str(self.end_date)
