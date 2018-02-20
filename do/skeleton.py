import os
import sys
import json
import click


def make_skeleton(project, choosen_license=None, setup=None, assist=False):
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
                writefile(file, choosen_license)
            elif file == 'setup.py':
                writefile(file, setup)
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
        # try:
        # file == '..' go back one directory
        if file == '..':
            os.chdir('..')
        else:
            with open(file, 'w') as f:
                f.write(content)
        # except Exception as e:
        #     click.echo('Error wrinting {}. Aborted!'.format(file))
        #     sys.exit(1)

    for folder in skeleton.keys():
        # create the folders
        makedir(folder)

        for files in skeleton[folder]:
            # assist=True == assistant mode - assist=False == create()
            if assist:
                makefile(files, assist=True)
            else:
                makefile(files)


if __name__ == '__main__':
    make_skeleton('test')
