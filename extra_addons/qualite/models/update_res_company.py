
import os
import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
import time


class Company(models.Model):
    _inherit = "res.company"

    codification_audit_pn = fields.Char('Codification audit place nette', track_visibility='onchange', default='QM-APN')
    version_audit_pn = fields.Char('Version audit place nette', track_visibility='onchange', default='3')
    page_audit_pn = fields.Char('Page audit place nette', track_visibility='onchange', default='1 sur 4')

    codification_audit = fields.Char('Codification audit hygiène', track_visibility='onchange', default='QU-PR2-EN1')
    version_audit = fields.Char('Version audit hygiène', track_visibility='onchange', default='2')
    page_audit = fields.Char('Page audit hygiène', track_visibility='onchange', default='1 sur 1')

    codification_document = fields.Char('Codification document', track_visibility='onchange', default='QU-PR6-TB1')
    version_document = fields.Char('Version document', track_visibility='onchange', default='2')
    page_document = fields.Char('Page document', track_visibility='onchange', default='1 sur 3')

    codification_enregistrement = fields.Char('Codification enregistrement', track_visibility='onchange',
                                              default='QU-PR6-TB2')
    version_enregistrement = fields.Char('Version enregistrement', track_visibility='onchange', default='2')
    page_enregistrement = fields.Char('Page enregistrement', track_visibility='onchange', default='1 sur 5')

    codification_acc = fields.Char('Codification Autocontrole Cuisine', track_visibility='onchange',
                                   default='PR-EN 010')
    version_acc = fields.Char('Version Autocontrole Cuisine', track_visibility='onchange', default='1')
    page_acc = fields.Char('Page Autocontrole Cuisine', track_visibility='onchange', default='1 sur 1')

    codification_acb = fields.Char('Codification Autocontrole Boulangerie', track_visibility='onchange',
                                   default='PR-EN 010')
    version_acb = fields.Char('Version Autocontrole Boulangerie', track_visibility='onchange', default='1')
    page_acb = fields.Char('Page Autocontrole Boulangerie', track_visibility='onchange', default='1 sur 1')

    codification_acv = fields.Char('Codification Autocontrole Viennoiserie', track_visibility='onchange',
                                   default='PR-EN 03')
    version_acv = fields.Char('Version Autocontrole Viennoiserie', track_visibility='onchange', default='2')
    page_acv = fields.Char('Page Autocontrole Viennoiserie', track_visibility='onchange', default='1 sur 1')

    codification_acp = fields.Char('Codification Autocontrole Pâtisserie', track_visibility='onchange',
                                   default='PR-EN 03')
    version_acp = fields.Char('Version Autocontrole Pâtisserie', track_visibility='onchange', default='2')
    page_acp = fields.Char('Page Autocontrole Pâtisserie', track_visibility='onchange', default='1 sur 1')

    codification_alert = fields.Char('Codification Non Conformité', track_visibility='onchange', default='QU-PR8-EN1')
    version_alert = fields.Char('Version Non Conformité', track_visibility='onchange', default='2')
    page_alert = fields.Char('Page audit Non Conformité', track_visibility='onchange', default='1 sur 1')

    codification_alert_r = fields.Char('Codification Réclamation', track_visibility='onchange', default='QU-PR8-EN3')
    version_alert_r = fields.Char('Version Réclamation', track_visibility='onchange', default='2')
    page_alert_r = fields.Char('Page audit Réclamation', track_visibility='onchange', default='1 sur 1')

    codification_ft = fields.Char('Codification Fiche Technique', track_visibility='onchange', default='QU-EN19')
    version_ft = fields.Char('Version Fiche Technique', track_visibility='onchange', default='1')
    page_ft = fields.Char('Page audit Fiche Technique', track_visibility='onchange', default='1 sur 1')

    # Pâtisserie

    frequence_creme = fields.Char('Fréquence Crèmes', track_visibility='onchange', default='Chaque 1h')
    frequence_petrissagemacarons = fields.Char('Fréquence Pétrissage Macarons', track_visibility='onchange',
                                               default='Chaque 1h')
    frequence_petrissagepateachoux = fields.Char('Fréquence Pétrissage Pâte à choux', track_visibility='onchange',
                                                 default='Chaque 1h')
    frequence_cuissonpateachoux = fields.Char('Fréquence Cuisson Pâte à choux', track_visibility='onchange',
                                              default='Chaque 1h')
    frequence_cake = fields.Char('Fréquence Cake', track_visibility='onchange', default='Chaque 1h')

    # Cuisine

    frequence_c_cuisson = fields.Char('Fréquence Cuisson', track_visibility='onchange', default='Chaque Chariot')
    frequence_c_refroidissement = fields.Char('Fréquence Refroidissement', track_visibility='onchange',
                                              default='Chaque Chariot')
    frequence_c_surgelation = fields.Char('Fréquence Surgélation', track_visibility='onchange',
                                          default='Chaque Chariot')

    # Boulangerie

    frequence_petrissage = fields.Char('Fréquence Pétrissage', track_visibility='onchange', default='Chaque Pétrin')
    frequence_pousse = fields.Char('Fréquence Pousse cuisson', track_visibility='onchange', default='Chaque Chariot')
    frequence_refroidissement = fields.Char('Fréquence Refroidissement', track_visibility='onchange',
                                            default='Chaque Chariot')
    frequence_surgelation = fields.Char('Fréquence Surgélation', track_visibility='onchange', default='Chaque Chariot')

    # Viennoiserie

    frequence_petris = fields.Char('Fréquence Pétrissage', track_visibility='onchange', default='Chaque 1h30')
    frequence_repos = fields.Char('Fréquence Repos', track_visibility='onchange', default='Chaque 1h')
    frequence_pous = fields.Char('Fréquence Pousse', track_visibility='onchange', default='Chaque 1h30')
    frequence_beurre = fields.Char('Fréquence T° Beurre', track_visibility='onchange', default='Chaque 1h')
    frequence_poids = fields.Char('Fréquence Poids', track_visibility='onchange', default='Chaque 15min')

    userR_id = fields.Many2one('res.users', 'Responsable', track_visibility='onchange')
    user1_id = fields.Many2one('res.users', 'Equipe Qualité 1', track_visibility='onchange')
    user2_id = fields.Many2one('res.users', 'Equipe Qualité 2', track_visibility='onchange')
    user3_id = fields.Many2one('res.users', 'Equipe Qualité 3', track_visibility='onchange')
    userR_patisserie_id = fields.Many2one('res.users', 'Responsable patisserie', track_visibility='onchange')
    userR_viennoiserie_id = fields.Many2one('res.users', 'Responsable viennoiserie', track_visibility='onchange')
    userR_boulangerie_id = fields.Many2one('res.users', 'Responsable boulangerie', track_visibility='onchange')
    userR_cuisine_id = fields.Many2one('res.users', 'Responsable cuisine', track_visibility='onchange')