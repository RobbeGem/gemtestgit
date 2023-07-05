from odoo import models, fields


class MyWizard(models.TransientModel):
    _name = 'my.wizard'
    _description = 'My Wizard'

    my_field = fields.Char(string='My Field')
