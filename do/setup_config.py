from string import Template


def setup_template(
    setup_name,
    setup_version,
    setup_description,
    setup_author,
    setup_author_email,
    setup_url,
):
    setup_file = Template(
        """# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='$setup_name',
    version='$setup_version',
    description='$setup_description',
    long_description=readme,
    author='$setup_author',
    author_email='$setup_author_email',
    url='$setup_url',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)"""
    )
    return setup_file.substitute(
        setup_name=setup_name,
        setup_version=setup_version,
        setup_description=setup_description,
        setup_author=setup_author,
        setup_author_email=setup_author_email,
        setup_url=setup_url,
    )

# TODO: change the setup to a file
