from datetime import datetime
from string import Template
import json
import os
import click
import sys

"""
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

# short names for licenses
apache2 = 'Apache License 2.0'
gnuAgpl = 'GNU Affero General Public License v3'
gnuGpl = 'GNU General Public License v3'
bsd = 'BSD License'
mit = 'MIT License'

# relativa path tho the licenses template folder
template_path = license_path = os.path.join(
    os.path.dirname(__file__), 'templates\\licenses\\')

# current year
year = str(datetime.now().year)

# open the index.json that contains the license names and filenames
try:
    with open(template_path + 'index.json', 'r') as i:
        license_list = json.load(i)
except FileNotFoundError:
    click.echo('LicenseNotFoundError: {} Not Found. Aborted!'
               .format(template_path + 'index.json'))
    sys.exit(1)


def show(index_json=license_list):
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
    # open the license templates and use Template() to replace variables
    try:
        with open(template_path + license_list[license_name], 'r') as f:
            license_content = Template(f.read())
    except FileNotFoundError:
        click.echo('LicenseNotFoundError: {} Not Found. Aborted!'
                   .format(template_path + license_list[license_name]))
        sys.exit(1)
    # licenses that need year and author name
    if (license_name == (apache2) or (license_name == bsd) or
        (license_name == gnuAgpl) or
            (license_name == mit)):
        return license_content.substitute(
            year=year,
            fullname=author_name
        )
    # licenses that need year, author name and project name
    elif license_name == gnuGpl:
        return license_content.substitute(
            year=year,
            fullname=author_name,
            project=project
        )
    else:
        return license_content.substitute()


if __name__ == '__main__':
    show()
