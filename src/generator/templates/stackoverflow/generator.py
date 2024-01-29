from jinja2 import FileSystemLoader, Environment


def get_template():
    loader = FileSystemLoader(searchpath="generator/templates/stackoverflow")
    env = Environment(loader=loader)
    return env.get_template('template.j2')


def generate(model):
    style = open('generator/templates/stackoverflow/style.css', 'r').read()

    template = get_template()

    return template.render(model=model, style=style)
