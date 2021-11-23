# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, api, fields, exceptions, _


class FeesTermsLine(models.Model):
    _name = "sch.fees.terms.line"
    _rec_name = "due_days"
    _description = "Fees Details Line"

    due_days = fields.Integer('Due Days')
    value = fields.Float('Value (%)')
    fees_element_line = fields.One2many("sch.fees.element",
                                        "fees_terms_line_id", "Fees Elements")
    fees_id = fields.Many2one('sch.fees.terms', 'Fees')


class FeesTerms(models.Model):
    _name = "sch.fees.terms"
    _inherit = "mail.thread"
    _description = "Fees Terms For Course"

    name = fields.Char('Fees Terms', required=True)
    active = fields.Boolean('Active', default=True)
    note = fields.Text('Description')
    company_id = fields.Many2one('res.company', 'Company', required=True,
                                 default=lambda s: s.env.user.company_id)
    no_days = fields.Integer('No of Days')
    day_type = fields.Selection([('before', 'Before'), ('after', 'After')],
                                'Type')
    line_ids = fields.One2many('sch.fees.terms.line', 'fees_id', 'Terms')
    discount = fields.Float(string='Discount (%)',
                            digits='Discount', default=0.0)

    @api.model
    def create(self, vals):
        res = super(FeesTerms, self).create(vals)
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
