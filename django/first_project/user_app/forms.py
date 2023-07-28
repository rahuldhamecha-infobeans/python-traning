from django import forms
from django.core import validators
from user_app.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
