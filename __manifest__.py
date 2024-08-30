{
    'name': 'Usability Testing Module',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Module for managing usability testing in software development',
    'author': 'Raidel Martínez Santos & Robert Hillary Serna',
    'website': 'https://github.com/YoshiLoL0526/usability_test_module',
    'depends': ['base'],
    'data': [
        'views/base_views.xml',
        'views/tests_views.xml',
        'views/principles_views.xml',
        'security/ir.model.access.csv',
        'data/principios.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
