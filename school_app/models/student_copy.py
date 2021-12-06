# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "schapp.student"
    _description = "Student"
    _inherits = {'res.partner': 'partner_id'}
    _rec_name = "name"
	
    partner_id = fields.Many2one('res.partner', ondelete='restrict', auto_join=True,string='Related Partner', help='Partner-related data of the student')

    name = fields.Char(related='partner_id.name', inherited=True, readonly=False)
    email = fields.Char(related='partner_id.email', inherited=True, readonly=False)
    image = fields.Binary(string="photo",attachment=True)
    parent_is_employee = fields.Boolean("Parent Is Employee" , default=False)

    parent_relation = fields.Selection([
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister')],string='Parent Relation', default='Father')
    parent_name = fields.Char(string="Parent Name",size=128, translate=True)
    address = fields.Text(string="Home Address",size=128, translate=True)
    phone = fields.Char(related='partner_id.phone', inherited=True, readonly=False)
    
    stage_id = fields.Many2one('schapp.stage',  'Stage' ,translate=True)
    level_id = fields.Many2one('schapp.level' , 'Level')
    parent_id = fields.Many2one('hr.employee','Parent')
    birth_date = fields.Date('Birth Date')
    blood_group = fields.Selection([
        ('A+', 'A+ve'),
        ('B+', 'B+ve'),
        ('O+', 'O+ve'),
        ('AB+', 'AB+ve'),
        ('A-', 'A-ve'),
        ('B-', 'B-ve'),
        ('O-', 'O-ve'),
        ('AB-', 'AB-ve')
    ], string='Blood Group')
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    ], 'Gender', required=True, default='m')
   # active = fields.Boolean(default=True)

    current_class= fields.Many2one('schapp.class','Student Class')
    nationality = fields.Many2one('res.country', 'Nationality')

    # name=fields.Char(compute="_compute_name", store=True)


    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "Birth Date can't be greater than current date!"))


    
    def create_customer_invoice(self):
        # name = self.name
        return {
            'res_model': 'account.move',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref("account.view_move_form").id,
            'target': 'current',
            # 'context': {'default_partner_id': name}

        }        





