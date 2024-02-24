from django import forms


class FormCreate(forms.Form):
    full_name = forms.CharField(max_length=255, required=True)
    phone = forms.CharField(max_length='20', required=True)
    message = forms.CharField(widget=forms.Textarea, required=False)
