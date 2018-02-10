from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse
from django.db import models
from pygments.formatters import HtmlFormatter
from pygments.lexers import (
    get_all_lexers, get_lexer_by_name, guess_lexer
)
from pygments import highlight
import uuid


PASTE_EXPOSURES = (
    ('public', _('public')),
    ('unlisted', _('unlisted')),
    ('private', _('private')),
)


class Paste(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_('identifier')
    )
    is_removed = models.BooleanField(
        default=False,
        blank=True,
        verbose_name=_('removed paste')
    )
    removal_reason = models.CharField(
        max_length=512,
        default='',
        blank=True,
        verbose_name=_('removal reason')
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
        choices=[(l[1][0], l[0]) for l in get_all_lexers()],
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
        verbose_name = 'Paste'
        verbose_name_plural = 'Pastes'

    def __str__(self):
        return '%s' % self.uuid
