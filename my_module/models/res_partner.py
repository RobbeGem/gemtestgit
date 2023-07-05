from odoo import models,fields,api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    my_field = fields.Char(string='My Field')