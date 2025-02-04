from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta


class Session(models.Model):
    _name = 'training.session'
    _description = 'Session'

    name = fields.Char(string='Session Name', size=100, required=True)
    course_id = fields.Many2one('training.course', string='Course', required=True)
    
    session_date = fields.Datetime(string='Session Date', required=True)
    
    stop_datetime = fields.Datetime(string="Stop Datetime", compute='_compute_stop_datetime', store=True)

    trainer_id = fields.Many2one('training.trainer', string='Trainer', required=True)
    participant_ids = fields.Many2many('hr.employee', string='Participants')
    #location = fields.Char(string='Location', size=100)
    location = fields.Selection(
        [('madrid', 'Madrid'), ('barcelona', 'Barcelona')],
        string='Location', default='madrid'
    )
    state = fields.Selection(
        [('planned', 'Planned'), ('in_progress', 'In Progress'), ('completed', 'Completed')],
        string='Status', default='planned'
    )
    duration = fields.Float(string='Duration', related='course_id.hours_per_session', store=True, readonly=True)
    display_title = fields.Char(
        string="Display Title",
        compute="_compute_display_title",
        store=True,
        help="Custom title for calendar view showing session name and course name."
    )

    # Para asignar los participantes del curso al campo de la sesión de entrenamiento
    @api.onchange('course_id')
    def _onchange_course_id(self):
        if self.course_id:
            self.participant_ids = self.course_id.participant_ids
    
    #La utilizo para calcular la fecha de finalización teniendo en cuenta la de empiece y 
    # la duración por defecto de las sesiones de este curso
    @api.depends('session_date', 'duration')
    def _compute_stop_datetime(self):
        """Calculate stop_datetime by adding duration to session_date."""
        for session in self:
            if session.session_date and session.duration:
                session.stop_datetime = session.session_date + timedelta(hours=session.duration)
            else:
                session.stop_datetime = False
    
    #Por si quiero tratar de concatenar el nombre sesion y el curso
    #@api.depends('name', 'course_id.name')
    #def _compute_display_title(self):
       # for session in self:
           # course_name = session.course_id.name if session.course_id else "N/A"
           # session.display_title = f"{session.name} ({course_name})"
    
     # Para asegurar de que el total de la duracion de las sesiones ya existentes no esceden la duración del curso
     # Añadir añade una restricción para validar la duración total de las sesiones.
    @api.constrains('course_id', 'duration')
    def _check_course_total_duration(self):
        """
        Ensure that the total duration of all sessions for a course does not exceed the course's duration.
        """
        for session in self:
            if session.course_id:
                #Calculo la duración total de las sesiones asociadas al curso, excluyendo la actual.
                total_duration = sum(
                    self.env['training.session'].search([
                        ('course_id', '=', session.course_id.id),
                        ('id', '!=', session.id)  # Excluir la sesión actual del cálculo
                    ]).mapped('duration')
                ) + session.duration

                #Valido si la duración total supera la duración del curso.
                if total_duration > session.course_id.duration:
                    raise exceptions.ValidationError(
                        f"Cannot add session '{session.name}'. The total duration of sessions for the course "
                        f"'{session.course_id.name}' exceeds the course duration of {session.course_id.duration} hours."
                    )
    
    


