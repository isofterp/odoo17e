from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    x_sap_code = fields.Char(related="product_id.x_sap_code")
    x_hs_code = fields.Char(related="product_id.x_hs_code")
    x_gross_weight = fields.Float(related="product_id.x_gross_weight")

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    x_sap_code = fields.Char(related="product_id.x_sap_code")
    x_hs_code = fields.Char(related="product_id.x_hs_code")
    x_gross_weight = fields.Float(related="product_id.x_gross_weight")