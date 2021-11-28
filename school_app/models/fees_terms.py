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

from odoo import models, api, fields, exceptions, _


class OpFeesTerms(models.Model):
    _name = "schapp.terms"
    _inherit = "mail.thread"
    _description = "Fees Terms For Course"
    _rec_name = "name"
    

    name = fields.Char('Fees Terms', required=True)
    active = fields.Boolean('Active', default=True)
    fees_terms = fields.Selection([('fixed_days', 'Fixed Fees of Days'),
                                   ('fixed_date', 'Fixed Fees of Dates')],
                                  string='Term Type', default='fixed_days')
    note = fields.Text('Description')
    
    company_id = fields.Many2one('res.company', 'Company', required=True,
                                 default=lambda s: s.env.user.company_id)
    order_date = fields.Datetime('date')
    day_type = fields.Selection([('before', 'Before'), ('after', 'After')])
  
     
    discount = fields.Float(string='Discount (%)', digits='Discount', default=0.0)
                           
    partner_id = fields.Many2one(
        'res.partner', string='Student',
        # states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)
    payment_term_id = fields.Many2one(
        'account.payment.term', string='Payment Terms', check_company=True,  # Unrequired company
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)
    fees_element = fields.One2many('schapp.feeselement' , 'fees')

    @api.model
    def create(self, vals):
        res = super(OpFeesTerms, self).create(vals)
        if not res.line_ids:
            raise exceptions.AccessError(_("Fees Terms must be Required!"))
        total = 0.0
        for line in res.line_ids:
            if line.value:
                total += line.value
        if total != 100.0:
            raise exceptions.AccessError(
                _("Fees terms must be divided as such sum up in 100%"))
        return res


# class OpStudentCourseInherit(models.Model):
#     _inherit = "op.student.course"

#     fees_term_id = fields.Many2one('op.fees.terms', 'Fees Term')
#     fees_start_date = fields.Date('Fees Start Date')
