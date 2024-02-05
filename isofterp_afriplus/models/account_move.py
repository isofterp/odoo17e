from odoo import fields, models, api, _
import odoo.addons.decimal_precision as dp
from odoo.tools import float_is_zero, float_compare
import json
import logging
import re
_logger = logging.getLogger(__name__)

class account_move_line(models.Model):

    _inherit = 'account.move.line'

    x_sap_code = fields.Char(related="product_id.x_sap_code")
