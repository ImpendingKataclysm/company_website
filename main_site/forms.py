from django import forms
from datetime import datetime


class SendEmailForm(forms.Form):
    """
    Collects the information entered into the email form
    """
    sender_name = forms.CharField()
    sender_email = forms.EmailField()
    date_sent = datetime.now()
    message = forms.CharField(widget=forms.Textarea)
