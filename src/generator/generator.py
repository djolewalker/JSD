from os import path, makedirs
from textx import generator

from src.generator.templates.kendall.generator import generate as kendall_generate
from src.generator.templates.macciato.generator import generate as macciato_generate
from src.generator.templates.stackoverflow.generator import generate as stackoverflow_generate

default_template = 'Kendall'


def generate(model):
    if model.template is None:
        model.template = default_template

    if model.template == "Kendall":
        return kendall_generate(model)
    elif model.template == "Macciato":
        return macciato_generate(model)
    elif model.template == "Stackoverflow":
        return stackoverflow_generate(model)
    else:
        raise Exception('Unsupported template type')


def write(resume, output_path='../output_dir'):
    output_filename = 'person_one'

    if not path.exists(output_path):
        makedirs(output_path)

    with open(path.join(output_path, f'{output_filename}.html'), 'w') as f:
        f.write(resume)


@generator('resume', 'HTML')
def resume_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    if output_path:
        resume = generate(model)
        write(resume, output_path)
        return resume
    else:
        return generate(model)
