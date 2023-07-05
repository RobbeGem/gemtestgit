from odoo import models,fields,api

class MyModel(models.Model):
    _name = 'my.model'
    _description = 'my model description'

    my_field = fields.Char(string="My field")
