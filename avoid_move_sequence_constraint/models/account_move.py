from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _must_check_constrains_date_sequence(self):
        if self.journal_id.avoid_move_sequence_constraint:
            return False
        return super()._must_check_constrains_date_sequence()
