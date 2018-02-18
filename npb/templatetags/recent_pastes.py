from django.db.models import Q
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
        expire_on__gte=timezone.now()
    )
    if context.request.user.is_authenticated:
        qs = qs.filter(Q(exposure='public') | Q(author=context.request.user))
    else:
        qs = qs.filter(exposure='public')
    qs = qs.order_by('-created_on')[:limit]
    return qs


@register.simple_tag
def recent_pastes_activated():
    return getattr(settings, 'NPB_PASTES_LIST_MAX', DEFAULT_NB) > 0
