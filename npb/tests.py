from django.utils import timezone
from django.conf import settings
from django.test import TestCase
from .models import Paste, Report
import datetime


class PasteModelTests(TestCase):
    def test_edited(self):
        now = timezone.now()
        p = Paste(created_on=now, edited_on=now)

        settings.NPB_EDIT_TOLERANCE = -1
        self.assertIs(p.edited(), True)

        settings.NPB_EDIT_TOLERANCE = 1
        self.assertIs(p.edited(), False)

        p.edited_on = now + datetime.timedelta(seconds=1)
        self.assertIs(p.edited(), False)

        p.edited_on = now + datetime.timedelta(seconds=2)
        self.assertIs(p.edited(), True)

        settings.NPB_EDIT_TOLERANCE = 10
        self.assertIs(p.edited(), False)
