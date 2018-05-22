from django.test import TestCase
from app_tdd.models import Semver
from app_tdd.forms import SemverForm

# Create your tests here.

class SemverModelTest(TestCase):

    """major"""
    def test_type_of_major_field(self):
        """[major]int型が入力されると生成される"""
        semver = Semver(major=1)
        self.assertEqual(type(int()), type(semver.major))

    def test_real_number_of_major_field(self):
        """[major]実数値が入力された場合、オブジェクトが生成できない"""
        form = SemverForm({"major":1.1})
        self.assertFalse(form.is_valid())

    def test_minus_of_major_field(self):
        """[major]負の値が入力された場合、オブジェクトが生成できない"""
        form = SemverForm({"major":-1})
        self.assertFalse(form.is_valid())


    """minor"""
    def test_type_of_minor_field(self):
        """[minor]int型が入力されると生成される"""
        semver = Semver(minor=1)
        self.assertEqual(type(int()), type(semver.minor))

    def test_real_number_of_minor_field(self):
        """[minor]実数値が入力された場合、オブジェクトが生成できない"""
        form = SemverForm({"minor":1.1})
        self.assertFalse(form.is_valid())

    def test_minus_of_minor_field(self):
        """[minor]負の値が入力された場合、オブジェクトが生成できない"""
        form = SemverForm({"minor":-1})
        self.assertFalse(form.is_valid())

    """patch"""
    def test_type_of_patch_field(self):
        """[patch]int型が入力されると生成される"""
        semver = Semver(patch=1)
        self.assertEqual(type(int()), type(semver.patch))

    def test_real_number_of_patch_field(self):
        """[patch]実数値が入力された場合、オブジェクトが生成できない"""
        form = SemverForm({"patch":1.1})
        self.assertFalse(form.is_valid())

    def test_minus_of_patch_field(self):
        """[patch]負の値が入力された場合、オブジェクトが生成できない"""
        form = SemverForm({"patch":-1})
        self.assertFalse(form.is_valid())
