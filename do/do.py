import do.template_config
import do.skeleton
import do.licenses
import do.assist
import do.config
import click
import sys
import os


# TODO: implement templates for create() (empty structure) 50%.
# TODO: template for python .gitignore


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
    # long messages
    notice = '\ndo will create your {} Project Structure.'.format(project_name)
    done = '{} was created on {}'

    # checks if a template was invoked
    if template:
        print('here comes the templates!!')
    else:
        click.echo(notice)
        if click.confirm('Do you want to continue?'):
            do.skeleton.make_skeleton(project_name)
            click.echo(done.format(project_name, os.path.join(os.getcwd())))


@main.command()
def assistant():
    """
    A step by step assistant.
    """
    # long messages
    msg_notice = '>> do will now start the assistant. Do you want to continue?'
    msg_lice_ref = '(more detailed info in https://choosealicense.com):\n'
    msg_choose_lice = '\nEnter the number of the license to choose one'

    # clear the console
    os.system('cls')

    # click.echo('do will now start the assistant.')
    if click.confirm(msg_notice):
        # retrieve default data from config.json
        config_field = do.config.show_common
        default_author = config_field('default_author')
        default_mail = config_field('default_mail')

        # ask
        project_name = click.prompt('\nproject name')
        setup_version = click.prompt('version', default='0.1.0dev')
        setup_description = click.prompt('description')
        setup_author = click.prompt('author', default=default_author)
        setup_author_email = click.prompt('author_email', default=default_mail)
        setup_url = click.prompt('url')
        click.echo('\n>> Select one of the following LICENSES ' + msg_lice_ref)

        # list the licenses in the console
        do.licenses.show()
        lice_num = click.prompt(msg_choose_lice)

        # save the template for the license
        chosen_licence = lice(lice_num, setup_author, project_name)

        # save the template for setup.py
        setup = do.template_config.setup_template(
            project_name, setup_version, setup_description,
            setup_author, setup_author_email, setup_url
        )
        # save the template for AUTHORS.rst
        authors = do.template_config.authors_template(
            project_name, setup_author, setup_author_email
        )
        # save the template for .gitignore
        gitignore = do.template_config.gitignore_template()
        # use the saved templates to generate the folders and files
        do.assist.make_skeleton(
            project_name, authors, chosen_licence,
            setup, gitignore
        )
        click.echo('\n>> {} was created on {}'.format(
            project_name, os.path.join(os.getcwd())))


@main.command()
def config():
    """
    A simple configuration for common fields.
    If executed twice, it will overwrite the previous one.
    """
    # retrieve the config data from config.json
    config_field = do.config.show_common
    default_author = config_field('default_author')
    default_mail = config_field('default_mail')

    # long messages
    msg_welcome = '\nWelcome to the configuration for common fields.'
    msg_ask_author = '\nauthor'
    msg_ask_mail = 'author_email'

    # ask
    click.echo(msg_welcome)
    if click.confirm('Do you want to continue?'):
        oneTime_author = click.prompt(msg_ask_author, default=default_author)
        oneTime_mail = click.prompt(msg_ask_mail, default=default_mail)
        # write the fields in config.json
        do.config.write_json(oneTime_author, oneTime_mail)


def lice(num, setup_author, project_name):
    # using a dict instead of an if statement
    choose = do.licenses.choose
    return {
        '1': lambda: choose('Apache License 2.0', setup_author),
        '2': lambda: choose('BSD License', setup_author),
        '3': lambda: choose('GNU Affero General Public License v3',
                            setup_author),
        '4': lambda: choose('GNU Lesser General Public License v3',
                            setup_author),
        '5': lambda: choose('GNU General Public License v3',
                            setup_author, project_name),
        '6': lambda: choose('MIT License', setup_author),
        '7': lambda: choose('Mozilla Public License Version 2.0'),
        '8': lambda: do.licenses.choose('Unlicensed')
    }.get(num, lambda: sys.exit(1))()


if __name__ == '__main__':
    main()
