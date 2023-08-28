from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class UserCreateform(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class meta:
        fields = ("username", "email", "first_name",
                  "last_name", "password1", "password2")
        model = User
         
    def save(self, commit=True):
        user = super(UserCreateform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
    

    def __init__(self, *args, **kwargs,):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["first_name"].label = "First Name"
        self.fields["last_name"].label = "Last Name"
        self.fields["email"].label = "Email"
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
