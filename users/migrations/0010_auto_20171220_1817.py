# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20171218_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerprofile',
            name='profile_picture',
            field=models.ImageField(default='C:\\Users\\Neuromancer/static/img/caaaat.png', help_text='Maximum image size is 8MB', upload_to='user_profiles'),
        ),
    ]
