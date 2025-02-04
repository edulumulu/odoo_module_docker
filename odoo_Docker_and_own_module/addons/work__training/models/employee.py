from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'

    # Cursos de formación en los que el empleado está inscrito
    training_courses_ids = fields.Many2many(
        'training.course', 
        string='Training Courses', 
        compute='_compute_training_courses', 
        store=False
    )

    # Sesiones de formación asociadas a los cursos del empleado
    training_sessions_ids = fields.Many2many(
        'training.session',
        string='Training Sessions',
        compute='_compute_training_sessions',
        store=False
    )

        # Computo los cursos de formación en los que el empleado está inscrito

    def _compute_training_courses(self):
        for employee in self:
            # Filtramos los cursos donde el empleado está como participante
            employee.training_courses_ids = self.env['training.course'].search([
                ('participant_ids', 'in', employee.id)
            ])


    # Computo las sesiones de formación asociadas a los cursos en los que el empleado está inscrito
    def _compute_training_sessions(self):
        for employee in self:
        # Buscar todos los cursos en los que el empleado está inscrito
            courses = self.env['training.course'].search([('participant_ids', 'in', employee.id)])
        # Obtener todas las sesiones asociadas a esos cursos
            sessions = self.env['training.session'].search([('course_id', 'in', courses.ids)])
        # Asignar las sesiones al campo correspondiente
            employee.training_sessions_ids = sessions
