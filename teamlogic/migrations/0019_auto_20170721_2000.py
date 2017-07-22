# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-21 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamlogic', '0018_auto_20170721_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchpair',
            name='first_penalty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='matchpair',
            name='is_penalty',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='matchpair',
            name='second_penalty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
