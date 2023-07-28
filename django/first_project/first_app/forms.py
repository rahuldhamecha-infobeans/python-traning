from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name Needs To Start with Z')
    return value

class MyForm(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField(label="Email")
    verify_email = forms.EmailField(label="Enter Your Email Again :")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        verify_email = all_cleaned_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError('Email is not matched')