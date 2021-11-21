# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2021-TODAY Prof-Dev Integrated(<http://www.prof-dev.com>).

###############################################################################

{
    'name': 'Prof-Dev School MGMT',
    'version': '1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 1,
    'summary': 'Manage Students, School stages,levels, classes and fees',
     'complexity': "easy",
    'author': 'Prof-Dev Integrated Solutions',
    'website': 'http://www.prof-dev.com',
    'depends': [ 'hr'],
    'data': [
        'views/students.xml',
        'views/parent.xml',
        'views/class.xml',
        'views/level.xml',
        'views/stage.xml',
        'views/study_year.xml',
        'views/enrollment.xml',
        'security/ir.model.access.csv'

       
    ]


}