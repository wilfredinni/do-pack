import os
import sys
import json
import click
import do.do


def make_skeleton(project, assist=False):
    """
    Create de skeleton of the python project and
    Redirect the files and folders to the proper function.
    """
    # TODO: 50% - implement a template system for the skeleton in .json
    try:
        # get the path for the default skeleton
        default_skeleton = os.path.join(
            os.path.dirname(__file__), 'templates/default.json')
    except FileNotFoundError:
        click.echo('Template file not found. Aborted!')
        sys.exit(1)
    # open the default skeleton template from templates folder
    with open(default_skeleton) as f:
        skeleton = json.load(f)

    for folder in skeleton.keys():
        # create the folders
        makedir(folder, project)

        for files in skeleton[folder]:
            # assist=True == assistant mode - assist=False == create()
            makefile(files, project, assist=True) if assist else makefile(
                files, project)


def makedir(directory, project):
    """
    Make the folders tree.
    """

    # change the name of base and bin for the name of the project
    if directory == 'base' or directory == 'bin':
        directory = project

    # write the folders name
    try:
        os.makedirs(directory)
        os.chdir(directory)
    except FileExistsError:
        click.echo('Folder {} alredy exists. Aborted!'.format(directory))
        sys.exit(1)


def makefile(file, project, assist=False):
    """
    Make the files for the project.
    """
    # change the names project.py and test_project.py
    if file == 'project.py':
        file = project + '.py'
    elif file == 'test_project.py':
        file = 'test_' + project + '.py'

    if assist:
        # assist=True == assistant
        if file == 'LICENSE':
            writefile(file, do.do.legal())
        elif file == 'setup.py':
            writefile(file, do.do.setup())
        else:
            writefile(file)
    else:
        # assist=False == project (write an empty file)
        writefile(file)


def writefile(file, content=''):
    """
    Function that write the files and go back one folder
    for the sake of the stucture.
    """
    try:
        # file == '..' go back one directory
        if file == '..':
            os.chdir('..')
        else:
            with open(file, 'w') as f:
                f.write(content)
    except Exception as e:
        click.echo('Error wrinting {}. Aborted!'.format(file))
        sys.exit(1)


if __name__ == '__main__':
    make_skeleton('test', assist=True)
