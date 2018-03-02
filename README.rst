do-pack
=======

A simple and quick command line tool to create python packages.

.. image:: https://badge.fury.io/py/do-pack.svg
    :target: https://badge.fury.io/py/do-pack

.. image:: https://travis-ci.org/wilfredinni/do-pack.svg?branch=master
    :target: https://travis-ci.org/wilfredinni/do-pack

.. image:: https://requires.io/github/wilfredinni/do-pack/requirements.svg?branch=master
    :target: https://requires.io/github/wilfredinni/do-pack/requirements/?branch=master  
    
.. image:: https://api.codacy.com/project/badge/Grade/33ea81ba45c64d1199f8b9cd94f11131
    :target: https://www.codacy.com/app/carlos.w.montecinos/do-pack?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wilfredinni/do-pack&amp;utm_campaign=Badge_Grade

.. image:: https://bettercodehub.com/edge/badge/wilfredinni/do-pack?branch=master
    :target: https://bettercodehub.com/

.. image:: http://img.shields.io/badge/license-MIT-green.svg
    :target: https://github.com/wilfredinni/do-pack/blob/master/LICENSE

Install
-------

::

    $ pip install do-pack

Usage
-----

<<<<<<< HEAD
- Run the config command:
=======
Run the ``config`` command to fill common fields once (if executed twice, it will overwrite the previous configuration):
>>>>>>> b10b4da58dc1e8bd89b7a6e4b19520d6073191e1

::

    $ do config


- Create a default python project:

::

    $ do create <project-name>

Create a project using one of the available templates:

::

    $ do create <project-name> -t <template>

*-t* is the short for *--template*.
Available templates: *flask*, *django* and *pymin* (minimal python project).

To use your own template put it in a *.json* file in your current directory. Ex.:

::

    $ do create <project-name> -t <my-template>

- Create a project using the step by step setup:

::

    $ do assistant

This command let you fill the ``setup.py``, ``AUTHORS.rst``, choose a ``LICENSE`` and write
a ``.gitignore`` file with rules for *Linux*, *MacOs*, *Windows*, *Python*, *Visual Studio*, *VS Code*, 
*Sublime Text* and *Pycharm* (made with https://www.gitignore.io/).

Default Folder Structure
----------------

::

    project_folder
    ├── project
    │   ├── __init__.py
    │   └── project.py
    ├── docs
    │   └── index.rst
    ├── tests
    │   ├── __init__.py
    │   └── project_test.py
    ├── .gitignore
    ├── LICENSE
    ├── README.rst
    ├── AUTHORS.rst
    ├── setup.py
    ├── requirements.txt
    └── test-requirements.txt


TODOs
-----

-  Implement a ``template`` system for a more flexible folder structure
   (75%).
-  Add github username to the ``config`` command to fill the project url.
-  Generate the documentation (sphinx).