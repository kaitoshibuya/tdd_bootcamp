from app_tdd.models import Semver
from django.forms import ModelForm
from django import forms
from django.core.validators import MinValueValidator

class SemverForm(forms.Form):
    major = forms.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )
    minor = forms.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    class Meta:
        model = Semver
