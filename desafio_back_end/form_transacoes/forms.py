from django import forms

class Form_transactions(forms.Form):
    file = forms.FileField(required=True, allow_empty_file=False)
    