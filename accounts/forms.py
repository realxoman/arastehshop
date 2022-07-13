from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput, PasswordInput
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(label=_('username'))
    password = forms.CharField(label=_('password'), widget=PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'رمز عبور'
    }))
    
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user