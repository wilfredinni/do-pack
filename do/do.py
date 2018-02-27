import click
import os
import do.skeleton
import do.licenses
import do.template_config

# TODO: create the file for the config and the function that save it.
# TODO: use the seved variables to replace the setup options.
# TODO: implement templates for create() (empty structure).


@click.group()
def main():
    """
    Simple command-line tool to create python packages.
    """
    pass


@main.command()
@click.option('--template', '-t',
              help='Lets you choose a Template.')
@click.argument('project-name')
def create(project_name, template):
    """
    creates an empty structure for your package.
    """
    click.echo('\ndo will create your {} Project Structure.'
               .format(project_name))
    if click.confirm('Do you want to continue?'):
        do.skeleton.make_skeleton(project_name)
        click.echo('{} was created on {}'
                   .format(project_name, os.path.join(os.getcwd())))


@main.command()
def assistant():
    """
    A step by step assistant.
    """
    clear()
    # click.echo('do will now start the assistant.')
    if click.confirm('>> do will now start the assistant.' +
                     ' Do you want to continue?'):

        project_name = click.prompt('\nproject name')
        setup_version = click.prompt('version')
        setup_description = click.prompt('description')
        setup_author = click.prompt('author')
        setup_author_email = click.prompt('author_email')
        setup_url = click.prompt('url')
        click.echo('\n>> Select one of the following LICENSES ' +
                   '(more detailed info in https://choosealicense.com):\n')

        do.licenses.show()
        chosen_licence = click.prompt(
            '\nEnter the number of the license to choose one')

        # using a dict instead of an if statement
        def lice(num=chosen_licence):
            return {
                '1': lambda: do.licenses.choose(
                    'Apache License 2.0', setup_author),
                '2': lambda: do.licenses.choose(
                    'BSD License', setup_author),
                '3': lambda: do.licenses.choose(
                    'GNU Affero General Public License v3', setup_author),
                '4': lambda: do.licenses.choose(
                    'GNU Lesser General Public License v3', setup_author),
                '5': lambda: do.licenses.choose(
                    'GNU General Public License v3', setup_author,
                    project_name),
                '6': lambda: do.licenses.choose(
                    'MIT License', setup_author),
                '7': lambda: do.licenses.choose(
                    'Mozilla Public License Version 2.0'),
                '8': lambda: do.licenses.choose(
                    'Unlicensed')
            }.get(num, lambda: None)()

        chosen_licence = lice()

        setup = do.template_config.setup_template(
            project_name,
            setup_version,
            setup_description,
            setup_author,
            setup_author_email,
            setup_url
        )

        authors = do.template_config.authors_template(
            project_name,
            setup_author,
            setup_author_email
        )

        do.skeleton.make_skeleton(
            project_name,
            authors,
            chosen_licence,
            setup,
            assist=True
        )

        click.echo('\n>> {} was created on {}'.format(
            project_name, os.path.join(os.getcwd())))


@main.command()
def config():
    """
    A simple configuration for common fields.
    If executed twice, it will overwrite the previous configuration.
    """
    click.echo('\nWelcome to the configuration for common fields.')
    if click.confirm('Do you want to continue?'):
        oneTime_author = click.prompt('\nauthor')
        oneTime_mail = click.prompt('author_email')


def clear(): return os.system('cls')


if __name__ == '__main__':
    main()
