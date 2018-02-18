# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='do-pack',
    version='0.1.0',
    description='A command-line tool to create python packages',
    long_description=readme,
    author='Carlos Montecinos Geisse',
    author_email='carlos.w.montecinos@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
