from django.utils import timezone
from django.conf import settings
from django.test import TestCase
from ..models import Paste, Report
import datetime


class PasteModelTests(TestCase):
    def test_edited_neg_tolerance_same_date(self):
        now = timezone.now()
        p = Paste(created_on=now, edited_on=now)
        settings.NPB_EDIT_TOLERANCE = -1
        self.assertIs(p.edited(), True)

    def test_edited_neg_tolerance_new_date_under(self):
        now = timezone.now()
        p = Paste(
            created_on=now,
            edited_on=now + datetime.timedelta(seconds=-360)
        )
        settings.NPB_EDIT_TOLERANCE = -5
        self.assertIs(p.edited(), True)

    def test_edited_neg_tolerance_new_date_above(self):
        now = timezone.now()
        p = Paste(
            created_on=now,
            edited_on=now + datetime.timedelta(seconds=360)
        )
        settings.NPB_EDIT_TOLERANCE = -5
        self.assertIs(p.edited(), True)

    def test_edited_pos_tolerance_same_date(self):
        now = timezone.now()
        p = Paste(created_on=now, edited_on=now)
        settings.NPB_EDIT_TOLERANCE = 1
        self.assertIs(p.edited(), False)

    def test_edited_pos_tolerance_new_date_under(self):
        now = timezone.now()
        p = Paste(
            created_on=now,
            edited_on=now + datetime.timedelta(seconds=360)
        )
        settings.NPB_EDIT_TOLERANCE = 361
        self.assertIs(p.edited(), False)

    def test_edited_pos_tolerance_new_date_above(self):
        now = timezone.now()
        p = Paste(
            created_on=now,
            edited_on=now + datetime.timedelta(seconds=360)
        )
        settings.NPB_EDIT_TOLERANCE = 256
        self.assertIs(p.edited(), True)

    def test_edited_pos_tolerance_new_date_equal(self):
        now = timezone.now()
        p = Paste(
            created_on=now,
            edited_on=now + datetime.timedelta(seconds=360)
        )
        settings.NPB_EDIT_TOLERANCE = 360
        self.assertIs(p.edited(), False)
