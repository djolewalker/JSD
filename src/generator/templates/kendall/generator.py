from jinja2 import FileSystemLoader, Environment
from importlib.resources import files


def set_profile_icons(model):
    for profile in model.personal_info.profiles:
        network = profile.network.lower()
        if network in ('google-plus', 'googleplus'):
            profile.icon_class = 'fab fa-google-plus'
        elif network in ('flickr', 'flicker'):
            profile.icon_class = 'fab fa-flickr'
        elif network in ('dribbble', 'dribble'):
            profile.icon_class = 'fab fa-dribbble'
        elif network in ('codepen', 'soundcloud', 'reddit', 'gitlab'):
            profile.icon_class = f'fab fa-{network}'
        elif network in ('tumblr', 'tumbler'):
            profile.icon_class = 'fab fa-tumblr'
        elif network in ('stack-overflow', 'stackoverflow'):
            profile.icon_class = 'fab fa-stack-overflow'
        elif network in ('blog', 'rss'):
            profile.icon_class = 'fas fa-rss'
        elif network == 'keybase':
            profile.icon_class = 'fas fa-key'
        else:
            profile.icon_class = f'fab fa-{network}'


def get_template():
    loader = FileSystemLoader(searchpath=str(files('generator').joinpath('templates/kendall')))
    env = Environment(loader=loader)
    return env.get_template('template.j2')


def generate(model):
    set_profile_icons(model)

    style = files('generator').joinpath('templates/kendall/style.css').read_text()
    print_style = files('generator').joinpath('templates/kendall/print.css').read_text()

    template = get_template()

    return template.render(model=model, style=style, print_style=print_style)
