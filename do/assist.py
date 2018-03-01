"""
Create de skeleton of the python project and
Redirect the files and folders to the proper function.

Also write the AUTHORS.rst, LICENSE and setup.py with
the users inputs.
"""
import os
import sys
import json
import click


def make_skeleton(project_name, authors, choosen_license, setup, gitignore):
    """
    Create de skeleton of the python project and
    Redirect the files and folders to the proper function.
    """
    # TODO: 50% - implement a template system for the skeleton in .json

    # make the folders
    for folder in load_template().keys():
        makedir(folder, project_name)
        # make the files
        for files in load_template()[folder]:
            makefile(files, project_name, authors,
                     choosen_license, setup, gitignore)


def load_template():
    """
    Load the template for the python package
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
    Make the folders tree.
    """
    # change the name of base and bin for the name of the project
    if directory == 'base' or directory == 'bin':
        directory = project_name
    # write the folders
    try:
        os.makedirs(directory)
        os.chdir(directory)
    except FileExistsError:
        click.echo('Folder {} alredy exists. Aborted!'.format(directory))
        sys.exit(1)


def makefile(file, project_name, authors, choosen_license, setup, gitignore):
    """
    Make the files for the project and write the content
    of AUTHORS.rst, LICENSE and setup.py in assistant mode
    """
    # change the names project.py and test_project.py
    if file == 'project.py':
        file = project_name + '.py'
    elif file == 'test_project.py':
        file = 'test_' + project_name + '.py'

    template_files = {
        'LICENSE': lambda: writefile(file, choosen_license),
        'AUTHORS.rst': lambda: writefile(file, authors),
        'setup.py': lambda: writefile(file, setup),
        '.gitignore': lambda: writefile(file, gitignore)
    }
    # if the file is found, template it, else, None
    template_files.get(file, lambda: writefile(file))()


def writefile(file, content=''):
    """
    Function that write the files and go back one folder
    for the sake of the stucture.
    """
    if file == '..':  # go back one directory
        os.chdir('..')
    else:
        try:
            with open(file, 'w') as f:
                f.write(content)
        except Exception as e:
            click.echo('Error wrinting {}. Aborted!'.format(file))
            sys.exit(1)


if __name__ == '__main__':
    pass
