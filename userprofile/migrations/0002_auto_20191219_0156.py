# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepicture',
            name='avatar',
            field=models.ImageField(upload_to='images/', verbose_name='Profile Pic'),
        ),
    ]
