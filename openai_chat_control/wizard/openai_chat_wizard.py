import openai

from odoo import fields, models
from odoo.tools import safe_eval


class OpenAIChatWizard(models.TransientModel):
    _name = "openai.chat.wizard"
    _description = "OpenAI Chat Wizard"

    message = fields.Text()

    def button_send(self):
        self.ensure_one()
        message = self.message
        company = self.env.user.company_id
        chat_context = company.openai_chat_context
        api_key = company.openai_api_key

        openai.api_key = api_key

        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[{"role": "user", "content": f"{chat_context}\n{message}"}],
        )
        safe_eval(result)
