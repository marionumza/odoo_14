# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Nikhil krishnan(odoo@cybrosys.com)
#    you can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Make MRP orders from POS',
    'version': '14.0.1.0.3',
    'summary': """Launch Automatic MRP Orders After Selling Through POS.""",
    'description': """Launch automatic MRP orders after selling through POS""",
    'author': 'Anhjean',
    'company': 'Bean Bakery',
    'website': 'https://www.beanbakery.vn',
    'category': 'Point of Sale',
    'depends': ['point_of_sale', 'mrp', 'stock'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/pos_template.xml',
    ],
    'qweb':[ 'views/custom.xml',
             'views/datepopup.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
