# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170719_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerprofile',
            name='profile_picture',
            field=models.ImageField(default='/home/bonzzo/testpets/static/img/caaaat.png', help_text='Maximum image size is 8MB', upload_to='pet_profiles'),
        ),
    ]
