from string import Template
import click
import sys
import os

path_template = os.path.join(
    os.path.dirname(__file__), 'templates')


def load_template(template_file, path=path_template):
    try:
        with open(os.path.join(path, template_file), 'r') as f:
            return Template(f.read())
    except FileNotFoundError:
        click.echo('fileNotFoundError: {} Not Found. Aborted!'
                   .format(path))
        sys.exit(1)


def setup_template(
        setup_name,
        setup_version,
        setup_description,
        setup_author,
        setup_author_email,
        setup_url
):
    setup_content = load_template('template_setup.txt')

    return setup_content.substitute(
        setup_name=setup_name,
        setup_version=setup_version,
        setup_description=setup_description,
        setup_author=setup_author,
        setup_author_email=setup_author_email,
        setup_url=setup_url
    )


def authors_template(
        project_name,
        setup_author,
        setup_author_email):

    authors_content = load_template('template_authors.txt')

    return authors_content.substitute(
        project_name=project_name,
        setup_author=setup_author,
        setup_author_email=setup_author_email
    )


def gitignore_template():
    file_i = 'template_gitignore.txt'
    try:
        with open(os.path.join(path_template, file_i), 'r') as git_content:
            return git_content.read()
    except FileNotFoundError:
        click.echo('fileNotFoundError: {} Not Found. Aborted!'
                   .format(file_i))
        sys.exit(1)


if __name__ == '__main__':
    a = gitignore_template()
    print(a)
