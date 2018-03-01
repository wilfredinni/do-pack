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

Run the ``config`` command to fill common fields once (if executed twice, it will overwrite the previous configuration):

::

    $ do config


Create an empty project:

::

    $ do create <project-name>

A step by step setup for new projects:

::

    $ do assistant

This command let you fill the ``setup.py``, ``AUTHORS.rst``, choose a ``LICENSE`` and write
a ``.gitignore`` file with rules for *Linux*, *MacOs*, *Windows*, *Python*, *Visual Studio*, *VS Code*, 
*Sublime Text* and *Pycharm* (made with https://www.gitignore.io/).

Folder Structure
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
   (50%).
-  Generate the documentation (sphinx).
