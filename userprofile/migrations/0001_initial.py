# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GMapLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200, blank=True)),
                ('locality', models.CharField(max_length=40, blank=True)),
                ('district', models.CharField(max_length=40, blank=True)),
                ('state', models.CharField(max_length=40, blank=True)),
                ('country', models.CharField(max_length=20, blank=True)),
                ('postal_code', models.CharField(max_length=20, blank=True)),
                ('lat', models.CharField(max_length=20, blank=True)),
                ('lng', models.CharField(max_length=20, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('website', models.CharField(max_length=50, blank=True)),
                ('summary', models.TextField()),
                ('phone', models.CharField(max_length=15, blank=True)),
                ('location', models.OneToOneField(to='userprofile.GMapLocation')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfilePicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'images/', verbose_name=b'Profile Pic')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
