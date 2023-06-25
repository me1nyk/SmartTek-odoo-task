from odoo import models, fields


class Demo(models.Model):
    _name = 'demo.demo'
    _description = 'Demo Object'

    name = fields.Char(string='Name', required=True)
