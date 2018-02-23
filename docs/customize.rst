Customize
=========

Add fields to the forms
-----------------------

There is many reason to use a custom form. The most obvious one is to add your favorite captcha engine. Fortunately, it is very simple to add such custom fields.

First, you need to build the form itself by overloading one of the default one. Base it upon npb.forms.PasteForm or npb.forms.ReportForm depending on which form you want to extend.

.. code-block:: python

    from django.utils.translation import gettext_lazy as _
    from npb.forms import PasteForm, ReportForm
    from django import forms


    class MyCustomForm(PasteForm):
        my_field = forms.CharField(
            label=_('My field'),
            max_length=128,
        )


Once your form is ready, pass it to the view.

.. code-block:: python

    from django.urls import path
    from npb import views as npb_views
    from .forms import MyCustomForm


    urlpatterns = [
        path(
            '',
            npb_views.CreatePasteView.as_view(form_class=MyCustomForm),
            name='index'
        ),
    ]


Editing the style
-----------------

The simplest and more powerful way to edit the style is to `override templates`_. The following templates are open to overriding:

npb/base.html
~~~~~~~~~~~~~

This template contains the HTML page's structure. It defines the following empty blocks that will be extended by other templates:

* ``headers``: A place to add extra HTML headers.
* ``title``: The page's title.
* ``content``: The page's content.

It also displays `Django's messages`_ and, if activated, recent pastes.

npb/paste_detail.html
~~~~~~~~~~~~~~~~~~~~~

This template is used to render a specific paste. For this purpose, it uses the ``paste`` variable. Please refer to the ``Past`` object in order to list its available properties.

npb/paste_form.html
~~~~~~~~~~~~~~~~~~~

This template is where the new past form is rendered. It uses the ``form`` variable which is by default a ``npb.PasteForm`` object.

npb/report_form.html
~~~~~~~~~~~~~~~~~~~~

Same as the new paste form but for a new report. The default associated form object is a ``npb.ReportForm``.

recent_pastes
~~~~~~~~~~~~~

In your templates, you can load ``recent_pastes`` to have access to the following tags:

* ``recent_pastes_activated``: True if the recent pastes list is activated, False otherwise.
* ``recent_pastes``: Return an iterator over the most recent pastes.


.. _override templates: https://docs.djangoproject.com/en/2.0/howto/overriding-templates/
.. _Django's messages: https://docs.djangoproject.com/en/2.0/ref/contrib/messages/#displaying-messages
