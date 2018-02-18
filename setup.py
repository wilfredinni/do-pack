# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='do-pack',
    version='0.1dev',
    description='A command-line tool to create python packages',
    long_description=readme,
    author='Carlos Montecinos Geisse',
    author_email='carlos.w.montecinos@gmail.com',
    url='https://github.com/wilfredinni/do-pack',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    install_requires=['click'],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'do = do.do:main',
        ]
    },
)
