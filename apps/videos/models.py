import uuid
import re

from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Video(models.Model):
  title = models.CharField(max_length=128)
  description = models.TextField(max_length=2000)
  date = models.DateTimeField(auto_now_add=True)
  topics = models.CharField(max_length=128)
  likes = models.IntegerField(default=0)
  dislikes = models.IntegerField(default=0)
  views = models.IntegerField(default=0)
  author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='videos')
  video = models.FileField(upload_to="%Y/%m/%d",
                           validators=[FileExtensionValidator(allowed_extensions=['mp4', 'wmv', 'ogg', 'mov'])])
  uuid = models.UUIDField(default=uuid.uuid4, unique=True)

  def is_recently_uploaded(self):
    return self.date >= (timezone.now() - timezone.timedelta(days=7))
  
  def __str__(self):
    return self.title

@receiver(pre_save, sender=Video)
def set_mp4(sender, instance, **kwargs):

  extension = re.search(r'.\w+$', instance.video.name)
  new_filename = instance.video.name.replace(extension.group(), '.mp4')
  instance.video.name = new_filename
  

class Comment(models.Model):
  author = models.ForeignKey(User, on_delete=models.PROTECT)
  video = models.ForeignKey(Video, on_delete=models.CASCADE)
  body = models.TextField(max_length=1500)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.author.username

