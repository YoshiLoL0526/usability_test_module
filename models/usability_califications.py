from odoo import models, fields


class UsabilityCalifications(models.Model):
    _name = 'usability.califications'
    _description = 'Calificaciones de Principios de Usabilidad'
    
    test_id = fields.Many2one('usability.test', string='Prueba')
    principle_id = fields.Many2one('usability.principles', string='Principio')
    calification = fields.Selection([
        ('good', 'Bien'),
        ('bad', 'Mal'),
        ('regular', 'Regular')
    ], string='Calificación', required=True)

    _sql_constraints = [
        ('unique_principle_test', 'UNIQUE(test_id, principle_id)', '¡Error! El mismo principio de usabilidad no puede ser asignado más de una vez a la misma prueba.')
    ]
