from os import path, makedirs
from textx import generator

from .templates.kendall.generator import generate as kendall_generate
from .templates.macciato.generator import generate as macciato_generate
from .templates.stackoverflow.generator import generate as stackoverflow_generate

default_template = 'Kendall'


def generate(model, output_path='../output'):
    if model.template is None:
        model.template = default_template

    resume = None
    if model.template == "Kendall":
        resume = kendall_generate(model)
    elif model.template == "Macciato":
        resume = macciato_generate(model)
    elif model.template == "Stackoverflow":
        resume = stackoverflow_generate(model)
    else:
        raise Exception('Unsupported template type')

    write(resume, output_path)


def write(resume, output_path):
    output_filename = 'resume'

    if not path.exists(output_path):
        makedirs(output_path)

    with open(path.join(output_path, f'{output_filename}.html'), 'w') as f:
        f.write(resume)


@generator('resume', 'HTML')
def resume_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    if output_path:
        resume = generate(model, output_path)
        return resume
    else:
        return generate(model, 'output')
