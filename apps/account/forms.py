from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.apps import apps


class SignInForm(AuthenticationForm):

  username = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Enter username:'
  }))
  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-control',
    'placeholder': 'Enter password:'
  }))

  def get_invalid_login_error(self):
    
    messages.error(self.request, 'Invalid username or password')
    return super().get_invalid_login_error() 


class SignUpForm(UserCreationForm):

  username = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Enter username:'
  }))

  password = forms.EmailField(widget=forms.EmailInput(attrs={
    'class': 'form-control',
    'placeholder': 'Enter email:'
  }))

  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-control',
    'placeholder': 'Enter password:'
  }))
  
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-control',
    'placeholder': 'Confirm password:'
  }))

class VideoUploadForm(forms.ModelForm):

  title = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Enter video title:'
  }))

  description = forms.CharField(widget=forms.Textarea(attrs={
    'class': 'form-control',
    'placeholder': 'Enter video description:',
    'style': 'resize: none;'
  }))

  topics = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Enter topics list due to pattern: "topic,topic,topic"'
  }))
  
  video = forms.FileField(widget=forms.FileInput(attrs={
    'class': 'form-control',
    'placeholder': 'Select video'
  }))

  class Meta:
    model = apps.get_model('videos', 'Video')
    fields = ('title', 'description', 'topics', 'video')

