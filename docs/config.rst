.. _config-opts:

Configuration options
=====================

The following configuration variables may be set in your project's settings.py file.


Common settings
---------------

NPB_DEFAULT_EXPIRATION
~~~~~~~~~~~~~~~~~~~~~~

Set which expiration duration is selected by default. The value is a pytimeparse_ duration which is set in NPB_EXPIRATION_LENGTH. Default is the first NPB_EXPIRATION_LENGTH value.

.. code-block:: python

    NPB_DEFAULT_EXPIRATION = '1d'

NPB_DEFAULT_EXPOSURE
~~~~~~~~~~~~~~~~~~~~

Default exposure for new pastes. Must be either "public", "unlisted" or "private". Default is "public".

NPB_EDIT_TOLERANCE
~~~~~~~~~~~~~~~~~~

Set the tolerance time during which a paste can be edited without being labeled as so.
Set to a negative value, it always shows the edit time.
Set to a positive value, it represents the number of seconds after the creation time during which edits are not shown.
Zero causes an undefined behavior. Default is 1.

NPB_EXPIRATION_LENGTH
~~~~~~~~~~~~~~~~~~~~~

Set the allowed expiration duration. It is a list of tuples where the first element if a pytimeparse_ duration (16 characters maximum) and the second one is the name to be displayed.

.. code-block:: python

    NPB_EXPIRATION_LENGTH = [
        ('15m', _('15 minutes')),
        ('1h', _('1 hour')),
        ('1d', _('1 day')),
        ('1w', _('1 week')),
        ('30d', _('30 days')),
        ('365d', _('365 days')),
        ('never', _('never')),
    ]

NPB_PASTES_LIST_MAX
~~~~~~~~~~~~~~~~~~~

Maximum number of posts displayed in the "recent posts" list. Set it to zero if you want to disable the list. Default is 5.

NPB_REPORT_CATEGORIES
~~~~~~~~~~~~~~~~~~~~~

Set the list of reasons a paste can be reported to an administrator. It is a list of tuples where the first element if a short identifier (16 characters maximum) and the second one is the name to be displayed.

.. code-block:: python

    NPB_REPORT_CATEGORIES = [
        ('illicit', _('illicit content')),
        ('explicit', _('explicit content')),
        ('copyright', _('copyright infrigment')),
        ('private', _('private information exposure')),
        ('other', _('other')),
    ]

NPB_TAB_SIZE
~~~~~~~~~~~~

Set the number of spaces needed to represent a tabulation. Default is 4.

NPB_X_FORWARDED_FOR
~~~~~~~~~~~~~~~~~~~

Defines how NPB must use the X-Forwarded-For HTTP header. The value must be one of the following:

* "none": Do not use the header at all.
* "first": Use the first IP listed as the end-user's one.
* "last": Use the last IP listed as the end-user's one.

Default is "none".


Development settings
--------------------

NPB_CSS_CLASS
~~~~~~~~~~~~~

Name of the generated CSS file for syntax highlighting.


.. _pytimeparse: https://pypi.python.org/pypi/pytimeparse
