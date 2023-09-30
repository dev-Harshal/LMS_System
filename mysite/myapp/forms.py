from django.forms import forms

class DatasheetForm(forms.Form):
    file = forms.FileField(required = False)
