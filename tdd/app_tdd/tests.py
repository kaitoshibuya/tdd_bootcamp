from django.test import TestCase
from .models import Semver

# Create your tests here.

class OutputString(TestCase):

    def test_config_string(self):
        sember = Semver()
        version = sember.version()
        self.assertEqual("", version)
