import click
import os
import do.skeleton
import do.licenses
import do.setup_config


def clear(): return os.system('cls')


@click.group()
def main():
    """
    Simple CLI based script to make your Repository Structure.
    """
    pass


@main.command()
@click.argument('project-name')
def create(project_name):
    """
    creates an empty proyect structure.
    """
    click.echo('\nPypro will create your {} Project Structure.'
               .format(project_name))
    if click.confirm('Do you want to continue?'):
        do.skeleton.make_skeleton(project_name)
        click.echo('{} was created on {}'.format(project_name,
                                                 os.path.join(os.getcwd())))
    else:
        click.echo('Aborded!')


@main.command()
def assistant():
    """
    A step by step assistant.
    """
    # TODO: change all the flag for assist
    clear()
    # click.echo('do will now start the assistant.')
    if click.confirm('>> do will now start the assistant.' +
                     ' Do you want to continue?'):
        clear()
        # project name
        name = click.prompt('>> Enter your Project name')
        # flag=True == asistant mode - flag=False == project mode
        clear()
        do.skeleton.make_skeleton(name, flag=True)


def legal():
    """
    Prints the licenses and let you choose one to be writed
    in the LICENSE file.
    """
    click.echo(
        '>> Select one of the following LICENSES ' +
        '(more detailed info in https://choosealicense.com):\n')

    do.licenses.show()
    chosen_licence = click.prompt(
        'Enter the number of the license to choose one')

    # TODO: check if the user imput is valid and change to a dict

    if chosen_licence == '1':
        clear()
        return do.licenses.choose('MIT License', 1)
    elif chosen_licence == '2':
        clear()
        return do.licenses.choose('Apache License 2.0', 1)
    elif chosen_licence == '3':
        clear()
        return do.licenses.choose('GNU GPLv3', 1)


def setup():
    """
    Allows you to fill in the basic fields of setup.py.
    """
    click.echo('>> Enter the informatión for your setup.py file:\n')
    setup_name = click.prompt('name')
    setup_version = click.prompt('version')
    setup_description = click.prompt('description')
    setup_author = click.prompt('author')
    setup_author_email = click.prompt('author_email')
    setup_url = click.prompt('url')

    return do.setup_config.setup_template(
        setup_name,
        setup_version,
        setup_description,
        setup_author,
        setup_author_email,
        setup_url
    )


if __name__ == '__main__':
    main()
