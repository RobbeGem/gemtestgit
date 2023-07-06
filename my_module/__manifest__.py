# -*- coding: utf-8 -*-
{
    'name': "my module",
    'description': """
        my description
    """,
    'summary': "",
	'author':"Gembaware",
	'website': 'http://gembaware.com',
	'category': 'Technical',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts',
    ],

    'data': [
        "security/groups.xml",
        'security/ir.model.access.csv',
        "views/my_model.xml",
        "views/res_partner.xml",
        "wizard/my_model_wizard.xml"
    ],
}

