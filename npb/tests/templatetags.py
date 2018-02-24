from django.utils import timezone
from django.conf import settings
from django.test import TestCase
from ..templatetags import recent_pastes
import datetime


class RecentPastesTemplateTagTest(TestCase):
    def test_recent_pastes_activated_neg(self):
        settings.NPB_PASTES_LIST_MAX = -1
        self.assertIs(recent_pastes.recent_pastes_activated(), False)

    def test_recent_pastes_activated_zero(self):
        settings.NPB_PASTES_LIST_MAX = 0
        self.assertIs(recent_pastes.recent_pastes_activated(), False)

    def test_recent_pastes_activated_pos(self):
        settings.NPB_PASTES_LIST_MAX = 1
        self.assertIs(recent_pastes.recent_pastes_activated(), True)
