=====
Usage
=====

To use pharmcrm2-hr in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'hr.apps.HrConfig',
        ...
    )

Add pharmcrm2-hr's URL patterns:

.. code-block:: python

    from hr import urls as hr_urls


    urlpatterns = [
        ...
        url(r'^', include(hr_urls)),
        ...
    ]
