# -*- coding: utf-8 -*-
{
   'name': "Academy",
   'summary': "summary",
   'description': "descrption",
   'author': "Company Name Here",
   'website': "http://www.yourcompanysite.com",
   'category': 'Website',
   'version': '0.1',
   'depends': ['base', 'website', 'mail', 'website_sale'],
   'application': True,
   'data': [
        #'security/ir.model.access.csv',
      'views/views.xml',
      'views/templates.xml',
      'views/allteachers.xml',
		'views/data.xml'
   ],
   'demo':['demo/demo.xml']
}