

do-pack
=======

A simple and quick command line tool to create python packages.

.. image:: https://requires.io/github/wilfredinni/do-pack/requirements.svg?branch=master
    :target: https://requires.io/github/wilfredinni/do-pack/requirements/?branch=master

.. image:: https://travis-ci.org/wilfredinni/do-pack.svg?branch=master
    :target: https://travis-ci.org/wilfredinni/do-pack

.. image:: http://img.shields.io/badge/license-MIT-green.svg
    :target: https://github.com/wilfredinni/do-pack/blob/master/LICENSE
    
Install
-------

::

    $ pip install do-pack

Usage
-----

Create an empty project:

::

    $ do create <project-name>

A step by step setup for new projects:

::

    $ do assistant

This command let you fill the ``setup.py``, ``AUTHORS.rst`` and choose a ``LICENSE``.

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
-  Add a ``congig`` command to fill common fields once (such as
   *autor_name* and *author_email*).
-  Generate the documentation (sphinx).
-  Fix *travis build*: ``load_index_json()`` in ``licenses.py``.


.. image:: https://api.codacy.com/project/badge/Grade/1c62be8d3a4a40a282da04aed89ea2f9
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/carlos.w.montecinos/do-pack?utm_source=github.com&utm_medium=referral&utm_content=wilfredinni/do-pack&utm_campaign=badger