# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-01 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0002_authority'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='user_type',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
