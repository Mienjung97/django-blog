from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Adds the form for commenting on a post.
    """
    class Meta:
        model = Comment
        fields = ('body',)