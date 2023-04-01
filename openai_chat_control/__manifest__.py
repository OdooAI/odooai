{
    "name": "OpenAI Chat Control",
    "version": "16.0.1.0.0",
    "category": "OdooAI",
    "author": "OdooAI",
    "website": "https://github.com/OdooAI/odooai",
    "license": "AGPL-3",
    "depends": ["base_setup"],
    "external_dependencies": {"python": ["openai"]},
    "data": [
        "views/res_config_settings_views.xml",
        "security/ir.model.access.csv",
        "wizard/openai_chat_wizard_views.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
