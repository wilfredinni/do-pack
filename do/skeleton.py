"""
Create an empty folder and a file structure for a
python project based on the name of the project.
"""

import os
import sys
import json
import click


def make_skeleton(project_name):
    """
    Creates an empty folder and file structure for a python project.
    """
    # make the folders
    for folder in load_template().keys():
        makedir(folder, project_name)
        # make the files
        for files in load_template()[folder]:
            makefile(files, project_name)


def load_template():
    """
    Load the default template for the python package.
    """
    try:
        default_skeleton = os.path.join(
            os.path.dirname(__file__), 'templates', 'default_structure.json'
        )
        with open(default_skeleton) as template:
            return json.load(template)
    except FileNotFoundError:
        click.echo('Template file not found. Aborted!')
        sys.exit(1)


def makedir(directory, project_name):
    """
    Make the folder tree.
    """
    # change the name of base and bin for the name of the project
    if directory == 'base' or directory == 'bin':
        directory = project_name
    # write the folders name
    try:
        os.makedirs(directory)
        os.chdir(directory)
    except FileExistsError:
        click.echo('Folder {} alredy exists. Aborted!'.format(directory))
        sys.exit(1)


def makefile(file, project_name, assist=False):
    """
    Write the files for the project_name
    """
    # change the names of project_name.py and test_project.py
    if file == 'project.py':
        file = '{}'.format(project_name + '.py')
    elif file == 'test_project.py':
        file = '{}'.format('test_' + project_name + '.py')

    if file == '..':  # go back one directory
        os.chdir('..')
    else:
        try:
            with open(file, 'w') as f:
                f.write('')
        except Exception as e:
            click.echo('Error wrinting {}. Aborted!'.format(file))
            sys.exit(1)
