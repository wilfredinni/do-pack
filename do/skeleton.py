import os
import sys
import click
import do.do


def make_skeleton(project, flag=False):
    """
    Create de skeleton of the python project and
    Redirect the files and folders to the proper function
    """
    # TODO: implement a template system for the skeleton in .json
    skeleton = {
        project: ['LICENSE', 'setup.py', 'README.rst'],
        'bin': [project + '.py', '__init__.py', '..'],
        'docs': ['index.rst', '..'],
        'tests': ['__init__.py', 'test_' + project + '.py', '..']
    }

    for folder in skeleton.keys():
        # ternary conditional operator
        makedir(project) if folder == 'bin' else makedir(folder)
        # change the name of the folder bin to project
        if flag:
            # flag=True == assistant mode
            for files in skeleton[folder]:
                makefile(files, flag=True)
        else:
            # flag=False == project
            for files in skeleton[folder]:
                makefile(files)


def makedir(directory):
    """
    Make the folders tree.
    """
    try:
        os.makedirs(directory)
        os.chdir(directory)
    except FileExistsError:
        click.echo('Folder {} alredy exists. Aborted!'.format(directory))
        sys.exit(1)


def makefile(file, flag=False):
    """
    Make the files for the project.
    """
    if flag:
        # flag=True == assistant
        if file == 'LICENSE':
            writefile(file, do.do.legal())
        elif file == 'setup.py':
            writefile(file, do.do.setup())
        else:
            writefile(file, '')

    else:
        # flag=False == project (write an empty file)
        writefile(file, '')


def writefile(file, content):
    """
    Function that write the files and go back one folder
    for the sake of the stucture
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
    make_skeleton('test', flag=True)
