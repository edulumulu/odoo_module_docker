from odoo import models, fields, api

class Trainer(models.Model):
    _name = 'training.trainer'
    _description = 'Trainer'

    # Relación con res.partner (para usar el nombre del formador de la tabla de partners)
    partner_id = fields.Many2one('res.partner', string='Trainer', required=True,
                                 domain="[('id', 'not in', trainer_ids)]")

    # Campo para la especialidad
    speciality = fields.Selection([
        ('data_science', 'Data Science'),
        ('digital_marketing', 'Digital Marketing'),
        ('project_management', 'Project Management'),
        ('software_development', 'Software Development'),
        ('graphic_design', 'Graphic Design'),
    ], string='Speciality', required=True)

    # Otros campos de res.partner que quiero mostrar
    email = fields.Char(related='partner_id.email', string='Email', readonly=True)
    phone = fields.Char(related='partner_id.phone', string='Phone', readonly=True)

    # Nombre del formador (para mostrarlo en la vista)
    name = fields.Char(related='partner_id.name', string='Trainer Name', readonly=True)

    # Campo computado para obtener los IDs de los formadores ya existentes
    trainer_ids = fields.Many2many('res.partner', string="Trainer Partners", compute='_compute_trainer_ids')

    # Para contrastar si el id del colaborador de res.partner ya ha sido seleccionado como formador
    @api.depends('partner_id')
    def _compute_trainer_ids(self):
        for record in self:
            # Aquí obtenemos los 'partner_id' de los formadores existentes
            existing_trainers = self.env['training.trainer'].search([]).mapped('partner_id')
            # Asignamos los 'partner_id' al campo Many2many 'trainer_ids'
            record.trainer_ids = existing_trainers