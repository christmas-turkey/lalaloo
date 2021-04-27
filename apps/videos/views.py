from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Video 

class MainPage(ListView):
  model = Video
  template_name = "videos/index.html"
  context_object_name = "videos"

class DetailVideo(DetailView):
  model = Video
  slug_url_kwarg = "video"
  template_name = "videos/detail-video.html"
  context_object_name = "video"
