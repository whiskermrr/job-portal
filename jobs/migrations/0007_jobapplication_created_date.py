# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20171230_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]