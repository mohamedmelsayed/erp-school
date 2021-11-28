# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenEduCat Inc.
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, fields


class OpFeesElementLine(models.Model):
    _name = "schapp.feeselement"
    _description = "Fees Element for course"
    _rec_name = "product_id"

    sequence = fields.Integer('Sequence')
    product_id = fields.Many2one('product.product',
                                 'Fees Name', required=True)
    value = fields.Float('Value')
    due_days = fields.Integer('Due Days')
    due_date = fields.Date('Due Date')
    fees = fields.Many2one('schapp.terms')
