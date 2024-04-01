from odoo import models, fields, api
from odoo.exceptions import ValidationError


class UsabilityTest(models.Model):
    _name = 'usability.test'
    _description = 'Usability Test'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    date = fields.Date(string='Fecha', required=True)

    @api.constrains('date')
    def _check_future_date(self):
        for rec in self:
            if rec.date and rec.date > fields.date.today():
                raise ValidationError('La fecha no puede ser en el futuro.')

    principles = fields.One2many('usability.principles', 'tests', string='Principios de Usabilidad')
    rating = fields.Selection([
        ('excellent', 'Excelente'),
        ('acceptable', 'Aceptable'),
        ('sufficient', 'Suficiente'),
        ('deficient', 'Deficiente')
    ], string='Calificación', compute='_compute_rating', store=True)
    specialists = fields.Many2one('res.partner', string='Especialista', required=True)
    recommendations = fields.Text(string='Recomendaciones')

    @api.depends('principles.rating')
    def _compute_rating(self):
        for test in self:
            total_principles = len(test.principles)
            good_count = len([principle.rating for principle in test.principles if principle.rating == 'good'])
            
            if good_count / total_principles > 0.9:  # 90% de principios bien
                test.rating = 'excellent'
            elif 0.8 <= good_count / total_principles <= 0.9:  # entre 80% y 90% de principios bien
                test.rating = 'acceptable'
            elif 0.7 <= good_count / total_principles < 0.8:  # entre 70% y 80% de principios bien
                test.rating = 'sufficient'
            elif 0.2 <= (total_principles - good_count) / total_principles <= 0.3:  # entre 20% y 30% de principios mal o regular
                test.rating = 'deficient'
            else:
                test.rating = 'deficient'
