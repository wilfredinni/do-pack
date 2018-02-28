import os
import sys
import json
import click


def make_skeleton(project,
                  authors=None,
                  choosen_license=None,
                  setup=None,
                  assist=False):
    """
    Create de skeleton of the python project and
    Redirect the files and folders to the proper function.

    Also write the AUTHORS.rst, LICENSE and setup.py with
    the users inputs in the assistant mode.
    """
    # TODO: 50% - implement a template system for the skeleton in .json

    def makedir(directory):
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

    def makefile(file, assist=False):
        """
        Make the files for the project and write the content
        of AUTHORS.rst, LICENSE and setup.py in assistant mode
        """
        # change the names project.py and test_project.py
        if file == 'project.py':
            file = project + '.py'
        elif file == 'test_project.py':
            file = 'test_' + project + '.py'

        if assist:
            # assist=True == assistant
            {
                'LICENSE': lambda: writefile(file, choosen_license),
                'AUTHORS.rst': lambda: writefile(file, authors),
                'setup.py': lambda: writefile(file, setup)
            }.get(file, lambda: writefile(file))()
        else:
            # assist=False == project (write an empty file)
            writefile(file)

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

    # from here starts the program
    # make the folders
    for folder in load_structure().keys():
        makedir(folder)
        # make the files
        for files in load_structure()[folder]:
            # assist=True == assistant mode - assist=False == create()
            if assist:
                makefile(files, assist=True)
            else:
                makefile(files)


def load_structure():
    """
    Load the template for the python package
    """
    try:
        default_skeleton = os.path.join(
            os.path.dirname(__file__),
            'templates', 'default_structure.json'
        )
        with open(default_skeleton) as f:
            return json.load(f)
    except FileNotFoundError:
        click.echo('Template file not found. Aborted!')
        sys.exit(1)


if __name__ == '__main__':
    pass
