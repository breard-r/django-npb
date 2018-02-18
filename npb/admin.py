from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Paste, Report


class PasteAdmin(admin.ModelAdmin):
    list_display = (
        'uuid', 'title', 'created_on', 'expire_on',
        'author', 'lexer', 'exposure', 'is_removed'
    )
    ordering = ('-created_on',)
    date_hierarchy = 'created_on'
    list_filter = ('exposure', 'is_removed')
    search_fields = ('author_ip', 'lexer', 'title', 'content')
    readonly_fields = ('author', 'author_ip', 'created_on', 'edited_on')
    fieldsets = [
        (_('Meta'), {'fields': [
            'exposure', 'author', 'author_ip',
            'created_on', 'edited_on', 'expire_on'
        ]}),
        (_('Paste'), {'fields': ['lexer', 'title', 'content']}),
        (_('Administration'), {'fields': ['is_removed', 'removal_reason']}),
    ]

    def has_add_permission(self, request):
        return False


class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'short_reason', 'category', 'reported_on',
        'paste', 'reporter', 'reporter_email'
    )
    ordering = ('-reported_on',)
    date_hierarchy = 'reported_on'
    list_filter = ('category',)
    list_select_related = ('paste',)
    readonly_fields = (
        'reporter', 'reporter_email', 'reporter_ip', 'reported_on',
        'paste', 'category', 'reason',
        'paste_content', 'paste_title'
    )
    fieldsets = [
        (_('Meta'), {'fields': [
            'reporter', 'reporter_email', 'reporter_ip',
            'reported_on', 'category', 'reason'
        ]}),
        (_('Paste'), {'fields': ['paste', 'paste_title', 'paste_content']}),
    ]

    def paste_title(self, obj):
        return obj.paste.title

    def paste_content(self, obj):
        return mark_safe(obj.paste.formated_content())

    def has_add_permission(self, request):
        return False

    class Media:
        css = {
            'all': ('npb/pygments.css',)
        }


admin.site.register(Paste, PasteAdmin)
admin.site.register(Report, ReportAdmin)
