from django.utils import timezone
from django.conf import settings
from django import template
from npb.models import Paste


register = template.Library()


@register.simple_tag(takes_context=True)
def get_recent_pastes(context):
    if getattr(settings, 'NPB_DISABLE_LIST', False):
        return []
    qs = Paste.objects.filter(
        is_removed=False,
        exposure='public',
        expire_on__gte=timezone.now()
    ).order_by('-created_on')[:10]
    return qs
