# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2001-2014 Micronaet SRL (<http://www.micronaet.it>).
#    Copyright (C) 2014 Agile Business Group sagl
#    (<http://www.agilebg.com>)
#    Copyright (C) 2014 Didotech SRL
#    (<http://www.didotech.com>)
#    Copyright (C) 2015 SimplERP Srl
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Payment terms - Commercial month",
    "version": "4.0.0.1",
    "author": "SimplERP Srl",
    "website": "http://www.simplerp.it",
    "category": "Account / Payments",
    "description": """

    """,
    "depends": [
        "account",
    ],
    "demo": [],
    "data": [
        "views/payment_view.xml",
    ],
    "test": [
        "test/invoice_emission.yml",
    ],
    "active": False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
