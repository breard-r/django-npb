from django.conf import settings


def get_client_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    fw_policy = getattr(settings, 'NPB_X_FORWARDED_FOR', 'none')

    if fw_policy in ('first', 'last'):
        forwarded = request.META.get('HTTP_X_FORWARDED_FOR') or ''
        if forwarded:
            forwarded = forwarded.split(',')
            if fw_policy == 'first':
                ip = forwarded[0]
            else:
                ip = forwarded.pop()

    return ip
