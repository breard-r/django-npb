from django.views import generic
from django.conf import settings
from .models import Paste


_css_file_name = getattr(settings, 'NPB_CSS_CLASS', 'pygments.css')


class ShowPasteView(generic.DetailView):
    model = Paste
    context_object_name = 'paste'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_file_name'] = 'npb/%s' % _css_file_name
        return context


class CreatePasteView(generic.edit.CreateView):
    model = Paste
    fields = ['is_private', 'lexer', 'title', 'content']
