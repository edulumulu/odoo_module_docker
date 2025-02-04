from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_trainer = fields.Boolean(
        string='Is Trainer',
        compute='_compute_is_trainer',
        store=False  # No almacenar en la base de datos, calcular dinámicamente
    )

    trainer_speciality = fields.Char(
        string='Trainer Speciality',
        compute='_compute_trainer_speciality',
        store=False
    )


       
    # Determinar si un partner está registrado como formador en el modelo 'training.trainer'. (true o false)
    @api.depends()
    def _compute_is_trainer(self):
        # Obtener el modelo training.trainer
        TrainerModel = self.env['training.trainer']

        for partner in self:
            # Verifico si este partner aparece en la tabla training.trainer como formador
            is_trainer = TrainerModel.search_count([('partner_id', '=', partner.id)]) > 0
            partner.is_trainer = is_trainer

    @api.depends('is_trainer')
    def _compute_trainer_speciality(self):
        for partner in self:
            if partner.is_trainer:
                # Busco la especialidad del formador en el modelo 'training.trainer'
                trainer = self.env['training.trainer'].search([('partner_id', '=', partner.id)], limit=1)
                partner.trainer_speciality = trainer.speciality if trainer else ''
            else:
                partner.trainer_speciality = ''  # Si no es formador, dejar vacío
