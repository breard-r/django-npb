from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views import generic
from django.http import Http404
from django.conf import settings
from .models import Paste, Report
from .forms import PasteForm, ReportForm
from .ip import get_client_ip


_css_file_name = getattr(settings, 'NPB_CSS_CLASS', 'pygments.css')


class ShowPasteView(generic.DetailView):
    model = Paste
    context_object_name = 'paste'

    def get_object(self, queryset=None):
        paste = super().get_object(queryset=queryset)
        restricted = all([
            paste.exposure == 'private',
            paste.author != self.request.user,
            not self.request.user.is_superuser,
            not self.request.user.is_staff
        ])
        if restricted:
            raise Http404()
        return paste

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['css_file_name'] = 'npb/%s' % _css_file_name
        return context


class CreatePasteView(generic.edit.CreateView):
    model = Paste
    form_class = PasteForm

    def get_form_class(self):
        form = super().get_form_class()
        if not self.request.user.is_authenticated:
            form.base_fields['exposure'].widget.choices = [
                c for c in form.base_fields['exposure'].widget.choices
                if c[0] != 'private'
            ]
        return form

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        form.instance.author_ip = get_client_ip(self.request)
        form.instance.expire_on = form.get_expiration_date()
        messages.info(self.request, _('Your paste has been created.'))
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
        messages.info(
            self.request,
            _('Your report has been sent to an administrator.')
        )
        return super().form_valid(form)
