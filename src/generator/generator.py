from src.generator.templates.kendall.generator import generate as kendall_generate
from src.generator.templates.macciato.generator import generate as macciato_generate

default_template = 'Kendall'


def generate(model):
    if model.template is None:
        model.template = default_template

    if model.template == "Kendall":
        return kendall_generate(model)
    if model.template == "Macciato":
        return macciato_generate(model)
    else:
        raise Exception('Unsupported template type')
