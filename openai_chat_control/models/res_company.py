from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    openai_api_key = fields.Char()

    openai_chat_context = fields.Text(
        default="""
Write a Odoo server action response.
- It returns a server action in odoo
- It returns his response in python
- do not use functions just code to evaluate
- I only need the script body.
Don’t add any explanation.
The task is described as follows:
        """
    )
