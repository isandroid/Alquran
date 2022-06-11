# -*- coding: utf-8 -*-
{
    'name': "quranum_majid",

    'summary': """Aplikasi Database Quranum Majid""",

    'description': """Aplikasi Database Quranum Majid""",

    'author': "Isa Mujahid Islam",
    'website': "https://github.com/isandroid",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'data/quranum_majid.quran_teks_arab.csv',
        'views/quran_teks_arab.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
