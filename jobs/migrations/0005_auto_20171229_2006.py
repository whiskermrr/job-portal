# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_jobapplication_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='currentStatus',
            field=models.CharField(blank=True, choices=[('student', 'Student'), ('working - the same industry', 'Working - the same industry'), ('working - other industry', 'Working - other industry'), ('unemployed', 'Unemployed')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='education',
            field=models.CharField(blank=True, choices=[('secondary education', 'Secondary Education'), ('bachelor degree', 'Bachelor degree'), ('master degree', 'Master Degree'), ('engineer', 'Engineer'), ('other', 'Other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='industry',
            field=models.CharField(choices=[('accounting', 'Accounting'), ('factory', 'Factory'), ('banking', 'Banking'), ('marketing', 'Marketing'), ('IT - software development', 'IT - Software Development'), ('IT - administration', 'IT - Administration'), ('transport', 'Transport'), ('medical', 'Medical'), ('education', 'Education'), ('hospitality', 'Hospitality'), ('real estate', 'Real Estate'), ('production', 'Production'), ('Engineering', 'Engineering'), ('other', 'Other')], max_length=50),
        ),
    ]
