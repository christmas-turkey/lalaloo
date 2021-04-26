from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Video(models.Model):
  title = models.CharField(max_length=128)
  description = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  topics = models.CharField(max_length=128)
  likes = models.IntegerField(default=0)
  dislikes = models.IntegerField(default=0)
  views = models.IntegerField(default=0)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  video = models.FileField(upload_to="%Y/%m/%d")

  def is_recently_uploaded(self):
    return self.date >= (timezone.now() - timezone.timedelta(days=7))

