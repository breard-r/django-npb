Quickstart
==========

You can install Django neo-pastebin directly from PyPI:

::

    pip install django-npb


Integrate with Django
---------------------

Add django-npb to your INSTALLED_APPS:

.. code-block:: python

    INSTALLED_APPS = [
        [skiped],
        'npb.apps.NpbConfig',
    ]

Then add the URLs:

.. code-block:: python

    urlpatterns = [
        [skiped],
        path('paste/', include('npb.urls', namespace='npb')),
    ]


If you uses internationalization, you are encouraged to add the path your i18n_patterns instead.


Configure
---------

To configure NPB once it is set up, see :ref:`config-opts`.
