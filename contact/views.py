from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from . import forms

# Create your views here.
class ContactUs(SuccessMessageMixin,CreateView):
    form_class = forms.ContactUsForm
    success_url = reverse_lazy('contact:contact')
    template_name = "contact/contact.html"
    success_message = "Submited successfully"
