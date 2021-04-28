from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

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

