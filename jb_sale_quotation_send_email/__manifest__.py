{
    'name': 'Sale Quotation Send By Email',
    'summary': 'This Module Send Quotation on Email And Also Send Quotation Report',
    'author': 'Joyanto Barmon',
    'license': 'AGPL-3',
    'website': 'http://examples.com.bd/',
    'category': 'sale',
    'sequence': 1,
    'version': '13.0.1.0.0',
    'depends': [
        'sale', 'mail',
    ],
    'data': [
        'data/sale_order_mail_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}