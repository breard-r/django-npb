from django.utils.translation import gettext_lazy as _
from django.forms import models as model_forms
from django.utils import timezone
from django.conf import settings
from django import forms
from pytimeparse import parse
from datetime import timedelta
from .models import Paste


EXPIRATION_LENGTH = getattr(settings, 'NPB_EXPIRATION_LENGTH', (
    ('15m', _('15 minutes')),
    ('1h', _('1 hour')),
    ('1d', _('1 day')),
    ('1w', _('1 week')),
    ('30d', _('30 days')),
    ('365d', _('365 days')),
    ('never', _('never')),
))
DEFAULT_EXPIRATION = getattr(
    settings,
    'NPB_DEFAULT_EXPIRATION',
    EXPIRATION_LENGTH[0][0]
)


def _get_paste_form():
    fields = ['content', 'title', 'lexer', 'exposure']
    form = model_forms.modelform_factory(Paste, fields=fields)
    return form


BasePasteForm = _get_paste_form()


class PasteForm(BasePasteForm):
    expire = forms.ChoiceField(
        label=_('expiration'),
        choices=EXPIRATION_LENGTH,
        initial=DEFAULT_EXPIRATION
    )

    def get_expiration_date(self):
        length = self.cleaned_data.get('expire', DEFAULT_EXPIRATION)
        delta_s = parse(length)
        if delta_s is None:
            return None
        now = timezone.now()
        delta = timedelta(seconds=delta_s)
        return now + delta
