from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    openai_api_key = fields.Char(related="company_id.openai_api_key", readonly=False)
    openai_chat_context = fields.Text(
        related="company_id.openai_chat_context", readonly=False
    )

    def action_open_openai_chat_wizard(self):
        return {
            "res_model": "openai.chat.wizard",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "target": "new",
        }
