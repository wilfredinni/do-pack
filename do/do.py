import click
import os
import do.skeleton
import do.licenses
import do.template_config
import do.config


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
    notice = '\ndo will create your {} Project Structure.'
    done = '{} was created on {}'

    click.echo(notice.format(project_name))
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

    clear()
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

        do.licenses.show()
        chosen_licence = click.prompt(msg_choose_lice)

        # using a dict instead of an if statement
        def lice(num=chosen_licence):
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
            }.get(num, lambda: None)()

        # save the template for the license
        # chosen_licence = lice()

        # save the template for setup.py
        setup = do.template_config.setup_template(
            project_name,
            setup_version,
            setup_description,
            setup_author,
            setup_author_email,
            setup_url
        )

        # save the template for AUTHORS.rst
        authors = do.template_config.authors_template(
            project_name,
            setup_author,
            setup_author_email
        )

        # use the saved templates to generate the folders and files
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

    click.echo(msg_welcome)
    if click.confirm('Do you want to continue?'):
        oneTime_author = click.prompt(msg_ask_author, default=default_author)
        oneTime_mail = click.prompt(msg_ask_mail, default=default_mail)
        do.config.write_json(oneTime_author,
                             oneTime_mail)


def clear(): return os.system('cls')


if __name__ == '__main__':
    main()
