# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "sch.student"
    _description = "Student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    #_inherits = {"res.partner"}

    student_name = fields.Char('Student Name', required=True ,  translate=True)
    image = fields.Binary()

    stage_id = fields.Many2one('sch.stage',  'Stage' ,translate=True)
    level_id = fields.Many2one('sch.level' , 'Level')
    parent_student = fields.Many2one('sch.parent','Parent', required=True)
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

    current_class= fields.Many2one('sch.class','Student Class')
    nationality = fields.Many2one('res.country', 'Nationality')


    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "Birth Date can't be greater than current date!"))



