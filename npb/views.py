from django.views import generic
from django.conf import settings
from .models import Paste
from .forms import PasteForm
from .ip import get_client_ip


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
    form_class = PasteForm

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        form.instance.author_ip = get_client_ip(self.request)
        form.instance.expire_on = form.get_expiration_date()
        return super().form_valid(form)
