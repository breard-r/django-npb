from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.conf import settings
from npb.models import Paste


class Command(BaseCommand):
    help = "Purge expired and removed pastes"

    def handle(self, *args, **options):
        Paste.objects.filter(expire_on__lt=timezone.now()).delete()
        self.stdout.write(self.style.SUCCESS("Pastes purged."))
