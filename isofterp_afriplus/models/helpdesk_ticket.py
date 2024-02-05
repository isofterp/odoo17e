from odoo import fields, models, api, _
import odoo.addons.decimal_precision as dp
from odoo.tools import float_is_zero, float_compare
import json
import logging
import re
_logger = logging.getLogger(__name__)

class HelpdeskTicket(models.Model):

    _inherit = 'helpdesk.ticket'

    x_technician = fields.Many2one('res.partner', string='Technician', tracking=True, index=True)
