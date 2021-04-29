from django.contrib import admin

from .models import Video, Comment

class VideoAdmin(admin.ModelAdmin):
  fields = ('title', 'description', 'topics', 'author', 'video')

class CommentAdmin(admin.ModelAdmin):
  pass

admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)
