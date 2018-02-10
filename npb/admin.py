from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import Paste


class PasteAdmin(admin.ModelAdmin):
    list_display = (
        'uuid', 'title', 'created_on', 'expire_on',
        'author', 'lexer', 'exposure', 'is_removed'
    )
    ordering = ('-created_on',)
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


admin.site.register(Paste, PasteAdmin)
