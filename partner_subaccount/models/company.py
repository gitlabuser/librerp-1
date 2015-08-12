# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 SimplERP srl (<http://www.simplerp.it>).
#    Copyright (c) 2013-2014 Didotech SRL (info at didotech.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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

from openerp import models, fields


class res_company(models.Model):
    _inherit = 'res.company'
    enable_partner_subaccount = fields.Boolean(
        string='Enable Partner Subaccount', default=True)


class account_config_settings(models.TransientModel):
    _inherit = 'account.config.settings'
    enable_partner_subaccount = fields.Boolean(
        string="Enable Partner Subaccount",
        related='company_id.enable_partner_subaccount')
