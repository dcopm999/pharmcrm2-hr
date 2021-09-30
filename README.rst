=============================
pharmcrm2-hr
=============================

.. image:: https://badge.fury.io/py/pharmcrm2-hr.svg
    :target: https://badge.fury.io/py/pharmcrm2-hr

.. image:: https://travis-ci.org/dcopm999/pharmcrm2-hr.svg?branch=master
    :target: https://travis-ci.org/dcopm999/pharmcrm2-hr

.. image:: https://codecov.io/gh/dcopm999/pharmcrm2-hr/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dcopm999/pharmcrm2-hr

PharmCRM2: Human resources

Documentation
-------------

The full documentation is at https://pharmcrm2-hr.readthedocs.io.

Quickstart
----------

Install pharmcrm2-hr::

    pip install pharmcrm2-hr

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'hr',
        ...
    )

Add pharmcrm2-hr's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
        path("hr/", include("hr.urls")),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
