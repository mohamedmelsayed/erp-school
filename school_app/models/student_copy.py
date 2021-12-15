# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, api, fields, _
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "schapp.student"
    _description = "Student"
    _inherits = {'res.partner': 'partner_id'}
    _rec_name = "name"
	
    partner_id = fields.Many2one('res.partner', ondelete='restrict', auto_join=True,string='Related Partner', help='Partner-related data of the student')

    name = fields.Char(related='partner_id.name', inherited=True, readonly=False, required=True)
    email = fields.Char(related='partner_id.email', inherited=True, readonly=False)
    image = fields.Binary(string="photo",attachment=True)
    parent_is_employee = fields.Boolean("Parent Is Employee" , default=False)
    sequence = fields.Char(default=lambda self:_('new'))
    invoice_count = fields.Integer(string='Invoice Count', readonly=True, default="1")
    student_cv = fields.Html(string="Student Cv")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    parent_relation = fields.Selection([
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister')],string='Parent Relation', default='Father')
    parent_name = fields.Char(string="Parent Name",size=128, translate=True)
    address = fields.Char(string="Home Address",size=128, translate=True)
    phone = fields.Char(related='partner_id.phone', inherited=True, readonly=False)
    mobile = fields.Char()
    
    stage_id = fields.Many2one('schapp.stage',  'Stage' ,translate=True)
    level_id = fields.Many2one('schapp.level' , 'Level')
    parent_id = fields.Many2one('hr.employee','Parent')
    birth_date = fields.Date('Birth Date')
    registration_date = fields.Date(' ', readonly=True, default=fields.Datetime.today())
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
    invoice_status = fields.Selection([
        ('upselling', 'Upselling Opportunity'),
        ('invoiced', 'Fully Invoiced'),
        ('to invoice', 'To Invoice'),
        ('no', 'Nothing to Invoice')
        ], string='Invoice Status', store=True, readonly=True)

    # name=fields.Char(compute="_compute_name", store=True)

    def action_confirm(self):
        self.state = 'confirm'  
    
    def action_cancel(self):
        self.state = 'cancel' 

    def action_draft(self):
        self.state = 'draft'       

    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError (_(
                    "Birth Date can't be greater than current date!"))


    
    def create_customer_invoice(self):

        return {
            'name':  _('Student Invoice'),
            'view_type': 'form',
            'res_model': 'account.move',
            'view_id': self.env.ref("account.view_move_form").id,
            'view_mode': 'form',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {'default_type': 'out_invoice','default_partner_id': self.partner_id.id}

        }  

    # @api.model
    # def action_view_invoice(self):
    #     res = super(Student, self).action_view_invoice()
    #     return res     

    @api.model
    def create(self, values):
        values["sequence"] = self.env['ir.sequence'].next_by_code('student.number')
        return super(Student ,self).create(values)
   



# class AMM(models.Model):
#     _inherit = 'account.move'

#     @api.onchange('partner_id')
#     def create_yu(self):
#         gender = self.env.context.get('gender')
#         raise ValidationError(_(gender))





