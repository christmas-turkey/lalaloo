from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib.auth.views import redirect_to_login
from django.db.models import F

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

  def get_object(self, queryset=None):
    uuid = self.kwargs['video']
    video = Video.objects.get(uuid=uuid)

    video.views = F('views') + 1
    video.save()
    video.refresh_from_db()

    return video

  def get_context_data(self,*args, **kwargs):
      context = super().get_context_data(*args, **kwargs)
      context['comments'] = Comment.objects.filter(video__uuid=self.kwargs['video']).order_by('-date')
      context['comment_form'] = CommentForm()
      return context

class AddComment(View):

  def post(self, request, *args, **kwargs):

    form = CommentForm(request.POST)
    if form.is_valid():

      if self.request.user.is_authenticated:
        Comment.objects.create(**form.cleaned_data, author=request.user, video=Video.objects.get(uuid=self.kwargs['video']))
      
      else:
        return redirect_to_login(login_url=reverse_lazy('account:signin'), next=reverse_lazy('videos:detail-video', kwargs={'video': self.kwargs['video']}))
    
    return redirect(reverse_lazy('videos:detail-video', kwargs={'video': self.kwargs['video']}))