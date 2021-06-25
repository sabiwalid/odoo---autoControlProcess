import logging
from odoo import models, fields, api
from datetime import datetime, timedelta

class AutoControleCuisine(models.Model):
    _name = "autocontrole.cuisine"
    _inherit = ['mail.thread']
    _description = "Autocontrole cuisine"

    @api.model
    def _get_default_code(self):
        return self.env.user.company_id_codification_acc

    @api.model
    def _get_default_version(self):
        return self.env.user.company_id.version_acc

    @api.model
    def _get_default_page(self):
        return self.env.user.company_id.page_acc

    @api.model
    def _get_frequence_c_cuisson(self):
        return self.env.user.company_id.frequence_c_cuisson

    @api.model
    def _get_frequence_c_refroidissement(self):
        return self.env.user.company_id.frequence_c_refroidissement

    @api.model
    def _get_frequence_c_surgelation(self):
        return self.env.user.company_id.frequence_c_surgelation

    name = fields.Char('Produit concerné', readonly=True, default = "Tous les produits")
    code = fields.Char('Code', required=True, default=_get_default_code, readonly=True)
    version = fields.Char('Version', required=True, default=_get_default_version, readonly=True)
    page = fields.Char('Page', required=True, default=_get_default_page, readonly=True)
    maj = fields.Date('Date', track_visibility="onchange")
    active = fields.Boolean(
        'Active', default=True,
        help="If unchecked, it will allow you to hide the product without removing it.")

    user_id_c_cuisson = fields.Many2one('res.users', 'Responsable Cuisson', required=True, track_visibility='onchange', default=lambda self: self.env.user)
    frequence_c_cuisson = fields.Char('Fréquence Cuisson', default=_get_frequence_c_cuisson, readonly=True)

    user_id_c_refroidissement = fields.Many2one('res.users', 'Responsable Refroidissement', required=True,
                                                track_visibility='onchange', default=lambda self: self.env.user)
    frequence_c_refroidissement = fields.Char('Fréquence Refroidissement', default=_get_frequence_c_refroidissement,
                                              readonly=True)

    user_id_c_surgelation = fields.Many2one('res.users', 'Responsable Surgélation', required=True,
                                            track_visibility='onchange', default=lambda self: self.env.user)
    frequence_c_surgelation = fields.Char('Fréquence Surgélation', default=_get_frequence_c_surgelation, readonly=True)

    cuisson_ids = fields.One2many('autocontrole.ccuisson', 'acc_id', 'Cuisson')
    refroidissement_ids = fields.One2many('autocontrole.crefroidissement', 'acc_id', 'Refroidissement')
    surgelation_ids = fields.One2many('autocontrole.csurgelation', 'acc_id', 'Surgelation')

    class AutoControleCcuisson(models.Model):
        _name = "autocontrole.ccuisson"
        _inherit = ['mail.thread']




