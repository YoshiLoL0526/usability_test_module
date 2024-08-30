from odoo import models, fields, api
from odoo.exceptions import ValidationError


class UsabilityPrinciples(models.Model):
    _name = 'usability.principles'
    _description = 'Principios de Usabilidad de Jakob Nielsen'

    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')

    @api.constrains('description')
    def _check_weird_chars(self):
        for record in self:
            for char in record.description:
                if 33 <= ord(char) <= 47 or 58 <= ord(char) <= 64 or 91 <= ord(char) <= 96 or 123 <= ord(char) <= 126:
                # if char in '_+=-_/?{}[]()*&^%$#@!~`':
                    raise ValidationError("La descripción no puede contener caracteres extraños.")

    @api.constrains('name')
    def _check_name_length(self):
        for record in self:
            if len(record.name) < 3:
                raise ValidationError("El nombre debe tener al menos 3 caracteres.")
