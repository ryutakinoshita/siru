from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Contact
from django.views.generic import (
    TemplateView,
    CreateView,

)


class SetViews(TemplateView,LoginRequiredMixin):
    template_name = 'siru/set.html'


class ContactView(CreateView,LoginRequiredMixin):
    template_name = 'siru/contact_form.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contact_result')

    def form_valid(self,form):
        form.instance.name = self.request.user
        form.send_email()
        return super().form_valid(form)

class ContactResultView(TemplateView,LoginRequiredMixin):
    template_name = 'siru/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context

