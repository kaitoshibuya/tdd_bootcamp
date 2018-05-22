from app_tdd.models import Semver
from django.forms import ModelForm
from django import forms
from django.core.validators import MinValueValidator

class SemverForm(ModelForm):
    major = forms.IntegerField()
    minor = forms.IntegerField()
    patch = forms.IntegerField()

    class Meta:
        model = Semver
        fields = ["major","minor","patch"]
