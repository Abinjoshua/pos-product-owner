# -*- coding: utf-8 -*-
{
    'name': "POS Product Owner",
    'version': "1.0",
    'license': "LGPL-3",
    'summary': """POS Product Owner, Designed to customize the POS module""",
    'description': """POS Product Owner, Designed to customize the POS module, adds a product owner field in the pos orderline and in the receipts""",
    'author': "Cybrosys",
    'website': "http://www.cybrosys.com",
    'sequence': 1,
    'application': True,
    'depends': ['base','point_of_sale','sale_management'],
    'auto_install': True,
    'data': ['views/product_product_views.xml',
             ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_product_owner/static/src/xml/custom_receipt.xml',
            'pos_product_owner/static/src/js/order_line.js',
            'pos_product_owner/static/src/xml/pos_order_line.xml',
            'pos_product_owner/static/src/xml/order_receipt.xml',
        ],
    }
}
