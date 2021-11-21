# -*- coding: utf-8 -*-
# Part of Nuca Erp create by Mahmudamen. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class respartnerarea(models.Model):
    _name = 'res.partner.area'
    _inherit = ['mail.thread', 'google_maps.drawing.shape.mixin']
    _description = 'Partner Area'

    partner_id = fields.Many2one(
        'res.partner', ondelete='cascade' )


class ResPartners(models.Model):
    _inherit = ['res.partner']
    _description = 'shape_line_ids'

    shape_line_ids = fields.One2many('res.partner.area', 'partner_id', string='Area')
    is_entity_company = fields.Boolean(string='entity company id')