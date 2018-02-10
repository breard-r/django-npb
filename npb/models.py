from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse
from django.db import models
from decouple import config
import uuid


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
    is_private = models.BooleanField(
        default=config('NPB_DEFAULT_IS_PRIVATE', default=False, cast=bool),
        verbose_name=_('private paste')
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
        blank=True,
        verbose_name=_('lexer')
    )
    title = models.CharField(
        max_length=256,
        default='',
        blank=True,
        verbose_name=_('title')
    )
    content = models.TextField(verbose_name=_('content'))

    def get_absolute_url(self):
        return reverse('npb:show_paste', args=[str(self.uuid)])

    def __meta__(self):
        verbose_name = 'Paste'
        verbose_name_plural = 'Pastes'

    def __str__(self):
        return '%s' % self.uuid
