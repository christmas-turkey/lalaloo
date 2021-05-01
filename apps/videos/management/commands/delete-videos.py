from django.core.management import BaseCommand
from videos.models import Video

class Command(BaseCommand):

  help = "Deletes all uploaded videos"

  def handle(self, *args, **options):

    videosQuantity = Video.objects.all().count()

    Video.objects.all().delete()

    self.stdout.write(self.style.SUCCESS(f'Successfully deleted {videosQuantity} videos'))