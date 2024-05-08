from django import forms

class example_form(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)