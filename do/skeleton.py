"""
Create an empty folder and a file structure for a
python package based on the name of the project.
"""

import os
import sys
import json
import click


def make_skeleton(project_name, template=False):
    """
    Create an empty structure for a python project.
    """
    if template:
        # load the structure for the custom template
        loaded_template = load_template(template)
    else:
        # load the structure for the default template
        loaded_template = load_template()

    for folder in loaded_template.keys():
        # make the folders
        makedir(folder, project_name)
        for files in loaded_template[folder]:
            # make the files
            makefile(files, project_name)


def load_template(template=False):
    """
    Load the default or custom template for the python package.
    """
    if template:
        if os.path.exists(os.path.join(os.getcwd(), template + '.json')):
            # relative path
            path = os.path.join(os.getcwd(), template + '.json')
        else:
            path = os.path.join(
                os.path.dirname(__file__), 'templates', template + '.json')
    else:
        # absolute path
        path = os.path.join(
            os.path.dirname(__file__), 'templates', 'default_structure.json')
    try:
        with open(path, 'r') as template:
            return json.load(template)
    except FileNotFoundError:
        click.echo('Template file not found. Aborted!')
        sys.exit(1)


def makedir(directory, project_name):
    """
    Make the folder tree.
    """
    # change the name of base and bin for the name of the project
    if (directory == 'base') or (directory == 'bin'):
        directory = project_name
    # write the folders name
    try:
        os.makedirs(directory)
        os.chdir(directory)
    except FileExistsError:
        click.echo('Folder {} alredy exists. Aborted!'.format(directory))
        sys.exit(1)


def makefile(file, project_name):
    """
    Write the files for the project_name
    """
    # change the names of project_name.py and test_project.py
    if file == 'project.py':
        file = '{}'.format(project_name + '.py')
    elif file == 'test_project.py':
        file = '{}'.format('test_' + project_name + '.py')

    if file == '<--':  # go back one directory
        os.chdir('..')
    else:
        try:
            with open(file, 'w') as f:
                f.write('')
        except Exception as e:
            click.echo('Error wrinting {}. Aborted!'.format(file))
            sys.exit(1)


if __name__ == '__main__':
    pass
