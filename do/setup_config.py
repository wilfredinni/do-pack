from string import Template
import os

path_setup = os.path.join(
    os.path.dirname(__file__), 'templates\\template_setup.txt')


def setup_template(
    setup_name,
    setup_version,
    setup_description,
    setup_author,
    setup_author_email,
    setup_url,
):
    with open(path_setup, 'r') as f:
        setup_content = Template(f.read())

    return setup_content.substitute(
        setup_name=setup_name,
        setup_version=setup_version,
        setup_description=setup_description,
        setup_author=setup_author,
        setup_author_email=setup_author_email,
        setup_url=setup_url
    )
