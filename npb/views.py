from django.views import generic
from .models import Paste


class ShowPasteView(generic.DetailView):
    model = Paste
    context_object_name = 'paste'


class CreatePasteView(generic.edit.CreateView):
    model = Paste
    fields = ['is_private', 'lexer', 'title', 'content']
