# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 04:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0011_auto_20180102_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=38)),
                ('user_one', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_one', to=settings.AUTH_USER_MODEL)),
                ('user_two', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_two', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('conversation', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.Conversation')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
