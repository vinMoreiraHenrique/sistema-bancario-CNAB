from django import forms

class form_transactions(forms.Form):
    file = forms.FileField(required=True, allow_empty_file=False)
    