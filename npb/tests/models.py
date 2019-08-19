from django.utils import timezone
from django.conf import settings
from django.test import TestCase
from ..models import Paste, Report, REPORT_CATEGORIES
import datetime
import uuid


class PasteModelTests(TestCase):
    def test_edited_neg_tolerance_same_date(self):
        now = timezone.now()
        p = Paste(created_on=now, edited_on=now)
        settings.NPB_EDIT_TOLERANCE = -1
        self.assertIs(p.edited(), True)

    def test_edited_neg_tolerance_new_date_under(self):
        now = timezone.now()
        p = Paste(created_on=now, edited_on=now + datetime.timedelta(seconds=-360))
        settings.NPB_EDIT_TOLERANCE = -5
        self.assertIs(p.edited(), True)

    def test_edited_neg_tolerance_new_date_above(self):
        now = timezone.now()
        p = Paste(created_on=now, edited_on=now + datetime.timedelta(seconds=360))
        settings.NPB_EDIT_TOLERANCE = -5
        self.assertIs(p.edited(), True)

    def test_edited_pos_tolerance_same_date(self):
        now = timezone.now()
        p = Paste(created_on=now, edited_on=now)
        settings.NPB_EDIT_TOLERANCE = 1
        self.assertIs(p.edited(), False)

    def test_edited_pos_tolerance_new_date_under(self):
        now = timezone.now()
        p = Paste(created_on=now, edited_on=now + datetime.timedelta(seconds=360))
        settings.NPB_EDIT_TOLERANCE = 361
        self.assertIs(p.edited(), False)

    def test_edited_pos_tolerance_new_date_above(self):
        now = timezone.now()
        p = Paste(created_on=now, edited_on=now + datetime.timedelta(seconds=360))
        settings.NPB_EDIT_TOLERANCE = 256
        self.assertIs(p.edited(), True)

    def test_edited_pos_tolerance_new_date_equal(self):
        now = timezone.now()
        p = Paste(created_on=now, edited_on=now + datetime.timedelta(seconds=360))
        settings.NPB_EDIT_TOLERANCE = 360
        self.assertIs(p.edited(), False)


class ReportModelTests(TestCase):
    def get_dummy_report(self, reason=None):
        now = timezone.now()
        p = Paste(uuid=uuid.uuid4(), created_on=now, edited_on=now)
        r = Report(
            reporter_email="derp@example.com",
            reporter_ip="::1",
            reported_on=timezone.now(),
            paste=p,
            category=REPORT_CATEGORIES[0][0],
            reason=reason or "",
        )
        return r

    def test_short_reason_under_limit(self):
        reason = "a" * 31
        r = self.get_dummy_report(reason=reason)
        self.assertEquals(len(r.short_reason()), len(reason))

    def test_short_reason_at_limit(self):
        reason = "a" * 32
        r = self.get_dummy_report(reason=reason)
        self.assertEquals(len(r.short_reason()), len(reason))

    def test_short_reason_over_limit(self):
        reason = "a" * 33
        r = self.get_dummy_report(reason=reason)
        self.assertEquals(len(r.short_reason()), 33)
        self.assertEquals(r.short_reason()[-1:], "…")

    def test_short_reason_way_over_limit(self):
        reason = "a" * 42
        r = self.get_dummy_report(reason=reason)
        self.assertEquals(len(r.short_reason()), 33)
        self.assertEquals(r.short_reason()[-1:], "…")
