from django import forms

class sampleForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()