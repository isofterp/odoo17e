# -*- coding: utf-8 -*-
{
    'name': "Isoft Afriplus",

    'summary': " Afriplus",

    'description': """
        Various Odoo customizations Afriplus
    """,

    'author': "I-Soft Solutions",
    'website': "https://www.isoft.co.za",

    'category': 'Sales/Sales',
    'version': '17.0',

    'depends': ['sale','account', 'stock', 'helpdesk_repair','repair'],
    'data': [
        'views/product_views.xml',
        'views/account_move_views.xml',
        'views/stock_picking_views.xml',
        'views/repair_views.xml',
        'views/helpdesk_ticket_views.xml',
        'report/report_invoice.xml',
        'report/report_stockpicking_operations.xml',
        'report/report_deliveryslip.xml',
    ],

    'application': True,
}
