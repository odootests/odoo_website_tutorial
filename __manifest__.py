# -*- coding: utf-8 -*-
{
    'name': "Academy",
    'summary': "summary",
    'description': "descrption",
    'author': "Company Name Here",
    'website': "http://www.yourcompanysite.com",
    'category': 'Website',
    'version': '0.1',
    'depends': ['base', 'website'],
    'application': True,
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/allteachers.xml'
    ],
    'demo':['demo/demo.xml']
}