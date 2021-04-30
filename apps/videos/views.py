import json

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views import View
from django.contrib.auth.views import redirect_to_login
from django.db.models import F
from django.http import JsonResponse

from .models import Video, Comment
from .forms import CommentForm

class MainPage(View):
  
  def get(self, request, *args, **kwargs):

      context = {
        'videos': Video.objects.all().order_by('-date') 
      }
      
      return render(request, 'videos/index.html', context)
  
  def post(self, request, *args, **kwargs):

    search_request = request.POST.get('search_request')

    videos = None

    if search_request.startswith('#'):

      topic = search_request.split('#')[1]

      videos = Video.objects.filter(topics__icontains=topic)
    
    else:
      
      videos = Video.objects.filter(title__icontains=search_request)
    
    context = {
      'videos': videos
    }

    return render(request, 'videos/index.html', context)

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

class LikeVideo(View):

  def post(self, request, *args, **kwargs):

    if request.is_ajax:

      like = json.loads(request.body.decode())['like']
      like_type = json.loads(request.body.decode())['like_type']

      video = Video.objects.get(uuid=kwargs['video'])
      
      if like_type == "like":
        video.likes = F('likes') + like
      else:
        video.dislikes = F('dislikes') + like

      video.save()

      return JsonResponse({'like': like})