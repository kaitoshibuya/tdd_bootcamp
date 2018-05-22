from django.test import TestCase
from app_tdd.models import Semver
from app_tdd.forms import SemverForm

# Create your tests here.

class SemverModelTest(TestCase):

    def test_real_number_of_major_field(self):
        """実数値が入力された場合、オブジェクトが生成できない"""
        form = SemverForm({"major":1.1})
        self.assertFalse(form.is_valid())

    def test_minus_of_major_field(self):
        """負の値が入力された場合、オブジェクトが生成できない"""
        form = SemverForm({"major":-1})
        self.assertFalse(form.is_valid())

    def test_type_of_major_field(self):
        """int型が入力されると生成される"""
        sember = Semver(major=1)
        major = sember.major
        self.assertEqual(type(int()), type(major))


