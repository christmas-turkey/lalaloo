from django.db import models

class Video(models.Model):
  title = models.CharField(max_length=128)
  description = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  topics = models.CharField(max_length=128)
  likes = models.IntegerField(default=0)
  video = models.FileField(upload_to="%Y/%m/%d")
