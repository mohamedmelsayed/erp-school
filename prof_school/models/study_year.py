# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class StudyYear(models.Model):
    _name = "sch.study_year"

    year_name = fields.Char('Year Name', translate=True)

    start_date = fields.Date('Begining Date')
    end_date = fields.Date('End Date')

    @api.onchange('year_name', 'end_date')
    def _onchange_name(self):
        self.year_name=self.start_date+" - "+self.end_date