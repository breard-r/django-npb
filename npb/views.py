from django.shortcuts import get_object_or_404
from django.views import generic
from django.conf import settings
from .models import Paste, Report
from .forms import PasteForm, ReportForm
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


class CreateReportView(generic.edit.CreateView):
    model = Report
    form_class = ReportForm

    def form_valid(self, form):
        paste = get_object_or_404(Paste, pk=self.kwargs.get('pk'))
        form.instance.paste = paste
        if self.request.user.is_authenticated:
            form.instance.reporter = self.request.user
        form.instance.reporter_ip = get_client_ip(self.request)
        return super().form_valid(form)
