# Generated by Django 2.0 on 2018-05-22 07:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tdd', '0004_auto_20180522_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='semver',
            name='patch',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]