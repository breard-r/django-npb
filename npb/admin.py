from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import Paste


class PasteAdmin(admin.ModelAdmin):
    list_display = [
        'uuid', 'title', 'created_on',
        'author', 'lexer', 'is_private', 'is_removed'
    ]
    list_filter = ['is_private', 'is_removed']
    search_fields = ['author_ip', 'lexer', 'title', 'content']
    fieldsets = [
        (_('Meta'), {'fields': ['is_private', 'author', 'expire_on']}),
        (_('Paste'), {'fields': ['lexer', 'title', 'content']}),
        (_('Administration'), {'fields': ['is_removed', 'removal_reason']}),
    ]

    def has_add_permission(self, request):
        return False


admin.site.register(Paste, PasteAdmin)
