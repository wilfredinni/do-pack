from string import Template
import click
import sys
import os

path_template = os.path.join(
    os.path.dirname(__file__), 'templates')


def load_template(template_file, path=path_template):
    try:
        with open(os.path.join(path, template_file), 'r') as f:
            loaded_template = Template(f.read())
    except FileNotFoundError:
        click.echo('fileNotFoundError: {} Not Found. Aborted!'
                   .format(path))
        sys.exit(1)
    return loaded_template


def setup_template(setup_name,
                   setup_version,
                   setup_description,
                   setup_author,
                   setup_author_email,
                   setup_url,
                   path=path_template,
                   ):

    setup_content = load_template('template_setup.txt')

    return setup_content.substitute(setup_name=setup_name,
                                    setup_version=setup_version,
                                    setup_description=setup_description,
                                    setup_author=setup_author,
                                    setup_author_email=setup_author_email,
                                    setup_url=setup_url
                                    )


def authors_template(project_name,
                     setup_author,
                     setup_author_email,
                     path=path_template):

    authors_content = load_template('template_authors.txt')

    return authors_content.substitute(project_name=project_name,
                                      setup_author=setup_author,
                                      setup_author_email=setup_author_email
                                      )


if __name__ == '__main__':
    author_test = authors_template('project', 'carlos', 'carlos@gmail.com')
    click.echo(author_test)
