from django import forms

from .models import Comment 

class CommentForm(forms.ModelForm):
  
  body = forms.CharField(widget=forms.Textarea(attrs={
    'class': 'form-control',
    'style': 'resize: none;',
    'placeholder': 'Leave your comment:'
  }))

  class Meta:
    model = Comment
    fields = ('body',)