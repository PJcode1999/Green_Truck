from django import forms
from .models import *

class Subscriberform(forms.ModelForm):
    class Meta():
        model = Subscriber
        fields = '__all__'