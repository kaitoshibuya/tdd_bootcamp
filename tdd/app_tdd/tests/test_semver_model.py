from django.test import TestCase
from app_tdd.models import Semver
from app_tdd.forms import SemverForm

# Create your tests here.

class SemverModelTest(TestCase):

    """major"""
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

    """minor"""
    def test_real_number_of_minor_field(self):
        """実数値が入力された場合、オブジェクトが生成できない"""
        form = SemverForm({"minor":1.1})
        self.assertFalse(form.is_valid())

    def test_minus_of_minor_field(self):
        """負の値が入力された場合、オブジェクトが生成できない"""
        form = SemverForm({"minor":-1})
        self.assertFalse(form.is_valid())

    def test_type_of_minor_field(self):
        """int型が入力されると生成される"""
        sember = Semver(major=1, minor=1)
        minor = sember.minor
        self.assertEqual(type(int()), type(minor))


