import uuid

from django.contrib.auth import views
from django.views.generic import CreateView, View, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.apps import apps

from . import forms


class SignIn(views.LoginView):
  template_name = "account/signin.html"
  form_class = forms.SignInForm

  def get_redirect_url(self):
    return reverse_lazy('account:profile', kwargs={'username': self.request.user.username})

class SignUp(CreateView):
  form_class = forms.SignUpForm
  template_name = "account/signup.html"
  
  def get_success_url(self):
    return reverse_lazy('account:profile', kwargs={'username': self.request.user.username})

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return redirect(self.get_success_url())

class SignOut(views.LogoutView):
  next_page = reverse_lazy('videos:main-page')

class Profile(LoginRequiredMixin, CreateView):
  login_url = reverse_lazy('account:signin')
  template_name = "account/profile.html"
  model = apps.get_model('videos', 'Video')
  form_class = forms.VideoUploadForm

  def form_valid(self, form):

    self.model.objects.create(**form.cleaned_data,
                              author=self.request.user,
                              uuid=uuid.uuid4())
                              
    return redirect('.')
