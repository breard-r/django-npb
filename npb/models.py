from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse
from django.db import models
from pygments.formatters import HtmlFormatter
from pygments.lexers import (
    get_all_lexers, get_lexer_by_name, guess_lexer
)
from pygments import highlight
from datetime import timedelta
import uuid


PASTE_EXPOSURES = (
    ('public', _('public')),
    ('unlisted', _('unlisted')),
    ('private', _('private')),
)

REPORT_CATEGORIES = getattr(settings, 'NPB_REPORT_CATEGORIES', (
    ('illicit', _('illicit content')),
    ('explicit', _('explicit content')),
    ('copyright', _('copyright infrigment')),
    ('private', _('private information exposure')),
    ('other', _('other')),
))

LEXERS = [('', _('auto detect'))]
LEXERS += [(l[1][0], l[0]) for l in get_all_lexers()]


class Paste(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_('identifier')
    )
    is_suspended = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_('suspended paste')
    )
    suspension_reason = models.CharField(
        max_length=512,
        default='',
        blank=True,
        verbose_name=_('suspension reason')
    )
    exposure = models.CharField(
        max_length=16,
        choices=PASTE_EXPOSURES,
        default=getattr(settings, 'NPB_DEFAULT_EXPOSURE', 'public'),
        verbose_name=_('exposure')
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name=_('created on')
    )
    edited_on = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name=_('edited on')
    )
    expire_on = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('expiration date')
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('author')
    )
    author_ip = models.GenericIPAddressField(
        null=True,
        blank=True,
        verbose_name=_('author\'s IP address')
    )
    lexer = models.CharField(
        max_length=128,
        choices=LEXERS,
        blank=True,
        verbose_name=_('language')
    )
    title = models.CharField(
        max_length=256,
        default='',
        blank=True,
        verbose_name=_('title')
    )
    content = models.TextField(verbose_name=_('content'))

    def edited(self):
        tolerance_setting = getattr(settings, 'NPB_EDIT_TOLERANCE', 1)
        if tolerance_setting < 0:
            return True
        delta = self.edited_on - self.created_on
        tolerance = timedelta(seconds=tolerance_setting)
        return delta > tolerance

    def formated_content(self):
        css_class = getattr(settings, 'NPB_CSS_CLASS', 'highlight')
        tabsize = getattr(settings, 'NPB_TAB_SIZE', 4)
        lexer = None
        lexer_options = {
            'stripall': True,
            'tabsize': tabsize,
        }
        if self.lexer != '':
            lexer = get_lexer_by_name(self.lexer, **lexer_options)
        else:
            lexer = guess_lexer(self.content, **lexer_options)
        formatter = HtmlFormatter(linenos=True, cssclass=css_class)
        return highlight(self.content, lexer, formatter)

    def get_absolute_url(self):
        return reverse('npb:show_paste', args=[str(self.uuid)])

    def __meta__(self):
        verbose_name = _('paste')
        verbose_name_plural = _('pastes')

    def __str__(self):
        return '%s' % self.uuid


class Report(models.Model):
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('author')
    )
    reporter_email = models.EmailField(verbose_name=_('reporter\'s email'))
    reporter_ip = models.GenericIPAddressField(
        null=True,
        blank=True,
        verbose_name=_('reporter\'s IP address')
    )
    reported_on = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name=_('reported on')
    )
    paste = models.ForeignKey(
        Paste,
        on_delete=models.CASCADE,
        verbose_name=_('reported paste')
    )
    category = models.CharField(
        max_length=16,
        choices=REPORT_CATEGORIES,
        verbose_name=_('category name')
    )
    reason = models.TextField(verbose_name=_('reason'))

    def short_reason(self):
        max_len = 32
        short = self.reason[:max_len]
        if len(self.reason) > max_len:
            short += '…'
        return short

    def get_absolute_url(self):
        return reverse('npb:show_paste', args=[str(self.paste.uuid)])

    def __meta__(self):
        verbose_name = _('report')
        verbose_name_plural = _('reports')

    def __str__(self):
        return self.short_reason()
