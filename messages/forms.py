from django import forms

class MessageForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    homepage = forms.URLField(required=False)
    title = forms.CharField(required=True)
    content = forms.CharField(required=True)
