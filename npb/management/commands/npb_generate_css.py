from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from pygments.formatters import HtmlFormatter
from npb.views import _css_file_name
import os


class Command(BaseCommand):
    help = 'Generates the CSS files used by Pygments'

    def handle(self, *args, **options):
        css_class = '.%s' % getattr(settings, 'NPB_CSS_CLASS', 'highlight')
        output_dir = os.path.join(settings.BASE_DIR, 'npb/static/npb')

        os.makedirs(output_dir, mode=0o755, exist_ok=True)
        with open(os.path.join(output_dir, _css_file_name), 'w') as f:
            css = HtmlFormatter().get_style_defs(css_class)
            f.write(css)
            output_msg = self.style.SUCCESS('CSS successfully generated.')
            self.stdout.write(output_msg)
