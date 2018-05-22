from django.test import TestCase
from app_tdd.models import Semver

# Create your tests here.

class OutputStringTest(TestCase):

    def test_config_string(self):
        sember = Semver()
        version = sember.version()
        self.assertEqual("0.0.0", version)
