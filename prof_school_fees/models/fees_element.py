# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, fields


class FeesElementLine(models.Model):
    _name = "sch.fees.element"
    _description = "Fees Element for course"

    sequence = fields.Integer('Sequence')
    product_id = fields.Many2one('product.product',
                                 'Product(s)', required=True)
    value = fields.Float('Value (%)')
    fees_terms_line_id = fields.Many2one('sch.fees.terms.line',
                                         string='Fees Terms')
