from django.shortcuts import render
from django.views.generic import ListView

from .models import Video 

class MainPage(ListView):
  model = Video
  template_name = "videos/index.html"
  context_object_name = "videos"

