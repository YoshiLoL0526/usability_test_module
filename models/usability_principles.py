from odoo import models, fields, api
from odoo.exceptions import ValidationError


class UsabilityPrinciples(models.Model):
    _name = 'usability.principles'
    _description = 'Principios de Usabilidad de Jakob Nielsen'

    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')

    @api.constrains('name')
    def _check_name_length(self):
        for record in self:
            if len(record.name) < 3:
                raise ValidationError("El nombre debe tener al menos 3 caracteres.")
