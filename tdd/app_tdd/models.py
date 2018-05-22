from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Semver(models.Model):
    major = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )
    minor = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )
    patch = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    def version(self):

        return ""
