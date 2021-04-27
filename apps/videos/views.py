from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Video, Comment
from .forms import CommentForm

class MainPage(ListView):
  model = Video
  template_name = "videos/index.html"
  context_object_name = "videos"
  queryset = Video.objects.all().order_by('-date')

class DetailVideo(DetailView):
  model = Video
  slug_url_kwarg = "video"
  template_name = "videos/detail-video.html"
  context_object_name = "video"

  def get_context_data(self,*args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      context['comments'] = Comment.objects.filter(video__slug=self.kwargs['video']).order_by('-date')
      context['comment_form'] = CommentForm()
      return context

class AddComment(View):
  def post(self, request, *args, **kwargs):

    form = CommentForm(request.POST)
    
    if form.is_valid():
      if request.user.is_authenticated:
        Comment.objects.create(**form.cleaned_data, author=request.user, video=Video.objects.get(slug=self.kwargs['video']))
      else:
        Comment.objects.create(**form.cleaned_data, author="Anonymous", video=Video.objects.get(slug=self.kwargs['video']))
    
    return redirect(reverse_lazy('videos:detail-video', kwargs={'video': self.kwargs['video']}))