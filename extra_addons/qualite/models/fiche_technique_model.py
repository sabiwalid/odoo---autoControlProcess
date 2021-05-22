# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Famille(models.Model):
    _name = 'produit.famille'

    name = fields.Char('famille')


class SousFamille(models.Model):
    _name = 'produit.sous_famille'

    name = fields.Char('sous famille')


class ProduitIngredient(models.Model):
    _name = "produit.ingredient"
    _order = "name desc"

    name = fields.Char('Ingeredient', required=True)
    fiche_technique_id = fields.Many2one('produit.fiche_technique', 'Fiche technique')


class DimensionsPoids(models.Model):

    _name = "produit.dimens_poids"

    name = fields.Char('Paramétre', required=True, track_visibility="onchange")
    valeur_cible = fields.Char('Valeur', required=True, track_visibility="onchange")
    valeur_min = fields.Float('Valeur Min', required=True, track_visibility="onchange")
    valeur_max = fields.Float('Valeur Max', required=True, track_visibility="onchange")
    fiche_technique_id = fields.Many2one('produit.fiche_technique', 'Fiche technique')


class Allergenes(models.Model):
    _name = "produit.allergenes"

    name = fields.Char('Allergènes majeurs', required=True, track_visibility="onchange")
    valeur = fields.Char('P/A/CC', required=True, track_visibility="onchange")
    fiche_technique_id = fields.Many2one('produit.fiche_technique', 'Fiche technique')


class CaractMicrobio(models.Model):
    _name = "produit.caract_microbio"

    name = fields.Char('Références', required=True, track_visibility="onchange")
    caract_microbio = fields.Char('Caractéristiques microbiologiques', required=True, track_visibility="onchange")
    valeur = fields.Char('Valeurs', required=True, track_visibility="onchange")
    fiche_technique_id = fields.Many2one('produit.fiche_technique', 'Fiche technique')


class FicheModification(models.Model):
    _name = "produit.fiche_modif"

    name = fields.Char('Description modification', required=True, track_visibility="onchange")
    date = fields.Date('Date de modification', required=True, track_visibility="onchange")
    type = fields.Selection([
        ('type_01', 'Process'),
        ('type_02', 'Recette'),
    ], string='Type de modification', index=True, track_visibility='onchange')
    motif = fields.Char('Motif de modification', required=True, track_visibility="onchange")
    nature = fields.Char('Nautre de modification', required=True, track_visibility="onchange")
    version = fields.Integer('Version', required=True, track_visibility="onchange")
    date_lancement = fields.Date('Date de lancement', required=True, track_visibility="onchange")
    fiche_technique_id = fields.Many2one('produit.fiche_technique', 'Fiche technique')


class FicheTechnique(models.Model):
    _name = 'qualite.fiche_technique'
    _description = 'qualite.qualite'

    name = fields.Many2one('product.product',string='Article')
    famille_ids = fields.Many2one('produit.famille',string='famille')
    sous_famille_ids = fields.Many2one('produit.sous_famille',string='sous famille')
    labo = fields.Selection([
        ('boulangerie', 'Boulangerie'),
        ('viennoiserie', 'Viennoiserie'),
        ('patisserie', 'Pâtisserie'),
        ('cuisine', 'Cuisine'),
    ], string='Labo')
    uom_id = fields.Many2one('uom.uom', 'Unité de mesure')
    echantillonnage = fields.Float('Echantillonnage')
    produit_code = fields.Char(related='name.default_code', store=True,string='code article')
    ingredient_ids = fields.One2many('produit.ingredient', 'fiche_technique_id', 'Ingredient')
    caract_microbio = fields.One2many('produit.caract_microbio', 'fiche_technique_id',
                                      'Caractéristiques microbiologiques')
    allergenes_ids = fields.One2many('produit.allergenes', 'fiche_technique_id', 'Allergènes')
    dimensions_poids_ids = fields.One2many('produit.dimens_poids', 'fiche_technique_id', 'Dimensions et Poids')
    conseil = fields.Text('Conseil d’utilisation')
    conditionnement = fields.Text('Conditionnement')
    duree_vie = fields.Text('Durée de vie et conditions de conservation')
    usage = fields.Text('Usage prévu')
    md_psf = fields.Text('Méthode de distribution: Produit Semi Fini')
    ml_pf = fields.Text('Méthode de livraison: Produit Fini')
    consommateur = fields.Text('Consommateur')
    condition_manipulation = fields.Text('Conditions de manipulation')
    fiche_modif_ids = fields.One2many('produit.fiche_modif', 'fiche_technique_id', 'Gestion des modifications')








