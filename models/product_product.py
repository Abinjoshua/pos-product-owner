# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.product'

    product_owner_id = fields.Many2one('res.partner', string="Owner")

    @api.model
    def _load_pos_data_fields(self, config_id):
        """Return fields to be loaded into the POS."""
        data = super()._load_pos_data_fields(config_id)
        data.append('product_owner_id')
        return data

