from odoo import models, fields, api

class Course(models.Model):
    _name = 'training.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', size=65 ,required=True, translate=True)
    description = fields.Char(string='Session description', size=300, required=True)
    trainer_id = fields.Many2one('training.trainer', string='Responsible', required=True)
    participant_ids = fields.Many2many(
        'hr.employee', string='Participants'
    )
    duration = fields.Float(string='Duration (hours)', required=True)
    hours_per_session = fields.Float(string='Hours per Session', required=True)
    sessions = fields.Integer(
        string='Number of Sessions', compute='_compute_sessions', store=True
    )  
    state = fields.Selection(
        [('planned', 'Planned'), ('in_progress', 'In Progress'), ('completed', 'Completed')],
        string='Status', default='planned'
    )
    session_ids = fields.One2many(
        'training.session', 'course_id', string='Sessions'
    )

    # Función para calcular el número de sesiones necesarias en función de la duración total y horas por sesión
    @api.depends('duration', 'hours_per_session')
    def _compute_sessions(self):
        for record in self:
            if record.hours_per_session > 0:
            # Calculo el número de sesiones dividiendo la duración total por las horas por sesión

                record.sessions = record.duration // record.hours_per_session
            else:
                # Si las horas por sesión no están definidas, el número de sesiones será 0
                record.sessions = 0

   
                