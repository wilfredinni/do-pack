"""
How to template the licenses:

$project - $year - $fullname
-------------------------------------
GNU_GPLv3   = year, fullname, project
apache2     = year, fullname
BSD         = year, fullname
GNU_AGPLv3  = year, fullname
mit         = year, fullname
GNU_LGPLv3  = None
Mozilla     = None
Unlicensed  = None
"""

from datetime import datetime
from string import Template
import json
import os
import click
import sys

# short names for licenses
apache2 = 'Apache License 2.0'
gnuAgpl = 'GNU Affero General Public License v3'
gnuGpl = 'GNU General Public License v3'
bsd = 'BSD License'
mit = 'MIT License'

# relative path tho the licenses template folder
template_path = os.path.join(
    os.path.dirname(__file__), 'templates\\licenses\\')

# current year
year = str(datetime.now().year)


def load_index_json(path=template_path):
    # open the index.json that contains the license names and filenames
    try:
        # !FIXME: error in travis!!!!
        with open(os.path.join(path, 'index.json'), 'r') as i:
            return json.load(i)
    except FileNotFoundError:
        click.echo('LicenseNotFoundError: {} Not Found. Aborted!'
                   .format(template_path + 'index.json'))
        sys.exit(1)


def load_license_content(license_name):
    """
    Load the content of a license
    """
    index_json = load_index_json()
    # open the license templates and use Template() to replace variables
    try:
        with open(template_path + index_json[license_name], 'r') as f:
            return Template(f.read())
    except FileNotFoundError:
        click.echo('LicenseNotFoundError: {} Not Found. Aborted!'
                   .format(template_path + index_json[license_name]))
        sys.exit(1)


def show(index_json=load_index_json()):
    """
    Prints a the list of licenses in the index.json for the user to choose
    """
    index = 1
    # iterates over the keys of index.json and print them
    for licenses in index_json.keys():
        click.echo('{} - {}'.format(str(index), licenses))
        index += 1


def choose(license_name, author_name=None, project=None):
    """
    Allows to Choose one license, but only in assistant mode.

    """
    # the call to the function that load the content a license
    lic_name = load_license_content(license_name)

    # licenses that need year and author name
    if ((license_name == apache2) or
        (license_name == bsd) or
        (license_name == gnuAgpl) or
            (license_name == mit)):
        return lic_name.substitute(year=year,
                                   fullname=author_name
                                   )
    # licenses that need year, author name and project name
    elif license_name == gnuGpl:
        return lic_name.substitute(year=year,
                                   fullname=author_name,
                                   project=project
                                   )
    else:
        return lic_name.substitute()


if __name__ == '__main__':
    show()
