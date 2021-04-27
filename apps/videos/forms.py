from django import forms

from .models import Comment 

class CommentForm(forms.ModelForm):
  
  body = forms.CharField(label='Leave your comment comment:', widget=forms.Textarea(attrs={
    'class': 'form-control',
    'style': 'resize: none;'
  }))

  class Meta:
    model = Comment
    fields = ('body',)