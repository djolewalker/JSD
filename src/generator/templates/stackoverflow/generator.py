from jinja2 import FileSystemLoader, Environment
from importlib.resources import files


def get_template():
    loader = FileSystemLoader(searchpath=str(files('generator').joinpath('templates/stackoverflow')))
    env = Environment(loader=loader)
    return env.get_template('template.j2')


def generate(model):
    style = files('generator').joinpath('templates/stackoverflow/style.css').read_text()

    template = get_template()

    return template.render(model=model, style=style)
