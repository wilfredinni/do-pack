# -*- coding: utf-8 -*-


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
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License 2.0',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
