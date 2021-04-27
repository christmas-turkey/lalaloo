from django.contrib import admin

from .models import Video

class VideoAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}

admin.site.register(Video, VideoAdmin)
