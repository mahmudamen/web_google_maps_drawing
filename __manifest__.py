# -*- coding: utf-8 -*-
{
    'name': 'Web Google Maps Drawing',
    'author': 'mahmudamen',
    'license': 'AGPL-3',
    'maintainer': 'mahmudamen',
    'support': 'mahmudamen@gmail.com',
    'category': 'Extra Tools',
    'description': """
Web Google Maps Drawing
=======================

Allows users to draw polygons, rectangles, and circles on the map.
""",
    'depends': [
        'web_google_maps','base', 'mail' ,'contacts'
    ],
    'demo': [],
    'images': ['static/description/thumbnails.png'],
    'data': [
        'security/ir.model.access.csv',
        'data/google_maps_library.xml',
        'views/template.xml',
        'views/res_config_settings.xml',
        'views/res_partner.xml',
        'views/res_partner_area.xml',
    ],
    'qweb': ['static/src/xml/drawing.xml'],
        "author": "Mahmudamen",
    "website": "https://mahmudamen.github.io/ten/",
    "installable": True,
    "application": True,
    "auto_install": False,
}
