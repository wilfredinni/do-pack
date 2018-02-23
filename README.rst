do-pack
=======

A simple and quick command line tool to create python packages.


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
