from jinja2 import FileSystemLoader, Environment


def get_template():
    loader = FileSystemLoader(searchpath="generator/templates/macciato")
    env = Environment(loader=loader)
    return env.get_template('template.j2')


def generate(model):
    style = open('generator/templates/macciato/style.css', 'r').read()

    template = get_template()

    return template.render(model=model, style=style)
