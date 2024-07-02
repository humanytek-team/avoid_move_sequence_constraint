from odoo import fields, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    avoid_move_sequence_constraint = fields.Boolean()
