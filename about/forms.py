from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Adds a form to send a message to the sites admin
    containing name, email and message.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')