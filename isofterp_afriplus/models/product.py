# Copyright 2015-2016 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models
from odoo.addons import decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_sap_code = fields.Char(string="SAP Code")
    x_hs_code = fields.Char(string="HS Code")
    x_gross_weight = fields.Float(
        'Gross weight',
        digits='Stock Weight',
        help="gross weight of the product"
    )
