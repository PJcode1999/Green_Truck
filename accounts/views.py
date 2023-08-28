from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from . import forms

class SignUp(CreateView):
    form_class =forms.UserCreateform
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
