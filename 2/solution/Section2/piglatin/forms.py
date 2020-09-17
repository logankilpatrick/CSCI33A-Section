from django import forms

class TextForm(forms.Form):
    plain = forms.CharField(label="Original Text", widget=forms.Textarea(attrs={'placeholder': 'Text to Translate...'}))