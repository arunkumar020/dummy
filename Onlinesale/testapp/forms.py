from django import forms
from django.core import validators
class online(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    contact=forms.IntegerField()

