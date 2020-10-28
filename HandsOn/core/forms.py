from django import forms
import datetime

class UserForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea,required=False)