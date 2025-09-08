from django import forms
from .models import Feedback

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment']
        widgets = {
            'comment':forms.Textarea(attrs = {'rows':4,'placeholder':'Leave your feedback here...'})
        }