from django.utils import timezone
from django.conf import settings
from django import template
from npb.models import Paste


DEFAULT_NB = 5
register = template.Library()


@register.simple_tag(takes_context=True)
def recent_pastes(context):
    limit = getattr(settings, 'NPB_PASTES_LIST_MAX', DEFAULT_NB)
    if limit <= 0:
        return []
    qs = Paste.objects.filter(
        is_suspended=False,
        exposure='public',
        expire_on__gte=timezone.now()
    ).order_by('-created_on')[:limit]
    return qs


@register.simple_tag
def recent_pastes_activated():
    return getattr(settings, 'NPB_PASTES_LIST_MAX', DEFAULT_NB) > 0
