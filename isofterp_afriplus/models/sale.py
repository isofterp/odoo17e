from odoo import models, fields, api, _
from datetime import datetime
import logging

class Sale(models.Model):
    _inherit = 'sale.order'
