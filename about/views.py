from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from . import forms
# Create your views here.
class AboutUs(SuccessMessageMixin,CreateView):
    form_class = forms.Subscriberform
    success_url = reverse_lazy('about:about')
    template_name = "about/about.html"
    success_message = "Subcribe successfully"